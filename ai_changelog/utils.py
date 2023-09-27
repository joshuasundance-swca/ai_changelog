"""Utility functions for the ai_changelog package"""

import os
import subprocess
from typing import Any, List, Union

from langchain import hub
from langchain.chains.openai_functions import (
    create_structured_output_chain,
)
from langchain.chat_models import ChatOpenAI, ChatAnthropic, ChatAnyscale
from langchain.chat_models.base import BaseChatModel
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import ChatPromptTemplate
from langchain.schema import HumanMessage
from langchain.schema.runnable import RunnableConfig

from ai_changelog.pydantic_models import CommitDescription, CommitInfo, Commit


def get_model(
    provider: str,
    model: str,
    temperature: float = 0.5,
    max_tokens: int = 1000,
) -> BaseChatModel:
    provider_model_dict = {
        "openai": ChatOpenAI,
        "anthropic": ChatAnthropic,
        "anyscale": ChatAnyscale,
    }
    try:
        model_class = provider_model_dict[provider]
    except KeyError as e:
        raise ValueError(f"Unknown provider {provider}") from e
    return model_class(model=model, temperature=temperature, max_tokens=max_tokens)


def get_prompt(
    hub_prompt_str: str = "joshuasundance/ai_changelog",
) -> ChatPromptTemplate:
    return hub.pull(hub_prompt_str)


def get_timestamp(commit_hash: str, format_str: str = "%cD") -> str:
    """Get the timestamp for a commit hash"""
    cmd = ["git", "show", "-s", f"--format={format_str}", commit_hash]
    return subprocess.check_output(cmd).decode().strip()


def rev_parse(ref: str) -> str:
    """Get the commit hash for a reference"""
    return subprocess.check_output(["git", "rev-parse", ref]).decode().strip()


def dt_diffs_from_hashes(
    hashes: List[str],
    context_lines: int = 5,
) -> List[List[str]]:
    cmd = "git --no-pager show --no-notes {commit} -s --pretty=%cd --quiet --patch -U{context_lines}"
    return [
        output.split("\n", maxsplit=1)
        for output in [
            subprocess.check_output(
                cmd.format(commit=commit, context_lines=context_lines).split(" "),
            )
            .decode()
            .strip()
            for commit in hashes
        ]
    ]


def get_commits(
    before_ref: str = "origin/main^",
    after_ref: str = "origin/main",
    context_lines: int = 5,
) -> List[Commit]:
    """Get the list of commits between two references"""
    # Get the commit hashes for BEFORE and AFTER
    before_hash = rev_parse(before_ref)
    subprocess.check_call(["git", "fetch"])
    after_hash = rev_parse(after_ref)

    # Get the list of commit hashes between before and after
    hashes: List[str] = (
        subprocess.check_output(
            ["git", "rev-list", "--no-merges", f"{before_hash}..{after_hash}"],
        )
        .decode()
        .splitlines()
    )

    dt_diffs = dt_diffs_from_hashes(hashes, context_lines=context_lines)
    dts = [dt_diff[0] for dt_diff in dt_diffs]
    diffs = [dt_diff[1] for dt_diff in dt_diffs]
    # Return a list of Commit objects
    return [
        Commit(
            commit_hash=commit_hash.strip(),
            date_time_str=date_time_str,
            diff=diff.strip(),
        )
        for commit_hash, date_time_str, diff in zip(
            hashes,
            dts,
            diffs,
        )
    ]


def get_descriptions(
    commits: List[Commit],
    provider: str,
    llm: BaseChatModel,
    prompt: ChatPromptTemplate,
    verbose: bool = True,
    max_concurrency: int = 0,
) -> List[CommitInfo]:
    """Get the descriptions for a list of commits"""
    config_dict: dict[str, Any] = {"verbose": verbose}

    if provider == "openai":
        chain = create_structured_output_chain(
            CommitDescription,
            llm,
            prompt,
        )
    else:
        parser = PydanticOutputParser(pydantic_object=CommitDescription)
        prompt = ChatPromptTemplate.from_messages(
            prompt.messages + [HumanMessage(content=parser.get_format_instructions())],
        )
        chain = prompt | llm | parser
    if max_concurrency > 0:
        config_dict["max_concurrency"] = max_concurrency

    results: List[dict] = chain.batch(
        [commit.dict() for commit in commits],
        RunnableConfig(config_dict),
    )

    outputs: List[CommitDescription] = [
        result["function"] if provider == "openai" else result for result in results
    ]

    return [
        CommitInfo(**commit.dict(), **commit_description.dict())
        for commit, commit_description in zip(commits, outputs)
    ]


def get_existing_changelog(before_ref: str) -> Union[str, None]:
    # Check to see if AI_CHANGELOG.md already exists
    if os.path.isfile("AI_CHANGELOG.md"):
        # If so, restore the original version from main
        subprocess.call(["git", "checkout", before_ref, "--", "AI_CHANGELOG.md"])

        # Get its contents starting from the second line
        with open("AI_CHANGELOG.md", "r") as existing_changelog:
            return "\n".join(
                [line.strip() for line in existing_changelog.readlines()[1:]],
            ).strip()
    return None


def update_changelog(
    before_ref: str,
    new_commits: List[Commit],
    provider: str,
    llm: BaseChatModel,
    prompt: ChatPromptTemplate,
    verbose: bool = True,
    max_concurrency: int = 0,
) -> None:
    new_commit_infos: List[CommitInfo] = get_descriptions(
        new_commits,
        provider,
        llm,
        prompt,
        verbose,
        max_concurrency,
    )
    new_descriptions: str = CommitInfo.infos_to_str(new_commit_infos).strip()
    existing_content = get_existing_changelog(before_ref) or ""

    output = f"# AI CHANGELOG\n{new_descriptions.strip()}\n{existing_content.strip()}".strip()

    # Write the output to AI_CHANGELOG.md
    with open("AI_CHANGELOG.md", "w") as new_changelog:
        new_changelog.write(output)
