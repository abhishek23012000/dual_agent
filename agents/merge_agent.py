from crewai import Agent
from models.llm_config import llm

merge_agent = Agent(
    role="Final Answer Synthesizer",
    goal="Combine public and private information into a unified, traceable answer.",
    backstory="Expert in merging multiple sources of information and clearly presenting sources.",
    llm=llm,
    verbose=True
)
