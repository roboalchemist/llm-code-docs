#!/usr/bin/env python3
"""
Scraper for Ubiquiti UniFi API documentation.

Scrapes the developer portal at https://developer.ui.com/ which is a
Single Page Application requiring Playwright to render.

Also downloads the community-maintained OpenAPI spec from:
https://github.com/ubiquiti-community/unifi-api

Output: docs/web-scraped/unifi-api/

APIs covered:
- Site Manager (v1.0.0) - Cloud-based multi-site management
- Network (latest) - Local controller API for APs, switches, gateways
- Protect (latest) - Camera/NVR management

Usage:
    python unifi-docs.py              # Scrape all APIs
    python unifi-docs.py --api network  # Scrape only Network API
    python unifi-docs.py --force      # Re-scrape existing files
"""

import argparse
import asyncio
import re
import subprocess
import sys
from pathlib import Path

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

OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "web-scraped" / "unifi-api"
SITEMAP_URL = "https://developer.ui.com/sitemap.xml"
OPENAPI_URL = "https://raw.githubusercontent.com/ubiquiti-community/unifi-api/main/assets/openapi.yaml"

# We only scrape the latest version of each API
LATEST_VERSIONS = {
    'site-manager': 'v1.0.0',
    # Network and Protect versions are auto-detected from sitemap
}


def fetch_sitemap() -> list[str]:
    """Fetch sitemap and return all URLs."""
    result = subprocess.run(
        ['curl', '-sL', SITEMAP_URL],
        capture_output=True, text=True, timeout=30
    )
    return re.findall(r'<loc>([^<]+)</loc>', result.stdout)


def detect_latest_versions(urls: list[str]) -> dict[str, str]:
    """Detect latest version for each API from sitemap URLs."""
    versions = {}

    for api in ['network', 'protect', 'site-manager']:
        pattern = rf'/{api}/(v[\d.]+)'
        api_versions = set()
        for url in urls:
            match = re.search(pattern, url)
            if match:
                api_versions.add(match.group(1))

        if api_versions:
            # Sort versions and pick the latest
            sorted_versions = sorted(api_versions, key=lambda v: [int(x) for x in v[1:].split('.')])
            versions[api] = sorted_versions[-1]

    return versions


def url_to_filename(url: str) -> str:
    """Convert URL to safe filename."""
    slug = url.rstrip('/').split('/')[-1] or 'index'
    slug = re.sub(r'[^a-zA-Z0-9_-]', '-', slug)
    return f"{slug}.md"


def html_to_markdown(html: str) -> str:
    """Convert HTML to clean markdown."""
    # Convert HTML to markdown
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

        # Skip multiple consecutive empty lines
        if is_empty and prev_empty:
            continue

        cleaned.append(line)
        prev_empty = is_empty

    return '\n'.join(cleaned).strip()


async def scrape_page(context, url: str, output_dir: Path, force: bool = False) -> str:
    """Scrape a single page and convert to markdown."""
    filename = url_to_filename(url)
    filepath = output_dir / filename

    if filepath.exists() and not force:
        return f"skip:{filename}"

    page = await context.new_page()
    try:
        await page.goto(url, wait_until="domcontentloaded", timeout=20000)
        await asyncio.sleep(0.5)

        # Get innerHTML instead of innerText to preserve structure
        html = await page.evaluate("""() => {
            const main = document.querySelector('main') || document.querySelector('article') || document.body;
            const clone = main.cloneNode(true);
            clone.querySelectorAll('nav, header, footer, script, style, .sidebar, [role="navigation"]').forEach(el => el.remove());
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


async def worker(browser, queue: asyncio.Queue, output_dir: Path, worker_id: int, force: bool) -> int:
    """Worker that processes URLs from queue."""
    context = await browser.new_context()
    count = 0

    while True:
        try:
            url = queue.get_nowait()
        except asyncio.QueueEmpty:
            break

        result = await scrape_page(context, url, output_dir, force)
        count += 1

        status = result.split(":")[0]
        if status == "error" or count % 10 == 0:
            print(f"    [W{worker_id}] {result}")

    await context.close()
    return count


async def scrape_api(browser, api_name: str, urls: list[str], force: bool, workers: int = 10):
    """Scrape all pages for an API."""
    output_dir = OUTPUT_DIR / api_name
    output_dir.mkdir(parents=True, exist_ok=True)

    existing = len(list(output_dir.glob("*.md")))
    print(f"  {api_name}: {len(urls)} pages ({existing} existing)")

    queue = asyncio.Queue()
    for url in urls:
        queue.put_nowait(url)

    tasks = [worker(browser, queue, output_dir, i, force) for i in range(min(workers, len(urls)))]
    await asyncio.gather(*tasks)

    final = len(list(output_dir.glob("*.md")))
    print(f"    Done: {final} files")


def download_openapi_spec():
    """Download the community OpenAPI spec for Network API."""
    output_file = OUTPUT_DIR / "openapi.yaml"

    print(f"Downloading OpenAPI spec...")
    result = subprocess.run(
        ['curl', '-sL', OPENAPI_URL, '-o', str(output_file)],
        capture_output=True, text=True, timeout=60
    )

    if result.returncode == 0 and output_file.exists():
        size = output_file.stat().st_size
        print(f"  Saved: {output_file} ({size / 1024:.0f} KB)")
    else:
        print(f"  Warning: Failed to download OpenAPI spec")


async def main(apis_to_scrape: list[str] | None = None, force: bool = False, workers: int = 10):
    """Main scraping function."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print("Fetching sitemap...")
    all_urls = fetch_sitemap()
    print(f"  Found {len(all_urls)} total URLs")

    # Detect latest versions
    versions = detect_latest_versions(all_urls)
    versions.update(LATEST_VERSIONS)  # Override with any fixed versions
    print(f"  Latest versions: {versions}")

    # Group URLs by API and filter to latest version
    api_urls = {}
    for api, version in versions.items():
        pattern = f"/{api}/{version}"
        api_urls[api] = [u for u in all_urls if pattern in u]

    # Filter to requested APIs
    if apis_to_scrape:
        api_urls = {k: v for k, v in api_urls.items() if k in apis_to_scrape}

    print(f"\nAPIs to scrape:")
    for api, urls in api_urls.items():
        print(f"  {api} ({versions.get(api, '?')}): {len(urls)} pages")

    # Download OpenAPI spec (always, unless filtering to specific non-network API)
    if not apis_to_scrape or 'network' in apis_to_scrape:
        download_openapi_spec()

    # Scrape each API
    print(f"\nScraping with {workers} workers...")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)

        for api_name, urls in api_urls.items():
            await scrape_api(browser, api_name, urls, force, workers)

        await browser.close()

    # Summary
    print(f"\n=== Complete ===")
    for api in api_urls.keys():
        api_dir = OUTPUT_DIR / api
        if api_dir.exists():
            count = len(list(api_dir.glob("*.md")))
            print(f"  {api}: {count} files")

    openapi_file = OUTPUT_DIR / "openapi.yaml"
    if openapi_file.exists():
        print(f"  openapi.yaml: {openapi_file.stat().st_size / 1024:.0f} KB")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scrape UniFi API documentation")
    parser.add_argument("--api", choices=['network', 'protect', 'site-manager'],
                       action='append', help="Specific API to scrape (can repeat)")
    parser.add_argument("--force", action="store_true", help="Re-scrape existing files")
    parser.add_argument("--workers", type=int, default=10, help="Parallel workers (default: 10)")

    args = parser.parse_args()

    asyncio.run(main(
        apis_to_scrape=args.api,
        force=args.force,
        workers=args.workers
    ))
