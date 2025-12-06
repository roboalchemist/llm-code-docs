#!/usr/bin/env python3
"""
Sentence Transformers Documentation Scraper
Downloads all sbert.net documentation pages and converts to markdown.
Sentence Transformers is a Python library for sentence, text and image embeddings.
"""

import os
import sys
import requests
from pathlib import Path
from urllib.parse import urlparse
import time
import re
import subprocess

# Sentence Transformers documentation pages from sbert.net
SBERT_DOC_PAGES = [
    # Core docs
    "index.html",
    "docs/installation.html",
    "docs/quickstart.html",
    "docs/migration_guide.html",

    # Sentence Transformer docs
    "docs/sentence_transformer/usage/usage.html",
    "docs/sentence_transformer/usage/semantic_textual_similarity.html",
    "docs/sentence_transformer/usage/custom_models.html",
    "docs/sentence_transformer/usage/efficiency.html",
    "docs/sentence_transformer/usage/mteb_evaluation.html",
    "docs/sentence_transformer/pretrained_models.html",
    "docs/sentence_transformer/training_overview.html",
    "docs/sentence_transformer/training/examples.html",
    "docs/sentence_transformer/training/distributed.html",
    "docs/sentence_transformer/dataset_overview.html",
    "docs/sentence_transformer/loss_overview.html",

    # Cross Encoder docs
    "docs/cross_encoder/usage/usage.html",
    "docs/cross_encoder/usage/efficiency.html",
    "docs/cross_encoder/pretrained_models.html",
    "docs/cross_encoder/training_overview.html",
    "docs/cross_encoder/training/examples.html",
    "docs/cross_encoder/loss_overview.html",

    # Sparse Encoder docs
    "docs/sparse_encoder/usage/usage.html",
    "docs/sparse_encoder/usage/efficiency.html",
    "docs/sparse_encoder/pretrained_models.html",
    "docs/sparse_encoder/training_overview.html",
    "docs/sparse_encoder/training/examples.html",
    "docs/sparse_encoder/loss_overview.html",

    # Package reference - Sentence Transformer
    "docs/package_reference/sentence_transformer/index.html",
    "docs/package_reference/sentence_transformer/SentenceTransformer.html",
    "docs/package_reference/sentence_transformer/datasets.html",
    "docs/package_reference/sentence_transformer/evaluation.html",
    "docs/package_reference/sentence_transformer/losses.html",
    "docs/package_reference/sentence_transformer/models.html",
    "docs/package_reference/sentence_transformer/quantization.html",
    "docs/package_reference/sentence_transformer/sampler.html",
    "docs/package_reference/sentence_transformer/trainer.html",
    "docs/package_reference/sentence_transformer/training_args.html",

    # Package reference - Cross Encoder
    "docs/package_reference/cross_encoder/index.html",
    "docs/package_reference/cross_encoder/cross_encoder.html",
    "docs/package_reference/cross_encoder/evaluation.html",
    "docs/package_reference/cross_encoder/losses.html",
    "docs/package_reference/cross_encoder/trainer.html",
    "docs/package_reference/cross_encoder/training_args.html",

    # Package reference - Sparse Encoder
    "docs/package_reference/sparse_encoder/index.html",
    "docs/package_reference/sparse_encoder/SparseEncoder.html",
    "docs/package_reference/sparse_encoder/evaluation.html",
    "docs/package_reference/sparse_encoder/losses.html",
    "docs/package_reference/sparse_encoder/models.html",
    "docs/package_reference/sparse_encoder/search_engines.html",
    "docs/package_reference/sparse_encoder/trainer.html",
    "docs/package_reference/sparse_encoder/training_args.html",
    "docs/package_reference/sparse_encoder/callbacks.html",

    # Package reference - Util
    "docs/package_reference/util.html",

    # Examples - Sentence Transformer Applications
    "examples/sentence_transformer/applications/computing-embeddings/README.html",
    "examples/sentence_transformer/applications/semantic-search/README.html",
    "examples/sentence_transformer/applications/retrieve_rerank/README.html",
    "examples/sentence_transformer/applications/clustering/README.html",
    "examples/sentence_transformer/applications/paraphrase-mining/README.html",
    "examples/sentence_transformer/applications/parallel-sentence-mining/README.html",
    "examples/sentence_transformer/applications/image-search/README.html",
    "examples/sentence_transformer/applications/embedding-quantization/README.html",

    # Examples - Sentence Transformer Training
    "examples/sentence_transformer/training/sts/README.html",
    "examples/sentence_transformer/training/nli/README.html",
    "examples/sentence_transformer/training/paraphrases/README.html",
    "examples/sentence_transformer/training/quora_duplicate_questions/README.html",
    "examples/sentence_transformer/training/ms_marco/README.html",
    "examples/sentence_transformer/training/multilingual/README.html",
    "examples/sentence_transformer/training/distillation/README.html",
    "examples/sentence_transformer/training/data_augmentation/README.html",
    "examples/sentence_transformer/training/matryoshka/README.html",
    "examples/sentence_transformer/training/adaptive_layer/README.html",
    "examples/sentence_transformer/training/prompts/README.html",
    "examples/sentence_transformer/training/peft/README.html",
    "examples/sentence_transformer/training/hpo/README.html",
    "examples/sentence_transformer/domain_adaptation/README.html",
    "examples/sentence_transformer/unsupervised_learning/README.html",

    # Examples - Cross Encoder
    "examples/cross_encoder/applications/README.html",
    "examples/cross_encoder/training/sts/README.html",
    "examples/cross_encoder/training/nli/README.html",
    "examples/cross_encoder/training/quora_duplicate_questions/README.html",
    "examples/cross_encoder/training/ms_marco/README.html",
    "examples/cross_encoder/training/distillation/README.html",
    "examples/cross_encoder/training/rerankers/README.html",

    # Examples - Sparse Encoder
    "examples/sparse_encoder/applications/computing_embeddings/README.html",
    "examples/sparse_encoder/applications/semantic_search/README.html",
    "examples/sparse_encoder/applications/retrieve_rerank/README.html",
    "examples/sparse_encoder/applications/semantic_textual_similarity/README.html",
    "examples/sparse_encoder/evaluation/README.html",
    "examples/sparse_encoder/training/sts/README.html",
    "examples/sparse_encoder/training/nli/README.html",
    "examples/sparse_encoder/training/quora_duplicate_questions/README.html",
    "examples/sparse_encoder/training/ms_marco/README.html",
    "examples/sparse_encoder/training/distillation/README.html",
    "examples/sparse_encoder/training/retrievers/README.html",
]

BASE_URL = "https://www.sbert.net"


def html_to_markdown(html_content, url):
    """Convert HTML to markdown using pandoc, falling back to basic extraction."""
    # Extract main content - sbert.net uses ReadTheDocs/Sphinx structure
    main_match = re.search(
        r'<div[^>]*class="[^"]*rst-content[^"]*"[^>]*>(.*?)<footer',
        html_content, flags=re.DOTALL | re.IGNORECASE
    )

    if main_match:
        html_content = main_match.group(1)
    else:
        # Try article tag
        article_match = re.search(
            r'<article[^>]*>(.*?)</article>',
            html_content, flags=re.DOTALL | re.IGNORECASE
        )
        if article_match:
            html_content = article_match.group(1)

    # Remove navigation elements
    html_content = re.sub(r'<div[^>]*class="[^"]*toctree[^"]*"[^>]*>.*?</div>', '', html_content, flags=re.DOTALL)
    html_content = re.sub(r'<div[^>]*class="[^"]*sidebar[^"]*"[^>]*>.*?</div>', '', html_content, flags=re.DOTALL)

    # Try pandoc first
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

    # Fallback: basic HTML to text extraction
    html_content = re.sub(r'<script[^>]*>.*?</script>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<style[^>]*>.*?</style>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<nav[^>]*>.*?</nav>', '', html_content, flags=re.DOTALL | re.IGNORECASE)

    # Convert headers
    for i in range(6, 0, -1):
        html_content = re.sub(rf'<h{i}[^>]*>(.*?)</h{i}>', r'\n' + '#' * i + r' \1\n', html_content, flags=re.DOTALL | re.IGNORECASE)

    # Code blocks
    html_content = re.sub(r'<pre[^>]*><code[^>]*>(.*?)</code></pre>', r'\n```\n\1\n```\n', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<code[^>]*>(.*?)</code>', r'`\1`', html_content, flags=re.DOTALL | re.IGNORECASE)

    # Links
    html_content = re.sub(r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>', r'[\2](\1)', html_content, flags=re.DOTALL | re.IGNORECASE)

    # Bold and italic
    html_content = re.sub(r'<strong[^>]*>(.*?)</strong>', r'**\1**', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<em[^>]*>(.*?)</em>', r'*\1*', html_content, flags=re.DOTALL | re.IGNORECASE)

    # Lists
    html_content = re.sub(r'<li[^>]*>(.*?)</li>', r'- \1\n', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<[ou]l[^>]*>', '\n', html_content, flags=re.IGNORECASE)
    html_content = re.sub(r'</[ou]l>', '\n', html_content, flags=re.IGNORECASE)

    # Paragraphs
    html_content = re.sub(r'<p[^>]*>(.*?)</p>', r'\n\1\n', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<br\s*/?>', '\n', html_content, flags=re.IGNORECASE)
    html_content = re.sub(r'<div[^>]*>', '\n', html_content, flags=re.IGNORECASE)
    html_content = re.sub(r'</div>', '\n', html_content, flags=re.IGNORECASE)

    # Remove remaining tags
    html_content = re.sub(r'<[^>]+>', '', html_content)

    # Decode entities
    html_content = html_content.replace('&nbsp;', ' ')
    html_content = html_content.replace('&lt;', '<')
    html_content = html_content.replace('&gt;', '>')
    html_content = html_content.replace('&amp;', '&')
    html_content = html_content.replace('&quot;', '"')

    # Clean up
    html_content = re.sub(r'\n\s*\n\s*\n', '\n\n', html_content)
    html_content = html_content.strip()

    return f"# Source: {url}\n\n{html_content}"


def download_page(url, output_path):
    """Download a page and convert to markdown."""
    try:
        print(f"Downloading: {url}")

        response = requests.get(url, timeout=15)
        response.raise_for_status()

        markdown = html_to_markdown(response.text, url)

        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(markdown)

        print(f"  -> Saved: {output_path.name}")
        return True

    except requests.exceptions.RequestException as e:
        print(f"  -> Error downloading {url}: {e}")
        return False
    except Exception as e:
        print(f"  -> Error processing {url}: {e}")
        return False


def path_to_filename(path):
    """Convert URL path to filename."""
    if path == "index.html":
        return "index.md"

    # Remove .html extension and convert path to flat filename
    clean_path = path.replace('.html', '').replace('README', 'readme')

    # Convert to flat filename: docs/sentence_transformer/usage -> docs-sentence_transformer-usage.md
    return clean_path.replace('/', '-') + ".md"


def main():
    """Main function to download all sentence-transformers documentation."""
    print("=" * 70)
    print("Sentence Transformers Documentation Scraper")
    print("=" * 70)
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
        url = f"{BASE_URL}/{page_path}"
        filename = path_to_filename(page_path)
        output_path = output_dir / filename

        print(f"[{i:3d}/{len(SBERT_DOC_PAGES)}] ", end="")

        if download_page(url, output_path):
            successful += 1
        else:
            failed += 1

        time.sleep(0.3)  # Be respectful

    elapsed = time.time() - start_time

    print()
    print("=" * 70)
    print("Download Summary")
    print("=" * 70)
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    print(f"Time: {elapsed:.1f} seconds")
    print(f"Output: {output_dir}")

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
