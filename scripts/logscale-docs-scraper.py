#!/usr/bin/env python3
"""
LogScale (Humio) Documentation Scraper

Scrapes LogScale documentation from library.humio.com (now owned by CrowdStrike).
Covers query language, dashboards, data analysis, APIs, and administration.

LogScale is the next-generation log analysis and search platform.
"""

import sys
from pathlib import Path
import requests
import xml.etree.ElementTree as ET
import time
import re
from html import unescape

# Base URL for LogScale documentation
BASE_URL = "https://library.humio.com"
SITEMAP_URL = f"{BASE_URL}/sitemap.xml"

# Output directory
OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "web-scraped" / "logscale"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Request headers
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (compatible; DocumentationBot/1.0)',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}


def fetch_sitemap():
    """Fetch and parse the sitemap to get all documentation URLs."""
    try:
        print("Fetching sitemap...")
        response = requests.get(SITEMAP_URL, headers=HEADERS, timeout=30)
        response.raise_for_status()

        root = ET.fromstring(response.content)

        # Extract URLs from sitemap
        urls = []
        namespace = {'sitemap': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
        for url_elem in root.findall('sitemap:url/sitemap:loc', namespace):
            urls.append(url_elem.text)

        print(f"Found {len(urls)} documentation pages")
        return sorted(urls)
    except Exception as e:
        print(f"Error fetching sitemap: {e}")
        return []


def fetch_page_as_text(url):
    """Fetch a single page and extract text content."""
    try:
        response = requests.get(url, headers=HEADERS, timeout=30)
        response.raise_for_status()

        # Extract title from HTML
        title_match = re.search(r'<title[^>]*>([^<]+)</title>', response.text)
        title = title_match.group(1) if title_match else ""

        # Extract main content
        content_match = re.search(
            r'<(?:main|article|div[^>]*class="[^"]*content[^"]*"[^>]*)(?:\s[^>]*)?>(.+?)</(?:main|article|div)>',
            response.text,
            re.DOTALL | re.IGNORECASE
        )

        if content_match:
            content_html = content_match.group(1)
        else:
            content_html = response.text

        # Remove script and style tags
        content_html = re.sub(r'<(?:script|style)[^>]*>.*?</(?:script|style)>', '', content_html, flags=re.DOTALL | re.IGNORECASE)

        # Remove HTML tags
        content_text = re.sub(r'<[^>]+>', '\n', content_html)
        content_text = re.sub(r'\n\s*\n', '\n\n', content_text)
        content_text = unescape(content_text.strip())

        return title, content_text
    except requests.RequestException as e:
        return None, None
    except Exception as e:
        return None, None


def url_to_filename(url):
    """Convert URL to filename."""
    path = url.replace(f"{BASE_URL}/", "").rstrip(".html").rstrip("/")
    if not path:
        path = "index"
    filename = path.replace("/", "-") + ".md"
    return filename


def scrape_documentation():
    """Scrape all documentation pages."""
    urls = fetch_sitemap()

    if not urls:
        print("No URLs found in sitemap")
        return

    print(f"\nScraping {len(urls)} pages...")

    successful = 0
    failed = 0

    for i, url in enumerate(urls, 1):
        if i % 10 == 0:
            print(f"  [{i}/{len(urls)}] Scraped: {successful}, Failed: {failed}...", flush=True)

        title, content = fetch_page_as_text(url)

        if content:
            filename = url_to_filename(url)
            output_path = OUTPUT_DIR / filename

            try:
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(f"# {title or 'LogScale Documentation'}\n\n")
                    f.write(f"**Source**: {url}\n\n")
                    f.write(content)
                successful += 1
            except Exception as e:
                failed += 1
        else:
            failed += 1

        time.sleep(0.3)

    print(f"\nScraping complete!")
    print(f"  Successful: {successful}")
    print(f"  Failed: {failed}")
    print(f"  Output directory: {OUTPUT_DIR}")

    # List sample files
    files = list(OUTPUT_DIR.glob("*.md"))
    if files:
        print(f"\nSample files created:")
        for f in sorted(files)[:5]:
            size = f.stat().st_size / 1024
            print(f"  {f.name} ({size:.1f}KB)")


def write_readme():
    """Write README for this documentation set."""
    readme_path = OUTPUT_DIR / "README.md"
    readme_content = """# LogScale Documentation

This directory contains scraped documentation for LogScale (formerly Humio),
a high-performance log analysis and search platform owned by CrowdStrike.

## Source
- **URL**: https://library.humio.com
- **Type**: Web-scraped content
- **Last Updated**: Auto-generated

## Contents
- Query Language and syntax documentation
- Data analysis guides
- Dashboard and visualization documentation
- API references (Ingest, Search, GraphQL)
- Administration and deployment guides
- Integration documentation

## Notes
- LogScale was formerly known as Humio, acquired by CrowdStrike
- Documentation covers both LogScale Cloud and Self-Hosted deployments
- Includes Falcon LogScale Collector documentation
"""
    with open(readme_path, 'w') as f:
        f.write(readme_content)


if __name__ == "__main__":
    write_readme()
    scrape_documentation()
