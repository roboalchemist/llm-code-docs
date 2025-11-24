#!/Users/joe/miniconda3/bin/python3
"""
Perplexity API Documentation Test Extractor using Crawl4AI
Tests extraction on 3 sample URLs before full extraction
"""

import asyncio
import sys
from pathlib import Path
from crawl4ai import AsyncWebCrawler, CrawlerRunConfig, CacheMode

# Paths
SCRIPT_DIR = Path(__file__).parent
OUTPUT_DIR = SCRIPT_DIR.parent / "perplexity"

# Test URLs: beginning, middle, end of the list
TEST_URLS = [
    "https://docs.perplexity.ai/getting-started/overview",  # First section
    "https://docs.perplexity.ai/guides/search-quickstart",   # Middle section
    "https://docs.perplexity.ai/api-reference/search-post",  # API reference
]

def url_to_filename(url):
    """Convert URL to filename using path segments."""
    # Extract path from URL
    path = url.replace("https://docs.perplexity.ai/", "")
    # Convert slashes to hyphens
    filename = path.replace("/", "-") + ".md"
    return filename

async def extract_page(crawler, url, output_path):
    """Extract a single page using Crawl4AI."""
    try:
        print(f"  Extracting: {url}")

        # Configure extraction
        config = CrawlerRunConfig(
            cache_mode=CacheMode.BYPASS,
            # CSS selector to target main content (from research)
            css_selector=".mdx-content",
            # Remove navigation and UI elements
            excluded_tags=['nav', 'header', 'footer', 'aside', 'script', 'style'],
            # Wait for page to fully load
            wait_for="css:.mdx-content"
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
            error_msg = result.error_message if hasattr(result, 'error_message') else 'Unknown error'
            print(f"    ✗ Failed: {error_msg}")
            return False, 0

    except Exception as e:
        print(f"    ✗ Error: {str(e)}")
        return False, 0

async def main():
    """Main test extraction function."""
    print("=" * 60)
    print("Perplexity Documentation Test Extraction (Crawl4AI)")
    print("=" * 60)
    print(f"\nTesting {len(TEST_URLS)} sample URLs")

    # Create output directory if needed
    OUTPUT_DIR.mkdir(exist_ok=True)

    # Statistics
    successful = 0
    failed = 0
    total_size = 0

    # Extract test pages
    print(f"\nExtracting to: {OUTPUT_DIR}")
    print("-" * 60)

    async with AsyncWebCrawler() as crawler:
        for i, url in enumerate(TEST_URLS, 1):
            # Generate filename from URL
            filename = url_to_filename(url)
            output_path = OUTPUT_DIR / filename

            print(f"[{i}/{len(TEST_URLS)}] {filename}")

            success, size = await extract_page(crawler, url, output_path)

            if success:
                successful += 1
                total_size += size
            else:
                failed += 1

            # Small delay between requests
            await asyncio.sleep(0.3)

    # Summary
    print("\n" + "=" * 60)
    print("Test Extraction Complete")
    print("=" * 60)
    print(f"Successful: {successful}/{len(TEST_URLS)}")
    print(f"Failed: {failed}/{len(TEST_URLS)}")
    print(f"Total size: {total_size:,} bytes ({total_size/1024:.2f} KB)")
    if successful > 0:
        print(f"Average size: {total_size//successful:,} bytes per file")
    print("=" * 60)

    return 0 if failed == 0 else 1

if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
