#!/usr/bin/env python3
"""
date-fns Documentation Scraper
Downloads date-fns documentation from GitHub repository and converts to markdown.
date-fns is a modern JavaScript date utility library.
"""

import os
import sys
import requests
from pathlib import Path
import time
import re

# date-fns documentation files
DATE_FNS_DOCS = [
    {
        "name": "README",
        "url": "https://raw.githubusercontent.com/date-fns/date-fns/main/README.md",
        "description": "Main README with overview, features, and quick start"
    },
    {
        "name": "getting-started",
        "url": "https://raw.githubusercontent.com/date-fns/date-fns/main/docs/gettingStarted.md",
        "description": "Getting started guide with examples"
    },
    {
        "name": "fp",
        "url": "https://raw.githubusercontent.com/date-fns/date-fns/main/docs/fp.md",
        "description": "Functional programming guide"
    },
    {
        "name": "i18n",
        "url": "https://raw.githubusercontent.com/date-fns/date-fns/main/docs/i18n.md",
        "description": "Internationalization guide"
    },
    {
        "name": "time-zones",
        "url": "https://raw.githubusercontent.com/date-fns/date-fns/main/docs/timeZones.md",
        "description": "Time zones support and usage"
    },
    {
        "name": "unicode-tokens",
        "url": "https://raw.githubusercontent.com/date-fns/date-fns/main/docs/unicodeTokens.md",
        "description": "Unicode tokens for formatting"
    },
    {
        "name": "webpack",
        "url": "https://raw.githubusercontent.com/date-fns/date-fns/main/docs/webpack.md",
        "description": "Webpack configuration and optimization"
    },
    {
        "name": "cdn",
        "url": "https://raw.githubusercontent.com/date-fns/date-fns/main/docs/cdn.md",
        "description": "CDN usage guide"
    },
    {
        "name": "i18n-contribution",
        "url": "https://raw.githubusercontent.com/date-fns/date-fns/main/docs/i18nContributionGuide.md",
        "description": "Internationalization contribution guide"
    },
    {
        "name": "release",
        "url": "https://raw.githubusercontent.com/date-fns/date-fns/main/docs/release.md",
        "description": "Release process documentation"
    },
]


def download_doc(doc_info, output_dir):
    """Download a documentation file from GitHub and save as markdown."""
    try:
        name = doc_info["name"]
        url = doc_info["url"]
        description = doc_info["description"]

        print(f"Downloading: {name} ({description})")

        response = requests.get(url, timeout=15)
        response.raise_for_status()

        markdown_content = response.text

        # Add metadata header
        header = f"""# date-fns - {name}
# Source: {url}
# Description: {description}

"""
        markdown_content = header + markdown_content

        # Create output file
        output_path = output_dir / f"{name}.md"
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(markdown_content)

        print(f"  -> Saved: {output_path}")
        return True

    except requests.exceptions.RequestException as e:
        print(f"  -> Error downloading {url}: {e}")
        return False
    except Exception as e:
        print(f"  -> Error processing {url}: {e}")
        return False


def main():
    """Main function to download all date-fns documentation."""
    print("=" * 60)
    print("date-fns Documentation Scraper")
    print("=" * 60)
    print(f"Documentation files to download: {len(DATE_FNS_DOCS)}")
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "web-scraped" / "date-fns"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Output directory: {output_dir}")
    print()

    successful = 0
    failed = 0
    start_time = time.time()

    for i, doc_info in enumerate(DATE_FNS_DOCS, 1):
        print(f"[{i:2d}/{len(DATE_FNS_DOCS)}] ", end="")

        if download_doc(doc_info, output_dir):
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
        print(f"Warning: {failed} documentation files failed to download")
        sys.exit(1)
    else:
        print("All documentation downloaded successfully!")
        sys.exit(0)


if __name__ == "__main__":
    main()
