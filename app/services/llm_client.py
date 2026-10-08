"""
LLM Client Factory — creates the right client based on available API keys.
In Node.js terms: this is like a service that wraps SDK initialization.

Usage:
    from app.services.llm_client import get_client, get_model
    client = get_client()
    model = get_model()
"""

from openai import OpenAI
from app.config import settings


def get_client() -> OpenAI:
    """
    Returns an OpenAI client — either real OpenAI or local Ollama.
    Like creating an axios instance with a baseURL in Node.js.
    """
    if settings.has_openai:
        return OpenAI(api_key=settings.OPENAI_API_KEY)
    else:
        return OpenAI(
            base_url=settings.OLLAMA_BASE_URL,
            api_key="ollama",  # Ollama doesn't need a real key
        )


def get_model() -> str:
    """Returns the model name to use."""
    if settings.has_openai:
        return settings.OPENAI_MODEL
    return settings.OLLAMA_MODEL


def chat(
    user_message: str,
    system_message: str = "You are a helpful assistant.",
    temperature: float = 0.7,
) -> str:
    """
    One-shot chat helper. Send a message, get a response.
    This wraps the OpenAI chat completions API.
    """
    client = get_client()
    model = get_model()

    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": user_message},
        ],
        temperature=temperature,
    )
    return response.choices[0].message.content or ""
