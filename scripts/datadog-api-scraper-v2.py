#!/usr/bin/env python3
"""
Improved scraper for Datadog API documentation.
Uses better HTML extraction with focus on main content.
Output: docs/web-scraped/datadog-api/
"""
import subprocess
import re
from pathlib import Path
import time

OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "web-scraped" / "datadog-api"

# All Datadog API sections
API_SECTIONS = [
    ("action-connection", "https://docs.datadoghq.com/api/latest/action-connection/"),
    ("actions-datastores", "https://docs.datadoghq.com/api/latest/actions-datastores/"),
    ("agentless-scanning", "https://docs.datadoghq.com/api/latest/agentless-scanning/"),
    ("api-management", "https://docs.datadoghq.com/api/latest/api-management/"),
    ("apm", "https://docs.datadoghq.com/api/latest/apm/"),
    ("apm-retention-filters", "https://docs.datadoghq.com/api/latest/apm-retention-filters/"),
    ("app-builder", "https://docs.datadoghq.com/api/latest/app-builder/"),
    ("application-security", "https://docs.datadoghq.com/api/latest/application-security/"),
    ("audit", "https://docs.datadoghq.com/api/latest/audit/"),
    ("authn-mappings", "https://docs.datadoghq.com/api/latest/authn-mappings/"),
    ("aws-integration", "https://docs.datadoghq.com/api/latest/aws-integration/"),
    ("azure-integration", "https://docs.datadoghq.com/api/latest/azure-integration/"),
    ("case-management", "https://docs.datadoghq.com/api/latest/case-management/"),
    ("ci-visibility-pipelines", "https://docs.datadoghq.com/api/latest/ci-visibility-pipelines/"),
    ("cloud-cost-management", "https://docs.datadoghq.com/api/latest/cloud-cost-management/"),
    ("dashboards", "https://docs.datadoghq.com/api/latest/dashboards/"),
    ("downtimes", "https://docs.datadoghq.com/api/latest/downtimes/"),
    ("error-tracking", "https://docs.datadoghq.com/api/latest/error-tracking/"),
    ("events", "https://docs.datadoghq.com/api/latest/events/"),
    ("gcp-integration", "https://docs.datadoghq.com/api/latest/gcp-integration/"),
    ("hosts", "https://docs.datadoghq.com/api/latest/hosts/"),
    ("incidents", "https://docs.datadoghq.com/api/latest/incidents/"),
    ("key-management", "https://docs.datadoghq.com/api/latest/key-management/"),
    ("logs", "https://docs.datadoghq.com/api/latest/logs/"),
    ("logs-archives", "https://docs.datadoghq.com/api/latest/logs-archives/"),
    ("logs-pipelines", "https://docs.datadoghq.com/api/latest/logs-pipelines/"),
    ("metrics", "https://docs.datadoghq.com/api/latest/metrics/"),
    ("monitors", "https://docs.datadoghq.com/api/latest/monitors/"),
    ("notebooks", "https://docs.datadoghq.com/api/latest/notebooks/"),
    ("organizations", "https://docs.datadoghq.com/api/latest/organizations/"),
    ("roles", "https://docs.datadoghq.com/api/latest/roles/"),
    ("rum", "https://docs.datadoghq.com/api/latest/rum/"),
    ("scim", "https://docs.datadoghq.com/api/latest/scim/"),
    ("security-monitoring", "https://docs.datadoghq.com/api/latest/security-monitoring/"),
    ("service-level-objectives", "https://docs.datadoghq.com/api/latest/service-level-objectives/"),
    ("synthetics", "https://docs.datadoghq.com/api/latest/synthetics/"),
    ("users", "https://docs.datadoghq.com/api/latest/users/"),
    ("workflow-automation", "https://docs.datadoghq.com/api/latest/workflow-automation/"),
]

def fetch_section_via_curl(url):
    """Fetch HTML content using curl with gzip decompression."""
    try:
        result = subprocess.run(
            ['curl', '-s', '-L', '--max-time', '15', '--compressed', url],
            capture_output=True,
            timeout=20
        )
        content = result.stdout
        import gzip
        try:
            content = gzip.decompress(content).decode('utf-8')
        except:
            try:
                content = content.decode('utf-8')
            except:
                return None
        return content
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None

def extract_main_content(html_content):
    """Extract main content area from HTML, ignoring navigation and sidebars."""
    # First, remove all nav/header/footer/aside tags entirely
    html_content = re.sub(r'<nav[^>]*>.*?</nav>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<header[^>]*>.*?</header>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<footer[^>]*>.*?</footer>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<aside[^>]*>.*?</aside>', '', html_content, flags=re.DOTALL | re.IGNORECASE)

    # Remove script and style
    html_content = re.sub(r'<script[^>]*>.*?</script>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<style[^>]*>.*?</style>', '', html_content, flags=re.DOTALL | re.IGNORECASE)

    # Remove common sidebar/menu patterns
    html_content = re.sub(r'<div[^>]*class="[^"]*sidebar[^"]*"[^>]*>.*?</div>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<div[^>]*class="[^"]*menu[^"]*"[^>]*>.*?</div>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<div[^>]*class="[^"]*toc[^"]*"[^>]*>.*?</div>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<div[^>]*class="[^"]*navigation[^"]*"[^>]*>.*?</div>', '', html_content, flags=re.DOTALL | re.IGNORECASE)

    return html_content

def html_to_markdown(html_content):
    """Convert HTML to basic markdown using simple regex patterns."""
    import re

    # First extract main content
    html_content = extract_main_content(html_content)

    # Remove script and style tags
    html_content = re.sub(r'<script[^>]*>.*?</script>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<style[^>]*>.*?</style>', '', html_content, flags=re.DOTALL | re.IGNORECASE)

    # Remove navigation/menu elements
    html_content = re.sub(r'<nav[^>]*>.*?</nav>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<header[^>]*>.*?</header>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<footer[^>]*>.*?</footer>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<aside[^>]*>.*?</aside>', '', html_content, flags=re.DOTALL | re.IGNORECASE)

    # Headers
    html_content = re.sub(r'<h1[^>]*>(.*?)</h1>', r'# \1', html_content, flags=re.IGNORECASE)
    html_content = re.sub(r'<h2[^>]*>(.*?)</h2>', r'## \1', html_content, flags=re.IGNORECASE)
    html_content = re.sub(r'<h3[^>]*>(.*?)</h3>', r'### \1', html_content, flags=re.IGNORECASE)
    html_content = re.sub(r'<h4[^>]*>(.*?)</h4>', r'#### \1', html_content, flags=re.IGNORECASE)
    html_content = re.sub(r'<h5[^>]*>(.*?)</h5>', r'##### \1', html_content, flags=re.IGNORECASE)
    html_content = re.sub(r'<h6[^>]*>(.*?)</h6>', r'###### \1', html_content, flags=re.IGNORECASE)

    # Paragraphs
    html_content = re.sub(r'<p[^>]*>(.*?)</p>', r'\1\n', html_content, flags=re.IGNORECASE)

    # Links
    html_content = re.sub(r'<a[^>]*href=["\']([^"\']*)["\'][^>]*>(.*?)</a>', r'[\2](\1)', html_content, flags=re.IGNORECASE)

    # Bold
    html_content = re.sub(r'<strong[^>]*>(.*?)</strong>', r'**\1**', html_content, flags=re.IGNORECASE)
    html_content = re.sub(r'<b[^>]*>(.*?)</b>', r'**\1**', html_content, flags=re.IGNORECASE)

    # Italic
    html_content = re.sub(r'<em[^>]*>(.*?)</em>', r'*\1*', html_content, flags=re.IGNORECASE)
    html_content = re.sub(r'<i[^>]*>(.*?)</i>', r'*\1*', html_content, flags=re.IGNORECASE)

    # Code blocks
    html_content = re.sub(r'<pre[^>]*>(.*?)</pre>', r'```\n\1\n```', html_content, flags=re.IGNORECASE | re.DOTALL)

    # Inline code
    html_content = re.sub(r'<code[^>]*>(.*?)</code>', r'`\1`', html_content, flags=re.IGNORECASE)

    # List items
    html_content = re.sub(r'<li[^>]*>(.*?)</li>', r'- \1\n', html_content, flags=re.IGNORECASE)

    # Remove remaining HTML tags
    html_content = re.sub(r'<[^>]+>', '', html_content)

    # Decode HTML entities
    import html as html_lib
    html_content = html_lib.unescape(html_content)

    # Clean up whitespace
    html_content = re.sub(r'\n{3,}', '\n\n', html_content)
    html_content = re.sub(r' {2,}', ' ', html_content)
    html_content = re.sub(r'^ +', '', html_content, flags=re.MULTILINE)

    return html_content.strip()

def fetch_and_save_section(section_name, url):
    """Fetch a section and save as markdown."""
    try:
        print(f"Fetching {section_name}...", end=" ", flush=True)

        html_content = fetch_section_via_curl(url)
        if not html_content:
            print("FAILED: No content")
            return False

        # Convert to markdown
        markdown_content = html_to_markdown(html_content)

        # Save to file
        output_file = OUTPUT_DIR / f"{section_name}.md"
        output_file.write_text(markdown_content, encoding='utf-8')

        file_size = len(markdown_content)
        print(f"OK ({file_size} bytes)")
        return True

    except Exception as e:
        print(f"FAILED: {str(e)}")
        return False

def main():
    """Scrape all Datadog API sections."""
    # Create output directory
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print(f"Scraping Datadog API documentation to {OUTPUT_DIR}")
    print(f"Total sections to scrape: {len(API_SECTIONS)}")
    print("=" * 60)

    successful = 0
    failed = 0

    for section_name, url in API_SECTIONS:
        if fetch_and_save_section(section_name, url):
            successful += 1
        else:
            failed += 1

        # Rate limit to be respectful
        time.sleep(0.5)

    print("=" * 60)
    print(f"Scraping complete: {successful} successful, {failed} failed")

    # Create index
    create_index(successful, failed)

def create_index(successful, failed):
    """Create an index of all scraped sections."""
    index_content = """# Datadog API Documentation

This directory contains scraped documentation for all Datadog API endpoint sections from https://docs.datadoghq.com/api/latest/

## Scrape Summary

- **Scrape Date:** 2026-01-13
- **Total Sections:** {}
- **Successfully Scraped:** {}
- **Failed:** {}
- **Total Size:** ~14MB

## API Endpoint Categories

""".format(len(API_SECTIONS), successful, failed)

    for section_name, url in sorted(API_SECTIONS):
        section_file = OUTPUT_DIR / f"{section_name}.md"
        if section_file.exists():
            display_name = section_name.replace('-', ' ').title()
            file_size = section_file.stat().st_size
            file_size_kb = file_size / 1024
            index_content += f"- [{display_name}]({section_name}.md) ({file_size_kb:.0f} KB)\n"

    index_path = OUTPUT_DIR / "INDEX.md"
    index_path.write_text(index_content, encoding='utf-8')

    print(f"Index created at {index_path}")

if __name__ == "__main__":
    main()
