#!/usr/bin/env python3
"""
Scraper for Microsoft Azure IoT Edge Documentation.
Output: docs/web-scraped/azure-iot-edge/

Extracts documentation from learn.microsoft.com including:
- Getting started guides
- How-to guides
- API references
- Tutorials and quickstarts
"""

import requests
from pathlib import Path
from urllib.parse import urljoin, urlparse
import re
from html.parser import HTMLParser
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "web-scraped" / "azure-iot-edge"
BASE_URL = "https://learn.microsoft.com/en-us/azure/iot-edge"
SESSION = requests.Session()
SESSION.headers.update({
    'User-Agent': 'Mozilla/5.0 (compatible; DocumentationBot/1.0)'
})

# Rate limiting
RATE_LIMIT_DELAY = 0.5  # seconds between requests


class DocumentationExtractor(HTMLParser):
    """Extract main content from Azure documentation pages."""

    def __init__(self):
        super().__init__()
        self.in_main = False
        self.in_script = False
        self.in_style = False
        self.content = []
        self.title = ""

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if tag == 'title':
            pass
        elif tag in ['script', 'style']:
            self.__dict__[f'in_{tag}'] = True
        elif tag in ['main', 'article'] or (tag == 'div' and 'main' in attrs_dict.get('class', '')):
            self.in_main = True
        elif tag == 'h1' and not self.in_script and not self.in_style:
            self.content.append('\n# ')
        elif tag in ['h2'] and not self.in_script and not self.in_style:
            self.content.append('\n## ')
        elif tag in ['h3'] and not self.in_script and not self.in_style:
            self.content.append('\n### ')
        elif tag in ['h4'] and not self.in_script and not self.in_style:
            self.content.append('\n#### ')
        elif tag == 'p' and not self.in_script and not self.in_style:
            self.content.append('\n')
        elif tag == 'code' and not self.in_script and not self.in_style:
            self.content.append('`')
        elif tag == 'pre' and not self.in_script and not self.in_style:
            self.content.append('\n```\n')
        elif tag in ['li', 'dd'] and not self.in_script and not self.in_style:
            self.content.append('\n- ')
        elif tag == 'br' and not self.in_script and not self.in_style:
            self.content.append('\n')
        elif tag == 'strong' and not self.in_script and not self.in_style:
            self.content.append('**')
        elif tag == 'em' and not self.in_script and not self.in_style:
            self.content.append('*')
        elif tag == 'a' and not self.in_script and not self.in_style:
            self.content.append('[')

    def handle_endtag(self, tag):
        if tag in ['script', 'style']:
            self.__dict__[f'in_{tag}'] = False
        elif tag in ['main', 'article']:
            self.in_main = False
        elif tag == 'code' and not self.in_script and not self.in_style:
            self.content.append('`')
        elif tag == 'pre' and not self.in_script and not self.in_style:
            self.content.append('\n```\n')
        elif tag in ['p', 'li', 'dd', 'h1', 'h2', 'h3', 'h4']:
            self.content.append('\n')
        elif tag == 'strong' and not self.in_script and not self.in_style:
            self.content.append('**')
        elif tag == 'em' and not self.in_script and not self.in_style:
            self.content.append('*')
        elif tag == 'a' and not self.in_script and not self.in_style:
            self.content.append(']')

    def handle_data(self, data):
        if not self.in_script and not self.in_style:
            text = data.strip()
            if text:
                self.content.append(text + ' ')

    def get_text(self):
        text = ''.join(self.content)
        # Clean up multiple newlines
        while '\n\n\n' in text:
            text = text.replace('\n\n\n', '\n\n')
        return text.strip()


def fetch_page(url):
    """Fetch and extract text from a page."""
    try:
        logger.info(f"  Fetching: {url}")
        response = SESSION.get(url, timeout=10)
        response.raise_for_status()

        parser = DocumentationExtractor()
        parser.feed(response.text)

        return parser.get_text()
    except Exception as e:
        logger.error(f"  Error fetching {url}: {e}")
        return None


def get_documentation_pages():
    """Get list of Azure IoT Edge documentation pages to scrape."""
    pages = {
        # Overview and Getting Started
        "overview.md": f"{BASE_URL}/about-iot-edge",
        "quickstart-linux.md": f"{BASE_URL}/quickstart-linux",
        "quickstart-windows.md": f"{BASE_URL}/quickstart-windows",

        # Concepts
        "architecture.md": f"{BASE_URL}/iot-edge-runtime",
        "edge-modules.md": f"{BASE_URL}/about-modules",
        "iot-edge-dev-environment.md": f"{BASE_URL}/development-environment",

        # Installation and Setup
        "install-linux.md": f"{BASE_URL}/how-to-provision-single-device-linux-symmetric",
        "install-windows.md": f"{BASE_URL}/how-to-provision-single-device-windows",
        "install-linux-on-windows.md": f"{BASE_URL}/how-to-install-iot-edge-on-linux",

        # Development
        "develop-modules.md": f"{BASE_URL}/module-development",
        "debug-modules.md": f"{BASE_URL}/how-to-debug-modules",
        "develop-custom-modules.md": f"{BASE_URL}/how-to-develop-csharp-module",

        # Deployment
        "deploy-modules.md": f"{BASE_URL}/how-to-deploy-modules-portal",
        "deployment-manifests.md": f"{BASE_URL}/module-composition",
        "monitor-module-health.md": f"{BASE_URL}/how-to-monitor-module-replicas",

        # Troubleshooting and Management
        "troubleshoot.md": f"{BASE_URL}/troubleshoot",
        "device-management.md": f"{BASE_URL}/how-to-update-iot-edge",
        "offline-capabilities.md": f"{BASE_URL}/offline-capabilities",
    }
    return pages


def create_index():
    """Create an index markdown file."""
    index_content = """# Azure IoT Edge Documentation

## Overview
Microsoft Azure IoT Edge is a fully managed service that delivers cloud analytics and custom business logic to devices through containerized modules. It brings the power of cloud computing to the edge, enabling you to process and analyze data closer to the source.

## Documentation Sections

### Getting Started
- [Overview and Architecture](overview.md)
- [Quickstart for Linux](quickstart-linux.md)
- [Quickstart for Windows](quickstart-windows.md)
- [Development Environment Setup](iot-edge-dev-environment.md)

### Core Concepts
- [IoT Edge Architecture](architecture.md)
- [About Modules](edge-modules.md)
- [Deployment Manifests](deployment-manifests.md)

### Installation and Configuration
- [Install on Linux](install-linux.md)
- [Install on Windows](install-windows.md)
- [IoT Edge for Linux on Windows](install-linux-on-windows.md)

### Module Development
- [Module Development Guide](develop-modules.md)
- [Develop Custom C# Modules](develop-custom-modules.md)
- [Debug Modules](debug-modules.md)

### Deployment and Management
- [Deploy Modules](deploy-modules.md)
- [Monitor Module Health](monitor-module-health.md)
- [Device Management](device-management.md)

### Advanced Topics
- [Troubleshooting](troubleshoot.md)
- [Offline Capabilities](offline-capabilities.md)

## Official Documentation
For the complete and latest documentation, visit: [https://learn.microsoft.com/en-us/azure/iot-edge/](https://learn.microsoft.com/en-us/azure/iot-edge/)

---
Source: https://learn.microsoft.com/en-us/azure/iot-edge/
"""
    return index_content


def main():
    """Main function to download all Azure IoT Edge documentation."""
    print("=" * 70)
    print("Azure IoT Edge Documentation Scraper")
    print("=" * 70)
    print()

    # Create output directory
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print(f"Output directory: {OUTPUT_DIR}")
    print()

    # Get documentation pages
    pages = get_documentation_pages()

    successful = 0
    failed = 0
    start_time = time.time()

    print(f"Scraping {len(pages)} documentation pages...")
    print()

    for idx, (filename, url) in enumerate(pages.items(), 1):
        print(f"[{idx:2d}/{len(pages)}] ", end="")

        content = fetch_page(url)

        if content:
            # Add metadata header
            header = f"""# Source: {url}

"""
            content = header + content

            # Save to file
            output_path = OUTPUT_DIR / filename
            try:
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Saved: {filename}")
                successful += 1
            except Exception as e:
                print(f"Error saving {filename}: {e}")
                failed += 1
        else:
            print(f"Failed: {filename}")
            failed += 1

        # Rate limiting
        time.sleep(RATE_LIMIT_DELAY)

    # Create index file
    index_path = OUTPUT_DIR / "README.md"
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(create_index())
    print()
    print(f"Created index: README.md")

    elapsed = time.time() - start_time

    print()
    print("=" * 70)
    print("Download Summary")
    print("=" * 70)
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    print(f"Time: {elapsed:.1f} seconds")
    print(f"Output: {OUTPUT_DIR}")

    # Calculate total size
    total_size = sum(f.stat().st_size for f in OUTPUT_DIR.glob("*") if f.is_file())
    print(f"Total size: {total_size:,} bytes ({total_size/1024:.1f} KB)")

    print()
    if failed > 0:
        print(f"Warning: {failed} files failed to download")
        return 1
    else:
        print("All documentation downloaded successfully!")
        return 0


if __name__ == "__main__":
    exit(main())
