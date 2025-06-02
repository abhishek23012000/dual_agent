from crewai import Task
from agents.merge_agent import merge_agent

def get_merge_task(public_task, private_task):
    return Task(
        description=(
            "You will receive context of the prevoius task.\n"
            "Combine them into a single clear answer.\n"
            "Then list the sources under a section called '📚 Sources'.\n"
            "Structure:\n"
            "1. Final Answer\n"
            "2. Sources\n"
            "- Public: <url>\n"
            "- Private: <doc names, pages>\n"
        ),
        expected_output="Merged response with clear answer and sources section",
        context=[private_task, public_task],
        agent=merge_agent
    )
