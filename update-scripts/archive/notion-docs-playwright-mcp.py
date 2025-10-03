#!/usr/bin/env /Users/joe/miniconda3/bin/python
"""
Notion API Documentation Extractor using Playwright MCP
Directly uses Playwright MCP tools for better control over extraction
"""

import subprocess
import json
import time
import sys
from pathlib import Path

# Problematic files to re-extract
PROBLEMATIC_FILES = {
    # Empty files (CRITICAL)
    'revoke-token': 'https://developers.notion.com/reference/revoke-token',
    'introspect-token': 'https://developers.notion.com/reference/introspect-token',
    'list-file-uploads': 'https://developers.notion.com/reference/list-file-uploads',
    'complete-a-file-upload': 'https://developers.notion.com/reference/complete-a-file-upload',
    'retrieve-a-file-upload': 'https://developers.notion.com/reference/retrieve-a-file-upload',

    # Severely undersized critical files (HIGH PRIORITY)
    'block': 'https://developers.notion.com/reference/block',
    'page': 'https://developers.notion.com/reference/page',
    'database': 'https://developers.notion.com/reference/database',
    'create-a-data-source': 'https://developers.notion.com/reference/create-a-data-source',
    'create-a-file-upload': 'https://developers.notion.com/reference/create-a-file-upload',
    'refresh-a-token': 'https://developers.notion.com/reference/refresh-a-token',
    'get-user': 'https://developers.notion.com/reference/get-user',

    # Suspicious undersized files (MEDIUM PRIORITY)
    'database-update': 'https://developers.notion.com/reference/database-update',
    'retrieve-comment': 'https://developers.notion.com/reference/retrieve-comment',
    'get-self': 'https://developers.notion.com/reference/get-self',
}

SCRIPT_DIR = Path(__file__).parent
OUTPUT_DIR = SCRIPT_DIR.parent / "notion"

def mcp_playwright_navigate(url):
    """Navigate to a URL using Playwright MCP"""
    cmd = [
        'mcp', 'playwright', 'navigate',
        '--url', url,
        '--headless', 'false',
        '--timeout', '30000'
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.returncode == 0

def mcp_playwright_get_html(selector='article#content'):
    """Get HTML content using Playwright MCP"""
    cmd = [
        'mcp', 'playwright', 'get_visible_html',
        '--selector', selector,
        '--removeScripts', 'true',
        '--removeStyles', 'true',
        '--cleanHtml', 'true',
        '--maxLength', '500000'
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode == 0:
        return result.stdout
    return None

def mcp_playwright_close():
    """Close Playwright browser"""
    cmd = ['mcp', 'playwright', 'close']
    subprocess.run(cmd, capture_output=True)

def html_to_markdown(html_content):
    """Convert HTML to Markdown using pandoc"""
    cmd = ['pandoc', '-f', 'html', '-t', 'markdown', '--wrap=none']
    result = subprocess.run(cmd, input=html_content, capture_output=True, text=True)
    if result.returncode == 0:
        return result.stdout
    return None

def extract_page(slug, url, output_path):
    """Extract a single page"""
    print(f"  Extracting: {url}")

    # Navigate to page
    if not mcp_playwright_navigate(url):
        print(f"    ✗ Failed to navigate to {url}")
        return False, 0

    # Wait for page to load
    time.sleep(5)

    # Get HTML content
    html_content = mcp_playwright_get_html()
    if not html_content or len(html_content) < 100:
        print(f"    ✗ Failed to get HTML content (got {len(html_content) if html_content else 0} chars)")
        return False, 0

    # Convert to markdown
    markdown_content = html_to_markdown(html_content)
    if not markdown_content or len(markdown_content) < 100:
        print(f"    ✗ Failed to convert to markdown")
        return False, 0

    # Add source header
    final_content = f"# Source: {url}\n\n{markdown_content}"

    # Save to file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(final_content)

    file_size = output_path.stat().st_size
    print(f"    ✓ Saved: {output_path.name} ({file_size:,} bytes)")

    return True, file_size

def main():
    """Main extraction function"""
    print("=" * 80)
    print("Notion API Documentation Fixes Extraction (Playwright MCP)")
    print("=" * 80)
    print(f"\nRe-extracting {len(PROBLEMATIC_FILES)} problematic files")
    print(f"Output directory: {OUTPUT_DIR}")

    OUTPUT_DIR.mkdir(exist_ok=True)

    successful = 0
    failed = 0
    total_size = 0

    print("\n" + "-" * 80)

    for i, (slug, url) in enumerate(PROBLEMATIC_FILES.items(), 1):
        output_path = OUTPUT_DIR / f"{slug}.md"

        old_size = 0
        if output_path.exists():
            old_size = output_path.stat().st_size

        print(f"\n[{i}/{len(PROBLEMATIC_FILES)}] {slug}")
        if old_size > 0:
            print(f"  Previous size: {old_size:,} bytes")

        success, new_size = extract_page(slug, url, output_path)

        if success:
            successful += 1
            total_size += new_size

            if new_size > old_size:
                improvement = ((new_size - old_size) / old_size * 100) if old_size > 0 else float('inf')
                if improvement == float('inf'):
                    print(f"  ↑ New content: {new_size:,} bytes (was empty)")
                else:
                    print(f"  ↑ Improved: {new_size:,} bytes (+{improvement:.1f}%)")
        else:
            failed += 1

        time.sleep(2)

    # Close browser
    mcp_playwright_close()

    # Summary
    print("\n" + "=" * 80)
    print("Extraction Complete")
    print("=" * 80)
    print(f"Successful: {successful}/{len(PROBLEMATIC_FILES)}")
    print(f"Failed: {failed}/{len(PROBLEMATIC_FILES)}")
    print(f"Total size: {total_size:,} bytes ({total_size/1024/1024:.2f} MB)")
    if successful > 0:
        print(f"Average size: {total_size//successful:,} bytes per file")
    print("=" * 80)

    return 0 if failed == 0 else 1

if __name__ == "__main__":
    sys.exit(main())
