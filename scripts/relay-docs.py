#!/usr/bin/env python3
"""
Relay Documentation Scraper
Downloads all Relay documentation pages and converts to markdown.
Relay is a powerful GraphQL client for React.
"""

import os
import sys
import requests
from pathlib import Path
from urllib.parse import urlparse
import time
import re
import subprocess

# Relay documentation pages from sitemap (v20.1.0 - current stable)
RELAY_DOC_PAGES = [
    "/docs/",
    "/docs/api-reference/commit-mutation/",
    "/docs/api-reference/entrypoint-container/",
    "/docs/api-reference/fetch-query/",
    "/docs/api-reference/field-logger/",
    "/docs/api-reference/graphql-and-directives/",
    "/docs/api-reference/load-entrypoint/",
    "/docs/api-reference/load-query/",
    "/docs/api-reference/relay-environment-provider/",
    "/docs/api-reference/relay-resolvers/docblock-format/",
    "/docs/api-reference/relay-resolvers/runtime-functions/",
    "/docs/api-reference/relay-runtime/api-reference/observe-fragment/",
    "/docs/api-reference/relay-runtime/relay-environment/",
    "/docs/api-reference/request-subscription/",
    "/docs/api-reference/runtime-config/",
    "/docs/api-reference/store/",
    "/docs/api-reference/types/CacheConfig/",
    "/docs/api-reference/types/Disposable/",
    "/docs/api-reference/types/GraphQLSubscriptionConfig/",
    "/docs/api-reference/types/MutationConfig/",
    "/docs/api-reference/types/SelectorStoreUpdater/",
    "/docs/api-reference/types/UploadableMap/",
    "/docs/api-reference/use-client-query/",
    "/docs/api-reference/use-entrypoint-loader/",
    "/docs/api-reference/use-fragment/",
    "/docs/api-reference/use-lazy-load-query/",
    "/docs/api-reference/use-mutation/",
    "/docs/api-reference/use-pagination-fragment/",
    "/docs/api-reference/use-prefetchable-forward-pagination-fragment/",
    "/docs/api-reference/use-preloaded-query/",
    "/docs/api-reference/use-query-loader/",
    "/docs/api-reference/use-refetchable-fragment/",
    "/docs/api-reference/use-relay-environment/",
    "/docs/api-reference/use-subscription/",
    "/docs/api-reference/wait-for-fragment-data/",
    "/docs/community-learning-resources/",
    "/docs/debugging/declarative-mutation-directives/",
    "/docs/debugging/disallowed-id-types-error/",
    "/docs/debugging/inconsistent-typename-error/",
    "/docs/debugging/relay-devtools/",
    "/docs/debugging/why-null/",
    "/docs/editor-support/",
    "/docs/error-reference/unknown-field/",
    "/docs/getting-started/babel-plugin/",
    "/docs/getting-started/compiler-config/",
    "/docs/getting-started/lint-rules/",
    "/docs/getting-started/production/",
    "/docs/getting-started/quick-start/",
    "/docs/glossary/",
    "/docs/guided-tour/accessing-data-without-react/retaining-queries/",
    "/docs/guided-tour/list-data/advanced-pagination/",
    "/docs/guided-tour/list-data/connections/",
    "/docs/guided-tour/list-data/introduction/",
    "/docs/guided-tour/list-data/pagination/",
    "/docs/guided-tour/list-data/rendering-connections/",
    "/docs/guided-tour/list-data/streaming-pagination/",
    "/docs/guided-tour/list-data/updating-connections/",
    "/docs/guided-tour/refetching/refetching-queries-with-different-data/",
    "/docs/guided-tour/refetching/refreshing-queries/",
    "/docs/guided-tour/rendering/environment/",
    "/docs/guided-tour/rendering/error-states/",
    "/docs/guided-tour/rendering/fragments/",
    "/docs/guided-tour/rendering/loading-states/",
    "/docs/guided-tour/rendering/queries/",
    "/docs/guided-tour/rendering/variables/",
    "/docs/guided-tour/reusing-cached-data/",
    "/docs/guided-tour/reusing-cached-data/fetch-policies/",
    "/docs/guided-tour/reusing-cached-data/filling-in-missing-data/",
    "/docs/guided-tour/reusing-cached-data/presence-of-data/",
    "/docs/guided-tour/reusing-cached-data/rendering-partially-cached-data/",
    "/docs/guided-tour/reusing-cached-data/staleness-of-data/",
    "/docs/guided-tour/updating-data/client-only-data/",
    "/docs/guided-tour/updating-data/graphql-mutations/",
    "/docs/guided-tour/updating-data/graphql-subscriptions/",
    "/docs/guided-tour/updating-data/imperatively-modifying-linked-fields/",
    "/docs/guided-tour/updating-data/imperatively-modifying-store-data-unsafe/",
    "/docs/guided-tour/updating-data/imperatively-modifying-store-data/",
    "/docs/guided-tour/updating-data/introduction/",
    "/docs/guided-tour/updating-data/local-data-updates/",
    "/docs/guided-tour/updating-data/typesafe-updaters-faq/",
    "/docs/guides/alias-directive/",
    "/docs/guides/catch-directive/",
    "/docs/guides/client-schema-extensions/",
    "/docs/guides/codemods/",
    "/docs/guides/compiler/",
    "/docs/guides/data-driven-dependencies/client-3d/",
    "/docs/guides/data-driven-dependencies/configuration/",
    "/docs/guides/data-driven-dependencies/introduction/",
    "/docs/guides/data-driven-dependencies/server-3d/",
    "/docs/guides/graphql-server-specification/",
    "/docs/guides/network-layer/",
    "/docs/guides/persisted-queries/",
    "/docs/guides/relay-resolvers/context/",
    "/docs/guides/relay-resolvers/defining-fields/",
    "/docs/guides/relay-resolvers/defining-types/",
    "/docs/guides/relay-resolvers/deprecated/",
    "/docs/guides/relay-resolvers/derived-fields/",
    "/docs/guides/relay-resolvers/descriptions/",
    "/docs/guides/relay-resolvers/enabling-resolvers/",
    "/docs/guides/relay-resolvers/errors/",
    "/docs/guides/relay-resolvers/field-arguments/",
    "/docs/guides/relay-resolvers/introduction/",
    "/docs/guides/relay-resolvers/limitations/",
    "/docs/guides/relay-resolvers/live-fields/",
    "/docs/guides/relay-resolvers/return-types/",
    "/docs/guides/relay-resolvers/suspense/",
    "/docs/guides/required-directive/",
    "/docs/guides/semantic-nullability/",
    "/docs/guides/testing-relay-components/",
    "/docs/guides/testing-relay-with-preloaded-queries/",
    "/docs/guides/throw-on-field-error-directive/",
    "/docs/guides/type-emission/",
    "/docs/principles-and-architecture/architecture-overview/",
    "/docs/principles-and-architecture/compiler-architecture/",
    "/docs/principles-and-architecture/runtime-architecture/",
    "/docs/principles-and-architecture/thinking-in-graphql/",
    "/docs/principles-and-architecture/thinking-in-relay/",
    "/docs/principles-and-architecture/videos/",
    "/docs/tutorial/arrays-lists/",
    "/docs/tutorial/fragments-1/",
    "/docs/tutorial/graphql/",
    "/docs/tutorial/interfaces-polymorphism/",
    "/docs/tutorial/intro/",
    "/docs/tutorial/mutations-updates/",
    "/docs/tutorial/organizing-mutations-queries-and-subscriptions/",
    "/docs/tutorial/queries-1/",
    "/docs/tutorial/queries-2/",
    "/docs/tutorial/refetchable-fragments/",
]

BASE_URL = "https://relay.dev"


def html_to_markdown(html_content, url):
    """Convert HTML to markdown, extracting main content only."""
    # Docusaurus uses <article> for main content
    article_match = re.search(
        r'<article[^>]*>(.*?)</article>',
        html_content, flags=re.DOTALL | re.IGNORECASE
    )

    if article_match:
        html_content = article_match.group(1)
    else:
        # Try alternate selector for Docusaurus
        main_match = re.search(
            r'<div[^>]*class="[^"]*markdown[^"]*"[^>]*>(.*?)</div>\s*</article>',
            html_content, flags=re.DOTALL | re.IGNORECASE
        )
        if main_match:
            html_content = main_match.group(1)

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
    """Convert URL path to filename."""
    if path == "/docs/" or path == "/docs":
        return "index.md"

    # Remove /docs/ prefix and trailing slash
    clean_path = path.replace("/docs/", "").strip("/")

    # Handle nested paths like /api-reference/use-fragment/
    if "/" in clean_path:
        # Convert to flat filename: api-reference/use-fragment -> api-reference-use-fragment.md
        return clean_path.replace("/", "-") + ".md"

    return clean_path + ".md"


def main():
    """Main function to download all Relay documentation."""
    print("=" * 60)
    print("Relay Documentation Scraper")
    print("=" * 60)
    print(f"Base URL: {BASE_URL}")
    print(f"Pages to download: {len(RELAY_DOC_PAGES)}")
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "web-scraped" / "relay"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Output directory: {output_dir}")
    print()

    successful = 0
    failed = 0
    start_time = time.time()

    for i, page_path in enumerate(RELAY_DOC_PAGES, 1):
        url = BASE_URL + page_path
        filename = path_to_filename(page_path)
        output_path = output_dir / filename

        print(f"[{i:3d}/{len(RELAY_DOC_PAGES)}] ", end="")

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
