"""
Week 2 — Multi-Model & Conversation Chains
===========================================
Topics: Comparing models (OpenAI, Gemini, Claude, Ollama),
        multi-turn conversations, streaming responses.

🚧 Placeholder — implement as you progress through the course.
"""

from fastapi import APIRouter

router = APIRouter(prefix="/week2", tags=["Week 2 — Multi-Model & Chains"])


@router.get("/")
async def week2_info():
    return {
        "week": 2,
        "title": "Multi-Model & Conversation Chains",
        "status": "🚧 Not yet implemented",
        "topics": [
            "Day 1: Comparing frontier models (GPT, Claude, Gemini)",
            "Day 2: Multi-turn conversations & memory",
            "Day 3: Streaming responses",
            "Day 4: Model routing — pick the best model per task",
            "Day 5: Building a multi-model chatbot UI",
        ],
        "todo": "Implement endpoints after completing Week 2 lectures.",
    }
