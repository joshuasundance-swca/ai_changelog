# ai_changelog

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![python](https://img.shields.io/badge/Python-3.7+-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)
[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v1.json)](https://github.com/charliermarsh/ruff)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![Update AI Changelog on Push to Main](https://github.com/joshuasundance-swca/ai_changelog/actions/workflows/ai_changelog_main_push.yml/badge.svg)](https://github.com/joshuasundance-swca/ai_changelog/actions/workflows/ai_changelog_main_push.yml)

`ai_changelog` is a Python project that automatically generates changelog files summarizing code changes, using AI.

It uses [LangChain](https://github.com/langchain-ai/langchain) and [OpenAI](https://openai.com/) models to analyze Git commit diffs and generate natural language descriptions of the changes. This allows maintaining an up-to-date changelog without manual effort.

This README was originally written by Claude, an LLM from Anthropic.

## Usage

### Local install

To generate a changelog locally:

```bash
pip install -r requirements.txt
pip install ai_changelog

ai_changelog --help
ai_changelog main..HEAD  # to summarize changes locally
```

### Docker

```bash
docker pull joshuasundance/ai_changelog:latest
docker run \
    -v /local_repo_dir:/container_dir_in_repo \
    -w /container_dir_in_repo \
    joshuasundance/ai_changelog:latest \
    ai_changelog main..HEAD
```

### GitHub Workflow

The [ai_changelog_main_pr.yml](.github/workflows/ai_changelog_main_push.yml) workflow runs on pushes to `main`.

It generates summaries for the new commits and appends them to `AI_CHANGELOG.md`. The updated file is then committed back to the PR branch.

```bash
ai_changelog origin/main^..origin/main  # in a GitHub action to summarize changes in response to a push to main
ai_changelog origin/main..HEAD  # in a GitHub action to summarize changes in response to a PR
```

Another flow was made to commit an updated changelog to an incoming PR before it was merged, but that seemed less useful although it did work well.

## Configuration

- Set `OPENAI_API_KEY` in your environment to use a specific OpenAI API key.
- Set LangSmith environment variables to enable LangSmith integration, if applicable.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## TODO

- Testing
- Customization / parameterization
- Integration with LangChain Hub
- Published GitHub action(s)
