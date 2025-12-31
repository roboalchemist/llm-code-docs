#!/usr/bin/env python3
"""
Storybook Documentation Scraper
Downloads Storybook documentation from storybook.js.org and converts to markdown.
Storybook is a frontend workshop for building UI components and pages in isolation.
"""

import os
import sys
import requests
from pathlib import Path
import time
from bs4 import BeautifulSoup
import html2text

# Base URL for Storybook documentation
BASE_URL = "https://storybook.js.org"

# Documentation pages to scrape
DOC_PAGES = [
    # Get Started
    "/docs/get-started",
    "/docs/get-started/why-storybook",
    "/docs/get-started/install",
    "/docs/get-started/whats-a-story",
    "/docs/get-started/browse-stories",
    "/docs/get-started/setup",
    "/docs/get-started/conclusion",

    # Writing Stories
    "/docs/writing-stories",
    "/docs/writing-stories/args",
    "/docs/writing-stories/parameters",
    "/docs/writing-stories/decorators",
    "/docs/writing-stories/play-function",
    "/docs/writing-stories/loaders",
    "/docs/writing-stories/tags",
    "/docs/writing-stories/naming-components-and-hierarchy",
    "/docs/writing-stories/build-pages-with-storybook",
    "/docs/writing-stories/stories-for-multiple-components",
    "/docs/writing-stories/typescript",

    # Writing Docs
    "/docs/writing-docs",
    "/docs/writing-docs/autodocs",
    "/docs/writing-docs/build-documentation",
    "/docs/writing-docs/code-panel",
    "/docs/writing-docs/doc-blocks",
    "/docs/writing-docs/mdx",

    # Configure
    "/docs/configure",
    "/docs/configure/environment-variables",
    "/docs/configure/story-layout",
    "/docs/configure/story-rendering",
    "/docs/configure/styling-and-css",
    "/docs/configure/telemetry",

    # API
    "/docs/api",
    "/docs/api/arg-types",
    "/docs/api/cli-options",
    "/docs/api/csf",
    "/docs/api/new-frameworks",
    "/docs/api/parameters",

    # Addons
    "/docs/addons",
    "/docs/addons/install-addons",
    "/docs/addons/configure-addons",
    "/docs/addons/addon-types",
    "/docs/addons/writing-addons",
    "/docs/addons/writing-presets",
    "/docs/addons/addons-api",
    "/docs/addons/addon-knowledge-base",
    "/docs/addons/integration-catalog",
    "/docs/addons/addon-migration-guide",

    # Essentials
    "/docs/essentials",
    "/docs/essentials/actions",
    "/docs/essentials/backgrounds",
    "/docs/essentials/controls",
    "/docs/essentials/highlight",
    "/docs/essentials/measure-and-outline",
    "/docs/essentials/toolbars-and-globals",
    "/docs/essentials/viewport",

    # Builders
    "/docs/builders",
    "/docs/builders/vite",
    "/docs/builders/webpack",
    "/docs/builders/builder-api",

    # Writing Tests
    "/docs/writing-tests",
    "/docs/writing-tests/interaction-testing",
    "/docs/writing-tests/visual-testing",
    "/docs/writing-tests/accessibility-testing",
    "/docs/writing-tests/snapshot-testing",
    "/docs/writing-tests/test-coverage",
    "/docs/writing-tests/in-ci",

    # Sharing
    "/docs/sharing",
    "/docs/sharing/publish-storybook",
    "/docs/sharing/embed",
    "/docs/sharing/storybook-composition",
    "/docs/sharing/package-composition",
    "/docs/sharing/design-integrations",

    # Releases
    "/docs/releases",
    "/docs/releases/upgrading",
    "/docs/releases/migration-guide",
    "/docs/releases/migration-guide-from-older-version",
    "/docs/releases/features",
    "/docs/releases/roadmap",

    # Contribute
    "/docs/contribute",
    "/docs/contribute/how-to-reproduce",
    "/docs/contribute/code",
    "/docs/contribute/framework",
    "/docs/contribute/RFC",

    # FAQ
    "/docs/faq",
]


def convert_html_to_markdown(html_content, url):
    """Convert HTML content to clean markdown."""
    try:
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find the main content area (usually in an article or main tag)
        main_content = soup.find('article') or soup.find('main') or soup.find('div', class_='docs-content')

        if not main_content:
            # Fallback: try to find content by common class names
            main_content = soup.find('div', class_=lambda x: x and ('content' in x.lower() or 'docs' in x.lower()))

        if not main_content:
            print(f"    -> Warning: Could not find main content area")
            main_content = soup

        # Remove navigation, headers, footers, and other UI elements
        for element in main_content.find_all(['nav', 'header', 'footer', 'aside']):
            element.decompose()

        # Remove script and style tags
        for element in main_content.find_all(['script', 'style']):
            element.decompose()

        # Convert to markdown
        h = html2text.HTML2Text()
        h.ignore_links = False
        h.ignore_images = False
        h.ignore_emphasis = False
        h.body_width = 0  # Don't wrap text
        h.single_line_break = False

        markdown_content = h.handle(str(main_content))

        return markdown_content.strip()

    except Exception as e:
        print(f"    -> Error converting HTML to markdown: {e}")
        return None


def download_page(page_path, output_dir):
    """Download a documentation page and convert to markdown."""
    try:
        url = f"{BASE_URL}{page_path}"

        print(f"  Downloading: {url}")

        response = requests.get(url, timeout=15)
        response.raise_for_status()

        # Convert HTML to markdown
        markdown_content = convert_html_to_markdown(response.text, url)

        if not markdown_content:
            print(f"    -> Failed to convert content")
            return False

        # Create output filename from path
        # e.g., "/docs/writing-stories/args" -> "writing-stories-args.md"
        filename = page_path.replace("/docs/", "").replace("/", "-")
        if not filename.endswith(".md"):
            filename += ".md"

        output_path = output_dir / filename

        # Add metadata header
        header = f"""# Storybook Documentation
# Source: {url}
# Page: {page_path}

"""

        content = header + markdown_content

        # Write to file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"    -> Saved: {output_path.name} ({len(content):,} bytes)")
        return True

    except requests.exceptions.RequestException as e:
        print(f"    -> Error downloading {page_path}: {e}")
        return False
    except Exception as e:
        print(f"    -> Error processing {page_path}: {e}")
        return False


def main():
    """Main function to download all Storybook documentation."""
    print("=" * 60)
    print("Storybook Documentation Scraper")
    print("=" * 60)
    print()

    # Check if required dependencies are available
    try:
        import bs4
        import html2text
    except ImportError as e:
        print(f"Error: Missing required dependency: {e}")
        print("Please install: pip install beautifulsoup4 html2text")
        sys.exit(1)

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "web-scraped" / "storybook"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Output directory: {output_dir}")
    print(f"Total pages to download: {len(DOC_PAGES)}")
    print()

    successful = 0
    failed = 0
    start_time = time.time()

    for idx, page_path in enumerate(DOC_PAGES, 1):
        print(f"[{idx:3d}/{len(DOC_PAGES)}]", end=" ")

        if download_page(page_path, output_dir):
            successful += 1
        else:
            failed += 1

        # Be respectful with rate limiting
        time.sleep(0.5)

    elapsed = time.time() - start_time

    print()
    print("=" * 60)
    print("Download Summary")
    print("=" * 60)
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    print(f"Time: {elapsed:.1f} seconds")
    print(f"Output: {output_dir}")

    # Calculate total size
    total_size = sum(f.stat().st_size for f in output_dir.glob("*.md") if f.is_file())
    print(f"Total size: {total_size:,} bytes ({total_size/1024:.1f} KB)")

    print()
    if successful == 0:
        print("Error: No files downloaded successfully!")
        sys.exit(1)
    elif failed > successful:
        print(f"Warning: More failures ({failed}) than successes ({successful})")
        sys.exit(1)
    else:
        print(f"Documentation downloaded successfully! ({successful} files)")
        sys.exit(0)


if __name__ == "__main__":
    main()
