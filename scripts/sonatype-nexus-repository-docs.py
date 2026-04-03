#!/usr/bin/env python3
"""
Sonatype Nexus Repository Documentation Scraper
Fetches key documentation pages from help.sonatype.com
"""

import requests
from pathlib import Path
import time
import sys
import re
from html.parser import HTMLParser
from html import unescape

OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "web-scraped" / "sonatype-nexus-repository"

# Key documentation pages to scrape
PAGES_TO_SCRAPE = [
    "https://help.sonatype.com/en/sonatype-nexus-repository.html",
    "https://help.sonatype.com/en/getting-started.html",
    "https://help.sonatype.com/en/installation.html",
    "https://help.sonatype.com/en/system-requirements.html",
    "https://help.sonatype.com/en/administration.html",
    "https://help.sonatype.com/en/accessing-the-sonatype-nexus-repository-pro-api.html",
    "https://help.sonatype.com/en/integrations.html",
    "https://help.sonatype.com/en/upgrading.html",
    "https://help.sonatype.com/en/supported-package-formats.html",
    "https://help.sonatype.com/en/high-availability.html",
]


class HTMLToMarkdown(HTMLParser):
    """Simple HTML to Markdown converter."""
    def __init__(self):
        super().__init__()
        self.text = []
        self.in_code = False
        self.in_pre = False
        self.code_lang = ''
        self.in_script = False
        self.in_style = False

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if tag == 'script' or tag == 'style':
            self.in_script = True
        elif tag == 'pre':
            self.in_pre = True
            self.code_lang = attrs_dict.get('data-lang', 'text')
            self.text.append(f'\n```{self.code_lang}\n')
        elif tag == 'code':
            self.in_code = True
            self.text.append('`')
        elif tag == 'h1':
            self.text.append('\n# ')
        elif tag == 'h2':
            self.text.append('\n## ')
        elif tag == 'h3':
            self.text.append('\n### ')
        elif tag == 'h4':
            self.text.append('\n#### ')
        elif tag == 'p':
            self.text.append('\n')
        elif tag == 'br':
            self.text.append('\n')
        elif tag == 'li':
            self.text.append('\n- ')
        elif tag == 'a':
            href = attrs_dict.get('href', '')
            if href:
                self.text.append('[')
        elif tag == 'strong' or tag == 'b':
            self.text.append('**')
        elif tag == 'em' or tag == 'i':
            self.text.append('*')
        elif tag == 'table':
            self.text.append('\n')
        elif tag == 'tr':
            pass
        elif tag == 'td' or tag == 'th':
            self.text.append('| ')

    def handle_endtag(self, tag):
        if tag == 'script' or tag == 'style':
            self.in_script = False
        elif tag == 'pre':
            self.in_pre = False
            self.text.append('\n```\n')
        elif tag == 'code':
            self.in_code = False
            self.text.append('`')
        elif tag in ['h1', 'h2', 'h3', 'h4', 'p']:
            self.text.append('\n')
        elif tag == 'a':
            self.text.append(']')
        elif tag == 'strong' or tag == 'b':
            self.text.append('**')
        elif tag == 'em' or tag == 'i':
            self.text.append('*')
        elif tag == 'td' or tag == 'th':
            self.text.append(' |')
        elif tag == 'tr':
            self.text.append('\n')

    def handle_data(self, data):
        if not self.in_script:
            self.text.append(unescape(data))

    def get_markdown(self):
        """Get the cleaned markdown."""
        content = ''.join(self.text)
        # Clean up excessive whitespace
        content = re.sub(r'\n\n+', '\n\n', content)
        return content.strip()


def fetch_page(url):
    """Fetch a page from the web."""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        return response.text
    except Exception as e:
        print(f"    Error fetching {url}: {e}")
        return None


def convert_to_markdown(html_content):
    """Convert HTML to Markdown."""
    parser = HTMLToMarkdown()
    parser.feed(html_content)
    return parser.get_markdown()


def main():
    """Main scraper function."""
    print("Scraping Sonatype Nexus Repository documentation")

    # Create output directory
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    success_count = 0
    for i, url in enumerate(PAGES_TO_SCRAPE, 1):
        print(f"  [{i}/{len(PAGES_TO_SCRAPE)}] Fetching {url}")

        html_content = fetch_page(url)
        if not html_content:
            continue

        # Convert to markdown
        markdown_content = convert_to_markdown(html_content)

        # Generate filename from URL
        path_parts = url.replace('https://', '').replace('http://', '').replace('.html', '').split('/')
        filename = path_parts[-1] if path_parts[-1] else 'index'
        filename = f"{filename}.md"

        # Write to file
        output_file = OUTPUT_DIR / filename
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(f"# Source: {url}\n\n")
                f.write(markdown_content)
            success_count += 1
            print(f"    -> Saved to {filename}")
        except Exception as e:
            print(f"    -> Error saving file: {e}")

        # Rate limiting
        time.sleep(1)

    print(f"\nSuccessfully scraped {success_count}/{len(PAGES_TO_SCRAPE)} pages")
    print(f"Documentation saved to {OUTPUT_DIR}")

    return success_count > 0


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
