#!/usr/bin/env python3
"""
Scraper for Lambda Labs/Lambda Cloud documentation.
Fetches all documentation from docs.lambda.ai/sitemap.xml

Output: docs/web-scraped/lambda-cloud/
"""

import urllib.request
import urllib.parse
import re
import os
from pathlib import Path
from html.parser import HTMLParser
from urllib.error import HTTPError, URLError
import time

OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "web-scraped" / "lambda-cloud"

class HTMLToMarkdown(HTMLParser):
    """Convert HTML to Markdown with basic formatting."""

    def __init__(self):
        super().__init__()
        self.text = []
        self.current_tag = []
        self.list_depth = 0
        self.code_block = False
        self.in_code = False

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)

        if tag == 'h1':
            self.text.append('\n# ')
        elif tag == 'h2':
            self.text.append('\n## ')
        elif tag == 'h3':
            self.text.append('\n### ')
        elif tag == 'h4':
            self.text.append('\n#### ')
        elif tag == 'h5':
            self.text.append('\n##### ')
        elif tag == 'h6':
            self.text.append('\n###### ')
        elif tag == 'p':
            self.text.append('\n')
        elif tag == 'br':
            self.text.append('\n')
        elif tag == 'strong' or tag == 'b':
            self.text.append('**')
        elif tag == 'em' or tag == 'i':
            self.text.append('*')
        elif tag == 'code':
            if not self.in_code:
                self.text.append('`')
                self.in_code = True
        elif tag == 'pre':
            self.text.append('\n```\n')
            self.code_block = True
        elif tag == 'ul' or tag == 'ol':
            self.list_depth += 1
        elif tag == 'li':
            indent = '  ' * (self.list_depth - 1)
            self.text.append(f'\n{indent}- ')
        elif tag == 'a':
            href = attrs_dict.get('href', '#')
            self.text.append('[')
            self.current_tag.append(('a', href))
        elif tag == 'img':
            alt = attrs_dict.get('alt', 'Image')
            src = attrs_dict.get('src', '')
            self.text.append(f'![{alt}]({src})')
        elif tag == 'blockquote':
            self.text.append('\n> ')

    def handle_endtag(self, tag):
        if tag == 'h1' or tag == 'h2' or tag == 'h3' or tag == 'h4' or tag == 'h5' or tag == 'h6' or tag == 'p':
            self.text.append('\n')
        elif tag == 'strong' or tag == 'b':
            self.text.append('**')
        elif tag == 'em' or tag == 'i':
            self.text.append('*')
        elif tag == 'code':
            if self.in_code:
                self.text.append('`')
                self.in_code = False
        elif tag == 'pre':
            self.text.append('\n```\n')
            self.code_block = False
        elif tag == 'ul' or tag == 'ol':
            self.list_depth = max(0, self.list_depth - 1)
        elif tag == 'a':
            if self.current_tag and self.current_tag[-1][0] == 'a':
                href = self.current_tag.pop()[1]
                self.text.append(f']({href})')

    def handle_data(self, data):
        if self.code_block or self.in_code:
            self.text.append(data)
        else:
            data = re.sub(r'\s+', ' ', data).strip()
            if data:
                self.text.append(data + ' ')

    def get_markdown(self):
        content = ''.join(self.text)
        content = re.sub(r'\n\n+', '\n\n', content)
        return content.strip()


def fetch_sitemap():
    """Fetch the sitemap and extract all documentation URLs."""
    url = "https://docs.lambda.ai/sitemap.xml"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            content = response.read().decode('utf-8')

        urls = re.findall(r'<loc>(.*?)</loc>', content)
        urls = [u for u in urls if '/tags/' not in u and u.strip('/') != 'https://docs.lambda.ai']
        return urls
    except Exception as e:
        print(f"Error fetching sitemap: {e}")
        return []


def url_to_filename(url):
    """Convert a URL to a safe filename."""
    path = urllib.parse.urlparse(url).path
    path = path.strip('/').replace('/', '_')

    if not path or path == 'docs.lambda.ai':
        path = 'index'

    return f"{path}.md"


def fetch_and_convert_page(url):
    """Fetch a page and convert HTML to Markdown."""
    try:
        req = urllib.request.Request(url, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })

        with urllib.request.urlopen(req, timeout=15) as response:
            if response.status != 200:
                return None

            html_content = response.read().decode('utf-8', errors='ignore')

        # Extract main content
        content_match = re.search(
            r'<(?:main|article|div[^>]*class="[^"]*content[^"]*"[^>]*|div[^>]*id="[^"]*content[^"]*"[^>]*)>.*?</(?:main|article|div)>',
            html_content,
            re.DOTALL | re.IGNORECASE
        )

        if not content_match:
            body_match = re.search(r'<body[^>]*>(.*?)</body>', html_content, re.DOTALL)
            content = body_match.group(1) if body_match else html_content
        else:
            content = content_match.group(0)

        # Extract title
        title_match = re.search(r'<title[^>]*>([^<]+)</title>', html_content)
        title = title_match.group(1) if title_match else ''
        title = title.replace(' | ', ' - ').replace('Lambda Docs', '').strip()

        # Convert HTML to Markdown
        parser = HTMLToMarkdown()
        try:
            parser.feed(content)
            markdown = parser.get_markdown()
        except Exception as e:
            markdown = content

        final_markdown = f"""# {title if title else 'Documentation Page'}

Source: {url}

---

{markdown}
"""

        return final_markdown

    except HTTPError as e:
        return None
    except URLError as e:
        return None
    except Exception as e:
        return None


def scrape_documentation():
    """Main scraping function."""
    print("Lambda Cloud Documentation Scraper")
    print("=" * 60)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print("\nFetching sitemap...")
    urls = fetch_sitemap()
    print(f"Found {len(urls)} documentation pages\n")

    if not urls:
        print("No URLs found in sitemap!")
        return

    # Categorize URLs by section
    sections = {}
    for url in urls:
        path = urllib.parse.urlparse(url).path.strip('/')
        section = path.split('/')[0] if '/' in path else 'root'

        if section not in sections:
            sections[section] = []
        sections[section].append(url)

    success_count = 0
    failure_count = 0

    for section in sorted(sections.keys()):
        print(f"\nSection: {section}/")
        section_urls = sections[section]

        for i, url in enumerate(sorted(section_urls), 1):
            filename = url_to_filename(url)
            filepath = OUTPUT_DIR / filename

            print(f"  [{i}/{len(section_urls)}] {filename}...", end=' ')

            markdown = fetch_and_convert_page(url)

            if markdown:
                filepath.write_text(markdown, encoding='utf-8')
                print("OK")
                success_count += 1
                time.sleep(0.5)
            else:
                print("SKIP")
                failure_count += 1

    print("\n" + "=" * 60)
    print(f"Scraping complete!")
    print(f"  Success: {success_count} pages")
    print(f"  Failed: {failure_count} pages")
    print(f"  Output: {OUTPUT_DIR}")

    files = list(OUTPUT_DIR.glob("*.md"))
    print(f"  Total files: {len(files)}")

    if files:
        total_size = sum(f.stat().st_size for f in files)
        print(f"  Total size: {total_size / 1024 / 1024:.2f} MB")


if __name__ == "__main__":
    scrape_documentation()
