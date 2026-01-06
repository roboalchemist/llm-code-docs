#!/usr/bin/env python3
"""
Scraper for APIable documentation.
Output: docs/web-scraped/apiable/

APIable is a developer portal as a service platform for API management.
This scraper extracts documentation and guides from their resources page.
"""
import requests
from pathlib import Path
from bs4 import BeautifulSoup
import re
import time

OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "web-scraped" / "apiable"
BASE_URL = "https://www.apiable.io"

# Article URLs to scrape
ARTICLES = [
    "/resources/what-is-an-api",
    "/resources/what-is-an-api-portal",
    "/resources/what-is-an-api-product",
    "/resources/how-apis-drive-network-effects",
    "/resources/api-portal-build-vs-buy-as-a-service",
    "/resources/bikmos-api-revolution",
    "/resources/case-study-pirate-weather",
    "/resources/api-business-plan-template",
]

def html_to_markdown(html_content):
    """Convert HTML to basic markdown."""
    # Remove script and style tags
    html_content = re.sub(r'<script[^>]*>.*?</script>', '', html_content, flags=re.DOTALL)
    html_content = re.sub(r'<style[^>]*>.*?</style>', '', html_content, flags=re.DOTALL)

    # Convert h1-h6 tags
    for i in range(1, 7):
        html_content = re.sub(rf'<h{i}[^>]*>(.*?)</h{i}>', rf'\n{"#" * i} \1\n', html_content, flags=re.DOTALL)

    # Convert paragraphs
    html_content = re.sub(r'<p[^>]*>(.*?)</p>', r'\1\n\n', html_content, flags=re.DOTALL)

    # Convert bold
    html_content = re.sub(r'<(strong|b)[^>]*>(.*?)</\1>', r'**\2**', html_content, flags=re.DOTALL)

    # Convert italic
    html_content = re.sub(r'<(em|i)[^>]*>(.*?)</\1>', r'*\2*', html_content, flags=re.DOTALL)

    # Convert links
    html_content = re.sub(r'<a[^>]*href=["\']([^"\']*)["\'][^>]*>(.*?)</a>', r'[\2](\1)', html_content, flags=re.DOTALL)

    # Convert line breaks
    html_content = re.sub(r'<br\s*/?>', '\n', html_content)

    # Remove remaining HTML tags
    html_content = re.sub(r'<[^>]+>', '', html_content)

    # Decode HTML entities
    html_content = html_content.replace('&nbsp;', ' ')
    html_content = html_content.replace('&amp;', '&')
    html_content = html_content.replace('&lt;', '<')
    html_content = html_content.replace('&gt;', '>')
    html_content = html_content.replace('&quot;', '"')
    html_content = html_content.replace('&apos;', "'")

    # Clean up whitespace
    lines = html_content.split('\n')
    cleaned_lines = [line.rstrip() for line in lines]
    html_content = '\n'.join(cleaned_lines)

    # Remove excessive blank lines
    while '\n\n\n' in html_content:
        html_content = html_content.replace('\n\n\n', '\n\n')

    return html_content.strip()

def fetch_article(url):
    """Fetch and convert article to markdown."""
    full_url = BASE_URL + url
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }

    try:
        print(f"Fetching: {full_url}")
        response = requests.get(full_url, headers=headers, timeout=10)
        response.raise_for_status()

        # Parse HTML
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract main content - look for article or main content div
        content = None
        for selector in ['article', '[role="main"]', '.prose', '.content', 'main']:
            content = soup.select_one(selector)
            if content:
                break

        if not content:
            # Fallback to body
            content = soup.body if soup.body else soup

        # Convert to markdown
        html_str = str(content)
        markdown_content = html_to_markdown(html_str)

        return markdown_content

    except Exception as e:
        print(f"Error fetching {full_url}: {e}")
        return None

def extract_title_from_url(url):
    """Extract a title from the URL path."""
    return url.split('/')[-1].replace('-', ' ').title()

def main():
    """Scrape all APIable documentation."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Create index file
    index_md = """# APIable Documentation

APIable is a developer portal as a service providing dedicated portal solutions for API management platforms. This documentation covers key concepts, guides, and case studies.

## Contents

"""

    scraped_count = 0

    for article_url in ARTICLES:
        content = fetch_article(article_url)

        if not content:
            continue

        # Generate filename
        filename = article_url.split('/')[-1] + '.md'
        filepath = OUTPUT_DIR / filename

        # Add source header
        title = extract_title_from_url(article_url)
        source_header = f"# Source: {BASE_URL}{article_url}\n\n"
        full_content = source_header + content

        # Write to file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(full_content)

        print(f"Saved: {filename}")
        index_md += f"- [{title}]({filename})\n"
        scraped_count += 1

        # Be respectful - add delay between requests
        time.sleep(0.5)

    # Write index
    index_file = OUTPUT_DIR / "index.md"
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(index_md)

    print(f"\nScraped {scraped_count} articles")
    print(f"Output directory: {OUTPUT_DIR}")
    print(f"Index: {index_file}")

if __name__ == "__main__":
    main()
