#!/usr/bin/env python3
"""
1Password Developer Documentation Scraper
Downloads all 1Password developer documentation pages and converts to markdown.
Covers CLI, Service Accounts, SDKs, Shell Plugins, and AI/Agentic features.
"""

import os
import sys
import requests
from pathlib import Path
from urllib.parse import urlparse
import time
import re
import subprocess

# 1Password developer documentation pages
ONEPASSWORD_DOC_PAGES = [
    # CLI - Core
    "/docs/cli",
    "/docs/cli/get-started",
    "/docs/cli/reference",
    "/docs/cli/best-practices",
    "/docs/cli/install-server",
    "/docs/cli/app-integration",
    "/docs/cli/app-integration-security",
    "/docs/cli/config-directories",
    "/docs/cli/scripts",
    "/docs/cli/item-create",
    "/docs/cli/recover-users",
    "/docs/cli/provision-users",
    "/docs/cli/grant-revoke-vault-permissions",
    # CLI - Secrets
    "/docs/cli/secret-references",
    "/docs/cli/secret-reference-syntax",
    "/docs/cli/secrets-config-files",
    "/docs/cli/secrets-scripts",
    # CLI - Reference Commands
    "/docs/cli/reference/commands/signin",
    "/docs/cli/reference/commands/signout",
    "/docs/cli/reference/commands/update",
    "/docs/cli/reference/commands/whoami",
    "/docs/cli/reference/commands/inject",
    "/docs/cli/reference/commands/read",
    "/docs/cli/reference/commands/run",
    "/docs/cli/reference/update",
    # CLI - Management Commands
    "/docs/cli/reference/management-commands/account",
    "/docs/cli/reference/management-commands/connect",
    "/docs/cli/reference/management-commands/document",
    "/docs/cli/reference/management-commands/events-api",
    "/docs/cli/reference/management-commands/group",
    "/docs/cli/reference/management-commands/item",
    "/docs/cli/reference/management-commands/plugin",
    "/docs/cli/reference/management-commands/service-account",
    "/docs/cli/reference/management-commands/user",
    "/docs/cli/reference/management-commands/vault",
    # Shell Plugins
    "/docs/cli/shell-plugins",
    "/docs/cli/shell-plugins/aws",
    "/docs/cli/shell-plugins/github",
    "/docs/cli/shell-plugins/gitlab",
    "/docs/cli/shell-plugins/akamai",
    "/docs/cli/shell-plugins/circleci",
    "/docs/cli/shell-plugins/digitalocean",
    "/docs/cli/shell-plugins/hashicorp-vault",
    "/docs/cli/shell-plugins/heroku",
    "/docs/cli/shell-plugins/homebrew",
    "/docs/cli/shell-plugins/ngrok",
    "/docs/cli/shell-plugins/contribute",
    "/docs/cli/shell-plugins/environments",
    "/docs/cli/shell-plugins/multiple-accounts",
    # Service Accounts
    "/docs/service-accounts",
    "/docs/service-accounts/get-started",
    "/docs/service-accounts/security",
    "/docs/service-accounts/use-with-1password-cli",
    "/docs/service-accounts/manage-service-accounts",
    "/docs/service-accounts/rate-limits",
    # SDKs
    "/docs/sdks",
    "/docs/sdks/concepts",
    "/docs/sdks/setup-tutorial",
    "/docs/sdks/tutorials",
    "/docs/sdks/load-secrets",
    "/docs/sdks/list-vaults-items",
    "/docs/sdks/manage-items",
    "/docs/sdks/files",
    "/docs/sdks/share-items",
    "/docs/sdks/vaults",
    "/docs/sdks/groups",
    "/docs/sdks/desktop-app-integrations",
    "/docs/sdks/ai-agent",
    # Agentic/AI
    "/docs/agentic-autofill",
    # Connect Server
    "/docs/connect",
    "/docs/connect/get-started",
    "/docs/connect/api-reference",
    "/docs/connect/connect-cli",
    "/docs/connect/security",
    # SSH
    "/docs/ssh",
    "/docs/ssh/get-started",
    "/docs/ssh/agent",
    "/docs/ssh/git-commit-signing",
    # Environments
    "/docs/environments",
    "/docs/environments/local-env-file",
    # Integrations
    "/docs/integrations",
    # Events API
    "/docs/events-api",
    "/docs/events-api/get-started",
    "/docs/events-api/reference",
]

BASE_URL = "https://developer.1password.com"


def html_to_markdown(html_content, url):
    """Convert HTML to markdown, extracting main content only."""
    # Docusaurus uses <article> or <main> for content
    article_match = re.search(
        r'<article[^>]*>(.*?)</article>',
        html_content, flags=re.DOTALL | re.IGNORECASE
    )

    if article_match:
        html_content = article_match.group(1)
    else:
        # Try main content area
        main_match = re.search(
            r'<main[^>]*>(.*?)</main>',
            html_content, flags=re.DOTALL | re.IGNORECASE
        )
        if main_match:
            html_content = main_match.group(1)

    # Remove navigation, sidebars, and other non-content elements
    html_content = re.sub(r'<nav[^>]*>.*?</nav>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<aside[^>]*>.*?</aside>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<footer[^>]*>.*?</footer>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<div[^>]*class="[^"]*pagination[^"]*"[^>]*>.*?</div>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<div[^>]*class="[^"]*tableOfContents[^"]*"[^>]*>.*?</div>', '', html_content, flags=re.DOTALL | re.IGNORECASE)

    # Try pandoc for conversion
    try:
        result = subprocess.run(
            ['pandoc', '-f', 'html', '-t', 'markdown', '--wrap=none'],
            input=html_content,
            capture_output=True,
            text=True,
            timeout=30
        )
        if result.returncode == 0:
            markdown = result.stdout
            # Clean up pandoc artifacts
            markdown = re.sub(r'^::+.*$', '', markdown, flags=re.MULTILINE)
            markdown = re.sub(r'\{[^}]*\}', '', markdown)
            markdown = re.sub(r'\n{3,}', '\n\n', markdown)
            markdown = re.sub(r'^\[Skip to main content\].*$', '', markdown, flags=re.MULTILINE)
            markdown = re.sub(r'^\*\*New!\*\*.*$', '', markdown, flags=re.MULTILINE)
            markdown = markdown.strip()
            return f"# Source: {url}\n\n{markdown}"
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass

    # Fallback: basic HTML to text extraction
    html_content = re.sub(r'<script[^>]*>.*?</script>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<style[^>]*>.*?</style>', '', html_content, flags=re.DOTALL | re.IGNORECASE)

    # Convert common HTML elements to markdown
    for i in range(6, 0, -1):
        html_content = re.sub(rf'<h{i}[^>]*>(.*?)</h{i}>', r'\n' + '#' * i + r' \1\n', html_content, flags=re.DOTALL | re.IGNORECASE)

    html_content = re.sub(r'<pre[^>]*><code[^>]*>(.*?)</code></pre>', r'\n```\n\1\n```\n', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<code[^>]*>(.*?)</code>', r'`\1`', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>', r'[\2](\1)', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<strong[^>]*>(.*?)</strong>', r'**\1**', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<b[^>]*>(.*?)</b>', r'**\1**', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<em[^>]*>(.*?)</em>', r'*\1*', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<li[^>]*>(.*?)</li>', r'- \1\n', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<[ou]l[^>]*>', '\n', html_content, flags=re.IGNORECASE)
    html_content = re.sub(r'</[ou]l>', '\n', html_content, flags=re.IGNORECASE)
    html_content = re.sub(r'<p[^>]*>(.*?)</p>', r'\n\1\n', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<br\s*/?>', '\n', html_content, flags=re.IGNORECASE)
    html_content = re.sub(r'<[^>]+>', '', html_content)

    # Decode HTML entities
    html_content = html_content.replace('&nbsp;', ' ')
    html_content = html_content.replace('&lt;', '<')
    html_content = html_content.replace('&gt;', '>')
    html_content = html_content.replace('&amp;', '&')
    html_content = html_content.replace('&quot;', '"')
    html_content = html_content.replace('&#39;', "'")

    html_content = re.sub(r'\n\s*\n\s*\n', '\n\n', html_content)
    html_content = html_content.strip()

    return f"# Source: {url}\n\n{html_content}"


def download_page(url, output_path):
    """Download a page and convert to markdown."""
    try:
        print(f"Downloading: {url}")

        response = requests.get(url, timeout=15)
        response.raise_for_status()

        markdown = html_to_markdown(response.text, url)

        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(markdown)

        print(f"  -> Saved: {output_path}")
        return True

    except requests.exceptions.RequestException as e:
        print(f"  -> Error downloading {url}: {e}")
        return False
    except Exception as e:
        print(f"  -> Error processing {url}: {e}")
        return False


def path_to_filename(path):
    """Convert URL path to filename."""
    if path == "/" or path == "":
        return "index.md"

    # Remove /docs/ prefix and leading/trailing slashes
    clean_path = path.replace("/docs/", "").strip("/")

    # Convert to flat filename: cli/get-started -> cli-get-started.md
    if "/" in clean_path:
        return clean_path.replace("/", "-") + ".md"

    return clean_path + ".md"


def main():
    """Main function to download all 1Password documentation."""
    print("=" * 60)
    print("1Password Developer Documentation Scraper")
    print("=" * 60)
    print(f"Base URL: {BASE_URL}")
    print(f"Pages to download: {len(ONEPASSWORD_DOC_PAGES)}")
    print()

    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "web-scraped" / "1password"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Output directory: {output_dir}")
    print()

    successful = 0
    failed = 0
    start_time = time.time()

    for i, page_path in enumerate(ONEPASSWORD_DOC_PAGES, 1):
        url = BASE_URL + page_path
        filename = path_to_filename(page_path)
        output_path = output_dir / filename

        print(f"[{i:2d}/{len(ONEPASSWORD_DOC_PAGES)}] ", end="")

        if download_page(url, output_path):
            successful += 1
        else:
            failed += 1

        # Be respectful with rate limiting
        time.sleep(0.5)

    elapsed = time.time() - start_time

    print()
    print("=" * 60)
    print("Download Summary")
    print("=" * 60)
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    print(f"Time: {elapsed:.1f} seconds")
    print(f"Output: {output_dir}")

    total_size = sum(f.stat().st_size for f in output_dir.glob("*.md"))
    print(f"Total size: {total_size:,} bytes ({total_size/1024:.1f} KB)")

    print()
    if failed > 0:
        print(f"Warning: {failed} pages failed to download")
        sys.exit(1)
    else:
        print("All pages downloaded successfully!")
        sys.exit(0)


if __name__ == "__main__":
    main()
