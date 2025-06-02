from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from core.crew_runner import run_crew

router = APIRouter()

class QueryRequest(BaseModel):
    query: str

@router.post("/query")
def query_handler(payload: QueryRequest):
    try:
        result = run_crew(payload.query)
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
