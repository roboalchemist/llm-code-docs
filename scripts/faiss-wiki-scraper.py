#!/usr/bin/env python3
"""
FAISS Wiki Documentation Scraper
Downloads all wiki pages from the FAISS GitHub repository.
"""

import os
import re
import requests
from pathlib import Path
from urllib.parse import urljoin
import time

# Base URLs
WIKI_BASE = "https://github.com/facebookresearch/faiss/wiki"
RAW_WIKI_BASE = "https://raw.githubusercontent.com/wiki/facebookresearch/faiss"

# Target directory
TARGET_DIR = Path(__file__).parent.parent / "docs" / "github-scraped" / "faiss" / "wiki"

# Known wiki pages from the navigation
WIKI_PAGES = [
    # Tutorial
    "Installing-Faiss",
    "Getting-started",
    "Faster-search",
    "Lower-memory-footprint",
    "Running-on-GPUs",

    # Basics
    "MetricType-and-distances",
    "Faiss-building-blocks:-clustering,-PCA,-quantization",
    "Guidelines-to-choose-an-index",

    # Faiss Indexes
    "Faiss-indexes",
    "Binary-Indexes",
    "Faiss-indexes-(composite)",
    "Pre-and-post-processing",
    "The-index-factory",
    "Index-IO,-cloning-and-hyper-parameter-tuning",
    "Special-operations-on-indexes",
    "Additive-quantizers",

    # GPU Faiss
    "Faiss-on-the-GPU",
    "Comparing-GPU-vs-CPU",
    "GPU-k-means-example",
    "GPU-Faiss-with-cuVS",
    "GPU-Faiss-with-cuVS-usage",

    # Advanced
    "Faiss-code-structure",
    "Threads-and-asynchronous-calls",
    "Inverted-list-objects-and-scanners",
    "Indexes-that-do-not-fit-in-RAM",
    "Vector-codecs",
    "Brute-force-search-without-an-index",
    "Fast-accumulation-of-PQ-and-AQ-codes-(FastScan)",
    "Implementation-notes",
    "Setting-search-parameters-for-one-query",
    "How-to-make-Faiss-run-faster",

    # Use Cases
    "Low-level-benchmarks",
    "Indexing-1M-vectors",
    "Indexing-1G-vectors",
    "Indexing-1T-vectors",
    "Vector-codec-benchmarks",
    "Binary-hashing-index-benchmark",
    "Hybrid-CPU-GPU-search-and-multiple-GPUs",
    "Case-studies",

    # Additional
    "FAQ",
    "Python-C-code-snippets",
    "Troubleshooting",
    "Related-projects",
]


def download_wiki_page(page_name: str) -> bool:
    """Download a single wiki page as markdown."""
    # Construct the raw markdown URL
    raw_url = f"{RAW_WIKI_BASE}/{page_name}.md"

    # Create sanitized filename
    safe_filename = re.sub(r'[^\w\s-]', '', page_name.replace(':', '')).strip().lower()
    safe_filename = re.sub(r'[-\s]+', '-', safe_filename)
    target_file = TARGET_DIR / f"{safe_filename}.md"

    print(f"Downloading: {page_name}")
    print(f"  From: {raw_url}")
    print(f"  To: {target_file}")

    try:
        response = requests.get(raw_url, timeout=10)
        response.raise_for_status()

        # Add source header
        content = f"# Source: {WIKI_BASE}/{page_name}\n\n"
        content += response.text

        # Write to file
        target_file.write_text(content, encoding='utf-8')
        print(f"  ✓ Downloaded ({len(response.text)} bytes)")
        return True

    except requests.exceptions.RequestException as e:
        print(f"  ✗ Failed: {e}")
        return False


def main():
    """Download all FAISS wiki pages."""
    print(f"FAISS Wiki Scraper")
    print(f"Target directory: {TARGET_DIR}")
    print(f"=" * 70)

    # Create target directory
    TARGET_DIR.mkdir(parents=True, exist_ok=True)

    # Download all pages
    success_count = 0
    failed_count = 0

    for page_name in WIKI_PAGES:
        if download_wiki_page(page_name):
            success_count += 1
        else:
            failed_count += 1
        time.sleep(0.5)  # Be polite to GitHub
        print()

    print("=" * 70)
    print(f"Download complete!")
    print(f"  Success: {success_count}")
    print(f"  Failed: {failed_count}")
    print(f"  Total: {len(WIKI_PAGES)}")


if __name__ == "__main__":
    main()
