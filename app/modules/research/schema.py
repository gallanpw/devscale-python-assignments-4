from pydantic import BaseModel, Field


class QueriesSchema(BaseModel):
    queries: list[str] = Field(
        description="List of queries generated to search for the topic"
    )


class ResearchInput(BaseModel):
    topic: str
