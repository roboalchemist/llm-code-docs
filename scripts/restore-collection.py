#!/usr/bin/env python3
"""
restore-collection.py - Restore collection directories from git history into library-centric format.

Collections like docs-rs/, javadoc/, rubydoc/ contain multiple sub-libraries bundled under
a single source-type directory. This script splits them into individual library directories.

Usage:
  python3 scripts/restore-collection.py --commit 94ab792 --collection docs-rs --source-type web
  python3 scripts/restore-collection.py --commit 94ab792 --collection docs-rs --source-type web --dry-run
"""

import argparse
import os
import subprocess
import sys
from pathlib import Path

# URL templates per collection type
URL_TEMPLATES = {
    "docs-rs": "https://docs.rs/{name}/",
    "javadoc": "",
    "rubydoc": "https://rubydoc.info/gems/{name}/",
    "readthedocs": "https://{name}.readthedocs.io/",
    "pkg-go-dev": "https://pkg.go.dev/{name}/",
    "go-native": "https://pkg.go.dev/{name}/",
    "hexdocs": "https://hexdocs.pm/{name}/",
    "github-repos": "",
    "specifications": "",
}


def find_repo_root() -> Path:
    result = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        return Path(__file__).parent.parent
    return Path(result.stdout.strip())


def list_subdirs_at_commit(commit: str, collection_path: str) -> list[str]:
    """List subdirectory names under a collection at a given commit."""
    result = subprocess.run(
        ["git", "ls-tree", "-d", "--name-only", f"{commit}:{collection_path}"],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        return []
    return [line.strip() for line in result.stdout.strip().split("\n") if line.strip()]


def list_files_at_commit(commit: str, path: str) -> list[str]:
    """List all files (not dirs) directly under a path at a given commit."""
    result = subprocess.run(
        ["git", "ls-tree", "--name-only", f"{commit}:{path}"],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        return []
    return [line.strip() for line in result.stdout.strip().split("\n") if line.strip()]


def generate_meta_yaml(name: str, source_type: str, url: str) -> str:
    """Generate _meta.yaml content for a restored library."""
    lines = [
        f"name: {name}",
        f"primary_source: {source_type}",
        "sources:",
        f"  - type: {source_type}",
    ]
    if url:
        lines.append(f"    url: {url}")
    lines.append('    last_fetched: "2026-04-08T00:00:00Z"')
    lines.append("description: >")
    lines.append(f"  {name} documentation")
    lines.append("quality_score: 0")
    lines.append("")
    return "\n".join(lines)


def restore_collection(
    commit: str,
    collection: str,
    source_type: str,
    dry_run: bool,
    repo_root: Path,
) -> int:
    docs_dir = repo_root / "docs"
    collection_path = f"docs/{collection}"

    # Get list of sub-libraries in the collection at the source commit
    subdirs = list_subdirs_at_commit(commit, collection_path)

    if not subdirs:
        # Maybe it's a flat collection (files, not subdirs)
        files = list_files_at_commit(commit, collection_path)
        if files:
            print(f"Collection {collection} has {len(files)} files at root (not sub-libraries)")
            print("Use manual restoration for flat collections.")
            return 1
        print(f"No sub-libraries found in {collection_path} at {commit}", file=sys.stderr)
        return 1

    print(f"{'DRY RUN: ' if dry_run else ''}Restoring {len(subdirs)} libraries from {collection}\n")

    url_template = URL_TEMPLATES.get(collection, "")
    restored = 0
    skipped = 0

    for lib_name in sorted(subdirs):
        target_dir = docs_dir / lib_name / source_type
        meta_path = docs_dir / lib_name / "_meta.yaml"

        # Check if target source subdir already exists
        if target_dir.exists():
            print(f"  SKIP {lib_name}/{source_type}/ (already exists)")
            skipped += 1
            continue

        url = url_template.format(name=lib_name) if url_template else ""

        if dry_run:
            print(f"  RESTORE {collection}/{lib_name}/ -> {lib_name}/{source_type}/")
            if not meta_path.exists():
                print(f"  CREATE {lib_name}/_meta.yaml")
            restored += 1
            continue

        # Step 1: Checkout from history into old-structure location
        old_path = docs_dir / collection / lib_name
        result = subprocess.run(
            ["git", "checkout", commit, "--", str(old_path)],
            capture_output=True, text=True,
        )
        if result.returncode != 0:
            print(f"  ERROR: git checkout failed for {lib_name}: {result.stderr.strip()}", file=sys.stderr)
            continue

        # Step 2: Move to library-centric location
        target_dir.parent.mkdir(parents=True, exist_ok=True)
        os.rename(str(old_path), str(target_dir))

        # Step 3: Generate _meta.yaml if not exists
        if not meta_path.exists():
            meta_content = generate_meta_yaml(lib_name, source_type, url)
            meta_path.write_text(meta_content)
            print(f"  RESTORED {lib_name}/{source_type}/ + _meta.yaml")
        else:
            print(f"  RESTORED {lib_name}/{source_type}/ (meta already exists)")

        restored += 1

    # Clean up the old collection directory if it's now empty
    old_collection_dir = docs_dir / collection
    if old_collection_dir.exists() and not dry_run:
        try:
            # Remove any empty directories recursively
            for dirpath, dirnames, filenames in os.walk(str(old_collection_dir), topdown=False):
                if not filenames and not dirnames:
                    os.rmdir(dirpath)
            if old_collection_dir.exists() and not any(old_collection_dir.iterdir()):
                old_collection_dir.rmdir()
                print(f"\n  Cleaned up empty {collection}/ directory")
        except OSError:
            pass

    print(f"\n{'DRY RUN: ' if dry_run else ''}Restored {restored}, skipped {skipped}")
    return 0


def main():
    parser = argparse.ArgumentParser(
        description="Restore collection directories from git history into library-centric format."
    )
    parser.add_argument("--commit", required=True, help="Source commit hash (e.g., 94ab792)")
    parser.add_argument("--collection", required=True, help="Collection directory name (e.g., docs-rs)")
    parser.add_argument("--source-type", required=True, help="Target source type (e.g., web, github)")
    parser.add_argument("--dry-run", action="store_true", help="Preview without making changes")
    parser.add_argument("--repo-root", type=Path, default=None, help="Repository root (default: auto-detect)")
    args = parser.parse_args()

    repo_root = args.repo_root or find_repo_root()
    sys.exit(restore_collection(
        commit=args.commit,
        collection=args.collection,
        source_type=args.source_type,
        dry_run=args.dry_run,
        repo_root=repo_root,
    ))


if __name__ == "__main__":
    main()
