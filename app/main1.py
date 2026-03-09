# Simple Deep Research
# -> User Input a Topic
# -> Generate sets of Queries
# -> Each query going to search to the web
# -> Summarize the results
# -> Generate Report

# import logging
# from app.methods import generate_queries, generate_report, search_web
# from markdown import markdown
# from weasyprint import HTML

# logger = logging.getLogger(__name__)


# def main():
#     topic = "Entry Level Jobs risk in AI Era"
#     research_context = ""
#     # logger.info("Starting workflow...")
#     queries = generate_queries(topic)
#     # print(queries.queries)
#     for query in queries.queries:
#         result = search_web(query)
#         research_context += f"Query: {query} \n\n Result: {result} \n\n"

#     research_result = generate_report(topic, research_context)
#     if not research_result:
#         raise ValueError("No research result generated")

#     # generate as html
#     result = markdown(research_result, output_format="html")
#     HTML(string=result).write_pdf("output-1.pdf")
#     # generate as html
#     # with open("research_context.txt", "w") as f:
#     #     f.write(research_context)


# if __name__ == "__main__":
#     main()
