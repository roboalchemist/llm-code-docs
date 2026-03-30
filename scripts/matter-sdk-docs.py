#!/usr/bin/env python3
"""
Scraper for Matter SDK (connectedhomeip) documentation.
Output: docs/web-scraped/matter-sdk/

Scrapes the Sphinx-built docs site at:
https://project-chip.github.io/connectedhomeip-doc/

Replaces the github-scraped version with proper rendered HTML content.
"""

import re
import sys
import time
from pathlib import Path
from urllib.parse import urljoin, urlparse

import html2text
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://project-chip.github.io/connectedhomeip-doc/"
OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "web-scraped" / "matter-sdk"

# Pages to skip (non-content pages)
SKIP_PATTERNS = [
    "genindex.html",
    "search.html",
    "_modules/",
    "_sources/",
    "_static/",
    "_images/",
]

# Rate limit between requests (seconds)
REQUEST_DELAY = 0.3


def should_skip(url: str) -> bool:
    """Return True if this URL should be skipped."""
    path = urlparse(url).path
    return any(pattern in path for pattern in SKIP_PATTERNS)


def url_to_filename(url: str) -> str:
    """Convert a page URL to an output filename.

    e.g. getting_started/first_example.html -> getting_started-first_example.html.md
         GLOSSARY.html -> GLOSSARY.html.md
         index.html -> index.html.md
    """
    parsed = urlparse(url)
    # Get path relative to the base path
    base_path = urlparse(BASE_URL).path  # /connectedhomeip-doc/
    rel_path = parsed.path
    if rel_path.startswith(base_path):
        rel_path = rel_path[len(base_path):]

    # Remove leading slash
    rel_path = rel_path.lstrip("/")

    # Handle root index page
    if not rel_path or rel_path == "index.html":
        return "index.html.md"

    # Replace path separators with dashes
    filename = rel_path.replace("/", "-")

    # Append .md
    return filename + ".md"


def extract_content(html: str) -> str | None:
    """Extract the main article content from a Sphinx/PyData page."""
    soup = BeautifulSoup(html, "html.parser")

    # PyData Sphinx theme uses bd-article-container or bd-article
    content = soup.find(class_="bd-article-container")
    if not content:
        content = soup.find("article", class_="bd-article")
    if not content:
        content = soup.find(class_="bd-content")
    if not content:
        # Fallback: try standard Sphinx content div
        content = soup.find("div", role="main")
    if not content:
        content = soup.find("article")

    if not content:
        return None

    # Remove elements that are navigation/chrome, not content
    for el in content.find_all(["nav", "footer"]):
        el.decompose()
    # Remove header bar with edit/download buttons (d-print-none = UI chrome)
    # Note: BeautifulSoup passes each individual class string to the lambda
    for el in content.find_all(class_=lambda c: c and "d-print-none" in c):
        el.decompose()
    for el in content.find_all(class_=lambda c: c and any(
        x in c for x in [
            "bd-toc", "page-toc", "prev-next", "breadcrumb",
            "header-article", "bd-header-article", "headerlink",
            "sphinx-tabs-tab", "btn-source-edit", "article-header",
        ]
    )):
        el.decompose()

    return str(content)


def html_to_markdown(html_content: str) -> str:
    """Convert HTML to clean Markdown using html2text."""
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.body_width = 0  # No line wrapping
    h.ignore_images = True
    h.protect_links = False
    h.unicode_snob = True

    md = h.handle(html_content)

    # Clean up excessive blank lines
    md = re.sub(r"\n{3,}", "\n\n", md)

    return md.strip()


def scrape_page(url: str) -> str | None:
    """Fetch a page and return its markdown content, or None on failure."""
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"    ERROR fetching {url}: {e}")
        return None

    content_html = extract_content(response.text)
    if not content_html:
        print(f"    WARNING: no content found at {url}")
        return None

    md = html_to_markdown(content_html)
    if not md or len(md.strip()) < 30:
        print(f"    WARNING: content too short at {url}")
        return None

    return md


def collect_all_links(index_url: str) -> list[str]:
    """Fetch the index page and collect all internal .html links."""
    try:
        response = requests.get(index_url, timeout=15)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"ERROR fetching index: {e}")
        sys.exit(1)

    soup = BeautifulSoup(response.text, "html.parser")
    links = set()

    for a in soup.find_all("a", href=True):
        href = a["href"]
        # Skip anchors and external links
        if href.startswith("#") or href.startswith("http"):
            continue
        # Build absolute URL
        full_url = urljoin(index_url, href)
        # Strip fragment
        full_url = full_url.split("#")[0]
        # Must be on the same site and end in .html
        if not full_url.startswith(BASE_URL):
            continue
        if not full_url.endswith(".html"):
            continue
        if should_skip(full_url):
            continue
        links.add(full_url)

    # Always include the index itself
    links.add(index_url)

    return sorted(links)


def main():
    """Main scraper entry point."""
    print("=" * 65)
    print("Matter SDK Documentation Scraper")
    print(f"Source: {BASE_URL}")
    print(f"Output: {OUTPUT_DIR}")
    print("=" * 65)

    # Create output directory
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Collect all page URLs from the index
    print("\nCollecting page links from index...")
    all_links = collect_all_links(BASE_URL)
    print(f"Found {len(all_links)} pages to scrape")

    scraped = 0
    failed = 0

    for i, url in enumerate(all_links, 1):
        filename = url_to_filename(url)
        output_path = OUTPUT_DIR / filename

        print(f"  [{i:3d}/{len(all_links)}] {url.replace(BASE_URL, '')} -> {filename}")

        md = scrape_page(url)
        if md:
            # Write with source header on line 1
            content = f"# Source: {url}\n\n{md}"
            output_path.write_text(content, encoding="utf-8")
            scraped += 1
        else:
            failed += 1

        # Rate limit
        if i < len(all_links):
            time.sleep(REQUEST_DELAY)

    print()
    print("=" * 65)
    print(f"Done!")
    print(f"  Scraped:  {scraped}")
    print(f"  Failed:   {failed}")
    total_size = sum(f.stat().st_size for f in OUTPUT_DIR.glob("*.md"))
    print(f"  Size:     {total_size / 1024:.1f} KB")
    print(f"  Output:   {OUTPUT_DIR}")
    print("=" * 65)


if __name__ == "__main__":
    main()
