
# Dual-Agent Knowledge API (CrewAI + FastAPI)

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
cd dual-agent-api
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




   



