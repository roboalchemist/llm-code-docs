#!/usr/bin/env python3
"""
Quality scorer for llm-code-docs libraries.

Scores every library 0-100 with visible heuristic signal breakdown.
Run --eval to measure accuracy against the labelled eval set.

Usage:
    python3 scripts/quality-check.py                   # score all
    python3 scripts/quality-check.py --min-score 50    # show score <= 50
    python3 scripts/quality-check.py --source llms-txt
    python3 scripts/quality-check.py --json
    python3 scripts/quality-check.py --fix             # delete score-0 entries
    python3 scripts/quality-check.py --eval            # run against eval set
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
EVAL_SET  = Path(__file__).parent / "quality-eval-set.json"
SOURCES = ["llms-txt", "github-scraped", "web-scraped"]

GENERIC_NAMES = {
    "readme", "contributing", "license", "changelog", "index",
    "llms-full", "llms", "llms-sitemap", "security", "code_of_conduct",
    "code-of-conduct", "authors", "maintainers", "contributors",
}

# ── Error / dead-page detection ───────────────────────────────────────────────

# Checked on prose-only (code blocks stripped)
PROSE_ERROR_PATTERNS = [re.compile(p, re.MULTILINE) for p in [
    r"(?i)^#{1,3}\s*(error\s*404|page not found|404 not found|403 forbidden)",
    r"(?i)^##\s*error\s*\d{3}",
    r"(?i)we couldn.t find the page",
    r"(?i)the page you.re looking for",
    r"(?i)this page does not exist",
    r"(?i)cloudflare.*ray id",
    r"(?i)just a moment\.?\s*$",
    r"(?i)^#+\s*(access denied|403 forbidden|unauthorized)",
    r"(?i)docs\.rs failed to build",
    r"(?i)failed to build .{0,60}",
]]

# Checked on full raw text
RAW_ERROR_PATTERNS = [re.compile(p) for p in [
    r"_0x[0-9a-f]{4}[^`\n]{20,}",   # obfuscated JS
    r"document\[_0x",
    r"(?i)EO_Bot_Ssid",
    r"(?i)setTimeout\(_0x",
]]

# HTML dump detection (checked in first 1000 chars of largest file)
HTML_DUMP_PATTERNS = [re.compile(p, re.IGNORECASE) for p in [
    r"<!DOCTYPE\s+html",
    r"<html[\s>]",
    r"<head[\s>]",
]]


def strip_code_blocks(text: str) -> str:
    text = re.sub(r"```[\s\S]*?```", "", text)
    text = re.sub(r"(?m)^    .+$", "", text)
    text = re.sub(r"`[^`]+`", "", text)
    return text


def count_code_lines(text: str) -> int:
    """Count lines inside fenced OR indented code blocks."""
    total = 0
    in_block = False
    lines = text.split("\n")
    for i, line in enumerate(lines):
        if line.strip().startswith("```"):
            in_block = not in_block
            continue
        if in_block:
            total += 1
            continue
        # Count indented code (4+ spaces or tab, not inside list items)
        if re.match(r'^(    |\t)\S', line):
            total += 1
    return total


def count_all_headings(text: str) -> int:
    """Count markdown headings AND RST underline-style headings."""
    prose = strip_code_blocks(text)
    lines = prose.split("\n")
    md_headings = len(re.findall(r"^#{1,4} \w", prose, re.MULTILINE))
    # RST underline headings: non-empty text line followed by line of === or ---
    # Require the underline to be at least 4 chars (avoid false positives)
    rst_count = 0
    for i in range(1, len(lines)):
        ul = lines[i].strip()
        prev = lines[i-1].strip()
        if (ul and prev and len(ul) >= 4
                and len(ul) >= len(prev) * 0.6
                and re.match(r'^[=\-~^]+$', ul)
                and not prev.startswith(':')     # skip RST directives
                and not prev.startswith('..')):  # skip RST directives
            rst_count += 1
    return md_headings + rst_count


def has_autodoc_stubs(text: str) -> bool:
    """Detect RST autodoc/autosummary stubs (placeholder, no real content)."""
    return bool(re.search(r'^\.\.\s+(automodule|autosummary|autoclass|autofunction)::', text, re.MULTILINE))


def is_html_dump(text: str) -> bool:
    """Return True if the file is a raw HTML page (not just markdown with HTML tables)."""
    # Only flag as HTML dump if the document ROOT is HTML — DOCTYPE or <html> within first 200 chars
    # This avoids flagging markdown files that contain inline HTML tables
    first = text[:200].strip()
    for pat in HTML_DUMP_PATTERNS:
        if pat.search(first):
            return True
    return False


def is_dead_content(text: str) -> tuple[bool, str]:
    for pat in RAW_ERROR_PATTERNS:
        if pat.search(text):
            return True, "obfuscated-js"
    prose = strip_code_blocks(text)
    for pat in PROSE_ERROR_PATTERNS:
        if pat.search(prose):
            return True, "error-page"
    if is_html_dump(text):
        return True, "html-dump"
    # Script tag before first heading (bot protection)
    first_500 = text[:500]
    if "<script" in first_500.lower():
        if not re.search(r"^#{1,3} \w", first_500, re.MULTILINE):
            return True, "bot-protect"
    return False, ""


# ── Scoring ───────────────────────────────────────────────────────────────────

@dataclass
class LibraryScore:
    source: str
    library: str
    score: int
    files: int
    kb: float

    # Heuristic signals
    h_dead: bool = False
    h_stub: bool = False
    h_html_dump: bool = False
    h_generic_only: bool = False
    h_single_file: bool = False
    h_avg_file_stub: bool = False    # avg file < 2KB (stub pages)
    h_has_headings: bool = False     # >= 3 headings in largest file
    h_has_code: bool = False         # >= 2 code blocks
    h_good_example_ratio: bool = False  # code lines >= 15% of total lines
    h_has_links: bool = False
    h_size_ok: bool = False          # >= 10KB
    h_multi_file: bool = False       # >= 5 real files
    h_large: bool = False            # >= 100KB
    h_code_dense: bool = False       # >= 1 code block per 100KB
    h_llms_txt_source: bool = False  # source is llms-txt

    error_reason: str = ""

    def signals(self) -> str:
        parts = []
        if self.h_dead:           parts.append(f"DEAD({self.error_reason})")
        if self.h_stub:           parts.append("STUB")
        if self.h_html_dump:      parts.append("HTML-DUMP")
        if self.h_generic_only:   parts.append("GENERIC-ONLY")
        if self.h_single_file:    parts.append("single-file")
        if self.h_avg_file_stub:  parts.append("stub-files⚠")
        if self.h_llms_txt_source: parts.append("llms-txt+")
        if self.h_has_headings:   parts.append("headings✓")
        if self.h_has_code:       parts.append("code✓")
        if self.h_good_example_ratio: parts.append("examples✓")
        if self.h_has_links:      parts.append("links✓")
        if self.h_size_ok:        parts.append("size✓")
        if self.h_multi_file:     parts.append("multi-file✓")
        if self.h_large:          parts.append("large✓")
        if self.h_code_dense:     parts.append("code-dense✓")
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

    s = LibraryScore(source=source, library=lib_dir.name, score=0,
                     files=len(all_files), kb=kb)

    s.h_llms_txt_source = (source == "llms-txt")

    # --- Hard failures ---

    if total_bytes < 500:
        s.h_stub = True
        s.score = 0
        return s

    largest = max(all_files, key=lambda f: f.stat().st_size)
    largest_bytes = largest.stat().st_size
    try:
        raw = largest.read_text(errors="ignore")
        # For large files, sample beginning + middle + end
        if len(raw) > 150000:
            chunk = 50000
            text = raw[:chunk] + raw[len(raw)//2 - chunk//2 : len(raw)//2 + chunk//2] + raw[-chunk:]
        else:
            text = raw[:200000]
    except Exception:
        s.score = 0
        return s

    # Aggregate content from multiple files (not just largest) for better signal coverage
    # Sample up to 5 additional files for heading/code counting
    agg_text = text
    if len(all_files) > 1:
        other_files = sorted(
            [f for f in all_files if f != largest],
            key=lambda f: f.stat().st_size, reverse=True
        )[:4]
        for f in other_files:
            try:
                agg_text += "\n" + f.read_text(errors="ignore")[:30000]
            except Exception:
                pass

    # HTML dump check (before other checks)
    if is_html_dump(text):
        s.h_dead = True
        s.h_html_dump = True
        s.error_reason = "html-dump"
        s.score = 0
        return s

    # Other dead content checks
    for pat in RAW_ERROR_PATTERNS:
        if pat.search(text):
            s.h_dead = True
            s.error_reason = "obfuscated-js"
            s.score = 0
            return s

    prose = strip_code_blocks(text)
    for pat in PROSE_ERROR_PATTERNS:
        if pat.search(prose):
            s.h_dead = True
            s.error_reason = "error-page"
            s.score = 0
            return s

    first_500 = text[:500]
    if "<script" in first_500.lower():
        if not re.search(r"^#{1,3} \w", first_500, re.MULTILINE):
            s.h_dead = True
            s.error_reason = "bot-protect"
            s.score = 0
            return s

    # --- Heuristic scoring ---

    score = 0

    # Source bonus: llms-txt is purpose-built for LLM consumption
    if s.h_llms_txt_source:
        score += 5

    # Generic-only / real content check
    s.h_generic_only = not real_files
    if real_files:
        score += 8
    else:
        score += 2

    # File count signals
    s.h_single_file = len(all_files) == 1
    num_real = len(real_files)
    if num_real >= 10:
        s.h_multi_file = True
        score += 18
    elif num_real >= 5:
        s.h_multi_file = True
        score += 12
    elif num_real >= 2:
        score += 6

    # Avg file size penalty: many tiny files = nav stubs
    if len(all_files) >= 5:
        avg_kb = kb / len(all_files)
        if avg_kb < 1.0:
            s.h_avg_file_stub = True
            score -= 30
        elif avg_kb < 2.0:
            s.h_avg_file_stub = True
            score -= 22
        elif avg_kb < 4.0:
            score -= 10

    # Random-sample stub check for large libraries (>50 files)
    # Detect when most files are actually stubs despite large totals
    if len(all_files) > 50:
        import random
        rng = random.Random(42)
        sample = rng.sample(all_files, min(15, len(all_files)))
        stub_count = sum(1 for f in sample if f.stat().st_size < 1500)
        stub_ratio = stub_count / len(sample)
        if stub_ratio > 0.6:
            s.h_avg_file_stub = True
            score -= int(35 * stub_ratio)  # -21 to -35 depending on severity

    # Size signals (total library size)
    if kb >= 100:
        s.h_large = True
        score += 20
    elif kb >= 10:
        s.h_size_ok = True
        score += 12
    elif kb >= 2:
        score += 5

    # Content signals — aggregate across largest + up to 4 more files
    agg_lines = agg_text.split("\n")
    total_lines = max(len(agg_lines), 1)
    code_lines = count_code_lines(agg_text)
    code_blocks = agg_text.count("```") // 2
    # Count indented runs: only runs that look like real code (contain =, (, ), {, })
    indented_runs = len(re.findall(
        r"(?m)(?:^(?:    |\t)[^\n]*[=(){};:\[\]<>][^\n]*\n){2,}", agg_text
    ))
    effective_code_blocks = code_blocks + indented_runs

    # Autodoc stubs: RST placeholder directives = lower quality
    autodoc_stub = has_autodoc_stubs(agg_text)
    if autodoc_stub:
        score -= 12

    # Headings across aggregated text
    heading_count = count_all_headings(agg_text)
    large_file = largest_bytes > 200000

    # Penalize heading-dense short files (navigation lists)
    heading_density = heading_count / max(total_lines, 1)
    if kb < 10 and heading_count >= 5 and heading_density > 0.15:
        score -= 10

    if heading_count >= 10:
        s.h_has_headings = True
        score += 18
    elif heading_count >= 5:
        s.h_has_headings = True
        score += 14
    elif heading_count >= 3:
        s.h_has_headings = True
        score += 10
    elif heading_count >= 1:
        s.h_has_headings = large_file
        score += (8 if large_file else 4)

    if effective_code_blocks >= 4:
        s.h_has_code = True
        score += 14
    elif effective_code_blocks >= 2:
        s.h_has_code = True
        score += 8

    # Example ratio: code lines as % of total — best discriminator
    example_ratio = code_lines / total_lines
    if example_ratio >= 0.15:
        s.h_good_example_ratio = True
        score += 18
    elif example_ratio >= 0.05:
        score += 8

    # Code density normalized by size
    if kb > 0:
        code_per_kb = effective_code_blocks / kb
        if code_per_kb >= 0.5:
            s.h_code_dense = True
            score += 10
        elif code_per_kb >= 0.1:
            score += 4

    # Penalize large multi-file library with very low code per file
    if s.h_multi_file and len(all_files) > 20:
        cpf = effective_code_blocks / len(all_files)
        if cpf < 0.05:
            score -= 20  # ENV0/Debricked pattern: hundreds of files, barely any code

    # Penalize large+multi-file with zero effective code (mapkit nav-scrape pattern)
    if kb > 100 and s.h_multi_file and effective_code_blocks == 0:
        score -= 15

    prose_agg = strip_code_blocks(agg_text)
    links = prose_agg.count("](")
    if links >= 5:
        s.h_has_links = True
        score += 8
    elif links >= 2:
        score += 4

    s.score = max(0, min(score, 100))
    return s


# ── Scanning ──────────────────────────────────────────────────────────────────

def scan_source(source: str, workers: int) -> list[LibraryScore]:
    src_dir = DOCS_ROOT / source
    if not src_dir.exists():
        return []
    lib_dirs = [d for d in src_dir.iterdir() if d.is_dir()]
    results = []
    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {executor.submit(score_library, d, source): d for d in lib_dirs}
        for future in as_completed(futures):
            r = future.result()
            if r is not None:
                results.append(r)
    return results


# ── Eval ──────────────────────────────────────────────────────────────────────

def run_eval(workers: int):
    if not EVAL_SET.exists():
        print(f"Eval set not found: {EVAL_SET}", file=sys.stderr)
        return

    cases = json.loads(EVAL_SET.read_text())
    scores_by_key = {}
    for source in SOURCES:
        for s in scan_source(source, workers):
            scores_by_key[(s.source, s.library)] = s

    passed = failed = 0
    print(f"\n{'Pass':<5} {'Score':<7} {'Range':<12} {'Source':<15} {'Library':<35} {'Signals'}")
    print("-" * 120)
    for case in cases:
        key = (case["source"], case["library"])
        s = scores_by_key.get(key)
        if s is None:
            rng = f"{case['min_score']}-{case['max_score']}"
            print(f"{'MISS':<5} {'N/A':<7} {rng:<12} {case['source']:<15} {case['library']:<35} (not found)")
            failed += 1
            continue
        in_range = case["min_score"] <= s.score <= case["max_score"]
        icon = "✓" if in_range else "✗"
        score_str = f"{s.score}"
        range_str = f"{case['min_score']}-{case['max_score']}"
        print(f"{icon:<5} {score_str:<7} {range_str:<12} {s.source:<15} {s.library:<35} {s.signals()}")
        if in_range:
            passed += 1
        else:
            failed += 1

    total = passed + failed
    pct = 100 * passed / total if total else 0
    print(f"\nResult: {passed}/{total} passed ({pct:.0f}%)")


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Quality scorer for llm-code-docs")
    parser.add_argument("--source", choices=SOURCES)
    parser.add_argument("--min-score", type=int, default=101,
                        help="Show libraries with score <= this (default: show all)")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--fix", action="store_true", help="Delete score-0 entries")
    parser.add_argument("--eval", action="store_true", help="Run eval set accuracy test")
    parser.add_argument("--workers", type=int, default=16)
    args = parser.parse_args()

    if args.eval:
        run_eval(args.workers)
        return

    sources = [args.source] if args.source else SOURCES
    show_all = args.min_score == 101

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
        print(f"{s.score:<7} {s.source:<15} {s.library:<35} {s.files:<6} {s.kb:<8.0f}KB {s.signals()}")

    print(f"\n{len(filtered)} libraries shown (total: {len(all_scores)})")

    buckets = [
        ("  0 (dead)",   lambda s: s.score == 0),
        (" 1-25 (poor)", lambda s: 1 <= s.score <= 25),
        ("26-50 (weak)", lambda s: 26 <= s.score <= 50),
        ("51-75 (ok)",   lambda s: 51 <= s.score <= 75),
        ("76+ (good)",   lambda s: s.score > 75),
    ]
    print("\nScore distribution:")
    for label, fn in buckets:
        n = sum(1 for s in all_scores if fn(s))
        bar = "█" * min(n // 5, 60)
        print(f"  {label}: {n:4d}  {bar}")

    if args.fix:
        to_del = [s for s in all_scores if s.score == 0]
        if not to_del:
            print("\nNothing to delete.")
            return
        print(f"\nDeleting {len(to_del)} score-0 entries...")
        for s in to_del:
            shutil.rmtree(DOCS_ROOT / s.source / s.library, ignore_errors=True)
            print(f"  Deleted {s.source}/{s.library}")
        print("Done. Run 'git add -A && git commit' to save.")


if __name__ == "__main__":
    main()
