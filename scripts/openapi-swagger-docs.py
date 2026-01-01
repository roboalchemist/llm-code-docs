#!/usr/bin/env python3
"""
Scraper for OpenAPI/Swagger documentation.
Extracts documentation from:
1. swagger.io documentation
2. OpenAPI Specification repository (versions folder)
3. Official OpenAPI specification details

Output: docs/web-scraped/openapi-swagger/
"""

import requests
from pathlib import Path
import json
import re
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import time

OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "web-scraped" / "openapi-swagger"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Track downloaded files to avoid duplicates
downloaded_urls = set()

def sanitize_filename(url):
    """Convert URL to safe filename"""
    parsed = urlparse(url)
    path = parsed.path.strip('/')
    if not path:
        path = 'index'
    # Remove query parameters and anchors
    path = path.split('?')[0].split('#')[0]
    # Replace slashes with dashes
    filename = path.replace('/', '-').replace('.html', '')
    return filename[:100] + '.md'

def extract_markdown_from_html(html_content, base_url=''):
    """Convert HTML to basic markdown"""
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Remove script and style elements
    for script in soup(['script', 'style', 'nav', 'footer']):
        script.decompose()
    
    # Get main content
    main_content = soup.find('main') or soup.find('article') or soup.find(class_='main')
    if main_content:
        content_html = str(main_content)
    else:
        content_html = str(soup)
    
    # Basic HTML to Markdown conversion
    markdown = convert_html_to_markdown(content_html)
    return markdown.strip()

def convert_html_to_markdown(html):
    """Simple HTML to Markdown converter"""
    # This is a simplified version - for production use pandoc or similar
    soup = BeautifulSoup(html, 'html.parser')
    
    # Extract headings, paragraphs, lists, and code blocks
    markdown_parts = []
    
    for elem in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'li', 'code', 'pre', 'a']):
        if elem.name.startswith('h'):
            level = int(elem.name[1])
            text = elem.get_text(strip=True)
            if text:
                markdown_parts.append(f"{'#' * level} {text}\n")
        elif elem.name == 'p':
            text = elem.get_text(strip=True)
            if text:
                markdown_parts.append(f"{text}\n\n")
        elif elem.name == 'li':
            text = elem.get_text(strip=True)
            if text:
                markdown_parts.append(f"- {text}\n")
        elif elem.name == 'pre':
            text = elem.get_text()
            if text:
                markdown_parts.append(f"```\n{text}```\n\n")
        elif elem.name == 'code':
            text = elem.get_text(strip=True)
            if text and len(text) < 100:
                markdown_parts.append(f"`{text}` ")
        elif elem.name == 'a':
            text = elem.get_text(strip=True)
            href = elem.get('href', '')
            if text and href:
                markdown_parts.append(f"[{text}]({href}) ")
    
    return ''.join(markdown_parts)

def download_page(url, base_url='https://swagger.io'):
    """Download a single page and convert to markdown"""
    if url in downloaded_urls:
        return None
    
    try:
        # Normalize URL
        if not url.startswith('http'):
            url = urljoin(base_url, url)
        
        # Skip non-swagger.io URLs except specific allowed ones
        parsed = urlparse(url)
        if parsed.netloc not in ['swagger.io', 'github.com', 'raw.githubusercontent.com']:
            return None
        
        downloaded_urls.add(url)
        
        print(f"Downloading: {url}")
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        # Extract markdown
        if 'text/html' in response.headers.get('content-type', ''):
            markdown = extract_markdown_from_html(response.text, url)
        else:
            markdown = response.text
        
        # Add source header
        markdown = f"# Source: {url}\n\n{markdown}"
        
        return markdown
    
    except Exception as e:
        print(f"Error downloading {url}: {e}")
        return None

def save_documentation(title, url, content):
    """Save documentation to file"""
    if content:
        filename = sanitize_filename(url)
        filepath = OUTPUT_DIR / filename
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Saved: {filepath}")
        return filepath
    return None

def scrape_swagger_docs():
    """Scrape swagger.io documentation"""
    print("\n=== Scraping Swagger.io Documentation ===")
    
    # Main documentation pages
    swagger_urls = [
        'https://swagger.io/docs/',
        'https://swagger.io/docs/specification/what-is-openapi/',
        'https://swagger.io/docs/specification/basic-structure/',
        'https://swagger.io/docs/specification/info-object/',
        'https://swagger.io/docs/specification/paths-and-operations/',
        'https://swagger.io/docs/specification/describing-parameters/',
        'https://swagger.io/docs/specification/request-bodies/',
        'https://swagger.io/docs/specification/responses/',
        'https://swagger.io/docs/specification/authentication/',
        'https://swagger.io/docs/specification/serialization/',
        'https://swagger.io/docs/open-source-tools/swagger-ui/usage-oauth2/',
        'https://swagger.io/docs/open-source-tools/swagger-ui/introduction/',
        'https://swagger.io/docs/open-source-tools/swagger-codegen/codegen-v3/about',
        'https://swagger.io/docs/open-source-tools/swagger-codegen/codegen-v3/generators',
    ]
    
    for url in swagger_urls:
        content = download_page(url)
        if content:
            save_documentation('Swagger', url, content)
        time.sleep(1)

def scrape_openapi_spec():
    """Scrape OpenAPI Specification from GitHub"""
    print("\n=== Scraping OpenAPI Specification ===")
    
    base_url = 'https://raw.githubusercontent.com/OAI/OpenAPI-Specification/main'
    
    # Key specification documents
    spec_files = [
        'README.md',
        'CONTRIBUTING.md',
        'SECURITY_CONSIDERATIONS.md',
        'versions/3.1.0.md',
        'versions/3.0.3.md',
        'versions/2.0.md',
    ]
    
    for file_path in spec_files:
        url = f"{base_url}/{file_path}"
        try:
            print(f"Downloading: {url}")
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            
            markdown = f"# Source: {url}\n\n{response.text}"
            
            filename = file_path.replace('/', '-').replace('.md', '') + '.md'
            filepath = OUTPUT_DIR / filename
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(markdown)
            
            print(f"Saved: {filepath}")
            
        except Exception as e:
            print(f"Error downloading {url}: {e}")
        
        time.sleep(1)

def create_index():
    """Create index file"""
    print("\n=== Creating Index ===")
    
    index_content = """# OpenAPI/Swagger Documentation Index

This directory contains comprehensive documentation for OpenAPI and Swagger tools.

## Overview

- **OpenAPI Specification**: The standard for describing REST APIs
- **Swagger Tools**: Open-source tools for working with OpenAPI specifications
  - Swagger UI: Interactive API documentation
  - Swagger Editor: API design and editing
  - Swagger Codegen: Generate client libraries and server stubs

## Documentation Sources

- **Swagger.io Documentation**: Official swagger.io docs and guides
- **OpenAPI Specification Repository**: Official OpenAPI spec versions and governance
- **Tool Documentation**: Usage guides for Swagger UI, Editor, and Codegen

## Files

### OpenAPI Specification
- `README.md` - OpenAPI specification overview
- `CONTRIBUTING.md` - Contribution guidelines
- `SECURITY_CONSIDERATIONS.md` - Security best practices

### Specification Versions
- `versions-3-1-0.md` - OpenAPI 3.1.0 specification
- `versions-3-0-3.md` - OpenAPI 3.0.3 specification
- `versions-2-0.md` - Swagger 2.0 specification

### Swagger Documentation Pages
Various pages covering:
- Specification basics and structure
- Parameters, request bodies, responses
- Authentication and security
- API serialization
- Tool usage (UI, Editor, Codegen)

## Quick Links

- [OpenAPI Specification](https://spec.openapis.org/)
- [Swagger.io](https://swagger.io/)
- [Swagger UI GitHub](https://github.com/swagger-api/swagger-ui)
- [Swagger Editor GitHub](https://github.com/swagger-api/swagger-editor)
- [Swagger Codegen GitHub](https://github.com/swagger-api/swagger-codegen)
"""
    
    index_file = OUTPUT_DIR / 'INDEX.md'
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(index_content)
    
    print(f"Created: {index_file}")

if __name__ == '__main__':
    print("Starting OpenAPI/Swagger documentation scraper...")
    print(f"Output directory: {OUTPUT_DIR}")
    
    scrape_openapi_spec()
    scrape_swagger_docs()
    create_index()
    
    # Count files
    files = list(OUTPUT_DIR.glob('*.md'))
    total_size = sum(f.stat().st_size for f in files) / (1024 * 1024)
    
    print(f"\n=== Summary ===")
    print(f"Total files: {len(files)}")
    print(f"Total size: {total_size:.2f} MB")
    print(f"Output directory: {OUTPUT_DIR}")
