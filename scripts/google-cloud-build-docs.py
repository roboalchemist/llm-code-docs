#!/usr/bin/env python3
"""
Google Cloud Build Documentation Scraper

Google Cloud Build is a managed CI/CD platform for building, testing, and deploying code on Google Cloud.
This scraper extracts key documentation pages from docs.cloud.google.com/build.

Source: https://docs.cloud.google.com/build/docs
Output: docs/web-scraped/google-cloud-build/
"""

import os
import sys
import requests
import time
from pathlib import Path
from urllib.parse import urljoin, urlparse
from html.parser import HTMLParser
import re

# Base URLs
BASE_URL = "https://cloud.google.com"
DOCS_BASE = "https://cloud.google.com/build/docs"

OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "web-scraped" / "google-cloud-build"

# Session for making requests
session = requests.Session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
})

# Key documentation pages for Cloud Build
DOCS_PAGES = [
    "/build/docs",                          # Overview
    "/build/docs/quickstart/build-push-docker-image",  # Quickstart
    "/build/docs/quickstart/build-push-gke-deploy",    # GKE quickstart
    "/build/docs/concepts",                 # Key concepts
    "/build/docs/cloud-builders",           # Cloud Builders
    "/build/docs/configuring-builds/configure-build-steps",  # Build steps
    "/build/docs/configuring-builds/configure-dockerfile-build",  # Dockerfile
    "/build/docs/configuring-builds/configure-substitutions",    # Substitutions
    "/build/docs/configuring-builds/create-basic-config",       # Basic config
    "/build/docs/configuring-builds/create-docker-config",      # Docker config
    "/build/docs/configuring-builds/substitute-variable-values", # Variables
    "/build/docs/automating-builds/automate-builds",           # Automate
    "/build/docs/automating-builds/github",                    # GitHub
    "/build/docs/automating-builds/github-app",                # GitHub App
    "/build/docs/automating-builds/gitlab",                    # GitLab
    "/build/docs/automating-builds/bitbucket",                 # Bitbucket
    "/build/docs/testing-builds/test-builds",                  # Testing
    "/build/docs/deploying-builds",                            # Deploying
    "/build/docs/deploying-gke",                               # Deploy to GKE
    "/build/docs/deploying-run",                               # Deploy to Cloud Run
    "/build/docs/deploying-cloud-functions",                   # Deploy to Functions
    "/build/docs/securing-builds",                             # Security
    "/build/docs/securing-builds/configure-encryption",        # Encryption
    "/build/docs/securing-builds/configure-private-pool",      # Private pools
    "/build/docs/securing-builds/configure-user-specified-service-account",  # Service accounts
    "/build/docs/api-reference",                               # API reference
    "/build/docs/gcloud-compute-builders",                     # gcloud builders
    "/build/docs/build-config-file-schema",                    # Schema
]

def fetch_page(url, timeout=30):
    """Fetch a page and return text."""
    try:
        resp = session.get(url, timeout=timeout, allow_redirects=True)
        resp.raise_for_status()
        return resp.text
    except Exception as e:
        print(f"Error fetching {url}: {e}", file=sys.stderr)
        return None

def extract_content_from_html(html_text):
    """Extract main content from Google Cloud docs HTML."""
    # Simple extraction - looks for main content div
    # Google Cloud docs use complex rendering, so we get what we can

    # Look for text content in the body
    if '<body' in html_text:
        try:
            start = html_text.find('<body')
            start = html_text.find('>', start) + 1
            end = html_text.rfind('</body>')
            content = html_text[start:end]

            # Remove script and style tags
            content = re.sub(r'<script[^>]*>.*?</script>', '', content, flags=re.DOTALL | re.IGNORECASE)
            content = re.sub(r'<style[^>]*>.*?</style>', '', content, flags=re.DOTALL | re.IGNORECASE)

            # Convert to markdown-like format
            content = re.sub(r'<h1[^>]*>(.*?)</h1>', r'\n# \1\n', content, flags=re.IGNORECASE)
            content = re.sub(r'<h2[^>]*>(.*?)</h2>', r'\n## \1\n', content, flags=re.IGNORECASE)
            content = re.sub(r'<h3[^>]*>(.*?)</h3>', r'\n### \1\n', content, flags=re.IGNORECASE)
            content = re.sub(r'<h4[^>]*>(.*?)</h4>', r'\n#### \1\n', content, flags=re.IGNORECASE)

            content = re.sub(r'<p[^>]*>(.*?)</p>', r'\1\n\n', content, flags=re.IGNORECASE)
            content = re.sub(r'<li[^>]*>(.*?)</li>', r'\n- \1', content, flags=re.IGNORECASE)
            content = re.sub(r'<code[^>]*>(.*?)</code>', r'`\1`', content, flags=re.IGNORECASE)

            # Remove remaining HTML tags
            content = re.sub(r'<[^>]+>', '', content)

            # Clean up whitespace
            content = re.sub(r'\n\s*\n\s*\n+', '\n\n', content)
            content = content.strip()

            return content
        except Exception as e:
            print(f"Error extracting content: {e}", file=sys.stderr)
            return None

    return None

def save_page(page_path, filename, content):
    """Save page content to file."""
    output_file = OUTPUT_DIR / filename
    output_file.parent.mkdir(parents=True, exist_ok=True)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Saved {filename} ({len(content)} bytes)")

def main():
    print("Google Cloud Build Documentation Scraper")
    print("=" * 50)

    # Create output directory
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    saved_count = 0

    for i, page_path in enumerate(DOCS_PAGES):
        url = BASE_URL + page_path
        filename = f"{i:03d}-{page_path.split('/')[-1]}.md"

        print(f"Fetching {page_path}...")
        html = fetch_page(url)

        if html:
            content = extract_content_from_html(html)
            if content:
                save_page(page_path, filename, content)
                saved_count += 1
            else:
                print(f"  Warning: Could not extract content from {url}")
        else:
            print(f"  Failed to fetch {url}")

        # Rate limiting
        time.sleep(1)

    print(f"\nSuccess! Saved {saved_count} pages")

    # List generated files
    files = list(OUTPUT_DIR.rglob("*"))
    print(f"Total files: {len([f for f in files if f.is_file()])}")

if __name__ == "__main__":
    main()
