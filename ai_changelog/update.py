from utils import get_commits, get_descriptions, infos_to_str


def main():
    commits = get_commits()
    infos = get_descriptions(commits)
    print(infos_to_str(infos))


if __name__ == "__main__":
    main()
