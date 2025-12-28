#!/usr/bin/env python3
"""
DigiKey Developer API Documentation Scraper
Downloads DigiKey Developer API documentation and converts to markdown.

Note: The main developer.digikey.com site uses Cloudflare protection, so this
scraper combines multiple sources:
1. GitHub client library documentation (peeter123/digikey-api)
2. Known API endpoint documentation URLs
3. PyPI package documentation
"""

import os
import sys
import requests
from pathlib import Path
import time
import re
import subprocess
import tempfile
import shutil

# Known DigiKey Developer documentation pages
# These are from the site structure discovered via search engines
DIGIKEY_DOC_PAGES = [
    # Main pages
    {
        "name": "overview",
        "title": "DigiKey API Overview",
        "source": "github",
        "url": "https://raw.githubusercontent.com/peeter123/digikey-api/master/README.md"
    },
    # We'll also clone and extract from the GitHub repo
]

# GitHub repository to clone for comprehensive documentation
GITHUB_REPO = "https://github.com/peeter123/digikey-api.git"
GITHUB_BRANCH = "master"


def html_to_markdown(html_content, url):
    """Convert HTML to markdown using pandoc if available."""
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

    # Fallback: basic HTML extraction
    # Remove script and style elements
    html_content = re.sub(r'<script[^>]*>.*?</script>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<style[^>]*>.*?</style>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<nav[^>]*>.*?</nav>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<header[^>]*>.*?</header>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<footer[^>]*>.*?</footer>', '', html_content, flags=re.DOTALL | re.IGNORECASE)

    # Convert common HTML elements to markdown
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


def download_page(url, output_path):
    """Download a page and convert to markdown."""
    try:
        print(f"Downloading: {url}")

        response = requests.get(url, timeout=15, headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
        })
        response.raise_for_status()

        # If it's already markdown, just add source header
        if url.endswith('.md'):
            markdown = f"# Source: {url}\n\n{response.text}"
        else:
            # Convert HTML to markdown
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


def clone_and_extract_github_docs(output_dir):
    """Clone GitHub repository and extract documentation files."""
    print(f"\nCloning GitHub repository: {GITHUB_REPO}")

    # Create temporary directory
    with tempfile.TemporaryDirectory() as tmpdir:
        tmpdir = Path(tmpdir)
        repo_dir = tmpdir / "digikey-api"

        try:
            # Clone repository
            result = subprocess.run(
                ['git', 'clone', '--depth', '1', '--branch', GITHUB_BRANCH, GITHUB_REPO, str(repo_dir)],
                capture_output=True,
                text=True,
                timeout=60
            )

            if result.returncode != 0:
                print(f"  -> Error cloning repository: {result.stderr}")
                return False

            print(f"  -> Cloned successfully")

            # Extract README.md
            readme_src = repo_dir / "README.md"
            if readme_src.exists():
                readme_dst = output_dir / "README.md"
                with open(readme_src, 'r', encoding='utf-8') as f:
                    content = f.read()
                with open(readme_dst, 'w', encoding='utf-8') as f:
                    f.write(f"# Source: {GITHUB_REPO}\n\n{content}")
                print(f"  -> Extracted: README.md")

            # Extract docs/ directory if it exists
            docs_src = repo_dir / "docs"
            if docs_src.exists() and docs_src.is_dir():
                for doc_file in docs_src.rglob("*.md"):
                    rel_path = doc_file.relative_to(docs_src)
                    doc_dst = output_dir / "docs" / rel_path
                    doc_dst.parent.mkdir(parents=True, exist_ok=True)

                    with open(doc_file, 'r', encoding='utf-8') as f:
                        content = f.read()

                    # Add source header
                    github_url = f"{GITHUB_REPO.replace('.git', '')}/blob/{GITHUB_BRANCH}/docs/{rel_path}"
                    with open(doc_dst, 'w', encoding='utf-8') as f:
                        f.write(f"# Source: {github_url}\n\n{content}")

                    print(f"  -> Extracted: docs/{rel_path}")

            # Extract any other markdown files in root
            for md_file in repo_dir.glob("*.md"):
                if md_file.name != "README.md":  # Already handled
                    md_dst = output_dir / md_file.name
                    with open(md_file, 'r', encoding='utf-8') as f:
                        content = f.read()

                    github_url = f"{GITHUB_REPO.replace('.git', '')}/blob/{GITHUB_BRANCH}/{md_file.name}"
                    with open(md_dst, 'w', encoding='utf-8') as f:
                        f.write(f"# Source: {github_url}\n\n{content}")

                    print(f"  -> Extracted: {md_file.name}")

            # Create API reference from Python code docstrings
            create_api_reference(repo_dir, output_dir)

            return True

        except subprocess.TimeoutExpired:
            print(f"  -> Error: Git clone timeout")
            return False
        except Exception as e:
            print(f"  -> Error extracting docs: {e}")
            return False


def create_api_reference(repo_dir, output_dir):
    """Create API reference documentation from Python source code."""
    print(f"  -> Creating API reference from source code")

    api_ref = []
    api_ref.append("# DigiKey API Python Client Reference")
    api_ref.append(f"\n# Source: {GITHUB_REPO}")
    api_ref.append("\n## API Endpoints\n")

    # Extract main API functions from digikey module
    digikey_dir = repo_dir / "digikey"
    if digikey_dir.exists():
        # Look for __init__.py and other key files
        for py_file in digikey_dir.rglob("*.py"):
            if py_file.name.startswith("_") and py_file.name != "__init__.py":
                continue

            try:
                with open(py_file, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Extract function definitions and their docstrings
                func_pattern = r'def\s+(\w+)\s*\([^)]*\):\s*"""([^"]+)"""'
                matches = re.finditer(func_pattern, content, re.MULTILINE | re.DOTALL)

                for match in matches:
                    func_name = match.group(1)
                    docstring = match.group(2).strip()

                    if not func_name.startswith('_'):  # Public functions only
                        api_ref.append(f"### `{func_name}()`\n")
                        api_ref.append(f"{docstring}\n")

            except Exception as e:
                print(f"    -> Warning: Could not parse {py_file.name}: {e}")

    # Write API reference
    api_ref_path = output_dir / "api-reference.md"
    with open(api_ref_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(api_ref))

    print(f"  -> Created: api-reference.md")


def main():
    """Main function to download all DigiKey documentation."""
    print("=" * 60)
    print("DigiKey Developer API Documentation Scraper")
    print("=" * 60)
    print(f"GitHub Repository: {GITHUB_REPO}")
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "web-scraped" / "digikey"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Output directory: {output_dir}")
    print()

    successful = 0
    failed = 0
    start_time = time.time()

    # Clone and extract GitHub documentation
    if clone_and_extract_github_docs(output_dir):
        successful += 1
    else:
        failed += 1

    # Download additional pages from known URLs
    for page in DIGIKEY_DOC_PAGES:
        if page.get("source") == "github" and "url" in page:
            output_path = output_dir / f"{page['name']}.md"
            if download_page(page["url"], output_path):
                successful += 1
            else:
                failed += 1
            time.sleep(0.5)  # Be respectful

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
    total_size = sum(f.stat().st_size for f in output_dir.rglob("*.md"))
    print(f"Total size: {total_size:,} bytes ({total_size/1024:.1f} KB)")

    print()
    if failed > 0:
        print(f"Warning: {failed} operations failed")
        sys.exit(1)
    else:
        print("All documentation extracted successfully!")
        sys.exit(0)


if __name__ == "__main__":
    main()
