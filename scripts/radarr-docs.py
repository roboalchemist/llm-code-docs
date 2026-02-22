#!/usr/bin/env python3
"""
Radarr Documentation Scraper
Scrapes documentation from:
1. GitHub repository (README, docs)
2. Wiki (wiki.servarr.com)
3. API documentation (OpenAPI JSON)

Radarr is a movie collection manager and automation tool (PVR for movies).
Main website: radarr.video
GitHub repo: https://github.com/Radarr/Radarr
Wiki: https://wiki.servarr.com/radarr/
"""

import os
import sys
import json
import requests
from pathlib import Path
import time
from urllib.parse import urljoin, urlparse
from datetime import datetime

# Output directory
OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "web-scraped" / "radarr"

# Rate limiting
REQUEST_DELAY = 1.0  # seconds between requests


def sanitize_filename(name):
    """Convert name to safe filename."""
    safe = name.lower().replace(" ", "-").replace("/", "-")
    safe = "".join(c if c.isalnum() or c in "-_" else "" for c in safe)
    return safe + ".md"


def html_to_markdown_basic(html_text):
    """Basic HTML to Markdown conversion."""
    import re

    # Remove script and style tags
    text = re.sub(r'<script[^>]*>.*?</script>', '', html_text, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.DOTALL | re.IGNORECASE)

    # Convert headers
    text = re.sub(r'<h1[^>]*>(.*?)</h1>', r'# \1\n', text, flags=re.IGNORECASE)
    text = re.sub(r'<h2[^>]*>(.*?)</h2>', r'## \1\n', text, flags=re.IGNORECASE)
    text = re.sub(r'<h3[^>]*>(.*?)</h3>', r'### \1\n', text, flags=re.IGNORECASE)
    text = re.sub(r'<h4[^>]*>(.*?)</h4>', r'#### \1\n', text, flags=re.IGNORECASE)

    # Convert paragraphs
    text = re.sub(r'<p[^>]*>(.*?)</p>', r'\1\n\n', text, flags=re.IGNORECASE)

    # Convert links
    text = re.sub(r'<a[^>]*href=["\']([^"\']+)["\'][^>]*>(.*?)</a>', r'[\2](\1)', text, flags=re.IGNORECASE)

    # Convert bold
    text = re.sub(r'<(?:b|strong)[^>]*>(.*?)</(?:b|strong)>', r'**\1**', text, flags=re.IGNORECASE)

    # Convert italic
    text = re.sub(r'<(?:i|em)[^>]*>(.*?)</(?:i|em)>', r'*\1*', text, flags=re.IGNORECASE)

    # Convert code blocks
    text = re.sub(r'<pre[^>]*>(.*?)</pre>', r'```\n\1\n```\n', text, flags=re.IGNORECASE | re.DOTALL)

    # Convert inline code
    text = re.sub(r'<code[^>]*>(.*?)</code>', r'`\1`', text, flags=re.IGNORECASE)

    # Convert line breaks
    text = re.sub(r'<br\s*/?>', '\n', text, flags=re.IGNORECASE)

    # Remove remaining HTML tags
    text = re.sub(r'<[^>]+>', '', text)

    # Clean up whitespace
    text = re.sub(r'\n\n\n+', '\n\n', text)
    text = re.sub(r'  +', ' ', text)

    return text.strip()


def fetch_github_readme():
    """Fetch Radarr README from GitHub."""
    print("Fetching GitHub README...")
    try:
        url = "https://raw.githubusercontent.com/Radarr/Radarr/develop/README.md"
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"  Error fetching GitHub README: {e}")
        return None


def fetch_github_contributing():
    """Fetch CONTRIBUTING.md from GitHub."""
    print("Fetching GitHub CONTRIBUTING guide...")
    try:
        url = "https://raw.githubusercontent.com/Radarr/Radarr/develop/CONTRIBUTING.md"
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"  Error fetching CONTRIBUTING: {e}")
        return None


def fetch_openapi_docs():
    """Fetch OpenAPI documentation from Radarr's GitHub."""
    print("Fetching OpenAPI documentation...")
    try:
        url = "https://raw.githubusercontent.com/Radarr/Radarr/develop/src/Radarr.Api.V3/openapi.json"
        response = requests.get(url, timeout=15)
        response.raise_for_status()

        # Parse OpenAPI and create a markdown guide
        openapi_data = response.json()

        markdown = "# Radarr API Documentation (v3)\n\n"
        markdown += f"Auto-generated from OpenAPI spec\n"
        markdown += f"Last updated: {datetime.now().strftime('%Y-%m-%d')}\n\n"

        if "info" in openapi_data:
            info = openapi_data["info"]
            markdown += f"## Info\n\n"
            if "title" in info:
                markdown += f"**Title:** {info['title']}\n"
            if "description" in info:
                markdown += f"**Description:** {info['description']}\n"
            if "version" in info:
                markdown += f"**Version:** {info['version']}\n"
            markdown += "\n"

        if "servers" in openapi_data:
            markdown += "## Servers\n\n"
            for server in openapi_data["servers"]:
                markdown += f"- {server.get('url', 'N/A')}"
                if "description" in server:
                    markdown += f" - {server['description']}"
                markdown += "\n"
            markdown += "\n"

        if "paths" in openapi_data:
            markdown += "## API Endpoints\n\n"
            paths = openapi_data["paths"]

            for path, methods in sorted(paths.items()):
                markdown += f"### {path}\n\n"

                for method, details in methods.items():
                    if isinstance(details, dict) and "summary" in details:
                        markdown += f"**{method.upper()}** - {details['summary']}\n"
                        if "description" in details:
                            markdown += f"\n{details['description']}\n"
                        markdown += "\n"

        return markdown
    except Exception as e:
        print(f"  Error fetching OpenAPI docs: {e}")
        return None


def fetch_wiki_page(path):
    """Fetch a wiki page from wiki.servarr.com."""
    try:
        # Wiki URL structure: https://wiki.servarr.com/radarr/{page}
        url = f"https://wiki.servarr.com/radarr/{path}"
        response = requests.get(url, timeout=15)
        response.raise_for_status()

        # Convert HTML to basic markdown
        markdown = html_to_markdown_basic(response.text)
        return markdown
    except Exception as e:
        print(f"  Error fetching {path}: {e}")
        return None


def fetch_wiki_docs():
    """Fetch main wiki pages for Radarr."""
    print("Fetching wiki documentation from wiki.servarr.com...")

    wiki_pages = [
        ("home", "Home / Introduction"),
        ("installation", "Installation Guide"),
        ("settings", "Settings & Configuration"),
        ("workflow", "Workflow & Setup"),
        ("library", "Library Management"),
        ("wanted", "Wanted / Missing Movies"),
        ("quality", "Quality Settings"),
        ("profiles", "Profiles"),
        ("custom-formats", "Custom Formats"),
        ("appdata", "AppData Documentation"),
        ("postgres", "PostgreSQL Setup"),
    ]

    wiki_docs = {}

    for page, title in wiki_pages:
        time.sleep(REQUEST_DELAY)
        print(f"  Fetching: {title}...")

        content = fetch_wiki_page(page)
        if content:
            wiki_docs[page] = (title, content)

    return wiki_docs


def save_markdown_file(filename, content):
    """Save content to a markdown file."""
    if content is None:
        return False

    try:
        file_path = OUTPUT_DIR / filename
        file_path.write_text(content, encoding='utf-8')
        print(f"  Saved: {filename}")
        return True
    except Exception as e:
        print(f"  Error saving {filename}: {e}")
        return False


def create_index_file():
    """Create an index/overview file."""
    index = """# Radarr Documentation Index

Radarr is a movie collection manager and automation tool (PVR for movies).

**Official Website:** https://radarr.video/
**GitHub Repository:** https://github.com/Radarr/Radarr
**Wiki:** https://wiki.servarr.com/radarr/
**API Documentation:** https://radarr.video/docs/api/

## Contents

### Getting Started
- **00-README.md** - Official project README
- **01-CONTRIBUTING.md** - Contributing guidelines

### API Documentation
- **02-API-V3.md** - Radarr API v3 reference

### Wiki Pages
- **03-Wiki-Installation.md** - Installation guide
- **03-Wiki-Settings.md** - Settings and configuration
- **03-Wiki-Workflow.md** - Workflow and initial setup
- **03-Wiki-Library.md** - Library management
- **03-Wiki-Wanted.md** - Wanted/missing movies

### Configuration
- **03-Wiki-Profiles.md** - Quality and release profiles
- **03-Wiki-Quality.md** - Quality settings
- **03-Wiki-CustomFormats.md** - Custom format configuration

### Advanced
- **03-Wiki-AppData.md** - AppData folder reference
- **03-Wiki-PostgreSQL.md** - PostgreSQL database setup

## API Quick Reference

Radarr provides a comprehensive REST API (v3) for automation and integration.

Access the interactive API documentation at: https://radarr.video/docs/api/

### Common API Endpoints

- `GET /api/v3/movie` - List all movies
- `GET /api/v3/movie/{id}` - Get movie details
- `POST /api/v3/movie` - Add a new movie
- `GET /api/v3/calendar` - Get calendar
- `GET /api/v3/wanted/missing` - Get wanted/missing movies
- `GET /api/v3/profile` - List quality profiles
- `GET /api/v3/customformat` - List custom formats

Requires API key authentication via `X-Api-Key` header or `apikey` query parameter.

## Key Features

- Automatic movie discovery and download
- Full integration with torrent and usenet clients
- Quality profiles and custom formats
- Multiple language support
- Calendar integration
- Wanted/missing movie tracking
- REST API for automation
- Docker support

## Related Projects

The Servarr project includes several related services:
- **Sonarr** - TV series automation (PVR for TV)
- **Lidarr** - Music library management
- **Prowlarr** - Indexer management
- **Bazarr** - Subtitle management

All share similar architecture and API patterns.
"""

    file_path = OUTPUT_DIR / "00-README.md"
    file_path.write_text(index, encoding='utf-8')
    print(f"  Saved: 00-README.md (index)")


def main():
    """Main scraper function."""
    print("\n" + "=" * 60)
    print("Radarr Documentation Scraper")
    print("=" * 60 + "\n")

    # Create output directory
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Output directory: {OUTPUT_DIR}\n")

    # Track saved files
    saved_files = []

    # 1. Fetch and save GitHub README
    print("Step 1: GitHub Repository")
    print("-" * 40)
    readme = fetch_github_readme()
    if save_markdown_file("00-README.md", readme):
        saved_files.append("00-README.md")
    time.sleep(REQUEST_DELAY)

    # 2. Fetch and save CONTRIBUTING guide
    contributing = fetch_github_contributing()
    if save_markdown_file("01-CONTRIBUTING.md", contributing):
        saved_files.append("01-CONTRIBUTING.md")
    time.sleep(REQUEST_DELAY)

    # 3. Fetch and save API documentation
    print("\nStep 2: API Documentation")
    print("-" * 40)
    openapi_docs = fetch_openapi_docs()
    if save_markdown_file("02-API-V3.md", openapi_docs):
        saved_files.append("02-API-V3.md")
    time.sleep(REQUEST_DELAY)

    # 4. Fetch and save wiki pages
    print("\nStep 3: Wiki Documentation")
    print("-" * 40)
    wiki_pages = fetch_wiki_docs()
    for page_key, (page_title, page_content) in wiki_pages.items():
        sanitized_name = f"03-Wiki-{page_key.replace('-', ' ').title().replace(' ', '')}.md"
        if save_markdown_file(sanitized_name, page_content):
            saved_files.append(sanitized_name)

    # 5. Create index file
    print("\nStep 4: Creating Index")
    print("-" * 40)
    create_index_file()
    saved_files.insert(0, "00-README.md")  # Index is first

    # Summary
    print("\n" + "=" * 60)
    print(f"Scraping complete!")
    print(f"Total files saved: {len(saved_files)}")
    print("\nFiles created:")
    for f in sorted(saved_files):
        print(f"  - {f}")
    print("=" * 60 + "\n")

    return 0


if __name__ == "__main__":
    sys.exit(main())
