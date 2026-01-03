#!/usr/bin/env python3
"""
dasp Documentation Scraper
Downloads dasp documentation from docs.rs and GitHub, converting to markdown.
dasp is a Rust library for digital audio signal processing (DSP) with filters and effects.
"""

import os
import sys
import requests
from pathlib import Path
import time
from html2text import html2text
from urllib.parse import urljoin, urlparse
import re

# Base URLs for dasp documentation
DOCS_RS_BASE = "https://docs.rs/"
GITHUB_BASE = "https://raw.githubusercontent.com/RustAudio/dasp/master/"

# Crates to scrape from docs.rs
DOCS_CRATES = [
    ("dasp", "dasp"),  # (crate_name, display_name)
    ("dasp_sample", "dasp_sample"),
    ("dasp_frame", "dasp_frame"),
    ("dasp_signal", "dasp_signal"),
    ("dasp_interpolate", "dasp_interpolate"),
    ("dasp_envelope", "dasp_envelope"),
    ("dasp_peak", "dasp_peak"),
    ("dasp_rms", "dasp_rms"),
    ("dasp_ring_buffer", "dasp_ring_buffer"),
    ("dasp_window", "dasp_window"),
    ("dasp_slice", "dasp_slice"),
    ("dasp_graph", "dasp_graph"),
]

REQUEST_DELAY = 0.3  # seconds between requests


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
        return html_content


def extract_main_content(html_content):
    """Extract main documentation content from docs.rs HTML."""
    try:
        # docs.rs uses specific class selectors for content
        # Try to extract from div with class 'rustdoc'
        match = re.search(r'<main[^>]*>(.*?)</main>', html_content, re.DOTALL)
        if match:
            return match.group(1)

        # Try content div
        match = re.search(r'<div[^>]*class="[^"]*content[^"]*"[^>]*>(.*?)</div>', html_content, re.DOTALL | re.IGNORECASE)
        if match:
            return match.group(1)

        # Fallback: extract from body
        match = re.search(r'<body[^>]*>(.*?)</body>', html_content, re.DOTALL)
        if match:
            return match.group(1)

        return html_content
    except Exception as e:
        print(f"    Warning: Could not extract main content: {e}")
        return html_content


def download_docs_rs_crate(crate_name, display_name, output_dir):
    """Download a crate documentation from docs.rs."""
    try:
        # Build full URL with /latest/ path
        url = f"{DOCS_RS_BASE}{crate_name}/latest/{crate_name}/"

        # Sanitize the filename
        filename = f"{crate_name}.md"

        print(f"  Downloading: {url}")

        response = requests.get(url, timeout=15)
        response.raise_for_status()

        html_content = response.text

        # Extract main content
        main_content = extract_main_content(html_content)

        # Convert to markdown
        markdown_content = html_to_markdown(main_content)

        # Add metadata header
        header = f"""# {display_name} Documentation
# Source: {url}

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
        print(f"    -> Error downloading {crate_name}: {e}")
        return False
    except Exception as e:
        print(f"    -> Error processing {crate_name}: {e}")
        return False


def download_readme():
    """Download README from GitHub."""
    try:
        url = urljoin(GITHUB_BASE, "README.md")
        print(f"  Downloading: {url}")

        response = requests.get(url, timeout=15)
        response.raise_for_status()

        readme_content = f"""# dasp README
# Source: {url}

"""
        readme_content += response.text

        return readme_content

    except requests.exceptions.RequestException as e:
        print(f"    -> Error downloading README: {e}")
        return None
    except Exception as e:
        print(f"    -> Error processing README: {e}")
        return None


def main():
    """Main function to download dasp documentation."""
    print("=" * 60)
    print("dasp Documentation Scraper")
    print("=" * 60)
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "web-scraped" / "dasp"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Output directory: {output_dir}")
    print()

    # Download README first
    print("Downloading README...")
    readme_content = download_readme()
    if readme_content:
        readme_path = output_dir / "readme.md"
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(readme_content)
        print(f"  -> Saved: readme.md")
    print()

    # Download all docs.rs crates
    print("Downloading documentation from docs.rs...")
    print()

    successful = 0
    failed = 0
    start_time = time.time()

    for idx, (crate_name, display_name) in enumerate(DOCS_CRATES, 1):
        print(f"[{idx:2d}/{len(DOCS_CRATES)}] ", end="")

        if download_docs_rs_crate(crate_name, display_name, output_dir):
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
    total_size = sum(f.stat().st_size for f in output_dir.glob("*.md"))
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
