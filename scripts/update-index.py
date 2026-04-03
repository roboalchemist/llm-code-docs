#!/usr/bin/env python3
"""
update-index.py - Generate index.yaml from the library-centric docs/ structure.

Each library lives at docs/{library}/ and may contain:
  - _meta.yaml          metadata (name, description, primary_source, sources, quality_score)
  - llms/               docs fetched via llms.txt protocol
  - github/             docs scraped from GitHub
  - web/                docs scraped from the web

The script scans docs/*/, skipping:
  - META_EXAMPLES (reserved for schema examples)
  - Any entry whose name starts with _ or .
  - Non-directories
"""

import os
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml


DOCS_DIR = Path(__file__).parent.parent / "docs"
OUTPUT_FILE = Path(__file__).parent.parent / "index.yaml"

# Source subdirectory names inside each library dir
SOURCE_SUBDIRS = ("llms", "github", "web")

# Top-level docs/ dirs to skip (case-sensitive)
SKIP_NAMES = {"META_EXAMPLES", "META_SCHEMA.md"}


def format_size(size_bytes: int) -> str:
    """Format bytes into a human-readable string (e.g. '1.3MB', '512.0KB')."""
    if size_bytes >= 1024 * 1024:
        return f"{size_bytes / (1024 * 1024):.1f}MB"
    elif size_bytes >= 1024:
        return f"{size_bytes / 1024:.1f}KB"
    return f"{size_bytes}B"


def count_files_and_size(directory: Path) -> tuple[int, int]:
    """Recursively count files and total bytes under directory."""
    file_count = 0
    total_bytes = 0
    try:
        for item in directory.rglob("*"):
            if item.is_file() and item.name != "_meta.yaml":
                file_count += 1
                try:
                    total_bytes += item.stat().st_size
                except OSError:
                    pass
    except OSError:
        pass
    return file_count, total_bytes


def read_meta(library_dir: Path) -> dict:
    """Read _meta.yaml if present; return empty dict otherwise."""
    meta_path = library_dir / "_meta.yaml"
    if meta_path.exists():
        try:
            with open(meta_path, "r", encoding="utf-8") as f:
                return yaml.safe_load(f) or {}
        except Exception as e:
            print(f"  Warning: could not read {meta_path}: {e}", file=sys.stderr)
    return {}


def build_library_entry(library_dir: Path) -> dict:
    """Build an index.yaml entry for a single library directory."""
    lib_name = library_dir.name
    meta = read_meta(library_dir)

    # Metadata from _meta.yaml (with fallbacks)
    name = meta.get("name", lib_name)
    description = meta.get("description", f"{lib_name} documentation")
    if isinstance(description, str):
        description = description.strip()
    primary_source = meta.get("primary_source", None)

    # Sources list: prefer _meta.yaml, otherwise empty
    sources_meta = meta.get("sources", [])
    sources = []
    for s in sources_meta:
        source_entry = {"type": s.get("type", "")}
        if s.get("url"):
            source_entry["url"] = s["url"]
        if s.get("last_fetched"):
            source_entry["last_fetched"] = s["last_fetched"]
        sources.append(source_entry)

    # Count files and sizes across source subdirs
    total_files = 0
    total_bytes = 0
    present_subdirs = []

    for subdir_name in SOURCE_SUBDIRS:
        subdir = library_dir / subdir_name
        if subdir.is_dir():
            present_subdirs.append(subdir_name)
            fc, fb = count_files_and_size(subdir)
            total_files += fc
            total_bytes += fb

    # If no source subdirs exist, count the library dir itself
    # (handles both old-style flat dirs and new-style structured dirs)
    if not present_subdirs:
        total_files, total_bytes = count_files_and_size(library_dir)

    # Determine status
    status = "fetched" if total_files > 0 else "pending"

    # Last updated: now (or from most recent meta source)
    last_updated = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M")
    for s in sources_meta:
        lf = s.get("last_fetched")
        if lf:
            # Use the most recent fetch time as last_updated
            try:
                dt_str = str(lf).replace("Z", "+00:00")
                dt = datetime.fromisoformat(dt_str)
                last_updated = dt.strftime("%Y-%m-%d %H:%M")
            except Exception:
                pass
            break

    entry = {
        "name": name,
        "description": description,
        "path": f"docs/{lib_name}/",
        "status": status,
        "file_count": total_files,
        "size": format_size(total_bytes),
        "last_updated": last_updated,
    }

    if primary_source:
        entry["primary_source"] = primary_source
    if sources:
        entry["sources"] = sources

    return entry


def scan_library_dirs(docs_dir: Path) -> list[Path]:
    """Return sorted list of library dirs under docs_dir, skipping reserved names."""
    dirs = []
    try:
        for item in sorted(docs_dir.iterdir()):
            if not item.is_dir():
                continue
            name = item.name
            # Skip META_EXAMPLES and other reserved names
            if name in SKIP_NAMES:
                continue
            # Skip anything starting with _ or .
            if name.startswith("_") or name.startswith("."):
                continue
            dirs.append(item)
    except OSError as e:
        print(f"Error reading docs dir: {e}", file=sys.stderr)
        sys.exit(1)
    return dirs


def generate_index(docs_dir: Path) -> dict:
    """Scan docs_dir and build the full index structure."""
    library_dirs = scan_library_dirs(docs_dir)
    print(f"Found {len(library_dirs)} library directories", file=sys.stderr)

    libraries = []
    total_files = 0
    total_bytes_all = 0

    for lib_dir in library_dirs:
        entry = build_library_entry(lib_dir)
        libraries.append(entry)
        total_files += entry["file_count"]
        # Parse size back to bytes for total (approximate)
        print(f"  {entry['name']}: {entry['file_count']} files, {entry['size']}", file=sys.stderr)

    now_str = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M")

    index = {
        "metadata": {
            "last_updated": now_str,
            "total_libraries": len(libraries),
            "total_files": total_files,
            "schema_version": "2",
        },
        "libraries": libraries,
    }

    return index


def main():
    if not DOCS_DIR.is_dir():
        print(f"Error: docs directory not found: {DOCS_DIR}", file=sys.stderr)
        sys.exit(1)

    print(f"Scanning {DOCS_DIR} ...", file=sys.stderr)
    index = generate_index(DOCS_DIR)

    # Write output
    header = (
        "# Documentation Index\n"
        "# Auto-generated by scripts/update-index.py\n"
        "# Do not edit manually - changes will be overwritten\n"
        "#\n"
        "# Schema version: 2 (library-centric)\n"
        "# One entry per library in docs/{library}/\n"
        "#\n"
        "# Status values:\n"
        "#   - fetched: Documentation successfully downloaded\n"
        "#   - pending: Library registered but not yet fetched\n"
        "\n"
    )

    yaml_str = yaml.dump(
        index,
        default_flow_style=False,
        allow_unicode=True,
        sort_keys=False,
        width=120,
    )

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(header)
        f.write(yaml_str)

    print(f"\nWrote {len(index['libraries'])} library entries to {OUTPUT_FILE}", file=sys.stderr)


if __name__ == "__main__":
    main()
