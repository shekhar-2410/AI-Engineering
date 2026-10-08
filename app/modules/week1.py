"""
Week 1 — LLM APIs & Prompt Engineering
=======================================
Topics: OpenAI API, Ollama, system/user prompts, web scraping + summarization.

Node.js analogy:
  This file is like  routes/week1.js  with  const router = express.Router()
  Each function is a route handler.
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.services.scraper import fetch_website_contents
from app.services.llm_client import chat, get_model

router = APIRouter(prefix="/week1", tags=["Week 1 — LLM APIs & Prompts"])


# ---------------------------------------------------------------------------
# Request / Response models (like Joi schemas or TypeScript interfaces)
# ---------------------------------------------------------------------------
class SummarizeRequest(BaseModel):
    url: str


class ChatRequest(BaseModel):
    message: str
    system_prompt: str = "You are a helpful assistant."
    temperature: float = 0.7


class LLMResponse(BaseModel):
    success: bool
    model: str
    result: str


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------
@router.get("/")
async def week1_info():
    """Overview of Week 1 module."""
    return {
        "week": 1,
        "title": "LLM APIs & Prompt Engineering",
        "topics": [
            "Day 1: OpenAI API basics, first LLM call",
            "Day 2: Multi-model (Gemini, Claude, Ollama)",
            "Day 3: Prompt engineering techniques",
            "Day 4: Web scraping + AI summarization",
            "Day 5: Building a Gradio UI",
        ],
        "endpoints": [
            "POST /week1/summarize  — scrape a URL and get AI summary",
            "POST /week1/chat       — send a message to the LLM",
            "GET  /week1/health     — check which model is active",
        ],
    }


@router.get("/health")
async def health():
    """Check which LLM model is currently configured."""
    model = get_model()
    return {"status": "ok", "active_model": model}


@router.post("/summarize", response_model=LLMResponse)
async def summarize_website(req: SummarizeRequest):
    """
    Day 4 exercise: Scrape a website and generate an AI summary.
    Equivalent to: POST /api/week1/summarize { "url": "https://..." }
    """
    try:
        website_text = fetch_website_contents(req.url)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Failed to fetch URL: {e}")

    if not website_text.strip():
        raise HTTPException(status_code=400, detail="No content found at that URL.")

    system_prompt = (
        "You are a helpful executive assistant. "
        "Analyze the provided website contents and produce a clear, concise summary. "
        "Highlight: 1) The company/topic name 2) Core purpose 3) Key announcements."
    )

    result = chat(
        user_message=f"Here is the website content:\n\n{website_text}",
        system_message=system_prompt,
    )

    return LLMResponse(success=True, model=get_model(), result=result)


@router.post("/chat", response_model=LLMResponse)
async def chat_endpoint(req: ChatRequest):
    """
    Simple chat endpoint — send a message, get a response.
    Use this to experiment with different system prompts & temperatures.
    """
    result = chat(
        user_message=req.message,
        system_message=req.system_prompt,
        temperature=req.temperature,
    )
    return LLMResponse(success=True, model=get_model(), result=result)
