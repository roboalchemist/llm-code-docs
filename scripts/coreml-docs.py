#!/usr/bin/env python3
"""
Apple Core ML Documentation Scraper
Downloads Core ML Tools (coremltools) API documentation and converts to markdown.
"""

import os
import sys
import requests
from pathlib import Path
import time
import re
import subprocess
from urllib.parse import urljoin, urlparse

# Base URL for coremltools documentation
BASE_URL = "https://apple.github.io/coremltools/"

# Main documentation pages to download
COREML_DOC_PAGES = [
    "",  # Main index
    "source/api-versions.html",
    "source/coremltools.converters.html",
    "source/coremltools.converters.mil.html",
    "source/coremltools.converters.mil.input_types.html",
    "source/coremltools.converters.mil.mil.ops.defs.html",
    "source/coremltools.converters.mil.mil.passes.defs.html",
    "source/coremltools.models.html",
    "source/coremltools.optimize.html",
    "source/coremltools.optimize.coreml.html",
    "source/coremltools.optimize.torch.html",
    "source/coremltools.proto.html",
    "docs-guides/index.html",
    "mlmodel/index.html",
]

# iOS-specific operation documentation
IOS_OPS_PAGES = [
    # iOS 15 ops
    "_modules/coremltools/converters/mil/mil/ops/defs/iOS15/activation.html",
    "_modules/coremltools/converters/mil/mil/ops/defs/iOS15/classify.html",
    "_modules/coremltools/converters/mil/mil/ops/defs/iOS15/control_flow.html",
    "_modules/coremltools/converters/mil/mil/ops/defs/iOS15/conv.html",
    "_modules/coremltools/converters/mil/mil/ops/defs/iOS15/elementwise_binary.html",
    "_modules/coremltools/converters/mil/mil/ops/defs/iOS15/elementwise_unary.html",
    "_modules/coremltools/converters/mil/mil/ops/defs/iOS15/image_resizing.html",
    "_modules/coremltools/converters/mil/mil/ops/defs/iOS15/linear.html",
    "_modules/coremltools/converters/mil/mil/ops/defs/iOS15/normalization.html",
    "_modules/coremltools/converters/mil/mil/ops/defs/iOS15/pool.html",
    "_modules/coremltools/converters/mil/mil/ops/defs/iOS15/recurrent.html",
    "_modules/coremltools/converters/mil/mil/ops/defs/iOS15/reduction.html",
    "_modules/coremltools/converters/mil/mil/ops/defs/iOS15/scatter_gather.html",
    "_modules/coremltools/converters/mil/mil/ops/defs/iOS15/tensor_operation.html",
    "_modules/coremltools/converters/mil/mil/ops/defs/iOS15/tensor_transformation.html",
    # iOS 16 ops
    "_modules/coremltools/converters/mil/mil/ops/defs/iOS16/constexpr_ops.html",
    "_modules/coremltools/converters/mil/mil/ops/defs/iOS16/image_resizing.html",
    "_modules/coremltools/converters/mil/mil/ops/defs/iOS16/scatter_gather.html",
    "_modules/coremltools/converters/mil/mil/ops/defs/iOS16/tensor_operation.html",
    "_modules/coremltools/converters/mil/mil/ops/defs/iOS16/tensor_transformation.html",
    # iOS 17 ops
    "_modules/coremltools/converters/mil/mil/ops/defs/iOS17/activation.html",
    "_modules/coremltools/converters/mil/mil/ops/defs/iOS17/conv.html",
    "_modules/coremltools/converters/mil/mil/ops/defs/iOS17/elementwise_unary.html",
    "_modules/coremltools/converters/mil/mil/ops/defs/iOS17/image_resizing.html",
    "_modules/coremltools/converters/mil/mil/ops/defs/iOS17/linear.html",
    "_modules/coremltools/converters/mil/mil/ops/defs/iOS17/normalization.html",
    "_modules/coremltools/converters/mil/mil/ops/defs/iOS17/quantization_ops.html",
    "_modules/coremltools/converters/mil/mil/ops/defs/iOS17/recurrent.html",
    "_modules/coremltools/converters/mil/mil/ops/defs/iOS17/reduction.html",
    "_modules/coremltools/converters/mil/mil/ops/defs/iOS17/scatter_gather.html",
    "_modules/coremltools/converters/mil/mil/ops/defs/iOS17/tensor_operation.html",
    "_modules/coremltools/converters/mil/mil/ops/defs/iOS17/tensor_transformation.html",
    # iOS 18 ops
    "_modules/coremltools/converters/mil/mil/ops/defs/iOS18/compression.html",
    "_modules/coremltools/converters/mil/mil/ops/defs/iOS18/recurrent.html",
    "_modules/coremltools/converters/mil/mil/ops/defs/iOS18/states.html",
    "_modules/coremltools/converters/mil/mil/ops/defs/iOS18/tensor_transformation.html",
    "_modules/coremltools/converters/mil/mil/ops/defs/iOS18/transformers.html",
]

# Combine all pages
ALL_PAGES = COREML_DOC_PAGES + IOS_OPS_PAGES


def html_to_markdown(html_content, url):
    """Convert HTML to markdown using pandoc if available, else basic conversion."""
    # Try pandoc first for best results
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
            markdown = re.sub(r'^::+.*$', '', markdown, flags=re.MULTILINE)
            markdown = re.sub(r'\{[^}]*\}', '', markdown)
            markdown = re.sub(r'\n{3,}', '\n\n', markdown)
            markdown = markdown.strip()
            return f"# Source: {url}\n\n{markdown}"
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass

    # Fallback: basic HTML to markdown conversion
    # Remove script and style elements
    html_content = re.sub(r'<script[^>]*>.*?</script>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<style[^>]*>.*?</style>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<nav[^>]*>.*?</nav>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<header[^>]*>.*?</header>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<footer[^>]*>.*?</footer>', '', html_content, flags=re.DOTALL | re.IGNORECASE)

    # Extract main content from Sphinx documentation
    main_match = re.search(
        r'<div[^>]*(?:class|role)="[^"]*(?:main|document|body|content)[^"]*"[^>]*>(.*?)</div>',
        html_content,
        flags=re.DOTALL | re.IGNORECASE
    )
    if main_match:
        html_content = main_match.group(1)

    # Convert headers
    for i in range(6, 0, -1):
        html_content = re.sub(
            rf'<h{i}[^>]*>(.*?)</h{i}>',
            r'\n' + '#' * i + r' \1\n',
            html_content,
            flags=re.DOTALL | re.IGNORECASE
        )

    # Code blocks
    html_content = re.sub(
        r'<pre[^>]*><code[^>]*>(.*?)</code></pre>',
        r'\n```\n\1\n```\n',
        html_content,
        flags=re.DOTALL | re.IGNORECASE
    )
    html_content = re.sub(r'<code[^>]*>(.*?)</code>', r'`\1`', html_content, flags=re.DOTALL | re.IGNORECASE)

    # Links
    html_content = re.sub(
        r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>',
        r'[\2](\1)',
        html_content,
        flags=re.DOTALL | re.IGNORECASE
    )

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
    if path == "" or path == "/":
        return "index.md"

    # Remove leading/trailing slashes
    clean_path = path.strip("/")

    # Remove .html extension
    clean_path = re.sub(r'\.html$', '', clean_path)

    # Convert slashes to dashes for nested paths
    filename = clean_path.replace("/", "-") + ".md"

    return filename


def main():
    """Main function to download all Core ML documentation."""
    print("=" * 60)
    print("Apple Core ML Documentation Scraper")
    print("=" * 60)
    print(f"Base URL: {BASE_URL}")
    print(f"Pages to download: {len(ALL_PAGES)}")
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "web-scraped" / "coreml"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Output directory: {output_dir}")
    print()

    successful = 0
    failed = 0
    start_time = time.time()

    for i, page_path in enumerate(ALL_PAGES, 1):
        url = urljoin(BASE_URL, page_path)
        filename = path_to_filename(page_path)
        output_path = output_dir / filename

        print(f"[{i:2d}/{len(ALL_PAGES)}] ", end="")

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
