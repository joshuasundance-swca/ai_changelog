import argparse
import os
import subprocess
from typing import Optional

from pydantic_models import Commit, CommitDescription
from utils import get_commits, get_descriptions, infos_to_str


def main(
    repo_path: Optional[str] = None,
    base_ref: str = "origin/main",
    head_ref: str = "HEAD",
    context_lines: int = 5,
):
    # Check to see if AI_CHANGELOG.md already exists
    if os.path.isfile("AI_CHANGELOG.md"):
        # If so, restore the original version from main
        subprocess.call(["git", "checkout", "origin/main", "--", "AI_CHANGELOG.md"])

        # Get its contents starting from the 3rd line
        with open("AI_CHANGELOG.md", "r") as existing_changelog:
            existing_content = "\n".join(existing_changelog.readlines()[2:]).strip()

    # Generate the new AI_CHANGELOG.md
    new_commits: list[Commit] = get_commits(
        repo_path=repo_path,
        base_ref=base_ref,
        head_ref=head_ref,
        context_lines=context_lines,
    )
    new_commit_infos: list[CommitDescription] = get_descriptions(new_commits)
    new_descriptions: str = infos_to_str(new_commit_infos).strip()

    output = f"# AI CHANGELOG\n\n{new_descriptions}\n\n{existing_content}".strip()

    # Write the output to AI_CHANGELOG.md
    with open("AI_CHANGELOG.md", "w") as new_changelog:
        new_changelog.write(output)

    # Add the file to git staging area
    subprocess.call(["git", "add", "AI_CHANGELOG.md"])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process command line arguments.")
    parser.add_argument(
        "--repo_path",
        type=str,
        default=None,
        help="Path to the repository",
    )
    parser.add_argument(
        "--base_ref",
        type=str,
        default="origin/main",
        help="Base reference for commits",
    )
    parser.add_argument(
        "--head_ref",
        type=str,
        default="HEAD",
        help="Head reference for commits",
    )
    parser.add_argument(
        "--context_lines",
        type=int,
        default=5,
        help="Number of context lines for each commit",
    )

    args = parser.parse_args()

    main(
        repo_path=args.repo_path,
        base_ref=args.base_ref,
        head_ref=args.head_ref,
        context_lines=args.context_lines,
    )
