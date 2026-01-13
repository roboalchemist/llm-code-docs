#!/usr/bin/env python3
"""
Scraper for AccessLint documentation.
Output: docs/web-scraped/accesslint/

Scrapes the help documentation from accesslint.com/help
"""
import requests
from pathlib import Path
import re
import html2text

OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "web-scraped" / "accesslint"

# Help pages to scrape
HELP_PAGES = [
    "/help/install-accesslint",
    "/help/github-permissions",
    "/help/what-is-covered",
    "/help/supported-file-types",
    "/help/change-or-cancel-plan",
]


def extract_content_from_html(html):
    """Extract the main content section from HTML."""
    # Find the s-long-form-content div which contains the actual content
    match = re.search(
        r'<div class="s-long-form-content">(.*?)</main>',
        html,
        re.DOTALL
    )
    if match:
        return match.group(1)
    return None


def html_to_markdown(html_content):
    """Convert HTML to Markdown using html2text."""
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.body_width = 0  # Don't wrap lines

    markdown = h.handle(html_content)

    # Clean up excessive whitespace
    markdown = re.sub(r'\n\n+', '\n\n', markdown)

    # Remove the back link if present
    markdown = re.sub(r'\[Help\]\(/help\)\n+', '', markdown)

    return markdown.strip()


def scrape_page(url, page_name):
    """Scrape a single help page and return markdown."""
    try:
        print(f"  Fetching {page_name}...")
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        # Extract main content
        content = extract_content_from_html(response.text)
        if not content:
            print(f"    Warning: No content found")
            return None

        # Convert to markdown
        markdown = html_to_markdown(content)

        if not markdown:
            print(f"    Warning: No content extracted")
            return None

        print(f"    Success")
        return markdown
    except Exception as e:
        print(f"    Error: {e}")
        return None


def main():
    """Main scraper function."""
    # Create output directory
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print(f"Scraping AccessLint documentation to {OUTPUT_DIR}")

    # Scrape main help page
    print("\nFetching main help page...")
    try:
        response = requests.get("https://accesslint.com/help", timeout=10)
        response.raise_for_status()

        # Extract the list of help links
        main_content = extract_content_from_html(response.text)
        if main_content:
            markdown = html_to_markdown(main_content)
            # Add source header
            content_with_source = f"# Source: https://accesslint.com/help\n\n{markdown}"
            help_file = OUTPUT_DIR / "index.md"
            help_file.write_text(content_with_source)
            print("  Success")
    except Exception as e:
        print(f"  Error: {e}")

    # Scrape individual help pages
    print("\nFetching individual help pages...")
    for page_url in HELP_PAGES:
        full_url = f"https://accesslint.com{page_url}"
        page_name = page_url.split("/")[-1]

        content = scrape_page(full_url, page_name)
        if content:
            # Add source header
            content_with_source = f"# Source: {full_url}\n\n{content}"

            output_file = OUTPUT_DIR / f"{page_name}.md"
            output_file.write_text(content_with_source)

    print(f"\nDone! Documentation saved to {OUTPUT_DIR}")
    print(f"Files created: {len(list(OUTPUT_DIR.glob('*.md')))}")


if __name__ == "__main__":
    main()
