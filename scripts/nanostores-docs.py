#!/usr/bin/env python3
"""
Nano Stores Documentation Scraper
Downloads Nano Stores documentation from GitHub repositories and converts to markdown.
Nano Stores is a tiny state manager for React, Vue, Svelte, and vanilla JS.
"""

import os
import sys
import requests
from pathlib import Path
import time
import re

# Nano Stores repositories and their READMEs
NANOSTORES_REPOS = [
    {
        "name": "nanostores",
        "url": "https://raw.githubusercontent.com/nanostores/nanostores/main/README.md",
        "description": "Core library - atoms, maps, computed stores, effects"
    },
    {
        "name": "router",
        "url": "https://raw.githubusercontent.com/nanostores/router/main/README.md",
        "description": "URL router for Nano Stores"
    },
    {
        "name": "persistent",
        "url": "https://raw.githubusercontent.com/nanostores/persistent/main/README.md",
        "description": "Persistent storage with localStorage/sessionStorage"
    },
    {
        "name": "query",
        "url": "https://raw.githubusercontent.com/nanostores/query/main/README.md",
        "description": "Query store for data fetching and caching"
    },
    {
        "name": "i18n",
        "url": "https://raw.githubusercontent.com/nanostores/i18n/main/README.md",
        "description": "Internationalization utilities"
    },
    {
        "name": "deepmap",
        "url": "https://raw.githubusercontent.com/nanostores/deepmap/main/README.md",
        "description": "Deep object stores with nested updates"
    },
    {
        "name": "media-query",
        "url": "https://raw.githubusercontent.com/nanostores/media-query/main/README.md",
        "description": "CSS media query stores"
    },
    {
        "name": "react",
        "url": "https://raw.githubusercontent.com/nanostores/react/main/README.md",
        "description": "React integration hooks"
    },
    {
        "name": "vue",
        "url": "https://raw.githubusercontent.com/nanostores/vue/main/README.md",
        "description": "Vue composables"
    },
    {
        "name": "solid",
        "url": "https://raw.githubusercontent.com/nanostores/solid/master/README.md",
        "description": "Solid.js integration"
    },
    {
        "name": "lit",
        "url": "https://raw.githubusercontent.com/nanostores/lit/main/readme.md",
        "description": "Lit reactive controllers"
    },
    {
        "name": "angular",
        "url": "https://raw.githubusercontent.com/nanostores/angular/main/README.md",
        "description": "Angular service integration"
    },
    {
        "name": "preact",
        "url": "https://raw.githubusercontent.com/nanostores/preact/main/README.md",
        "description": "Preact integration hooks"
    },
]


def download_readme(repo_info, output_dir):
    """Download a README from GitHub and save as markdown."""
    try:
        name = repo_info["name"]
        url = repo_info["url"]
        description = repo_info["description"]

        print(f"Downloading: {name} ({description})")

        response = requests.get(url, timeout=15)
        response.raise_for_status()

        markdown_content = response.text

        # Add metadata header
        header = f"""# Nano Stores - {name}
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
    """Main function to download all Nano Stores documentation."""
    print("=" * 60)
    print("Nano Stores Documentation Scraper")
    print("=" * 60)
    print(f"Repositories to download: {len(NANOSTORES_REPOS)}")
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "web-scraped" / "nanostores"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Output directory: {output_dir}")
    print()

    successful = 0
    failed = 0
    start_time = time.time()

    for i, repo_info in enumerate(NANOSTORES_REPOS, 1):
        print(f"[{i:2d}/{len(NANOSTORES_REPOS)}] ", end="")

        if download_readme(repo_info, output_dir):
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
        print(f"Warning: {failed} repositories failed to download")
        sys.exit(1)
    else:
        print("All documentation downloaded successfully!")
        sys.exit(0)


if __name__ == "__main__":
    main()
