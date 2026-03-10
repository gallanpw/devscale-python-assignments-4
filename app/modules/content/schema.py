from pydantic import BaseModel, Field


class OutlineSection(BaseModel):
    heading: str = Field(description="Section heading")
    subheadings: list[str] = Field(description="List of subheadings under this section")


class OutlineSchema(BaseModel):
    title: str = Field(description="Article/blog post title")
    sections: list[OutlineSection] = Field(description="List of sections with subheadings")


class ContentInput(BaseModel):
    topic: str
    target_audience: str
    tone: str = "informative"
