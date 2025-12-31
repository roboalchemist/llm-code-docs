#!/usr/bin/env python3
"""
Playwright Documentation Scraper
Downloads all Playwright documentation pages and converts to markdown.
Playwright is a browser automation framework for end-to-end testing.
"""

import os
import sys
import requests
from pathlib import Path
from urllib.parse import urlparse
import time
import re
import subprocess

# Playwright documentation pages from sitemap
# These are extracted from https://playwright.dev/sitemap.xml
PLAYWRIGHT_DOC_PAGES = [
    "/docs/accessibility-testing",
    "/docs/actionability",
    "/docs/api-testing",
    "/docs/api/class-android",
    "/docs/api/class-androiddevice",
    "/docs/api/class-androidinput",
    "/docs/api/class-androidsocket",
    "/docs/api/class-androidwebview",
    "/docs/api/class-apirequest",
    "/docs/api/class-apirequestcontext",
    "/docs/api/class-apiresponse",
    "/docs/api/class-apiresponseassertions",
    "/docs/api/class-browser",
    "/docs/api/class-browsercontext",
    "/docs/api/class-browserserver",
    "/docs/api/class-browsertype",
    "/docs/api/class-cdpsession",
    "/docs/api/class-clock",
    "/docs/api/class-consolemessage",
    "/docs/api/class-coverage",
    "/docs/api/class-dialog",
    "/docs/api/class-download",
    "/docs/api/class-electron",
    "/docs/api/class-electronapplication",
    "/docs/api/class-elementhandle",
    "/docs/api/class-filechooser",
    "/docs/api/class-fixtures",
    "/docs/api/class-frame",
    "/docs/api/class-framelocator",
    "/docs/api/class-fullconfig",
    "/docs/api/class-fullproject",
    "/docs/api/class-genericassertions",
    "/docs/api/class-jshandle",
    "/docs/api/class-keyboard",
    "/docs/api/class-location",
    "/docs/api/class-locator",
    "/docs/api/class-locatorassertions",
    "/docs/api/class-logger",
    "/docs/api/class-mouse",
    "/docs/api/class-page",
    "/docs/api/class-pageassertions",
    "/docs/api/class-playwright",
    "/docs/api/class-playwrightassertions",
    "/docs/api/class-reporter",
    "/docs/api/class-request",
    "/docs/api/class-response",
    "/docs/api/class-route",
    "/docs/api/class-selectors",
    "/docs/api/class-snapshotassertions",
    "/docs/api/class-suite",
    "/docs/api/class-test",
    "/docs/api/class-testcase",
    "/docs/api/class-testconfig",
    "/docs/api/class-testerror",
    "/docs/api/class-testinfo",
    "/docs/api/class-testinfoerror",
    "/docs/api/class-testoptions",
    "/docs/api/class-testproject",
    "/docs/api/class-testresult",
    "/docs/api/class-teststep",
    "/docs/api/class-teststepinfo",
    "/docs/api/class-timeouterror",
    "/docs/api/class-touchscreen",
    "/docs/api/class-tracing",
    "/docs/api/class-video",
    "/docs/api/class-weberror",
    "/docs/api/class-websocket",
    "/docs/api/class-websocketroute",
    "/docs/api/class-worker",
    "/docs/api/class-workerinfo",
    "/docs/aria-snapshots",
    "/docs/auth",
    "/docs/best-practices",
    "/docs/browser-contexts",
    "/docs/browsers",
    "/docs/canary-releases",
    "/docs/chrome-extensions",
    "/docs/ci",
    "/docs/ci-intro",
    "/docs/clock",
    "/docs/codegen",
    "/docs/codegen-intro",
    "/docs/debug",
    "/docs/dialogs",
    "/docs/docker",
    "/docs/downloads",
    "/docs/emulation",
    "/docs/evaluating",
    "/docs/events",
    "/docs/extensibility",
    "/docs/frames",
    "/docs/getting-started-vscode",
    "/docs/handles",
    "/docs/input",
    "/docs/intro",
    "/docs/languages",
    "/docs/library",
    "/docs/locators",
    "/docs/mock",
    "/docs/mock-browser-apis",
    "/docs/navigations",
    "/docs/network",
    "/docs/other-locators",
    "/docs/pages",
    "/docs/pom",
    "/docs/protractor",
    "/docs/puppeteer",
    "/docs/release-notes",
    "/docs/running-tests",
    "/docs/screenshots",
    "/docs/selenium-grid",
    "/docs/service-workers",
    "/docs/test-agents",
    "/docs/test-annotations",
    "/docs/test-assertions",
    "/docs/test-cli",
    "/docs/test-components",
    "/docs/test-configuration",
    "/docs/test-fixtures",
    "/docs/test-global-setup-teardown",
    "/docs/test-parallel",
    "/docs/test-parameterize",
    "/docs/test-projects",
    "/docs/test-reporters",
    "/docs/test-retries",
    "/docs/test-sharding",
    "/docs/test-snapshots",
    "/docs/test-timeouts",
    "/docs/test-typescript",
    "/docs/test-ui-mode",
    "/docs/test-use-options",
    "/docs/test-webserver",
    "/docs/testing-library",
    "/docs/touch-events",
    "/docs/trace-viewer",
    "/docs/trace-viewer-intro",
    "/docs/videos",
    "/docs/webview2",
    "/docs/writing-tests",
]

BASE_URL = "https://playwright.dev"


def html_to_markdown(html_content, url):
    """Convert HTML to markdown, extracting main content only."""
    # First, extract just the main article content to avoid nav/sidebar noise
    # Docusaurus uses <article> or <main> tags
    article_match = re.search(
        r'<article[^>]*>(.*?)</article>',
        html_content, flags=re.DOTALL | re.IGNORECASE
    )

    if article_match:
        html_content = article_match.group(1)
    else:
        # Try main tag
        main_match = re.search(
            r'<main[^>]*>(.*?)</main>',
            html_content, flags=re.DOTALL | re.IGNORECASE
        )
        if main_match:
            html_content = main_match.group(1)

    # Try pandoc on cleaned content
    try:
        result = subprocess.run(
            ['pandoc', '-f', 'html', '-t', 'markdown', '--wrap=none'],
            input=html_content,
            capture_output=True,
            text=True,
            timeout=30
        )
        if result.returncode == 0:
            markdown = result.stdout
            # Clean up pandoc artifacts
            markdown = re.sub(r'^::+.*$', '', markdown, flags=re.MULTILINE)  # Remove ::: div markers
            markdown = re.sub(r'\{[^}]*\}', '', markdown)  # Remove {.class} attributes
            markdown = re.sub(r'\n{3,}', '\n\n', markdown)  # Normalize whitespace
            markdown = markdown.strip()
            return f"# Source: {url}\n\n{markdown}"
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass

    # Fallback: basic HTML to text extraction
    # Remove script and style elements
    html_content = re.sub(r'<script[^>]*>.*?</script>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<style[^>]*>.*?</style>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<nav[^>]*>.*?</nav>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<header[^>]*>.*?</header>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<footer[^>]*>.*?</footer>', '', html_content, flags=re.DOTALL | re.IGNORECASE)

    # Convert common HTML elements to markdown
    # Headers
    for i in range(6, 0, -1):
        html_content = re.sub(rf'<h{i}[^>]*>(.*?)</h{i}>', r'\n' + '#' * i + r' \1\n', html_content, flags=re.DOTALL | re.IGNORECASE)

    # Code blocks
    html_content = re.sub(r'<pre[^>]*><code[^>]*>(.*?)</code></pre>', r'\n```\n\1\n```\n', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<code[^>]*>(.*?)</code>', r'`\1`', html_content, flags=re.DOTALL | re.IGNORECASE)

    # Links
    html_content = re.sub(r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>', r'[\2](\1)', html_content, flags=re.DOTALL | re.IGNORECASE)

    # Bold and italic
    html_content = re.sub(r'<strong[^>]*>(.*?)</strong>', r'**\1**', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<b[^>]*>(.*?)</b>', r'**\1**', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<em[^>]*>(.*?)</em>', r'*\1*', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<i[^>]*>(.*?)</i>', r'*\1*', html_content, flags=re.DOTALL | re.IGNORECASE)

    # Lists
    html_content = re.sub(r'<li[^>]*>(.*?)</li>', r'- \1\n', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<[ou]l[^>]*>', '\n', html_content, flags=re.IGNORECASE)
    html_content = re.sub(r'</[ou]l>', '\n', html_content, flags=re.IGNORECASE)

    # Paragraphs and line breaks
    html_content = re.sub(r'<p[^>]*>(.*?)</p>', r'\n\1\n', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<br\s*/?>', '\n', html_content, flags=re.IGNORECASE)
    html_content = re.sub(r'<div[^>]*>', '\n', html_content, flags=re.IGNORECASE)
    html_content = re.sub(r'</div>', '\n', html_content, flags=re.IGNORECASE)

    # Remove remaining HTML tags
    html_content = re.sub(r'<[^>]+>', '', html_content)

    # Decode HTML entities
    html_content = html_content.replace('&nbsp;', ' ')
    html_content = html_content.replace('&lt;', '<')
    html_content = html_content.replace('&gt;', '>')
    html_content = html_content.replace('&amp;', '&')
    html_content = html_content.replace('&quot;', '"')
    html_content = html_content.replace('&#39;', "'")

    # Clean up whitespace
    html_content = re.sub(r'\n\s*\n\s*\n', '\n\n', html_content)
    html_content = html_content.strip()

    return f"# Source: {url}\n\n{html_content}"


def download_page(url, output_path):
    """Download a page and convert to markdown."""
    try:
        print(f"Downloading: {url}")

        response = requests.get(url, timeout=15)
        response.raise_for_status()

        # Convert HTML to markdown
        markdown = html_to_markdown(response.text, url)

        # Create directory if needed
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # Write markdown file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(markdown)

        print(f"  -> Saved: {output_path}")
        return True

    except requests.exceptions.RequestException as e:
        print(f"  -> Error downloading {url}: {e}")
        return False
    except Exception as e:
        print(f"  -> Error processing {url}: {e}")
        return False


def path_to_filename(path):
    """Convert URL path to filename."""
    if path == "/" or path == "":
        return "index.md"

    # Remove leading/trailing slashes
    clean_path = path.strip("/")

    # Remove /docs/ prefix if present
    if clean_path.startswith("docs/"):
        clean_path = clean_path[5:]

    # Convert nested paths like api/class-page to api-class-page.md
    if "/" in clean_path:
        return clean_path.replace("/", "-") + ".md"

    return clean_path + ".md"


def main():
    """Main function to download all Playwright documentation."""
    print("=" * 60)
    print("Playwright Documentation Scraper")
    print("=" * 60)
    print(f"Base URL: {BASE_URL}")
    print(f"Pages to download: {len(PLAYWRIGHT_DOC_PAGES)}")
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "web-scraped" / "playwright"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Output directory: {output_dir}")
    print()

    successful = 0
    failed = 0
    start_time = time.time()

    for i, page_path in enumerate(PLAYWRIGHT_DOC_PAGES, 1):
        url = BASE_URL + page_path
        filename = path_to_filename(page_path)
        output_path = output_dir / filename

        print(f"[{i:3d}/{len(PLAYWRIGHT_DOC_PAGES)}] ", end="")

        if download_page(url, output_path):
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
    total_size = sum(f.stat().st_size for f in output_dir.glob("*.md"))
    print(f"Total size: {total_size:,} bytes ({total_size/1024:.1f} KB)")

    print()
    if failed > 0:
        print(f"Warning: {failed} pages failed to download")
        sys.exit(1)
    else:
        print("All pages downloaded successfully!")
        sys.exit(0)


if __name__ == "__main__":
    main()
