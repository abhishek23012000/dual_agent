
# Dual-Agent Knowledge (CrewAI + FastAPI)

This project is a FastAPI-based web service that uses **CrewAI agents** to intelligently answer queries using both **public sources (Wikipedia)** and **private/internal documents (PDFs Quadrant)**.

The architecture is built to scale, modularize, and maintain a clean separation between logic, agents, and orchestration layers.

---

## ✨ Features

-  Dual-agent system using `CrewAI`
-  Combines public (Wikipedia) and private (internal docs) knowledge
-  Modular architecture with separate agents and tasks
-  Source traceability in answers
-  REST API powered by FastAPI

---


---

## 🔧 Setup Instructions

1. **Clone the repository**
```bash
git clone [https://github.com/your-username/dual-agent-api.git](https://github.com/abhishek23012000/dual_agent.git)
cd dual_agent
```
2. **Install dependencies**
```bash
pip install -r requirements.txt
   ```

4. **Run the FastAPI server**
```bash
  uvicorn main:app --reload
```

5. **Test the API**
```bash
http://localhost:8000/docs
```



## Architecture
![download](https://github.com/user-attachments/assets/80f6450c-a08d-447d-931d-4bbf36fafefe)

## ⚙ How It Works

### 1. Agents Setup

- **Public Agent** uses `WikipediaTool` to fetch relevant data from Wikipedia.
- **Private Agent** uses `QuadrantSearchTool` to search embedded company documents (PDF, CSV).
- **Merge Agent** takes both summaries and constructs a final, well-structured response.

---

### 2. Tasks Execution

Each agent is tied to a specific `Task`:

- `public_task`: Pulls structured summaries from public sources.
- `private_task`: Gathers relevant data from internal documents.
- `merge_task`: Synthesizes a final answer with full traceability of data sources.

---

### 3. Crew Orchestration

- All agents and tasks are bundled into a `Crew`.
- The `Crew.kickoff()` method is used to **execute tasks sequentially**:
  - First, the **Public** and **Private** tasks run to gather data.
  - Then, the **Merge** task runs to combine their outputs into one clear, cited answer.

---

### 4. API Response

The FastAPI `/api/query` endpoint returns the result in JSON format. The response includes:

-  Final synthesized answer
- Clear source citations (from both public and private data)

---

### 🧪 Example Output

```json
{
  "result": {
    "Final Answer": "Generative AI creates new content, like text or images, based on patterns in data. Large Language Models (LLMs) are a powerful form of this AI, generating human-like text, while Small Language Models (SLMs) focus on specialized tasks with less data. Retrieval-Augmented Generation (RAG) enhances these models by pulling in external information for more accurate results.",
    "📚 Sources": {
      "Public": "https://en.wikipedia.org/wiki/gen ai",
      "Private": ["internal_report.pdf (page 5)", "gen_ai.pdf"]
    }
  }
}
```
