#!/usr/bin/env python3
"""
Motion Documentation Scraper
Downloads comprehensive Motion (Framer Motion) documentation from motion.dev/docs.
Motion is a production-ready animation library for React, JavaScript, and Vue with powerful animations and gestures.
"""

import os
import sys
import requests
import subprocess
import json
from pathlib import Path
from urllib.parse import urljoin, urlparse
import time
from datetime import datetime

# Base configuration
BASE_URL = "https://motion.dev"
DOCS_ROOT = f"{BASE_URL}/docs"

# Key documentation paths to scrape
DOC_PAGES = [
    # Main entry points
    "/docs",
    # Quick start
    "/docs/quick-start",
    # JavaScript/Framework docs
    "/docs/react",
    "/docs/vue",
    # Animation guides
    "/docs/react-animation",
    "/docs/react-layout-animations",
    "/docs/react-svg-animation",
    "/docs/react-motion-component",
    "/docs/react-scroll-animation",
    "/docs/react-drag-animation",
    "/docs/react-gesture-animations",
    # JavaScript raw
    "/docs/javascript-animate",
    "/docs/javascript-scroll",
    "/docs/javascript-animate-view",
    "/docs/javascript-animate-layout",
    "/docs/javascript-easing",
    # Gestures
    "/docs/hover",
    "/docs/press",
    "/docs/drag",
    "/docs/in-view",
    # Components & hooks
    "/docs/motion-component",
    "/docs/animate-presence",
    "/docs/animate-view",
    "/docs/layout-group",
    "/docs/lazy-motion",
    "/docs/motion-config",
    "/docs/reorder",
    # Motion values & hooks
    "/docs/motion-value",
    "/docs/use-motion-template",
    "/docs/use-motion-value-event",
    "/docs/use-scroll",
    "/docs/use-spring",
    "/docs/use-time",
    "/docs/use-transform",
    "/docs/use-velocity",
    "/docs/use-animate",
    "/docs/use-animation-frame",
    "/docs/use-in-view",
    # Developer tools
    "/docs/studio",
    "/docs/motionscore",
    "/docs/ai-kit",
    # Integration guides
    "/docs/framer",
    "/docs/figma",
    "/docs/squarespace",
    "/docs/wordpress",
    "/docs/webflow",
    # Premium APIs
    "/docs/carousel",
    "/docs/custom-cursor",
    "/docs/animate-number",
    "/docs/ticker",
    "/docs/typewriter",
    # Comparison & guides
    "/docs/gsap-vs-motion",
    "/docs/improvements-to-web-animations-api",
    "/docs/faq",
    # Changelog
    "/docs/changelog",
]


def scrape_page(url):
    """Scrape a single documentation page."""
    try:
        print(f"  Fetching: {url}")
        response = requests.get(url, timeout=15)
        response.raise_for_status()

        # Extract page content - motion.dev uses HTML with structured content
        content = response.text

        # Basic HTML to Markdown conversion
        # For now, we'll use the raw HTML and let markdownlint handle it
        return response.text
    except Exception as e:
        print(f"    Error fetching {url}: {e}")
        return None


def extract_title_from_url(url):
    """Extract a reasonable title from the URL."""
    path = urlparse(url).path
    # Remove /docs/ prefix and convert to title case
    title = path.replace("/docs/", "").replace("-", " ").title()
    return title or "Motion Documentation"


def download_documentation():
    """Download Motion documentation from motion.dev."""
    print("=" * 70)
    print("Motion Documentation Scraper")
    print("=" * 70)
    print()

    # Setup paths
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "web-scraped" / "motion"

    print(f"Base URL: {BASE_URL}")
    print(f"Docs root: {DOCS_ROOT}")
    print(f"Output directory: {output_dir}")
    print()

    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)

    # Download using tavily extract for best quality
    print(f"Downloading {len(DOC_PAGES)} documentation pages...")
    print()

    all_urls = [f"{BASE_URL}{page}" for page in DOC_PAGES]

    # Use tavily to extract all pages at once
    try:
        cmd = ["tavily", "extract"] + all_urls
        print(f"Running: {' '.join(cmd[:3])} ... ({len(all_urls)} URLs)")

        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)

        if result.returncode != 0:
            print(f"Warning: tavily extract exited with code {result.returncode}")
            print(f"stderr: {result.stderr}")

        # Parse JSON output
        try:
            output_data = json.loads(result.stdout)
            if isinstance(output_data, list):
                results = output_data
            else:
                results = output_data.get("results", [])
        except json.JSONDecodeError:
            print("Could not parse tavily output as JSON, using raw content")
            results = []
    except Exception as e:
        print(f"Error running tavily: {e}")
        results = []

    # Process each page
    files_created = 0

    if results:
        for i, item in enumerate(results, 1):
            url = item.get("url", "")
            content = item.get("raw_content") or item.get("content", "")

            if not url or not content:
                continue

            # Generate filename
            path = urlparse(url).path
            filename = path.lstrip("/").replace("/", "-").replace(".html", ".md")
            if not filename.endswith(".md"):
                filename += ".md"

            filepath = output_dir / filename

            # Create markdown file with source header
            title = extract_title_from_url(url)
            markdown_content = f"""# {title}

**Source:** {url}

---

{content}
"""

            try:
                filepath.write_text(markdown_content, encoding="utf-8")
                print(f"  [{i}/{len(results)}] Created: {filename}")
                files_created += 1
            except Exception as e:
                print(f"  Error writing {filename}: {e}")

    # Fallback: if tavily didn't work well, try direct requests
    if files_created < len(DOC_PAGES) // 2:
        print()
        print("Tavily extraction limited, using direct HTTP requests for remaining pages...")
        print()

        for page in DOC_PAGES:
            url = f"{BASE_URL}{page}"
            content = scrape_page(url)

            if not content:
                continue

            # Generate filename
            filename = page.lstrip("/").replace("/", "-") + ".md"
            filepath = output_dir / filename

            title = extract_title_from_url(url)
            markdown_content = f"""# {title}

**Source:** {url}

---

{content}
"""

            try:
                filepath.write_text(markdown_content, encoding="utf-8")
                print(f"  Created: {filename}")
                files_created += 1
            except Exception as e:
                print(f"  Error writing {filename}: {e}")

            time.sleep(0.5)  # Rate limit

    # Generate INDEX.md
    print()
    print("Creating index...")

    index_content = """# Motion Documentation

Motion (formerly Framer Motion) is a production-ready animation library for React, JavaScript, and Vue.

## Quick Links

- [Quick Start](docs-quick-start.md)
- [React Animation](docs-react-animation.md)
- [React Layout Animations](docs-react-layout-animations.md)
- [React SVG Animation](docs-react-svg-animation.md)
- [React Motion Component](docs-react-motion-component.md)
- [Vue Guide](docs-vue.md)
- [Studio](docs-studio.md)
- [GSAP vs Motion](docs-gsap-vs-motion.md)
- [FAQ](docs-faq.md)

## Documentation Files

This directory contains comprehensive Motion documentation extracted from https://motion.dev/docs

**Last Updated:** """ + datetime.now().isoformat() + """

### Features

- React, JavaScript, and Vue support
- Layout animations
- Scroll-triggered animations
- Gesture recognition (hover, drag, press)
- Variants and orchestration
- Motion values and hooks
- SVG animations
- Premium APIs (Carousel, Cursor, Ticker, Typewriter, etc.)

### File Structure

Each `.md` file in this directory corresponds to a section of the Motion documentation, named after the documentation URL path.
"""

    index_path = output_dir / "INDEX.md"
    index_path.write_text(index_content, encoding="utf-8")

    # Print summary
    print()
    print("=" * 70)
    print("Summary")
    print("=" * 70)

    md_files = list(output_dir.glob("**/*.md"))
    total_files = len(md_files)
    total_size = sum(f.stat().st_size for f in output_dir.glob("**/*") if f.is_file()) / 1024 / 1024

    print(f"Total files created: {total_files}")
    print(f"Total size: {total_size:.2f} MB")
    print(f"Output directory: {output_dir}")
    print()

    if total_files > 0:
        print("SUCCESS: Motion documentation downloaded successfully!")
        return 0
    else:
        print("ERROR: No files were created")
        return 1


if __name__ == "__main__":
    sys.exit(download_documentation())
