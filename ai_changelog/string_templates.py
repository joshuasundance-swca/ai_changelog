sys_msg = """
You are a senior developer tasked with code review and devops.
You are reviewing commits from a junior developer.
You want to demonstrate how to craft meaningful descriptions that are concise and easy to understand.
Interpret the commit and diff messages below to create descriptions for each commit.
"""


hum_msg = """
{commit_hash}
----------------
{diff}
"""


markdown_template = """
## [{short_description}](https://github.com/{repo_name}/commits/{commit_hash})
{bullet_points}
"""
