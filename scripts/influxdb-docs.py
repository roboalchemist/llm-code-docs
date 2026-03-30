#!/usr/bin/env python3
"""
Scraper for InfluxDB documentation from llms.txt
Downloads documentation from https://docs.influxdata.com/llms.txt
Output: docs/llms-txt/influxdb/
"""

import re
import sys
from pathlib import Path
from urllib.parse import urljoin

import requests

BASE_URL = "https://docs.influxdata.com/"
LLMS_TXT_URL = urljoin(BASE_URL, "llms.txt")
OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "llms-txt" / "influxdb"


def download_llms_txt():
    """Download the main llms.txt index file."""
    print(f"Fetching {LLMS_TXT_URL}")
    response = requests.get(LLMS_TXT_URL, timeout=30)
    response.raise_for_status()
    return response.text


def extract_doc_urls(llms_txt_content: str) -> list[tuple[str, str]]:
    """Extract documentation URLs from llms.txt content.
    
    Returns list of (url, filename) tuples.
    """
    docs = []
    # Match markdown links: [text](path)
    pattern = r'\]\(([^)]+\.(?:md|section\.md))\)'
    
    for match in re.finditer(pattern, llms_txt_content):
        rel_path = match.group(1)
        full_url = urljoin(BASE_URL, rel_path)
        
        # Create a safe filename from the path
        # influxdb3/core/index.section.md -> influxdb3_core_index.section.md
        # telegraf/v1/index.section.md -> telegraf_v1_index.section.md
        safe_name = rel_path.replace('/', '_')
        
        docs.append((full_url, safe_name))
    
    return docs


def download_file(url: str, output_path: Path) -> bool:
    """Download a file from URL to output_path."""
    try:
        print(f"  Downloading {output_path.name}...", end=" ", flush=True)
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        
        output_path.write_bytes(response.content)
        size_kb = output_path.stat().st_size / 1024
        print(f"✓ ({size_kb:.1f} KB)")
        return True
    except Exception as e:
        print(f"✗ Error: {e}")
        return False


def main():
    """Download all InfluxDB documentation."""
    # Create output directory
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    print(f"InfluxDB Documentation Downloader")
    print(f"Output directory: {OUTPUT_DIR}")
    print()
    
    # Download llms.txt
    try:
        llms_txt = download_llms_txt()
    except Exception as e:
        print(f"Error downloading llms.txt: {e}", file=sys.stderr)
        sys.exit(1)
    
    # Extract documentation URLs
    docs = extract_doc_urls(llms_txt)
    print(f"Found {len(docs)} documentation files")
    print()
    
    if not docs:
        print("No documentation files found in llms.txt", file=sys.stderr)
        sys.exit(1)
    
    # Download each file
    successful = 0
    failed = 0
    
    for url, filename in docs:
        output_path = OUTPUT_DIR / filename
        if download_file(url, output_path):
            successful += 1
        else:
            failed += 1
    
    print()
    print(f"Summary: {successful} successful, {failed} failed")
    
    if failed > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
