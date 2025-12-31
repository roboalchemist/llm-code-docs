#!/usr/bin/env python3
"""
SparkFun Tutorials Documentation Scraper
Downloads all SparkFun tutorials from learn.sparkfun.com and converts to markdown.
SparkFun is a popular electronics retailer with extensive tutorials for Arduino, Raspberry Pi, sensors, and hardware projects.
"""

import os
import sys
import requests
from pathlib import Path
from urllib.parse import urljoin
import time
import re
import subprocess

BASE_URL = "https://learn.sparkfun.com"
TUTORIALS_URL = f"{BASE_URL}/tutorials"


def get_all_tutorials():
    """Fetch all tutorial URLs from the tutorials page using regex."""
    print(f"Fetching tutorials list from: {TUTORIALS_URL}?page=all")

    try:
        # Request the page with all tutorials on one page
        response = requests.get(f"{TUTORIALS_URL}?page=all", timeout=60)
        response.raise_for_status()

        html = response.text

        # Find all tutorial tiles
        # Pattern: <div class="tile tutorial-tile" ...> followed by <a href="...">
        # The URL is in format: https://learn.sparkfun.com/tutorials/tutorial-name
        pattern = r'<div class="tile tutorial-tile[^>]*>[\s\S]*?<a href="(https://learn\.sparkfun\.com/tutorials/[^"]+)"'
        matches = re.findall(pattern, html, re.IGNORECASE)

        # Deduplicate
        tutorial_links = []
        seen = set()

        for url in matches:
            if url not in seen:
                seen.add(url)
                tutorial_links.append(url)

        print(f"Found {len(tutorial_links)} unique tutorials")
        return sorted(tutorial_links)

    except Exception as e:
        print(f"Error fetching tutorials list: {e}")
        sys.exit(1)


def sanitize_filename(url):
    """Create a safe filename from tutorial URL."""
    # Extract tutorial name from URL: /tutorials/tutorial-name -> tutorial-name.md
    parts = url.rstrip('/').split('/')
    tutorial_name = parts[-1] if parts[-1] else parts[-2]

    # Clean up the name
    tutorial_name = re.sub(r'[^\w\-]', '_', tutorial_name)
    tutorial_name = re.sub(r'_+', '_', tutorial_name)
    tutorial_name = tutorial_name.strip('_')

    return f"{tutorial_name}.md"


def html_to_markdown(html_content, url):
    """Convert HTML to markdown using pandoc."""

    # SparkFun tutorials have content in multiple <div class="section tutorial-page"> sections
    # Extract all of them and combine
    section_pattern = r'<div class="section tutorial-page"[^>]*>(.*?)</div>\s*(?=<div class="section tutorial-page"|<div class="related-tutorials"|$)'
    sections = re.findall(section_pattern, html_content, re.DOTALL | re.IGNORECASE)

    if sections:
        # Combine all sections
        cleaned_html = '\n\n'.join(sections)
    else:
        # Fallback: try other patterns
        content_patterns = [
            r'<article[^>]*>(.*?)</article>',
            r'<main[^>]*>(.*?)</main>',
        ]
        cleaned_html = html_content
        for pattern in content_patterns:
            match = re.search(pattern, html_content, re.DOTALL | re.IGNORECASE)
            if match:
                cleaned_html = match.group(1)
                break

    # Remove script and style elements
    cleaned_html = re.sub(r'<script[^>]*>.*?</script>', '', cleaned_html, flags=re.DOTALL | re.IGNORECASE)
    cleaned_html = re.sub(r'<style[^>]*>.*?</style>', '', cleaned_html, flags=re.DOTALL | re.IGNORECASE)
    cleaned_html = re.sub(r'<nav[^>]*>.*?</nav>', '', cleaned_html, flags=re.DOTALL | re.IGNORECASE)
    cleaned_html = re.sub(r'<header[^>]*>.*?</header>', '', cleaned_html, flags=re.DOTALL | re.IGNORECASE)
    cleaned_html = re.sub(r'<footer[^>]*>.*?</footer>', '', cleaned_html, flags=re.DOTALL | re.IGNORECASE)
    cleaned_html = re.sub(r'<aside[^>]*>.*?</aside>', '', cleaned_html, flags=re.DOTALL | re.IGNORECASE)
    cleaned_html = re.sub(r'<iframe[^>]*>.*?</iframe>', '', cleaned_html, flags=re.DOTALL | re.IGNORECASE)

    # Try pandoc for best quality conversion
    try:
        result = subprocess.run(
            ['pandoc', '-f', 'html', '-t', 'markdown', '--wrap=none'],
            input=cleaned_html,
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

    # Fallback: Basic text extraction
    # Remove all HTML tags
    text = re.sub(r'<[^>]+>', ' ', cleaned_html)
    # Decode HTML entities
    text = text.replace('&nbsp;', ' ')
    text = text.replace('&lt;', '<')
    text = text.replace('&gt;', '>')
    text = text.replace('&amp;', '&')
    text = text.replace('&quot;', '"')
    text = text.replace('&#39;', "'")
    # Normalize whitespace
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = re.sub(r' {2,}', ' ', text)
    text = text.strip()

    return f"# Source: {url}\n\n{text}"


def download_tutorial(url, output_dir):
    """Download a single tutorial and convert to markdown."""
    try:
        # Fetch the page
        response = requests.get(url, timeout=30)
        response.raise_for_status()

        # Convert to markdown
        markdown_content = html_to_markdown(response.text, url)

        # Save to file
        filename = sanitize_filename(url)
        output_path = output_dir / filename
        output_path.write_text(markdown_content, encoding='utf-8')

        return True, len(markdown_content)

    except Exception as e:
        print(f"  -> Error: {e}")
        return False, 0


def main():
    """Main function to download all SparkFun tutorials."""
    print("=" * 60)
    print("SparkFun Tutorials Documentation Scraper")
    print("=" * 60)
    print("Source: learn.sparkfun.com")
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "web-scraped" / "sparkfun"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Output directory: {output_dir}")
    print()

    # Check for pandoc
    try:
        subprocess.run(['pandoc', '--version'], capture_output=True, timeout=5)
        print("Pandoc found - will use for high-quality markdown conversion")
    except (FileNotFoundError, subprocess.TimeoutExpired):
        print("Warning: Pandoc not found - will use fallback conversion")
    print()

    start_time = time.time()

    # Get all tutorials
    tutorial_urls = get_all_tutorials()

    if not tutorial_urls:
        print("Error: No tutorials found")
        sys.exit(1)

    print(f"\nStarting download of {len(tutorial_urls)} tutorials...")
    print("This may take a while...")
    print()

    successful = 0
    failed = 0
    total_bytes = 0

    for i, url in enumerate(tutorial_urls, 1):
        # Extract tutorial name for display
        tutorial_name = url.split('/')[-1] or url.split('/')[-2]

        print(f"[{i:4d}/{len(tutorial_urls)}] {tutorial_name}", end=" ")

        success, byte_count = download_tutorial(url, output_dir)

        if success:
            successful += 1
            total_bytes += byte_count
            print(f"-> OK ({byte_count:,} bytes)")
        else:
            failed += 1
            print("-> FAILED")

        # Rate limiting - be nice to the server
        if i < len(tutorial_urls):
            time.sleep(0.5)  # 500ms delay between requests

    elapsed = time.time() - start_time

    print()
    print("=" * 60)
    print("Download Summary")
    print("=" * 60)
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    print(f"Time: {elapsed:.1f} seconds ({elapsed/60:.1f} minutes)")
    print(f"Output: {output_dir}")
    print(f"Total size: {total_bytes:,} bytes ({total_bytes/1024/1024:.1f} MB)")
    print(f"Average: {total_bytes/successful:,.0f} bytes per tutorial" if successful > 0 else "")

    print()
    if failed > 0:
        print(f"Warning: {failed} tutorials failed to download")
    else:
        print("All tutorials downloaded successfully!")

    sys.exit(0 if failed == 0 else 1)


if __name__ == "__main__":
    main()
