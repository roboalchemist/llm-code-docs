#!/usr/bin/env python3
"""
DBeaver Documentation Scraper
Downloads DBeaver documentation from dbeaver.com/docs/dbeaver/ and converts to markdown.
DBeaver is a universal database client supporting 90+ databases.
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

# Base URL for DBeaver documentation
BASE_URL = "https://dbeaver.com/docs/dbeaver/"

# Comprehensive list of documentation pages extracted from the index
# These are the actual pages available on dbeaver.com/docs/dbeaver/
DOCS_PAGES = [
    "",  # Index/main page
    "Getting-started/",
    "First-steps/",
    "Installation/",
    "Application-Window-Overview/",
    "Basic-operations/",
    "User-Interface-Themes/",
    "UI-Language/",
    "Accessibility-Guide/",
    "Toolbar-Customization/",
    "Database-Object-Editor/",
    "Reset-UI-settings/",
    "Shortcuts/",
    "Security-in-DBeaver-PRO/",
    "Security/",
    "Managing-Master-Password/",
    "Automation-Security/",
    "Integrated-Security/",
    "Secret-Providers/",
    "Create-Connection/",
    "Edit-Connection/",
    "Invalidate-and-Reconnect-to-Database/",
    "Disconnect-from-Database/",
    "Change-current-user-password/",
    "Working-with-Shell-Commands-in-DBeaver/",
    "Configure-Connection-Initialization-Settings/",
    "Managing-security-restrictions-for-database-connection/",
    "Connection-Types/",
    "Local-Client-Configuration/",
    "Separate-Connections/",
    "Network-configuration/",
    "SSH-Configuration/",
    "SSL-Configuration/",
    "Managing-Truststore-Settings/",
    "Import-SSL-Certificates/",
    "Proxy-configuration/",
    "Proxy-configuration-with-system-files/",
    "Kerberos-Authentication/",
    "Authentication-Database-Native/",
    "Authentication-LDAP-Mechanism/",
    "Authentication-MongoDB/",
    "Authentication-PostgreSQL-Pgpass/",
    "Authentication-PostgreSQL-SSPI/",
    "Authentication-Microsoft-Entra-ID/",
    "Authentication-Salesforce/",
    "Authentication-Snowflake/",
    "Authentication-Databricks/",
    "Authentication-DBeaver-profile/",
    "Database-drivers/",
    "Database-driver-MySQL/",
    "Database-driver-PostgreSQL/",
    "Database-driver-Oracle/",
    "Database-driver-Microsoft-SQL-Server/",
    "Database-driver-SQLite/",
    "Database-driver-MariaDB/",
    "Database-driver-BigQuery/",
    "Database-driver-Snowflake/",
    "Database-driver-Amazon-Redshift/",
    "Database-driver-MongoDB/",
    "Database-driver-Neo4j/",
    "Database-driver-Cassandra/",
    "Database-driver-IBM-Db2/",
    "Database-driver-Teradata/",
    "Database-driver-Databricks/",
    "Database-driver-Salesforce/",
    "Database-driver-Trino/",
    "Database-driver-Google-Cloud-Spanner/",
    "Database-driver-Firestore/",
    "Database-driver-Parquet/",
    "Database-driver-CSV/",
    "Database-driver-JSON/",
    "Database-driver-XML/",
    "Database-driver-XLSX/",
    "Database-driver-Files-MultiSource/",
    "Database-driver-CosmosDB/",
    "Database-driver-Azure-CosmosDB-for-NoSQL/",
    "Database-driver-Amazon-Timestream/",
    "Database-driver-Amazon-Athena/",
    "Database-driver-AlloyDB-for-PostgreSQL/",
    "Database-driver-Aurora-DSQL/",
    "Database-driver-Greenplum/",
    "Database-driver-Netezza/",
    "Database-driver-Yellowbrick/",
    "Database-driver-Microsoft-SQL-Server-on-Google-Cloud/",
    "Database-driver-MySQL-on-Google-Cloud/",
    "Database-driver-PostgreSQL-on-Google-Cloud/",
    "Database-driver-Neptune/",
    "Deprecated-legacy-ODBC-driver/",
    "Navigation/",
    "Database-Navigator/",
    "Projects/",
    "Project-Explorer/",
    "Projects-View/",
    "Project-team-work/",
    "Project-security/",
    "DB-Metadata-Search/",
    "DB-Full-Text-Search/",
    "Filter-Database-Objects/",
    "Data-Viewing-and-Editing/",
    "Data-Editor/",
    "Data-Editor-preferences/",
    "Data-View-and-Format/",
    "Data-Filters/",
    "Data-Search/",
    "Data-Refresh/",
    "Data-import/",
    "Data-export/",
    "Data-compare/",
    "Data-migration/",
    "Mock-Data-Generation-in-DBeaver/",
    "Working-with-XML-and-JSON/",
    "Working-with-Spatial-GIS-data/",
    "Working-with-Dictionary-Data/",
    "PostgreSQL-Arrays/",
    "SQL-Code-Editor/",
    "SQL-Editor/",
    "SQL-Assist-and-Auto-Complete/",
    "SQL-Execution/",
    "SQL-Formatting/",
    "SQL-Generation/",
    "SQL-Terminal/",
    "SQL-Templates/",
    "Query-Execution-Plan/",
    "Query-Manager/",
    "Query-Trace-Panel/",
    "Background-Tasks/",
    "Panels/",
    "Metadata-Panel/",
    "References-Panel/",
    "Result-Details-Panel/",
    "Value-Panel/",
    "Grouping-Panel/",
    "Calc-Panel/",
    "Variables-panel/",
    "Bookmarks/",
    "Lock-Manager/",
    "Pending-Transactions/",
    "Transaction-Log/",
    "ER-Diagrams/",
    "Database-Structure-Diagrams/",
    "Custom-Diagrams/",
    "Data-Transfer/",
    "Data-transfer/",
    "Data-Transfer-Actions/",
    "Data-transfer-email/",
    "Data-transfer-external-storage/",
    "Cloud-Storage/",
    "Cloud-Explorer/",
    "AWS-Cloud-Explorer/",
    "AWS-Credentials/",
    "AWS-Permissions/",
    "AWS-SSO/",
    "AWS-SSM-Configuration/",
    "AWS-DocumentDB/",
    "AWS-DynamoDB/",
    "AWS-Keyspaces/",
    "Azure-Cloud-Explorer/",
    "Azure-Permissions/",
    "GCP-Credentials/",
    "GCP-SSO/",
    "Google-Cloud-Explorer/",
    "Driver-Manager/",
    "Admin-Manage-Connections/",
    "Admin-Manage-Drivers/",
    "Admin-Manage-Preferences/",
    "Admin-Preference-Restrictions/",
    "Admin-Variables/",
    "Configuration-files-in-DBeaver/",
    "Workspace-Location/",
    "Reset-workspace/",
    "License-Administration/",
    "How-to-Import-License/",
    "How-to-Update-License/",
    "How-to-Reassign-License/",
    "Differences-between-license-types/",
    "Enterprise-Edition/",
    "Ultimate-Edition/",
    "Lite-Edition/",
    "Early-Access-Program-license/",
    "DBeaver-release-cycles/",
    "Sample-Database/",
    "New-Table-Creation/",
    "Creating-columns/",
    "Creating-Indexes/",
    "Implementing-Constraints/",
    "Utilizing-Foreign-Keys/",
    "Incorporating-Triggers/",
    "How-to-work-with-database-Partitions/",
    "Connecting-to-Oracle-databases/",
    "Connecting-to-Oracle-Database-using-JDBC-OCI-driver/",
    "Oracle/",
    "PostgreSQL-Extensions/",
    "MySQL-Two-factor/",
    "Snowflake/",
    "MongoDB/",
    "Cassandra/",
    "InfluxDB/",
    "Google-Bigtable/",
    "Apache-Hive/",
    "Clickhouse/",
    "Couchbase/",
    "Redis/",
    "AI-Assistance-and-Data-Privacy/",
    "AI-Assistance-settings/",
    "Quick-start-with-AI-Assistance/",
    "AI-Smart-Assistance/",
    "AI-Functions/",
    "AI-query-suggestion/",
    "AI-query-explanation/",
    "AI-error-explanation/",
    "AI-chat/",
    "AI-command/",
    "AI-speech-recognition/",
    "AI-smart-metadata-description/",
    "AI-integration-with-OpenAI/",
    "AI-integration-with-Anthropic-Claude/",
    "AI-integration-with-Azure-OpenAI/",
    "AI-integration-with-Google-Gemini/",
    "AI-integration-with-GitHub-Copilot/",
    "AI-integration-with-Amazon-Bedrock/",
    "AI-integration-with-Ollama/",
    "Disable-AI-assistance/",
    "Task-Management/",
    "Task-Scheduler/",
    "Composite-Tasks/",
    "Troubleshooting-task-scheduler-issues/",
    "Schema-compare/",
    "Backup-Restore/",
    "Tableau-integration-in-DBeaver/",
    "Using-Liquibase-in-DBeaver/",
    "Eclipse-extensions/",
    "Command-Line/",
    "ODBC-JDBC-Driver/",
    "Client-Side-Scripting/",
    "PGDebugger/",
    "Dashboards/",
    "Search-Tool/",
    "File-Search/",
    "Session-Manager-Guide/",
    "Managing-Charts/",
    "Managing-Data-Formats/",
    "Edit-mode/",
    "Simple-and-Advanced-View/",
    "Visual-Query-Builder/",
    "Advanced-Metadata-Read-Actions/",
    "View-and-Editor-Actions/",
    "Virtual-Keys/",
    "Virtual-column-expressions/",
    "How-to-import-Connections-from-External-Tools/",
    "How-to-add-additional-artifacts-to-the-driver/",
    "How-to-set-a-variable-if-dbeaver-ini-is-read-only/",
    "JDBC-Time-Zones/",
    "JDBC-Tracing/",
    "Log-files/",
    "Making-a-thread-dump/",
    "Troubleshooting-system-issues/",
    "Importing-CA-certificates-from-your-local-Java-into-DBeaver/",
    "SQL-Plus-Script-Execution/",
    "Kubernetes-configuration/",
    "Windows-Silent-Install/",
    "Snap-installation/",
    "Network-profiles/",
    "Pre-configured-Variables/",
    "JDBC-Time-Zones/",
    "Statistics-Collection/",
    "Customer-technical-support-information/",
    "Posting-issues/",
    "FAQ/",
]

REQUEST_DELAY = 0.5  # seconds between requests


def sanitize_filename(path):
    """Convert path to safe filename."""
    # Remove trailing slashes
    path = path.rstrip("/")

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

        # Try to find main content area
        main = soup.find('main')
        if main:
            return str(main)

        # Try to find article
        article = soup.find('article')
        if article:
            return str(article)

        # Try to find divs with content class
        content_div = soup.find('div', class_=re.compile('content|main|body|article', re.I))
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
        if page_path:
            url = urljoin(BASE_URL, page_path)
        else:
            url = BASE_URL

        # Sanitize the filename
        if page_path:
            filename = sanitize_filename(page_path)
        else:
            filename = "index.md"

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
    """Main function to download DBeaver documentation."""
    print("=" * 60)
    print("DBeaver Documentation Scraper")
    print("=" * 60)
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "web-scraped" / "dbeaver"
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
