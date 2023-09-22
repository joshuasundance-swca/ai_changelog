from ai_changelog.utils import get_commits, get_descriptions, infos_to_str


if __name__ == "__main__":
    commits = get_commits()
    infos = get_descriptions(commits)
    print(infos_to_str(infos))
