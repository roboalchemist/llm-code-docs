#!/usr/bin/env python3
"""
check-compliance.py - Verify all library directories follow the library-centric structure.

Every library at docs/{name}/ must have:
  1. A _meta.yaml file with valid fields (name, primary_source, sources, description)
  2. At least one source subdirectory: llms/, github/, or web/
  3. No legacy subdirectory names (web-scraped/, github-scraped/, llms-txt/)
  4. No loose .md files at root level (all docs belong in source subdirs)
  5. At least one non-meta content file somewhere

Usage:
  python3 scripts/check-compliance.py          # Report all issues
  python3 scripts/check-compliance.py --fix    # Auto-fix what's possible (rename legacy subdirs)
  python3 scripts/check-compliance.py --json   # JSON output for CI
"""

import argparse
import json
import os
import sys
from pathlib import Path

import yaml

DOCS_DIR = Path(__file__).parent.parent / "docs"
VALID_SOURCE_SUBDIRS = {"llms", "github", "web"}
LEGACY_SUBDIR_MAP = {
    "llms-txt": "llms",
    "github-scraped": "github",
    "web-scraped": "web",
}
SKIP_NAMES = {"META_EXAMPLES", "META_SCHEMA.md"}
REQUIRED_META_FIELDS = {"name", "primary_source", "sources", "description"}


def check_library(lib_dir: Path) -> list[dict]:
    """Check a single library directory for compliance. Returns list of issues."""
    lib_name = lib_dir.name
    issues = []

    # Check 1: _meta.yaml exists and is valid
    meta_path = lib_dir / "_meta.yaml"
    if not meta_path.exists():
        issues.append({"type": "no_meta", "message": "Missing _meta.yaml"})
    else:
        try:
            with open(meta_path) as f:
                meta = yaml.safe_load(f)
            if not isinstance(meta, dict):
                issues.append({"type": "invalid_meta", "message": "_meta.yaml is not a valid YAML mapping"})
            else:
                missing = REQUIRED_META_FIELDS - set(meta.keys())
                if missing:
                    issues.append({
                        "type": "incomplete_meta",
                        "message": f"_meta.yaml missing fields: {', '.join(sorted(missing))}",
                    })
                # Check name field type (the "0" bug)
                if "name" in meta and not isinstance(meta["name"], str):
                    issues.append({
                        "type": "meta_type_error",
                        "message": f"name field is {type(meta['name']).__name__}, should be quoted string",
                    })
        except Exception as e:
            issues.append({"type": "meta_parse_error", "message": f"Failed to parse _meta.yaml: {e}"})

    # Check 2: Has at least one valid source subdirectory
    has_source = any((lib_dir / sub).is_dir() for sub in VALID_SOURCE_SUBDIRS)
    if not has_source:
        issues.append({"type": "no_source_subdir", "message": "No llms/, github/, or web/ subdirectory"})

    # Check 3: No legacy subdirectory names
    for legacy, canonical in LEGACY_SUBDIR_MAP.items():
        if (lib_dir / legacy).is_dir():
            issues.append({
                "type": "legacy_subdir",
                "message": f"Legacy subdirectory '{legacy}/' should be renamed to '{canonical}/'",
                "fixable": True,
                "fix_from": legacy,
                "fix_to": canonical,
            })

    # Check 4: No loose .md files at root level
    root_mds = [f.name for f in lib_dir.iterdir() if f.is_file() and f.suffix == ".md"]
    if root_mds:
        issues.append({
            "type": "root_md_files",
            "message": f"{len(root_mds)} .md file(s) at root level (should be in source subdir)",
            "files": root_mds[:5],
        })

    # Check 5: Has at least one content file
    content_files = 0
    for item in lib_dir.rglob("*"):
        if item.is_file() and item.name != "_meta.yaml":
            content_files += 1
            if content_files > 0:
                break
    if content_files == 0:
        issues.append({"type": "empty", "message": "No content files (only _meta.yaml)"})

    return issues


def fix_issue(lib_dir: Path, issue: dict) -> bool:
    """Attempt to auto-fix a single issue. Returns True if fixed."""
    if issue["type"] == "legacy_subdir":
        src = lib_dir / issue["fix_from"]
        dst = lib_dir / issue["fix_to"]
        if dst.exists():
            print(f"  SKIP: {dst} already exists, cannot rename", file=sys.stderr)
            return False
        os.rename(str(src), str(dst))
        return True
    return False


def main():
    parser = argparse.ArgumentParser(description="Check library-centric structure compliance.")
    parser.add_argument("--fix", action="store_true", help="Auto-fix fixable issues")
    parser.add_argument("--json", action="store_true", help="JSON output")
    args = parser.parse_args()

    if not DOCS_DIR.is_dir():
        print(f"Error: docs directory not found: {DOCS_DIR}", file=sys.stderr)
        sys.exit(1)

    results = {}
    total_libs = 0
    total_issues = 0
    total_fixed = 0

    for item in sorted(DOCS_DIR.iterdir()):
        if not item.is_dir():
            continue
        name = item.name
        if name in SKIP_NAMES or name.startswith("_") or name.startswith("."):
            continue

        total_libs += 1
        issues = check_library(item)

        if issues:
            results[name] = issues
            total_issues += len(issues)

            if args.fix:
                for issue in issues:
                    if issue.get("fixable"):
                        if fix_issue(item, issue):
                            total_fixed += 1
                            issue["fixed"] = True

    if args.json:
        output = {
            "total_libraries": total_libs,
            "compliant": total_libs - len(results),
            "non_compliant": len(results),
            "total_issues": total_issues,
            "issues": results,
        }
        if args.fix:
            output["fixed"] = total_fixed
        print(json.dumps(output, indent=2))
    else:
        if not results:
            print(f"All {total_libs} libraries are compliant.")
        else:
            for lib_name, issues in results.items():
                print(f"\n{lib_name}:")
                for issue in issues:
                    fixed = " [FIXED]" if issue.get("fixed") else ""
                    print(f"  - [{issue['type']}] {issue['message']}{fixed}")
                    if "files" in issue:
                        for f in issue["files"]:
                            print(f"      {f}")

            print(f"\n--- Summary ---")
            print(f"Total libraries: {total_libs}")
            print(f"Compliant: {total_libs - len(results)}")
            print(f"Non-compliant: {len(results)} ({total_issues} issues)")
            if args.fix:
                print(f"Auto-fixed: {total_fixed}")

    sys.exit(1 if results and not args.fix else 0)


if __name__ == "__main__":
    main()
