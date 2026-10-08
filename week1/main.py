"""
LLM Engineering - Week 1: Getting Started from Scratch
=====================================================
This is your minimal starting module. It demonstrates the 4 fundamental steps:
  1. Load environment variables (.env)
  2. Scrape website content
  3. Formulate system & user prompts
  4. Call the LLM (OpenAI or local Ollama)
"""

import os
from dotenv import load_dotenv
from openai import OpenAI
from scraper import fetch_website_contents

# ---------------------------------------------------------------------------
# Step 1: Load API Key from .env
# ---------------------------------------------------------------------------
# This searches for a .env file in the current directory or parent directory
load_dotenv(override=True)

api_key = os.getenv("OPENAI_API_KEY")

# Choose LLM Client:
# If you have an OpenAI key in .env, use OpenAI.
# If not, fall back to local Ollama (free local model).
if api_key:
    client = OpenAI(api_key=api_key)
    MODEL = "gpt-4o-mini"
    print(f"Using OpenAI model: {MODEL}")
else:
    # Local Ollama fallback (requires Ollama running: `ollama run llama3.2`)
    client = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")
    MODEL = "llama3.2"
    print(f"No OPENAI_API_KEY found. Defaulting to local Ollama model: {MODEL}")


# ---------------------------------------------------------------------------
# Step 2: Define System & User Prompts
# ---------------------------------------------------------------------------
# System prompt defines the persona and rules for the AI
SYSTEM_PROMPT = """You are a helpful executive assistant.
Analyze the provided website contents and produce a clear, concise summary.
Highlight:
1. The company or topic name
2. Core purpose / value proposition
3. Key announcements or bullet points
"""

def summarize_website(url: str) -> str:
    """Fetch website text and generate an AI summary."""
    print(f"\n1. Fetching website content from: {url}")
    website_text = fetch_website_contents(url)

    if not website_text.strip():
        return "Could not retrieve any content from the URL."

    print("2. Sending content to LLM...")
    user_prompt = f"Here is the website content:\n\n{website_text}"

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_prompt}
    ]

    # Step 3: Call the Chat Completion API
    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        temperature=0.7,
    )

    return response.choices[0].message.content


# ---------------------------------------------------------------------------
# Step 4: Run the script
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    # Test URL - you can change this to any website you want to analyze
    target_url = "https://edwarddonner.com"

    summary = summarize_website(target_url)

    print("\n" + "=" * 50)
    print("AI SUMMARY RESULTS:")
    print("=" * 50)
    print(summary)
