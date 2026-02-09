#!/usr/bin/env python3
"""
Generic SPA (Single Page Application) scraper using Playwright.

For sites that render content via JavaScript and can't be scraped with requests.
Requires a sitemap.xml to discover pages.

Usage:
    # Scrape all pages from sitemap
    python spa-scraper.py https://example.com/sitemap.xml --output docs/web-scraped/example/

    # Filter to specific path prefix
    python spa-scraper.py https://example.com/sitemap.xml --output docs/web-scraped/example/ --filter "/api/v2"

    # Limit concurrency
    python spa-scraper.py https://example.com/sitemap.xml --output docs/web-scraped/example/ --workers 5

    # Force re-scrape existing files
    python spa-scraper.py https://example.com/sitemap.xml --output docs/web-scraped/example/ --force

Dependencies:
    pip install playwright markdownify
    playwright install chromium
"""

import argparse
import asyncio
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import urlparse

try:
    from playwright.async_api import async_playwright
except ImportError:
    print("Error: playwright not installed. Run: pip install playwright && playwright install chromium")
    sys.exit(1)

try:
    from markdownify import markdownify as md
except ImportError:
    print("Error: markdownify not installed. Run: pip install markdownify")
    sys.exit(1)


def fetch_sitemap(sitemap_url: str) -> list[str]:
    """Fetch and parse sitemap.xml, return list of URLs."""
    result = subprocess.run(
        ['curl', '-sL', sitemap_url],
        capture_output=True, text=True, timeout=30
    )
    if result.returncode != 0:
        raise RuntimeError(f"Failed to fetch sitemap: {result.stderr}")

    urls = re.findall(r'<loc>([^<]+)</loc>', result.stdout)
    if not urls:
        raise RuntimeError(f"No URLs found in sitemap: {sitemap_url}")

    return urls


def url_to_filename(url: str) -> str:
    """Convert URL to safe filename."""
    parsed = urlparse(url)
    path = parsed.path.strip('/')

    if not path:
        return 'index.md'

    # Use last path segment as filename
    slug = path.split('/')[-1]

    # Sanitize
    slug = re.sub(r'[^a-zA-Z0-9_-]', '-', slug)
    slug = re.sub(r'-+', '-', slug).strip('-')

    return f"{slug or 'index'}.md"


def html_to_markdown(html: str) -> str:
    """Convert HTML to clean markdown."""
    markdown = md(
        html,
        heading_style="ATX",
        code_language="",
        strip=['script', 'style', 'nav', 'header', 'footer'],
    )

    # Clean up excessive whitespace
    lines = markdown.split('\n')
    cleaned = []
    prev_empty = False

    for line in lines:
        line = line.rstrip()
        is_empty = not line.strip()
        if is_empty and prev_empty:
            continue
        cleaned.append(line)
        prev_empty = is_empty

    return '\n'.join(cleaned).strip()


async def scrape_page(context, url: str, output_path: Path, force: bool = False) -> str:
    """Scrape a single page, convert to markdown, and save to file."""
    filename = url_to_filename(url)
    filepath = output_path / filename

    if filepath.exists() and not force:
        return f"skip:{filename}"

    page = await context.new_page()
    try:
        await page.goto(url, wait_until="domcontentloaded", timeout=30000)
        await asyncio.sleep(0.5)  # Let JS render

        # Extract main content as HTML, removing navigation elements
        html = await page.evaluate("""() => {
            const selectors = ['main', 'article', '[role="main"]', '.content', '.docs-content'];
            let main = null;
            for (const sel of selectors) {
                main = document.querySelector(sel);
                if (main) break;
            }
            if (!main) main = document.body;

            const clone = main.cloneNode(true);
            clone.querySelectorAll('nav, header, footer, script, style, .sidebar, .navigation, [role="navigation"]').forEach(el => el.remove());
            return clone.innerHTML;
        }""")

        if html and len(html.strip()) > 100:
            content = html_to_markdown(html)

            if content and len(content) > 50:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(f"# {filename.replace('.md', '')}\n\n")
                    f.write(f"Source: {url}\n\n---\n\n")
                    f.write(content)
                return f"ok:{filename}"
        return f"empty:{filename}"

    except Exception as e:
        return f"error:{filename}:{str(e)[:50]}"
    finally:
        await page.close()


async def worker(browser, queue: asyncio.Queue, output_path: Path, worker_id: int, force: bool) -> int:
    """Worker that processes URLs from queue."""
    context = await browser.new_context()
    count = 0
    errors = 0

    while True:
        try:
            url = queue.get_nowait()
        except asyncio.QueueEmpty:
            break

        result = await scrape_page(context, url, output_path, force)
        count += 1

        status = result.split(":")[0]
        if status == "error":
            errors += 1
            print(f"  [W{worker_id}] {result}")
        elif count % 10 == 0:
            print(f"  [W{worker_id}] Processed {count} pages...")

    await context.close()
    return count


async def scrape_sitemap(
    sitemap_url: str,
    output_path: Path,
    filter_prefix: str | None = None,
    workers: int = 10,
    force: bool = False
) -> dict:
    """Scrape all pages from a sitemap."""

    print(f"Fetching sitemap: {sitemap_url}")
    urls = fetch_sitemap(sitemap_url)
    print(f"  Found {len(urls)} URLs")

    # Apply filter if specified
    if filter_prefix:
        urls = [u for u in urls if filter_prefix in u]
        print(f"  Filtered to {len(urls)} URLs matching '{filter_prefix}'")

    if not urls:
        print("No URLs to scrape")
        return {"total": 0, "scraped": 0}

    output_path.mkdir(parents=True, exist_ok=True)

    # Build queue
    queue = asyncio.Queue()
    for url in urls:
        queue.put_nowait(url)

    print(f"Scraping with {workers} workers...")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)

        tasks = [
            worker(browser, queue, output_path, i, force)
            for i in range(min(workers, len(urls)))
        ]
        results = await asyncio.gather(*tasks)

        await browser.close()

    total_processed = sum(results)
    final_count = len(list(output_path.glob("*.md")))

    print(f"\nComplete:")
    print(f"  Processed: {total_processed}")
    print(f"  Files: {final_count}")

    return {"total": len(urls), "scraped": final_count}


def main():
    parser = argparse.ArgumentParser(
        description="Scrape Single Page Applications using Playwright",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s https://docs.example.com/sitemap.xml -o docs/web-scraped/example/
  %(prog)s https://api.example.com/sitemap.xml -o docs/ --filter "/v2/" --workers 5
        """
    )
    parser.add_argument("sitemap_url", help="URL to sitemap.xml")
    parser.add_argument("-o", "--output", required=True, help="Output directory for scraped files")
    parser.add_argument("-f", "--filter", help="Only scrape URLs containing this string")
    parser.add_argument("-w", "--workers", type=int, default=10, help="Number of parallel workers (default: 10)")
    parser.add_argument("--force", action="store_true", help="Re-scrape existing files")

    args = parser.parse_args()

    output_path = Path(args.output)

    asyncio.run(scrape_sitemap(
        sitemap_url=args.sitemap_url,
        output_path=output_path,
        filter_prefix=args.filter,
        workers=args.workers,
        force=args.force
    ))


if __name__ == "__main__":
    main()
