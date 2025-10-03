#!/usr/bin/env /Users/joe/miniconda3/bin/python
"""
Notion API Documentation Extractor using Crawl4AI
Extracts complete documentation including JavaScript-rendered content
"""

import asyncio
import os
import sys
from pathlib import Path
from datetime import datetime
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode

# Read URLs from links file
SCRIPT_DIR = Path(__file__).parent
LINKS_FILE = SCRIPT_DIR / "notion-api-links.txt"
OUTPUT_DIR = SCRIPT_DIR.parent / "notion"

def load_urls():
    """Load URLs from the links file."""
    urls = []
    with open(LINKS_FILE, 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                urls.append(line)
    return urls

async def extract_page(crawler, url, output_path):
    """Extract a single page using Crawl4AI."""
    try:
        print(f"  Extracting: {url}")

        # Configure extraction
        config = CrawlerRunConfig(
            cache_mode=CacheMode.BYPASS,
            # CSS selector to target main content
            css_selector="article#content",
            # Remove navigation and UI elements
            excluded_tags=['nav', 'header', 'footer', 'aside', 'script', 'style'],
            # Wait for page to fully load
            wait_for="css:article#content"
        )

        result = await crawler.arun(url=url, config=config)

        if result.success:
            # Get the markdown content
            markdown_content = result.markdown_v2.raw_markdown if hasattr(result, 'markdown_v2') else result.markdown

            # Add source header
            final_content = f"# Source: {url}\n\n{markdown_content}"

            # Save to file
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(final_content)

            file_size = output_path.stat().st_size
            print(f"    ✓ Saved: {output_path.name} ({file_size:,} bytes)")
            return True, file_size
        else:
            print(f"    ✗ Failed: {result.error_message if hasattr(result, 'error_message') else 'Unknown error'}")
            return False, 0

    except Exception as e:
        print(f"    ✗ Error: {str(e)}")
        return False, 0

async def main():
    """Main extraction function."""
    print("=" * 60)
    print("Notion API Documentation Extraction (Crawl4AI)")
    print("=" * 60)

    # Load URLs
    urls = load_urls()
    print(f"\nLoaded {len(urls)} URLs from {LINKS_FILE.name}")

    # Create output directory if needed
    OUTPUT_DIR.mkdir(exist_ok=True)

    # Statistics
    successful = 0
    failed = 0
    total_size = 0

    # Extract pages
    print(f"\nExtracting to: {OUTPUT_DIR}")
    print("-" * 60)

    async with AsyncWebCrawler() as crawler:
        for i, url in enumerate(urls, 1):
            # Extract page slug from URL
            slug = url.rstrip('/').split('/')[-1]
            output_path = OUTPUT_DIR / f"{slug}.md"

            print(f"[{i}/{len(urls)}] {slug}")

            success, size = await extract_page(crawler, url, output_path)

            if success:
                successful += 1
                total_size += size
            else:
                failed += 1

            # Small delay to avoid overwhelming the server
            await asyncio.sleep(0.3)

    # Summary
    print("\n" + "=" * 60)
    print("Extraction Complete")
    print("=" * 60)
    print(f"Successful: {successful}/{len(urls)}")
    print(f"Failed: {failed}/{len(urls)}")
    print(f"Total size: {total_size:,} bytes ({total_size/1024/1024:.2f} MB)")
    if successful > 0:
        print(f"Average size: {total_size//successful:,} bytes per file")
    print("=" * 60)

    return 0 if failed == 0 else 1

if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
