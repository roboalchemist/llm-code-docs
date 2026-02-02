#!/usr/bin/env python3
"""
Markdown Quality Validator for llm-code-docs

Scans all .md files and scores them on quality metrics to identify
files that aren't "real" markdown or have quality issues.

Usage:
    python3 scripts/validate-markdown.py                    # Full report
    python3 scripts/validate-markdown.py --json             # JSON output
    python3 scripts/validate-markdown.py --source llms-txt  # Specific source
    python3 scripts/validate-markdown.py --fix-report       # Generate fix recommendations
"""

import argparse
import json
import re
import subprocess
import sys
from collections import defaultdict
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Optional


@dataclass
class FileQuality:
    path: str
    size_bytes: int
    line_count: int
    source: str  # llms-txt, github-scraped, web-scraped

    # Quality scores (0-100, higher is better)
    overall_score: int = 100

    # Issues found
    issues: list = field(default_factory=list)

    # Metrics
    has_headings: bool = False
    heading_count: int = 0
    has_code_blocks: bool = False
    code_block_count: int = 0
    has_links: bool = False
    link_count: int = 0
    html_tag_count: int = 0
    html_density: float = 0.0  # tags per line

    # Flags
    is_empty: bool = False
    is_stub: bool = False
    is_binary: bool = False
    has_nav_artifacts: bool = False
    has_docusaurus_html: bool = False
    has_encoding_issues: bool = False


def check_encoding(path: Path) -> tuple[bool, str]:
    """Check if file has encoding issues using `file` command."""
    try:
        result = subprocess.run(
            ['file', str(path)],
            capture_output=True, text=True, timeout=5
        )
        output = result.stdout.lower()

        if 'utf-8' in output or 'ascii' in output or 'empty' in output:
            return True, 'utf-8'
        elif 'dyalog' in output or 'data' in output:
            return False, output.strip()
        else:
            return True, output.strip()
    except Exception as e:
        return True, str(e)


def analyze_file(path: Path, docs_root: Path) -> Optional[FileQuality]:
    """Analyze a single markdown file for quality issues."""

    # Determine source
    rel_path = path.relative_to(docs_root)
    parts = rel_path.parts
    if len(parts) >= 2:
        source = parts[0]  # llms-txt, github-scraped, web-scraped
    else:
        source = 'unknown'

    # Basic stats
    try:
        size = path.stat().st_size
    except OSError:
        return None

    quality = FileQuality(
        path=str(rel_path),
        size_bytes=size,
        line_count=0,
        source=source
    )

    # Check for empty files
    if size == 0:
        quality.is_empty = True
        quality.issues.append('empty_file')
        quality.overall_score = 0
        return quality

    # Check encoding
    is_valid_encoding, encoding_info = check_encoding(path)
    if not is_valid_encoding:
        quality.is_binary = True
        quality.has_encoding_issues = True
        quality.issues.append(f'encoding_issue: {encoding_info}')
        quality.overall_score = 0
        return quality

    # Read content
    try:
        content = path.read_text(encoding='utf-8', errors='replace')
    except Exception as e:
        quality.issues.append(f'read_error: {e}')
        quality.overall_score = 0
        return quality

    lines = content.split('\n')
    quality.line_count = len(lines)

    # Check for stub/placeholder content
    stub_patterns = [
        r'^#\s*PLACEHOLDER\s*$',
        r'^#\s*TODO\s*$',
        r'^#\s*WIP\s*$',
        r'^\[object Object\]',
        r'^\[object Array\]',
    ]
    for pattern in stub_patterns:
        if re.search(pattern, content, re.MULTILINE):
            quality.is_stub = True
            quality.issues.append('stub_placeholder')
            break

    # Count markdown features
    quality.heading_count = len(re.findall(r'^#{1,6}\s+\S', content, re.MULTILINE))
    quality.has_headings = quality.heading_count > 0

    quality.code_block_count = len(re.findall(r'```', content)) // 2
    quality.has_code_blocks = quality.code_block_count > 0

    quality.link_count = len(re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content))
    quality.has_links = quality.link_count > 0

    # Count HTML tags
    html_tags = re.findall(r'<[a-zA-Z][^>]*>', content)
    quality.html_tag_count = len(html_tags)
    quality.html_density = quality.html_tag_count / max(quality.line_count, 1)

    # Check for Docusaurus/React HTML artifacts
    docusaurus_patterns = [
        r'class="anchor',
        r'anchorTargetStickyNavbar',
        r'style=\{\{',
        r'className=',
        r'data-sentry-',
    ]
    for pattern in docusaurus_patterns:
        if re.search(pattern, content):
            quality.has_docusaurus_html = True
            quality.issues.append('docusaurus_html')
            break

    # Check for navigation artifacts
    nav_patterns = [
        r'Skip to (main )?content',
        r'Search for:',
        r'javascript:void\(0\)',
        r'\[ Open toolbar',
        r'Products!|Solutions!|Resources!',
        r'\[ \]\(https?://',  # Empty link text
    ]
    for pattern in nav_patterns:
        if re.search(pattern, content, re.IGNORECASE):
            quality.has_nav_artifacts = True
            quality.issues.append('nav_artifacts')
            break

    # Calculate overall score
    score = 100

    # Penalties
    if quality.is_empty:
        score = 0
    elif quality.is_stub:
        score = 10
    elif quality.is_binary:
        score = 0
    else:
        # Size penalties
        if size < 50:
            score -= 30
            quality.issues.append('very_small_file')
        elif size < 200:
            score -= 15
            quality.issues.append('small_file')

        # No headings penalty
        if not quality.has_headings:
            score -= 20
            quality.issues.append('no_headings')

        # High HTML density penalty
        if quality.html_density > 0.3:
            score -= 40
            quality.issues.append('high_html_density')
        elif quality.html_density > 0.1:
            score -= 20
            quality.issues.append('moderate_html_density')

        # Docusaurus artifacts
        if quality.has_docusaurus_html:
            score -= 15

        # Nav artifacts
        if quality.has_nav_artifacts:
            score -= 20

        # Bonuses for good content
        if quality.has_code_blocks and quality.code_block_count >= 3:
            score += 10
        if quality.heading_count >= 5:
            score += 5

    quality.overall_score = max(0, min(100, score))
    return quality


def main():
    parser = argparse.ArgumentParser(description='Validate markdown file quality')
    parser.add_argument('--json', action='store_true', help='Output as JSON')
    parser.add_argument('--source', choices=['llms-txt', 'github-scraped', 'web-scraped'],
                        help='Only check specific source')
    parser.add_argument('--min-score', type=int, default=0,
                        help='Only show files below this score (default: show all)')
    parser.add_argument('--max-score', type=int, default=100,
                        help='Only show files at or below this score')
    parser.add_argument('--fix-report', action='store_true',
                        help='Generate detailed fix recommendations')
    parser.add_argument('--limit', type=int, default=0,
                        help='Limit output to N files per category')
    args = parser.parse_args()

    docs_root = Path('/Users/joe/github/llm-code-docs/docs')

    # Find all markdown files
    if args.source:
        search_path = docs_root / args.source
    else:
        search_path = docs_root

    md_files = list(search_path.rglob('*.md'))
    print(f"Scanning {len(md_files)} markdown files...", file=sys.stderr)

    # Analyze all files
    results = []
    for i, path in enumerate(md_files):
        if (i + 1) % 1000 == 0:
            print(f"  Processed {i + 1}/{len(md_files)}...", file=sys.stderr)

        quality = analyze_file(path, docs_root)
        if quality:
            results.append(quality)

    # Filter by score
    if args.min_score > 0 or args.max_score < 100:
        results = [r for r in results if args.min_score <= r.overall_score <= args.max_score]

    # Sort by score (worst first)
    results.sort(key=lambda x: (x.overall_score, x.path))

    if args.json:
        output = {
            'total_files': len(md_files),
            'analyzed_files': len(results),
            'files': [asdict(r) for r in results]
        }
        print(json.dumps(output, indent=2))
        return

    # Summary statistics
    by_source = defaultdict(list)
    by_issue = defaultdict(list)
    score_buckets = {'0-25': [], '26-50': [], '51-75': [], '76-100': []}

    for r in results:
        by_source[r.source].append(r)
        for issue in r.issues:
            by_issue[issue.split(':')[0]].append(r)

        if r.overall_score <= 25:
            score_buckets['0-25'].append(r)
        elif r.overall_score <= 50:
            score_buckets['26-50'].append(r)
        elif r.overall_score <= 75:
            score_buckets['51-75'].append(r)
        else:
            score_buckets['76-100'].append(r)

    # Print summary
    print("\n" + "=" * 60)
    print("MARKDOWN QUALITY REPORT")
    print("=" * 60)

    print(f"\nTotal files scanned: {len(md_files)}")
    print(f"Files in results: {len(results)}")

    print("\n--- Score Distribution ---")
    for bucket, files in score_buckets.items():
        pct = len(files) / len(results) * 100 if results else 0
        print(f"  {bucket}: {len(files):>6} files ({pct:>5.1f}%)")

    print("\n--- By Source ---")
    for source in ['llms-txt', 'github-scraped', 'web-scraped']:
        files = by_source.get(source, [])
        if files:
            avg_score = sum(f.overall_score for f in files) / len(files)
            low_quality = sum(1 for f in files if f.overall_score < 50)
            print(f"  {source}: {len(files)} files, avg score {avg_score:.1f}, {low_quality} low-quality")

    print("\n--- Issue Frequency ---")
    for issue, files in sorted(by_issue.items(), key=lambda x: -len(x[1])):
        print(f"  {issue}: {len(files)} files")

    if args.fix_report:
        print("\n" + "=" * 60)
        print("FIX RECOMMENDATIONS")
        print("=" * 60)

        # Binary/encoding files - need re-extraction
        if by_issue.get('encoding_issue'):
            print(f"\n### Files with encoding issues ({len(by_issue['encoding_issue'])}) - Need re-extraction:")
            for f in by_issue['encoding_issue'][:args.limit or 20]:
                print(f"  rm '{docs_root / f.path}'")

        # Empty files - just delete
        if by_issue.get('empty_file'):
            print(f"\n### Empty files ({len(by_issue['empty_file'])}) - Delete:")
            for f in by_issue['empty_file'][:args.limit or 20]:
                print(f"  rm '{docs_root / f.path}'")

        # Stub files - delete or re-extract
        if by_issue.get('stub_placeholder'):
            print(f"\n### Stub/placeholder files ({len(by_issue['stub_placeholder'])}) - Review and delete:")
            for f in by_issue['stub_placeholder'][:args.limit or 20]:
                print(f"  # {f.path}")

        # High HTML density - need HTML stripping
        if by_issue.get('high_html_density'):
            print(f"\n### High HTML density ({len(by_issue['high_html_density'])}) - Need HTML cleanup:")
            for f in by_issue['high_html_density'][:args.limit or 10]:
                print(f"  # {f.path} ({f.html_density:.2f} tags/line)")

    # Show worst files
    print("\n" + "=" * 60)
    print("WORST FILES (score < 50)")
    print("=" * 60)

    worst = [r for r in results if r.overall_score < 50]
    limit = args.limit or 50
    for r in worst[:limit]:
        issues = ', '.join(r.issues) if r.issues else 'low quality'
        print(f"  [{r.overall_score:>3}] {r.path}")
        print(f"        Issues: {issues}")

    if len(worst) > limit:
        print(f"\n  ... and {len(worst) - limit} more files with score < 50")


if __name__ == '__main__':
    main()
