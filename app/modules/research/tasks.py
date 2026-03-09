# from time import sleep
from markdown import markdown
from weasyprint import HTML
from app.modules.research.methods import generate_queries, generate_report, search_web
from app.celery_app import celery_app


def research(topic: str):
    research_context = ""
    # logger.info("Starting workflow...")
    queries = generate_queries(topic)
    # print(queries.queries)
    for query in queries.queries:
        result = search_web(query)
        research_context += f"Query: {query} \n\n Result: {result} \n\n"

    research_result = generate_report(topic=topic, research_context=research_context)
    if not research_result:
        raise ValueError("No research result generated")

    # generate as html
    result = markdown(text=research_result, output_format="html")
    HTML(string=result).write_pdf("output-2.pdf")
    # generate as html
    # with open("research_context.txt", "w") as f:
    #     f.write(research_context)


@celery_app.task
def research_task(topic: str):
    # sleep(10)
    # print(topic)
    research(topic)
