#!/usr/bin/env python3
"""
Quality scanner for llm-code-docs libraries.

Scans all library directories in parallel and detects genuinely bad docs:
- 404 / page not found errors
- Bot protection / JS injection
- Empty or near-empty stubs (< 500 bytes)
- README-only fetches with no real content

Usage:
    python3 scripts/quality-check.py                  # scan all sources
    python3 scripts/quality-check.py --source llms-txt
    python3 scripts/quality-check.py --json           # JSON output
    python3 scripts/quality-check.py --fix            # delete confirmed dead entries
    python3 scripts/quality-check.py --workers 20     # parallelism (default: 16)
"""

import argparse
import json
import re
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path


DOCS_ROOT = Path(__file__).parent.parent / "docs"
SOURCES = ["llms-txt", "github-scraped", "web-scraped"]

# Signals that a file is a dead/bad fetch
# Signals checked against raw text (not inside code blocks)
PROSE_ERROR_SIGNALS = [
    r"(?i)^#{1,3}\s*(error\s*404|page not found|404 not found|403 forbidden)",
    r"(?i)^##\s*error\s*\d{3}",
    r"(?i)we couldn.t find the page",
    r"(?i)the page you.re looking for",
    r"(?i)this page does not exist",
    r"(?i)cloudflare.*ray id",
    r"(?i)just a moment\.?\s*$",     # Cloudflare challenge
    r"(?i)^#+\s*(access denied|403 forbidden|unauthorized)",
]

# Signals checked against full raw text (including code blocks)
RAW_ERROR_SIGNALS = [
    r"_0x[0-9a-f]{4}[^`\n]{20,}",  # obfuscated JS (long sequences, not in one-liners)
    r"document\[_0x",               # obfuscated JS
    r"(?i)EO_Bot_Ssid",             # bot detection cookie
    r"(?i)setTimeout\(_0x",         # obfuscated timer
]

PROSE_PATTERNS = [re.compile(p, re.MULTILINE) for p in PROSE_ERROR_SIGNALS]
RAW_PATTERNS = [re.compile(p) for p in RAW_ERROR_SIGNALS]

# Generic file names that don't count as real content
GENERIC_NAMES = {
    "readme", "contributing", "license", "changelog", "index",
    "llms-full", "llms", "llms-sitemap", "security", "code_of_conduct",
    "code-of-conduct", "authors", "maintainers", "contributors",
}


def strip_code_blocks(text: str) -> str:
    """Remove fenced code blocks and inline code so we don't match error signals inside examples."""
    # Remove fenced code blocks (``` ... ```)
    text = re.sub(r"```[\s\S]*?```", "", text)
    # Remove indented code blocks (4-space indent)
    text = re.sub(r"(?m)^    .+$", "", text)
    # Remove inline code
    text = re.sub(r"`[^`]+`", "", text)
    return text


def is_bad_content(text: str) -> tuple[bool, str]:
    """Check if content is a bad fetch (404, bot protection, etc.)"""
    # Check raw patterns (obfuscated JS etc.) against full text
    for pattern in RAW_PATTERNS:
        if pattern.search(text):
            return True, f"bot/obfuscated: {pattern.pattern[:40]}"

    # Check prose error signals against text with code blocks removed
    prose = strip_code_blocks(text)
    for pattern in PROSE_PATTERNS:
        if pattern.search(prose):
            return True, f"error page: {pattern.pattern[:50]}"

    # Check if file is almost entirely script tags (bot protection page)
    # Only flag if <script> appears in the first 500 chars with no real headings before it
    first_500 = text[:500]
    if "<script" in first_500.lower():
        headings_before = re.findall(r"^#{1,3} \w", first_500, re.MULTILINE)
        if not headings_before:
            return True, "script tag in page header (bot protection)"

    return False, ""


def scan_library(lib_dir: Path, source: str) -> dict | None:
    """Scan a single library directory. Returns None if quality is OK."""
    all_files = (
        list(lib_dir.glob("**/*.md"))
        + list(lib_dir.glob("**/*.rst"))
        + list(lib_dir.glob("**/*.txt"))
    )
    if not all_files:
        return None

    total_bytes = sum(f.stat().st_size for f in all_files)

    # Check for empty/stub
    if total_bytes < 500:
        return {
            "source": source,
            "library": lib_dir.name,
            "verdict": "STUB",
            "reason": f"total size {total_bytes} bytes",
            "files": len(all_files),
            "kb": total_bytes / 1024,
        }

    # Sample the largest file for content checks
    largest = max(all_files, key=lambda f: f.stat().st_size)
    try:
        text = largest.read_text(errors="ignore")[:50000]
    except Exception:
        return None

    # Check for bad content
    bad, reason = is_bad_content(text)
    if bad:
        return {
            "source": source,
            "library": lib_dir.name,
            "verdict": "BAD_CONTENT",
            "reason": reason,
            "files": len(all_files),
            "kb": total_bytes / 1024,
            "sample_file": str(largest.name),
        }

    # Check if all files are generic names with no real content
    real_files = [f for f in all_files if f.stem.lower() not in GENERIC_NAMES]
    if not real_files and total_bytes < 5000:
        return {
            "source": source,
            "library": lib_dir.name,
            "verdict": "GENERIC_ONLY",
            "reason": f"only generic files, {total_bytes} bytes total",
            "files": len(all_files),
            "kb": total_bytes / 1024,
        }

    return None  # OK


def scan_source(source: str, workers: int) -> list[dict]:
    src_dir = DOCS_ROOT / source
    if not src_dir.exists():
        return []

    lib_dirs = [d for d in src_dir.iterdir() if d.is_dir()]
    results = []

    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {executor.submit(scan_library, d, source): d for d in lib_dirs}
        for future in as_completed(futures):
            result = future.result()
            if result:
                results.append(result)

    return results


def main():
    parser = argparse.ArgumentParser(description="Quality scanner for llm-code-docs")
    parser.add_argument("--source", choices=SOURCES, help="Scan only this source")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument("--fix", action="store_true", help="Delete confirmed dead entries (STUB + BAD_CONTENT)")
    parser.add_argument("--workers", type=int, default=16, help="Parallel workers (default: 16)")
    args = parser.parse_args()

    sources = [args.source] if args.source else SOURCES

    all_results = []
    for source in sources:
        if not args.json:
            print(f"Scanning {source}...", file=sys.stderr)
        results = scan_source(source, args.workers)
        all_results.extend(results)

    # Sort: BAD_CONTENT first, then STUB, then GENERIC_ONLY; within each by size
    order = {"BAD_CONTENT": 0, "STUB": 1, "GENERIC_ONLY": 2}
    all_results.sort(key=lambda x: (order.get(x["verdict"], 9), x["kb"]))

    if args.json:
        print(json.dumps(all_results, indent=2))
        return

    if not all_results:
        print("✓ All libraries pass quality checks.")
        return

    # Group by verdict
    by_verdict = {}
    for r in all_results:
        by_verdict.setdefault(r["verdict"], []).append(r)

    for verdict, items in sorted(by_verdict.items(), key=lambda x: order.get(x[0], 9)):
        print(f"\n{verdict} ({len(items)}):")
        print(f"  {'Source':<15} {'Library':<35} {'Files':<6} {'Size':<8} Reason")
        print(f"  {'-'*85}")
        for r in items:
            print(f"  {r['source']:<15} {r['library']:<35} {r['files']:<6} {r['kb']:<7.0f}KB {r['reason']}")

    print(f"\nTotal: {len(all_results)} libraries need attention")

    if args.fix:
        to_delete = [r for r in all_results if r["verdict"] in ("BAD_CONTENT", "STUB")]
        if not to_delete:
            print("\nNothing to auto-fix.")
            return
        print(f"\nDeleting {len(to_delete)} confirmed bad entries...")
        for r in to_delete:
            lib_dir = DOCS_ROOT / r["source"] / r["library"]
            import shutil
            shutil.rmtree(lib_dir)
            print(f"  Deleted {r['source']}/{r['library']}")
        print("Done. Run 'git add -A && git commit' to save.")


if __name__ == "__main__":
    main()
