#!/usr/bin/env python3
"""
Fastify Documentation Scraper
Downloads Fastify web framework documentation from GitHub repository and converts to markdown.
Fastify is a fast and low overhead web framework for Node.js.
"""

import os
import sys
import requests
from pathlib import Path
import time
import json

# Base URL for Fastify GitHub repository
RAW_BASE_URL = "https://raw.githubusercontent.com/fastify/fastify/main"

# Known documentation files based on repository structure
# This avoids hitting GitHub API rate limits
DOCS_FILES = [
    "README.md",
    "docs/index.md",
    # Guides
    "docs/Guides/Index.md",
    "docs/Guides/Getting-Started.md",
    "docs/Guides/Benchmarking.md",
    "docs/Guides/Contributing.md",
    "docs/Guides/Database.md",
    "docs/Guides/Delay-Accepting-Requests.md",
    "docs/Guides/Detecting-When-Clients-Abort.md",
    "docs/Guides/Ecosystem.md",
    "docs/Guides/Fluent-Schema.md",
    "docs/Guides/Migration-Guide-V3.md",
    "docs/Guides/Migration-Guide-V4.md",
    "docs/Guides/Migration-Guide-V5.md",
    "docs/Guides/Plugins-Guide.md",
    "docs/Guides/Prototype-Poisoning.md",
    "docs/Guides/Recommendations.md",
    "docs/Guides/Serverless.md",
    "docs/Guides/Style-Guide.md",
    "docs/Guides/Testing.md",
    "docs/Guides/Write-Plugin.md",
    "docs/Guides/Write-Type-Provider.md",
    # Reference documentation
    "docs/Reference/ContentTypeParser.md",
    "docs/Reference/Decorators.md",
    "docs/Reference/Encapsulation.md",
    "docs/Reference/Errors.md",
    "docs/Reference/Hooks.md",
    "docs/Reference/HTTP2.md",
    "docs/Reference/LTS.md",
    "docs/Reference/Lifecycle.md",
    "docs/Reference/Logging.md",
    "docs/Reference/Middleware.md",
    "docs/Reference/Plugins.md",
    "docs/Reference/Reply.md",
    "docs/Reference/Request.md",
    "docs/Reference/Routes.md",
    "docs/Reference/Server.md",
    "docs/Reference/TypeScript.md",
    "docs/Reference/Validation-and-Serialization.md",
]


def download_file(repo_path, output_path):
    """Download a markdown/MDX file from GitHub repository."""
    try:
        raw_url = f"{RAW_BASE_URL}/{repo_path}"

        print(f"  Downloading: {repo_path}")

        response = requests.get(raw_url, timeout=15)
        response.raise_for_status()

        content = response.text

        # Add metadata header
        header = f"""# Fastify Documentation
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
    """Main function to download all Fastify documentation."""
    print("=" * 60)
    print("Fastify Documentation Scraper")
    print("=" * 60)
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "web-scraped" / "fastify"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Output directory: {output_dir}")
    print()

    print(f"Downloading {len(DOCS_FILES)} documentation files...")
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
            # docs/Guides/Getting-Started.md -> docs-Guides-Getting-Started.md
            output_filename = repo_path.replace("/", "-")
            # Convert .mdx to .md for consistency
            if output_filename.endswith(".mdx"):
                output_filename = output_filename[:-4] + ".md"

        output_path = output_dir / output_filename

        if download_file(repo_path, output_path):
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
