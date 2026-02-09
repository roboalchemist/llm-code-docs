#!/usr/bin/env python3
"""
Scraper for Datadog API documentation - All missing sections.
Output: docs/web-scraped/datadog-api/

This scraper fetches all missing Datadog API sections from the official docs.
Uses BeautifulSoup for HTML parsing without external dependencies.
"""
import requests
from pathlib import Path
import time
import sys
import re
from html.parser import HTMLParser
from html import unescape

OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "web-scraped" / "datadog-api"

# All missing sections to scrape
MISSING_SECTIONS = [
    "authentication",
    "aws-logs-integration",
    "case-management-attribute",
    "case-management-type",
    "ci-visibility-tests",
    "cloud-network-monitoring",
    "cloudflare-integration",
    "confluent-cloud",
    "container-images",
    "containers",
    "csm-agents",
    "csm-coverage-analysis",
    "csm-threats",
    "dashboard-lists",
    "datasets",
    "deployment-gates",
    "domain-allowlist",
    "dora-metrics",
    "embeddable-graphs",
    "fastly-integration",
    "fleet-automation",
    "incident-services",
    "incident-teams",
    "ip-allowlist",
    "ip-ranges",
    "logs-custom-destinations",
    "logs-indexes",
    "logs-metrics",
    "logs-restriction-queries",
    "microsoft-teams-integration",
    "network-device-monitoring",
    "observability-pipelines",
    "okta-integration",
    "on-call",
    "on-call-paging",
    "opsgenie-integration",
    "org-connections",
    "pagerduty-integration",
    "powerpack",
    "processes",
    "product-analytics",
    "reference-tables",
    "restriction-policies",
    "rum-audience-management",
    "rum-metrics",
    "rum-retention-filters",
    "screenboards",
    "sensitive-data-scanner",
    "service-accounts",
    "service-checks",
    "service-definition",
    "service-dependencies",
    "service-level-objective-corrections",
    "service-scorecards",
    "slack-integration",
    "snapshots",
    "software-catalog",
    "spa",
    "spans",
    "spans-metrics",
    "static-analysis",
    "tags",
    "teams",
    "test-optimization",
    "timeboards",
    "usage-metering",
    "webhooks-integration",
]

class HTMLToMarkdown(HTMLParser):
    """Simple HTML to Markdown converter."""
    def __init__(self):
        super().__init__()
        self.text = []
        self.in_code = False
        self.in_pre = False
        self.code_lang = ''

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if tag == 'h1':
            self.text.append('\n# ')
        elif tag == 'h2':
            self.text.append('\n## ')
        elif tag == 'h3':
            self.text.append('\n### ')
        elif tag == 'h4':
            self.text.append('\n#### ')
        elif tag == 'h5':
            self.text.append('\n##### ')
        elif tag == 'h6':
            self.text.append('\n###### ')
        elif tag == 'p':
            self.text.append('\n')
        elif tag == 'br':
            self.text.append('\n')
        elif tag == 'code':
            self.in_code = True
            self.text.append('`')
        elif tag == 'pre':
            self.in_pre = True
            self.code_lang = attrs_dict.get('class', '').replace('language-', '').strip()
            self.text.append(f'\n```{self.code_lang}\n')
        elif tag == 'ul' or tag == 'ol':
            self.text.append('\n')
        elif tag == 'li':
            self.text.append('- ')
        elif tag == 'strong' or tag == 'b':
            self.text.append('**')
        elif tag == 'em' or tag == 'i':
            self.text.append('*')
        elif tag == 'a':
            href = attrs_dict.get('href', '#')
            self.text.append('[')

    def handle_endtag(self, tag):
        if tag == 'code':
            self.in_code = False
            self.text.append('`')
        elif tag == 'pre':
            self.in_pre = False
            self.text.append('\n```\n')
        elif tag == 'strong' or tag == 'b':
            self.text.append('**')
        elif tag == 'em' or tag == 'i':
            self.text.append('*')
        elif tag == 'a':
            # This would need better handling with href tracking
            pass

    def handle_data(self, data):
        if data.strip():
            self.text.append(unescape(data))

    def get_text(self):
        return ''.join(self.text)

def extract_text_content(html_content):
    """Extract clean text content from HTML."""
    try:
        # Simple regex extraction - grab main content
        # Look for content divs or main sections
        patterns = [
            r'<main[^>]*>(.*?)</main>',
            r'<article[^>]*>(.*?)</article>',
            r'<div[^>]*class="[^"]*content[^"]*"[^>]*>(.*?)</div>',
        ]

        content = html_content
        for pattern in patterns:
            match = re.search(pattern, html_content, re.DOTALL | re.IGNORECASE)
            if match:
                content = match.group(1)
                break

        # Clean up HTML
        content = re.sub(r'<script[^>]*>.*?</script>', '', content, flags=re.DOTALL)
        content = re.sub(r'<style[^>]*>.*?</style>', '', content, flags=re.DOTALL)
        content = re.sub(r'<nav[^>]*>.*?</nav>', '', content, flags=re.DOTALL)
        content = re.sub(r'<footer[^>]*>.*?</footer>', '', content, flags=re.DOTALL)

        # Convert to markdown using our simple parser
        parser = HTMLToMarkdown()
        parser.feed(content)
        return parser.get_text()
    except Exception as e:
        print(f"Error converting to markdown: {e}")
        return html_content

def scrape_datadog_api_page(section_name):
    """Scrape a single Datadog API documentation page."""
    url = f"https://docs.datadoghq.com/api/latest/{section_name}/"

    print(f"Fetching: {url}")

    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        response = requests.get(url, headers=headers, timeout=20)
        response.raise_for_status()

        # Extract main content area
        content = response.text

        # Convert to markdown
        markdown_content = extract_text_content(content)

        # Clean up the markdown
        markdown_content = re.sub(r'\n\n+', '\n\n', markdown_content)
        markdown_content = markdown_content.strip()

        # Add metadata header
        final_content = f"""# {section_name.replace('-', ' ').title()}

**Source:** {url}
**Last Updated:** {time.strftime('%Y-%m-%d')}

---

{markdown_content}
"""

        return final_content

    except requests.exceptions.RequestException as e:
        print(f"  ERROR: {e}")
        return None

def save_documentation(section_name, content):
    """Save documentation to file."""
    if not content:
        return False

    output_file = OUTPUT_DIR / f"{section_name}.md"

    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(content)
        size = len(content)
        print(f"  Saved: {output_file.name} ({size:,} bytes)")
        return True
    except Exception as e:
        print(f"  Error saving: {e}")
        return False

def main():
    """Main scraper function."""
    # Create output directory if it doesn't exist
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    print(f"Scraping {len(MISSING_SECTIONS)} Datadog API sections...")
    print(f"Output directory: {OUTPUT_DIR}")
    print()

    successful = 0
    failed = 0
    failed_sections = []

    for i, section in enumerate(MISSING_SECTIONS, 1):
        print(f"[{i}/{len(MISSING_SECTIONS)}] {section}")

        content = scrape_datadog_api_page(section)

        if content and save_documentation(section, content):
            successful += 1
        else:
            failed += 1
            failed_sections.append(section)

        # Rate limiting - be respectful to the server
        if i < len(MISSING_SECTIONS):
            time.sleep(1)

    print()
    print("="*60)
    print(f"Scraping completed!")
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    print(f"Total: {len(MISSING_SECTIONS)}")
    if failed_sections:
        print(f"\nFailed sections:")
        for section in failed_sections:
            print(f"  - {section}")
    print(f"Output directory: {OUTPUT_DIR}")
    print("="*60)

    return failed == 0

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
