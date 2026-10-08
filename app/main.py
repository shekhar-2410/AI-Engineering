"""
LLM Engineering — FastAPI Server (like server.js in Express)
============================================================
This is the entry point. It:
  1. Creates the FastAPI app          (like: const app = express())
  2. Registers middleware             (like: app.use(cors(), errorHandler))
  3. Mounts all weekly module routers (like: app.use('/api/week1', week1Router))
  4. Starts with: uvicorn app.main:app --reload  (like: nodemon server.js)

Interactive API docs auto-generated at:
  http://localhost:8000/docs     (Swagger UI)
  http://localhost:8000/redoc    (ReDoc)
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.middleware.error_handler import global_exception_handler

# Import all weekly module routers
from app.modules import week1, week2, week3, week4, week5, week6, week7, week8

# ---------------------------------------------------------------------------
# Create the app (like: const app = express())
# ---------------------------------------------------------------------------
app = FastAPI(
    title="LLM Engineering — Course API",
    description=(
        "FastAPI server for the 8-week LLM Engineering course. "
        "Each week is a separate module with its own routes."
    ),
    version="1.0.0",
)

# ---------------------------------------------------------------------------
# Middleware (like: app.use(...) in Express)
# ---------------------------------------------------------------------------
# CORS — allow all origins (like cors() in Express)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global error handler
app.add_exception_handler(Exception, global_exception_handler)

# ---------------------------------------------------------------------------
# Mount routers (like: app.use('/api/week1', week1Router) in Express)
# ---------------------------------------------------------------------------
app.include_router(week1.router)
app.include_router(week2.router)
app.include_router(week3.router)
app.include_router(week4.router)
app.include_router(week5.router)
app.include_router(week6.router)
app.include_router(week7.router)
app.include_router(week8.router)


# ---------------------------------------------------------------------------
# Root route (like: app.get('/', (req, res) => { ... }) in Express)
# ---------------------------------------------------------------------------
@app.get("/", tags=["Root"])
async def root():
    """Welcome endpoint — shows server status and available modules."""
    model_info = (
        f"OpenAI ({settings.OPENAI_MODEL})"
        if settings.has_openai
        else f"Ollama ({settings.OLLAMA_MODEL})"
    )
    return {
        "message": "🚀 LLM Engineering API is running!",
        "active_model": model_info,
        "docs": "Visit /docs for interactive API documentation (Swagger UI)",
        "modules": {
            "week1": "/week1 — LLM APIs & Prompt Engineering ✅",
            "week2": "/week2 — Multi-Model & Chains 🚧",
            "week3": "/week3 — Embeddings & Vector DB 🚧",
            "week4": "/week4 — RAG Pipeline 🚧",
            "week5": "/week5 — LangChain & Agents 🚧",
            "week6": "/week6 — Fine-Tuning 🚧",
            "week7": "/week7 — Evaluation & Cost 🚧",
            "week8": "/week8 — Agentic AI 🚧",
        },
    }


@app.get("/health", tags=["Root"])
async def health():
    """Health check endpoint."""
    return {"status": "healthy", "server": "FastAPI"}
