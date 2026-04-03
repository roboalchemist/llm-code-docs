#!/usr/bin/env python3
"""
Lucia Authentication Documentation Scraper
Downloads Lucia authentication library documentation from GitHub repository and converts to markdown.
Lucia is an open source resource on implementing authentication with JavaScript.
"""

import os
import sys
import requests
from pathlib import Path
import time
import json

# Base URL for Lucia GitHub repository
BASE_URL = "https://api.github.com/repos/lucia-auth/lucia/contents"
RAW_BASE_URL = "https://raw.githubusercontent.com/lucia-auth/lucia/main"

# All markdown files we want to download
DOCS_FILES = [
    "README.md",
    "pages/index.md",
    "pages/examples/email-password-2fa-webauthn.md",
    "pages/examples/email-password-2fa.md",
    "pages/examples/github-oauth.md",
    "pages/examples/google-oauth.md",
    "pages/lucia-v3/migrate.md",
    "pages/rate-limit/token-bucket.md",
    "pages/sessions/basic.md",
    "pages/sessions/frameworks/index.md",
    "pages/sessions/frameworks/nextjs.md",
    "pages/sessions/frameworks/sveltekit.md",
    "pages/sessions/inactivity-timeout.md",
    "pages/sessions/overview.md",
    "pages/sessions/stateless-tokens.md",
    "pages/tutorials/github-oauth/astro.md",
    "pages/tutorials/github-oauth/index.md",
    "pages/tutorials/github-oauth/nextjs.md",
    "pages/tutorials/github-oauth/sveltekit.md",
    "pages/tutorials/google-oauth/astro.md",
    "pages/tutorials/google-oauth/index.md",
    "pages/tutorials/google-oauth/nextjs.md",
    "pages/tutorials/google-oauth/sveltekit.md",
]


def download_file(repo_path, output_path):
    """Download a markdown file from GitHub repository."""
    try:
        raw_url = f"{RAW_BASE_URL}/{repo_path}"

        print(f"  Downloading: {repo_path}")

        response = requests.get(raw_url, timeout=15)
        response.raise_for_status()

        content = response.text

        # Add metadata header
        header = f"""# Lucia Authentication Documentation
# Source: {raw_url}
# Path: {repo_path}

"""
        content = header + content

        # Create output file
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"    -> Saved: {output_path}")
        return True

    except requests.exceptions.RequestException as e:
        print(f"    -> Error downloading {repo_path}: {e}")
        return False
    except Exception as e:
        print(f"    -> Error processing {repo_path}: {e}")
        return False


def main():
    """Main function to download all Lucia documentation."""
    print("=" * 60)
    print("Lucia Authentication Documentation Scraper")
    print("=" * 60)
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "web-scraped" / "lucia"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Output directory: {output_dir}")
    print()

    print(f"Found {len(DOCS_FILES)} markdown files to download")
    print()

    successful = 0
    failed = 0
    start_time = time.time()

    for idx, repo_path in enumerate(DOCS_FILES, 1):
        print(f"[{idx:2d}/{len(DOCS_FILES)}] ", end="")

        # Create category-based output filename
        if repo_path == "README.md":
            output_filename = "main-README.md"
        else:
            # pages/sessions/basic.md -> pages-sessions-basic.md
            output_filename = repo_path.replace("/", "-")

        output_path = output_dir / output_filename

        if download_file(repo_path, output_path):
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
        print(f"Warning: {failed} files failed to download")
        sys.exit(1)
    else:
        print("All documentation downloaded successfully!")
        sys.exit(0)


if __name__ == "__main__":
    main()
