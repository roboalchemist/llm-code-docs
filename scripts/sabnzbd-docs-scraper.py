#!/usr/bin/env python3
"""
SABnzbd Documentation Scraper

Scrapes SABnzbd documentation from the official wiki at sabnzbd.org.
Focuses on API documentation, configuration, and usage guides.

SABnzbd is an open-source Usenet binary newsreader / download automation tool.
"""

import os
import sys
from pathlib import Path
import subprocess
import urllib.request
import urllib.error
from html.parser import HTMLParser
import html2text
import time

# Wiki pages to scrape (path relative to sabnzbd.org/wiki/)
WIKI_PAGES = {
    # API Documentation (Priority 1)
    "configuration/4.5/api": "01-api-reference.md",

    # Configuration (Priority 2)
    "configuration/4.5/configure": "02-configuration-main.md",
    "configuration/4.5/general": "03-configuration-general.md",
    "configuration/4.5/folders": "04-configuration-folders.md",
    "configuration/4.5/servers": "05-configuration-servers.md",
    "configuration/4.5/categories": "06-configuration-categories.md",
    "configuration/4.5/sorting": "07-configuration-sorting.md",
    "configuration/4.5/switches": "08-configuration-switches.md",
    "configuration/4.5/notifications": "09-configuration-notifications.md",
    "configuration/4.5/scheduling": "10-configuration-scheduling.md",
    "configuration/4.5/rss": "11-configuration-rss.md",
    "configuration/4.5/special": "12-configuration-special.md",

    # Introduction & Usage
    "introduction/quick-setup": "20-introduction-quicksetup.md",
    "introduction/usage": "21-introduction-usage.md",
    "introduction/nzb-sources": "22-introduction-nzb-sources.md",
    "introduction/howto": "23-introduction-howto.md",
    "introduction/known-issues": "24-introduction-known-issues.md",

    # Installation & Setup
    "installation/install-windows": "30-install-windows.md",
    "installation/install-macos": "31-install-macos.md",
    "installation/install-unix": "32-install-unix.md",
    "installation/install-nas": "33-install-nas.md",
    "installation/install-off-modules": "34-install-from-source.md",

    # Scripts
    "configuration/4.5/scripts/pre-queue-scripts": "40-scripts-pre-queue.md",
    "configuration/4.5/scripts/post-processing-scripts": "41-scripts-post-processing.md",
    "configuration/4.5/scripts/notification-scripts": "42-scripts-notification.md",

    # Advanced Topics
    "advanced/highspeed-downloading": "50-advanced-highspeed.md",
    "advanced/https": "51-advanced-https.md",
    "advanced/command-line-parameters": "52-advanced-command-line.md",
    "advanced/directory-setup": "53-advanced-directory-setup.md",
    "advanced/unix-permissions": "54-advanced-unix-permissions.md",
    "advanced/password-protected-rars": "55-advanced-rar-password.md",
    "advanced/ipv6": "56-advanced-ipv6.md",
    "advanced/certificate-errors": "57-advanced-ssl-tls.md",
    "advanced/ssl-ciphers": "58-advanced-ssl-ciphers.md",
    "advanced/sabnzbd-as-a-windows-service": "59-advanced-windows-service.md",
    "advanced/android": "60-advanced-android.md",

    # Other
    "extensions-for-sabnzbd": "70-extensions.md",
    "faq": "71-faq.md",
}


class HTMLToMarkdownParser(HTMLParser):
    """Parse HTML content and convert to markdown."""

    def __init__(self):
        super().__init__()
        self.text = []
        self.in_code = False
        self.in_pre = False
        self.in_table = False

    def handle_starttag(self, tag, attrs):
        if tag == 'code' or tag == 'pre':
            self.in_code = True

    def handle_endtag(self, tag):
        if tag == 'code' or tag == 'pre':
            self.in_code = False

    def handle_data(self, data):
        self.text.append(data)


def scrape_wiki_page(page_path):
    """Scrape a single wiki page from sabnzbd.org."""
    try:
        url = f"https://sabnzbd.org/wiki/{page_path}"
        print(f"  Fetching: {page_path}...", end=" ", flush=True)

        # Set a User-Agent to avoid being blocked
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
        }

        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=15) as response:
                html_content = response.read().decode('utf-8')
                print("✓")

                # Convert HTML to Markdown using html2text
                h = html2text.HTML2Text()
                h.body_width = 0  # No wrapping
                h.ignore_links = False
                h.ignore_images = False
                markdown_content = h.handle(html_content)
                return markdown_content

        except urllib.error.HTTPError as e:
            if e.code == 404:
                print("✗ (not found)")
                return None
            else:
                print(f"✗ (HTTP {e.code})")
                return None
        except urllib.error.URLError as e:
            print(f"✗ (connection error)")
            return None
        except Exception as e:
            print(f"✗ ({str(e)[:30]})")
            return None

        # Add delay to avoid rate limiting
        time.sleep(0.5)

    except Exception as e:
        print(f"  Error fetching {page_path}: {e}")
        return None


def write_markdown_file(output_dir, filename, content, source_url):
    """Write markdown content to a file with source header."""
    try:
        output_file = output_dir / filename

        # Create source header with link
        header = f"""# Source: {source_url}

"""

        # Clean up markdown content
        # Remove excessive whitespace and newlines
        lines = content.split('\n')
        cleaned_lines = []
        prev_empty = False

        for line in lines:
            is_empty = line.strip() == ''
            if is_empty and prev_empty:
                # Skip consecutive empty lines
                continue
            cleaned_lines.append(line)
            prev_empty = is_empty

        cleaned_content = '\n'.join(cleaned_lines)

        # Write to file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(header)
            f.write(cleaned_content)

        return True

    except Exception as e:
        print(f"    Error writing {filename}: {e}")
        return False


def create_index(output_dir):
    """Create an index document for the scraped documentation."""
    try:
        index_content = """# SABnzbd Documentation Index

SABnzbd is an open-source Usenet binary newsreader and automation tool that automates downloading NZBs from newsgroups.

## Quick Links

- **Official Website**: https://sabnzbd.org
- **GitHub Repository**: https://github.com/sabnzbd/sabnzbd
- **Forum**: https://forums.sabnzbd.org

## Documentation Structure

### API Documentation
1. **API Reference** - Complete REST API endpoints, authentication, and response formats
   - Queue functions (pause, resume, add, delete, priority management)
   - History functions (retrieve completed jobs, retry, statistics)
   - Status monitoring (CPU, disk space, server stats)
   - Configuration management and utilities

### Configuration
2. **General Settings** - Basic SABnzbd configuration
3. **Folder Configuration** - Directory paths for downloads and temporary files
4. **Server Configuration** - Usenet server setup and credentials
5. **Categories** - Job categorization and routing
6. **Sorting** - Post-processing job sorting rules
7. **Switches** - Feature toggles and performance settings

### Installation & Setup
8. **Windows Installation** - Windows-specific installation instructions
9. **macOS Installation** - macOS-specific installation instructions
10. **Linux Installation** - Linux distribution installation guides
11. **Quick Start Guide** - Getting started with SABnzbd

### Scripting & Automation
12. **Post-Processing Scripts** - Scripts that run after downloads complete
13. **Pre-Queue Scripts** - Scripts that filter/modify NZBs before queueing

### Advanced Topics
14. **HTTPS/SSL Setup** - Secure web interface configuration
15. **Command Line Options** - CLI parameters and startup configuration
16. **High-Speed Tweaks** - Performance optimization settings

## Common Use Cases

### Integration with Sonarr/Radarr
SABnzbd serves as the download engine for Sonarr (TV) and Radarr (Movies):
- Configure API key in SABnzbd settings
- Use API endpoint: `http://host:port/api`
- Support for job categories, post-processing scripts, and priority control

### Automation & Monitoring
- Use the REST API to programmatically manage downloads
- Monitor queue status and history
- Implement custom post-processing workflows with scripts
- Setup RSS feeds for automatic NZB discovery

## Version Information

This documentation is for SABnzbd 4.5 (latest stable version at time of scraping).
"""

        index_file = output_dir / "00-index.md"
        with open(index_file, 'w', encoding='utf-8') as f:
            f.write(index_content)

        return True

    except Exception as e:
        print(f"Error creating index: {e}")
        return False


def main():
    """Main function to scrape SABnzbd documentation."""
    print("=" * 70)
    print("SABnzbd Documentation Scraper")
    print("=" * 70)
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "web-scraped" / "sabnzbd"

    print(f"Source: sabnzbd.org/wiki/")
    print(f"Output directory: {output_dir}")
    print()

    # Remove existing output directory if it exists
    if output_dir.exists():
        print("Removing existing output directory...")
        import shutil
        shutil.rmtree(output_dir)

    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)

    # Create index first
    print("Creating documentation index...")
    if not create_index(output_dir):
        print("Warning: Failed to create index")
    print()

    # Scrape wiki pages
    print("Scraping wiki pages...")
    scraped_count = 0
    failed_count = 0

    for page_path, filename in sorted(WIKI_PAGES.items()):
        content = scrape_wiki_page(page_path)

        if content:
            source_url = f"https://sabnzbd.org/wiki/{page_path}"
            if write_markdown_file(output_dir, filename, content, source_url):
                scraped_count += 1
            else:
                failed_count += 1
        else:
            failed_count += 1

    print()
    print(f"Scraped: {scraped_count} pages")
    print(f"Failed: {failed_count} pages")
    print()

    # Verify extraction
    print("Verifying extraction...")
    if not output_dir.exists():
        print("  Error: Output directory was not created")
        sys.exit(1)

    markdown_files = list(output_dir.glob("**/*.md"))
    total_size = sum(f.stat().st_size for f in markdown_files)

    print(f"  Total files: {len(markdown_files)}")
    print(f"  Total size: {total_size:,} bytes ({total_size/1024/1024:.2f} MB)")

    if len(markdown_files) == 0:
        print("\n  Error: No files found in output directory")
        sys.exit(1)

    # List main files
    print("\n  Documentation files:")
    for md_file in sorted(markdown_files):
        file_size = md_file.stat().st_size
        print(f"    - {md_file.relative_to(output_dir)} ({file_size:,} bytes)")

    print()
    print("=" * 70)
    print("Extraction Complete")
    print("=" * 70)
    print(f"Output: {output_dir}")
    print()


if __name__ == "__main__":
    main()
