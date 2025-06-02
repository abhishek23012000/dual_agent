from crewai import Agent
from tools.wikipedia_tool import WikipediaTool
from models.llm_config import llm

public_agent = Agent(
    role="Public Data Analyst",
    goal="Fetch and summarize public data from Wikipedia sources",
    backstory="An expert researcher trained on Wikipedia.",
    tools=[WikipediaTool()],
    llm=llm,
    verbose=True
)
