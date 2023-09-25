#!/usr/local/bin/python3
"""Update the AI_CHANGELOG.md file with the latest changes."""
import argparse
from typing import List

from ai_changelog import Commit, get_commits, update_changelog


def main() -> None:
    """Update the AI_CHANGELOG.md file with the latest changes."""
    parser = argparse.ArgumentParser(description="Process command line arguments.")
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

    before_ref = args.before_ref

    after_ref = args.after_ref

    context_lines = args.context_lines

    # Generate the new AI_CHANGELOG.md
    new_commits: List[Commit] = get_commits(
        before_ref=before_ref,
        after_ref=after_ref,
        context_lines=context_lines,
    )

    if new_commits:
        update_changelog(before_ref=before_ref, new_commits=new_commits)


if __name__ == "__main__":
    main()
