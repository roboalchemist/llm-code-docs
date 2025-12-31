#!/usr/bin/env python3
"""
React Cosmos Documentation Scraper
Downloads react-cosmos documentation from GitHub repository and converts to markdown.
React Cosmos is a sandbox for developing and testing UI components in isolation.
"""

import os
import sys
import requests
from pathlib import Path
import time

# Base URL for react-cosmos GitHub repository
BASE_URL = "https://api.github.com/repos/react-cosmos/react-cosmos/contents"
RAW_BASE_URL = "https://raw.githubusercontent.com/react-cosmos/react-cosmos/main"

# Files to download (verified to exist)
FILES_TO_DOWNLOAD = [
    "README.md",
    "docs/pages/docs/getting-started/vite.mdx",
    "docs/pages/docs/getting-started/webpack.mdx",
    "docs/pages/docs/getting-started/react-native.mdx",
    "docs/pages/docs/getting-started/next.mdx",
    "docs/pages/docs/getting-started/create-react-app.mdx",
    "docs/pages/docs/getting-started/custom-bundler.mdx",
    "docs/pages/docs/getting-started/troubleshooting.mdx",
    "docs/pages/docs/migration-guide.mdx",
    "docs/pages/docs/user-interface.mdx",
    "docs/pages/docs/cli.mdx",
    "docs/pages/docs/fixtures.mdx",
    "docs/pages/docs/fixtures/fixture-modules.mdx",
    "docs/pages/docs/fixtures/file-conventions.mdx",
    "docs/pages/docs/fixtures/decorators.mdx",
    "docs/pages/docs/fixtures/fixture-options.mdx",
    "docs/pages/docs/fixtures/fixture-inputs.mdx",
    "docs/pages/docs/fixtures/viewport.mdx",
    "docs/pages/docs/configuration/cosmos-config.mdx",
    "docs/pages/docs/static-export.mdx",
    "docs/pages/docs/plugins.mdx",
    "packages/react-cosmos-core/src/userModules/fixtureTypes.ts",
]


def download_file(repo_path, output_path):
    """Download a file from GitHub repository."""
    try:
        raw_url = f"{RAW_BASE_URL}/{repo_path}"

        print(f"  Downloading: {repo_path}")

        response = requests.get(raw_url, timeout=15)
        response.raise_for_status()

        content = response.text

        # Add metadata header
        header = f"""# React Cosmos Documentation
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
    """Main function to download all react-cosmos documentation."""
    print("=" * 60)
    print("React Cosmos Documentation Scraper")
    print("=" * 60)
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "web-scraped" / "react-cosmos"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Output directory: {output_dir}")
    print()

    successful = 0
    failed = 0
    start_time = time.time()

    for idx, repo_path in enumerate(FILES_TO_DOWNLOAD, 1):
        print(f"[{idx:2d}/{len(FILES_TO_DOWNLOAD)}] ", end="")

        # Create output filename from repo_path
        if repo_path == "README.md":
            output_filename = "main-README.md"
        elif repo_path.startswith("docs/pages/"):
            # docs/pages/docs/getting-started/vite.mdx -> docs-getting-started-vite.mdx
            output_filename = repo_path.replace("docs/pages/", "").replace("/", "-")
        elif repo_path.startswith("packages/"):
            # packages/react-cosmos-core/src/userModules/fixtureTypes.ts -> packages-react-cosmos-core-fixtureTypes.ts
            parts = repo_path.split("/")
            package_name = parts[1]  # react-cosmos-core
            file_name = parts[-1]  # fixtureTypes.ts
            output_filename = f"packages-{package_name}-{file_name}"
        else:
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
    total_size = sum(f.stat().st_size for f in output_dir.glob("*") if f.is_file())
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
