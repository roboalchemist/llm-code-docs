#!/usr/bin/env python3
"""
Download NeMo Framework documentation from llms.txt
"""

import os
import re
import requests
from pathlib import Path
from urllib.parse import urlparse

OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "llms-txt" / "nemo-framework"
LLMS_TXT_URL = "https://docs.nvidia.com/nemo-framework/llms.txt"

def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Download llms.txt
    print(f"Fetching {LLMS_TXT_URL}")
    response = requests.get(LLMS_TXT_URL)
    response.raise_for_status()
    llms_content = response.text

    # Save llms.txt
    (OUTPUT_DIR / "llms.txt").write_text(llms_content)
    print(f"Saved llms.txt")

    # Extract URLs from markdown links: ](url.md)
    urls = re.findall(r'\]\(([^)]+\.md)\)', llms_content)
    urls = sorted(set(urls))

    print(f"Found {len(urls)} documentation URLs")

    success = 0
    failed = 0

    for url in urls:
        # Add https:// if needed
        if not url.startswith('http'):
            full_url = f"https://{url}"
        else:
            full_url = url

        # Create filename from path
        # docs.nvidia.com/nemo-framework/user-guide/latest/overview.html.md -> latest_overview.html.md
        path = url.replace('docs.nvidia.com/nemo-framework/user-guide/', '')
        filename = path.replace('/', '_')

        print(f"  Downloading: {filename}")

        try:
            resp = requests.get(full_url, timeout=30)
            resp.raise_for_status()

            content = resp.text

            # Add source header
            content = f"# Source: {full_url}\n\n{content}"

            (OUTPUT_DIR / filename).write_text(content)
            success += 1
        except Exception as e:
            print(f"    Failed: {e}")
            failed += 1

    print(f"\nCompleted: {success} successful, {failed} failed")
    print(f"Output directory: {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
