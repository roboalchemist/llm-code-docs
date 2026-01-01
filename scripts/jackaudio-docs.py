#!/usr/bin/env python3
"""
Scraper for JACK Audio documentation.
Output: docs/web-scraped/jackaudio/

This scraper extracts the main documentation from jackaudio.org
and converts it to markdown format.
"""
import os
import sys
import requests
from pathlib import Path
from html2text import HTML2Text
from urllib.parse import urljoin, urlparse
import json
from datetime import datetime

OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "web-scraped" / "jackaudio"

# Create output directory
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# List of important URLs to scrape from jackaudio.org
URLS_TO_SCRAPE = [
    "https://jackaudio.org/",  # Home page
    "https://jackaudio.org/api/",  # API documentation
    "https://jackaudio.org/developers.html",
    "https://jackaudio.org/community.html",
    "https://jackaudio.org/faq/",
    "https://jackaudio.org/faq/about.html",
    "https://jackaudio.org/faq/linux_rt_config.html",
    "https://jackaudio.org/faq/jack_on_windows.html",
    "https://jackaudio.org/faq/pulseaudio_and_jack.html",
    "https://jackaudio.org/faq/making_a_jack_app.html",
    "https://jackaudio.org/faq/netjack.html",
    "https://jackaudio.org/faq/routing_alsa.html",
    "https://jackaudio.org/metadata/",
    "https://jackaudio.org/applications/",
]

# Use the cloned repository files as primary source
REPO_DIR = Path("/tmp/jackaudio.github.com")

def convert_html_to_markdown(html_content, url):
    """Convert HTML to markdown using html2text."""
    h = HTML2Text()
    h.ignore_links = False
    h.body_width = 0
    markdown = h.handle(html_content)
    return markdown

def extract_markdown_files():
    """Extract markdown files directly from the cloned repository."""
    markdown_files = {}
    
    # Important markdown files to extract
    important_files = [
        "index.md",
        "community.md",
        "developers.md",
        "faq/index.md",
        "faq/about.md",
        "faq/build_info.md",
        "faq/comparing_jack.md",
        "faq/device_naming.md",
        "faq/device_support.md",
        "faq/documentation.md",
        "faq/gstreamer_via_jack.md",
        "faq/jack_on_windows.md",
        "faq/linux_group_sched.md",
        "faq/linux_rt_config.md",
        "faq/macbook_distortion.md",
        "faq/making_a_jack_app.md",
        "faq/multiple_devices.md",
        "faq/netjack.md",
        "faq/no_extra_latency.md",
        "faq/persistent_connections.md",
        "faq/pulseaudio_and_jack.md",
        "faq/realtime_vs_realtime_kernel.md",
        "faq/routing_alsa.md",
        "faq/routing_audacious.md",
        "faq/routing_flash.md",
        "faq/routing_phonon.md",
        "metadata/index.md",
        "metadata/connected/index.md",
        "metadata/event-types/index.md",
        "metadata/hardware/index.md",
        "metadata/icon-large/index.md",
        "metadata/icon-name/index.md",
        "metadata/icon-small/index.md",
        "metadata/order/index.md",
        "metadata/port-group/index.md",
        "metadata/pretty-name/index.md",
        "metadata/signal-type/index.md",
        "applications/index.md",
        "downloads/index.md",
    ]
    
    for file_path in important_files:
        full_path = REPO_DIR / file_path
        if full_path.exists():
            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read()
            # Create relative path in output
            output_name = file_path.replace('/', '_').replace('_index.md', '.md')
            if output_name.endswith('_'):
                output_name = output_name[:-1] + '.md'
            markdown_files[output_name] = content
            print(f"Extracted: {file_path}")
    
    return markdown_files

def scrape_html_api_docs():
    """Scrape and convert key HTML API documentation pages."""
    html_files = {}
    
    api_html_files = [
        "api/index.html",
        "api/modules.html",
        "api/pages.html",
        "api/globals_func.html",
        "api/group__ClientFunctions.html",
        "api/group__ClientCallbacks.html",
        "api/group__PortFunctions.html",
        "api/group__MIDIAPI.html",
        "api/group__TransportControl.html",
    ]
    
    h = HTML2Text()
    h.ignore_links = False
    h.body_width = 0
    
    for file_path in api_html_files:
        full_path = REPO_DIR / file_path
        if full_path.exists():
            with open(full_path, 'r', encoding='utf-8') as f:
                html_content = f.read()
            try:
                markdown = h.handle(html_content)
                # Create output filename
                output_name = file_path.replace('/', '_').replace('.html', '.md')
                html_files[output_name] = markdown
                print(f"Converted: {file_path}")
            except Exception as e:
                print(f"Error converting {file_path}: {e}", file=sys.stderr)
    
    return html_files

def save_documentation(markdown_files):
    """Save markdown files to output directory."""
    for filename, content in markdown_files.items():
        output_path = OUTPUT_DIR / filename
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Add source header
        header = f"# Source: https://jackaudio.org/\n\n"
        full_content = header + content
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(full_content)
        print(f"Saved: {output_path}")

def main():
    """Main scraper function."""
    print("Scraping JACK Audio documentation...")
    
    all_files = {}
    
    # Extract markdown files from repository
    markdown_files = extract_markdown_files()
    all_files.update(markdown_files)
    
    # Convert HTML API docs
    html_files = scrape_html_api_docs()
    all_files.update(html_files)
    
    # Save all documentation
    save_documentation(all_files)
    
    print(f"\nTotal files scraped: {len(all_files)}")
    print(f"Output directory: {OUTPUT_DIR}")
    print(f"Directory size: {sum(f.stat().st_size for f in OUTPUT_DIR.rglob('*') if f.is_file()) / 1024:.1f} KB")

if __name__ == "__main__":
    main()
