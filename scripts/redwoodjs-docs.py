#!/usr/bin/env python3
"""
RedwoodJS Documentation Scraper
Downloads all RedwoodJS documentation pages and converts to markdown.
RedwoodJS is a full-stack React framework for building web applications.
"""

import os
import sys
import requests
from pathlib import Path
from urllib.parse import urlparse
import time
import re
import subprocess

# RedwoodJS documentation pages from sitemap (latest version only, no version-specific docs)
REDWOODJS_DOC_PAGES = [
    "/docs/accessibility",
    "/docs/app-configuration-redwood-toml",
    "/docs/assets-and-files",
    "/docs/auth/auth0",
    "/docs/auth/azure",
    "/docs/auth/clerk",
    "/docs/auth/custom",
    "/docs/auth/dbauth",
    "/docs/authentication",
    "/docs/auth/firebase",
    "/docs/auth/netlify",
    "/docs/auth/supabase",
    "/docs/auth/supertokens",
    "/docs/background-jobs",
    "/docs/builds",
    "/docs/cells",
    "/docs/cli-commands",
    "/docs/connection-pooling",
    "/docs/contributing",
    "/docs/contributing-walkthrough",
    "/docs/cors",
    "/docs/create-redwood-app",
    "/docs/database-seeds",
    "/docs/data-migrations",
    "/docs/deploy/baremetal",
    "/docs/deploy/coherence",
    "/docs/deploy/edgio",
    "/docs/deploy/flightcontrol",
    "/docs/deploy/introduction",
    "/docs/deployment/index",
    "/docs/deploy/netlify",
    "/docs/deploy/render",
    "/docs/deploy/serverless",
    "/docs/deploy/vercel",
    "/docs/directives",
    "/docs/docker",
    "/docs/environment-variables",
    "/docs/forms",
    "/docs/graphql",
    "/docs/graphql/caching",
    "/docs/graphql/fragments",
    "/docs/graphql/index",
    "/docs/graphql/mocking-graphql-requests",
    "/docs/graphql/realtime",
    "/docs/graphql/trusted-documents",
    "/docs/how-to/build-dashboards-fast-with-tremor",
    "/docs/how-to/creating-a-background-worker-with-exec-and-faktory",
    "/docs/how-to/custom-function",
    "/docs/how-to/dbauth-passwordless",
    "/docs/how-to/disable-api-database",
    "/docs/how-to/file-uploads",
    "/docs/how-to/gotrue-auth",
    "/docs/how-to/index",
    "/docs/how-to/mocking-graphql-in-storybook",
    "/docs/how-to/oauth",
    "/docs/how-to/pagination",
    "/docs/how-to/role-based-access-control-rbac",
    "/docs/how-to/self-hosting-redwood",
    "/docs/how-to/sending-emails",
    "/docs/how-to/supabase-auth",
    "/docs/how-to/test-in-github-actions",
    "/docs/how-to/using-a-third-party-api",
    "/docs/how-to/using-gitpod",
    "/docs/how-to/using-nvm",
    "/docs/how-to/using-yarn",
    "/docs/how-to/windows-development-setup",
    "/docs/index",
    "/docs/introduction",
    "/docs/intro-to-servers",
    "/docs/local-postgres-setup",
    "/docs/logger",
    "/docs/mailer",
    "/docs/monitoring/index",
    "/docs/monitoring/sentry",
    "/docs/prerender",
    "/docs/project-configuration-dev-test-build",
    "/docs/quick-start",
    "/docs/realtime",
    "/docs/redwoodrecord",
    "/docs/router",
    "/docs/schema-relations",
    "/docs/security",
    "/docs/seo-head",
    "/docs/server-file",
    "/docs/serverless-functions",
    "/docs/services",
    "/docs/storybook",
    "/docs/studio",
    "/docs/testing",
    "/docs/toast-notifications",
    "/docs/tutorial/afterword",
    "/docs/tutorial/chapter0/what-is-redwood",
    "/docs/tutorial/chapter1/file-structure",
    "/docs/tutorial/chapter1/first-page",
    "/docs/tutorial/chapter1/installation",
    "/docs/tutorial/chapter1/layouts",
    "/docs/tutorial/chapter1/prerequisites",
    "/docs/tutorial/chapter1/second-page",
    "/docs/tutorial/chapter2/cells",
    "/docs/tutorial/chapter2/getting-dynamic",
    "/docs/tutorial/chapter2/routing-params",
    "/docs/tutorial/chapter2/side-quest",
    "/docs/tutorial/chapter3/forms",
    "/docs/tutorial/chapter3/saving-data",
    "/docs/tutorial/chapter4/authentication",
    "/docs/tutorial/chapter4/deployment",
    "/docs/tutorial/chapter5/first-story",
    "/docs/tutorial/chapter5/first-test",
    "/docs/tutorial/chapter5/storybook",
    "/docs/tutorial/chapter5/testing",
    "/docs/tutorial/chapter6/comment-form",
    "/docs/tutorial/chapter6/comments-schema",
    "/docs/tutorial/chapter6/multiple-comments",
    "/docs/tutorial/chapter6/the-redwood-way",
    "/docs/tutorial/chapter7/api-side-currentuser",
    "/docs/tutorial/chapter7/rbac",
    "/docs/tutorial/foreword",
    "/docs/tutorial/intermission",
    "/docs/typescript/generated-types",
    "/docs/typescript/index",
    "/docs/typescript/introduction",
    "/docs/typescript/strict-mode",
    "/docs/typescript/utility-types",
    "/docs/upgrade-guides/v8",
    "/docs/uploads",
    "/docs/vite-configuration",
    "/docs/webhooks",
]

BASE_URL = "https://docs.redwoodjs.com"


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
        # Try main tag
        main_match = re.search(
            r'<main[^>]*>(.*?)</main>',
            html_content, flags=re.DOTALL | re.IGNORECASE
        )
        if main_match:
            html_content = main_match.group(1)

    # Try pandoc first for best quality conversion
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
            markdown = re.sub(r'^::+.*$', '', markdown, flags=re.MULTILINE)  # Remove ::: div markers
            markdown = re.sub(r'\{[^}]*\}', '', markdown)  # Remove {.class} attributes
            markdown = re.sub(r'\n{3,}', '\n\n', markdown)  # Normalize whitespace
            markdown = markdown.strip()
            return f"# Source: {url}\n\n{markdown}"
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass

    # Fallback: basic HTML to text extraction
    # Remove script and style elements
    html_content = re.sub(r'<script[^>]*>.*?</script>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<style[^>]*>.*?</style>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<nav[^>]*>.*?</nav>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<header[^>]*>.*?</header>', '', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<footer[^>]*>.*?</footer>', '', html_content, flags=re.DOTALL | re.IGNORECASE)

    # Convert common HTML elements to markdown
    # Headers
    for i in range(6, 0, -1):
        html_content = re.sub(rf'<h{i}[^>]*>(.*?)</h{i}>', r'\n' + '#' * i + r' \1\n', html_content, flags=re.DOTALL | re.IGNORECASE)

    # Code blocks
    html_content = re.sub(r'<pre[^>]*><code[^>]*>(.*?)</code></pre>', r'\n```\n\1\n```\n', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<code[^>]*>(.*?)</code>', r'`\1`', html_content, flags=re.DOTALL | re.IGNORECASE)

    # Links
    html_content = re.sub(r'<a[^>]*href="([^"]*)"[^>]*>(.*?)</a>', r'[\2](\1)', html_content, flags=re.DOTALL | re.IGNORECASE)

    # Bold and italic
    html_content = re.sub(r'<strong[^>]*>(.*?)</strong>', r'**\1**', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<b[^>]*>(.*?)</b>', r'**\1**', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<em[^>]*>(.*?)</em>', r'*\1*', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<i[^>]*>(.*?)</i>', r'*\1*', html_content, flags=re.DOTALL | re.IGNORECASE)

    # Lists
    html_content = re.sub(r'<li[^>]*>(.*?)</li>', r'- \1\n', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<[ou]l[^>]*>', '\n', html_content, flags=re.IGNORECASE)
    html_content = re.sub(r'</[ou]l>', '\n', html_content, flags=re.IGNORECASE)

    # Paragraphs and line breaks
    html_content = re.sub(r'<p[^>]*>(.*?)</p>', r'\n\1\n', html_content, flags=re.DOTALL | re.IGNORECASE)
    html_content = re.sub(r'<br\s*/?>', '\n', html_content, flags=re.IGNORECASE)
    html_content = re.sub(r'<div[^>]*>', '\n', html_content, flags=re.IGNORECASE)
    html_content = re.sub(r'</div>', '\n', html_content, flags=re.IGNORECASE)

    # Remove remaining HTML tags
    html_content = re.sub(r'<[^>]+>', '', html_content)

    # Decode HTML entities
    html_content = html_content.replace('&nbsp;', ' ')
    html_content = html_content.replace('&lt;', '<')
    html_content = html_content.replace('&gt;', '>')
    html_content = html_content.replace('&amp;', '&')
    html_content = html_content.replace('&quot;', '"')
    html_content = html_content.replace('&#39;', "'")

    # Clean up whitespace
    html_content = re.sub(r'\n\s*\n\s*\n', '\n\n', html_content)
    html_content = html_content.strip()

    return f"# Source: {url}\n\n{html_content}"


def download_page(url, output_path):
    """Download a page and convert to markdown."""
    try:
        print(f"Downloading: {url}")

        response = requests.get(url, timeout=15)
        response.raise_for_status()

        # Convert HTML to markdown
        markdown = html_to_markdown(response.text, url)

        # Create directory if needed
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # Write markdown file
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
    """Convert URL path to filename, preserving directory structure."""
    if path == "/docs" or path == "/docs/":
        return "index.md"

    # Remove leading /docs/ and trailing slash
    clean_path = path.replace("/docs/", "").strip("/")

    if not clean_path:
        return "index.md"

    # Handle nested paths by creating subdirectories
    # e.g., /docs/tutorial/chapter1/installation -> tutorial/chapter1/installation.md
    if "/" in clean_path:
        parts = clean_path.split("/")
        # Last part becomes filename, rest become directory structure
        filename = parts[-1] + ".md"
        directory = "/".join(parts[:-1])
        return f"{directory}/{filename}"

    return clean_path + ".md"


def main():
    """Main function to download all RedwoodJS documentation."""
    print("=" * 60)
    print("RedwoodJS Documentation Scraper")
    print("=" * 60)
    print(f"Base URL: {BASE_URL}")
    print(f"Pages to download: {len(REDWOODJS_DOC_PAGES)}")
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "web-scraped" / "redwoodjs"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Output directory: {output_dir}")
    print()

    successful = 0
    failed = 0
    start_time = time.time()

    for i, page_path in enumerate(REDWOODJS_DOC_PAGES, 1):
        url = BASE_URL + page_path
        filename = path_to_filename(page_path)
        output_path = output_dir / filename

        print(f"[{i:3d}/{len(REDWOODJS_DOC_PAGES)}] ", end="")

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

    # Calculate total size
    total_size = sum(f.stat().st_size for f in output_dir.rglob("*.md"))
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
