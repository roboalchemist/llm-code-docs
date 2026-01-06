#!/usr/bin/env python3
"""
Tilt Documentation Scraper
Downloads Tilt documentation from docs.tilt.dev and converts to markdown.
Tilt is a local Kubernetes development tool with smart rebuilds and live updates.
"""

import os
import sys
import requests
from pathlib import Path
import time
from html2text import html2text
from urllib.parse import urljoin, urlparse
import re

# Base URL for Tilt documentation
BASE_URL = "https://docs.tilt.dev/"

# Manual list of documentation pages to scrape (.html files)
DOCS_PAGES = [
    "index.html",  # Main page
    "install.html",
    "upgrade.html",
    "snippets.html",
    "editor.html",
    "api.html",
    "tiltfile_authoring.html",
    "controlloop.html",
    "choosing_clusters.html",
    "local_vs_remote.html",
    "faq.html",
    "debug_faq.html",
    "telemetry_faq.html",
    "product_faq.html",
    "code_of_conduct.html",
    "tutorial/index.html",
    "tutorial/1-prerequisites.html",
    "tutorial/2-tilt-up.html",
    "tutorial/3-tilt-ui.html",
    "tutorial/4-code-update-repeat.html",
    "tutorial/5-live-update.html",
    "example_go.html",
    "example_nodejs.html",
    "example_python.html",
    "example_java.html",
    "example_csharp.html",
    "example_bazel.html",
    "live_update_reference.html",
    "live_update_tutorial.html",
    "custom_build.html",
    "custom_resource.html",
    "local_resource.html",
    "docker_compose.html",
    "helm.html",
    "bazel.html",
    "skaffold.html",
    "file_changes.html",
    "templating.html",
    "buttons.html",
    "dependent_images.html",
    "disable_resource.html",
    "personal_registry.html",
    "multiple_repos.html",
    "manual_update_control.html",
    "resource_endpoints.html",
    "snapshots.html",
    "extensions.html",
    "ci.html",
]

REQUEST_DELAY = 0.5  # seconds between requests


def sanitize_filename(path):
    """Convert path to safe filename."""
    # Remove trailing slashes
    path = path.rstrip("/")

    # If empty, use 'index'
    if not path:
        return "index.md"

    # Replace slashes with dashes
    safe = path.replace("/", "-")

    # Ensure .md extension
    if not safe.endswith('.md'):
        safe = safe + '.md'

    return safe


def html_to_markdown(html_content):
    """Convert HTML content to markdown."""
    try:
        # Use html2text for conversion
        markdown = html2text(html_content)
        return markdown
    except Exception as e:
        print(f"    Warning: Could not convert HTML to markdown: {e}")
        # Fallback: return raw content
        return html_content


def extract_main_content(html_content):
    """Extract main documentation content from Tilt HTML."""
    try:
        # Try to extract from main content div
        # Tilt uses various content containers
        patterns = [
            r'<main[^>]*>(.*?)</main>',
            r'<article[^>]*>(.*?)</article>',
            r'<div class="[^"]*content[^"]*"[^>]*>(.*?)</div>',
        ]

        for pattern in patterns:
            match = re.search(pattern, html_content, re.DOTALL)
            if match:
                return match.group(1)

        # Try body content
        match = re.search(r'<body[^>]*>(.*?)</body>', html_content, re.DOTALL)
        if match:
            return match.group(1)

        # Fallback: return original
        return html_content
    except Exception as e:
        print(f"    Warning: Could not extract main content: {e}")
        return html_content


def download_page(page_path, output_dir):
    """Download a documentation page from Tilt."""
    try:
        # Build full URL
        url = urljoin(BASE_URL, page_path)

        # Sanitize the filename - replace .html with .md
        filename = page_path.replace(".html", ".md")
        filename = filename.replace("/", "-")

        print(f"  Downloading: {url}")

        response = requests.get(url, timeout=15)
        response.raise_for_status()

        html_content = response.text

        # Extract main content
        main_content = extract_main_content(html_content)

        # Convert to markdown
        markdown_content = html_to_markdown(main_content)

        # Add metadata header
        header = f"""# Tilt Documentation
# Source: {url}
# Path: {page_path}

"""
        content = header + markdown_content

        # Save to file
        output_path = output_dir / filename
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"    -> Saved: {filename}")
        return True

    except requests.exceptions.RequestException as e:
        print(f"    -> Error downloading {page_path}: {e}")
        return False
    except Exception as e:
        print(f"    -> Error processing {page_path}: {e}")
        return False


def main():
    """Main function to download Tilt documentation."""
    print("=" * 60)
    print("Tilt Documentation Scraper")
    print("=" * 60)
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "web-scraped" / "tilt"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Output directory: {output_dir}")
    print()

    # Download all pages
    print("Downloading documentation pages...")
    print()

    successful = 0
    failed = 0
    start_time = time.time()

    for idx, page_path in enumerate(DOCS_PAGES, 1):
        print(f"[{idx:3d}/{len(DOCS_PAGES)}] ", end="")

        if download_page(page_path, output_dir):
            successful += 1
        else:
            failed += 1

        # Be respectful with rate limiting
        time.sleep(REQUEST_DELAY)

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
    total_size = sum(f.stat().st_size for f in output_dir.rglob("*.md"))
    print(f"Total size: {total_size:,} bytes ({total_size/1024:.1f} KB)")

    print()
    if failed > 0:
        print(f"Warning: {failed} files failed to download")
        sys.exit(1)
    else:
        print("All documentation downloaded successfully!")
        sys.exit(0)


if __name__ == "__main__":
    main()
