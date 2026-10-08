"""
Week 5 — LangChain & Agents
============================
Topics: LangChain framework, tools, agents, function calling.

🚧 Placeholder — implement as you progress through the course.
"""

from fastapi import APIRouter

router = APIRouter(prefix="/week5", tags=["Week 5 — LangChain & Agents"])


@router.get("/")
async def week5_info():
    return {
        "week": 5,
        "title": "LangChain & Agents",
        "status": "🚧 Not yet implemented",
        "topics": [
            "Day 1: LangChain basics — chains & prompts",
            "Day 2: Tools & function calling",
            "Day 3: Building autonomous agents",
            "Day 4: Agent memory & planning",
            "Day 5: Multi-tool agent project",
        ],
        "todo": "Implement endpoints after completing Week 5 lectures.",
    }
