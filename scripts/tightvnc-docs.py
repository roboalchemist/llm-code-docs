#!/usr/bin/env python3
"""
TightVNC Documentation Scraper
Downloads TightVNC documentation PDFs and converts to markdown.
TightVNC is a free remote desktop software package.
"""

import os
import sys
import requests
from pathlib import Path
from urllib.parse import urlparse
import time
import re
import subprocess
import tempfile

# TightVNC documentation URLs
TIGHTVNC_DOC_URLS = [
    # Windows documentation (PDFs)
    "https://www.tightvnc.com/doc/win/TightVNC_for_Windows-Installation_and_Getting_Started.pdf",
    "https://www.tightvnc.com/doc/win/TightVNC_2.7_for_Windows_Installing_from_MSI_Packages.pdf",
    "https://www.tightvnc.com/doc/win/TightVNC_2.7_for_Windows_Server_Command-Line_Options.pdf",
    # Main documentation page
    "https://www.tightvnc.com/docs.php",
    # FAQ page
    "https://www.tightvnc.com/faq.php",
]

BASE_URL = "https://www.tightvnc.com"


def pdf_to_markdown(pdf_path, url):
    """Convert PDF to markdown using pdftotext."""
    try:
        # Try pdftotext first (part of poppler-utils)
        result = subprocess.run(
            ['pdftotext', '-layout', pdf_path, '-'],
            capture_output=True,
            text=True,
            timeout=30
        )
        if result.returncode == 0:
            text = result.stdout
            # Clean up the text
            text = re.sub(r'\n{3,}', '\n\n', text)  # Normalize whitespace
            text = text.strip()
            return f"# Source: {url}\n\n{text}"
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass

    # Fallback: Try pandoc
    try:
        result = subprocess.run(
            ['pandoc', '-f', 'pdf', '-t', 'markdown', '--wrap=none', pdf_path],
            capture_output=True,
            text=True,
            timeout=30
        )
        if result.returncode == 0:
            markdown = result.stdout
            # Clean up pandoc artifacts
            markdown = re.sub(r'^::+.*$', '', markdown, flags=re.MULTILINE)
            markdown = re.sub(r'\{[^}]*\}', '', markdown)
            markdown = re.sub(r'\n{3,}', '\n\n', markdown)
            markdown = markdown.strip()
            return f"# Source: {url}\n\n{markdown}"
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass

    return None


def html_to_markdown(html_content, url):
    """Convert HTML to markdown, extracting main content only."""
    # Remove script and style elements
    html_content = re.sub(r'<script[^>]*>.*?</script>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<style[^>]*>.*?</style>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<nav[^>]*>.*?</nav>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<header[^>]*>.*?</header>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<footer[^>]*>.*?</footer>', '', html_content, flags=re.DOTALL | re.IGNORECASE)

    # Try pandoc first
    try:
        result = subprocess.run(
            ['pandoc', '-f', 'html', '-t', 'markdown', '--wrap=none'],
            input=html_content,
            capture_output=True,
            text=True,
            timeout=30
        )
        if result.returncode == 0:
            markdown = result.stdout
            # Clean up pandoc artifacts
            markdown = re.sub(r'^::+.*$', '', markdown, flags=re.MULTILINE)
            markdown = re.sub(r'\{[^}]*\}', '', markdown)
            markdown = re.sub(r'\n{3,}', '\n\n', markdown)
            markdown = markdown.strip()
            return f"# Source: {url}\n\n{markdown}"
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass

    # Fallback: basic HTML to markdown conversion
    # Headers
    for i in range(6, 0, -1):
        html_content = re.sub(rf'<h{i}[^>]*>(.*?)</h{i}>', r'\n' + '#' * i + r' \1\n', html_content, flags=re.DOTALL | re.IGNORECASE)

    # Code blocks
    html_content = re.sub(r'<pre[^>]*><code[^>]*>(.*?)</code></pre>', r'\n```\n\1\n```\n', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<code[^>]*>(.*?)</code>', r'`\1`', html_content, flags=re.DOTALL | re.IGNORECASE)

    # Links
    html_content = re.sub(r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>', r'[\2](\1)', html_content, flags=re.DOTALL | re.IGNORECASE)

    # Bold and italic
    html_content = re.sub(r'<strong[^>]*>(.*?)</strong>', r'**\1**', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<b[^>]*>(.*?)</b>', r'**\1**', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<em[^>]*>(.*?)</em>', r'*\1*', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<i[^>]*>(.*?)</i>', r'*\1*', html_content, flags=re.DOTALL | re.IGNORECASE)

    # Lists
    html_content = re.sub(r'<li[^>]*>(.*?)</li>', r'- \1\n', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<[ou]l[^>]*>', '\n', html_content, flags=re.IGNORECASE)
    html_content = re.sub(r'</[ou]l>', '\n', html_content, flags=re.IGNORECASE)

    # Paragraphs and line breaks
    html_content = re.sub(r'<p[^>]*>(.*?)</p>', r'\n\1\n', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<br\s*/?>', '\n', html_content, flags=re.IGNORECASE)
    html_content = re.sub(r'<div[^>]*>', '\n', html_content, flags=re.IGNORECASE)
    html_content = re.sub(r'</div>', '\n', html_content, flags=re.IGNORECASE)

    # Remove remaining HTML tags
    html_content = re.sub(r'<[^>]+>', '', html_content)

    # Decode HTML entities
    html_content = html_content.replace('&nbsp;', ' ')
    html_content = html_content.replace('&lt;', '<')
    html_content = html_content.replace('&gt;', '>')
    html_content = html_content.replace('&amp;', '&')
    html_content = html_content.replace('&quot;', '"')
    html_content = html_content.replace('&#39;', "'")

    # Clean up whitespace
    html_content = re.sub(r'\n\s*\n\s*\n', '\n\n', html_content)
    html_content = html_content.strip()

    return f"# Source: {url}\n\n{html_content}"


def download_document(url, output_path):
    """Download a document (PDF or HTML) and convert to markdown."""
    try:
        print(f"Downloading: {url}")

        response = requests.get(url, timeout=15)
        response.raise_for_status()

        markdown = None

        # Check if PDF
        if url.endswith('.pdf') or 'application/pdf' in response.headers.get('Content-Type', ''):
            # Save PDF temporarily
            with tempfile.NamedTemporaryFile(suffix='.pdf', delete=False) as tmp_file:
                tmp_file.write(response.content)
                tmp_path = tmp_file.name

            try:
                markdown = pdf_to_markdown(tmp_path, url)
            finally:
                # Clean up temp file
                try:
                    os.unlink(tmp_path)
                except:
                    pass

            if not markdown:
                print(f"  -> Error: Could not convert PDF (install pdftotext or pandoc)")
                return False
        else:
            # HTML page
            markdown = html_to_markdown(response.text, url)

        # Create directory if needed
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # Write markdown file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(markdown)

        print(f"  -> Saved: {output_path}")
        return True

    except requests.exceptions.RequestException as e:
        print(f"  -> Error downloading {url}: {e}")
        return False
    except Exception as e:
        print(f"  -> Error processing {url}: {e}")
        return False


def url_to_filename(url):
    """Convert URL to filename."""
    parsed = urlparse(url)
    path = parsed.path

    # Remove leading/trailing slashes
    path = path.strip("/")

    # Get filename from path
    if path.endswith('.pdf'):
        # For PDFs, use the filename
        filename = os.path.basename(path)
        # Remove .pdf and add .md
        filename = filename.replace('.pdf', '.md')
    elif path.endswith('.php'):
        # For PHP pages, use the name
        filename = os.path.basename(path).replace('.php', '.md')
    else:
        # Default
        filename = path.replace('/', '-') + '.md'

    # Clean up filename
    filename = re.sub(r'[^a-zA-Z0-9_.-]', '-', filename)
    filename = re.sub(r'-+', '-', filename)

    return filename if filename else 'index.md'


def main():
    """Main function to download all TightVNC documentation."""
    print("=" * 60)
    print("TightVNC Documentation Scraper")
    print("=" * 60)
    print(f"Base URL: {BASE_URL}")
    print(f"Documents to download: {len(TIGHTVNC_DOC_URLS)}")
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "web-scraped" / "tightvnc"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Output directory: {output_dir}")
    print()

    successful = 0
    failed = 0
    start_time = time.time()

    for i, url in enumerate(TIGHTVNC_DOC_URLS, 1):
        filename = url_to_filename(url)
        output_path = output_dir / filename

        print(f"[{i:2d}/{len(TIGHTVNC_DOC_URLS)}] ", end="")

        if download_document(url, output_path):
            successful += 1
        else:
            failed += 1

        # Be respectful with rate limiting
        time.sleep(0.5)

    elapsed = time.time() - start_time

    print()
    print("=" * 60)
    print("Download Summary")
    print("=" * 60)
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    print(f"Time: {elapsed:.1f} seconds")
    print(f"Output: {output_dir}")

    # Calculate total size
    total_size = sum(f.stat().st_size for f in output_dir.glob("*.md"))
    print(f"Total size: {total_size:,} bytes ({total_size/1024:.1f} KB)")

    print()
    if failed > 0:
        print(f"Warning: {failed} documents failed to download")
        sys.exit(1)
    else:
        print("All documents downloaded successfully!")
        sys.exit(0)


if __name__ == "__main__":
    main()
