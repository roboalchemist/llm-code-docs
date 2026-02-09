#!/usr/bin/env python3
"""
Crawl specific missing Datadog API pages.
"""

import asyncio
import re
from pathlib import Path

from crawl4ai import AsyncWebCrawler
from crawl4ai.async_configs import BrowserConfig, CrawlerRunConfig

OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "web-scraped" / "datadog-api-v2"

# Missing sections to crawl
MISSING_SECTIONS = [
    "action-connection",
    "actions-datastores",
    "app-builder",
    "application-security",
    "audit",
    "authentication",
    "authn-mappings",
    "aws-integration",
    "aws-logs-integration",
    "azure-integration",
    "case-management-attribute",
    "case-management-type",
    "cloud-network-monitoring",
    "cloudflare-integration",
    "confluent-cloud",
    "container-images",
    "containers",
    "csm-agents",
    "csm-coverage-analysis",
    "csm-threats",
    "deployment-gates",
    "dora-metrics",
    "embeddable-graphs",
    "fastly-integration",
    "fleet-automation",
    "gcp-integration",
    "ip-ranges",
    "key-management",
    "logs",
    "logs-archives",
    "logs-custom-destinations",
    "logs-indexes",
    "logs-metrics",
    "logs-pipelines",
    "logs-restriction-queries",
    "microsoft-teams-integration",
    "network-device-monitoring",
    "notebooks",
    "observability-pipelines",
    "okta-integration",
    "on-call",
    "on-call-paging",
    "opsgenie-integration",
    "organizations",
    "pagerduty-integration",
    "processes",
    "product-analytics",
    "reference-tables",
    "restriction-policies",
    "rum",
    "rum-audience-management",
    "rum-metrics",
    "rum-retention-filters",
    "scim",
    "screenboards",
    "sensitive-data-scanner",
    "service-accounts",
    "service-checks",
    "service-dependencies",
    "slack-integration",
    "snapshots",
    "spa",
    "spans-metrics",
    "tags",
    "timeboards",
    "apm-retention-filters",
]


async def crawl_page(crawler, section: str) -> tuple[str, str, bool]:
    """Crawl a single page."""
    url = f"https://docs.datadoghq.com/api/latest/{section}/"

    run_config = CrawlerRunConfig(
        wait_until="networkidle",
        page_timeout=120000,
        excluded_tags=["nav", "header", "footer"],
        remove_overlay_elements=True,
    )

    try:
        result = await crawler.arun(url=url, config=run_config)
        if result.success and result.markdown and len(result.markdown) > 500:
            return (section, result.markdown, True)
        return (section, f"Too short: {len(result.markdown or '')} chars", False)
    except Exception as e:
        return (section, str(e), False)


async def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    browser_config = BrowserConfig(headless=True, verbose=True)

    print(f"Crawling {len(MISSING_SECTIONS)} missing sections...")

    async with AsyncWebCrawler(config=browser_config) as crawler:
        for i, section in enumerate(MISSING_SECTIONS):
            print(f"\n[{i+1}/{len(MISSING_SECTIONS)}] {section}")

            section_name, content, success = await crawl_page(crawler, section)

            if success:
                filepath = OUTPUT_DIR / f"{section}.md"
                url = f"https://docs.datadoghq.com/api/latest/{section}/"
                full_content = f"# Source: {url}\n\n{content}"
                filepath.write_text(full_content)
                print(f"  ✓ Saved ({len(content):,} chars)")
            else:
                print(f"  ✗ Failed: {content[:100]}")

    print(f"\nDone! Files saved to {OUTPUT_DIR}")


if __name__ == "__main__":
    asyncio.run(main())
