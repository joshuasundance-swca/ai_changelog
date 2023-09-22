import os
import subprocess

from pydantic_models import Commit, CommitDescription
from utils import get_commits, get_descriptions, infos_to_str


def main():
    # Check to see if AI_CHANGELOG.md already exists
    if os.path.isfile("AI_CHANGELOG.md"):
        # If so, restore the original version from main
        subprocess.call(["git", "checkout", "origin/main", "--", "AI_CHANGELOG.md"])

        # Get its contents starting from the 3rd line
        with open("AI_CHANGELOG.md", "r") as existing_changelog:
            existing_content = "\n".join(existing_changelog.readlines()[2:]).strip()

    # Generate the new AI_CHANGELOG.md
    new_commits: list[Commit] = get_commits()
    new_commit_infos: list[CommitDescription] = get_descriptions(new_commits)
    new_descriptions: str = infos_to_str(new_commit_infos).strip()

    output = f"# AI CHANGELOG\n\n{new_descriptions}\n\n{existing_content}".strip()

    # Write the output to AI_CHANGELOG.md
    with open("AI_CHANGELOG.md", "w") as new_changelog:
        new_changelog.write(output)

    # Add the file to git staging area
    subprocess.call(["git", "add", "AI_CHANGELOG.md"])


if __name__ == "__main__":
    main()
