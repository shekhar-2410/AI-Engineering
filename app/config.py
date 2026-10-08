"""
Configuration module — loads .env and exposes settings.
Think of this like: config/index.js in Node.js
"""

import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env from project root (2 levels up from app/config.py)
_env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(_env_path, override=True)


class Settings:
    """
    Central settings object — similar to how you'd export a config object in Node.
    Usage:  from app.config import settings
            settings.OPENAI_API_KEY
    """

    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    GOOGLE_API_KEY: str = os.getenv("GOOGLE_API_KEY", "")
    ANTHROPIC_API_KEY: str = os.getenv("ANTHROPIC_API_KEY", "")
    HF_TOKEN: str = os.getenv("HF_TOKEN", "")

    # Default models
    OPENAI_MODEL: str = "gpt-4o-mini"
    OLLAMA_MODEL: str = "llama3.2"
    OLLAMA_BASE_URL: str = "http://localhost:11434/v1"

    @property
    def has_openai(self) -> bool:
        return bool(self.OPENAI_API_KEY and self.OPENAI_API_KEY.strip())


settings = Settings()
