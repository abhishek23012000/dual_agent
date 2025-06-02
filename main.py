from fastapi import FastAPI
from api.endpoints import router
import os
os.environ['GEMINI_API_KEY'] = 'AIzaSyBIyXhQ1W96bGS640s8pNYcN--sZo2Kqws'
os.environ['HF_TOKEN']='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'
app = FastAPI(title="Dual Agent Knowledge API")

app.include_router(router, prefix="/api")
