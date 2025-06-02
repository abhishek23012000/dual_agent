from crewai import Agent

from tools.quadrant_tool import QuadrantSearchTool
from models.llm_config import llm

private_agent = Agent(
    role="Private Data Agent",
    goal="Search internal company documents to find relevant answers",
    backstory="Knows how to work with internal PDFs and CSVs embedded in Quadrant.",
    tools=[QuadrantSearchTool()],
    llm=llm,
    verbose=True
)
