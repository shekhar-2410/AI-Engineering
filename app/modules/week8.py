"""
Week 8 — Agentic AI: The Capstone
==================================
Topics: Autonomous agents, multi-agent systems, tool orchestration,
        building a production agentic AI system.

🚧 Placeholder — implement as you progress through the course.
"""

from fastapi import APIRouter

router = APIRouter(prefix="/week8", tags=["Week 8 — Agentic AI"])


@router.get("/")
async def week8_info():
    return {
        "week": 8,
        "title": "Agentic AI — The Capstone",
        "status": "🚧 Not yet implemented",
        "topics": [
            "Day 1: What is Agentic AI? Architecture patterns",
            "Day 2: Multi-agent communication",
            "Day 3: Tool orchestration & planning",
            "Day 4: Building the capstone agent",
            "Day 5: Deployment & final project",
        ],
        "todo": "Implement endpoints after completing Week 8 lectures.",
    }
