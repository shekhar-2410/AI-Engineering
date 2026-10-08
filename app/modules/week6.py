"""
Week 6 — Fine-Tuning LLMs
==========================
Topics: LoRA, QLoRA, Hugging Face Transformers, training on custom data.

🚧 Placeholder — implement as you progress through the course.
"""

from fastapi import APIRouter

router = APIRouter(prefix="/week6", tags=["Week 6 — Fine-Tuning"])


@router.get("/")
async def week6_info():
    return {
        "week": 6,
        "title": "Fine-Tuning LLMs",
        "status": "🚧 Not yet implemented",
        "topics": [
            "Day 1: Why fine-tune? When to use it vs prompting",
            "Day 2: Hugging Face Transformers & datasets",
            "Day 3: LoRA & QLoRA — efficient fine-tuning",
            "Day 4: Training on custom data (Google Colab)",
            "Day 5: Deploying your fine-tuned model",
        ],
        "todo": "Implement endpoints after completing Week 6 lectures.",
    }
