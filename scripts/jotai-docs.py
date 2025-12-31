#!/usr/bin/env python3
"""
Jotai Documentation Scraper
Downloads all Jotai documentation pages and converts to markdown.
Jotai is a primitive and flexible state management library for React.
"""

import os
import sys
import requests
from pathlib import Path
from urllib.parse import urlparse
import time
import re
import subprocess

# Jotai documentation pages from sitemap
JOTAI_DOC_PAGES = [
    # Root
    "/docs/",
    # Core
    "/docs/core/atom",
    "/docs/core/use-atom",
    "/docs/core/store",
    "/docs/core/provider",
    # Utilities
    "/docs/utilities/storage",
    "/docs/utilities/ssr",
    "/docs/utilities/async",
    "/docs/utilities/lazy",
    "/docs/utilities/resettable",
    "/docs/utilities/family",
    "/docs/utilities/callback",
    "/docs/utilities/reducer",
    "/docs/utilities/select",
    "/docs/utilities/split",
    # Extensions
    "/docs/extensions/trpc",
    "/docs/extensions/query",
    "/docs/extensions/effect",
    "/docs/extensions/urql",
    "/docs/extensions/immer",
    "/docs/extensions/xstate",
    "/docs/extensions/location",
    "/docs/extensions/cache",
    "/docs/extensions/scope",
    "/docs/extensions/optics",
    "/docs/extensions/redux",
    "/docs/extensions/relay",
    "/docs/extensions/valtio",
    "/docs/extensions/zustand",
    # Basics
    "/docs/basics/concepts",
    "/docs/basics/comparison",
    "/docs/basics/showcase",
    "/docs/basics/functional-programming-and-jotai",
    # Guides
    "/docs/guides/migrating-to-v2-api",
    "/docs/guides/typescript",
    "/docs/guides/nextjs",
    "/docs/guides/waku",
    "/docs/guides/remix",
    "/docs/guides/react-native",
    "/docs/guides/debugging",
    "/docs/guides/performance",
    "/docs/guides/testing",
    "/docs/guides/core-internals",
    "/docs/guides/composing-atoms",
    "/docs/guides/atoms-in-atom",
    "/docs/guides/initialize-atom-on-render",
    "/docs/guides/persistence",
    "/docs/guides/using-store-outside-react",
    "/docs/guides/async",
    "/docs/guides/resettable",
    "/docs/guides/vite",
    # Recipes
    "/docs/recipes/large-objects",
    "/docs/recipes/custom-useatom-hooks",
    "/docs/recipes/use-atom-effect",
    "/docs/recipes/atom-with-toggle",
    "/docs/recipes/atom-with-compare",
    "/docs/recipes/atom-with-toggle-and-storage",
    "/docs/recipes/atom-with-refresh",
    "/docs/recipes/atom-with-refresh-and-default",
    "/docs/recipes/atom-with-listeners",
    "/docs/recipes/atom-with-broadcast",
    "/docs/recipes/atom-with-debounce",
    "/docs/recipes/use-reducer-atom",
    # Tools
    "/docs/tools/swc",
    "/docs/tools/babel",
    "/docs/tools/devtools",
]

BASE_URL = "https://jotai.org"


def html_to_markdown(html_content, url):
    """Convert HTML to markdown, extracting main content only."""
    # Jotai uses Next.js with main content in <main> or <article> tags
    # Try to extract main content area
    article_match = re.search(
        r'<article[^>]*>(.*?)</article>',
        html_content, flags=re.DOTALL | re.IGNORECASE
    )

    if article_match:
        html_content = article_match.group(1)
    else:
        # Try main tag
        main_match = re.search(
            r'<main[^>]*>(.*?)</main>',
            html_content, flags=re.DOTALL | re.IGNORECASE
        )
        if main_match:
            html_content = main_match.group(1)

    # Remove navigation elements
    html_content = re.sub(r'<nav[^>]*>.*?</nav>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<aside[^>]*>.*?</aside>', '', html_content, flags=re.DOTALL | re.IGNORECASE)

    # Try pandoc on cleaned content
    try:
        result = subprocess.run(
            ['pandoc', '-f', 'html', '-t', 'markdown', '--wrap=none'],
            input=html_content,
            capture_output=True,
            text=True,
            timeout=30
        )
        if result.returncode == 0:
            markdown = result.stdout
            # Clean up pandoc artifacts
            markdown = re.sub(r'^::+.*$', '', markdown, flags=re.MULTILINE)  # Remove ::: div markers
            markdown = re.sub(r'\{[^}]*\}', '', markdown)  # Remove {.class} attributes
            markdown = re.sub(r'\n{3,}', '\n\n', markdown)  # Normalize whitespace
            markdown = markdown.strip()
            return f"# Source: {url}\n\n{markdown}"
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass

    # Fallback: basic HTML to text extraction
    # Remove script and style elements
    html_content = re.sub(r'<script[^>]*>.*?</script>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<style[^>]*>.*?</style>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<header[^>]*>.*?</header>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<footer[^>]*>.*?</footer>', '', html_content, flags=re.DOTALL | re.IGNORECASE)

    # Convert common HTML elements to markdown
    # Headers
    for i in range(6, 0, -1):
        html_content = re.sub(rf'<h{i}[^>]*>(.*?)</h{i}>', r'\n' + '#' * i + r' \1\n', html_content, flags=re.DOTALL | re.IGNORECASE)

    # Code blocks
    html_content = re.sub(r'<pre[^>]*><code[^>]*>(.*?)</code></pre>', r'\n```\n\1\n```\n', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<code[^>]*>(.*?)</code>', r'`\1`', html_content, flags=re.DOTALL | re.IGNORECASE)

    # Links
    html_content = re.sub(r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>', r'[\2](\1)', html_content, flags=re.DOTALL | re.IGNORECASE)

    # Bold and italic
    html_content = re.sub(r'<strong[^>]*>(.*?)</strong>', r'**\1**', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<b[^>]*>(.*?)</b>', r'**\1**', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<em[^>]*>(.*?)</em>', r'*\1*', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<i[^>]*>(.*?)</i>', r'*\1*', html_content, flags=re.DOTALL | re.IGNORECASE)

    # Lists
    html_content = re.sub(r'<li[^>]*>(.*?)</li>', r'- \1\n', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<[ou]l[^>]*>', '\n', html_content, flags=re.IGNORECASE)
    html_content = re.sub(r'</[ou]l>', '\n', html_content, flags=re.IGNORECASE)

    # Paragraphs and line breaks
    html_content = re.sub(r'<p[^>]*>(.*?)</p>', r'\n\1\n', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<br\s*/?>', '\n', html_content, flags=re.IGNORECASE)
    html_content = re.sub(r'<div[^>]*>', '\n', html_content, flags=re.IGNORECASE)
    html_content = re.sub(r'</div>', '\n', html_content, flags=re.IGNORECASE)

    # Remove remaining HTML tags
    html_content = re.sub(r'<[^>]+>', '', html_content)

    # Decode HTML entities
    html_content = html_content.replace('&nbsp;', ' ')
    html_content = html_content.replace('&lt;', '<')
    html_content = html_content.replace('&gt;', '>')
    html_content = html_content.replace('&amp;', '&')
    html_content = html_content.replace('&quot;', '"')
    html_content = html_content.replace('&#39;', "'")

    # Clean up whitespace
    html_content = re.sub(r'\n\s*\n\s*\n', '\n\n', html_content)
    html_content = html_content.strip()

    return f"# Source: {url}\n\n{html_content}"


def download_page(url, output_path):
    """Download a page and convert to markdown."""
    try:
        print(f"Downloading: {url}")

        response = requests.get(url, timeout=15)
        response.raise_for_status()

        # Convert HTML to markdown
        markdown = html_to_markdown(response.text, url)

        # Create directory if needed
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # Write markdown file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(markdown)

        print(f"  -> Saved: {output_path}")
        return True

    except requests.exceptions.RequestException as e:
        print(f"  -> Error downloading {url}: {e}")
        return False
    except Exception as e:
        print(f"  -> Error processing {url}: {e}")
        return False


def path_to_filename(path):
    """Convert URL path to filename."""
    if path == "/docs/" or path == "/docs":
        return "index.md"

    # Remove /docs/ prefix and leading/trailing slashes
    clean_path = path.replace("/docs/", "").strip("/")

    # Handle nested paths like /docs/core/atom -> core-atom.md
    if "/" in clean_path:
        return clean_path.replace("/", "-") + ".md"

    return clean_path + ".md"


def main():
    """Main function to download all Jotai documentation."""
    print("=" * 60)
    print("Jotai Documentation Scraper")
    print("=" * 60)
    print(f"Base URL: {BASE_URL}")
    print(f"Pages to download: {len(JOTAI_DOC_PAGES)}")
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "web-scraped" / "jotai"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Output directory: {output_dir}")
    print()

    successful = 0
    failed = 0
    start_time = time.time()

    for i, page_path in enumerate(JOTAI_DOC_PAGES, 1):
        url = BASE_URL + page_path
        filename = path_to_filename(page_path)
        output_path = output_dir / filename

        print(f"[{i:2d}/{len(JOTAI_DOC_PAGES)}] ", end="")

        if download_page(url, output_path):
            successful += 1
        else:
            failed += 1

        # Be respectful with rate limiting
        time.sleep(0.5)

    elapsed = time.time() - start_time

    print()
    print("=" * 60)
    print("Download Summary")
    print("=" * 60)
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    print(f"Time: {elapsed:.1f} seconds")
    print(f"Output: {output_dir}")

    # Calculate total size
    total_size = sum(f.stat().st_size for f in output_dir.glob("*.md"))
    print(f"Total size: {total_size:,} bytes ({total_size/1024:.1f} KB)")

    print()
    if failed > 0:
        print(f"Warning: {failed} pages failed to download")
        sys.exit(1)
    else:
        print("All pages downloaded successfully!")
        sys.exit(0)


if __name__ == "__main__":
    main()
