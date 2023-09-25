# AI CHANGELOG
## [Bump project version to 0.0.4](https://github.com/joshuasundance-swca/ai_changelog/commit/7b378b121c752d86cbd83afa4d46b9989bd1b122)
Mon Sep 25 17:42:00 2023 -0400
- The project's version number has been incremented from 0.0.3 to 0.0.4. This change has been reflected in the project's main __init__.py file, the pyproject.toml file, and the bumpver tool's configuration.
## [Modified GitHub Actions workflow and updated AI_CHANGELOG.md](https://github.com/joshuasundance-swca/ai_changelog/commit/93cec296e86418f26cf1df2c1c36790666145a47)
Mon Sep 25 17:41:50 2023 -0400
- In the GitHub Actions workflow, the trigger for the build job was changed. It now only runs on push events that start with 'refs/tags', instead of on all push events to the 'main' branch and any tags. The 'AI_CHANGELOG.md' file was also updated, but the changes were not specified.
## [Refactored GitHub workflows for AI Changelog and PyPi publishing](https://github.com/joshuasundance-swca/ai_changelog/commit/640d8401422e768be6c5e8abfa45f0381cde6d43)
Mon Sep 25 16:00:04 2023 -0400
- Removed the REPO_NAME environment variable from the AI Changelog workflow as it was not being used.
- Added tags trigger to the PyPi publishing workflow to ensure package publishing occurs whenever a new tag is pushed.
- Removed the condition to only publish to PyPi on tag pushes as it's now redundant with the new tags trigger.
## [Bumped up the version from 0.0.2 to 0.0.3](https://github.com/joshuasundance-swca/ai_changelog/commit/8999719b7183627be97bfdaa4e64b40a349e6518)
Mon Sep 25 15:50:27 2023 -0400
- This commit includes an update to the version number of the 'ai_changelog' project. The version number has been incremented from 0.0.2 to 0.0.3. This change has been made in the '__init__.py', 'pyproject.toml' files, and the 'tool.bumpver' section of the project.
## [Renamed environment names in GitHub actions](https://github.com/joshuasundance-swca/ai_changelog/commit/1e75f6c64f95cfe4b8d2ffe638a172e928bd6ce1)
Mon Sep 25 15:47:41 2023 -0400
- This commit changes the 'name' property of the 'environment' in the GitHub action workflows for publishing to PyPI and TestPyPI. The name 'pypi' and 'testpypi' have been replaced with 'release' in both workflows.
## [Added GitHub workflow for Python package publishing](https://github.com/joshuasundance-swca/ai_changelog/commit/dc06aeef1fa8540f8e60c5fdc140ed94c12601f7)
Mon Sep 25 15:42:42 2023 -0400
- A new GitHub workflow file has been added to automate the process of publishing the Python package to PyPI and TestPyPI. The workflow triggers on push events to the main branch, excluding changes to the 'AI_CHANGELOG.md' file.
- The workflow includes several jobs: building the distribution package, publishing the package to PyPI and TestPyPI, signing the distribution with Sigstore, and uploading the signed package to a GitHub Release.
- The building process uses Python 3.11 and the pypa/build module. The distribution packages are stored as artifacts for later jobs.
- The publishing process to PyPI only triggers on tag pushes. The publishing to TestPyPI happens regardless of the push event type.
- The signing process uses the sigstore/gh-action-sigstore-python GitHub action and the signatures are uploaded to a GitHub Release.
## [Updated the project version to 0.0.2](https://github.com/joshuasundance-swca/ai_changelog/commit/d05f7c9c14c411f81f3e9b4e157dae990eb77ff3)
Mon Sep 25 15:16:19 2023 -0400
- The version of the 'ai_changelog' project has been updated from 0.0.1 to 0.0.2. This change is reflected in the '__init__.py' file, the 'pyproject.toml' file, and the 'bumpver' tool settings.
## [Updated AI_CHANGELOG.md, __init__.py, and pyproject.toml files](https://github.com/joshuasundance-swca/ai_changelog/commit/fb81aaffc7902b4960ede066299cc73d5804066e)
Mon Sep 25 15:15:47 2023 -0400
- Updated AI_CHANGELOG.md to include a newline at the end of the file.
- Added a version variable to __init__.py in the ai_changelog module.
- Updated the pyproject.toml file to include the author's name, changed the keywords, added optional dependencies, and included bumpver tool configurations.
## [Adjusted changelog parsing start line](https://github.com/joshuasundance-swca/ai_changelog/commit/275a1b053f5cd5f8e6fa8d1787347f3950129325)
Mon Sep 25 13:23:18 2023 -0400
- Updated the line from which the AI_CHANGELOG.md file starts being read. Previously, it was starting from the 3rd line, now it starts from the 2nd line.
## [Updated GitHub Actions Workflow](https://github.com/joshuasundance-swca/ai_changelog/commit/1e52ffe64077caa49ff22719e8b35a16c54ae956)
Mon Sep 25 13:12:38 2023 -0400
- In this commit, the token used for the Checkout code step in the GitHub Actions workflow (ai_changelog_main_push.yml) was changed from GITHUB_TOKEN to PAT. Additionally, the force push option was removed from the Commit changes step.
Mon Sep 25 12:47:54 2023 -0400
- This commit introduces a README.md file for the AI Changelog project. The README provides details about the project, such as its licensing, Python version compatibility, and security measures. It also includes usage instructions for local and GitHub workflow environments, configuration tips, and a list of pending tasks.
## [Fixed argument parsing bug in ai_changelog](https://github.com/joshuasundance-swca/ai_changelog/commit/981e5d9ca2d97f43ba265dab079e9c46fd7aa9d7)
Mon Sep 25 12:17:57 2023 -0400
- This commit fixes a bug in the argument parsing section of the ai_changelog script. The bug was causing the script to fail when trying to split the 'ref' argument. The argument name has been corrected from 'ref' to 'refs'.
## [Refactored AI Changelog Script and Updated Changelog](https://github.com/joshuasundance-swca/ai_changelog/commit/a153a21df0da27dbbdd8fb4bc7bb20d79f0b6a98)
Mon Sep 25 12:17:03 2023 -0400
- The commit includes changes in three files: ai_changelog_main_push.yml, AI_CHANGELOG.md, and __main__.py in the ai_changelog directory.
- In ai_changelog_main_push.yml, the run command for the ai_changelog script was simplified to 'ai_changelog origin/main^..origin/main'.
- In AI_CHANGELOG.md, a newline character was added at the end of the file.
- In __main__.py, the argument parser in the main function was refactored. The '--before_ref' and '--after_ref' arguments were replaced with a single 'refs' argument. This argument takes a range of references in the format 'origin/main^..origin/main'. The before_ref and after_ref variables were then set by splitting the 'refs' argument.
Mon Sep 25 11:31:17 2023 -0400
- This commit introduces the MIT License to the project. The license grants permission for anyone to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the software. It also includes a disclaimer of warranty.
Mon Sep 25 14:13:28 2023 +0000
- The Pydantic library version was upgraded from 2.3.0 to 2.4.0 in the requirements.txt file.
- The langchain package version in the requirements.txt file has been updated from 0.0.298 to 0.0.300.
Mon Sep 25 10:07:01 2023 -0400
- This commit introduces several new files to the GitHub repository. It includes bug report and feature request templates, a pull request template, and a Dependabot configuration file. This will help streamline the issue reporting and feature request process, as well as ensure dependencies are kept up to date.
- Additionally, the AI Changelog workflow has been updated to use the correct parameter names for the ai_changelog command.
Sun Sep 24 00:56:46 2023 -0400
- In the get_commits function, the outputs variable was refactored into two separate variables: dts and diffs. This change improves code readability by clearly separating the date time strings and diffs for each commit.
## [Refactored CommitInfo class in pydantic_models.py](https://github.com/joshuasundance-swca/ai_changelog/commit/66ed925d62e9e0c2933ed4f31efa4eed2289a89b)
Sun Sep 24 00:43:32 2023 -0400
- Removed unnecessary comment line in CommitDescription class.
- Simplified the markdown method in the CommitInfo class by removing the optional repo_name parameter and the related error handling, instead directly using the get_repo_name method.
## [Refactored get_commits function in utils.py](https://github.com/joshuasundance-swca/ai_changelog/commit/7a2ad04177df1e1c1811f3823d8a78120cd34f3d)
Sun Sep 24 00:39:38 2023 -0400
- The get_commits function in utils.py was refactored to improve its readability and efficiency. The changes include the extraction of the dt_diffs_from_hashes function call to a separate variable 'outputs' before the return statement. This is followed by printing the 'outputs' to the console for debugging purposes. The diff attribute of the Commit object was also modified to strip any leading or trailing whitespace.
## [Refactoring and comment addition in `pydantic_models.py` and `utils.py`](https://github.com/joshuasundance-swca/ai_changelog/commit/47bedf192c67163a509856ef57e68c24732a9b82)
Sun Sep 24 00:31:46 2023 -0400
- Added a comment in `pydantic_models.py` for testing purposes.
- Refactored the `get_commits` function in `utils.py` to call `dt_diffs_from_hashes` directly in the list comprehension.
Sat Sep 23 21:17:03 2023 -0400
- This commit includes a change to the AI Changelog GitHub Actions workflow. Specifically, it adds a commit message to the 'Commit changes' step of the workflow.
Sun Sep 24 01:07:48 2023 +0000
- This commit updates the Python setup and installation steps in the GitHub workflow. The Python version is now set to 3.11, and pip cache is enabled. The step for installing dependencies is renamed to 'Install Python libraries', and a command to install the current directory as a package is added.
Sat Sep 23 20:37:34 2023 -0400
- This commit refactors the import statements in __main__.py, pydantic_models.py, and utils.py. The changes involve removing the ai_changelog prefix from the import statements, which suggests a possible restructuring of the project's directory.
Sat Sep 23 20:14:34 2023 -0400
- This commit introduces several improvements to the formatting of the AI Changelog and Python scripts.
- In the AI Changelog, leading and trailing whitespaces are now being stripped from each line. This ensures that the formatting of the commit descriptions is consistent and neat.
- In the Python scripts, the 'infos_to_str' method in the 'CommitInfo' class now joins the commit descriptions with a single newline character instead of two, reducing the amount of whitespace in the output. Furthermore, the 'get_commits' function in 'utils.py' has been updated to strip leading and trailing whitespaces from the commit hash, date_time_str, and diff.
## [Improved whitespace handling in AI_CHANGELOG.md and refactored Python scripts](https://github.com/joshuasundance-swca/ai_changelog/commit/637ee98a2b90cdb527f5dd4778d0335f5567d5d9)
Sat Sep 23 20:05:42 2023 -0400
- This commit introduces several improvements to the handling of whitespace in the AI_CHANGELOG.md file and refactors parts of the Python scripts.
- In the AI_CHANGELOG.md file, leading and trailing whitespaces are now being stripped from each line. This ensures that the formatting of the commit descriptions is consistent and neat.
- In the Python scripts, the 'infos_to_str' method in the 'CommitInfo' class now joins the commit descriptions with a single newline character instead of two, reducing the amount of whitespace in the output.
- Additionally, the 'main' function in the 'update.py' script now also strips leading and trailing whitespaces from each line of the existing content of the AI_CHANGELOG.md file. This prevents any unnecessary blank lines or spaces from appearing in the final output.
## [Added docstrings and refactored code in ai_changelog](https://github.com/joshuasundance-swca/ai_changelog/commit/1851d1db5e81c109bde4a222c52cfcd54a7e6bba)
Sat Sep 23 19:57:20 2023 -0400
- Added descriptive docstrings to classes and functions in pydantic_models.py, update.py, and utils.py for better code understanding and readability.
- Refactored the main function in update.py to handle command line arguments directly, simplifying the code structure.
- Modified get_timestamp function in utils.py to rename the 'format' parameter to 'format_str' to avoid naming conflict with the built-in Python function 'format'.
## [Added .idea to .gitignore, updated AI_CHANGELOG.md, created Dockerfile, and refactored Python scripts](https://github.com/joshuasundance-swca/ai_changelog/commit/7ea969841abf61edc54cbf3ca78c3c35390b2bd7)
Sat Sep 23 19:11:08 2023 -0400
- The .idea directory was added to the .gitignore file to ignore files generated by the JetBrains IDE.
- A newline character was added at the end of the AI_CHANGELOG.md file.
- A new Dockerfile was created with instructions to build a Docker image for a Python 3.11 Alpine application.
- The infos_to_str method was moved from the utils.py file to the pydantic_models.py file as a static method of the CommitInfo class.
- The shebang line was added to the top of the update.py file to specify the Python 3 interpreter.
- The call to the infos_to_str function in the update.py file was replaced with a call to the static method CommitInfo.infos_to_str.
## [Moved get_repo_name function from utils.py to pydantic_models.py](https://github.com/joshuasundance-swca/ai_changelog/commit/7250a98677a35700b431276f5c75fc0d17421e26)
Sat Sep 23 13:08:14 2023 -0400
- In this commit, the get_repo_name function was moved from the utils.py file to the pydantic_models.py file. This function is now a static method within the CommitInfo class. In addition, the function call in the markdown method has been updated to use the new location of the get_repo_name function.
## [Stripped extra whitespace from commit descriptions and existing content](https://github.com/joshuasundance-swca/ai_changelog/commit/37e40ab998fae03e4f54464b81a09945efd2cf10)
Sat Sep 23 12:24:52 2023 -0400
- The first commit removes any leading or trailing whitespace from the bullet points in the commit descriptions. This ensures that the formatting of the commit descriptions is consistent and neat.
- The second commit makes sure that the existing content is stripped of any leading or trailing whitespace before it is appended to the new descriptions in the AI Changelog. This prevents any unnecessary blank lines or spaces from appearing in the final output.
## [Refactored commit fetching in update script](https://github.com/joshuasundance-swca/ai_changelog/commit/4e7d92dc02a93593824d2146fd30e3da6f08d210)
Sat Sep 23 12:18:58 2023 -0400
- The commit contains changes to the AI_CHANGELOG.md, ai_changelog/update.py, and ai_changelog/utils.py files. The changes in the update.py and utils.py scripts involve refactoring how commits are fetched. The 'base_ref' and 'head_ref' parameters were renamed to 'before_ref' and 'after_ref' to better reflect their purpose. The 'before_ref' represents the state of the repository before the changes, and the 'after_ref' represents the state after the changes. The way the commits are fetched was also changed. Instead of finding the common ancestor of 'before_ref' and 'after_ref', the commit hashes for 'before_ref' and 'after_ref' are fetched directly. The changes in the AI_CHANGELOG.md file involve adding a newline at the end of the file.
## [Refactored update.py to Encapsulate Logic in main() Function](https://github.com/joshuasundance-swca/ai_changelog/commit/d12fd25f591598805658854bfdaf2dc9eb5a3fb1)
Fri Sep 22 17:58:04 2023 -0400
- The code in update.py was refactored to encapsulate the main logic within a new main() function. This change improves the readability and structure of the code. The main() function now contains the logic for checking if AI_CHANGELOG.md exists, restoring the original version if it does, reading its contents, generating the new AI_CHANGELOG.md, writing the output, and adding the file to the git staging area. The script now calls the main() function if it is run as the main module.
## [Replaced bash script with python for updating changelog](https://github.com/joshuasundance-swca/ai_changelog/commit/c21e386472d9aa04c8d73d6399e2103b83bc5357)
Fri Sep 22 17:53:25 2023 -0400
- The bash script used for updating the AI changelog has been replaced with a Python script. The Python script checks if the AI_CHANGELOG.md file exists. If it does, it restores the original version from the main branch and gets its contents starting from the 3rd line.
- The script then generates new commit descriptions and combines them with the existing content. The new content is written to AI_CHANGELOG.md and the file is added to the git staging area.
- In the GitHub workflow file, the run command has been updated to use the Python script instead of the bash script.
## [Updated Commit class field description](https://github.com/joshuasundance-swca/ai_changelog/commit/6f2e1077f88b32071a07dac5b1092b413ed61e20)
Fri Sep 22 16:00:00 2023 -0400
- The description for the 'date_time_str' field in the Commit class has been updated to improve clarity. The previous version lacked the 'description' keyword, which has now been added.
## [Added '--no-notes' option to git show command in get_commits function](https://github.com/joshuasundance-swca/ai_changelog/commit/f637f0de5bb2875872bb250b9f59d2d7607b8e0b)
Fri Sep 22 15:58:51 2023 -0400
- This commit introduces a modification to the 'get_commits' function in 'ai_changelog/utils.py'.
- Specifically, the '--no-notes' option has been added to the git show command. This option suppresses the display of notes that annotate a commit, providing a cleaner output.
## [Added date and time to commit information](https://github.com/joshuasundance-swca/ai_changelog/commit/08866a85b73efb4cd7961ed695a5264569f2f337)
Fri Sep 22 15:57:01 2023 -0400
- The commit adds a formatted date and time string to the commit information. This is achieved by modifying the Commit class in the pydantic_models.py file, adding a new attribute 'date_time_str'.
- In the string_templates.py file, the markdown template is updated to include the date and time string. The commit also simplifies the sys_msg and hum_msg templates in the same file.
- The utils.py file is updated to include a new function 'get_timestamp' that retrieves the timestamp for a given commit hash. The 'get_commits' function is also modified to include the timestamp in the commit information.
## [Fixed issue with repeating commit summaries in changelog](https://github.com/joshuasundance-swca/ai_changelog/commit/b84998fbdf949bc0daa9ac0d4f724b4406f67851)
- This commit addresses the issue of repeating commit summaries in the changelog. Previously, the script would not properly rollback the previous additions to the AI_CHANGELOG.md file, leading to an accumulation of repeated summaries.
- The fix involves changing the 'git checkout' command to specifically checkout the 'AI_CHANGELOG.md' file from the 'origin/main' branch, effectively discarding changes made in the working tree.
## [Updated AI Changelog](https://github.com/joshuasundance-swca/ai_changelog/commit/529609cb0748a803c601dee4408815a00cac8bfc)
- The commit 529609cb0748a803c601dee4408815a00cac8bfc includes several updates to the AI Changelog:
- 1) Fixed a typo in the markdown_template URL in the file ai_changelog/string_templates.py.
- 2) Introduced a hyperlink to the commit in the markdown output by modifying the markdown template in 'string_templates.py' and updating the 'markdown' method in the 'CommitInfo' class of 'pydantic_models.py'.
- 3) Added the 'REPO_NAME' environment variable in '.github/workflows/ai_changelog_main_pr.yml' to store the repository name.
- 4) Included the functionality to create hyperlinks in markdown by modifying the markdown template in the 'string_templates.py' file and adding an optional 'repo_name' parameter to the 'markdown' method in the 'CommitInfo' class.
## [Fixed typo in markdown_template string](https://github.com/joshuasundance-swca/ai_changelog/commit/ddd9ce75383893fee14132a284eec573c46a002c)
- The commit ddd9ce75383893fee14132a284eec573c46a002c by Joshua Sundance Bailey on Fri Sep 22 15:05:12 2023 is a minor fix for a typo in the 'markdown_template' string in the ai_changelog/string_templates.py file.
- The change involves correcting the GitHub URL format in the markdown template. The word 'commits' has been changed to 'commit' in the hyperlink format.
## [Added hyperlink to commit in markdown](https://github.com/joshuasundance-swca/ai_changelog/commit/eb037d5ab4211fcfb8db3a96c96dbd4359fac967)
- The commit '7e7e956c59fb42752f6f607b28427669e30c24f5' introduces a hyperlink to the commit in the markdown output. This was achieved by modifying the markdown template in 'string_templates.py' to include the repository name and commit hash in a GitHub URL format.
- To accommodate this change, the 'markdown' method in 'CommitInfo' class of 'pydantic_models.py' was updated to accept an optional 'repo_name' parameter. If 'repo_name' is not provided, the method attempts to fetch it from the environment variables.
- A new environment variable 'REPO_NAME' is added in '.github/workflows/ai_changelog_main_pr.yml' to store the repository name.
## [Added hyperlink functionality to markdown](https://github.com/joshuasundance-swca/ai_changelog/commit/7e7e956c59fb42752f6f607b28427669e30c24f5)
- The commit introduces the functionality to create hyperlinks in markdown. Changes were made to the 'ai_changelog_main_pr.yml', 'pydantic_models.py', and 'string_templates.py' files.
- In the 'ai_changelog_main_pr.yml', the REPO_NAME was added as an environment variable.
- In 'pydantic_models.py', the 'markdown' method was updated to include the 'repo_name' parameter, which defaults to the REPO_NAME environment variable if not provided. If the 'repo_name' is not provided and the REPO_NAME environment variable is not set, a ValueError is raised.
- In 'string_templates.py', the markdown template was modified to include a hyperlink to the commit in the short description.
## Added .gitignore file
7389ceff6fc1a2e81146f0215d83b58419e9cbdd
----------------
- This commit introduces a .gitignore file to the project. The .gitignore file specifies intentionally untracked files that Git should ignore. This includes various Python-related files and directories, such as .pyc files, __pycache__ directories, virtual environments (venv), and others. This helps to keep the repository clean from unnecessary files, especially those that are generated during code execution or by the development environment.
## Fixed pip install command in GitHub Actions workflow
3ac4b562ceb2b11b1edcb9d196c7086365274608
----------------
- Corrected the pip install command in the .github/workflows/ai_changelog_main_pr.yml GitHub Actions workflow file. The previous command attempted to install a package called 'requirements.txt', which is incorrect. The corrected command uses the -r flag to correctly install the packages listed in the requirements.txt file.
## Added requirements.txt
1f59a6ee1804d15af2d59eb047b178cc512ea969
----------------
- A new file named requirements.txt has been added to the project. This file contains the following Python dependencies:
- 1. langchain version 0.0.298
- 2. openai version 0.28.0
- 3. pydantic version 2.3.0
## Separated Python setup and dependency installation steps in GitHub workflow
897ac1dd8135ed3099d660d15035504c425e3d3e
----------------
- In the GitHub workflow file 'ai_changelog_main_pr.yml', the Python setup and dependency installation steps were previously combined. This commit separates these two steps into individual actions. The Python setup now uses the 'actions/setup-python@v4' action with Python version 3.11 and pip caching. The installation of dependencies is now a separate step, which runs 'pip install --user requirements.txt'.
## Refactored Python setup in GitHub workflow and updated import statements in Python scripts
5df12c7f15ffeea1447734a3354dbc37bdb31df9
----------------
- Updated Python setup in GitHub workflow to use version 4 of the setup-python action and added pip cache. Also, changed the installation of dependencies to use a requirements file instead of installing packages individually.
- Removed unnecessary __init__.py file from ai_changelog directory.
- Refactored import statements in pydantic_models.py, update.py, and utils.py to import from local directories instead of ai_changelog.
- Wrapped main execution block in update.py within a main() function.
## Fixed script execution command
b88f695bf2f58c70e828077830fb4365aacff32e
----------------
- Updated the command to execute the 'update_changelog.sh' script in the GitHub workflow file 'ai_changelog_main_pr.yml'.
- The script is now being run with '/bin/bash' to ensure the correct shell environment.
## Refactored AI Changelog Update Process
ff7719e90b74122f6d326b5a4c1ff070fdcc698f
----------------
- This commit refactors the AI changelog update process. Previously, the update process was directly embedded in the Github Action workflow file (ai_changelog_main_pr.yml). This commit moves the update process into a separate shell script (update_changelog.sh) to improve code organization and readability.
## Installation and implementation of pre-commit hooks
baa19fd17f49932c007e76fecf0dcda90e986283
----------------
- This commit introduces the installation and running of pre-commit hooks to ensure code quality before commits are pushed. The hooks include checks for syntax errors, merge conflicts, trailing whitespaces, and more.
- The commit also includes minor modifications to the ai_changelog_main_pr.yml, AI_CHANGELOG.md, pydantic_models.py, and utils.py files. These changes mainly involve formatting adjustments and do not impact the functionality of the code.
## Updated GitHub action to call the update script from new location
2d28faafa321b4a3b38fff09d54e2d7025034d1c
----------------
- This commit updates the GitHub action workflow to call the update script from its new location. Previously, the script was called directly from the root directory. Now, it's located inside the 'ai_changelog' directory.
## Refactor main function to new file and rename ai_changelog.py to utils.py
bad72996e057ae700e957f00a5a8dddd9827dfd7
----------------
- The main function that was previously in ai_changelog.py has been moved to a new file called update.py. This helps in organizing the codebase and separating concerns.
- The ai_changelog.py file has been renamed to utils.py, indicating that this file is now primarily used for utility functions like get_commits, get_descriptions, and infos_to_str.
## Refactored main script into separate functions
610f994f9aeb242b76e9bfc0966079c96670a797
----------------
- This commit refactors the main script in 'ai_changelog.py' by splitting the main execution block into separate functions. This change improves the modularity and readability of the code.
- The 'get_commits' function was already present. Two new functions were added: 'get_descriptions' and 'infos_to_str'.
- 'get_descriptions' takes a list of commits as input and returns a list of 'CommitInfo' objects, which contain both the original commit and its generated description.
- 'infos_to_str' takes a list of 'CommitInfo' objects and returns a formatted string representation of these objects, ready for printing.
- The main execution block now simply calls these functions in sequence and prints the final string.
## Moved ai_changelog.py to a new directory
1cd076994b323ffb646df8428d2a7ad241be9d27
----------------
- The ai_changelog.py file was moved from the root directory to a new subdirectory named ai_changelog. This change does not affect the functionality of the file but helps in organizing the codebase.
## Refactored code by moving Pydantic models to a separate file
87294d34d1112c45376f6e8ae334208bf2c19e8b
----------------
- Moved the Pydantic models 'Commit', 'CommitDescription', and 'CommitInfo' from 'ai_changelog.py' to a new file named 'ai_changelog/pydantic_models.py'.
- This change helps to keep the codebase organized and improves the readability of the 'ai_changelog.py' file by reducing its length and complexity.
## Refactored string templates to a separate file
5f9ac629d38703cc640456ac2474e5aef95aafcc
----------------
- The commit involves moving the string templates (sys_msg, hum_msg, markdown_template) used in the ai_changelog.py file to a separate file named string_templates.py within the same directory.
- This change helps in improving the code organization and readability by separating the string templates from the main logic of the program.
- The ai_changelog.py file was updated to import the string templates from the new location.
## Creation of ai_changelog/__init__.py
b8b3377a6f0016108c8860d28fa23ef0098e4418
----------------
- This commit introduces a new file, ai_changelog/__init__.py. The file does not contain any code yet as it is an initialization file.
## Removed hello_world.py
b79d5c378120eabad7062cbad29dc0e1e9b6b2b1
----------------
- This commit deletes the file hello_world.py from the repository. The file previously contained a simple script for printing a 'Hello, world!' message and testing the bot's ability to generate commit messages from diffs.
## Added additional print statements to hello_world.py
a4273faacb57222dfcec6f3446efc2f12bf40fc5
----------------
- The commit adds two new print statements to the 'hello_world.py' script. These messages provide more information about the purpose of the script and how the diff is generated.
## Added hello_world.py
0fdc81b6b26fe9c8d3dfed936e8c692f369119a7
----------------
- This commit introduces a new Python file named 'hello_world.py'.
- The file contains a simple script that prints 'Hello, world!' when run.