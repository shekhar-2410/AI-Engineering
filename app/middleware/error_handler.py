"""
Global error handling middleware.
In Express:   app.use((err, req, res, next) => { ... })
In FastAPI:   @app.exception_handler(Exception)
"""

from fastapi import Request
from fastapi.responses import JSONResponse


async def global_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    """
    Catches any unhandled exception and returns a clean JSON error.
    This is registered in main.py — just like app.use(errorHandler) in Express.
    """
    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "error": str(exc),
            "path": str(request.url),
            "tip": "Check server logs for full traceback.",
        },
    )
