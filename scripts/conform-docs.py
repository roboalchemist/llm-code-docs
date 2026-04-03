#!/usr/bin/env python3
"""
Conform Documentation Scraper
Downloads all Conform documentation pages and converts to markdown.
Conform is a type-safe form validation library for React/Remix/Next.js.
"""

import os
import sys
import requests
from pathlib import Path
from urllib.parse import urlparse
import time
import re
import subprocess

# Conform documentation pages extracted from site navigation
CONFORM_DOC_PAGES = [
    # Getting Started
    "/",
    "/installation",
    "/tutorial",
    "/upgrading-v1",

    # Guides
    "/validation",
    "/complex-structures",
    "/intent-button",
    "/accessibility",
    "/checkbox-and-radio-group",
    "/file-upload",

    # Integration
    "/integration/ui-libraries",
    "/integration/remix",
    "/integration/nextjs",

    # API Reference
    "/api/react/useForm",
    "/api/react/useField",
    "/api/react/useFormMetadata",
    "/api/react/useInputControl",
    "/api/react/FormProvider",
    "/api/react/FormStateInput",

    # Future APIs
    "/api/react/future/useForm",
    "/api/react/future/useFormData",
    "/api/react/future/useFormMetadata",
    "/api/react/future/useField",
    "/api/react/future/useControl",
    "/api/react/future/useIntent",
    "/api/react/future/parseSubmission",
    "/api/react/future/report",
    "/api/react/future/getFieldValue",
    "/api/react/future/isDirty",
    "/api/react/future/FormProvider",
    "/api/react/future/FormOptionsProvider",
    "/api/react/future/memoize",

    # Future APIs (Zod Schema)
    "/api/zod/future/coerceFormValue",
    "/api/zod/future/formatResult",

    # Future APIs (Valibot Schema)
    "/api/valibot/future/coerceFormValue",
    "/api/valibot/future/formatResult",

    # Utilities
    "/api/react/getFormProps",
    "/api/react/getFieldsetProps",
    "/api/react/getInputProps",
    "/api/react/getSelectProps",
    "/api/react/getTextareaProps",
    "/api/react/getCollectionProps",

    # Zod Schema
    "/api/zod/parseWithZod",
    "/api/zod/coerceFormValue",
    "/api/zod/getZodConstraint",
    "/api/zod/conformZodMessage",

    # Valibot Schema
    "/api/valibot/parseWithValibot",
    "/api/valibot/coerceFormValue",
    "/api/valibot/getValibotConstraint",
    "/api/valibot/conformValibotMessage",

    # Yup Schema
    "/api/yup/parseWithYup",
    "/api/yup/getYupConstraint",
]

BASE_URL = "https://conform.guide"


def html_to_markdown(html_content, url):
    """Convert HTML to markdown, extracting main content only."""
    # First, extract just the main article content to avoid nav/sidebar noise
    # Conform uses <article> tag for main content
    article_match = re.search(
        r'<article[^>]*>(.*?)</article>',
        html_content, flags=re.DOTALL | re.IGNORECASE
    )

    if article_match:
        html_content = article_match.group(1)
    else:
        # Try alternate selector - main tag
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
    html_content = html_content.replace('&#x27;', "'")

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

    # Remove leading/trailing slashes and convert to filename
    clean_path = path.strip("/")

    # Handle nested paths like /api/react/useForm
    if "/" in clean_path:
        # Convert to flat filename: api/react/useForm -> api-react-useForm.md
        return clean_path.replace("/", "-") + ".md"

    return clean_path + ".md"


def main():
    """Main function to download all Conform documentation."""
    print("=" * 60)
    print("Conform Documentation Scraper")
    print("=" * 60)
    print(f"Base URL: {BASE_URL}")
    print(f"Pages to download: {len(CONFORM_DOC_PAGES)}")
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "web-scraped" / "conform"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Output directory: {output_dir}")
    print()

    successful = 0
    failed = 0
    start_time = time.time()

    for i, page_path in enumerate(CONFORM_DOC_PAGES, 1):
        url = BASE_URL + page_path
        filename = path_to_filename(page_path)
        output_path = output_dir / filename

        print(f"[{i:2d}/{len(CONFORM_DOC_PAGES)}] ", end="")

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
