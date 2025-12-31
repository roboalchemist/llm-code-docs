#!/usr/bin/env python3
"""
Update index.yaml based on configuration files and actual documentation state.

Reads from:
- scripts/llms-sites.yaml (llms.txt documentation sources)
- scripts/repo_config.yaml (GitHub repository extractions)
- docs/web-scraped/ directory (web-scraped documentation)

Writes to:
- index.yaml (documentation catalog)

Usage:
    python3 scripts/update-index.py
"""

import os
import sys
from datetime import datetime
from pathlib import Path

import yaml

# Configuration
SCRIPT_DIR = Path(__file__).parent
REPO_ROOT = SCRIPT_DIR.parent
LLMS_SITES_CONFIG = SCRIPT_DIR / "llms-sites.yaml"
REPO_CONFIG = SCRIPT_DIR / "repo_config.yaml"
DOCS_DIR = REPO_ROOT / "docs"
INDEX_FILE = REPO_ROOT / "index.yaml"


def load_yaml(path: Path) -> dict:
    """Load a YAML file."""
    try:
        with open(path, 'r') as f:
            return yaml.safe_load(f) or {}
    except FileNotFoundError:
        print(f"Warning: {path} not found", file=sys.stderr)
        return {}
    except yaml.YAMLError as e:
        print(f"Error parsing {path}: {e}", file=sys.stderr)
        return {}


def get_dir_stats(dir_path: Path) -> dict:
    """Get statistics for a documentation directory."""
    if not dir_path.exists():
        return {
            "exists": False,
            "file_count": 0,
            "size_bytes": 0,
            "last_modified": None
        }

    file_count = 0
    total_size = 0
    latest_mtime = 0

    for file in dir_path.rglob("*"):
        if file.is_file() and file.suffix in ['.md', '.rst', '.txt', '.html']:
            file_count += 1
            total_size += file.stat().st_size
            mtime = file.stat().st_mtime
            if mtime > latest_mtime:
                latest_mtime = mtime

    return {
        "exists": True,
        "file_count": file_count,
        "size_bytes": total_size,
        "last_modified": datetime.fromtimestamp(latest_mtime).strftime("%Y-%m-%d %H:%M") if latest_mtime > 0 else None
    }


def format_size(size_bytes: int) -> str:
    """Format bytes as human-readable size."""
    if size_bytes < 1024:
        return f"{size_bytes}B"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.1f}KB"
    else:
        return f"{size_bytes / (1024 * 1024):.1f}MB"


def build_llms_txt_entries() -> list:
    """Build llms.txt documentation entries from config."""
    config = load_yaml(LLMS_SITES_CONFIG)
    sites = config.get("sites", [])

    entries = []
    for site in sites:
        name = site.get("name", "")
        if not name:
            continue

        path = DOCS_DIR / "llms-txt" / name
        stats = get_dir_stats(path)

        entry = {
            "name": name,
            "description": site.get("description", ""),
            "url": site.get("base_url", ""),
            "path": f"docs/llms-txt/{name}/",
            "status": "fetched" if stats["exists"] and stats["file_count"] > 0 else "pending",
        }

        if stats["exists"] and stats["file_count"] > 0:
            entry["file_count"] = stats["file_count"]
            entry["size"] = format_size(stats["size_bytes"])
            if stats["last_modified"]:
                entry["last_updated"] = stats["last_modified"]

        entries.append(entry)

    return entries


def build_github_entries() -> list:
    """Build GitHub repository entries from config."""
    config = load_yaml(REPO_CONFIG)
    repos = config.get("repositories", [])

    entries = []
    for repo in repos:
        name = repo.get("name", "")
        if not name:
            continue

        target_folder = repo.get("target_folder", f"docs/github-scraped/{name.lower()}")
        path = REPO_ROOT / target_folder
        stats = get_dir_stats(path)

        # Extract repo owner/name from URL
        repo_url = repo.get("repo_url", "")
        repo_name = ""
        if "github.com" in repo_url:
            parts = repo_url.replace(".git", "").split("github.com/")
            if len(parts) > 1:
                repo_name = parts[1]

        entry = {
            "name": name.lower().replace(" ", "-"),
            "description": repo.get("description", ""),
            "repo": repo_name,
            "branch": repo.get("branch", "main"),
            "source_folder": repo.get("source_folder", "docs"),
            "path": target_folder + "/",
            "status": "fetched" if stats["exists"] and stats["file_count"] > 0 else "pending",
        }

        if stats["exists"] and stats["file_count"] > 0:
            entry["file_count"] = stats["file_count"]
            entry["size"] = format_size(stats["size_bytes"])
            if stats["last_modified"]:
                entry["last_updated"] = stats["last_modified"]

        entries.append(entry)

    return entries


def build_web_scraped_entries() -> list:
    """Build web-scraped documentation entries by scanning directory."""
    web_scraped_dir = DOCS_DIR / "web-scraped"

    # Known web scrapers and their metadata
    known_scrapers = {
        "claude-code-sdk": {
            "description": "Anthropic Claude Code SDK documentation",
            "url": "https://docs.anthropic.com/en/docs/claude-code/",
            "script": "scripts/claude-code-sdk-docs.py"
        },
        "readmes": {
            "description": "Individual README files from various projects",
            "script": "scripts/pull-readmes.py"
        }
    }

    entries = []

    if not web_scraped_dir.exists():
        return entries

    for subdir in sorted(web_scraped_dir.iterdir()):
        if not subdir.is_dir():
            continue

        name = subdir.name
        stats = get_dir_stats(subdir)

        metadata = known_scrapers.get(name, {})

        entry = {
            "name": name,
            "description": metadata.get("description", f"{name} documentation"),
            "path": f"docs/web-scraped/{name}/",
            "status": "fetched" if stats["exists"] and stats["file_count"] > 0 else "pending",
        }

        if metadata.get("url"):
            entry["url"] = metadata["url"]
        if metadata.get("script"):
            entry["script"] = metadata["script"]

        if stats["exists"] and stats["file_count"] > 0:
            entry["file_count"] = stats["file_count"]
            entry["size"] = format_size(stats["size_bytes"])
            if stats["last_modified"]:
                entry["last_updated"] = stats["last_modified"]

        entries.append(entry)

    return entries


def generate_index() -> dict:
    """Generate the complete index structure."""
    llms_txt = build_llms_txt_entries()
    github = build_github_entries()
    web_scraped = build_web_scraped_entries()

    # Count fetched entries
    llms_txt_fetched = sum(1 for e in llms_txt if e.get("status") == "fetched")
    github_fetched = sum(1 for e in github if e.get("status") == "fetched")
    web_scraped_fetched = sum(1 for e in web_scraped if e.get("status") == "fetched")

    index = {
        "metadata": {
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "total_sources": len(llms_txt) + len(github) + len(web_scraped),
            "total_fetched": llms_txt_fetched + github_fetched + web_scraped_fetched,
            "llms_txt_count": len(llms_txt),
            "llms_txt_fetched": llms_txt_fetched,
            "github_count": len(github),
            "github_fetched": github_fetched,
            "web_scraped_count": len(web_scraped),
            "web_scraped_fetched": web_scraped_fetched,
        },
        "llms_txt": llms_txt,
        "github": github,
        "web_scraped": web_scraped,
    }

    return index


def write_index(index: dict):
    """Write index to YAML file with proper formatting."""
    header = """# Documentation Index
# Auto-generated by scripts/update-index.py
# Do not edit manually - changes will be overwritten
#
# Status values:
#   - fetched: Documentation successfully downloaded
#   - pending: Configuration exists but not yet fetched

"""

    # Custom YAML dumper for cleaner output
    class CleanDumper(yaml.SafeDumper):
        pass

    def str_representer(dumper, data):
        if '\n' in data:
            return dumper.represent_scalar('tag:yaml.org,2002:str', data, style='|')
        return dumper.represent_scalar('tag:yaml.org,2002:str', data)

    CleanDumper.add_representer(str, str_representer)

    yaml_content = yaml.dump(
        index,
        Dumper=CleanDumper,
        default_flow_style=False,
        allow_unicode=True,
        sort_keys=False,
        width=120
    )

    with open(INDEX_FILE, 'w') as f:
        f.write(header)
        f.write(yaml_content)

    print(f"✅ Updated {INDEX_FILE}")


def main():
    print("📋 Updating documentation index...")
    print(f"   Reading from: {LLMS_SITES_CONFIG}")
    print(f"   Reading from: {REPO_CONFIG}")
    print(f"   Scanning: {DOCS_DIR}")
    print()

    index = generate_index()

    # Print summary
    meta = index["metadata"]
    print(f"📊 Index Summary:")
    print(f"   llms.txt sites: {meta['llms_txt_fetched']}/{meta['llms_txt_count']} fetched")
    print(f"   GitHub repos:   {meta['github_fetched']}/{meta['github_count']} fetched")
    print(f"   Web scraped:    {meta['web_scraped_fetched']}/{meta['web_scraped_count']} fetched")
    print(f"   Total:          {meta['total_fetched']}/{meta['total_sources']} fetched")
    print()

    write_index(index)


if __name__ == "__main__":
    main()
