# ai_changelog

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![python](https://img.shields.io/badge/Python-3.7+-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org)

[![Publish to PyPI](https://github.com/joshuasundance-swca/ai_changelog/actions/workflows/publish_on_pypi.yml/badge.svg)](https://github.com/joshuasundance-swca/ai_changelog/actions/workflows/publish_on_pypi.yml)
![GitHub tag (with filter)](https://img.shields.io/github/v/tag/joshuasundance-swca/ai_changelog)

[![Push to Docker Hub](https://github.com/joshuasundance-swca/ai_changelog/actions/workflows/docker-hub.yml/badge.svg)](https://github.com/joshuasundance-swca/ai_changelog/actions/workflows/docker-hub.yml)
[![Docker Image Size (tag)](https://img.shields.io/docker/image-size/joshuasundance/ai_changelog/latest)](https://hub.docker.com/r/joshuasundance/ai_changelog)

![Code Climate maintainability](https://img.shields.io/codeclimate/maintainability/joshuasundance-swca/ai_changelog)
![Code Climate issues](https://img.shields.io/codeclimate/issues/joshuasundance-swca/ai_changelog)
![Code Climate technical debt](https://img.shields.io/codeclimate/tech-debt/joshuasundance-swca/ai_changelog)

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v1.json)](https://github.com/charliermarsh/ruff)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
![Known Vulnerabilities](https://snyk.io/test/github/joshuasundance-swca/ai_changelog/badge.svg)

[![Update AI Changelog on Push to Main](https://github.com/joshuasundance-swca/ai_changelog/actions/workflows/ai_changelog_main_push.yml/badge.svg)](https://github.com/joshuasundance-swca/ai_changelog/actions/workflows/ai_changelog_main_push.yml)

`ai_changelog` is a Python project that automatically generates changelog files summarizing code changes, using AI.

It uses [LangChain](https://github.com/langchain-ai/langchain) and [OpenAI](https://openai.com/) models to analyze Git commit diffs and generate natural language descriptions of the changes. This allows maintaining an up-to-date changelog without manual effort.

This README was originally written by Claude, an LLM from Anthropic.

## Usage

```bash
usage: ai_changelog [-h] [--provider {openai,anthropic,anyscale}] [--model MODEL] [--temperature TEMPERATURE] [--max_tokens MAX_TOKENS] [--hub_prompt HUB_PROMPT]
                    [--context_lines CONTEXT_LINES] [--max_concurrency MAX_CONCURRENCY] [-v]
                    refs

Process command line arguments.

positional arguments:
  refs                  Reference comparison with standard git syntax

options:
  -h, --help            show this help message and exit
  --provider {openai,anthropic,anyscale}
                        Model API provider
  --model MODEL         Model name
  --temperature TEMPERATURE
                        Model temperature
  --max_tokens MAX_TOKENS
                        Max tokens in output
  --hub_prompt HUB_PROMPT
                        Prompt to pull from LangChain Hub
  --context_lines CONTEXT_LINES
                        Number of context lines for each commit
  --max_concurrency MAX_CONCURRENCY
                        Number of concurrent connections to llm provider (0 means no limit)
  -v, --verbose         Run LangChain in verbose mode

http://github.com/joshuasundance-swca/ai_changelog
```

### Local install

To generate a changelog locally:

```bash
pip install ai_changelog

ai_changelog --help
ai_changelog main..HEAD  # to summarize changes locally
```

### Docker

```bash
docker pull joshuasundance/ai_changelog:latest
docker run \
    --env-file .env \
    -v /local_repo_dir:/container_dir_in_repo \
    -w /container_dir_in_repo \
    joshuasundance/ai_changelog:latest \
    main..HEAD
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

- Set environment variables as needed for your provider of choice (default requires `OPENAI_API_KEY`).
- Set LangSmith environment variables to enable LangSmith integration, if applicable.
- Use command line arguments.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## TODO

- Testing
- Get CodeLlama working reliably in CICD (currently hit or miss on structured output)
