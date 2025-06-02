from crewai import LLM
import os
import os
from dotenv import load_dotenv

load_dotenv()  # loads variables from .env into os.environ

gemini_api_key = os.getenv("GEMINI_API_KEY")
os.environ['GEMINI_API_KEY'] = gemini_api_key
# llm = LLM(
#     model="gemini/gemini-2.0-flash",
#     temperature=0.9,
# )
# llm = LLM(
#     model="huggingface/openai/whisper-large-v3"
# )
llm = LLM(
    model="ollama/phi3:3.8b-mini-4k-instruct-q2_K",
    base_url="http://localhost:11434"
)
