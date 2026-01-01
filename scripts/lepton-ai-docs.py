#!/usr/bin/env python3
"""
Scraper for Lepton AI documentation.
Output: docs/web-scraped/lepton-ai/
"""

import os
import re
import requests
from pathlib import Path
from urllib.parse import urljoin, urlparse
try:
    from markdownify import markdownify as md
except ImportError:
    import html2text
    def md(html):
        h = html2text.HTML2Text()
        h.ignore_links = False
        h.body_width = 0
        return h.handle(html)

OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "web-scraped" / "lepton-ai"

# Documentation pages to scrape from NVIDIA DGX Cloud Lepton
PAGES_TO_SCRAPE = [
    ("Introduction", "https://docs.nvidia.com/dgx-cloud/lepton/"),
    ("Getting Started - Endpoint", "https://docs.nvidia.com/dgx-cloud/lepton/get-started/endpoint"),
    ("Getting Started - Dev Pod", "https://docs.nvidia.com/dgx-cloud/lepton/get-started/dev-pod"),
    ("Getting Started - Batch Job", "https://docs.nvidia.com/dgx-cloud/lepton/get-started/batch-job"),
    ("Getting Started - Node Group", "https://docs.nvidia.com/dgx-cloud/lepton/get-started/node-group"),
    ("Getting Started - Workspace", "https://docs.nvidia.com/dgx-cloud/lepton/get-started/workspace"),
    ("Endpoint Configurations", "https://docs.nvidia.com/dgx-cloud/lepton/features/endpoints/configurations"),
    ("Create LLM Endpoint", "https://docs.nvidia.com/dgx-cloud/lepton/features/endpoints/create-llm"),
    ("Create NIM Endpoint", "https://docs.nvidia.com/dgx-cloud/lepton/features/endpoints/create-from-nim"),
    ("Dev Pod Configurations", "https://docs.nvidia.com/dgx-cloud/lepton/features/dev-pods/configurations"),
    ("Batch Job Configurations", "https://docs.nvidia.com/dgx-cloud/lepton/features/batch-jobs/configurations"),
    ("Bring Your Own Compute", "https://docs.nvidia.com/dgx-cloud/lepton/compute/bring-your-own-compute"),
    ("Workspace Members", "https://docs.nvidia.com/dgx-cloud/lepton/features/workspace/members"),
    ("Workspace Tokens", "https://docs.nvidia.com/dgx-cloud/lepton/features/workspace/token"),
    ("Workspace Secrets", "https://docs.nvidia.com/dgx-cloud/lepton/features/workspace/secret"),
    ("Python SDK Reference", "https://docs.nvidia.com/dgx-cloud/lepton/reference/api"),
]

GITHUB_README_URL = "https://raw.githubusercontent.com/leptonai/leptonai/main/README.md"
GITHUB_CONTRIBUTING_URL = "https://raw.githubusercontent.com/leptonai/leptonai/main/CONTRIBUTING.md"


def create_output_dir():
    """Create output directory if it doesn't exist."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def fetch_page(url):
    """Fetch a page and extract main content."""
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        response = requests.get(url, timeout=10, headers=headers)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None


def extract_markdown_from_html(html_content, title=""):
    """Extract markdown content from HTML."""
    try:
        # Convert HTML to markdown
        markdown_content = md(html_content)

        # Add source header
        source_line = f"# Source: {title}\n\n"

        return source_line + markdown_content
    except Exception as e:
        print(f"Error converting to markdown: {e}")
        return None


def fetch_github_docs(url, filename):
    """Fetch documentation from GitHub."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"Error fetching GitHub {filename}: {e}")
        return None


def sanitize_filename(filename):
    """Sanitize filename for file system."""
    # Replace spaces and special characters
    filename = re.sub(r'[^\w\s-]', '', filename)
    filename = re.sub(r'[-\s]+', '-', filename)
    return filename.lower()


def scrape_documentation():
    """Main scraping function."""
    create_output_dir()

    print(f"Scraping Lepton AI documentation to {OUTPUT_DIR}")

    # Scrape NVIDIA DGX Cloud Lepton documentation pages
    for page_title, page_url in PAGES_TO_SCRAPE:
        print(f"Fetching: {page_title}")

        html_content = fetch_page(page_url)
        if not html_content:
            continue

        markdown_content = extract_markdown_from_html(html_content, page_url)
        if not markdown_content:
            continue

        # Create filename from title
        safe_filename = sanitize_filename(page_title)
        output_file = OUTPUT_DIR / f"{safe_filename}.md"

        try:
            with open(output_file, "w", encoding="utf-8") as f:
                f.write(markdown_content)
            print(f"  ✓ Saved to {output_file.name}")
        except Exception as e:
            print(f"  ✗ Error saving {output_file.name}: {e}")

    # Fetch GitHub README
    print("Fetching GitHub README")
    readme_content = fetch_github_docs(GITHUB_README_URL, "README.md")
    if readme_content:
        output_file = OUTPUT_DIR / "github-readme.md"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(f"# Source: {GITHUB_README_URL}\n\n")
            f.write(readme_content)
        print(f"  ✓ Saved GitHub README")

    # Fetch CONTRIBUTING guide
    print("Fetching CONTRIBUTING guide")
    contributing_content = fetch_github_docs(GITHUB_CONTRIBUTING_URL, "CONTRIBUTING.md")
    if contributing_content:
        output_file = OUTPUT_DIR / "contributing.md"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(f"# Source: {GITHUB_CONTRIBUTING_URL}\n\n")
            f.write(contributing_content)
        print(f"  ✓ Saved CONTRIBUTING guide")

    # Create index file
    create_index_file()

    print(f"\nDocumentation saved to {OUTPUT_DIR}")
    print(f"Total files: {len(list(OUTPUT_DIR.glob('*.md')))}")


def create_index_file():
    """Create an index file for easy navigation."""
    index_content = """# Lepton AI Documentation Index

## Overview
Lepton AI is a containerized inference deployment platform with autoscaling capabilities.

**Official Documentation:** https://docs.nvidia.com/dgx-cloud/lepton/
**GitHub Repository:** https://github.com/leptonai/leptonai

## Documentation Sections

### Getting Started
- **Introduction** - Overview of DGX Cloud Lepton
- **Endpoint** - Deploy and manage AI model endpoints
- **Dev Pod** - Lightweight AI development environments
- **Batch Job** - Run one-off tasks and jobs
- **Node Group** - Manage compute node groups
- **Workspace** - Workspace setup and management

### Features
- **Endpoint Configurations** - Configure endpoint settings, autoscaling, access control
- **Create LLM Endpoint** - Deploy Large Language Models
- **Create NIM Endpoint** - Deploy NVIDIA NIM endpoints
- **Dev Pod Configurations** - Configure development pod settings
- **Batch Job Configurations** - Configure batch job parameters
- **Workspace Members** - Manage workspace access and permissions
- **Workspace Tokens** - Authentication tokens
- **Workspace Secrets** - Secret management

### Compute
- **Bring Your Own Compute** - Use your own infrastructure with Lepton

### Reference
- **Python SDK Reference** - API documentation and examples

### Repository
- **GitHub README** - Project overview and getting started
- **CONTRIBUTING** - Contributing guidelines

## Key Concepts

### Endpoint
A running instance of an AI model that exposes an HTTP server. Accessible via REST APIs with support for:
- Autoscaling based on traffic (QPM) or GPU utilization
- Access control (IP allowlist, tokens)
- Health checks and monitoring

### Dev Pod
Lightweight, container-based AI development environments for building and testing applications.
- Full web terminal access
- SSH support
- JupyterLab integration
- Starter kits for common workflows

### Batch Job
One-off tasks like model training or data processing that run to completion.
- Simple configuration
- Status tracking
- Automatic archiving after completion

### Bring Your Own Compute (BYOC)
Integrate your existing hardware infrastructure with Lepton's management platform.

## Quick Links

- **Main Documentation:** https://docs.nvidia.com/dgx-cloud/lepton/
- **GitHub:** https://github.com/leptonai/leptonai
- **Examples:** https://github.com/leptonai/examples
"""

    index_file = OUTPUT_DIR / "index.md"
    with open(index_file, "w", encoding="utf-8") as f:
        f.write(index_content)
    print(f"  ✓ Created index file")


if __name__ == "__main__":
    scrape_documentation()
