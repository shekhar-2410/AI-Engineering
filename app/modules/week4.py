"""
Week 4 — RAG (Retrieval-Augmented Generation)
==============================================
Topics: RAG pipeline, document chunking, context injection, Q&A systems.

🚧 Placeholder — implement as you progress through the course.
"""

from fastapi import APIRouter

router = APIRouter(prefix="/week4", tags=["Week 4 — RAG Pipeline"])


@router.get("/")
async def week4_info():
    return {
        "week": 4,
        "title": "RAG — Retrieval-Augmented Generation",
        "status": "🚧 Not yet implemented",
        "topics": [
            "Day 1: What is RAG? Why do LLMs need external knowledge?",
            "Day 2: Document loading & text splitting",
            "Day 3: Building the retrieval pipeline",
            "Day 4: Combining retrieval + generation",
            "Day 5: Building a full RAG Q&A system",
        ],
        "todo": "Implement endpoints after completing Week 4 lectures.",
    }
