#!/usr/local/bin/python3
"""Update the AI_CHANGELOG.md file with the latest changes."""
import argparse
import os
import subprocess

from pydantic_models import Commit, CommitInfo
from utils import get_commits, get_descriptions


def main():
    """Update the AI_CHANGELOG.md file with the latest changes."""
    parser = argparse.ArgumentParser(description="Process command line arguments.")
    parser.add_argument(
        "--repo_path",
        type=str,
        default=None,
        help="Path to the repository",
    )
    parser.add_argument(
        "--before_ref",
        type=str,
        default="origin/main^",
        help="Reference point before the changes",
    )
    parser.add_argument(
        "--after_ref",
        type=str,
        default="origin/main",
        help="Reference point after the changes",
    )
    parser.add_argument(
        "--context_lines",
        type=int,
        default=5,
        help="Number of context lines for each commit",
    )

    args = parser.parse_args()

    repo_path = args.repo_path

    before_ref = args.before_ref

    after_ref = args.after_ref

    context_lines = args.context_lines

    # Check to see if AI_CHANGELOG.md already exists
    if os.path.isfile("AI_CHANGELOG.md"):
        # If so, restore the original version from main
        subprocess.call(["git", "checkout", before_ref, "--", "AI_CHANGELOG.md"])

        # Get its contents starting from the 3rd line
        with open("AI_CHANGELOG.md", "r") as existing_changelog:
            existing_content = "\n".join(existing_changelog.readlines()[2:]).strip()

    # Generate the new AI_CHANGELOG.md
    new_commits: list[Commit] = get_commits(
        repo_path=repo_path,
        before_ref=before_ref,
        after_ref=after_ref,
        context_lines=context_lines,
    )
    if new_commits:
        new_commit_infos: list[CommitInfo] = get_descriptions(new_commits)
        new_descriptions: str = CommitInfo.infos_to_str(new_commit_infos).strip()
        existing_content = existing_content.strip() if existing_content else ""

        output = f"# AI CHANGELOG\n\n{new_descriptions}\n\n{existing_content}".strip()

        # Write the output to AI_CHANGELOG.md
        with open("AI_CHANGELOG.md", "w") as new_changelog:
            new_changelog.write(output)

        # Add the file to git staging area
        subprocess.call(["git", "add", "AI_CHANGELOG.md"])


if __name__ == "__main__":
    main()
