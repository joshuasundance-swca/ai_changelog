import os
import subprocess
from typing import Optional, List

from langchain.chains.openai_functions import (
    create_structured_output_chain,
)
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.pydantic_v1 import BaseModel, Field


sys_msg = """
You are a senior developer tasked with code review and devops.
You are reviewing commits from a junior developer.
You want to demonstrate how to craft meaningful descriptions that are concise and easy to understand.
Interpret the commit and diff messages below to create descriptions for each commit.
"""

hum_msg = """
{commit_hash}
----------------
{diff}
"""


markdown_template = """
## {short_description}
{commit_hash}
----------------
{bullet_points}
"""


class Commit(BaseModel):
    commit_hash: str = Field(..., description="The commit hash")
    diff: str = Field(..., description="The diff for the commit")


class CommitDescription(BaseModel):
    short_description: str = Field(..., description="A technical and concise description of changes implemented in the commit")
    long_description: List[str] = Field(..., description="Markdown bullet-point formatted list of changes implemented in the commit")


class CommitInfo(Commit, CommitDescription):
    def markdown(self):
        bullet_points = "\n".join([f"- {line.strip('*- ')}" for line in self.long_description])
        return markdown_template.format(
            short_description=self.short_description,
            commit_hash=self.commit_hash,
            bullet_points=bullet_points
        )


def get_commits(
    repo_path: Optional[str] = None,
    base_ref: str = "origin/main",
    head_ref: str = "HEAD",
    context_lines: int = 5
) -> list[Commit]:
    # Use current working directory if no repo path is provided
    repo_path = repo_path or os.getcwd()
    # Navigate to the repo path
    subprocess.check_call(["cd", repo_path], shell=True)
    # Get the list of commit hashes between base_ref and head_ref
    hashes: list[str] = (
        subprocess.check_output(["git", "rev-list", f"{base_ref}..{head_ref}"])
        .decode()
        .splitlines()
    )
    # Get the diff for each commit in the list
    diffs: list[str] = [
        subprocess.check_output(
            [
                "git",
                "--no-pager",
                "show",
                commit,
                "--quiet",
                "--patch",
                f"-U{context_lines}"
            ]
        )
        .decode()
        for commit in hashes
    ]
    return [
        Commit(commit_hash=commit_hash, diff=diff)
        for commit_hash, diff in zip(hashes, diffs)
    ]


if __name__ == "__main__":
    commits = get_commits()

    llm = ChatOpenAI(model="gpt-4", temperature=0.5)

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", sys_msg),
            ("human", hum_msg),
            ("human", "Tip: Make sure to answer in the correct format"),
        ]
    )

    chain = create_structured_output_chain(CommitDescription, llm, prompt)

    results: list[dict] = chain.batch([commit.dict() for commit in commits])

    outputs: list[CommitDescription] = [result["function"] for result in results]

    infos = [
        CommitInfo(**commit.dict(), **commit_description.dict())
        for commit, commit_description in zip(commits, outputs)
    ]

    print("\n".join(info.markdown() for info in infos))
