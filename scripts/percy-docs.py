#!/usr/bin/env python3
"""
Scraper for Percy visual testing documentation.
Extracts documentation from BrowserStack's Percy docs at:
https://www.browserstack.com/docs/percy/

Output: docs/web-scraped/percy/
"""

import requests
from pathlib import Path
import time
from urllib.parse import urlparse, urljoin
from bs4 import BeautifulSoup
import re

OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "web-scraped" / "percy"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Track downloaded files to avoid duplicates
downloaded_urls = set()

# Base URL for Percy docs
BASE_URL = "https://www.browserstack.com/docs/percy/"

def sanitize_filename(url):
    """Convert URL to safe filename"""
    parsed = urlparse(url)
    path = parsed.path.strip('/')
    if not path or path == 'docs/percy':
        return 'index.md'

    # Extract the part after /docs/percy/
    if '/docs/percy/' in path:
        path = path.split('/docs/percy/')[-1]

    # Remove query parameters and anchors
    path = path.split('?')[0].split('#')[0]
    # Replace slashes with dashes, remove trailing slashes
    path = path.rstrip('/')
    filename = path.replace('/', '-')
    if not filename:
        filename = 'index'

    return filename[:120] + '.md'

def extract_markdown_from_html(html_content, url=''):
    """Convert HTML to basic markdown"""
    soup = BeautifulSoup(html_content, 'html.parser')

    # Remove unwanted elements
    for elem in soup(['script', 'style', 'nav', 'footer', '.sidebar', 'aside']):
        elem.decompose()

    # Remove common navigation/UI elements
    for elem in soup.find_all(class_=['sidebar', 'nav', 'navigation', 'breadcrumb']):
        elem.decompose()

    # Get main content
    main_content = soup.find('main')
    if not main_content:
        main_content = soup.find(class_=['main-content', 'content', 'article'])
    if not main_content:
        main_content = soup.find('article')

    if main_content:
        content_html = str(main_content)
    else:
        content_html = str(soup)

    # Basic HTML to Markdown conversion
    markdown = convert_html_to_markdown(content_html)
    return markdown.strip()

def convert_html_to_markdown(html):
    """Convert HTML to Markdown"""
    soup = BeautifulSoup(html, 'html.parser')

    markdown_parts = []
    processed_texts = set()

    # Process all relevant elements
    for elem in soup.find_all(True):
        if elem.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            text = elem.get_text(strip=True)
            if text and text not in processed_texts:
                level = int(elem.name[1])
                markdown_parts.append(f"\n{'#' * level} {text}\n")
                processed_texts.add(text)

        elif elem.name == 'p':
            text = elem.get_text(strip=True)
            if text and len(text) > 0 and text not in processed_texts:
                markdown_parts.append(f"{text}\n\n")
                processed_texts.add(text)

        elif elem.name == 'li':
            text = elem.get_text(strip=True)
            if text and text not in processed_texts:
                markdown_parts.append(f"- {text}\n")
                processed_texts.add(text)

        elif elem.name in ['pre', 'code']:
            text = elem.get_text()
            if text and len(text) > 3:
                if elem.name == 'pre':
                    markdown_parts.append(f"\n```\n{text}\n```\n\n")
                else:
                    # Only add inline code if it's not too long
                    if len(text) < 100:
                        markdown_parts.append(f"`{text.strip()}`")

        elif elem.name == 'a':
            href = elem.get('href', '')
            text = elem.get_text(strip=True)
            if text and href and 'javascript:' not in href:
                if href.startswith('/'):
                    href = urljoin(BASE_URL, href)
                markdown_parts.append(f"[{text}]({href})")

        elif elem.name == 'table':
            # Simple table conversion
            markdown_parts.append("\n")
            for row in elem.find_all('tr'):
                cells = []
                for cell in row.find_all(['td', 'th']):
                    cells.append(cell.get_text(strip=True))
                if cells:
                    markdown_parts.append("| " + " | ".join(cells) + " |\n")
            markdown_parts.append("\n")

    result = ''.join(markdown_parts)
    # Clean up excessive whitespace
    result = re.sub(r'\n\n\n+', '\n\n', result)
    return result.strip()

def download_page(url):
    """Download a single page and convert to markdown"""
    if url in downloaded_urls:
        return None

    try:
        # Only download from browserstack.com/docs/percy
        if 'browserstack.com/docs/percy' not in url:
            return None

        downloaded_urls.add(url)

        print(f"  Downloading: {url}")
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
        }

        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()

        # Extract markdown
        if 'text/html' in response.headers.get('content-type', ''):
            markdown = extract_markdown_from_html(response.text, url)
        else:
            markdown = response.text

        if markdown and len(markdown) > 100:
            # Add source header
            markdown = f"# Source: {url}\n\n{markdown}"
            return markdown

    except requests.exceptions.Timeout:
        print(f"  Timeout: {url}")
    except requests.exceptions.HTTPError as e:
        print(f"  HTTP Error {e.response.status_code}: {url}")
    except Exception as e:
        print(f"  Error downloading {url}: {e}")

    return None

def save_documentation(url, content):
    """Save documentation to file"""
    if content and len(content) > 100:
        filename = sanitize_filename(url)
        filepath = OUTPUT_DIR / filename

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"    Saved: {filename} ({len(content)} bytes)")
        return filepath
    return None

def get_documentation_urls():
    """Get list of all Percy documentation URLs"""
    # List of key Percy documentation pages (from crawl results)
    urls = [
        "https://www.browserstack.com/docs/percy/",
        "https://www.browserstack.com/docs/percy/get-started",
        "https://www.browserstack.com/docs/percy/get-started/first-percy-build",
        "https://www.browserstack.com/docs/percy/integrate/overview",
        "https://www.browserstack.com/docs/percy/integrate/percy-sdk-workflow",
        "https://www.browserstack.com/docs/percy/api-reference/authentication",
        "https://www.browserstack.com/docs/percy/build-results/overview",
        "https://www.browserstack.com/docs/percy/build-results/visual-testing",
        "https://www.browserstack.com/docs/percy/build-results/approval",
        "https://www.browserstack.com/docs/percy/build-results/build-lifecycle",
        "https://www.browserstack.com/docs/percy/build-results/responsive-testing",
        "https://www.browserstack.com/docs/percy/build-results/diff-highlighter",
        "https://www.browserstack.com/docs/percy/build-results/ignore-regions",
        "https://www.browserstack.com/docs/percy/build-results/layout-testing",
        "https://www.browserstack.com/docs/percy/build-results/labels",
        "https://www.browserstack.com/docs/percy/build-results/comments",
        "https://www.browserstack.com/docs/percy/build-results/root-cause-analysis",
        "https://www.browserstack.com/docs/percy/advanced-snapshots/percy-css",
        "https://www.browserstack.com/docs/percy/ci-cd/overview",
        "https://www.browserstack.com/docs/percy/baseline-management/git",
        "https://www.browserstack.com/docs/percy/figma/overview",
        "https://www.browserstack.com/docs/percy/figma/configuration",
        "https://www.browserstack.com/docs/percy/figma/baseline-management",
        # Framework-specific integrations
        "https://www.browserstack.com/docs/percy/cypress/getting-started",
        "https://www.browserstack.com/docs/percy/cypress/getting-started/integrate-your-tests",
        "https://www.browserstack.com/docs/percy/playwright/getting-started",
        "https://www.browserstack.com/docs/percy/webdriverio/getting-started",
        "https://www.browserstack.com/docs/percy/appium/get-started",
        "https://www.browserstack.com/docs/percy/puppeteer/getting-started",
        "https://www.browserstack.com/docs/percy/protractor/getting-started",
        "https://www.browserstack.com/docs/percy/selenium/getting-started",
        "https://www.browserstack.com/docs/percy/testcafe/getting-started",
        "https://www.browserstack.com/docs/percy/ember/getting-started",
        "https://www.browserstack.com/docs/percy/gatsby/getting-started",
        "https://www.browserstack.com/docs/percy/nightwatch/getting-started",
        # Common issues
        "https://www.browserstack.com/docs/percy/common-issue/common-errors/missing-percy-token",
        "https://www.browserstack.com/docs/percy/common-issue/common-errors/browser-spawn-failure",
        "https://www.browserstack.com/docs/percy/common-issue/asset-not-captured",
        "https://www.browserstack.com/docs/percy/common-issue/lazy-loading-elements",
        "https://www.browserstack.com/docs/percy/common-issue/hover-state",
        "https://www.browserstack.com/docs/percy/common-issue/handling-csp",
        "https://www.browserstack.com/docs/percy/common-issue/proxy-requests",
    ]
    return urls

def scrape_percy_docs():
    """Scrape Percy documentation from BrowserStack"""
    print("\n=== Scraping Percy Documentation ===")

    urls = get_documentation_urls()

    saved_count = 0
    for url in urls:
        content = download_page(url)
        if save_documentation(url, content):
            saved_count += 1
        time.sleep(1)  # Rate limiting

    return saved_count

def create_index():
    """Create comprehensive index file"""
    print("\n=== Creating Index ===")

    index_content = """# Percy Visual Testing Documentation Index

This directory contains comprehensive documentation for Percy, a visual testing and review platform by BrowserStack.

## Overview

Percy is an all-in-one visual testing and review platform that:
- Captures screenshots and DOM snapshots
- Compares against baseline images
- Detects visual regressions automatically
- Provides AI-powered analysis of visual changes
- Integrates with CI/CD pipelines
- Supports multiple testing frameworks

## Getting Started

- **First Percy Build**: Run your first visual test with Percy
- **SDK Workflow**: Understand how Percy SDKs work
- **Integration Guide**: Add Percy to your existing test suite

## Framework Integrations

Percy supports integration with:
- Cypress
- Playwright
- WebdriverIO
- Puppeteer
- Appium
- Selenium
- TestCafe
- Nightwatch
- Ember
- Gatsby
- And more...

## Key Features

### Visual Testing
- DOM snapshot capture during tests
- Multi-browser rendering
- Responsive testing across screen widths
- Pixel-perfect UI validation
- AI-powered change detection

### Build Results
- Visual change review interface
- Approval/rejection workflow
- Diff highlighting and comparison
- Snapshot grouping and organization
- Comments and collaboration
- Root cause analysis

### Advanced Features
- Figma design integration
- Percy-specific CSS for ignoring regions
- Git baseline management
- Layout testing
- Responsive testing
- Performance optimization

### CI/CD Integration
- GitHub, GitLab, Bitbucket integration
- Automatic build creation
- PR status checks
- Build finalization control

## API Reference

- **Authentication**: Token-based API authentication
- **REST API**: Full API documentation
- **Error Codes**: Common error messages and troubleshooting

## Common Issues & Troubleshooting

Percy documentation covers solutions for:
- Missing or invalid Percy tokens
- Browser spawn/launch failures
- Asset discovery and loading issues
- CORS and CSP handling
- Lazy loading elements
- Proxy and network issues
- Encoding and character issues
- And many more...

## Documentation Structure

- `index.md` - This file
- `*-getting-started*.md` - Framework integration guides
- `build-results-*.md` - Build review and management
- `api-reference-*.md` - API documentation
- `common-issue-*.md` - Troubleshooting guides
- `advanced-snapshots-*.md` - Advanced snapshot techniques
- `baseline-management-*.md` - Git baseline strategies
- `figma-*.md` - Figma design integration
- `ci-cd-*.md` - CI/CD pipeline integration

## Key Resources

- **Official Site**: https://percy.io/
- **BrowserStack Percy Docs**: https://www.browserstack.com/docs/percy/
- **Percy GitHub**: https://github.com/percy/
- **Discord Community**: BrowserStack Discord server

## Quick Links

### Setup & Configuration
1. Create a Percy account at percy.io
2. Generate a project token
3. Install the appropriate SDK for your framework
4. Add visual checks to your tests
5. Run your tests and review results

### Popular Integrations
- [Cypress Integration](cypress-getting-started.md)
- [Playwright Integration](playwright-getting-started.md)
- [WebdriverIO Integration](webdriverio-getting-started.md)
- [Appium/Selenium Integration](appium-get-started.md)

### Essential Concepts
- [What is a Percy Snapshot](get-started-first-percy-build.md)
- [Build Review Interface](build-results-overview.md)
- [API Authentication](api-reference-authentication.md)
- [Git Baseline Management](baseline-management-git.md)

## Notes

- Percy is owned and operated by BrowserStack
- Visual tests run in Percy's cloud infrastructure
- Support available through BrowserStack support channels
- Free tier available for getting started
- Pricing based on screenshot volume and team size

## Last Updated

2026-01-01

---

For the latest documentation and updates, visit [BrowserStack Percy Docs](https://www.browserstack.com/docs/percy/)
"""

    index_file = OUTPUT_DIR / 'INDEX.md'
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(index_content)

    print(f"Created index: {index_file}")

def create_readme():
    """Create README for the Percy documentation"""
    readme_content = """# Percy Documentation

Complete documentation for Percy visual testing platform.

## About Percy

Percy is a comprehensive visual testing solution that integrates with your existing test automation frameworks to catch visual bugs before they reach production.

## What's Included

This directory contains:
- Integration guides for multiple testing frameworks
- API reference documentation
- Build results and review features guide
- Troubleshooting and common issues
- Advanced snapshot techniques
- CI/CD integration guides
- Figma design comparison guides

## Quick Start

1. **Sign up** at [percy.io](https://percy.io/)
2. **Choose your framework** from the integration guides
3. **Install the SDK** for your framework
4. **Add visual checks** to your test suite
5. **Run and review** visual test results

## Framework Support

Percy supports:
- Cypress
- Playwright
- WebdriverIO
- Puppeteer
- Selenium/Appium
- TestCafe
- Ember
- Gatsby
- And many more...

## Key Features

- **Visual Regression Testing**: Automatically detect visual changes
- **AI-Powered Analysis**: Get intelligent summaries of visual changes
- **Responsive Testing**: Test across multiple screen sizes
- **Team Collaboration**: Comment and approve changes together
- **CI/CD Integration**: Seamless pipeline integration
- **Figma Sync**: Compare with design files
- **Git Baseline Management**: Smart baseline management strategies

## Documentation Files

- `INDEX.md` - Comprehensive index with quick links
- `README.md` - This file
- Integration guides for each supported framework
- API reference and authentication docs
- Build results and review features
- Troubleshooting and common issues
- Advanced techniques and best practices

## Support

- **Documentation**: https://www.browserstack.com/docs/percy/
- **Official Site**: https://percy.io/
- **GitHub**: https://github.com/percy/
- **BrowserStack Support**: support.browserstack.com

## License

This documentation is extracted from BrowserStack's official Percy documentation.
See individual files for source attribution.
"""

    readme_file = OUTPUT_DIR / 'README.md'
    with open(readme_file, 'w', encoding='utf-8') as f:
        f.write(readme_content)

    print(f"Created README: {readme_file}")

if __name__ == '__main__':
    print("Starting Percy documentation scraper...")
    print(f"Output directory: {OUTPUT_DIR}")

    saved = scrape_percy_docs()
    create_readme()
    create_index()

    # Count and summarize
    files = list(OUTPUT_DIR.glob('*.md'))
    total_size = sum(f.stat().st_size for f in files) / (1024 * 1024)

    print(f"\n=== Summary ===")
    print(f"Total files: {len(files)}")
    print(f"Total size: {total_size:.2f} MB")
    print(f"Output directory: {OUTPUT_DIR}")
    print(f"Documentation successfully scraped and saved!")
