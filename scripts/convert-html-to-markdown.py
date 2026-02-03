#!/usr/bin/env python3
"""
Convert HTML files to Markdown using ReaderLM-v2

Uses ReaderLM-v2 for HTML-to-markdown conversion. Tries vLLM server first,
falls back to local MLX if server is unavailable.

Usage:
    python3 scripts/convert-html-to-markdown.py                    # Process all HTML files
    python3 scripts/convert-html-to-markdown.py --site langchain   # Process single site
    python3 scripts/convert-html-to-markdown.py --dry-run          # Show what would be converted
    python3 scripts/convert-html-to-markdown.py --local            # Force local MLX
    python3 scripts/convert-html-to-markdown.py --workers 8        # Set concurrent workers (vLLM)
"""

import argparse
import re
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import requests


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


VLLM_SERVER = "http://chungus2:8000"


def check_vllm_server() -> bool:
    """Check if vLLM server is available."""
    try:
        resp = requests.get(f"{VLLM_SERVER}/v1/models", timeout=5)
        return resp.status_code == 200
    except:
        return False


def convert_html_to_markdown_vllm(html: str) -> str:
    """Convert HTML to markdown using vLLM server."""
    instruction = "Extract the main content from the given HTML and transform it to Markdown format."
    prompt_content = f"{instruction}\n```html\n{html}\n```"

    response = requests.post(
        f"{VLLM_SERVER}/v1/chat/completions",
        json={
            "model": "jinaai/ReaderLM-v2",
            "messages": [{"role": "user", "content": prompt_content}],
            "max_tokens": 8192,
            "temperature": 0.0,
        },
        timeout=300,
    )
    response.raise_for_status()
    result = response.json()["choices"][0]["message"]["content"].strip()

    # Clean up the response - strip markdown code fences if present
    if result.startswith('```markdown'):
        result = result[len('```markdown'):].strip()
    if result.startswith('```'):
        result = result[3:].strip()
    if result.endswith('```'):
        result = result[:-3].strip()

    return result


def convert_html_to_markdown_mlx(html: str, model, tokenizer) -> str:
    """Convert HTML to markdown using local MLX."""
    from mlx_lm import generate

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
    parser.add_argument('--local', action='store_true', help='Force local MLX (skip vLLM server)')
    parser.add_argument('--workers', type=int, default=8,
                        help='Number of concurrent workers for vLLM (default: 8, optimal for dual 3090s)')
    parser.add_argument('--max-size', type=int, default=100,
                        help='Skip files larger than this size in KB (default: 100KB)')
    parser.add_argument('--model-path', default='roboalchemist/ReaderLM-v2-mlx-fp16',
                        help='HuggingFace model path for MLX fallback')
    args = parser.parse_args()

    # Determine docs root relative to this script
    script_dir = Path(__file__).resolve().parent
    docs_root = script_dir.parent / 'docs'

    print("Scanning for HTML files...", file=sys.stderr)
    html_files = find_html_files(docs_root, args.site)

    if not html_files:
        print("No HTML files found.")
        return

    # Filter by size
    max_bytes = args.max_size * 1024
    original_count = len(html_files)
    html_files = [f for f in html_files if f.stat().st_size <= max_bytes]
    skipped = original_count - len(html_files)
    if skipped > 0:
        print(f"Skipping {skipped} files larger than {args.max_size}KB", file=sys.stderr)

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

    # Check for vLLM server first (unless --local)
    use_vllm = False
    model, tokenizer = None, None

    if not args.local:
        print(f"\nChecking vLLM server at {VLLM_SERVER}...", file=sys.stderr)
        if check_vllm_server():
            print("✓ vLLM server available, using remote GPU", file=sys.stderr)
            use_vllm = True
        else:
            print("✗ vLLM server unavailable, falling back to local MLX", file=sys.stderr)

    if not use_vllm:
        print(f"\nLoading ReaderLM-v2 from {args.model_path}...", file=sys.stderr)
        from mlx_lm import load
        model, tokenizer = load(args.model_path)
        print("Model loaded.", file=sys.stderr)

    # Process files
    converted = 0
    failed = 0

    def process_file(html_file: Path) -> tuple[Path, bool, str]:
        """Process a single HTML file. Returns (path, success, message)."""
        try:
            html_content = html_file.read_text(encoding='utf-8', errors='replace')

            if use_vllm:
                markdown = convert_html_to_markdown_vllm(html_content)
            else:
                markdown = convert_html_to_markdown_mlx(html_content, model, tokenizer)

            if markdown and len(markdown) > 100:
                # Add title if model didn't generate one
                if not markdown.startswith('#'):
                    # Try to extract title from HTML
                    title_match = re.search(r'<title>([^<]+)</title>', html_content, re.IGNORECASE)
                    title = title_match.group(1) if title_match else html_file.stem
                    # Clean title (remove " | Site Name" suffixes)
                    title = re.sub(r'\s*\|.*$', '', title).strip()
                    markdown = f"# {title}\n\n{markdown}"

                html_file.write_text(markdown, encoding='utf-8')
                return (html_file, True, f"Converted ({len(markdown)} chars)")
            else:
                return (html_file, False, "Empty/short output, skipping")

        except Exception as e:
            return (html_file, False, f"Error: {e}")

    # Use concurrent processing for vLLM, sequential for MLX
    if use_vllm and args.workers > 1:
        print(f"\nProcessing {len(html_files)} files with {args.workers} concurrent workers...", file=sys.stderr)
        with ThreadPoolExecutor(max_workers=args.workers) as executor:
            futures = {executor.submit(process_file, f): f for f in html_files}
            for i, future in enumerate(as_completed(futures), 1):
                html_file, success, message = future.result()
                rel_path = html_file.relative_to(docs_root)
                status = "✓" if success else "✗"
                print(f"[{i}/{len(html_files)}] {status} {rel_path}: {message}", file=sys.stderr)
                if success:
                    converted += 1
                else:
                    failed += 1
    else:
        # Sequential processing (MLX or single worker)
        for i, html_file in enumerate(html_files, 1):
            rel_path = html_file.relative_to(docs_root)
            print(f"\n[{i}/{len(html_files)}] Converting: {rel_path}", file=sys.stderr)
            _, success, message = process_file(html_file)
            print(f"  {'✓' if success else '✗'} {message}", file=sys.stderr)
            if success:
                converted += 1
            else:
                failed += 1

    print(f"\n{'='*60}", file=sys.stderr)
    print(f"Conversion complete: {converted} converted, {failed} failed", file=sys.stderr)


if __name__ == '__main__':
    main()
