#!/usr/bin/env python3
"""
openWakeWord Documentation Scraper
Downloads all openWakeWord documentation from GitHub repository.
openWakeWord is an open-source wake word detection library.
"""

import sys
import time
from pathlib import Path

import requests

# GitHub raw content base URL
BASE_URL = "https://raw.githubusercontent.com/dscripka/openWakeWord/main"

# Documentation files to download
OPENWAKEWORD_DOC_FILES = [
    # Main README
    ("README.md", "readme.md"),
    # Docs folder
    ("docs/custom_verifier_models.md", "custom-verifier-models.md"),
    ("docs/synthetic_data_generation.md", "synthetic-data-generation.md"),
    # Model documentation
    ("docs/models/alexa.md", "models-alexa.md"),
    ("docs/models/hey_jarvis.md", "models-hey-jarvis.md"),
    ("docs/models/hey_mycroft.md", "models-hey-mycroft.md"),
    ("docs/models/timers.md", "models-timers.md"),
    ("docs/models/weather.md", "models-weather.md"),
]


def download_file(source_path: str, output_path: Path) -> bool:
    """Download a markdown file from GitHub."""
    url = f"{BASE_URL}/{source_path}"
    try:
        print(f"Downloading: {source_path}")

        response = requests.get(url, timeout=15)
        response.raise_for_status()

        content = response.text

        # Add source header
        full_url = f"https://github.com/dscripka/openWakeWord/blob/main/{source_path}"
        header = f"# Source: {full_url}\n\n"

        # Write with header
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(header + content, encoding='utf-8')

        print(f"  -> Saved: {output_path.name}")
        return True

    except requests.exceptions.RequestException as e:
        print(f"  -> Error downloading {url}: {e}")
        return False
    except Exception as e:
        print(f"  -> Error processing {url}: {e}")
        return False


def main():
    """Main function to download all openWakeWord documentation."""
    print("=" * 60)
    print("openWakeWord Documentation Scraper")
    print("=" * 60)
    print(f"Source: GitHub (dscripka/openWakeWord)")
    print(f"Files to download: {len(OPENWAKEWORD_DOC_FILES)}")
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "github-repos" / "openwakeword"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Output directory: {output_dir}")
    print()

    successful = 0
    failed = 0
    start_time = time.time()

    for i, (source_path, output_name) in enumerate(OPENWAKEWORD_DOC_FILES, 1):
        output_path = output_dir / output_name

        print(f"[{i:2d}/{len(OPENWAKEWORD_DOC_FILES)}] ", end="")

        if download_file(source_path, output_path):
            successful += 1
        else:
            failed += 1

        # Rate limiting
        time.sleep(0.2)

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
        print("All files downloaded successfully!")
        sys.exit(0)


if __name__ == "__main__":
    main()
