#!/usr/bin/env python3
"""
Convert HTML files to Markdown using ReaderLM-v2 (MLX)

Uses the full-precision ReaderLM-v2 model for highest quality HTML-to-markdown conversion.
Scans docs/llms-txt for files containing HTML and converts them in place.

Usage:
    python3 scripts/convert-html-to-markdown.py                    # Process all HTML files
    python3 scripts/convert-html-to-markdown.py --site langchain   # Process single site
    python3 scripts/convert-html-to-markdown.py --dry-run          # Show what would be converted
"""

import argparse
import os
import re
import sys
from pathlib import Path


def is_html_content(content: str) -> bool:
    """Check if content is HTML rather than markdown."""
    content_lower = content.strip().lower()[:2000]

    # Check for HTML markers
    if content_lower.startswith('<!doctype html') or content_lower.startswith('<html'):
        return True
    if '<head>' in content_lower and '<body>' in content_lower:
        return True
    if re.search(r'<html[^>]*>', content_lower):
        return True

    return False


def convert_html_to_markdown(html: str, model, tokenizer) -> str:
    """Convert HTML to markdown using ReaderLM-v2 with proper chat template."""
    from mlx_lm import generate

    # Use the correct ReaderLM-v2 prompt format with chat template
    instruction = "Extract the main content from the given HTML and transform it to Markdown format."
    prompt_content = f"{instruction}\n```html\n{html}\n```"

    messages = [{"role": "user", "content": prompt_content}]
    prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)

    response = generate(
        model,
        tokenizer,
        prompt=prompt,
        max_tokens=8192,
        verbose=False,
    )

    # Clean up the response - strip markdown code fences if present
    result = response.strip()
    if result.startswith('```markdown'):
        result = result[len('```markdown'):].strip()
    if result.startswith('```'):
        result = result[3:].strip()
    if result.endswith('```'):
        result = result[:-3].strip()

    return result


def find_html_files(docs_root: Path, site: str = None) -> list[Path]:
    """Find all .md files that contain HTML instead of markdown."""
    html_files = []

    if site:
        search_path = docs_root / 'llms-txt' / site
        if not search_path.exists():
            print(f"Site not found: {site}", file=sys.stderr)
            return []
    else:
        search_path = docs_root / 'llms-txt'

    for md_file in search_path.rglob('*.md'):
        try:
            content = md_file.read_text(encoding='utf-8', errors='replace')
            if is_html_content(content):
                html_files.append(md_file)
        except Exception as e:
            print(f"Error reading {md_file}: {e}", file=sys.stderr)

    return html_files


def main():
    parser = argparse.ArgumentParser(description='Convert HTML files to Markdown using ReaderLM-v2')
    parser.add_argument('--site', help='Process only this site')
    parser.add_argument('--dry-run', action='store_true', help='Show files without converting')
    parser.add_argument('--model-path', default='roboalchemist/ReaderLM-v2-mlx-fp16',
                        help='HuggingFace model path (default: roboalchemist/ReaderLM-v2-mlx-fp16)')
    args = parser.parse_args()

    docs_root = Path('/Users/joe/github/llm-code-docs/docs')

    print("Scanning for HTML files...", file=sys.stderr)
    html_files = find_html_files(docs_root, args.site)

    if not html_files:
        print("No HTML files found.")
        return

    # Group by site
    by_site = {}
    for f in html_files:
        site = f.relative_to(docs_root / 'llms-txt').parts[0]
        by_site.setdefault(site, []).append(f)

    print(f"\nFound {len(html_files)} HTML files across {len(by_site)} sites:")
    for site, files in sorted(by_site.items()):
        print(f"  {site}: {len(files)} files")

    if args.dry_run:
        print("\n--dry-run: No changes made")
        return

    # Load model
    print(f"\nLoading ReaderLM-v2 from {args.model_path}...", file=sys.stderr)
    from mlx_lm import load
    model, tokenizer = load(args.model_path)
    print("Model loaded.", file=sys.stderr)

    # Process files
    converted = 0
    failed = 0

    for i, html_file in enumerate(html_files, 1):
        rel_path = html_file.relative_to(docs_root)
        print(f"\n[{i}/{len(html_files)}] Converting: {rel_path}", file=sys.stderr)

        try:
            html_content = html_file.read_text(encoding='utf-8', errors='replace')
            markdown = convert_html_to_markdown(html_content, model, tokenizer)

            if markdown and len(markdown) > 100:
                # Add title if model didn't generate one
                if not markdown.startswith('#'):
                    # Try to extract title from HTML
                    title_match = re.search(r'<title>([^<]+)</title>', html_content, re.IGNORECASE)
                    title = title_match.group(1) if title_match else rel_path.stem
                    # Clean title (remove " | Site Name" suffixes)
                    title = re.sub(r'\s*\|.*$', '', title).strip()
                    markdown = f"# {title}\n\n{markdown}"

                html_file.write_text(markdown, encoding='utf-8')
                converted += 1
                print(f"  ✓ Converted ({len(markdown)} chars)", file=sys.stderr)
            else:
                print(f"  ✗ Empty/short output, skipping", file=sys.stderr)
                failed += 1

        except Exception as e:
            print(f"  ✗ Error: {e}", file=sys.stderr)
            failed += 1

    print(f"\n{'='*60}", file=sys.stderr)
    print(f"Conversion complete: {converted} converted, {failed} failed", file=sys.stderr)


if __name__ == '__main__':
    main()
