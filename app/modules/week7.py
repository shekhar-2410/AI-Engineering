"""
Week 7 — Evaluation, Testing & Cost Optimization
=================================================
Topics: LLM evaluation metrics, A/B testing, cost tracking, guardrails.

🚧 Placeholder — implement as you progress through the course.
"""

from fastapi import APIRouter

router = APIRouter(prefix="/week7", tags=["Week 7 — Evaluation & Cost"])


@router.get("/")
async def week7_info():
    return {
        "week": 7,
        "title": "Evaluation, Testing & Cost Optimization",
        "status": "🚧 Not yet implemented",
        "topics": [
            "Day 1: How to evaluate LLM outputs",
            "Day 2: Automated testing & benchmarks",
            "Day 3: Cost tracking & optimization strategies",
            "Day 4: Guardrails & safety filters",
            "Day 5: Production-ready evaluation pipeline",
        ],
        "todo": "Implement endpoints after completing Week 7 lectures.",
    }
