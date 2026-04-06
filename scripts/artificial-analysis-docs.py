#!/usr/bin/env python3
"""
Fetch Artificial Analysis API documentation.
Converts HTML to markdown using basic text extraction.
"""

import sys
from pathlib import Path
from urllib.request import urlopen, Request
from urllib.error import URLError
from html.parser import HTMLParser
import re


class HTMLToMarkdown(HTMLParser):
    """Simple HTML to Markdown converter."""

    def __init__(self):
        super().__init__()
        self.markdown = []
        self.in_script = False
        self.in_style = False
        self.current_tag = None
        self.code_block = False
        self.list_level = 0

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)

        if tag == "script" or tag == "style":
            self.in_script = True
        elif tag == "h1":
            self.markdown.append("\n# ")
        elif tag == "h2":
            self.markdown.append("\n## ")
        elif tag == "h3":
            self.markdown.append("\n### ")
        elif tag == "h4":
            self.markdown.append("\n#### ")
        elif tag == "h5":
            self.markdown.append("\n##### ")
        elif tag == "p":
            self.markdown.append("\n")
        elif tag == "br":
            self.markdown.append("\n")
        elif tag == "hr":
            self.markdown.append("\n---\n")
        elif tag == "strong" or tag == "b":
            self.markdown.append("**")
        elif tag == "em" or tag == "i":
            self.markdown.append("*")
        elif tag == "code":
            self.markdown.append("`")
        elif tag == "pre":
            self.code_block = True
            lang = attrs_dict.get("class", "").replace("language-", "")
            self.markdown.append(f"\n```{lang}\n")
        elif tag == "a":
            href = attrs_dict.get("href", "")
            self.markdown.append("[")
            self.current_tag = ("a", href)
        elif tag == "ul":
            self.list_level += 1
        elif tag == "ol":
            self.list_level += 1
        elif tag == "li":
            self.markdown.append("  " * (self.list_level - 1) + "- ")
        elif tag == "table":
            self.markdown.append("\n| ")
        elif tag == "tr":
            pass
        elif tag == "th" or tag == "td":
            self.markdown.append(" | ")
        elif tag == "blockquote":
            self.markdown.append("\n> ")

    def handle_endtag(self, tag):
        if tag == "script" or tag == "style":
            self.in_script = False
        elif tag == "h1" or tag == "h2" or tag == "h3" or tag == "h4" or tag == "h5":
            self.markdown.append("\n")
        elif tag == "p":
            self.markdown.append("\n")
        elif tag == "strong" or tag == "b":
            self.markdown.append("**")
        elif tag == "em" or tag == "i":
            self.markdown.append("*")
        elif tag == "code":
            self.markdown.append("`")
        elif tag == "pre":
            self.code_block = False
            self.markdown.append("\n```\n")
        elif tag == "a":
            if self.current_tag and self.current_tag[0] == "a":
                self.markdown.append(f"]({self.current_tag[1]})")
                self.current_tag = None
        elif tag == "ul" or tag == "ol":
            self.list_level = max(0, self.list_level - 1)
        elif tag == "li":
            self.markdown.append("\n")
        elif tag == "tr":
            self.markdown.append("|\n")
        elif tag == "blockquote":
            self.markdown.append("\n")

    def handle_data(self, data):
        if not self.in_script:
            text = data.strip()
            if text:
                self.markdown.append(text)

    def get_markdown(self):
        return "".join(self.markdown)


def fetch_url(url, timeout=15):
    """Fetch URL content."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36"
    }
    req = Request(url, headers=headers)
    try:
        with urlopen(req, timeout=timeout) as response:
            return response.read().decode("utf-8", errors="ignore")
    except URLError as e:
        print(f"✗ Failed to fetch {url}: {e}")
        return None


def fetch_api_docs():
    """Fetch Artificial Analysis API reference documentation."""

    OUT = Path("docs/artificial-analysis/web")
    OUT.mkdir(parents=True, exist_ok=True)

    base_url = "https://artificialanalysis.ai"
    main_url = f"{base_url}/api-reference"

    print(f"Fetching {main_url}...")
    html = fetch_url(main_url)

    if not html:
        print("ERROR: Failed to fetch main page")
        return False

    # Convert HTML to markdown
    converter = HTMLToMarkdown()
    converter.feed(html)
    markdown = converter.get_markdown()

    # Clean up markdown
    markdown = re.sub(r"\n\n\n+", "\n\n", markdown)  # Multiple newlines
    markdown = re.sub(r"^\s+", "", markdown, flags=re.MULTILINE)  # Leading whitespace

    # Save main page
    output_file = OUT / "api-reference.md"
    output_file.write_text(markdown)
    print(f"✓ Saved: {output_file} ({len(markdown)} bytes)")

    # Extract links to other API pages from the HTML
    # Look for common API endpoint patterns
    urls_to_fetch = set()

    # Common API reference sections
    common_sections = [
        "/api-reference/authentication",
        "/api-reference/endpoints",
        "/api-reference/models",
        "/api-reference/leaderboards",
        "/api-reference/benchmarks",
        "/api-reference/providers",
        "/api-reference/errors",
    ]

    for section in common_sections:
        urls_to_fetch.add(f"{base_url}{section}")

    # Try to extract links from the HTML itself
    link_pattern = r'href=["\']([^"\']*api[^"\']*)["\']'
    for match in re.finditer(link_pattern, html):
        href = match.group(1)
        if href.startswith("/"):
            urls_to_fetch.add(f"{base_url}{href}")
        elif href.startswith("http"):
            if "artificialanalysis.ai" in href:
                urls_to_fetch.add(href)

    # Fetch additional pages
    fetched_count = 0
    for url in sorted(urls_to_fetch):
        if url == main_url:
            continue
        if fetched_count >= 10:  # Limit to 10 additional pages
            break

        print(f"Fetching {url}...")
        html = fetch_url(url)
        if html:
            converter = HTMLToMarkdown()
            converter.feed(html)
            markdown = converter.get_markdown()

            # Generate safe filename from URL
            path_part = (
                url.replace(f"{base_url}/", "")
                .replace("/", "_")
                .replace("-", "_")
                .replace("?", "_")
            )
            if not path_part:
                path_part = "index"

            output_file = OUT / f"{path_part}.md"
            output_file.write_text(markdown)
            print(f"✓ Saved: {output_file} ({len(markdown)} bytes)")
            fetched_count += 1
        else:
            print(f"✗ Skipped: {url}")

    print(f"\nFetched {fetched_count + 1} pages total")
    return True


if __name__ == "__main__":
    success = fetch_api_docs()
    sys.exit(0 if success else 1)
