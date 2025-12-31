#!/usr/bin/env python3
"""
next-intl Documentation Scraper
Downloads next-intl documentation from GitHub repository and converts to markdown.
next-intl is internationalization (i18n) for Next.js.
"""

import os
import sys
import requests
from pathlib import Path
import time

# Base URL for next-intl GitHub repository
RAW_BASE_URL = "https://raw.githubusercontent.com/amannn/next-intl/main"

# Known documentation files based on website structure
KNOWN_FILES = [
    # Main docs
    "docs/src/pages/docs/getting-started.mdx",
    "docs/src/pages/docs/getting-started/app-router.mdx",
    "docs/src/pages/docs/getting-started/pages-router.mdx",

    # Usage
    "docs/src/pages/docs/usage.mdx",
    "docs/src/pages/docs/usage/translations.mdx",
    "docs/src/pages/docs/usage/numbers.mdx",
    "docs/src/pages/docs/usage/dates-times.mdx",
    "docs/src/pages/docs/usage/lists.mdx",
    "docs/src/pages/docs/usage/configuration.mdx",
    "docs/src/pages/docs/usage/extraction.mdx",
    "docs/src/pages/docs/usage/plugin.mdx",

    # Routing
    "docs/src/pages/docs/routing.mdx",
    "docs/src/pages/docs/routing/setup.mdx",
    "docs/src/pages/docs/routing/configuration.mdx",
    "docs/src/pages/docs/routing/middleware.mdx",
    "docs/src/pages/docs/routing/navigation.mdx",

    # Environments
    "docs/src/pages/docs/environments.mdx",
    "docs/src/pages/docs/environments/server-client-components.mdx",
    "docs/src/pages/docs/environments/actions-metadata-route-handlers.mdx",
    "docs/src/pages/docs/environments/error-files.mdx",
    "docs/src/pages/docs/environments/testing.mdx",
    "docs/src/pages/docs/environments/core-library.mdx",
    "docs/src/pages/docs/environments/runtime-requirements.mdx",

    # Workflows
    "docs/src/pages/docs/workflows.mdx",
    "docs/src/pages/docs/workflows/typescript.mdx",
    "docs/src/pages/docs/workflows/localization-management.mdx",
    "docs/src/pages/docs/workflows/vscode-integration.mdx",
    "docs/src/pages/docs/workflows/storybook.mdx",
    "docs/src/pages/docs/workflows/messages.mdx",

    # Other
    "docs/src/pages/docs/design-principles.mdx",

    # Root README
    "README.md",
]


def try_download_file(repo_path, output_path):
    """Try to download a file from GitHub repository."""
    try:
        raw_url = f"{RAW_BASE_URL}/{repo_path}"

        print(f"  Trying: {repo_path}")

        response = requests.get(raw_url, timeout=15)

        if response.status_code == 404:
            print(f"    -> Not found (404)")
            return False

        response.raise_for_status()

        content = response.text

        # Add metadata header
        header = f"""# next-intl Documentation
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
        if "404" not in str(e):
            print(f"    -> Error downloading {repo_path}: {e}")
        return False
    except Exception as e:
        print(f"    -> Error processing {repo_path}: {e}")
        return False


def main():
    """Main function to download all next-intl documentation."""
    print("=" * 60)
    print("next-intl Documentation Scraper")
    print("=" * 60)
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "web-scraped" / "next-intl"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Output directory: {output_dir}")
    print()

    files_to_download = KNOWN_FILES

    print(f"\nAttempting to download {len(files_to_download)} files")
    print()

    successful = 0
    failed = 0
    start_time = time.time()

    for idx, repo_path in enumerate(files_to_download, 1):
        print(f"[{idx:2d}/{len(files_to_download)}] ", end="")

        # Create output filename
        if repo_path == "README.md":
            output_filename = "main-README.md"
        elif repo_path.startswith("docs/src/pages/docs/"):
            # Remove "docs/src/pages/docs/" prefix
            relative_path = repo_path.replace("docs/src/pages/docs/", "")
            # Replace slashes with dashes
            output_filename = relative_path.replace("/", "-")
        else:
            output_filename = repo_path.replace("/", "-")

        output_path = output_dir / output_filename

        if try_download_file(repo_path, output_path):
            successful += 1
        else:
            failed += 1

        # Be respectful with rate limiting
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
    total_size = sum(f.stat().st_size for f in output_dir.glob("*") if f.is_file())
    print(f"Total size: {total_size:,} bytes ({total_size/1024:.1f} KB)")

    print()
    if successful == 0:
        print("Error: No files downloaded successfully!")
        sys.exit(1)
    elif failed > successful:
        print(f"Warning: More failures ({failed}) than successes ({successful})")
        sys.exit(1)
    else:
        print(f"Documentation downloaded successfully! ({successful} files)")
        sys.exit(0)


if __name__ == "__main__":
    main()
