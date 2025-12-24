#!/usr/bin/env python3
"""
Mozilla Common Voice Documentation Scraper
Downloads documentation from Common Voice GitHub repositories.
Common Voice is Mozilla's initiative to help teach machines how real people speak.
"""

import os
import sys
import requests
from pathlib import Path
import time

# Documentation files from the main common-voice/common-voice repository
MAIN_REPO_DOCS = [
    "docs/API/statistics.md",
    "docs/CHANGELOG.md",
    "docs/CODE_OF_CONDUCT.md",
    "docs/COMMUNITIES.md",
    "docs/DEVELOPMENT.md",
    "docs/EMAIL.md",
    "docs/HOWTO_S3.md",
    "docs/LANGUAGE.md",
    "docs/SENTENCES.md",
    "docs/data_dictionary.md",
    "docs/languages/README.md",
    "docs/submitting-bulk-sentences.md",
    "docs/taxonomies/du-covid-keywords.md",
    "docs/taxonomies/singleword-benchmark.md",
]

# Top-level markdown files from main repo
MAIN_REPO_ROOT = [
    "README.md",
]

# Documentation files from the community-playbook repository
PLAYBOOK_DOCS = [
    "README.md",
    "SUMMARY.md",
    "language/language-communities-+-contributors.md",
    "language/language-communities-+-contributors/README.md",
    "language/language-communities-+-contributors/diversity-equity-and-inclusion.md",
    "language/language-communities-+-contributors/language-communities.md",
    "language/language-communities-+-contributors/open-leadership.md",
    "language/language-communities-+-contributors/open-source-newbie.md",
    "language/localization/README.md",
    "language/localization/case-studies.md",
    "language/text-corpus/README.md",
    "language/text-corpus/case-studies.md",
    "language/voice-corpus/README.md",
    "language/voice-corpus/case-studies.md",
    "sub_pages/Lang_Variant.md",
    "sub_pages/Localization.md",
    "sub_pages/campaign_guidelines.md",
    "sub_pages/cc0waiver_process.md",
    "sub_pages/communities.md",
    "sub_pages/maintenance.md",
    "sub_pages/mobilization.md",
    "sub_pages/onboarding.md",
    "sub_pages/text.md",
    "sub_pages/voice.md",
]

MAIN_REPO_RAW = "https://raw.githubusercontent.com/common-voice/common-voice/main"
PLAYBOOK_RAW = "https://raw.githubusercontent.com/common-voice/community-playbook/master"


def download_file(url, output_path):
    """Download a file and add source header."""
    try:
        print(f"Downloading: {url}")
        response = requests.get(url, timeout=15)
        response.raise_for_status()

        content = response.text

        # Add source header
        content = f"# Source: {url}\n\n{content}"

        # Create directory if needed
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # Write file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"  -> Saved: {output_path}")
        return True

    except requests.exceptions.RequestException as e:
        print(f"  -> Error downloading {url}: {e}")
        return False
    except Exception as e:
        print(f"  -> Error processing {url}: {e}")
        return False


def path_to_filename(path, prefix=""):
    """Convert path to flat filename."""
    if prefix:
        path = f"{prefix}-{path}"

    # Remove leading slashes
    path = path.lstrip("/")

    # Convert slashes to dashes for flat structure
    filename = path.replace("/", "-")

    # Ensure .md extension
    if not filename.endswith(".md"):
        filename += ".md"

    return filename


def main():
    """Main function to download all Common Voice documentation."""
    print("=" * 60)
    print("Mozilla Common Voice Documentation Scraper")
    print("=" * 60)
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "github-scraped" / "common-voice"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Output directory: {output_dir}")
    print()

    successful = 0
    failed = 0
    start_time = time.time()

    # Download main repo docs
    print("=" * 60)
    print("Downloading from common-voice/common-voice repository...")
    print("=" * 60)

    all_main_files = MAIN_REPO_ROOT + MAIN_REPO_DOCS
    for i, file_path in enumerate(all_main_files, 1):
        url = f"{MAIN_REPO_RAW}/{file_path}"
        filename = path_to_filename(file_path, prefix="main")
        output_path = output_dir / filename

        print(f"[{i:2d}/{len(all_main_files)}] ", end="")

        if download_file(url, output_path):
            successful += 1
        else:
            failed += 1

        time.sleep(0.3)

    # Download community playbook docs
    print()
    print("=" * 60)
    print("Downloading from community-playbook repository...")
    print("=" * 60)

    for i, file_path in enumerate(PLAYBOOK_DOCS, 1):
        url = f"{PLAYBOOK_RAW}/{file_path}"
        filename = path_to_filename(file_path, prefix="playbook")
        output_path = output_dir / filename

        print(f"[{i:2d}/{len(PLAYBOOK_DOCS)}] ", end="")

        if download_file(url, output_path):
            successful += 1
        else:
            failed += 1

        time.sleep(0.3)

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
