from crewai import Task
from agents.public_agent import public_agent

def get_public_task(query: str):
    return Task(
        description=f"Find public information about {query} using Wikipedia.",
        expected_output="A short, well-cited summary of public information. with sources",
        agent=public_agent,
          async_execution=True,
    )
