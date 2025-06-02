from crewai.tools import BaseTool
from core.vector_store import vector_store  # assuming this is defined somewhere

class QuadrantSearchTool(BaseTool):
    name: str = "Private Vector Search Tool"
    description: str = "Searches private documents from a Quadrant vector DB."

    def _run(self, query: str):
        print(query)
        results = vector_store.similarity_search_with_score(query=query, k=2)
        print(results)

        sources = []
        texts = []

        for res in results:
            doc = res[0]
            text = doc.page_content
            source = f"{doc.metadata.get('source', 'unknown')} (page {doc.metadata.get('page_label', '?')})"
            texts.append(text)
            sources.append(source)

        return {
            "answer": "\n\n".join(texts),
            "source": sources
        }
