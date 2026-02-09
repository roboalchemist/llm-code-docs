#!/usr/bin/env python3
"""
Datadog API Documentation Crawler using crawl4ai

Deep crawls from the base URL to discover and extract all API docs.
"""

import asyncio
import re
from pathlib import Path

from crawl4ai import AsyncWebCrawler
from crawl4ai.async_configs import BrowserConfig, CrawlerRunConfig
from crawl4ai.deep_crawling import BFSDeepCrawlStrategy
from crawl4ai.deep_crawling.filters import FilterChain, URLPatternFilter

# Output directory
OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "web-scraped" / "datadog-api-v2"
BASE_URL = "https://docs.datadoghq.com/api/latest/"


def url_to_filename(url: str) -> str:
    """Convert URL to a safe filename."""
    path = url.replace(BASE_URL, "").strip("/")
    if not path:
        return "index"
    return re.sub(r'[^a-zA-Z0-9-]', '-', path).lower()


async def crawl_datadog_api():
    """Deep crawl Datadog API docs starting from base URL."""

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    browser_config = BrowserConfig(
        headless=True,
        verbose=True,
    )

    # BFS deep crawl - discovers links and follows them
    deep_crawl = BFSDeepCrawlStrategy(
        max_depth=2,
        include_external=False,
        max_pages=150,
        filter_chain=FilterChain([URLPatternFilter(patterns=["*api/latest/*"])]),
    )

    run_config = CrawlerRunConfig(
        deep_crawl_strategy=deep_crawl,
        wait_until="networkidle",
        page_timeout=60000,
        excluded_tags=["nav", "header", "footer"],
        remove_overlay_elements=True,
    )

    print(f"Starting deep crawl from: {BASE_URL}")
    print(f"Output directory: {OUTPUT_DIR}")

    async with AsyncWebCrawler(config=browser_config) as crawler:
        results = await crawler.arun(url=BASE_URL, config=run_config)

        # Handle single or multiple results
        if not isinstance(results, list):
            results = [results]

        print(f"\nCrawled {len(results)} pages")

        saved = 0
        for result in results:
            if result.success and result.markdown and len(result.markdown) > 500:
                filename = url_to_filename(result.url) + ".md"
                filepath = OUTPUT_DIR / filename

                content = f"# Source: {result.url}\n\n{result.markdown}"
                filepath.write_text(content)
                print(f"  ✓ {filename} ({len(result.markdown):,} chars)")
                saved += 1
            elif result.success:
                print(f"  ⚠ {result.url} - too short ({len(result.markdown or '')} chars)")
            else:
                print(f"  ✗ {result.url} - {result.error_message}")

        print(f"\nSaved {saved} pages to {OUTPUT_DIR}")


if __name__ == "__main__":
    asyncio.run(crawl_datadog_api())
