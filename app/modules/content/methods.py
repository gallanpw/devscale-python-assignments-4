# -> User Input (topic + target_audience + tone)
# -> Generate outline (headings + subheadings)
# -> Generate content per section
# -> Review & polish final content
# -> Export to PDF

import logging
from app.utils.openai import oa_client
from .schema import OutlineSchema
from .prompt import SECTION_WRITER_PROMPT, CONTENT_POLISH_PROMPT

logger = logging.getLogger(__name__)


def generate_outline(topic: str, target_audience: str, tone: str) -> OutlineSchema:
    response = oa_client.chat.completions.parse(
        model="google/gemini-3-flash-preview",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a content strategist. Generate a detailed article outline "
                    "with a title, 4-6 sections, and 2-3 subheadings per section."
                ),
            },
            {
                "role": "user",
                "content": (
                    f"Topic: {topic}\n"
                    f"Target Audience: {target_audience}\n"
                    f"Tone: {tone}"
                ),
            },
        ],
        response_format=OutlineSchema,
    )

    if not response:
        raise ValueError("No response from OpenAI")

    parsed_data = response.choices[0].message.parsed.model_dump()  # type: ignore
    logger.info(f"Generated outline: {parsed_data}")

    return OutlineSchema(**parsed_data)


def write_section(
    topic: str,
    target_audience: str,
    tone: str,
    title: str,
    heading: str,
    subheadings: list[str],
) -> str:
    response = oa_client.chat.completions.create(
        model="google/gemini-3-flash-preview",
        messages=[
            {
                "role": "system",
                "content": SECTION_WRITER_PROMPT.format(
                    topic=topic,
                    target_audience=target_audience,
                    tone=tone,
                    title=title,
                    heading=heading,
                    subheadings=", ".join(subheadings),
                ),
            },
            {"role": "user", "content": f"Write the section: {heading}"},
        ],
    )

    return response.choices[0].message.content  # type: ignore


def polish_content(topic: str, target_audience: str, tone: str, draft_content: str) -> str:
    response = oa_client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": CONTENT_POLISH_PROMPT.format(
                    topic=topic,
                    target_audience=target_audience,
                    tone=tone,
                    draft_content=draft_content,
                ),
            },
            {"role": "user", "content": "Please review and polish this article."},
        ],
        extra_body={"reasoning": {"enabled": True}},
    )

    return response.choices[0].message.content  # type: ignore
