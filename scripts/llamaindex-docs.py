#!/usr/bin/env python3
"""
LlamaIndex Documentation Scraper
Downloads LlamaIndex documentation from docs.llamaindex.ai (redirects to developers.llamaindex.ai)
and converts to markdown.
LlamaIndex is a data framework for LLM applications including RAG, agents, and workflows.
"""

import os
import sys
import requests
from pathlib import Path
import time
from html2text import html2text
from urllib.parse import urljoin, urlparse
import re

# Base URL for LlamaIndex documentation
# Note: docs.llamaindex.ai redirects to developers.llamaindex.ai
BASE_URL = "https://developers.llamaindex.ai"

# Key documentation sections - comprehensive coverage of Python framework
DOCS_PAGES = [
    "/",  # Main page
    "/python/cloud/",
    "/python/cloud/cookbooks/",
    "/python/cloud/general/billing/",
    "/python/cloud/llamaparse/",
    "/python/cloud/llamaparse/examples/",
    "/python/cloud/llamasheets/examples/",
    "/python/examples/embeddings/openai/",
    "/python/examples/llm/openrouter/",
    "/python/examples/retrievers/recursive_retriever_nodes/",
    "/python/examples/vector_stores/chroma_auto_retriever/",
    "/python/framework/",
    "/python/framework-api-reference/",
    "/python/framework/changelog/",
    "/python/framework/getting_started/installation/",
    "/python/framework/module_guides/",
    "/python/framework/understanding/",
    "/python/framework/use_cases/",
    "/python/framework/use_cases/extraction/",
    "/python/llamaagents/overview/",
    "/python/llamaagents/workflows/",
    "/python/llamaagents/workflows/retry_steps/",
    "/python/workflows-api-reference/",
    "/python/workflows/deployment/",
    "/python/shared/mcp/",
]

REQUEST_DELAY = 0.5  # seconds between requests
MAX_RETRIES = 3
TIMEOUT = 20


def sanitize_filename(path):
    """Convert URL path to safe filename."""
    # Remove leading/trailing slashes
    path = path.strip("/")

    # If empty, use 'index'
    if not path:
        return "index.md"

    # Replace slashes with hyphens
    safe = path.replace("/", "-")

    # Remove query parameters
    safe = safe.split("?")[0]

    # Remove fragment identifiers
    safe = safe.split("#")[0]

    # Ensure .md extension
    if not safe.endswith('.md'):
        safe = safe + '.md'

    return safe


def html_to_markdown(html_content):
    """Convert HTML content to markdown."""
    try:
        # Use html2text for conversion
        markdown = html2text(html_content)
        # Clean up excessive newlines
        markdown = re.sub(r'\n\n\n+', '\n\n', markdown)
        return markdown
    except Exception as e:
        print(f"    Warning: Could not convert HTML to markdown: {e}")
        return html_content


def extract_main_content(html_content, url):
    """Extract main documentation content from the HTML."""
    try:
        # Try to extract from main role first (most common)
        match = re.search(r'<main[^>]*>(.*?)</main>', html_content, re.DOTALL)
        if match:
            content = match.group(1)
            # Remove script and style tags
            content = re.sub(r'<script[^>]*>.*?</script>', '', content, flags=re.DOTALL)
            content = re.sub(r'<style[^>]*>.*?</style>', '', content, flags=re.DOTALL)
            return content

        # Try article tag
        match = re.search(r'<article[^>]*>(.*?)</article>', html_content, re.DOTALL)
        if match:
            content = match.group(1)
            content = re.sub(r'<script[^>]*>.*?</script>', '', content, flags=re.DOTALL)
            content = re.sub(r'<style[^>]*>.*?</style>', '', content, flags=re.DOTALL)
            return content

        # Try to find content-like classes
        match = re.search(r'<div[^>]*class="[^"]*content[^"]*"[^>]*>(.*?)</div>\s*</div>',
                         html_content, re.DOTALL)
        if match:
            return match.group(1)

        # Fallback: return body content
        match = re.search(r'<body[^>]*>(.*?)</body>', html_content, re.DOTALL)
        if match:
            return match.group(1)

        return html_content
    except Exception as e:
        print(f"    Warning: Could not extract main content: {e}")
        return html_content


def download_page(page_path, output_dir, session):
    """Download a documentation page."""
    try:
        # Build full URL
        full_url = BASE_URL + page_path

        # Sanitize filename
        filename = sanitize_filename(page_path)

        # Check if already exists to avoid re-downloading
        output_path = output_dir / filename
        if output_path.exists():
            print(f"  Skipping (exists): {filename}")
            return True

        print(f"  Downloading: {page_path}", flush=True)

        # Retry logic
        response = None
        for attempt in range(MAX_RETRIES):
            try:
                response = session.get(full_url, timeout=TIMEOUT, allow_redirects=True)
                response.raise_for_status()
                break
            except requests.exceptions.RequestException as e:
                if attempt < MAX_RETRIES - 1:
                    print(f"    Retry {attempt + 1}/{MAX_RETRIES - 1}...", flush=True)
                    time.sleep(2)
                else:
                    print(f"    -> Error: {str(e)[:80]}")
                    return False

        if response is None:
            return False

        html_content = response.text

        # Extract main content
        main_content = extract_main_content(html_content, full_url)

        # Convert to markdown
        markdown_content = html_to_markdown(main_content)

        # Add metadata header with source URL
        header = f"""# LlamaIndex Documentation

Source: {full_url}

---

"""
        content = header + markdown_content

        # Save to file
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)

        file_size = len(content.encode('utf-8'))
        print(f"    -> Saved: {filename} ({file_size:,} bytes)")
        return True

    except Exception as e:
        print(f"    -> Error processing {page_path}: {e}")
        return False


def main():
    """Main function to download LlamaIndex documentation."""
    print("=" * 70)
    print("LlamaIndex Documentation Scraper")
    print("=" * 70)
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "llms-txt" / "llamaindex"
    output_dir.mkdir(parents=True, exist_ok=True)

    # Remove old HTML file if it exists
    old_html = output_dir / "llamaindex-full.md"
    if old_html.exists():
        print(f"Removing old incomplete documentation: {old_html.name}")
        old_html.unlink()

    print(f"Output directory: {output_dir}")
    print()

    # Create a session with user agent
    session = requests.Session()
    session.headers.update({
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    })

    print(f"Downloading {len(DOCS_PAGES)} documentation pages...")
    print()

    successful = 0
    failed = 0
    failed_pages = []
    start_time = time.time()

    for idx, page_path in enumerate(DOCS_PAGES, 1):
        print(f"[{idx:2d}/{len(DOCS_PAGES)}] ", end="", flush=True)

        if download_page(page_path, output_dir, session):
            successful += 1
        else:
            failed += 1
            failed_pages.append(page_path)

        # Be respectful with rate limiting
        time.sleep(REQUEST_DELAY)

    elapsed = time.time() - start_time

    print()
    print("=" * 70)
    print("Download Summary")
    print("=" * 70)
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    print(f"Time: {elapsed:.1f} seconds")
    print(f"Output: {output_dir}")

    # Calculate statistics
    md_files = list(output_dir.glob("*.md"))
    total_files = len(md_files)
    total_size = sum(f.stat().st_size for f in md_files)

    print()
    print(f"Files downloaded: {total_files}")
    print(f"Total size: {total_size:,} bytes ({total_size/1024:.1f} KB)")

    if failed_pages and failed > 5:
        print()
        print("Failed pages (first 10):")
        for page in failed_pages[:10]:
            print(f"  - {page}")
        if len(failed_pages) > 10:
            print(f"  ... and {len(failed_pages) - 10} more")

    print()
    if failed > 0 and successful == 0:
        print(f"Error: No pages downloaded successfully")
        return 1
    elif failed > 0:
        print(f"Warning: {failed} pages failed, but {successful} pages were downloaded")
        return 0
    else:
        print("All documentation downloaded successfully!")
        return 0


if __name__ == "__main__":
    sys.exit(main())
