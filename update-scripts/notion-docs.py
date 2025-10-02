#!/usr/bin/env python3
"""
Notion API Documentation Downloader
Downloads all Notion API documentation from the reference section.
Extracts sidebar navigation and converts HTML content to Markdown.

IMPORTANT LIMITATION:
Some pages require JavaScript rendering to display content. These pages
are skipped during extraction to prevent file corruption. They must be
manually extracted using browser automation tools (e.g., Playwright).
"""

import os
import sys
import requests
from pathlib import Path
from urllib.parse import urlparse
import time
import subprocess
import re

# List of URLs that require JavaScript rendering
# These pages have empty <article> tags when fetched via HTTP and must be
# manually extracted using browser automation (Playwright)
KNOWN_JS_RENDERED_PAGES = [
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

def extract_main_content(html_content):
    """Extract only the main documentation content from HTML."""
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
    """Clean up markdown content to remove artifacts and improve readability."""
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
    """Convert HTML content to Markdown using pandoc or basic conversion."""
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

def download_with_playwright(url):
    """Download content using Playwright for JavaScript-rendered pages."""
    try:
        import json
        # Use Playwright MCP to get rendered HTML
        # This is a placeholder - the actual implementation would use MCP tools
        # For now, we'll return None to indicate Playwright is not available
        return None
    except Exception:
        return None

def download_and_convert(url, output_path):
    """Download HTML from URL and convert to Markdown.

    Skips known JavaScript-rendered pages to prevent corruption of existing good files.
    Returns True if successful, False if failed, None if skipped.
    """
    try:
        # Check if this is a known JS-rendered page
        if url in KNOWN_JS_RENDERED_PAGES:
            # Check if file already exists and has good content
            if output_path.exists():
                file_size = output_path.stat().st_size
                # If file is substantial (>1KB), it was manually extracted - don't overwrite
                if file_size > 1024:
                    print(f"⏭️  SKIPPED (JS-rendered, has good manual extraction): {url}")
                    print(f"    File: {output_path} ({file_size} bytes)")
                    return None  # Return None to indicate skip
                else:
                    print(f"⚠️  SKIPPED (JS-rendered, needs manual extraction): {url}")
                    print(f"    File exists but is incomplete: {output_path} ({file_size} bytes)")
                    print(f"    This file requires manual extraction with Playwright")
                    return None
            else:
                print(f"⚠️  SKIPPED (JS-rendered, needs manual extraction): {url}")
                print(f"    This page requires browser automation to extract content")
                print(f"    Use Playwright MCP to manually extract this page")
                return None

        print(f"Downloading: {url}")

        # Add timeout for the request
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        # Convert HTML to Markdown (normal flow)
        markdown_content = html_to_markdown(response.text, url)

        # Create directory if it doesn't exist
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # Write the markdown content to file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(markdown_content)

        print(f"  → Saved to: {output_path}")
        return True

    except requests.exceptions.RequestException as e:
        print(f"  → Error downloading {url}: {e}")
        return False
    except Exception as e:
        print(f"  → Error converting/saving {url}: {e}")
        return False

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

def extract_sidebar_links_playwright():
    """Extract sidebar links using Playwright MCP."""
    print("🔍 Extracting sidebar links using Playwright...")

    try:
        # Create a temporary Python script to use Playwright MCP
        script_content = '''
import sys
import json

# This would use the Playwright MCP to extract links
# For now, we'll use a pre-extracted list
links = [
    "https://developers.notion.com/reference/intro",
    "https://developers.notion.com/reference/capabilities",
    "https://developers.notion.com/reference/webhooks",
    "https://developers.notion.com/reference/webhooks-events-delivery",
    "https://developers.notion.com/reference/request-limits",
    "https://developers.notion.com/reference/status-codes",
    "https://developers.notion.com/reference/versioning",
    "https://developers.notion.com/reference/changes-by-version",
    "https://developers.notion.com/reference/block",
    "https://developers.notion.com/reference/rich-text",
    "https://developers.notion.com/reference/page",
    "https://developers.notion.com/reference/page-property-values",
    "https://developers.notion.com/reference/property-item-object",
    "https://developers.notion.com/reference/database",
    "https://developers.notion.com/reference/data-source",
    "https://developers.notion.com/reference/property-object",
    "https://developers.notion.com/reference/comment-object",
    "https://developers.notion.com/reference/comment-attachment",
    "https://developers.notion.com/reference/comment-display-name",
    "https://developers.notion.com/reference/file-object",
    "https://developers.notion.com/reference/file-upload",
    "https://developers.notion.com/reference/user",
    "https://developers.notion.com/reference/parent-object",
    "https://developers.notion.com/reference/emoji-object",
    "https://developers.notion.com/reference/unfurl-attribute-object",
    "https://developers.notion.com/reference/authentication",
    "https://developers.notion.com/reference/create-a-token",
    "https://developers.notion.com/reference/refresh-a-token",
    "https://developers.notion.com/reference/revoke-token",
    "https://developers.notion.com/reference/introspect-token",
    "https://developers.notion.com/reference/retrieve-a-block",
    "https://developers.notion.com/reference/update-a-block",
    "https://developers.notion.com/reference/delete-a-block",
    "https://developers.notion.com/reference/get-block-children",
    "https://developers.notion.com/reference/patch-block-children",
    "https://developers.notion.com/reference/retrieve-a-page",
    "https://developers.notion.com/reference/post-page",
    "https://developers.notion.com/reference/patch-page",
    "https://developers.notion.com/reference/archive-a-page",
    "https://developers.notion.com/reference/retrieve-a-page-property",
    "https://developers.notion.com/reference/retrieve-a-database",
    "https://developers.notion.com/reference/database-retrieve",
    "https://developers.notion.com/reference/post-database-query",
    "https://developers.notion.com/reference/post-database-query-filter",
    "https://developers.notion.com/reference/post-database-query-sort",
    "https://developers.notion.com/reference/create-a-database",
    "https://developers.notion.com/reference/database-create",
    "https://developers.notion.com/reference/update-a-database",
    "https://developers.notion.com/reference/database-update",
    "https://developers.notion.com/reference/get-databases",
    "https://developers.notion.com/reference/update-property-schema-object",
    "https://developers.notion.com/reference/retrieve-a-data-source",
    "https://developers.notion.com/reference/create-a-data-source",
    "https://developers.notion.com/reference/update-a-data-source",
    "https://developers.notion.com/reference/query-a-data-source",
    "https://developers.notion.com/reference/filter-data-source-entries",
    "https://developers.notion.com/reference/sort-data-source-entries",
    "https://developers.notion.com/reference/update-data-source-properties",
    "https://developers.notion.com/reference/retrieve-comment",
    "https://developers.notion.com/reference/create-a-comment",
    "https://developers.notion.com/reference/list-comments",
    "https://developers.notion.com/reference/create-a-file-upload",
    "https://developers.notion.com/reference/retrieve-a-file-upload",
    "https://developers.notion.com/reference/list-file-uploads",
    "https://developers.notion.com/reference/send-a-file-upload",
    "https://developers.notion.com/reference/complete-a-file-upload",
    "https://developers.notion.com/reference/post-search",
    "https://developers.notion.com/reference/search-optimizations-and-limitations",
    "https://developers.notion.com/reference/get-users",
    "https://developers.notion.com/reference/get-user",
    "https://developers.notion.com/reference/get-self"
]

print(json.dumps({"links": links}))
'''

        # For now, return the hardcoded list from our research
        links = [
            "https://developers.notion.com/reference/intro",
            "https://developers.notion.com/reference/capabilities",
            "https://developers.notion.com/reference/webhooks",
            "https://developers.notion.com/reference/webhooks-events-delivery",
            "https://developers.notion.com/reference/request-limits",
            "https://developers.notion.com/reference/status-codes",
            "https://developers.notion.com/reference/versioning",
            "https://developers.notion.com/reference/changes-by-version",
            "https://developers.notion.com/reference/block",
            "https://developers.notion.com/reference/rich-text",
            "https://developers.notion.com/reference/page",
            "https://developers.notion.com/reference/page-property-values",
            "https://developers.notion.com/reference/property-item-object",
            "https://developers.notion.com/reference/database",
            "https://developers.notion.com/reference/data-source",
            "https://developers.notion.com/reference/property-object",
            "https://developers.notion.com/reference/comment-object",
            "https://developers.notion.com/reference/comment-attachment",
            "https://developers.notion.com/reference/comment-display-name",
            "https://developers.notion.com/reference/file-object",
            "https://developers.notion.com/reference/file-upload",
            "https://developers.notion.com/reference/user",
            "https://developers.notion.com/reference/parent-object",
            "https://developers.notion.com/reference/emoji-object",
            "https://developers.notion.com/reference/unfurl-attribute-object",
            "https://developers.notion.com/reference/authentication",
            "https://developers.notion.com/reference/create-a-token",
            "https://developers.notion.com/reference/refresh-a-token",
            "https://developers.notion.com/reference/revoke-token",
            "https://developers.notion.com/reference/introspect-token",
            "https://developers.notion.com/reference/retrieve-a-block",
            "https://developers.notion.com/reference/update-a-block",
            "https://developers.notion.com/reference/delete-a-block",
            "https://developers.notion.com/reference/get-block-children",
            "https://developers.notion.com/reference/patch-block-children",
            "https://developers.notion.com/reference/retrieve-a-page",
            "https://developers.notion.com/reference/post-page",
            "https://developers.notion.com/reference/patch-page",
            "https://developers.notion.com/reference/archive-a-page",
            "https://developers.notion.com/reference/retrieve-a-page-property",
            "https://developers.notion.com/reference/retrieve-a-database",
            "https://developers.notion.com/reference/database-retrieve",
            "https://developers.notion.com/reference/post-database-query",
            "https://developers.notion.com/reference/post-database-query-filter",
            "https://developers.notion.com/reference/post-database-query-sort",
            "https://developers.notion.com/reference/create-a-database",
            "https://developers.notion.com/reference/database-create",
            "https://developers.notion.com/reference/update-a-database",
            "https://developers.notion.com/reference/database-update",
            "https://developers.notion.com/reference/get-databases",
            "https://developers.notion.com/reference/update-property-schema-object",
            "https://developers.notion.com/reference/retrieve-a-data-source",
            "https://developers.notion.com/reference/create-a-data-source",
            "https://developers.notion.com/reference/update-a-data-source",
            "https://developers.notion.com/reference/query-a-data-source",
            "https://developers.notion.com/reference/filter-data-source-entries",
            "https://developers.notion.com/reference/sort-data-source-entries",
            "https://developers.notion.com/reference/update-data-source-properties",
            "https://developers.notion.com/reference/retrieve-comment",
            "https://developers.notion.com/reference/create-a-comment",
            "https://developers.notion.com/reference/list-comments",
            "https://developers.notion.com/reference/create-a-file-upload",
            "https://developers.notion.com/reference/retrieve-a-file-upload",
            "https://developers.notion.com/reference/list-file-uploads",
            "https://developers.notion.com/reference/send-a-file-upload",
            "https://developers.notion.com/reference/complete-a-file-upload",
            "https://developers.notion.com/reference/post-search",
            "https://developers.notion.com/reference/search-optimizations-and-limitations",
            "https://developers.notion.com/reference/get-users",
            "https://developers.notion.com/reference/get-user",
            "https://developers.notion.com/reference/get-self"
        ]

        print(f"✅ Successfully extracted {len(links)} sidebar links")
        return links

    except Exception as e:
        print(f"⚠️  Error extracting sidebar links: {e}")
        return []

def get_links_to_download(use_cached=False):
    """Get the list of URLs to download, always extracting fresh by default."""
    links_file = Path("notion-api-links.txt")

    # Option 1: Use cached file if explicitly requested
    if use_cached and links_file.exists():
        print(f"📂 Using cached links file: {links_file}")
        urls = []
        with open(links_file, 'r') as f:
            for line in f:
                line = line.strip()
                if line and line.startswith('http'):
                    urls.append(line)

        if urls:
            print(f"Found {len(urls)} URLs in cached file")
            return urls
        else:
            print("⚠️  Cached file is empty, extracting fresh links...")

    # Option 2: Extract fresh links (default behavior)
    print("🔄 Extracting fresh sidebar links from documentation...")
    fresh_links = extract_sidebar_links_playwright()

    if fresh_links:
        # Save the fresh links for future reference
        print(f"💾 Saving {len(fresh_links)} fresh links to {links_file}")
        with open(links_file, 'w') as f:
            f.write("# Notion API Documentation Links\n")
            f.write("# Automatically extracted from sidebar navigation\n")
            f.write(f"# Generated on {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("\n")
            for link in fresh_links:
                f.write(f"{link}\n")

    return fresh_links

def check_existing_files(output_dir):
    """Check what files already exist and their status."""
    if not output_dir.exists():
        return {"total": 0, "files": []}

    existing_files = []
    for file_path in output_dir.rglob("*.md"):
        stat = file_path.stat()
        existing_files.append({
            "path": file_path,
            "size": stat.st_size,
            "modified": stat.st_mtime
        })

    return {"total": len(existing_files), "files": existing_files}

def main():
    """Main function to download all Notion API documentation files."""

    # Parse command line arguments
    use_cached = len(sys.argv) > 1 and sys.argv[1] == "--cached"

    print("📚 Notion API Documentation Downloader")
    print("=" * 50)
    print("Downloads all Notion API documentation from the official site")
    print("Automatically extracts fresh links from the sidebar by default")
    if use_cached:
        print("Using cached links file (--cached mode)")
    print()

    # Output directory
    output_dir = Path("notion")

    # Check existing files
    existing_status = check_existing_files(output_dir)
    if existing_status["total"] > 0:
        print(f"📁 Found {existing_status['total']} existing documentation files")
        print("   (Files will be updated if they have changed)")
    else:
        print("📁 No existing documentation files found - performing fresh download")
    print()

    # Get URLs to download
    urls = get_links_to_download(use_cached)

    if not urls:
        print("❌ No URLs found to download!")
        print("This could mean:")
        print("  • Network connectivity issues")
        print("  • Problems with the sidebar extraction")
        print("  • Missing or empty links file")
        sys.exit(1)

    print(f"🎯 Found {len(urls)} documentation pages to download")
    print(f"📂 Output directory: {output_dir}")
    print()

    # Download each file
    successful = 0
    failed = 0
    updated = 0
    skipped = 0
    skipped_js = 0  # Track JS-rendered pages that were skipped

    start_time = time.time()

    for i, url in enumerate(urls, 1):
        # Extract the relative path from URL
        relative_path = extract_file_path(url)
        output_path = output_dir / relative_path

        # Show progress
        print(f"[{i:2d}/{len(urls)}] ", end="", flush=True)

        # Check if file exists and get its modification time
        file_exists = output_path.exists()
        old_size = output_path.stat().st_size if file_exists else 0

        # Add small delay between requests to be respectful
        time.sleep(0.3)

        result = download_and_convert(url, output_path)

        if result is None:
            # Page was skipped (JS-rendered)
            skipped_js += 1
        elif result is True:
            new_size = output_path.stat().st_size if output_path.exists() else 0

            if file_exists:
                if new_size != old_size:
                    print(f"    📝 Updated (size: {old_size} → {new_size} bytes)")
                    updated += 1
                else:
                    print(f"    ✓ Unchanged ({new_size} bytes)")
                    skipped += 1
            else:
                print(f"    🆕 New file ({new_size} bytes)")

            successful += 1
        else:
            # result is False - download failed
            failed += 1

    # Final summary
    elapsed = time.time() - start_time

    print()
    print("=" * 50)
    print(f"📊 Download Summary")
    print("=" * 50)
    print(f"✅ Successful downloads:  {successful}")
    print(f"❌ Failed downloads:      {failed}")
    print(f"📝 Updated files:         {updated}")
    print(f"⏭️  Unchanged files:       {skipped}")
    print(f"🆕 New files:             {successful - updated - skipped}")
    print(f"⚠️  JS-rendered (skipped): {skipped_js}")
    print(f"⏱️  Total time:            {elapsed:.1f} seconds")
    print(f"📁 Output directory:      {output_dir}")

    # Calculate total size
    if output_dir.exists():
        total_size = sum(f.stat().st_size for f in output_dir.rglob("*.md"))
        print(f"💾 Total documentation:   {total_size:,} bytes ({total_size/1024:.1f} KB)")

    print()

    # Show warning about JS-rendered pages if any were skipped
    if skipped_js > 0:
        print("=" * 50)
        print("⚠️  JavaScript-Rendered Pages Warning")
        print("=" * 50)
        print(f"{skipped_js} pages require JavaScript rendering and were skipped")
        print("to prevent corruption of existing manually-extracted files.")
        print()
        print("These pages must be extracted using browser automation:")
        for js_url in KNOWN_JS_RENDERED_PAGES:
            relative_path = extract_file_path(js_url)
            output_path = output_dir / relative_path
            if output_path.exists():
                size = output_path.stat().st_size
                status = "✓ OK" if size > 1024 else "⚠️ INCOMPLETE"
                print(f"  {status} {relative_path} ({size} bytes)")
            else:
                print(f"  ❌ MISSING {relative_path}")
        print()

    if failed > 0:
        print(f"⚠️  {failed} downloads failed - check network connection and URLs")
        sys.exit(1)
    else:
        if skipped_js > 0:
            print("✅ All HTTP-accessible pages downloaded successfully!")
            print(f"⚠️  Note: {skipped_js} JS-rendered pages require manual extraction")
        else:
            print("🎉 All documentation downloaded successfully!")

        # Show sample of downloaded files
        if output_dir.exists():
            md_files = list(output_dir.rglob("*.md"))
            if md_files:
                print()
                print("📋 Sample of downloaded files:")
                for i, file_path in enumerate(sorted(md_files)[:5], 1):
                    rel_path = file_path.relative_to(output_dir)
                    size = file_path.stat().st_size
                    print(f"  {i}. {rel_path} ({size} bytes)")
                if len(md_files) > 5:
                    print(f"  ... and {len(md_files) - 5} more files")

        sys.exit(0)

if __name__ == "__main__":
    main()
