import os
import subprocess
from typing import Optional

from langchain.chains.openai_functions import (
    create_structured_output_chain,
)
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

from pydantic_models import CommitDescription, CommitInfo, Commit
from string_templates import sys_msg, hum_msg


def get_timestamp(commit_hash: str, format: str = "%cD") -> str:
    cmd = ["git", "show", "-s", f"--format={format}", commit_hash]
    return subprocess.check_output(cmd).decode().strip()


def get_commits(
    repo_path: Optional[str] = None,
    base_ref: str = "origin/main",
    head_ref: str = "HEAD",
    context_lines: int = 5,
) -> list[Commit]:
    # Use current working directory if no repo path is provided
    repo_path = repo_path or os.getcwd()
    # Navigate to the repo path
    subprocess.check_call(["cd", repo_path], shell=True)
    # Get the list of commit hashes between base_ref and head_ref
    hashes: list[str] = (
        subprocess.check_output(
            ["git", "rev-list", "--no-merges", f"{base_ref}..{head_ref}"],
        )
        .decode()
        .splitlines()
    )
    # Get the diff for each commit in the list
    outputs: list[str] = [
        subprocess.check_output(
            [
                "git",
                "--no-pager",
                "show",
                commit,
                "-s",
                "--pretty=%cd",
                "--quiet",
                "--patch",
                f"-U{context_lines}",
            ],
        ).decode()
        for commit in hashes
    ]

    def _gen():
        for commit_hash, output in zip(hashes, outputs):
            first_linebreak = output.find("\n")
            dt = output[:first_linebreak].strip()
            diff = output[first_linebreak:].strip()
            yield Commit(
                commit_hash=commit_hash,
                date_time_str=dt,
                diff=diff,
            )

    return list(_gen())


def get_descriptions(commits: list[Commit]) -> list[CommitInfo]:
    llm = ChatOpenAI(model="gpt-4", temperature=0.5)

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", sys_msg),
            ("human", hum_msg),
            ("human", "Tip: Make sure to answer in the correct format"),
        ],
    )

    chain = create_structured_output_chain(CommitDescription, llm, prompt)

    results: list[dict] = chain.batch([commit.dict() for commit in commits])

    outputs: list[CommitDescription] = [result["function"] for result in results]

    return [
        CommitInfo(**commit.dict(), **commit_description.dict())
        for commit, commit_description in zip(commits, outputs)
    ]


def infos_to_str(infos: list[CommitInfo]) -> str:
    return "\n\n".join([info.markdown() for info in infos])
