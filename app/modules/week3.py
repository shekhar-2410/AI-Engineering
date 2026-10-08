"""
Week 3 — Embeddings & Vector Databases
=======================================
Topics: Text embeddings, ChromaDB, semantic search, similarity scoring.

🚧 Placeholder — implement as you progress through the course.
"""

from fastapi import APIRouter

router = APIRouter(prefix="/week3", tags=["Week 3 — Embeddings & Vector DB"])


@router.get("/")
async def week3_info():
    return {
        "week": 3,
        "title": "Embeddings & Vector Databases",
        "status": "🚧 Not yet implemented",
        "topics": [
            "Day 1: What are embeddings? Text → vectors",
            "Day 2: ChromaDB setup & storing embeddings",
            "Day 3: Semantic search vs keyword search",
            "Day 4: Similarity scoring & nearest neighbors",
            "Day 5: Building a semantic search API",
        ],
        "todo": "Implement endpoints after completing Week 3 lectures.",
    }
