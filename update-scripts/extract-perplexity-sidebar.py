#!/usr/bin/env python3
"""
Extract Perplexity documentation links from sidebar navigation.

This script consolidates links extracted manually using Playwright MCP tools.
The links were extracted from three navigation tabs:
1. https://docs.perplexity.ai (main docs)
2. https://docs.perplexity.ai/api-reference/search-post (API reference)
3. https://docs.perplexity.ai/cookbook (examples)

Usage: python extract-perplexity-sidebar.py
"""

from datetime import datetime
from pathlib import Path


def main():
    """Consolidate and save all extracted documentation links."""

    # Links extracted from https://docs.perplexity.ai (after expanding 6 collapsibles)
    page1_links = [
        "https://docs.perplexity.ai/getting-started/overview",
        "https://docs.perplexity.ai/cookbook",
        "https://docs.perplexity.ai/api-reference/search-post",
        "https://docs.perplexity.ai/getting-started/pricing",
        "https://docs.perplexity.ai/guides/perplexity-sdk",
        "https://docs.perplexity.ai/guides/perplexity-sdk-error-handling",
        "https://docs.perplexity.ai/guides/perplexity-sdk-configuration",
        "https://docs.perplexity.ai/guides/perplexity-sdk-performance",
        "https://docs.perplexity.ai/guides/perplexity-sdk-type-safety",
        "https://docs.perplexity.ai/guides/perplexity-sdk-best-practices",
        "https://docs.perplexity.ai/guides/search-quickstart",
        "https://docs.perplexity.ai/guides/search-best-practices",
        "https://docs.perplexity.ai/getting-started/quickstart",
        "https://docs.perplexity.ai/getting-started/models",
        "https://docs.perplexity.ai/guides/chat-completions-sdk",
        "https://docs.perplexity.ai/guides/chat-completions-guide",
        "https://docs.perplexity.ai/guides/prompt-guide",
        "https://docs.perplexity.ai/guides/structured-outputs",
        "https://docs.perplexity.ai/guides/streaming-responses",
        "https://docs.perplexity.ai/guides/search-domain-filters",
        "https://docs.perplexity.ai/guides/academic-filter-guide",
        "https://docs.perplexity.ai/guides/date-range-filter-guide",
        "https://docs.perplexity.ai/guides/sec-guide",
        "https://docs.perplexity.ai/guides/user-location-filter-guide",
        "https://docs.perplexity.ai/guides/search-context-size-guide",
        "https://docs.perplexity.ai/guides/search-control-guide",
        "https://docs.perplexity.ai/guides/returning-images",
        "https://docs.perplexity.ai/guides/returning-videos",
        "https://docs.perplexity.ai/guides/image-attachments",
        "https://docs.perplexity.ai/guides/file-attachments",
        "https://docs.perplexity.ai/guides/mcp-server",
        "https://docs.perplexity.ai/getting-started/api-groups",
        "https://docs.perplexity.ai/guides/api-key-management",
        "https://docs.perplexity.ai/guides/rate-limits-usage-tiers",
        "https://docs.perplexity.ai/changelog/changelog",
        "https://docs.perplexity.ai/discussions/discussions",
        "https://docs.perplexity.ai/feature-roadmap",
        "https://docs.perplexity.ai/faq/faq",
        "https://docs.perplexity.ai/status/status",
        "https://docs.perplexity.ai/guides/privacy-security",
        "https://docs.perplexity.ai/guides/bots",
    ]

    # Links extracted from https://docs.perplexity.ai/api-reference/search-post (1 collapsible)
    page2_links = [
        "https://docs.perplexity.ai/api-reference/search-post",
        "https://docs.perplexity.ai/api-reference/chat-completions-post",
        "https://docs.perplexity.ai/api-reference/async-chat-completions-post",
        "https://docs.perplexity.ai/api-reference/async-chat-completions-get",
        "https://docs.perplexity.ai/api-reference/async-chat-completions-request_id-get",
        "https://docs.perplexity.ai/api-reference/generate-auth-token-post",
        "https://docs.perplexity.ai/api-reference/revoke-auth-token-post",
        "https://docs.perplexity.ai/api-reference/chat-completions-post",
    ]

    # Links extracted from https://docs.perplexity.ai/cookbook (4 collapsibles)
    page3_links = [
        "https://docs.perplexity.ai/cookbook",
        "https://docs.perplexity.ai/cookbook/examples/README",
        "https://docs.perplexity.ai/cookbook/showcase/briefo",
        "https://docs.perplexity.ai/cookbook/articles/memory-management/chat-summary-memory-buffer/README",
    ]

    # Combine all links and deduplicate
    all_links = set(page1_links + page2_links + page3_links)
    sorted_links = sorted(list(all_links))

    print("Perplexity Documentation Link Extraction")
    print("=" * 70)
    print(f"Total unique URLs: {len(sorted_links)}")

    # Save to output file
    output_file = Path(__file__).parent / 'perplexity-docs-links.txt'
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    with open(output_file, 'w') as f:
        f.write("# Perplexity Documentation Links\n")
        f.write("# Automatically extracted from sidebar navigation\n")
        f.write(f"# Generated on {timestamp}\n")
        f.write(f"# Total pages: {len(sorted_links)}\n")
        f.write("\n")

        for link in sorted_links:
            f.write(f"{link}\n")

    print(f"\n✓ Saved to: {output_file}")

    # Display sample
    print("\nFirst 10 URLs:")
    print("-" * 70)
    for i, link in enumerate(sorted_links[:10], 1):
        print(f"{i:2d}. {link}")

    if len(sorted_links) > 10:
        print(f"... and {len(sorted_links) - 10} more")

    print("\n" + "=" * 70)
    print("✓ Extraction complete!")

    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
