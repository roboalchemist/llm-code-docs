#!/usr/bin/env python3
"""
Migrate docs/ from source-centric layout to library-centric layout.

Before:
  docs/llms-txt/X/*
  docs/github-scraped/X/*
  docs/web-scraped/X/*

After:
  docs/X/llms/*
  docs/X/github/*
  docs/X/web/*
  docs/X/_meta.yaml  (generated from index.yaml data)

Usage:
  python3 scripts/migrate-to-library-centric.py --dry-run
  python3 scripts/migrate-to-library-centric.py
"""

import argparse
import os
import subprocess
import sys
import yaml
from datetime import datetime, timezone
from pathlib import Path

# Map source directory names to their short aliases used in the new layout
SOURCE_MAP = {
    "llms-txt": "llms",
    "github-scraped": "github",
    "web-scraped": "web",
}

# Source-type enum values for _meta.yaml
SOURCE_TYPE_MAP = {
    "llms-txt": "llms",
    "github-scraped": "github",
    "web-scraped": "web",
}


def find_repo_root() -> Path:
    """Find the git repository root from the current working directory."""
    result = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        # Fall back to the parent of the scripts/ directory
        return Path(__file__).parent.parent
    return Path(result.stdout.strip())


def load_index_data(repo_root: Path) -> dict:
    """
    Load index.yaml and build a lookup dict:
      lib_name -> {source_type: entry_dict}
    """
    index_path = repo_root / "index.yaml"
    if not index_path.exists():
        print(f"WARNING: index.yaml not found at {index_path}", file=sys.stderr)
        return {}

    with open(index_path) as f:
        data = yaml.safe_load(f)

    lookup: dict[str, dict] = {}
    section_to_type = {
        "llms_txt": "llms-txt",
        "github_scraped": "github-scraped",
        "web_scraped": "web-scraped",
    }
    for section, source_type in section_to_type.items():
        for entry in data.get(section, []):
            name = entry.get("name", "")
            if name not in lookup:
                lookup[name] = {}
            lookup[name][source_type] = entry

    return lookup


def load_llms_sites_urls(repo_root: Path) -> dict[str, str]:
    """Return a map of lib_name -> base_url from scripts/llms-sites.yaml."""
    sites_path = repo_root / "scripts" / "llms-sites.yaml"
    if not sites_path.exists():
        return {}
    with open(sites_path) as f:
        data = yaml.safe_load(f)
    result = {}
    for site in data.get("sites", []):
        name = site.get("name", "")
        url = site.get("base_url") or site.get("url", "")
        if name and url:
            result[name] = url
    return result


def load_repo_config_data(repo_root: Path) -> dict[str, dict]:
    """Return a map of lib_name -> {url, description} from scripts/repo_config.yaml."""
    cfg_path = repo_root / "scripts" / "repo_config.yaml"
    if not cfg_path.exists():
        return {}
    with open(cfg_path) as f:
        data = yaml.safe_load(f)
    result = {}
    for repo in data.get("repositories", []):
        target = repo.get("target_folder", "").rstrip("/")
        lib = os.path.basename(target)
        url = repo.get("repo_url", "")
        desc = repo.get("description", "")
        if lib:
            result[lib] = {"url": url, "description": desc}
    return result


def collect_all_libraries(docs_dir: Path) -> dict[str, list[str]]:
    """
    Returns a dict: lib_name -> [list of source_dirs that contain it]
    e.g. {'tornado': ['github-scraped'], 'apple-developer-docs': ['web-scraped']}
    """
    libs: dict[str, list[str]] = {}
    for source_dir in SOURCE_MAP:
        source_path = docs_dir / source_dir
        if not source_path.is_dir():
            continue
        for entry in sorted(source_path.iterdir()):
            if entry.is_dir():
                libs.setdefault(entry.name, []).append(source_dir)
    return libs


def determine_primary_source(source_dirs: list[str]) -> str:
    """
    Choose the primary source type given a list of source_dirs for one library.
    Priority: llms-txt > github-scraped > web-scraped
    """
    priority = ["llms-txt", "github-scraped", "web-scraped"]
    for p in priority:
        if p in source_dirs:
            return SOURCE_TYPE_MAP[p]
    return SOURCE_TYPE_MAP[source_dirs[0]]


def build_meta_yaml(
    lib_name: str,
    source_dirs: list[str],
    index_lookup: dict,
    llms_urls: dict[str, str],
    repo_config_data: dict[str, dict],
) -> str:
    """
    Build the content for docs/X/_meta.yaml.
    Pulls description and URL from index.yaml / llms-sites.yaml / repo_config.yaml.
    """
    primary_source = determine_primary_source(source_dirs)

    sources = []
    description = f"{lib_name} documentation"
    fallback_ts = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    # Check repo_config for a richer description
    rc_entry = repo_config_data.get(lib_name, {})
    if rc_entry.get("description"):
        description = rc_entry["description"]

    for src_dir in sorted(source_dirs, key=lambda x: ["llms-txt", "github-scraped", "web-scraped"].index(x)):
        src_type = SOURCE_TYPE_MAP[src_dir]
        entry = index_lookup.get(lib_name, {}).get(src_dir, {})

        # Determine URL
        url = ""
        if src_dir == "llms-txt":
            # Try llms-sites.yaml first, then index.yaml url field
            url = llms_urls.get(lib_name, entry.get("url", ""))
        elif src_dir == "github-scraped":
            # Try repo_config.yaml first, then index.yaml url field
            raw_url = rc_entry.get("url", entry.get("url", ""))
            # Strip .git suffix for cleaner display
            if raw_url.endswith(".git"):
                url = raw_url[:-4]
            else:
                url = raw_url
        elif src_dir == "web-scraped":
            url = entry.get("url", "")

        # Determine last_fetched
        last_updated = entry.get("last_updated", "")
        if last_updated:
            # index.yaml uses "YYYY-MM-DD HH:MM" format; convert to ISO 8601
            try:
                dt = datetime.strptime(str(last_updated), "%Y-%m-%d %H:%M")
                last_fetched = dt.strftime("%Y-%m-%dT%H:%M:%SZ")
            except ValueError:
                last_fetched = fallback_ts
        else:
            last_fetched = fallback_ts

        # Pull description from index entry if it's more meaningful than a bare placeholder.
        # Placeholder patterns: "{lib} from GitHub" and "{lib} documentation"
        idx_desc = entry.get("description", "")
        if idx_desc:
            is_github_placeholder = idx_desc == f"{lib_name} from GitHub"
            is_doc_placeholder = idx_desc == f"{lib_name} documentation"
            if not is_github_placeholder and not is_doc_placeholder:
                description = idx_desc

        src_entry: dict = {"type": src_type}
        if url:
            src_entry["url"] = url
        src_entry["last_fetched"] = last_fetched
        sources.append(src_entry)

    # Build the YAML content manually for clean formatting
    lines = [
        f"name: {lib_name}",
        f"primary_source: {primary_source}",
        "sources:",
    ]
    for src in sources:
        lines.append(f"  - type: {src['type']}")
        if "url" in src:
            lines.append(f"    url: {src['url']}")
        lines.append(f"    last_fetched: \"{src['last_fetched']}\"")

    # Wrap description at ~80 chars using YAML block scalar
    lines.append("description: >")
    words = description.split()
    line_buf = []
    char_count = 0
    for word in words:
        if char_count + len(word) + 1 > 75 and line_buf:
            lines.append("  " + " ".join(line_buf))
            line_buf = [word]
            char_count = len(word)
        else:
            line_buf.append(word)
            char_count += len(word) + 1
    if line_buf:
        lines.append("  " + " ".join(line_buf))

    lines.append("quality_score: 0")
    lines.append("")  # trailing newline

    return "\n".join(lines)


def git_mv(src: Path, dst: Path, dry_run: bool) -> bool:
    """
    Run git mv src dst. In dry-run mode, just print what would happen.
    Returns True on success (or dry_run).
    """
    src_rel = str(src)
    dst_rel = str(dst)
    if dry_run:
        print(f"  git mv {src_rel}  ->  {dst_rel}")
        return True

    result = subprocess.run(
        ["git", "mv", src_rel, dst_rel],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(f"ERROR: git mv failed: {result.stderr.strip()}", file=sys.stderr)
        return False
    return True


def migrate(dry_run: bool, repo_root: Path) -> int:
    """
    Perform (or preview) the migration.
    Returns 0 on success, 1 on error.
    """
    docs_dir = repo_root / "docs"

    # Load all data sources
    index_lookup = load_index_data(repo_root)
    llms_urls = load_llms_sites_urls(repo_root)
    repo_config_data = load_repo_config_data(repo_root)

    # Discover all libraries and which source dirs they live in
    libs = collect_all_libraries(docs_dir)

    if not libs:
        print("No libraries found in docs/ source directories.", file=sys.stderr)
        return 1

    print(f"{'DRY RUN: ' if dry_run else ''}Migrating {len(libs)} libraries to library-centric layout\n")

    errors = []

    for lib_name in sorted(libs.keys()):
        source_dirs = libs[lib_name]
        print(f"[{lib_name}]  sources: {', '.join(source_dirs)}")

        for src_dir in source_dirs:
            src_alias = SOURCE_MAP[src_dir]
            src_path = docs_dir / src_dir / lib_name   # e.g. docs/llms-txt/notion
            dst_dir = docs_dir / lib_name / src_alias  # e.g. docs/notion/llms
            dst_parent = docs_dir / lib_name           # e.g. docs/notion

            # Idempotency check: if dst_dir already exists, skip this move
            if dst_dir.exists() and not dry_run:
                print(f"  SKIP (already migrated): {dst_dir}")
                continue
            if dst_dir.exists() and dry_run:
                print(f"  SKIP (already exists): docs/{lib_name}/{src_alias}/")
                continue

            # In non-dry-run, create parent directory if needed
            if not dry_run:
                dst_parent.mkdir(parents=True, exist_ok=True)

            # Move the source directory into the new location
            ok = git_mv(src_path, dst_dir, dry_run)
            if not ok:
                errors.append(f"{lib_name}: git mv {src_path} -> {dst_dir} failed")

        # Generate _meta.yaml for this library
        meta_path = docs_dir / lib_name / "_meta.yaml"
        meta_content = build_meta_yaml(lib_name, source_dirs, index_lookup, llms_urls, repo_config_data)

        if dry_run:
            print(f"  CREATE docs/{lib_name}/_meta.yaml")
        elif meta_path.exists():
            print(f"  SKIP _meta.yaml (already exists)")
        else:
            meta_path.parent.mkdir(parents=True, exist_ok=True)
            meta_path.write_text(meta_content)
            print(f"  WROTE docs/{lib_name}/_meta.yaml")

        print()

    if errors:
        print("\nErrors encountered:")
        for e in errors:
            print(f"  {e}")
        return 1

    print("Migration complete." if not dry_run else "Dry run complete (no changes made).")
    return 0


def main():
    parser = argparse.ArgumentParser(
        description="Migrate docs/ from source-centric to library-centric layout."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print planned moves without executing them.",
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=None,
        help="Path to the repository root (default: auto-detect via git).",
    )
    args = parser.parse_args()

    repo_root = args.repo_root or find_repo_root()
    sys.exit(migrate(dry_run=args.dry_run, repo_root=repo_root))


if __name__ == "__main__":
    main()
