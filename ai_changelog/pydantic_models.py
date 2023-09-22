from typing import List

from langchain.pydantic_v1 import BaseModel, Field

from string_templates import markdown_template


class Commit(BaseModel):
    commit_hash: str = Field(..., description="The commit hash")
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
    def markdown(self):
        bullet_points = "\n".join(
            [f"- {line.strip('*- ')}" for line in self.long_description],
        )
        return markdown_template.format(
            short_description=self.short_description,
            commit_hash=self.commit_hash,
            bullet_points=bullet_points,
        )
