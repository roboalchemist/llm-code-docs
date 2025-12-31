#!/usr/bin/env python3
"""
Panda CSS Documentation Scraper
Downloads Panda CSS documentation from llms.txt standard URLs.
Panda CSS is a CSS-in-JS framework with build-time optimizations for styling web applications.
"""

import os
import sys
import requests
from pathlib import Path
import time

# Base URL for Panda CSS llms.txt
BASE_URL = "https://panda-css.com"

# Documentation sections to download
DOCS_SECTIONS = [
    ("llms-full.txt", "complete.md"),  # Complete documentation
    ("llms.txt/overview", "overview.md"),
    ("llms.txt/installation", "installation.md"),
    ("llms.txt/concepts", "concepts.md"),
    ("llms.txt/theming", "theming.md"),
    ("llms.txt/utilities", "utilities.md"),
    ("llms.txt/customization", "customization.md"),
    ("llms.txt/guides", "guides.md"),
    ("llms.txt/migration", "migration.md"),
    ("llms.txt/references", "references.md"),
]


def download_section(section_url, output_filename):
    """Download a documentation section from Panda CSS."""
    try:
        url = f"{BASE_URL}/{section_url}"

        print(f"  Downloading: {section_url}")

        response = requests.get(url, timeout=15)
        response.raise_for_status()

        content = response.text

        # Add metadata header
        header = f"""# Panda CSS Documentation
# Source: {url}
# Section: {section_url}

"""
        content = header + content

        return content

    except requests.exceptions.RequestException as e:
        print(f"    -> Error downloading {section_url}: {e}")
        return None
    except Exception as e:
        print(f"    -> Error processing {section_url}: {e}")
        return None


def main():
    """Main function to download all Panda CSS documentation."""
    print("=" * 60)
    print("Panda CSS Documentation Scraper")
    print("=" * 60)
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "llms-txt" / "pandacss"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Output directory: {output_dir}")
    print()

    print(f"Downloading {len(DOCS_SECTIONS)} documentation sections...")
    print()

    successful = 0
    failed = 0
    start_time = time.time()

    for idx, (section_url, output_filename) in enumerate(DOCS_SECTIONS, 1):
        print(f"[{idx:2d}/{len(DOCS_SECTIONS)}] ", end="")

        output_path = output_dir / output_filename

        content = download_section(section_url, output_filename)

        if content:
            try:
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"    -> Saved: {output_path}")
                successful += 1
            except Exception as e:
                print(f"    -> Error writing file: {e}")
                failed += 1
        else:
            failed += 1

        # Be respectful with rate limiting
        if idx < len(DOCS_SECTIONS):
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
        print(f"Warning: {failed} files failed to download")
        sys.exit(1)
    else:
        print("All documentation downloaded successfully!")
        sys.exit(0)


if __name__ == "__main__":
    main()
