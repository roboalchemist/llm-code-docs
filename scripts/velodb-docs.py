#!/usr/bin/env python3
"""
VeloDB Documentation Scraper
Downloads VeloDB documentation from docs.velodb.io and converts to markdown.
VeloDB is a high-performance analytical database based on Apache Doris for log analytics.
"""

import os
import sys
import requests
from pathlib import Path
import time
from html2text import html2text
from urllib.parse import urljoin, urlparse
import re
from bs4 import BeautifulSoup

# Base URL for VeloDB documentation
BASE_URL = "https://docs.velodb.io"

# Documentation pages extracted from the Docusaurus sidebar
# These are the main sections and key pages available on docs.velodb.io
DOCS_PAGES = [
    "/cloud/4.x/getting-started/overview",
    "/cloud/4.x/getting-started/quick-start",
    "/cloud/4.x/use-cases/observability/overview",
    "/cloud/4.x/use-cases/observability/metrics-overview",
    "/cloud/4.x/use-cases/observability/tracing-overview",
    "/cloud/4.x/use-cases/observability/logs-overview",
    "/cloud/4.x/use-cases/observability/profile-overview",
    "/cloud/4.x/use-cases/observability/event-overview",
    "/cloud/4.x/user-guide/db-connect/database-connect",
    "/cloud/4.x/user-guide/db-connect/data-source-config",
    "/cloud/4.x/user-guide/table-design/overview",
    "/cloud/4.x/user-guide/table-design/create-table",
    "/cloud/4.x/user-guide/table-design/table-organization",
    "/cloud/4.x/user-guide/data-operate/import/load-manual",
    "/cloud/4.x/user-guide/data-operate/import/load-doris-connector",
    "/cloud/4.x/user-guide/data-operate/import/load-from-s3",
    "/cloud/4.x/user-guide/data-operate/update/update-overview",
    "/cloud/4.x/user-guide/data-operate/update/update-data",
    "/cloud/4.x/user-guide/data-operate/update/delete-data",
    "/cloud/4.x/user-guide/data-operate/export/export-overview",
    "/cloud/4.x/user-guide/data-operate/export/export-to-s3",
    "/cloud/4.x/user-guide/data-operate/export/export-to-mysql",
    "/cloud/4.x/user-guide/query-data/mysql-compatibility",
    "/cloud/4.x/user-guide/query-data/query-tips",
    "/cloud/4.x/user-guide/query-acceleration/performance-tuning-overview/tuning-overview",
    "/cloud/4.x/user-guide/query-acceleration/performance-tuning-overview/tuning-strategy",
    "/cloud/4.x/user-guide/query-acceleration/performance-tuning-overview/sql-tuning",
    "/cloud/4.x/user-guide/lakehouse/lakehouse-overview",
    "/cloud/4.x/user-guide/lakehouse/lakehouse-operations",
    "/cloud/4.x/user-guide/compute-storage-decoupled/before-deployment",
    "/cloud/4.x/user-guide/compute-storage-decoupled/deployment-architecture",
    "/cloud/4.x/user-guide/admin-manual/system-tables/overview",
    "/cloud/4.x/user-guide/admin-manual/system-tables/system-databases",
    "/cloud/4.x/user-guide/admin-manual/privilege-management",
    "/cloud/4.x/user-guide/admin-manual/user-account",
    "/cloud/4.x/user-guide/studio/overview",
    "/cloud/4.x/user-guide/studio/sql-editor",
    "/cloud/4.x/user-guide/studio/data-visualization",
    "/cloud/4.x/management-guide/console-overview",
    "/cloud/4.x/management-guide/warehouse-management/overview",
    "/cloud/4.x/management-guide/warehouse-management/create-warehouse",
    "/cloud/4.x/management-guide/warehouse-management/configure-warehouse",
    "/cloud/4.x/management-guide/cluster-management",
    "/cloud/4.x/management-guide/connections",
    "/cloud/4.x/management-guide/studio",
    "/cloud/4.x/management-guide/monitoring-overview",
    "/cloud/4.x/management-guide/backup",
    "/cloud/4.x/management-guide/usage-and-billing",
    "/cloud/4.x/management-guide/user-and-organization",
    "/cloud/4.x/management-guide/more/amazon-aws/create-data-credential",
    "/cloud/4.x/integration/overview",
    "/cloud/4.x/ecosystem/observability/logstash",
    "/cloud/4.x/ecosystem/observability/fluent-bit",
    "/cloud/4.x/ecosystem/observability/fluentd",
    "/cloud/4.x/integration/data-processing/spark-doris-connector",
    "/cloud/4.x/integration/data-processing/flink-doris-connector",
    "/cloud/4.x/integration/bi/tableau",
    "/cloud/4.x/integration/bi/metabase",
    "/cloud/4.x/integration/bi/grafana",
    "/cloud/4.x/integration/sql-client/dbeaver",
    "/cloud/4.x/integration/sql-client/mysql-command",
    "/cloud/4.x/integration/sql-client/jdbc",
    "/cloud/4.x/integration/data-source/doris-kafka-connector",
    "/cloud/4.x/integration/data-source/doris-jdbc-connector",
    "/cloud/4.x/sql-manual/basic-element/sql-data-types/data-type-overview",
    "/cloud/4.x/sql-manual/basic-element/sql-data-types/data-type-numeric",
    "/cloud/4.x/sql-manual/basic-element/sql-data-types/data-type-string",
    "/cloud/4.x/sql-manual/sql-functions/scalar-functions/numeric-functions/abs",
    "/cloud/4.x/sql-manual/sql-functions/scalar-functions/numeric-functions/acos",
    "/cloud/4.x/sql-manual/sql-functions/scalar-functions/string-functions/concat",
    "/cloud/4.x/sql-manual/sql-functions/scalar-functions/string-functions/length",
    "/cloud/4.x/sql-manual/sql-statements/data-query/SELECT",
    "/cloud/4.x/sql-manual/sql-statements/data-manipulation/INSERT",
    "/cloud/4.x/sql-manual/sql-statements/data-manipulation/UPDATE",
    "/cloud/4.x/sql-manual/sql-statements/data-manipulation/DELETE",
    "/cloud/4.x/best-practice/data-faq",
    "/cloud/4.x/best-practice/sql-faq",
    "/cloud/4.x/best-practice/lakehouse-faq",
    "/cloud/4.x/best-practice/bi-faq",
    "/cloud/4.x/best-practice/load-faq",
    "/cloud/4.x/security/security-overview",
    "/cloud/4.x/security/auth/authentication-and-authorization",
    "/cloud/4.x/security/auth/ldap-authentication",
    "/cloud/4.x/security/audit-plugin",
    "/cloud/4.x/security/encryption/encryption-function",
    "/cloud/4.x/security/integrations/aws-authentication-and-authorization",
    "/cloud/4.x/security/privacy-compliance/security-features",
    "/cloud/4.x/release-notes/platform-release-notes",
]

REQUEST_DELAY = 0.3  # seconds between requests


def sanitize_filename(path):
    """Convert path to safe filename."""
    # Remove leading slashes
    path = path.lstrip("/")

    # If empty, use 'index'
    if not path:
        return "index.md"

    # Replace slashes with dashes
    safe = path.replace("/", "-")

    # Ensure .md extension
    if not safe.endswith('.md'):
        safe = safe + '.md'

    return safe


def html_to_markdown(html_content):
    """Convert HTML content to markdown."""
    try:
        # Use html2text for conversion
        markdown = html2text(html_content)
        return markdown
    except Exception as e:
        print(f"    Warning: Could not convert HTML to markdown: {e}")
        # Fallback: return raw content
        return html_content


def extract_main_content(html_content):
    """Extract main documentation content from the HTML."""
    try:
        soup = BeautifulSoup(html_content, 'html.parser')

        # Remove script and style tags
        for tag in soup(['script', 'style', 'nav', 'footer']):
            tag.decompose()

        # Try to find main content area
        main = soup.find('main')
        if main:
            return str(main)

        # Try to find article
        article = soup.find('article')
        if article:
            return str(article)

        # Try to find divs with content class
        content_div = soup.find('div', class_=re.compile('content|main|body|article|doc', re.I))
        if content_div:
            return str(content_div)

        # Fallback: return original
        return html_content
    except Exception as e:
        print(f"    Warning: Could not extract main content: {e}")
        return html_content


def download_page(page_path, output_dir):
    """Download a documentation page."""
    try:
        # Build full URL
        if page_path.startswith("/"):
            url = BASE_URL + page_path
        else:
            url = urljoin(BASE_URL, page_path)

        # Sanitize the filename
        filename = sanitize_filename(page_path)

        print(f"  Downloading: {url}")

        response = requests.get(url, timeout=15)

        # Skip 404s and other errors gracefully
        if response.status_code == 404:
            print(f"    -> Page not found (404)")
            return False

        response.raise_for_status()

        html_content = response.text

        # Extract main content
        main_content = extract_main_content(html_content)

        # Convert to markdown
        markdown_content = html_to_markdown(main_content)

        # Add metadata header
        header = f"""# Source: {url}

"""
        content = header + markdown_content

        # Save to file
        output_path = output_dir / filename
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"    -> Saved: {filename}")
        return True

    except requests.exceptions.RequestException as e:
        print(f"    -> Error downloading {page_path}: {e}")
        return False
    except Exception as e:
        print(f"    -> Error processing {page_path}: {e}")
        return False


def main():
    """Main function to download VeloDB documentation."""
    print("=" * 60)
    print("VeloDB Documentation Scraper")
    print("=" * 60)
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "web-scraped" / "velodb"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Output directory: {output_dir}")
    print(f"Documentation source: {BASE_URL}")
    print()

    # Download all pages
    print("Downloading documentation pages...")
    print()

    successful = 0
    failed = 0
    skipped = 0
    start_time = time.time()

    for idx, page_path in enumerate(DOCS_PAGES, 1):
        print(f"[{idx:2d}/{len(DOCS_PAGES)}] ", end="")

        result = download_page(page_path, output_dir)
        if result is True:
            successful += 1
        elif result is False:
            skipped += 1
        else:
            failed += 1

        # Be respectful with rate limiting
        time.sleep(REQUEST_DELAY)

    elapsed = time.time() - start_time

    print()
    print("=" * 60)
    print("Download Summary")
    print("=" * 60)
    print(f"Successful: {successful}")
    print(f"Skipped (404): {skipped}")
    print(f"Failed: {failed}")
    print(f"Time: {elapsed:.1f} seconds")
    print(f"Output: {output_dir}")

    # Calculate total size
    md_files = list(output_dir.glob("**/*.md"))
    if md_files:
        total_size = sum(f.stat().st_size for f in md_files)
        print(f"Total files: {len(md_files)}")
        print(f"Total size: {total_size:,} bytes ({total_size/1024:.1f} KB)")
    else:
        print("No files were created!")

    print()
    if successful == 0:
        print("Warning: No files were successfully downloaded")
        sys.exit(1)
    else:
        print(f"Successfully downloaded {successful} documentation pages!")
        sys.exit(0)


if __name__ == "__main__":
    main()
