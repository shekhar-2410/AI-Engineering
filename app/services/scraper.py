"""
Web scraper service — fetches and extracts readable text from a URL.

Uses requests + BeautifulSoup (already in project dependencies).
"""

import requests
from bs4 import BeautifulSoup


def fetch_website_contents(url: str) -> str:
    """
    Fetch a web page and return its visible text content.

    Args:
        url: The URL to scrape.

    Returns:
        Cleaned text extracted from the page body.

    Raises:
        ValueError: If the URL is unreachable or returns a non-200 status.
    """
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0.0.0 Safari/537.36"
        )
    }

    response = requests.get(url, headers=headers, timeout=15)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    # Remove non-visible / non-content elements
    for tag in soup(["script", "style", "nav", "footer", "header", "noscript", "svg", "img"]):
        tag.decompose()

    text = soup.get_text(separator="\n", strip=True)

    # Collapse excessive blank lines
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    return "\n".join(lines)
