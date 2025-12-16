#!/usr/bin/env python3
"""
Sentence Transformers Documentation Scraper
Downloads all sbert.net documentation pages and converts to markdown.
Sentence Transformers is the Python library for state-of-the-art sentence, text and image embeddings.
"""

import os
import sys
import requests
from pathlib import Path
from urllib.parse import urlparse, urljoin
import time
import re
import subprocess

# sbert.net documentation pages from sitemap analysis
SBERT_DOC_PAGES = [
    # Getting Started
    "/docs/installation.html",
    "/docs/quickstart.html",
    "/docs/migration_guide.html",

    # Sentence Transformer - Usage
    "/docs/sentence_transformer/usage/usage.html",
    "/examples/sentence_transformer/applications/computing-embeddings/README.html",
    "/docs/sentence_transformer/usage/semantic_textual_similarity.html",
    "/examples/sentence_transformer/applications/semantic-search/README.html",
    "/examples/sentence_transformer/applications/retrieve_rerank/README.html",
    "/examples/sentence_transformer/applications/clustering/README.html",
    "/examples/sentence_transformer/applications/paraphrase-mining/README.html",
    "/examples/sentence_transformer/applications/parallel-sentence-mining/README.html",
    "/examples/sentence_transformer/applications/image-search/README.html",
    "/examples/sentence_transformer/applications/embedding-quantization/README.html",
    "/docs/sentence_transformer/usage/custom_models.html",
    "/docs/sentence_transformer/usage/mteb_evaluation.html",
    "/docs/sentence_transformer/usage/efficiency.html",

    # Sentence Transformer - Models & Training
    "/docs/sentence_transformer/pretrained_models.html",
    "/docs/sentence_transformer/training_overview.html",
    "/docs/sentence_transformer/dataset_overview.html",
    "/docs/sentence_transformer/loss_overview.html",
    "/docs/sentence_transformer/training/examples.html",
    "/docs/sentence_transformer/training/distributed.html",

    # Cross Encoder
    "/docs/cross_encoder/usage/usage.html",
    "/docs/cross_encoder/pretrained_models.html",
    "/docs/cross_encoder/training_overview.html",
    "/docs/cross_encoder/loss_overview.html",
    "/docs/cross_encoder/training/examples.html",

    # Sparse Encoder
    "/docs/sparse_encoder/usage/usage.html",
    "/docs/sparse_encoder/pretrained_models.html",
    "/docs/sparse_encoder/training_overview.html",
    "/docs/sparse_encoder/loss_overview.html",
    "/docs/sparse_encoder/training/examples.html",

    # Package Reference
    "/docs/package_reference/sentence_transformer/index.html",
    "/docs/package_reference/sentence_transformer/SentenceTransformer.html",
    "/docs/package_reference/sentence_transformer/models.html",
    "/docs/package_reference/sentence_transformer/losses.html",
    "/docs/package_reference/sentence_transformer/datasets.html",
    "/docs/package_reference/sentence_transformer/evaluation.html",
    "/docs/package_reference/sentence_transformer/training_args.html",
    "/docs/package_reference/sentence_transformer/trainer.html",
    "/docs/package_reference/cross_encoder/index.html",
    "/docs/package_reference/cross_encoder/CrossEncoder.html",
    "/docs/package_reference/cross_encoder/losses.html",
    "/docs/package_reference/cross_encoder/evaluation.html",
    "/docs/package_reference/cross_encoder/training_args.html",
    "/docs/package_reference/cross_encoder/trainer.html",
    "/docs/package_reference/sparse_encoder/index.html",
    "/docs/package_reference/sparse_encoder/SparseEncoder.html",
    "/docs/package_reference/sparse_encoder/models.html",
    "/docs/package_reference/sparse_encoder/losses.html",
    "/docs/package_reference/sparse_encoder/evaluation.html",
    "/docs/package_reference/sparse_encoder/training_args.html",
    "/docs/package_reference/sparse_encoder/trainer.html",
    "/docs/package_reference/util.html",

    # Main index
    "/index.html",
]

BASE_URL = "https://www.sbert.net"


def html_to_markdown(html_content, url):
    """Convert HTML to markdown, extracting main content only."""
    # Sphinx ReadTheDocs theme uses different selectors
    # Try to extract main content area

    # Primary: Look for main content div
    main_match = re.search(
        r'<div[^>]*class="[^"]*rst-content[^"]*"[^>]*>(.*?)<footer',
        html_content, flags=re.DOTALL | re.IGNORECASE
    )

    if main_match:
        html_content = main_match.group(1)
    else:
        # Fallback: Look for article/section
        article_match = re.search(
            r'<article[^>]*>(.*?)</article>',
            html_content, flags=re.DOTALL | re.IGNORECASE
        )
        if article_match:
            html_content = article_match.group(1)
        else:
            # Another fallback: role="main"
            role_main = re.search(
                r'<div[^>]*role="main"[^>]*>(.*?)</div>\s*(?:<footer|<div[^>]*class="[^"]*footer)',
                html_content, flags=re.DOTALL | re.IGNORECASE
            )
            if role_main:
                html_content = role_main.group(1)

    # Remove navigation elements
    html_content = re.sub(r'<nav[^>]*>.*?</nav>', '', html_content, flags=re.DOTALL)
    html_content = re.sub(r'<div[^>]*class="[^"]*toctree[^"]*"[^>]*>.*?</div>', '', html_content, flags=re.DOTALL)

    # Remove "Edit on GitHub" and other meta links
    html_content = re.sub(r'<a[^>]*class="[^"]*edit-link[^"]*"[^>]*>.*?</a>', '', html_content, flags=re.DOTALL)
    html_content = re.sub(r'<a[^>]*href="[^"]*github\.com[^"]*"[^>]*>\s*Edit on GitHub\s*</a>', '', html_content, flags=re.DOTALL)

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
    if path == "/" or path == "" or path == "/index.html":
        return "index.md"

    # Remove leading/trailing slashes and .html extension
    clean_path = path.strip("/")
    if clean_path.endswith(".html"):
        clean_path = clean_path[:-5]

    # Handle nested paths - flatten to single filename
    # e.g., docs/sentence_transformer/usage/usage -> sentence_transformer-usage-usage.md
    # Remove common prefixes for cleaner names
    clean_path = re.sub(r'^docs/', '', clean_path)
    clean_path = re.sub(r'^examples/', 'examples-', clean_path)

    # Convert slashes to hyphens
    filename = clean_path.replace("/", "-")

    # Handle README files
    filename = re.sub(r'-README$', '', filename)

    return filename + ".md"


def main():
    """Main function to download all Sentence Transformers documentation."""
    print("=" * 60)
    print("Sentence Transformers Documentation Scraper")
    print("=" * 60)
    print(f"Base URL: {BASE_URL}")
    print(f"Pages to download: {len(SBERT_DOC_PAGES)}")
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "web-scraped" / "sentence-transformers"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Output directory: {output_dir}")
    print()

    successful = 0
    failed = 0
    start_time = time.time()

    for i, page_path in enumerate(SBERT_DOC_PAGES, 1):
        url = BASE_URL + page_path
        filename = path_to_filename(page_path)
        output_path = output_dir / filename

        print(f"[{i:2d}/{len(SBERT_DOC_PAGES)}] ", end="")

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
