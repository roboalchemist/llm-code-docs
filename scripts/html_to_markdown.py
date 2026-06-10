#!/usr/bin/env python3
"""
HTML to Markdown Converter using ReaderLM-v2

This script converts HTML files to clean Markdown using the local ReaderLM-v2 service.
The service must be running (./scripts/start_readerlm.sh) before using this script.

Usage:
    # Convert a single file
    python scripts/html_to_markdown.py input.html output.md

    # Convert a file in-place (overwrite)
    python scripts/html_to_markdown.py input.md --inplace

    # Process multiple files
    python scripts/html_to_markdown.py file1.md file2.md --inplace

    # Dry run (show what would be converted)
    python scripts/html_to_markdown.py input.md --dry-run

Environment:
    READERLM_URL: Override default URL (http://localhost:10010)
"""

import argparse
import os
import sys
import requests
from pathlib import Path
from typing import Optional

try:
    from bs4 import BeautifulSoup
    HAS_BS4 = True
except ImportError:
    HAS_BS4 = False


# Default configuration
READERLM_URL = os.environ.get("READERLM_URL", "http://localhost:10010")
MAX_CHUNK_SIZE = 24000  # Characters per chunk (stay under token limits)
MODEL = "jinaai/ReaderLM-v2"


def check_service() -> bool:
    """Check if ReaderLM service is running."""
    try:
        response = requests.get(f"{READERLM_URL}/health", timeout=5)
        return response.status_code == 200
    except requests.RequestException:
        return False


def is_html_content(content: str) -> bool:
    """Check if content appears to be HTML (not already clean markdown)."""
    # Check for HTML document indicators
    if content.strip().startswith("<!DOCTYPE html") or content.strip().startswith("<html"):
        return True

    # Check for significant HTML tag density
    import re
    html_tags = re.findall(r'<[a-z][^>]*>', content[:5000], re.IGNORECASE)
    total_chars = min(len(content), 5000)
    if total_chars > 0 and len(html_tags) > total_chars / 100:  # More than 1 tag per 100 chars
        return True

    # Check for JSX/MDX patterns
    if '{{' in content and '}}' in content:  # JSX style syntax
        return True

    return False


def clean_html(html: str) -> str:
    """Pre-process HTML to reduce noise."""
    if not HAS_BS4:
        return html

    soup = BeautifulSoup(html, 'html.parser')

    # Remove non-content elements
    for tag in soup(['script', 'style', 'meta', 'link', 'noscript', 'svg']):
        tag.decompose()

    # Try to find main content area
    main = soup.find('main') or soup.find('article') or soup.find('.content') or soup.find('#content')
    if main:
        return str(main)

    # Otherwise return body or full content
    body = soup.find('body')
    if body:
        return str(body)

    return str(soup)


def convert_chunk(html: str) -> str:
    """Convert a single chunk of HTML to Markdown."""
    prompt = f"""Extract the main content from the given HTML and convert it to Markdown format.
```html
{html}
```"""

    try:
        response = requests.post(
            f"{READERLM_URL}/v1/chat/completions",
            json={
                "model": MODEL,
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0,
                "max_tokens": 8192,
                "repetition_penalty": 1.08
            },
            timeout=120
        )
        response.raise_for_status()
        result = response.json()

        if "choices" in result:
            content = result["choices"][0]["message"]["content"]
            # Strip markdown code block wrapper if present
            if content.startswith("```markdown"):
                content = content[11:]
            if content.startswith("```"):
                content = content[3:]
            if content.endswith("```"):
                content = content[:-3]
            return content.strip()
        else:
            raise ValueError(f"Unexpected response format: {result}")

    except requests.RequestException as e:
        raise RuntimeError(f"API request failed: {e}")


def convert_html_to_markdown(html: str) -> str:
    """Convert HTML to Markdown, handling large files with chunking."""
    # Pre-process HTML
    if HAS_BS4:
        html = clean_html(html)

    # If content is small enough, process in one go
    if len(html) <= MAX_CHUNK_SIZE:
        return convert_chunk(html)

    # For large files, we need to chunk
    # This is a simple approach - for better results, consider semantic chunking
    chunks = []
    for i in range(0, len(html), MAX_CHUNK_SIZE):
        chunk = html[i:i + MAX_CHUNK_SIZE]
        chunks.append(chunk)

    # Convert each chunk
    results = []
    for i, chunk in enumerate(chunks):
        print(f"  Processing chunk {i+1}/{len(chunks)}...", file=sys.stderr)
        try:
            result = convert_chunk(chunk)
            results.append(result)
        except Exception as e:
            print(f"  Warning: Chunk {i+1} failed: {e}", file=sys.stderr)
            results.append(f"<!-- Conversion failed for chunk {i+1} -->\n{chunk}")

    return "\n\n".join(results)


def convert_file(input_path: Path, output_path: Optional[Path] = None, dry_run: bool = False) -> bool:
    """Convert a single file."""
    print(f"Processing: {input_path}", file=sys.stderr)

    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"  Error reading file: {e}", file=sys.stderr)
        return False

    # Check if content needs conversion
    if not is_html_content(content):
        print(f"  Skipping: Does not appear to contain HTML", file=sys.stderr)
        return False

    if dry_run:
        print(f"  Would convert: {len(content)} chars", file=sys.stderr)
        return True

    # Convert
    try:
        markdown = convert_html_to_markdown(content)
    except Exception as e:
        print(f"  Conversion error: {e}", file=sys.stderr)
        return False

    # Write output
    out_path = output_path or input_path
    try:
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(markdown)
        print(f"  Saved: {out_path} ({len(markdown)} chars)", file=sys.stderr)
        return True
    except Exception as e:
        print(f"  Error writing file: {e}", file=sys.stderr)
        return False


def main():
    parser = argparse.ArgumentParser(
        description="Convert HTML to Markdown using ReaderLM-v2",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument("files", nargs="+", help="Input file(s)")
    parser.add_argument("-o", "--output", help="Output file (only for single file)")
    parser.add_argument("--inplace", action="store_true", help="Modify files in place")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be converted")
    args = parser.parse_args()

    # Check service
    if not args.dry_run and not check_service():
        print(f"Error: ReaderLM service not running at {READERLM_URL}", file=sys.stderr)
        print("Start it with: ./scripts/start_readerlm.sh", file=sys.stderr)
        sys.exit(1)

    # Validate arguments
    if args.output and len(args.files) > 1:
        print("Error: --output can only be used with a single input file", file=sys.stderr)
        sys.exit(1)

    if len(args.files) > 1 and not args.inplace and not args.dry_run:
        print("Error: Use --inplace or --dry-run for multiple files", file=sys.stderr)
        sys.exit(1)

    # Process files
    success = 0
    failed = 0
    skipped = 0

    for file_path in args.files:
        path = Path(file_path)
        if not path.exists():
            print(f"Error: File not found: {path}", file=sys.stderr)
            failed += 1
            continue

        if args.output:
            output = Path(args.output)
        elif args.inplace:
            output = path
        else:
            output = path.with_suffix('.converted.md')

        result = convert_file(path, output, dry_run=args.dry_run)
        if result:
            success += 1
        elif result is False:
            failed += 1
        else:
            skipped += 1

    print(f"\nSummary: {success} converted, {skipped} skipped, {failed} failed", file=sys.stderr)
    sys.exit(0 if failed == 0 else 1)


if __name__ == "__main__":
    main()
