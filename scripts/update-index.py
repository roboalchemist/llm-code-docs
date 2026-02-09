#!/usr/bin/env python3
"""
Documentation Index Generator
Scans the docs directory and generates index.yaml
"""

import os
import yaml
from pathlib import Path
from datetime import datetime


def get_dir_stats(path):
    """Get file count and total size for a directory."""
    if not path.exists():
        return 0, 0

    md_files = list(path.glob("**/*.md"))
    mdx_files = list(path.glob("**/*.mdx"))
    rst_files = list(path.glob("**/*.rst"))
    txt_files = list(path.glob("**/*.txt"))
    sy_files = list(path.glob("**/*.sy"))
    json_files = list(path.glob("**/*.json"))
    all_files = md_files + mdx_files + rst_files + txt_files + sy_files + json_files

    file_count = len(all_files)
    total_size = sum(f.stat().st_size for f in all_files)
    return file_count, total_size


def format_size(size_bytes):
    """Format size in bytes to human readable format."""
    if size_bytes < 1024:
        return f"{size_bytes}B"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.1f}KB"
    else:
        return f"{size_bytes / (1024 * 1024):.1f}MB"


def scan_web_scraped(docs_dir):
    """Scan web-scraped documentation directories."""
    web_scraped_dir = docs_dir / "web-scraped"
    if not web_scraped_dir.exists():
        return []

    entries = []
    for subdir in sorted(web_scraped_dir.iterdir()):
        if not subdir.is_dir():
            continue

        name = subdir.name
        file_count, size = get_dir_stats(subdir)

        if file_count > 0:
            entries.append({
                'name': name,
                'description': f'{name} documentation',
                'path': f'docs/web-scraped/{name}/',
                'status': 'fetched',
                'file_count': file_count,
                'size': format_size(size),
                'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M')
            })

    return entries


def scan_llms_txt(docs_dir):
    """Scan llms-txt documentation directories."""
    llms_txt_dir = docs_dir / "llms-txt"
    if not llms_txt_dir.exists():
        return []

    entries = []
    for subdir in sorted(llms_txt_dir.iterdir()):
        if not subdir.is_dir():
            continue

        name = subdir.name
        file_count, size = get_dir_stats(subdir)

        if file_count > 0:
            # Try to get description from first file
            first_file = next(subdir.glob("**/*.md"), None) or next(subdir.glob("**/*.mdx"), None)
            description = f'{name} documentation'

            if first_file:
                try:
                    with open(first_file, 'r', encoding='utf-8') as f:
                        for line in f:
                            if line.startswith('# ') and not line.startswith('# Source:') and not line.startswith('# Path:'):
                                description = line[2:].strip()
                                break
                except:
                    pass

            entries.append({
                'name': name,
                'description': description[:100] + ('...' if len(description) > 100 else ''),
                'url': f'https://{name}.com/',  # Placeholder
                'path': f'docs/llms-txt/{name}/',
                'status': 'fetched',
                'file_count': file_count,
                'size': format_size(size),
                'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M')
            })

    return entries


def scan_github_scraped(docs_dir):
    """Scan github-scraped documentation directories."""
    github_dir = docs_dir / "github-scraped"
    if not github_dir.exists():
        return []

    entries = []
    for subdir in sorted(github_dir.iterdir()):
        if not subdir.is_dir():
            continue

        name = subdir.name
        file_count, size = get_dir_stats(subdir)

        if file_count > 0:
            entries.append({
                'name': name,
                'description': f'{name} from GitHub',
                'path': f'docs/github-scraped/{name}/',
                'status': 'fetched',
                'file_count': file_count,
                'size': format_size(size),
                'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M')
            })

    return entries


def main():
    """Generate index.yaml from documentation directories."""
    script_dir = Path(__file__).parent.parent
    docs_dir = script_dir / "docs"
    index_path = script_dir / "index.yaml"

    print("Scanning documentation directories...")

    # Scan all documentation types
    llms_txt_entries = scan_llms_txt(docs_dir)
    github_entries = scan_github_scraped(docs_dir)
    web_scraped_entries = scan_web_scraped(docs_dir)

    # Calculate totals
    total_llms = len(llms_txt_entries)
    total_github = len(github_entries)
    total_web = len(web_scraped_entries)
    total_sources = total_llms + total_github + total_web

    # Build index structure
    index = {
        'metadata': {
            'last_updated': datetime.now().strftime('%Y-%m-%d %H:%M'),
            'total_sources': total_sources,
            'total_fetched': total_sources,
            'llms_txt_count': total_llms,
            'llms_txt_fetched': total_llms,
            'github_count': total_github,
            'github_fetched': total_github,
            'web_scraped_count': total_web,
            'web_scraped_fetched': total_web,
        },
        'llms_txt': llms_txt_entries,
        'github_scraped': github_entries,
        'web_scraped': web_scraped_entries,
    }

    # Write index
    print(f"\nWriting index to {index_path}")
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write("# Documentation Index\n")
        f.write("# Auto-generated by scripts/update-index.py\n")
        f.write("# Do not edit manually - changes will be overwritten\n")
        f.write("#\n")
        f.write("# Status values:\n")
        f.write("#   - fetched: Documentation successfully downloaded\n")
        f.write("#   - pending: Configuration exists but not yet fetched\n\n")
        yaml.dump(index, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    print("\nIndex Summary:")
    print(f"  LLMs.txt sources: {total_llms}")
    print(f"  GitHub sources: {total_github}")
    print(f"  Web scraped sources: {total_web}")
    print(f"  Total sources: {total_sources}")
    print(f"\nIndex updated successfully!")


if __name__ == "__main__":
    main()
