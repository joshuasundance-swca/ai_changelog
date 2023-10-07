# AI CHANGELOG
## [Upgrade langchain dependency](https://github.com/joshuasundance-swca/ai_changelog/commit/63d56639876f067797b382c94edeeba5b1c715ba)
Thu Oct 5 13:54:40 2023 +0000
- Upgrade langchain from 0.0.305 to 0.0.308
- This includes bug fixes and new features added in 0.0.306 - 0.0.308
## [Bump version 0.0.11 -> 0.0.12](https://github.com/joshuasundance-swca/ai_changelog/commit/57c1da05f42208a57a1326bac6eaa42067c4cc5d)
Mon Oct 2 09:01:46 2023 -0400
- Bumped version number in __init__.py and pyproject.toml from 0.0.11 to 0.0.12
- Ran bumpver to update version in pyproject.toml and commit changes
## [Bump pydantic to 2.4.2](https://github.com/joshuasundance-swca/ai_changelog/commit/0fb3a28fe832c7194073270dca51597c9894e689)
Mon Oct 2 08:38:36 2023 +0000
- Upgrade pydantic dependency to version 2.4.2 for improved type hints and bug fixes.
- This includes fixes for issues with GenericModel and better support for Python 3.11.
## [Upgrade langchain dependency](https://github.com/joshuasundance-swca/ai_changelog/commit/cd7606d9f794816c90a5e582be8e56a574491e40)
Mon Oct 2 08:38:27 2023 +0000
- Upgrade langchain from 0.0.300 to 0.0.305
- This includes bug fixes and new features added in langchain 0.0.301 through 0.0.305
## [Bump openai dependency to 0.28.1](https://github.com/joshuasundance-swca/ai_changelog/commit/8e28e72c875302ba17e62b8b34da7b214970ad89)
Mon Oct 2 08:38:16 2023 +0000
- Upgrade openai package to latest patch version 0.28.1 for bug fixes and improvements.
- This includes fixes for issues with completions and embeddings.
## [Bump version 0.0.10 -> 0.0.11](https://github.com/joshuasundance-swca/ai_changelog/commit/1a15c0ebe991cbc32d5a01ab0e9ee949a2d201bf)
Thu Sep 28 14:32:58 2023 -0400
- Bump version in __init__.py
- Bump version in pyproject.toml
- Bump version via bumpver
## [Update GitHub workflow](https://github.com/joshuasundance-swca/ai_changelog/commit/2478280647ca2d5e865254b76ed0df71bf585b8d)
Thu Sep 28 14:31:19 2023 -0400
- Modify .github/workflows/ai_changelog_main_push.yml workflow to run changelog generation in parallel
- Launch OpenAI, Anthropic, and CodeLlama jobs together and wait for completion
- Remove commented-out CodeLlama job
## [Removed TODO task from README](https://github.com/joshuasundance-swca/ai_changelog/commit/a72e1649321d42f27645b6a42d50a6aebe289e97)
Thu Sep 28 18:25:40 2023 +0000
- This commit removes the task 'More robust chains for non-OpenAI LLMs' from the TODO list in the README file.
- The task may have been completed or deemed unnecessary.