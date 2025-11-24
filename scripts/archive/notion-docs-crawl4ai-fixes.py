#!/usr/bin/env /Users/joe/miniconda3/bin/python
"""
Notion API Documentation Fixes Extractor using Crawl4AI
Re-extracts problematic files with improved wait times and validation
"""

import asyncio
import os
import sys
from pathlib import Path
from datetime import datetime
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode

# Problematic files to re-extract (from QA report)
PROBLEMATIC_FILES = {
    # Empty files (CRITICAL)
    'revoke-token': 'https://developers.notion.com/reference/revoke-token',
    'introspect-token': 'https://developers.notion.com/reference/introspect-token',
    'list-file-uploads': 'https://developers.notion.com/reference/list-file-uploads',
    'complete-a-file-upload': 'https://developers.notion.com/reference/complete-a-file-upload',
    'retrieve-a-file-upload': 'https://developers.notion.com/reference/retrieve-a-file-upload',

    # Severely undersized critical files (HIGH PRIORITY)
    'block': 'https://developers.notion.com/reference/block',
    'page': 'https://developers.notion.com/reference/page',
    'database': 'https://developers.notion.com/reference/database',
    'create-a-data-source': 'https://developers.notion.com/reference/create-a-data-source',
    'create-a-file-upload': 'https://developers.notion.com/reference/create-a-file-upload',
    'refresh-a-token': 'https://developers.notion.com/reference/refresh-a-token',
    'get-user': 'https://developers.notion.com/reference/get-user',

    # Suspicious undersized files (MEDIUM PRIORITY)
    'database-update': 'https://developers.notion.com/reference/database-update',
    'retrieve-comment': 'https://developers.notion.com/reference/retrieve-comment',
    'get-self': 'https://developers.notion.com/reference/get-self',
}

# Expected minimum sizes for validation
EXPECTED_SIZES = {
    'block': 100 * 1024,  # >100KB
    'page': 15 * 1024,    # >15KB
    'database': 15 * 1024, # >15KB
    'create-a-data-source': 4 * 1024,  # >4KB
    'create-a-file-upload': 3 * 1024,  # >3KB
    'revoke-token': 2 * 1024,  # >2KB
    'introspect-token': 2 * 1024,  # >2KB
    'list-file-uploads': 3 * 1024,  # >3KB
    'complete-a-file-upload': 3 * 1024,  # >3KB
    'retrieve-a-file-upload': 3 * 1024,  # >3KB
    'refresh-a-token': 2 * 1024,  # >2KB
    'get-user': 2 * 1024,  # >2KB
    'database-update': 2 * 1024,  # >2KB
    'retrieve-comment': 2 * 1024,  # >2KB
    'get-self': 2 * 1024,  # >2KB
}

SCRIPT_DIR = Path(__file__).parent
OUTPUT_DIR = SCRIPT_DIR.parent / "notion"

async def extract_page_with_retry(crawler, slug, url, output_path, max_retries=3):
    """Extract a single page with retry logic and validation."""

    for attempt in range(max_retries):
        try:
            if attempt > 0:
                print(f"  Retry {attempt}/{max_retries-1}...")
                await asyncio.sleep(3)  # Wait before retry

            print(f"  Extracting: {url}")

            # Configure extraction with longer waits
            config = CrawlerRunConfig(
                cache_mode=CacheMode.BYPASS,
                # CSS selector to target main content
                css_selector="article#content",
                # Remove navigation and UI elements
                excluded_tags=['nav', 'header', 'footer', 'aside', 'script', 'style'],
                # Wait for page to fully load with longer timeout
                wait_for="css:article#content",
                # Additional wait time for dynamic content
                page_timeout=30000,  # 30 seconds timeout
                # Add JavaScript execution to expand collapsible sections
                js_code=[
                    # Wait for page to be fully loaded
                    "await new Promise(resolve => setTimeout(resolve, 3000));",

                    # Expand all details/summary elements (collapsible sections)
                    "document.querySelectorAll('details:not([open])').forEach(d => d.open = true);",

                    # Click any "Show more" or expand buttons
                    "document.querySelectorAll('button').forEach(btn => {",
                    "  const text = btn.textContent.toLowerCase();",
                    "  if (text.includes('show') || text.includes('expand') || text.includes('more')) {",
                    "    btn.click();",
                    "  }",
                    "});",

                    # Scroll to bottom to trigger lazy loading
                    "window.scrollTo(0, document.body.scrollHeight);",

                    # Wait for any animations/lazy loading
                    "await new Promise(resolve => setTimeout(resolve, 2000));",

                    # Scroll back to top
                    "window.scrollTo(0, 0);",

                    # Final wait for content stabilization
                    "await new Promise(resolve => setTimeout(resolve, 1000));",
                ]
            )

            result = await crawler.arun(url=url, config=config)

            if result.success:
                # Get the markdown content
                markdown_content = result.markdown_v2.raw_markdown if hasattr(result, 'markdown_v2') else result.markdown

                # Validate content is not empty
                if not markdown_content or len(markdown_content.strip()) < 100:
                    print(f"    ⚠ Warning: Extracted content too short ({len(markdown_content)} chars)")
                    if attempt < max_retries - 1:
                        continue
                    else:
                        print(f"    ✗ Failed: Content still too short after {max_retries} attempts")
                        return False, 0

                # Add source header
                final_content = f"# Source: {url}\n\n{markdown_content}"

                # Save to file
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(final_content)

                file_size = output_path.stat().st_size

                # Validate against expected size
                expected_size = EXPECTED_SIZES.get(slug, 500)  # Default 500 bytes minimum
                if file_size < expected_size:
                    print(f"    ⚠ Warning: File size {file_size:,} bytes < expected {expected_size:,} bytes")
                    if attempt < max_retries - 1:
                        print(f"    ↻ Retrying to get more complete content...")
                        continue
                    else:
                        print(f"    ⚠ Saving anyway after {max_retries} attempts")

                print(f"    ✓ Saved: {output_path.name} ({file_size:,} bytes)")
                return True, file_size
            else:
                error_msg = result.error_message if hasattr(result, 'error_message') else 'Unknown error'
                print(f"    ✗ Failed: {error_msg}")
                if attempt < max_retries - 1:
                    continue
                return False, 0

        except Exception as e:
            print(f"    ✗ Error: {str(e)}")
            if attempt < max_retries - 1:
                continue
            return False, 0

    return False, 0

async def main():
    """Main extraction function."""
    print("=" * 80)
    print("Notion API Documentation Fixes Extraction (Crawl4AI)")
    print("=" * 80)
    print(f"\nRe-extracting {len(PROBLEMATIC_FILES)} problematic files")
    print(f"Output directory: {OUTPUT_DIR}")

    # Create output directory if needed
    OUTPUT_DIR.mkdir(exist_ok=True)

    # Statistics
    successful = 0
    failed = 0
    improved = 0
    total_size = 0
    results = []

    # Extract pages
    print("\n" + "-" * 80)

    async with AsyncWebCrawler(verbose=False) as crawler:
        for i, (slug, url) in enumerate(PROBLEMATIC_FILES.items(), 1):
            output_path = OUTPUT_DIR / f"{slug}.md"

            # Store old size for comparison
            old_size = 0
            if output_path.exists():
                old_size = output_path.stat().st_size

            print(f"\n[{i}/{len(PROBLEMATIC_FILES)}] {slug}")
            if old_size > 0:
                print(f"  Previous size: {old_size:,} bytes")

            success, new_size = await extract_page_with_retry(crawler, slug, url, output_path)

            if success:
                successful += 1
                total_size += new_size

                if new_size > old_size:
                    improved += 1
                    improvement = ((new_size - old_size) / old_size * 100) if old_size > 0 else float('inf')
                    if improvement == float('inf'):
                        print(f"  ↑ New content: {new_size:,} bytes (was empty)")
                    else:
                        print(f"  ↑ Improved: {new_size:,} bytes (+{improvement:.1f}%)")

                results.append((slug, True, new_size, old_size))
            else:
                failed += 1
                results.append((slug, False, 0, old_size))

            # Delay between requests to avoid overwhelming server
            await asyncio.sleep(1)

    # Summary
    print("\n" + "=" * 80)
    print("Extraction Complete")
    print("=" * 80)
    print(f"Successful: {successful}/{len(PROBLEMATIC_FILES)}")
    print(f"Failed: {failed}/{len(PROBLEMATIC_FILES)}")
    print(f"Improved: {improved}/{len(PROBLEMATIC_FILES)}")
    print(f"Total size: {total_size:,} bytes ({total_size/1024/1024:.2f} MB)")
    if successful > 0:
        print(f"Average size: {total_size//successful:,} bytes per file")

    # Detailed results
    print("\n" + "-" * 80)
    print("DETAILED RESULTS")
    print("-" * 80)

    for slug, success, new_size, old_size in results:
        status = "✓" if success else "✗"
        expected = EXPECTED_SIZES.get(slug, 500)
        size_ok = "✓" if new_size >= expected else "⚠"

        if success:
            if old_size > 0:
                change = new_size - old_size
                change_pct = (change / old_size * 100) if old_size > 0 else 0
                print(f"{status} {slug:30s} {size_ok} {new_size:8,} bytes (was {old_size:8,}, {change:+,} bytes, {change_pct:+.1f}%)")
            else:
                print(f"{status} {slug:30s} {size_ok} {new_size:8,} bytes (was EMPTY)")
        else:
            print(f"{status} {slug:30s} ✗ FAILED")

    print("=" * 80)

    return 0 if failed == 0 else 1

if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
