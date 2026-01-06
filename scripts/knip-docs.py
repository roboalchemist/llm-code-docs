#!/usr/bin/env python3
"""
Scraper for Knip documentation.
Knip is a TypeScript tool for detecting unused files, dependencies, and exports.
Output: docs/web-scraped/knip/
"""

import os
import requests
from pathlib import Path
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import time

BASE_URL = "https://knip.dev"
OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "web-scraped" / "knip"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Core documentation pages to scrape
CORE_PAGES = [
    "/",
    "/overview/getting-started",
    "/overview/requirements",
    "/overview/features",
    "/reference/configuration",
    "/reference/cli-commands",
    "/reference/api",
    "/reference/plugins",
    "/reference/faq",
    "/features/auto-fix",
    "/features/compilers",
    "/features/integrated-monorepos",
    "/features/monorepos-and-workspaces",
    "/features/production-mode",
    "/features/reporters",
    "/features/rules-and-filters",
    "/features/script-parser",
    "/features/source-mapping",
    "/explanations/comparison-and-migration",
    "/explanations/entry-files",
    "/explanations/plugins",
    "/explanations/why-use-knip",
    "/guides/configuring-project-files",
    "/guides/contributing",
    "/guides/handling-issues",
    "/guides/issue-reproduction",
    "/guides/namespace-imports",
    "/guides/performance",
    "/guides/troubleshooting",
]

def html_to_markdown(html_content):
    """Convert HTML to markdown format."""
    soup = BeautifulSoup(html_content, 'html.parser')

    # Remove script and style elements
    for script in soup(["script", "style"]):
        script.decompose()

    # Extract main content - typically in article or main tags
    main_content = soup.find('main') or soup.find('article') or soup.find('body')
    if not main_content:
        main_content = soup

    lines = []

    for element in main_content.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'li', 'code', 'pre', 'a']):
        if element.name.startswith('h'):
            level = int(element.name[1])
            text = element.get_text(strip=True)
            if text:
                lines.append(f"{'#' * level} {text}\n")
        elif element.name == 'p':
            text = element.get_text(strip=True)
            if text:
                lines.append(f"{text}\n")
        elif element.name == 'li':
            text = element.get_text(strip=True)
            if text:
                lines.append(f"- {text}\n")
        elif element.name == 'pre':
            code = element.get_text(strip=True)
            if code:
                lines.append(f"```\n{code}\n```\n")
        elif element.name == 'code' and element.parent.name != 'pre':
            text = element.get_text(strip=True)
            if text:
                lines.append(f"`{text}`")

    # Clean up output
    markdown = ''.join(lines)
    # Remove excessive blank lines
    markdown = '\n'.join([line for line in markdown.split('\n') if line.strip() or len([l for l in lines if not l.strip()]) < 2])

    return markdown.strip()

def scrape_page(url_path, filename=None):
    """Scrape a single documentation page."""
    full_url = urljoin(BASE_URL, url_path)
    if not filename:
        # Convert path to filename: /overview/getting-started -> overview-getting-started.md
        filename = url_path.strip('/').replace('/', '-') + '.md'

    print(f"Scraping {full_url}...")

    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (compatible; Documentation Scraper)'
        }
        response = requests.get(full_url, timeout=10, headers=headers)
        response.raise_for_status()

        # Extract main content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the main content area
        main = soup.find('main')
        if not main:
            main = soup.find('article')
        if not main:
            main = soup.body

        if not main:
            print(f"  Warning: Could not find main content for {url_path}")
            return False

        # Extract title
        title_elem = main.find(['h1', 'title'])
        title = title_elem.get_text(strip=True) if title_elem else url_path

        # Build markdown content
        content = f"# {title}\n\n"
        content += f"Source: {full_url}\n\n"

        # Extract content more intelligently
        for element in main.find_all(True):
            if element.name in ['h2', 'h3', 'h4', 'h5', 'h6']:
                text = element.get_text(strip=True)
                if text and text != title:
                    level = int(element.name[1])
                    content += f"{'#' * level} {text}\n\n"
            elif element.name == 'p':
                text = element.get_text(strip=True)
                if text and len(text) > 10:
                    content += f"{text}\n\n"
            elif element.name == 'ul' or element.name == 'ol':
                for li in element.find_all('li', recursive=False):
                    text = li.get_text(strip=True)
                    if text:
                        content += f"- {text}\n"
                content += "\n"
            elif element.name == 'pre':
                code_text = element.get_text(strip=True)
                if code_text:
                    # Try to detect language
                    lang = 'typescript'
                    if 'bash' in code_text.lower() or element.get('class', []):
                        lang = 'bash'
                    content += f"```{lang}\n{code_text}\n```\n\n"

        # Write to file
        output_file = OUTPUT_DIR / filename
        output_file.parent.mkdir(parents=True, exist_ok=True)
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"  Saved to {filename} ({len(content)} bytes)")
        return True

    except Exception as e:
        print(f"  Error scraping {full_url}: {e}")
        return False

def main():
    """Main scraper function."""
    print(f"Knip Documentation Scraper")
    print(f"Output directory: {OUTPUT_DIR}\n")

    # Create index file
    index_content = """# Knip Documentation Index

Knip is a TypeScript tool for detecting unused files, dependencies, and exports in projects.

## Quick Links

- [Getting Started](overview-getting-started.md)
- [Configuration Reference](reference-configuration.md)
- [CLI Commands](reference-cli-commands.md)
- [FAQ](reference-faq.md)
- [Plugins](reference-plugins.md)

## Documentation Sections

### Overview
- Getting Started
- Requirements
- Features

### Reference
- Configuration
- CLI Commands
- API
- Plugins
- FAQ

### Features
- Auto-fix
- Compilers
- Monorepos and Workspaces
- Production Mode
- Reporters
- Rules and Filters
- Script Parser
- Source Mapping

### Explanations
- Comparison and Migration
- Entry Files
- Plugins
- Why Use Knip

### Guides
- Configuring Project Files
- Contributing
- Handling Issues
- Issue Reproduction
- Namespace Imports
- Performance
- Troubleshooting

## External Resources

- Official Website: https://knip.dev
- GitHub Repository: https://github.com/webpro-nl/knip
- NPM Package: https://www.npmjs.com/package/knip
"""

    with open(OUTPUT_DIR / "INDEX.md", 'w', encoding='utf-8') as f:
        f.write(index_content)
    print(f"Created INDEX.md\n")

    # Scrape all pages
    successful = 0
    failed = 0

    for page in CORE_PAGES:
        if scrape_page(page):
            successful += 1
        else:
            failed += 1
        time.sleep(0.5)  # Rate limiting

    print(f"\nScraping complete: {successful} successful, {failed} failed")
    print(f"Documentation saved to {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
