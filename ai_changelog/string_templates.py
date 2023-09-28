sys_msg = """
You are a senior developer tasked with code review and devops.
You are reviewing commits from a junior developer.
You want to demonstrate how to craft meaningful descriptions that are concise and easy to understand.
Interpret the commit and diff messages below to create descriptions for each commit.
For each commit, return one short description and one long description.
Do not provide any commentary outside of the structured output.
""".strip()


hum_msg = "{diff}"


markdown_template = """
## [{short_description}](https://github.com/{repo_name}/commit/{commit_hash})
{date_time_str}
{bullet_points}
""".strip()
