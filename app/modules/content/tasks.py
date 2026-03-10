import uuid
from markdown import markdown
from weasyprint import HTML
from app.modules.content.methods import generate_outline, write_section, polish_content
from app.celery_app import celery_app


def content(topic: str, target_audience: str, tone: str):
    # Step 1: Generate outline
    outline = generate_outline(topic=topic, target_audience=target_audience, tone=tone)

    # Step 2: Generate content per section
    draft_content = f"# {outline.title}\n\n"
    for section in outline.sections:
        section_content = write_section(
            topic=topic,
            target_audience=target_audience,
            tone=tone,
            title=outline.title,
            heading=section.heading,
            subheadings=section.subheadings,
        )
        draft_content += section_content + "\n\n"

    # Step 3: Review & polish
    final_content = polish_content(
        topic=topic,
        target_audience=target_audience,
        tone=tone,
        draft_content=draft_content,
    )
    if not final_content:
        raise ValueError("No content generated")

    # Step 4: Export to PDF
    html_content = markdown(text=final_content, output_format="html")
    output_filename = f"output-{uuid.uuid4()}.pdf"
    HTML(string=html_content).write_pdf(output_filename)


@celery_app.task
def content_task(topic: str, target_audience: str, tone: str):
    content(topic=topic, target_audience=target_audience, tone=tone)
