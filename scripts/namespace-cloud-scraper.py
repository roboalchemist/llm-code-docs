#!/usr/bin/env python3
"""
Scrape all namespace.so/docs pages to ~/github/llm-code-docs/docs/namespace-cloud/

Pages are pre-rendered Next.js static HTML. Content lives in <article> tags.
Uses markdownify to convert HTML to clean markdown.
"""

import os
import re
import sys
import time
import urllib.request
import urllib.error
from pathlib import Path

try:
    from markdownify import markdownify as md
except ImportError:
    print("ERROR: pip install markdownify", file=sys.stderr)
    sys.exit(1)

URLS_FILE = "/tmp/namespace-doc-urls.txt"
OUTPUT_DIR = Path.home() / "github/llm-code-docs/docs/namespace-cloud"
DELAY = 0.25  # seconds between requests


def url_to_filename(url: str) -> str:
    """Convert a docs URL to a safe filename, preserving hierarchy with dashes."""
    path = url.replace("https://namespace.so/docs/", "").strip("/")
    safe = re.sub(r"[^a-zA-Z0-9._-]", "-", path)
    safe = re.sub(r"-+", "-", safe).strip("-")
    return safe + ".md"


def extract_title(html: str) -> str:
    """Extract page title from <title> tag."""
    m = re.search(r"<title>([^<]+)</title>", html)
    if m:
        title = m.group(1).strip()
        # Remove " | Namespace" suffix
        title = re.sub(r"\s*\|\s*Namespace\s*$", "", title)
        return title
    return ""


def extract_content(html: str) -> str | None:
    """Extract <article> content from pre-rendered HTML."""
    m = re.search(r"<article[^>]*>(.*?)</article>", html, re.DOTALL)
    if m:
        return m.group(1)

    # Fallback: look for main content div
    m = re.search(r'<div[^>]+class="[^"]*nextra-content[^"]*"[^>]*>(.*?)</div>', html, re.DOTALL)
    if m:
        return m.group(1)

    return None


def html_to_markdown(html_content: str, title: str, url: str) -> str:
    """Convert HTML article content to clean markdown."""
    content_md = md(
        html_content,
        heading_style="ATX",
        bullets="-",
        strip=["script", "style", "nav", "footer"],
    )

    # Clean up excessive blank lines
    content_md = re.sub(r"\n{3,}", "\n\n", content_md)
    content_md = content_md.strip()

    # Prepend source URL comment
    header = f"<!-- Source: {url} -->\n\n"
    if title and not content_md.startswith("# "):
        header += f"# {title}\n\n"

    return header + content_md + "\n"


def fetch_page(url: str) -> tuple[str, str] | tuple[None, None]:
    """Fetch a page and return (html, final_url)."""
    try:
        req = urllib.request.Request(
            url,
            headers={
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36",
                "Accept": "text/html,application/xhtml+xml,*/*",
            },
        )
        with urllib.request.urlopen(req, timeout=15) as resp:
            return resp.read().decode("utf-8"), resp.url
    except Exception as e:
        print(f"  FETCH ERROR: {e}", file=sys.stderr)
        return None, None


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Load URL list from sitemap
    with open(URLS_FILE) as f:
        urls = [line.strip() for line in f if line.strip()]

    print(f"Total URLs from sitemap: {len(urls)}")
    print(f"Output dir: {OUTPUT_DIR}")

    # Count existing files
    existing = {p.name for p in OUTPUT_DIR.glob("*.md")}
    print(f"Existing files: {len(existing)}")
    print()

    success = 0
    skipped = 0
    failed = []

    for i, url in enumerate(urls, 1):
        filename = url_to_filename(url)
        filepath = OUTPUT_DIR / filename

        if filepath.exists():
            print(f"[{i:3d}/{len(urls)}] SKIP  {filename}")
            skipped += 1
            continue

        print(f"[{i:3d}/{len(urls)}] FETCH {url}", end="", flush=True)

        html, final_url = fetch_page(url)
        if not html:
            print(" -> FAILED (no response)")
            failed.append(url)
            continue

        article_html = extract_content(html)
        if not article_html:
            print(" -> FAILED (no <article> tag)")
            failed.append(url)
            continue

        title = extract_title(html)
        markdown = html_to_markdown(article_html, title, url)

        if len(markdown.strip()) < 50:
            print(f" -> FAILED (content too short: {len(markdown)} chars)")
            failed.append(url)
            continue

        filepath.write_text(markdown, encoding="utf-8")
        print(f" -> {filename} ({len(markdown):,} chars)")
        success += 1

        time.sleep(DELAY)

    print()
    print(f"Results: {success} fetched, {skipped} skipped, {len(failed)} failed")
    print(f"Total files in output: {len(list(OUTPUT_DIR.glob('*.md')))}")

    if failed:
        print(f"\nFailed ({len(failed)}):")
        for u in failed:
            print(f"  {u}")
        with open("/tmp/namespace-failed-urls.txt", "w") as f:
            f.write("\n".join(failed))
        print(f"Saved to /tmp/namespace-failed-urls.txt")


if __name__ == "__main__":
    main()
