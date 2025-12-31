#!/usr/bin/env python3
"""
Motion (formerly Framer Motion) Documentation Scraper
Downloads all Motion.dev documentation and converts to markdown.

Output: docs/web-scraped/motion/
"""

import os
import sys
import requests
from pathlib import Path
from urllib.parse import urlparse, urljoin
import time
import re

try:
    from bs4 import BeautifulSoup
    HAS_BS4 = True
except ImportError:
    HAS_BS4 = False
    print("Warning: BeautifulSoup not available, HTML cleaning will be limited")


# Configuration
OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "web-scraped" / "motion"
BASE_URL = "https://motion.dev"
READERLM_URL = os.environ.get("READERLM_URL", "http://localhost:10010")
MAX_CHUNK_SIZE = 24000  # Characters per chunk


def check_readerlm() -> bool:
    """Check if ReaderLM service is running."""
    try:
        response = requests.get(f"{READERLM_URL}/health", timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False


def clean_html(html: str) -> str:
    """Extract main content from HTML."""
    if not HAS_BS4:
        return html

    soup = BeautifulSoup(html, 'html.parser')

    # Remove non-content elements
    for tag in soup(['script', 'style', 'meta', 'link', 'noscript', 'svg', 'nav', 'footer']):
        tag.decompose()

    # Try to find main content area
    main = soup.find('main') or soup.find('article') or soup.find(class_='content')
    if main:
        return str(main)

    # Otherwise return body
    body = soup.find('body')
    if body:
        return str(body)

    return str(soup)


def convert_to_markdown(html: str, use_readerlm: bool = True) -> str:
    """Convert HTML to Markdown using ReaderLM or fallback."""
    # Clean HTML first
    if HAS_BS4:
        html = clean_html(html)

    if use_readerlm and check_readerlm():
        try:
            prompt = f"""Extract the main content from the given HTML and convert it to clean Markdown format.
```html
{html[:MAX_CHUNK_SIZE]}
```"""

            response = requests.post(
                f"{READERLM_URL}/v1/chat/completions",
                json={
                    "model": "jinaai/ReaderLM-v2",
                    "messages": [{"role": "user", "content": prompt}],
                    "temperature": 0,
                    "max_tokens": 8192,
                },
                timeout=120
            )
            response.raise_for_status()
            result = response.json()

            if "choices" in result:
                content = result["choices"][0]["message"]["content"]
                # Strip markdown code block wrapper if present
                if content.startswith("```markdown"):
                    content = content[11:]
                if content.startswith("```"):
                    content = content[3:]
                if content.endswith("```"):
                    content = content[:-3]
                return content.strip()
        except Exception as e:
            print(f"  ReaderLM failed: {e}, using fallback")

    # Fallback: basic conversion
    soup = BeautifulSoup(html, 'html.parser') if HAS_BS4 else None
    if soup:
        # Remove remaining noise
        for tag in soup(['header', 'aside', 'button']):
            tag.decompose()
        text = soup.get_text(separator='\n', strip=True)
    else:
        # Very basic HTML stripping
        text = re.sub(r'<[^>]+>', '', html)

    return text


def url_to_filename(url: str) -> str:
    """Convert URL to safe filename."""
    path = urlparse(url).path
    # Remove /docs/ prefix and normalize
    path = path.replace('/docs/', '').replace('/docs', '')
    if not path or path == '/':
        return 'index.md'

    # Clean up path
    path = path.strip('/')
    # Replace slashes with underscores
    filename = path.replace('/', '_') + '.md'
    # Remove any unsafe characters
    filename = re.sub(r'[^\w\-_.]', '_', filename)
    return filename


def fetch_page(url: str) -> tuple[str, str]:
    """Fetch a page and return (html, title)."""
    print(f"  Fetching: {url}")

    headers = {
        'User-Agent': 'Mozilla/5.0 (compatible; llm-code-docs-scraper/1.0)',
    }

    response = requests.get(url, headers=headers, timeout=30)
    response.raise_for_status()

    html = response.text

    # Extract title
    title_match = re.search(r'<title[^>]*>(.*?)</title>', html, re.IGNORECASE | re.DOTALL)
    title = title_match.group(1) if title_match else urlparse(url).path
    title = re.sub(r'\s+', ' ', title).strip()

    return html, title


def scrape_motion_docs():
    """Scrape all Motion documentation."""
    print("Motion Documentation Scraper")
    print("=" * 50)

    # Create output directory
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Output directory: {OUTPUT_DIR}")

    # Check if ReaderLM is available
    use_readerlm = check_readerlm()
    if use_readerlm:
        print("✓ ReaderLM service is running")
    else:
        print("⚠ ReaderLM service not available, using fallback conversion")

    # Load URLs from sitemap
    print("\nFetching sitemap...")
    sitemap_url = f"{BASE_URL}/sitemap.xml"
    response = requests.get(sitemap_url, timeout=10)
    response.raise_for_status()

    # Extract doc URLs from sitemap
    doc_urls = re.findall(r'<loc>(https://motion\.dev/docs[^<]*)</loc>', response.text)
    doc_urls = sorted(set(doc_urls))

    print(f"Found {len(doc_urls)} documentation URLs")

    # Process each URL
    success_count = 0
    error_count = 0

    for i, url in enumerate(doc_urls, 1):
        try:
            # Fetch page
            html, title = fetch_page(url)

            # Convert to markdown
            markdown = convert_to_markdown(html, use_readerlm)

            # Add frontmatter
            filename = url_to_filename(url)
            output = f"""# {title}

Source: {url}

---

{markdown}
"""

            # Save to file
            output_path = OUTPUT_DIR / filename
            output_path.write_text(output, encoding='utf-8')

            print(f"  [{i}/{len(doc_urls)}] ✓ Saved: {filename}")
            success_count += 1

            # Rate limiting
            time.sleep(0.5)

        except Exception as e:
            print(f"  [{i}/{len(doc_urls)}] ✗ Error: {e}")
            error_count += 1
            continue

    # Summary
    print("\n" + "=" * 50)
    print(f"Scraping complete!")
    print(f"  Success: {success_count}")
    print(f"  Errors:  {error_count}")
    print(f"  Total:   {len(doc_urls)}")
    print(f"\nOutput: {OUTPUT_DIR}")

    # List files
    files = sorted(OUTPUT_DIR.glob("*.md"))
    total_size = sum(f.stat().st_size for f in files)
    print(f"Files created: {len(files)}")
    print(f"Total size: {total_size / 1024:.1f} KB")


if __name__ == "__main__":
    try:
        scrape_motion_docs()
    except KeyboardInterrupt:
        print("\n\nInterrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\nFatal error: {e}")
        sys.exit(1)
