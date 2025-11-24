#!/usr/bin/env python3
"""
README Documentation Puller

Downloads individual README files from GitHub repositories and saves them
to the readmes/ directory with descriptive filenames.
"""

import os
import sys
import requests
from pathlib import Path
import time

# Configuration: List of README files to download
# Format: (url, output_filename)
READMES = [
    (
        "https://raw.githubusercontent.com/scientifichackers/ampy/refs/heads/master/README.md",
        "ampy.md"
    ),
    (
        "https://raw.githubusercontent.com/dhylands/rshell/refs/heads/master/README.rst",
        "rshell.rst"
    ),
]

def download_readme(url, output_filename):
    """Download a README file from URL and save to readmes directory."""
    output_dir = Path("web-scraped-docs/readmes")
    output_path = output_dir / output_filename

    try:
        print(f"Downloading: {url}")

        # Add timeout for the request
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        # Create directory if it doesn't exist
        output_dir.mkdir(parents=True, exist_ok=True)

        # Write the content to file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(response.text)

        file_size = output_path.stat().st_size
        print(f"  ✅ Saved to: {output_path} ({file_size:,} bytes)")
        return True

    except requests.exceptions.RequestException as e:
        print(f"  ❌ Error downloading {url}: {e}")
        return False
    except Exception as e:
        print(f"  ❌ Error saving {url}: {e}")
        return False

def main():
    """Main function to download all README files."""

    print("📚 README Documentation Puller")
    print("=" * 50)
    print(f"Downloading {len(READMES)} README file(s)")
    print()

    successful = 0
    failed = 0

    start_time = time.time()

    for i, (url, filename) in enumerate(READMES, 1):
        print(f"[{i}/{len(READMES)}] ", end="", flush=True)

        # Add small delay between requests to be respectful
        if i > 1:
            time.sleep(0.3)

        if download_readme(url, filename):
            successful += 1
        else:
            failed += 1

    # Final summary
    elapsed = time.time() - start_time

    print()
    print("=" * 50)
    print(f"📊 Download Summary")
    print("=" * 50)
    print(f"✅ Successful downloads:  {successful}")
    print(f"❌ Failed downloads:      {failed}")
    print(f"⏱️  Total time:            {elapsed:.1f} seconds")
    print(f"📁 Output directory:      web-scraped-docs/readmes/")

    # Calculate total size
    readme_dir = Path("web-scraped-docs/readmes")
    if readme_dir.exists():
        total_size = sum(f.stat().st_size for f in readme_dir.glob("*.md"))
        print(f"💾 Total documentation:   {total_size:,} bytes ({total_size/1024:.1f} KB)")

    print()

    if failed > 0:
        print(f"⚠️  {failed} download(s) failed - check network connection and URLs")
        sys.exit(1)
    else:
        print("🎉 All READMEs downloaded successfully!")
        sys.exit(0)

if __name__ == "__main__":
    main()
