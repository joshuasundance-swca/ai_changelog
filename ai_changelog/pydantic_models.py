from typing import List, Optional

from langchain.pydantic_v1 import BaseModel, Field

from string_templates import markdown_template

import os


class Commit(BaseModel):
    commit_hash: str = Field(..., description="The commit hash")
    date_time_str: str = Field(..., "Formatted date and time str")
    diff: str = Field(..., description="The diff for the commit")


class CommitDescription(BaseModel):
    short_description: str = Field(
        ...,
        description="A technical and concise description of changes implemented in the commit",
    )
    long_description: List[str] = Field(
        ...,
        description="Markdown bullet-point formatted list of changes implemented in the commit",
    )


class CommitInfo(Commit, CommitDescription):
    def markdown(self, repo_name: Optional[str] = None) -> str:
        _repo_name = repo_name or os.environ["REPO_NAME"]
        if _repo_name is None:
            raise ValueError(
                "repo_name not given and REPO_NAME not found in environment variables",
            )
        bullet_points = "\n".join(
            [f"- {line.strip('*- ')}" for line in self.long_description],
        )
        return markdown_template.format(
            short_description=self.short_description,
            commit_hash=self.commit_hash,
            bullet_points=bullet_points,
            repo_name=_repo_name,
            date_time_str=self.date_time_str,
        )
