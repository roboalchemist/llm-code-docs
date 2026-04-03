#!/usr/bin/env python3
"""
Quality scanner for llm-code-docs libraries.

Scores every library 0-100 across multiple heuristics and reports all results.
Use --min-score to filter (default: show all). Use --fix to delete score-0 entries.

Usage:
    python3 scripts/quality-check.py                   # score all, show everything
    python3 scripts/quality-check.py --min-score 50    # show only score < 50
    python3 scripts/quality-check.py --source llms-txt
    python3 scripts/quality-check.py --json
    python3 scripts/quality-check.py --fix             # delete score-0 entries
    python3 scripts/quality-check.py --workers 32
"""

import argparse
import json
import re
import shutil
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field, asdict
from pathlib import Path


DOCS_ROOT = Path(__file__).parent.parent / "docs"
SOURCES = ["llms-txt", "github-scraped", "web-scraped"]

GENERIC_NAMES = {
    "readme", "contributing", "license", "changelog", "index",
    "llms-full", "llms", "llms-sitemap", "security", "code_of_conduct",
    "code-of-conduct", "authors", "maintainers", "contributors",
}

# Checked on prose only (code blocks stripped)
PROSE_ERROR_PATTERNS = [re.compile(p, re.MULTILINE) for p in [
    r"(?i)^#{1,3}\s*(error\s*404|page not found|404 not found|403 forbidden)",
    r"(?i)^##\s*error\s*\d{3}",
    r"(?i)we couldn.t find the page",
    r"(?i)the page you.re looking for",
    r"(?i)this page does not exist",
    r"(?i)cloudflare.*ray id",
    r"(?i)just a moment\.?\s*$",
    r"(?i)^#+\s*(access denied|403 forbidden|unauthorized)",
]]

# Checked on raw text
RAW_ERROR_PATTERNS = [re.compile(p) for p in [
    r"_0x[0-9a-f]{4}[^`\n]{20,}",
    r"document\[_0x",
    r"(?i)EO_Bot_Ssid",
    r"(?i)setTimeout\(_0x",
]]


def strip_code_blocks(text: str) -> str:
    text = re.sub(r"```[\s\S]*?```", "", text)
    text = re.sub(r"(?m)^    .+$", "", text)
    text = re.sub(r"`[^`]+`", "", text)
    return text


@dataclass
class LibraryScore:
    source: str
    library: str
    score: int                      # 0-100 final score
    files: int
    kb: float

    # Individual heuristic signals (shown in report)
    h_error_page: bool = False      # 404/bot-protection detected
    h_stub: bool = False            # < 500 bytes total
    h_generic_only: bool = False    # only README/CONTRIBUTING etc.
    h_single_file: bool = False     # exactly 1 file
    h_has_headings: bool = False    # >= 3 real headings
    h_has_code: bool = False        # >= 2 code blocks
    h_has_links: bool = False       # >= 5 links
    h_size_ok: bool = False         # >= 10KB
    h_multi_file: bool = False      # >= 5 real files
    h_large: bool = False           # >= 100KB

    error_reason: str = ""

    def signals(self) -> str:
        """Compact signal string for display."""
        parts = []
        if self.h_error_page:   parts.append(f"ERROR({self.error_reason[:30]})")
        if self.h_stub:         parts.append("STUB")
        if self.h_generic_only: parts.append("GENERIC-ONLY")
        if self.h_single_file:  parts.append("single-file")
        if self.h_has_headings: parts.append("headings✓")
        if self.h_has_code:     parts.append("code✓")
        if self.h_has_links:    parts.append("links✓")
        if self.h_size_ok:      parts.append("size✓")
        if self.h_multi_file:   parts.append("multi-file✓")
        if self.h_large:        parts.append("large✓")
        return " ".join(parts) if parts else "ok"


def score_library(lib_dir: Path, source: str) -> LibraryScore | None:
    all_files = (
        list(lib_dir.glob("**/*.md"))
        + list(lib_dir.glob("**/*.rst"))
        + list(lib_dir.glob("**/*.txt"))
    )
    if not all_files:
        return None

    total_bytes = sum(f.stat().st_size for f in all_files)
    kb = total_bytes / 1024
    real_files = [f for f in all_files if f.stem.lower() not in GENERIC_NAMES]

    s = LibraryScore(
        source=source,
        library=lib_dir.name,
        score=0,
        files=len(all_files),
        kb=kb,
    )

    # --- Hard failures (score = 0) ---

    if total_bytes < 500:
        s.h_stub = True
        s.score = 0
        return s

    # Sample largest file
    largest = max(all_files, key=lambda f: f.stat().st_size)
    try:
        text = largest.read_text(errors="ignore")[:60000]
    except Exception:
        s.score = 0
        return s

    # Raw error signals
    for pat in RAW_ERROR_PATTERNS:
        if pat.search(text):
            s.h_error_page = True
            s.error_reason = f"obfuscated-js"
            s.score = 0
            return s

    # Prose error signals
    prose = strip_code_blocks(text)
    for pat in PROSE_ERROR_PATTERNS:
        if pat.search(prose):
            s.h_error_page = True
            s.error_reason = "error-page"
            s.score = 0
            return s

    # Script tag in header (bot protection)
    first_500 = text[:500]
    if "<script" in first_500.lower():
        headings_before = re.findall(r"^#{1,3} \w", first_500, re.MULTILINE)
        if not headings_before:
            s.h_error_page = True
            s.error_reason = "bot-protect"
            s.score = 0
            return s

    # --- Heuristic scoring ---

    score = 0

    # Generic-only files (no real content pages)
    if not real_files:
        s.h_generic_only = True
        # Still score on content quality of what's there
        score += 5
    else:
        score += 10

    # File count
    s.h_single_file = len(all_files) == 1
    if len(real_files) >= 5:
        s.h_multi_file = True
        score += 20
    elif len(real_files) >= 2:
        score += 10

    # Size
    if kb >= 100:
        s.h_large = True
        score += 25
    elif kb >= 10:
        s.h_size_ok = True
        score += 15
    elif kb >= 2:
        score += 5

    # Content quality from largest file
    headings = re.findall(r"^#{1,4} \w", prose, re.MULTILINE)
    if len(headings) >= 3:
        s.h_has_headings = True
        score += 20
    elif len(headings) >= 1:
        score += 10

    code_blocks = text.count("```")
    if code_blocks >= 4:
        s.h_has_code = True
        score += 15
    elif code_blocks >= 2:
        score += 7

    links = prose.count("](")
    if links >= 5:
        s.h_has_links = True
        score += 10

    s.score = min(score, 100)
    return s


def scan_source(source: str, workers: int) -> list[LibraryScore]:
    src_dir = DOCS_ROOT / source
    if not src_dir.exists():
        return []
    lib_dirs = [d for d in src_dir.iterdir() if d.is_dir()]
    results = []
    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {executor.submit(score_library, d, source): d for d in lib_dirs}
        for future in as_completed(futures):
            result = future.result()
            if result is not None:
                results.append(result)
    return results


def main():
    parser = argparse.ArgumentParser(description="Quality scorer for llm-code-docs")
    parser.add_argument("--source", choices=SOURCES, help="Scan only this source")
    parser.add_argument("--min-score", type=int, default=101,
                        help="Only show libraries with score <= this value (default: show all)")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument("--fix", action="store_true", help="Delete score-0 entries")
    parser.add_argument("--workers", type=int, default=16, help="Parallel workers (default: 16)")
    args = parser.parse_args()

    sources = [args.source] if args.source else SOURCES
    show_all = args.min_score == 101  # default: show everything

    all_scores: list[LibraryScore] = []
    for source in sources:
        if not args.json:
            print(f"Scanning {source}...", file=sys.stderr)
        all_scores.extend(scan_source(source, args.workers))

    all_scores.sort(key=lambda x: (x.score, x.kb))

    threshold = 100 if show_all else args.min_score
    filtered = [s for s in all_scores if s.score <= threshold]

    if args.json:
        print(json.dumps([asdict(s) for s in filtered], indent=2))
        return

    if not filtered:
        print(f"✓ All {len(all_scores)} libraries score above {threshold}.")
        return

    print(f"\n{'Score':<7} {'Source':<15} {'Library':<35} {'Files':<6} {'Size':<9} Signals")
    print("-" * 110)
    for s in filtered:
        score_str = f"{s.score:3d}"
        print(f"{score_str:<7} {s.source:<15} {s.library:<35} {s.files:<6} {s.kb:<8.0f}KB {s.signals()}")

    print(f"\n{len(filtered)} libraries shown (total scanned: {len(all_scores)})")

    # Summary stats
    buckets = {
        "  0 (dead)":   [s for s in all_scores if s.score == 0],
        " 1-25 (poor)": [s for s in all_scores if 1 <= s.score <= 25],
        "26-50 (weak)": [s for s in all_scores if 26 <= s.score <= 50],
        "51-75 (ok)":   [s for s in all_scores if 51 <= s.score <= 75],
        "76+ (good)":   [s for s in all_scores if s.score > 75],
    }
    print("\nScore distribution:")
    for label, items in buckets.items():
        bar = "█" * min(len(items) // 5, 60)
        print(f"  {label}: {len(items):4d}  {bar}")

    if args.fix:
        to_delete = [s for s in all_scores if s.score == 0]
        if not to_delete:
            print("\nNothing to delete (no score-0 entries).")
            return
        print(f"\nDeleting {len(to_delete)} score-0 entries...")
        for s in to_delete:
            lib_dir = DOCS_ROOT / s.source / s.library
            shutil.rmtree(lib_dir, ignore_errors=True)
            print(f"  Deleted {s.source}/{s.library}")
        print("Done. Run 'git add -A && git commit' to save.")


if __name__ == "__main__":
    main()
