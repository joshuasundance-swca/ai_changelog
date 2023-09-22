# AI CHANGELOG


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
