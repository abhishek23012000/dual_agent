from crewai import Task
from agents.private_agent import private_agent


def get_private_task(query: str):
    return Task(
        description=f"Find relevant internal information about {query} from PDF.",
        expected_output="A summary of findings from private documents with sources",
        agent=private_agent
    )
