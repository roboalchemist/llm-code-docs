#!/usr/bin/env python3
"""
SWC Documentation Scraper
Downloads and converts SWC documentation from https://swc.rs to markdown format.
SWC is a super-fast Rust-based JavaScript/TypeScript compiler with integrated linting.
Output: docs/web-scraped/swc/
"""

import requests
from pathlib import Path
import time
import sys
from typing import List, Tuple
import re
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse

# Configuration
BASE_URL = "https://swc.rs"
REQUEST_TIMEOUT = 15
REQUEST_DELAY = 0.5  # seconds between requests
OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "web-scraped" / "swc"

# Key documentation pages to scrape (discovered from site navigation)
DOCUMENTATION_PAGES = [
    "/docs/getting-started",
    "/docs/usage/cli",
    "/docs/usage/core",
    "/docs/usage/wasm",
    "/docs/usage/jest",
    "/docs/usage/swc-loader",
    "/docs/usage/html",
    "/docs/usage/bundling",
    "/docs/configuration/swcrc",
    "/docs/configuration/supported-browsers",
    "/docs/configuration/modules",
    "/docs/configuration/minification",
    "/docs/configuration/bundling",
    "/docs/plugin/selecting-swc-core",
    "/docs/plugin/ecmascript/getting-started",
    "/docs/plugin/ecmascript/cheatsheet",
    "/docs/plugin/ecmascript/compatibility",
    "/docs/plugin/publishing",
]


class HTMLToMarkdownConverter(HTMLParser):
    """Simple HTML to Markdown converter for documentation."""

    def __init__(self):
        super().__init__()
        self.markdown = []
        self.current_section = []
        self.in_pre = False
        self.in_code = False
        self.in_strong = False
        self.in_em = False
        self.in_h1 = False
        self.in_h2 = False
        self.in_h3 = False
        self.in_h4 = False
        self.in_li = False
        self.in_p = False
        self.list_depth = 0
        self.skip_content = False

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)

        # Skip navigation and UI elements
        if tag in ["nav", "header", "footer"]:
            self.skip_content = True
        elif tag == "main":
            self.skip_content = False
        elif self.skip_content:
            return

        if tag == "h1":
            self.in_h1 = True
        elif tag == "h2":
            if self.current_section:
                self.markdown.append("\n".join(self.current_section))
                self.current_section = []
            self.in_h2 = True
        elif tag == "h3":
            self.in_h3 = True
        elif tag == "h4":
            self.in_h4 = True
        elif tag == "p":
            self.in_p = True
        elif tag == "pre":
            self.in_pre = True
            self.current_section.append("```")
        elif tag == "code" and not self.in_pre:
            self.in_code = True
            self.current_section.append("`")
        elif tag == "strong" or tag == "b":
            self.in_strong = True
            self.current_section.append("**")
        elif tag == "em" or tag == "i":
            self.in_em = True
            self.current_section.append("*")
        elif tag == "ul" or tag == "ol":
            self.list_depth += 1
        elif tag == "li":
            indent = "  " * (self.list_depth - 1)
            self.current_section.append(f"{indent}- ")
            self.in_li = True
        elif tag == "a":
            href = attrs_dict.get("href", "#")
            if href and not href.startswith("javascript:"):
                self.current_section.append("[")
        elif tag == "br":
            self.current_section.append("\n")
        elif tag == "img":
            alt = attrs_dict.get("alt", "image")
            src = attrs_dict.get("src", "#")
            self.current_section.append(f"![{alt}]({src})")
        elif tag == "table":
            self.current_section.append("\n")
        elif tag == "tr":
            pass
        elif tag == "td" or tag == "th":
            self.current_section.append("| ")
        elif tag == "blockquote":
            self.current_section.append("> ")

    def handle_endtag(self, tag):
        if self.skip_content and tag not in ["nav", "header", "footer", "main"]:
            return

        if tag == "h1":
            if self.current_section:
                self.markdown.append("# " + "".join(self.current_section))
                self.current_section = []
            self.in_h1 = False
        elif tag == "h2":
            if self.current_section:
                self.markdown.append("## " + "".join(self.current_section))
                self.current_section = []
            self.in_h2 = False
        elif tag == "h3":
            if self.current_section:
                self.markdown.append("### " + "".join(self.current_section))
                self.current_section = []
            self.in_h3 = False
        elif tag == "h4":
            if self.current_section:
                self.markdown.append("#### " + "".join(self.current_section))
                self.current_section = []
            self.in_h4 = False
        elif tag == "p":
            if self.current_section:
                text = "".join(self.current_section).strip()
                if text:
                    self.markdown.append(text)
                self.current_section = []
            self.in_p = False
        elif tag == "pre":
            self.in_pre = False
            self.current_section.append("```")
            self.markdown.append("".join(self.current_section))
            self.current_section = []
        elif tag == "code" and not self.in_pre:
            self.in_code = False
            self.current_section.append("`")
        elif tag == "strong" or tag == "b":
            self.in_strong = False
            self.current_section.append("**")
        elif tag == "em" or tag == "i":
            self.in_em = False
            self.current_section.append("*")
        elif tag == "ul" or tag == "ol":
            self.list_depth -= 1
            self.markdown.append("\n".join(self.current_section))
            self.current_section = []
        elif tag == "li":
            self.in_li = False
            self.markdown.append("".join(self.current_section))
            self.current_section = []
        elif tag == "a":
            self.current_section.append("]")
            # The href should be handled, but we'll leave simple reference
        elif tag == "table":
            self.markdown.append("".join(self.current_section))
            self.current_section = []
        elif tag == "tr":
            self.current_section.append("|\n")
        elif tag == "td" or tag == "th":
            self.current_section.append(" |")
        elif tag == "blockquote":
            self.markdown.append("".join(self.current_section))
            self.current_section = []

    def handle_data(self, data):
        if self.skip_content:
            return
        # Clean up whitespace but preserve intentional spaces
        text = data.strip()
        if text:
            self.current_section.append(text + " ")

    def handle_entityref(self, name):
        if not self.skip_content:
            # Convert common HTML entities
            entities = {
                "nbsp": " ",
                "lt": "<",
                "gt": ">",
                "amp": "&",
                "quot": '"',
                "apos": "'",
            }
            self.current_section.append(entities.get(name, f"&{name};"))

    def get_markdown(self):
        if self.current_section:
            self.markdown.append("".join(self.current_section))
        return "\n".join(self.markdown)


def clean_markdown(text: str) -> str:
    """Clean up markdown text."""
    # Remove excessive blank lines
    text = re.sub(r"\n\n\n+", "\n\n", text)
    # Fix markdown formatting issues
    text = re.sub(r"\*\* +", "**", text)
    text = re.sub(r" +\*\*", "**", text)
    # Remove trailing whitespace on lines
    lines = [line.rstrip() for line in text.split("\n")]
    return "\n".join(lines)


def extract_text_content(html: str, page_url: str) -> str:
    """Extract meaningful text content from HTML using simple parsing."""
    # Remove script and style tags
    html = re.sub(r"<script[^>]*>.*?</script>", "", html, flags=re.DOTALL)
    html = re.sub(r"<style[^>]*>.*?</style>", "", html, flags=re.DOTALL)

    # Extract main content div
    main_match = re.search(r"<main[^>]*>(.*?)</main>", html, re.DOTALL)
    if main_match:
        html = main_match.group(1)

    # Use HTML parser for conversion
    converter = HTMLToMarkdownConverter()
    try:
        converter.feed(html)
    except Exception as e:
        print(f"    Warning: Error parsing HTML: {e}")

    content = converter.get_markdown()
    content = clean_markdown(content)

    return content


def download_page(url: str, output_dir: Path) -> bool:
    """Download a single documentation page and convert to markdown."""
    try:
        print(f"  Downloading: {url}")

        # Use requests with automatic decompression for brotli
        response = requests.get(url, timeout=REQUEST_TIMEOUT, headers={
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36",
            "Accept-Encoding": "gzip, deflate"  # Skip brotli to avoid encoding issues
        })
        response.raise_for_status()

        # Extract page title and content
        html = response.text
        page_title = "SWC Documentation"

        # Try to extract title from HTML
        title_match = re.search(r"<title[^>]*>([^<]+)</title>", html)
        if title_match:
            page_title = title_match.group(1).split("|")[0].strip()

        # Extract content
        content = extract_text_content(html, url)

        # Add metadata header
        header = f"""# Source: {url}

"""

        content = header + content

        # Create output filename from URL path
        path_parts = urlparse(url).path.strip("/").split("/")
        if path_parts:
            filename = "-".join(path_parts) + ".md"
        else:
            filename = "index.md"

        output_path = output_dir / filename

        # Write file
        output_dir.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"    -> Saved: {filename}")
        return True

    except requests.exceptions.RequestException as e:
        print(f"    -> Error downloading {url}: {e}")
        return False
    except Exception as e:
        print(f"    -> Error processing {url}: {e}")
        return False


def main():
    """Main function to download SWC documentation."""
    print("=" * 70)
    print("SWC Documentation Scraper")
    print("=" * 70)
    print()

    print(f"Base URL: {BASE_URL}")
    print(f"Output directory: {OUTPUT_DIR}")
    print()

    # Create output directory
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    start_time = time.time()
    successful = 0
    failed = 0

    print(f"Downloading {len(DOCUMENTATION_PAGES)} documentation pages...")
    print()

    for page_path in DOCUMENTATION_PAGES:
        url = urljoin(BASE_URL, page_path)
        if download_page(url, OUTPUT_DIR):
            successful += 1
        else:
            failed += 1
        time.sleep(REQUEST_DELAY)

    elapsed = time.time() - start_time

    print()
    print("=" * 70)
    print("Download Summary")
    print("=" * 70)
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    print(f"Total: {successful + failed}")
    print(f"Time: {elapsed:.1f} seconds")
    print()

    # Calculate total size
    if OUTPUT_DIR.exists():
        md_files = list(OUTPUT_DIR.glob("*.md"))
        total_size = sum(f.stat().st_size for f in md_files)
        print(f"Files created: {len(md_files)}")
        print(f"Total size: {total_size:,} bytes ({total_size / 1024:.1f} KB)")
    else:
        print("Error: Output directory was not created")

    print(f"Output: {OUTPUT_DIR}")
    print()

    if failed > 0:
        print(f"Warning: {failed} pages failed to download")
        return 1
    else:
        print("All documentation downloaded successfully!")
        return 0


if __name__ == "__main__":
    sys.exit(main())
