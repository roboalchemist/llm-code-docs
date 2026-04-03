#!/usr/bin/env python3
"""
Scraper for Klaviyo developer documentation.
Output: docs/web-scraped/klaviyo/

Scrapes the documentation from developers.klaviyo.com
"""
import httpx
from pathlib import Path
import re
import html2text
from urllib.parse import urljoin, urlparse
import time

OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "web-scraped" / "klaviyo"
BASE_URL = "https://developers.klaviyo.com"

# URLs to scrape
PAGES_TO_SCRAPE = [
    "/en/docs/get_started",
    "/en/docs/sdk_overview",
    "/en/docs/create_a_test_account",
    "/en/docs/generate_sample_data",
    "/en/reference/api_overview",
]


def extract_content_from_html(html):
    """Extract the main content section from HTML."""
    # Try multiple content selectors common in README-based sites
    selectors = [
        r'<main[^>]*>(.*?)</main>',
        r'<article[^>]*>(.*?)</article>',
        r'<div class="[^"]*content[^"]*">(.*?)</div>',
    ]

    for selector in selectors:
        match = re.search(selector, html, re.DOTALL | re.IGNORECASE)
        if match:
            return match.group(1)
    return None


def html_to_markdown(html_content):
    """Convert HTML to Markdown using html2text."""
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.body_width = 0  # Don't wrap lines
    h.ignore_emphasis = False

    markdown = h.handle(html_content)

    # Clean up excessive whitespace
    markdown = re.sub(r'\n\n+', '\n\n', markdown)

    return markdown.strip()


def scrape_page(url):
    """Scrape a single page and return markdown."""
    try:
        print(f"  Fetching {url}...")
        response = httpx.get(url, timeout=15, follow_redirects=True)
        response.raise_for_status()

        # Extract main content
        content = extract_content_from_html(response.text)
        if not content:
            # If we can't extract, save the full page
            content = response.text

        # Convert to markdown
        markdown = html_to_markdown(content)

        if not markdown or len(markdown) < 50:
            print(f"    Warning: Minimal content extracted ({len(markdown)} chars)")
            return None

        print(f"    Success ({len(markdown)} chars)")
        return markdown
    except Exception as e:
        print(f"    Error: {e}")
        return None


def main():
    """Main scraper function."""
    # Create output directory
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print(f"Scraping Klaviyo developer documentation to {OUTPUT_DIR}")

    files_created = 0

    # Scrape each page
    print("\nFetching documentation pages...")
    for page_path in PAGES_TO_SCRAPE:
        full_url = urljoin(BASE_URL, page_path)
        page_name = page_path.split("/")[-1]

        content = scrape_page(full_url)
        if content:
            # Add source header
            content_with_source = f"# Source: {full_url}\n\n{content}"

            output_file = OUTPUT_DIR / f"{page_name}.md"
            output_file.write_text(content_with_source)
            files_created += 1

        # Be respectful with rate limiting
        time.sleep(0.5)

    print(f"\nDone! Documentation saved to {OUTPUT_DIR}")
    print(f"Files created: {files_created}")


if __name__ == "__main__":
    main()
