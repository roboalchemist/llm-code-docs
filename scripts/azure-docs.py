#!/usr/bin/env python3
"""
Azure Documentation Scraper
Downloads Azure documentation from Microsoft's GitHub repository and converts to markdown.
Focuses on core Azure services documentation for LLM consumption.
Source: https://github.com/MicrosoftDocs/azure-docs
"""

import os
import sys
import requests
from pathlib import Path
import time
import json

# Base URL for Azure docs GitHub repository
BASE_URL = "https://api.github.com/repos/MicrosoftDocs/azure-docs/contents"
RAW_BASE_URL = "https://raw.githubusercontent.com/MicrosoftDocs/azure-docs/main"

# Key Azure documentation directories to scrape
# These map to major service categories
AZURE_DOCS_DIRS = {
    # Core services
    "virtual-machines": "articles/virtual-machines",
    "app-service": "articles/app-service",
    "functions": "articles/azure-functions",
    "container-instances": "articles/container-instances",
    "kubernetes": "articles/aks",

    # Storage
    "storage": "articles/storage",
    "cosmos-db": "articles/cosmos-db",

    # Networking
    "virtual-network": "articles/virtual-network",
    "load-balancer": "articles/load-balancer",
    "application-gateway": "articles/application-gateway",

    # Identity & Security
    "key-vault": "articles/key-vault",

    # Databases
    "sql-database": "articles/azure-sql",
    "postgresql": "articles/postgresql",

    # Developer Tools
    "resource-manager": "articles/azure-resource-manager",

    # AI & ML
    "ai-services": "articles/ai-services",
    "openai": "articles/ai-services/openai",

    # Monitoring
    "monitor": "articles/azure-monitor",
}

# Limit files per directory to avoid overwhelming the docs
MAX_FILES_PER_DIR = 50


def get_markdown_files_in_dir(dir_path, category_name):
    """Get markdown files from a directory in the GitHub repo."""
    try:
        url = f"{BASE_URL}/{dir_path}"
        print(f"  Fetching directory: {category_name} ({dir_path})")

        response = requests.get(url, timeout=15)

        # Handle rate limiting
        if response.status_code == 403:
            print(f"    -> Rate limited, waiting 60 seconds...")
            time.sleep(60)
            response = requests.get(url, timeout=15)

        response.raise_for_status()
        contents = response.json()

        # Filter for markdown files (not subdirectories)
        md_files = []
        for item in contents:
            if item["type"] == "file" and item["name"].endswith(".md"):
                # Skip TOC and includes files
                if item["name"].lower() in ["toc.md", "toc.yml"] or item["name"].startswith("_"):
                    continue
                md_files.append({
                    "path": item["path"],
                    "name": item["name"],
                    "download_url": item["download_url"]
                })

        # Limit to avoid too many files
        if len(md_files) > MAX_FILES_PER_DIR:
            print(f"    -> Found {len(md_files)} files, limiting to {MAX_FILES_PER_DIR}")
            # Prioritize overview/README files first
            priority_files = [f for f in md_files if any(x in f["name"].lower() for x in ["overview", "readme", "index", "intro"])]
            other_files = [f for f in md_files if f not in priority_files]
            md_files = priority_files + other_files[:MAX_FILES_PER_DIR - len(priority_files)]

        print(f"    -> Found {len(md_files)} markdown files")
        return md_files

    except requests.exceptions.RequestException as e:
        print(f"    -> Error fetching directory: {e}")
        return []
    except Exception as e:
        print(f"    -> Error processing directory: {e}")
        return []


def download_file(file_info, output_path, category_name):
    """Download a markdown file from GitHub."""
    try:
        print(f"    Downloading: {file_info['name']}")

        response = requests.get(file_info["download_url"], timeout=15)
        response.raise_for_status()

        content = response.text

        # Add metadata header
        header = f"""# Azure Documentation: {category_name.replace('-', ' ').title()}
# Source: https://github.com/MicrosoftDocs/azure-docs/blob/main/{file_info['path']}
# File: {file_info['name']}

---

"""
        content = header + content

        # Create output file
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)

        return True

    except requests.exceptions.RequestException as e:
        print(f"      -> Error downloading: {e}")
        return False
    except Exception as e:
        print(f"      -> Error processing: {e}")
        return False


def main():
    """Main function to download Azure documentation."""
    print("=" * 60)
    print("Azure Documentation Scraper")
    print("=" * 60)
    print()
    print("Source: https://github.com/MicrosoftDocs/azure-docs")
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "web-scraped" / "azure"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Output directory: {output_dir}")
    print(f"Scraping {len(AZURE_DOCS_DIRS)} Azure service categories")
    print()

    successful = 0
    failed = 0
    start_time = time.time()

    for idx, (category, dir_path) in enumerate(AZURE_DOCS_DIRS.items(), 1):
        print(f"[{idx:2d}/{len(AZURE_DOCS_DIRS)}] Processing: {category}")

        # Get all markdown files in this directory
        md_files = get_markdown_files_in_dir(dir_path, category)

        if not md_files:
            print(f"    -> No files found, skipping")
            failed += 1
            continue

        # Download each file
        for file_idx, file_info in enumerate(md_files, 1):
            # Create output filename with category prefix
            output_filename = f"{category}_{file_info['name']}"
            output_path = output_dir / output_filename

            if download_file(file_info, output_path, category):
                successful += 1
            else:
                failed += 1

            # Rate limiting - be respectful to GitHub API
            if file_idx % 10 == 0:
                print(f"    -> Progress: {file_idx}/{len(md_files)} files")
            time.sleep(0.5)

        print()
        # Pause between categories
        time.sleep(2)

    elapsed = time.time() - start_time

    print()
    print("=" * 60)
    print("Download Summary")
    print("=" * 60)
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    print(f"Time: {elapsed:.1f} seconds ({elapsed/60:.1f} minutes)")
    print(f"Output: {output_dir}")

    # Calculate total size
    total_size = sum(f.stat().st_size for f in output_dir.glob("*.md"))
    print(f"Total size: {total_size:,} bytes ({total_size/1024/1024:.1f} MB)")

    print()
    if successful == 0:
        print("Error: No files were downloaded successfully")
        sys.exit(1)
    elif failed > successful:
        print(f"Warning: More failures ({failed}) than successes ({successful})")
        sys.exit(1)
    else:
        print(f"Documentation downloaded successfully! ({successful} files)")
        if failed > 0:
            print(f"Note: {failed} files failed to download")
        sys.exit(0)


if __name__ == "__main__":
    main()
