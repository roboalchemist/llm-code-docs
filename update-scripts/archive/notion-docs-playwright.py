#!/usr/bin/env python3
"""
Notion API Documentation Downloader - Playwright Version
Extracts JavaScript-rendered pages that require browser automation.

This script complements notion-docs.py by extracting pages that require
JavaScript rendering to display their content properly.
"""

import os
import sys
import json
import subprocess
import re
import time
from pathlib import Path
from urllib.parse import urlparse

# List of JavaScript-rendered pages that require Playwright extraction
JS_RENDERED_PAGES = [
    "https://developers.notion.com/reference/revoke-token",
    "https://developers.notion.com/reference/introspect-token",
    "https://developers.notion.com/reference/list-file-uploads",
    "https://developers.notion.com/reference/complete-a-file-upload",
    "https://developers.notion.com/reference/retrieve-a-file-upload",
    "https://developers.notion.com/reference/refresh-a-token",
    "https://developers.notion.com/reference/create-a-data-source",
    "https://developers.notion.com/reference/create-a-file-upload",
]

try:
    from bs4 import BeautifulSoup
    HAS_BS4 = True
except ImportError:
    HAS_BS4 = False
    print("Warning: BeautifulSoup not available. Install with: pip install beautifulsoup4")

def extract_main_content(html_content):
    """Extract only the main documentation content from HTML.

    This function is identical to the one in notion-docs.py to ensure
    consistent output formatting.
    """
    if HAS_BS4:
        # Use BeautifulSoup for precise content extraction
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find the article with id="content" - this is the main content container
        article = soup.find('article', {'class': 'rm-Article', 'id': 'content'})

        if article:
            # First, preserve content from content-head headers by unwrapping them
            # (keep their content but remove the header tag wrapper)
            for header in article.find_all('header', {'id': 'content-head'}):
                header.unwrap()

            # Remove all script and style tags
            for tag in article.find_all(['script', 'style', 'nav', 'aside', 'header', 'footer', 'button']):
                tag.decompose()

            # Remove elements with specific classes that are UI elements
            for tag in article.find_all(class_=lambda x: x and any(
                cls in str(x) for cls in [
                    'CodeTabs-toolbar',
                    'heading-anchor-icon',
                    'callout-icon',
                    'heading-anchor',
                    'anchor',
                    'waypoint',
                    'headline-container'
                ]
            )):
                tag.decompose()

            # Remove elements with specific data-testid attributes
            for tag in article.find_all(attrs={'data-testid': True}):
                # For RDMD div, unwrap it (keep content, remove tag)
                if tag.get('data-testid') == 'RDMD' and tag.name == 'div':
                    tag.unwrap()
                else:
                    tag.decompose()

            # Unwrap heading-text divs (keep content, remove wrapper)
            for tag in article.find_all('div', class_=lambda x: x and 'heading-text' in str(x)):
                tag.unwrap()

            # Remove all class and style attributes to clean the HTML
            for tag in article.find_all(True):
                # Keep only essential attributes
                allowed_attrs = ['href', 'src', 'alt', 'title', 'name', 'id']
                tag.attrs = {k: v for k, v in tag.attrs.items() if k in allowed_attrs}

            # Also clean the article tag itself
            article.attrs = {}

            # Get the cleaned HTML (return just the innerHTML, not the article tag)
            return article.decode_contents()

        # Fallback: try to find content-body div if article not found
        content_div = soup.find('div', class_=lambda x: x and 'content-body' in x)
        if content_div:
            for tag in content_div.find_all(['script', 'style', 'nav', 'aside']):
                tag.decompose()
            for tag in content_div.find_all(True):
                tag.attrs = {k: v for k, v in tag.attrs.items() if k not in ['class', 'style', 'data-lang', 'tabindex', 'role']}
            return str(content_div)

    # Fallback to regex-based extraction if BeautifulSoup not available
    # Look for the article tag with id="content"
    article_match = re.search(r'<article[^>]*id="content"[^>]*>(.*?)</article>', html_content, re.DOTALL | re.IGNORECASE)
    if article_match:
        content = article_match.group(1)
    else:
        # Try other patterns including section with id="hub-content" for API endpoints
        patterns = [
            r'<article[^>]*class="[^"]*rm-Article[^"]*"[^>]*>(.*?)</article>',
            r'<section[^>]*id="hub-content"[^>]*>(.*?)</section>',
            r'<div[^>]*class="[^"]*content-body[^"]*"[^>]*>(.*?)</div>',
            r'<main[^>]*>(.*?)</main>',
        ]

        content = None
        for pattern in patterns:
            match = re.search(pattern, html_content, re.DOTALL | re.IGNORECASE)
            if match:
                content = match.group(1)
                break

        if not content:
            return html_content

    # First preserve content-head headers by extracting their inner HTML
    # and replacing the whole header tag with just the inner content
    content = re.sub(
        r'<header[^>]*id=["\']content-head["\'][^>]*>(.*?)</header>',
        r'\1',
        content,
        flags=re.DOTALL | re.IGNORECASE
    )

    # Remove unwanted elements
    content = re.sub(r'<script[^>]*>.*?</script>', '', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<style[^>]*>.*?</style>', '', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<nav[^>]*>.*?</nav>', '', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<aside[^>]*>.*?</aside>', '', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<header[^>]*>.*?</header>', '', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<footer[^>]*>.*?</footer>', '', content, flags=re.DOTALL | re.IGNORECASE)

    return content

def clean_markdown(markdown):
    """Clean up markdown content to remove artifacts and improve readability.

    This function is identical to the one in notion-docs.py to ensure
    consistent output formatting.
    """
    # Remove CSS class annotations like {.rdmd-code .lang- .theme-light}
    markdown = re.sub(r'\{\.[\w\-\s_]+\}', '', markdown)

    # Remove attribute annotations like {#section-id}
    markdown = re.sub(r'\{#[\w\-]+\}', '', markdown)

    # Remove standalone attribute blocks like {target="_self"}
    markdown = re.sub(r'\{[^}]*="[^"]*"\}', '', markdown)

    # Remove excessive colons used for div containers (::::::::::::)
    markdown = re.sub(r'^:{3,}.*$', '', markdown, flags=re.MULTILINE)

    # Remove fenced divs like ::: and ::::
    markdown = re.sub(r'^::+\s*$', '', markdown, flags=re.MULTILINE)
    markdown = re.sub(r'^::+\s+\{[^}]+\}.*$', '', markdown, flags=re.MULTILINE)

    # Remove HTML comment markers
    markdown = re.sub(r'<!--.*?-->', '', markdown, flags=re.DOTALL)

    # Convert remaining HTML links to markdown (multiple patterns to catch all)
    # Match <a href="url" >text</a> (with attributes and spaces)
    markdown = re.sub(r'<a\s+[^>]*href="([^"]+)"[^>]*>([^<]+)</a>', r'[\2](\1)', markdown)

    # Convert inline code tags to markdown
    markdown = re.sub(r'<code[^>]*>([^<]+)</code>', r'`\1`', markdown)

    # Convert <br> and <br /> tags to markdown line breaks
    markdown = re.sub(r'<br\s*/?>','\n', markdown)

    # Remove table-related HTML tags (they're often malformed from extraction)
    markdown = re.sub(r'</?table[^>]*>', '', markdown)
    markdown = re.sub(r'</?thead[^>]*>', '', markdown)
    markdown = re.sub(r'</?tbody[^>]*>', '', markdown)
    markdown = re.sub(r'</?tr[^>]*>', '\n', markdown)  # Convert table rows to newlines
    markdown = re.sub(r'</?th[^>]*>', ' | ', markdown)  # Convert table headers to pipe separators
    markdown = re.sub(r'</?td[^>]*>', ' | ', markdown)  # Convert table data to pipe separators
    markdown = re.sub(r'<col[^>]*/?>', '', markdown)

    # Remove remaining HTML tags (opening and closing)
    # Be careful to preserve code blocks marked with backticks
    markdown = re.sub(r'</?div[^>]*>', '', markdown)
    markdown = re.sub(r'</?span[^>]*>', '', markdown)
    markdown = re.sub(r'</?section[^>]*>', '', markdown)
    markdown = re.sub(r'</?article[^>]*>', '', markdown)
    markdown = re.sub(r'</?header[^>]*>', '', markdown)
    markdown = re.sub(r'</?footer[^>]*>', '', markdown)
    markdown = re.sub(r'</?nav[^>]*>', '', markdown)
    markdown = re.sub(r'</?aside[^>]*>', '', markdown)

    # Remove excessive blank lines (more than 2 consecutive)
    markdown = re.sub(r'\n{3,}', '\n\n', markdown)

    # Remove lines that are just whitespace
    lines = [line.rstrip() for line in markdown.split('\n')]
    markdown = '\n'.join(lines)

    # Remove specific UI element artifacts
    ui_artifacts = [
        'CodeTabs-toolbar',
        'CodeTabs-inner',
        'CodeTabs_initial',
        'heading-anchor',
        'heading-anchor-icon',
        'callout-icon',
        'callout-heading',
        'Article-wrapper',
        'Article-container',
        'markdown-body',
        'content-body',
        'heading-text',
        'rdmd-table',
        'rdmd-table-inner',
        'Flex',
        'Flex_row',
    ]

    for artifact in ui_artifacts:
        markdown = re.sub(rf'.*{re.escape(artifact)}.*\n?', '', markdown)

    # Clean up role and aria attributes in text
    markdown = re.sub(r'role="[^"]*"', '', markdown)
    markdown = re.sub(r'aria-label="[^"]*"', '', markdown)
    markdown = re.sub(r'testid="[^"]*"', '', markdown)
    markdown = re.sub(r'tabindex="?\d+"?', '', markdown)
    markdown = re.sub(r'data-lang="[^"]*"', '', markdown)
    markdown = re.sub(r'target="_self"', '', markdown)
    markdown = re.sub(r'align="[^"]*"', '', markdown)
    markdown = re.sub(r'justify="[^"]*"', '', markdown)
    markdown = re.sub(r'style="[^"]*"', '', markdown)

    # Remove empty markdown headings (just # symbols with no text)
    markdown = re.sub(r'^#{1,6}\s*$', '', markdown, flags=re.MULTILINE)

    # Remove lines that are just closing tags or empty
    lines = []
    for line in markdown.split('\n'):
        stripped = line.strip()
        # Skip empty lines, lone closing tags, and artifact lines
        if stripped and not re.match(r'^</?\w+>$', stripped):
            lines.append(line)

    markdown = '\n'.join(lines)

    # Clean up excessive whitespace again after all removals
    markdown = re.sub(r'\n{3,}', '\n\n', markdown)
    markdown = markdown.strip()

    return markdown

def html_to_markdown(html_content, url):
    """Convert HTML content to Markdown using pandoc or basic conversion.

    This function is identical to the one in notion-docs.py to ensure
    consistent output formatting.
    """
    # First extract the main content
    content = extract_main_content(html_content)

    try:
        # Try using pandoc if available with options for cleaner output
        result = subprocess.run(
            [
                'pandoc',
                '-f', 'html',
                '-t', 'gfm',  # GitHub Flavored Markdown for better formatting
                '--wrap=none',
                '--strip-comments',  # Remove HTML comments
            ],
            input=content,
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            markdown = result.stdout

            # Post-process to clean up remaining artifacts
            markdown = clean_markdown(markdown)

            # Add source URL as header
            header = f"# Source: {url}\n\n"
            return header + markdown
    except (subprocess.TimeoutExpired, FileNotFoundError):
        pass

    # Fallback: basic HTML to Markdown conversion
    # This is a simple conversion - not perfect but functional
    content = content

    # Remove script and style tags
    content = re.sub(r'<script[^>]*>.*?</script>', '', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<style[^>]*>.*?</style>', '', content, flags=re.DOTALL | re.IGNORECASE)

    # Convert headers
    for i in range(6, 0, -1):
        content = re.sub(f'<h{i}[^>]*>(.*?)</h{i}>', f"{'#' * i} \\1\n", content, flags=re.DOTALL | re.IGNORECASE)

    # Convert links
    content = re.sub(r'<a[^>]*href=["\']([^"\']*)["\'][^>]*>(.*?)</a>', r'[\2](\1)', content, flags=re.DOTALL | re.IGNORECASE)

    # Convert bold and italic
    content = re.sub(r'<strong[^>]*>(.*?)</strong>', r'**\1**', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<b[^>]*>(.*?)</b>', r'**\1**', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<em[^>]*>(.*?)</em>', r'*\1*', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<i[^>]*>(.*?)</i>', r'*\1*', content, flags=re.DOTALL | re.IGNORECASE)

    # Convert code blocks
    content = re.sub(r'<pre[^>]*><code[^>]*>(.*?)</code></pre>', r'```\n\1\n```', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<code[^>]*>(.*?)</code>', r'`\1`', content, flags=re.DOTALL | re.IGNORECASE)

    # Convert lists
    content = re.sub(r'<li[^>]*>(.*?)</li>', r'- \1', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<ul[^>]*>|</ul>|<ol[^>]*>|</ol>', '', content, flags=re.IGNORECASE)

    # Convert paragraphs
    content = re.sub(r'<p[^>]*>(.*?)</p>', r'\1\n\n', content, flags=re.DOTALL | re.IGNORECASE)

    # Remove remaining HTML tags
    content = re.sub(r'<[^>]+>', '', content)

    # Decode HTML entities
    content = content.replace('&nbsp;', ' ')
    content = content.replace('&lt;', '<')
    content = content.replace('&gt;', '>')
    content = content.replace('&amp;', '&')
    content = content.replace('&quot;', '"')
    content = content.replace('&#39;', "'")

    # Clean up excessive whitespace
    content = re.sub(r'\n{3,}', '\n\n', content)
    content = content.strip()

    # Apply markdown cleaning
    content = clean_markdown(content)

    # Add source URL as header
    header = f"# Source: {url}\n\n"

    return header + content

def extract_file_path(url):
    """Extract the file path from the URL to preserve directory structure."""
    parsed = urlparse(url)
    # Remove the leading /reference/ part to get the relative path
    path = parsed.path
    if path.startswith('/reference/'):
        relative_path = path[len('/reference/'):]
        # If it's the root, use intro.md
        if not relative_path or relative_path == '/':
            return 'intro.md'
        return relative_path + '.md'
    else:
        # Fallback to just the filename
        return Path(path).name + '.md'

def extract_with_playwright_mcp(url, output_path, playwright_funcs):
    """Extract content using Playwright MCP for JavaScript-rendered pages.

    Args:
        url: The URL to extract
        output_path: Path to save the markdown file
        playwright_funcs: Dictionary of Playwright MCP functions

    Returns:
        True if successful
        False if failed
    """
    try:
        print(f"  Navigating to {url}...")

        # Navigate to the page
        navigate = playwright_funcs['navigate']
        navigate(url=url, headless=True, timeout=30000)

        # Wait a bit for JavaScript to render
        time.sleep(2)

        # Get the rendered HTML
        get_html = playwright_funcs['get_html']
        html_content = get_html(removeScripts=True, cleanHtml=False)

        if not html_content or len(html_content) < 100:
            print(f"  Warning: Retrieved HTML is too short ({len(html_content) if html_content else 0} bytes)")
            return False

        print(f"  Retrieved {len(html_content)} bytes of HTML")

        # Convert HTML to Markdown using the same logic as the main script
        markdown_content = html_to_markdown(html_content, url)

        # Check if we got meaningful content
        if len(markdown_content) < 100:
            print(f"  Warning: Converted markdown is too short ({len(markdown_content)} bytes)")
            return False

        # Create directory if it doesn't exist
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # Write the markdown content to file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(markdown_content)

        file_size = output_path.stat().st_size
        print(f"  Saved {file_size} bytes to {output_path.name}")

        return True

    except Exception as e:
        print(f"  Error extracting {url}: {e}")
        import traceback
        traceback.print_exc()
        return False

def get_files_to_extract():
    """Get the list of files that need extraction.

    Returns:
        List of tuples (url, output_path, status)
    """
    output_dir = Path(__file__).parent.parent / "notion"
    files_to_extract = []

    for url in JS_RENDERED_PAGES:
        relative_path = extract_file_path(url)
        output_path = output_dir / relative_path

        if output_path.exists():
            file_size = output_path.stat().st_size
            if file_size > 500:
                status = "existing_good"
            else:
                status = "incomplete"
                files_to_extract.append((url, output_path, status))
        else:
            status = "missing"
            files_to_extract.append((url, output_path, status))

    return files_to_extract

def run_extraction(playwright_funcs):
    """Run the extraction using Playwright MCP tools.

    Args:
        playwright_funcs: Dictionary with 'navigate' and 'get_html' functions

    Returns:
        Dictionary with extraction statistics
    """
    print("=" * 70)
    print("Notion API Documentation - Playwright Extraction")
    print("=" * 70)
    print()

    output_dir = Path(__file__).parent.parent / "notion"
    files_to_extract = get_files_to_extract()

    print(f"Output directory: {output_dir}")
    print(f"Files to extract: {len(files_to_extract)}")
    print()

    if not files_to_extract:
        print("All JavaScript-rendered pages already extracted!")
        return {"success": 0, "failed": 0, "skipped": len(JS_RENDERED_PAGES)}

    # Extract each file
    successful = 0
    failed = 0

    for i, (url, output_path, status) in enumerate(files_to_extract, 1):
        rel_path = output_path.relative_to(output_dir)
        print(f"[{i}/{len(files_to_extract)}] {rel_path} ({status.upper()})")

        result = extract_with_playwright_mcp(url, output_path, playwright_funcs)

        if result:
            successful += 1
            print(f"  SUCCESS")
        else:
            failed += 1
            print(f"  FAILED")

        print()

        # Small delay between requests
        if i < len(files_to_extract):
            time.sleep(1)

    # Print summary
    print("=" * 70)
    print("Extraction Summary")
    print("=" * 70)
    print(f"Successful: {successful}")
    print(f"Failed:     {failed}")
    print(f"Total:      {len(files_to_extract)}")
    print()

    return {
        "success": successful,
        "failed": failed,
        "total": len(files_to_extract)
    }

def main():
    """Main function to extract JavaScript-rendered Notion API documentation."""

    print("=" * 70)
    print("Notion API Documentation - Playwright Extraction")
    print("=" * 70)
    print("Extracts JavaScript-rendered pages using browser automation")
    print()

    # Output directory (same as main script)
    output_dir = Path(__file__).parent.parent / "notion"

    print(f"Output directory: {output_dir}")
    print(f"Pages to extract: {len(JS_RENDERED_PAGES)}")
    print()

    # Check which files need extraction
    files_to_extract = []
    existing_good = []
    existing_incomplete = []
    missing = []

    for url in JS_RENDERED_PAGES:
        relative_path = extract_file_path(url)
        output_path = output_dir / relative_path

        if output_path.exists():
            file_size = output_path.stat().st_size
            if file_size > 500:  # Consider files > 500 bytes as potentially good
                existing_good.append((url, output_path, file_size))
            else:
                existing_incomplete.append((url, output_path, file_size))
                files_to_extract.append((url, output_path))
        else:
            missing.append((url, output_path))
            files_to_extract.append((url, output_path))

    # Print status
    print("File Status:")
    print(f"  Existing (good):       {len(existing_good)}")
    print(f"  Existing (incomplete): {len(existing_incomplete)}")
    print(f"  Missing:               {len(missing)}")
    print(f"  Total to extract:      {len(files_to_extract)}")
    print()

    if existing_good:
        print("Existing files with good content:")
        for url, path, size in existing_good:
            rel_path = path.relative_to(output_dir)
            print(f"  {rel_path} ({size} bytes)")
        print()

    if not files_to_extract:
        print("All JavaScript-rendered pages already extracted!")
        return 0

    # Show what needs to be extracted
    print("Files that need extraction:")
    for url, path in files_to_extract:
        rel_path = path.relative_to(output_dir)
        status = "MISSING" if path not in [p for _, p, _ in existing_incomplete] else "INCOMPLETE"
        print(f"  [{status}] {rel_path}")
        print(f"           {url}")
    print()

    # Note about MCP requirement
    print("=" * 70)
    print("IMPORTANT: This script requires Playwright MCP tools")
    print("=" * 70)
    print()
    print("This script has been designed to work with Claude Code's Playwright MCP.")
    print("To extract the pages, you need to run this script through Claude Code,")
    print("which will use the MCP tools to:")
    print()
    print("  1. Navigate to each URL with a headless browser")
    print("  2. Wait for JavaScript to render the content")
    print("  3. Extract the rendered HTML from article#content")
    print("  4. Convert to markdown using the same logic as notion-docs.py")
    print("  5. Save to the notion/ directory")
    print()
    print("=" * 70)
    print()

    # If BeautifulSoup is not available, warn about it
    if not HAS_BS4:
        print("WARNING: BeautifulSoup is not installed!")
        print("  Install it with: pip install beautifulsoup4")
        print("  The script will use regex-based extraction as a fallback.")
        print()

    # Return the list of files that need extraction
    return files_to_extract

if __name__ == "__main__":
    result = main()

    if isinstance(result, list):
        # Output the extraction list as JSON for programmatic use
        extraction_list = [
            {
                "url": url,
                "output_path": str(path),
                "filename": path.name
            }
            for url, path in result
        ]

        print("\nExtraction List (JSON):")
        print(json.dumps(extraction_list, indent=2))

        sys.exit(1 if result else 0)
    else:
        sys.exit(result)
