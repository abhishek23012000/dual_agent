from crewai import Crew
from tasks.public_task import get_public_task
from tasks.private_task import get_private_task
from tasks.merge_task import get_merge_task
from agents.public_agent import public_agent
from agents.private_agent import private_agent
from agents.merge_agent import merge_agent

def run_crew(query: str):
    public_task = get_public_task(query)
    private_task = get_private_task(query)
    merge_task = get_merge_task(public_task, private_task)

    crew = Crew(
        agents=[public_agent, private_agent, merge_agent],
        tasks=[public_task, private_task, merge_task],
        process_type="sequential",
        verbose=False
    )
    result = crew.kickoff({"query": query})
    return result
