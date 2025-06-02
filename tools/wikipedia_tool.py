from crewai.tools import BaseTool
import wikipedia
from typing import Any

class WikipediaTool(BaseTool):
    name: str = "Wikipedia Search Tool"
    description: str = "Fetches public information from Wikipedia."

    def _run(self, query: str) -> dict[str, Any]:
        try:
            page = wikipedia.page(query)
            summary = wikipedia.summary(query, sentences=3)
            return {
                "answer": summary,
                "source": page.url
            }
        except Exception:
            return {
                "answer": "Wikipedia page not found.",
                "source": "Wikipedia search failed."
            }
