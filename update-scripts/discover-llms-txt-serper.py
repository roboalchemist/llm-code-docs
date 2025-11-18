#!/usr/bin/env python3
"""
Google Search for llms.txt files via Serper.dev API

Uses Serper.dev to search Google for llms.txt files and add new sites
to the llms-sites.yaml configuration.

Note: Serper blocks search operators like 'filetype:' and 'inurl:' so we use
alternative search patterns that work around this limitation.

Usage:
    python3 discover-llms-txt-serper.py [--add-to-yaml] [--limit N]

Environment:
    SERPER_API_KEY - Your Serper.dev API key
"""

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path
from typing import List, Dict, Set
from urllib.parse import urlparse

import requests
import yaml

# Configuration
SCRIPT_DIR = Path(__file__).parent
REPO_ROOT = SCRIPT_DIR.parent
CONFIG_FILE = SCRIPT_DIR / "llms-sites.yaml"
OUTPUT_FILE = REPO_ROOT / "discovered-serper-llms-txt.json"

# API Key
SERPER_API_KEY = os.getenv('SERPER_API_KEY')


def load_existing_sites() -> Set[str]:
    """Load base URLs from existing YAML config to avoid duplicates."""
    try:
        with open(CONFIG_FILE, 'r') as f:
            config = yaml.safe_load(f)

        existing = set()
        for site in config.get('sites', []):
            base_url = site.get('base_url', '').rstrip('/')
            existing.add(base_url)

        return existing
    except Exception as e:
        print(f"Warning: Could not load existing sites: {e}", file=sys.stderr)
        return set()


def normalize_url(url: str) -> str:
    """Normalize URL for comparison."""
    parsed = urlparse(url)
    domain = parsed.netloc.replace('www.', '')
    return f"{parsed.scheme}://{domain}{parsed.path}".rstrip('/')


def extract_base_url(llms_txt_url: str) -> str:
    """Extract base URL from llms.txt URL."""
    base = llms_txt_url.replace('/llms.txt', '').replace('/llms-full.txt', '')
    if not base.endswith('/'):
        base += '/'
    return base


def search_serper(query: str, num: int = 100, max_pages: int = 5) -> List[Dict]:
    """
    Search using Serper API (Google).

    Note: Serper blocks 'filetype:' and 'inurl:' operators,
    so we use plain text queries that Google can interpret.
    """
    if not SERPER_API_KEY:
        print("ERROR: SERPER_API_KEY environment variable not set", file=sys.stderr)
        print("Get your API key from: https://serper.dev/", file=sys.stderr)
        return []

    results = []
    per_page = 100  # Serper max per request

    try:
        print(f"Searching Google via Serper: '{query}'")
        print(f"  Max pages: {max_pages}")
        print(f"  Results per page: {per_page}")
        print()

        for page in range(max_pages):
            if page * per_page >= num:
                break

            print(f"  Page {page + 1}/{max_pages}...", end=' ', flush=True)

            response = requests.post(
                'https://google.serper.dev/search',
                headers={
                    'X-API-KEY': SERPER_API_KEY,
                    'Content-Type': 'application/json'
                },
                json={
                    'q': query,
                    'num': min(per_page, num - (page * per_page)),
                    'page': page + 1
                },
                timeout=30
            )

            # Handle errors
            if response.status_code == 400:
                error_data = response.json()
                if 'Query not allowed' in error_data.get('message', ''):
                    print("✗ Query blocked (contains restricted operators)")
                    print(f"  Serper blocks operators like 'filetype:' and 'inurl:'")
                    return results
                response.raise_for_status()
            elif response.status_code != 200:
                response.raise_for_status()

            data = response.json()
            page_results = data.get('organic', [])

            if not page_results:
                print("✓ No more results")
                break

            page_count = 0
            for item in page_results:
                url = item.get('link', '')

                # Check if URL contains llms.txt
                if '/llms.txt' in url or '/llms-full.txt' in url:
                    results.append({
                        'url': url,
                        'title': item.get('title', ''),
                        'snippet': item.get('snippet', ''),
                        'source': 'serper',
                        'query': query
                    })
                    page_count += 1

            print(f"✓ Found {page_count} llms.txt URLs")

            # Rate limiting between pages
            if page < max_pages - 1:
                time.sleep(1)

        print()
        print(f"Total from this query: {len(results)} llms.txt URLs")

    except Exception as e:
        print(f"✗ Search failed: {e}", file=sys.stderr)

    return results


def dedupe_results(all_results: List[Dict], existing_sites: Set[str]) -> List[Dict]:
    """Deduplicate results and filter out existing sites."""
    seen = set()
    unique = []

    for result in all_results:
        base_url = extract_base_url(result['url'])
        normalized = normalize_url(base_url)

        # Skip if already in YAML config
        if any(normalize_url(existing) == normalized for existing in existing_sites):
            continue

        # Skip if already seen
        if normalized in seen:
            continue

        seen.add(normalized)
        result['base_url'] = base_url
        unique.append(result)

    return unique


def generate_site_name(base_url: str) -> str:
    """Generate a kebab-case name for the site."""
    parsed = urlparse(base_url)
    domain = parsed.netloc.replace('www.', '')
    domain_parts = domain.split('.')

    # Use subdomain or domain name
    if len(domain_parts) > 2 and domain_parts[0] not in ['docs', 'api', 'developer', 'developers']:
        name = domain_parts[0]
    else:
        name = domain_parts[0] if domain_parts[0] != 'docs' else (
            domain_parts[1] if len(domain_parts) > 1 else domain_parts[0]
        )

    # Add path if meaningful
    path = parsed.path.strip('/').replace('/', '-')
    if path and path not in ['docs', 'documentation', 'api']:
        name = f"{name}-{path}"

    # Sanitize
    name = re.sub(r'[^a-z0-9-]', '', name.lower())
    name = re.sub(r'-+', '-', name).strip('-')

    return name or 'unknown'


def generate_description(title: str, snippet: str, base_url: str) -> str:
    """Generate a brief description."""
    if title and len(title) > 10:
        return title[:100]
    elif snippet and len(snippet) > 10:
        return snippet[:100]
    else:
        parsed = urlparse(base_url)
        domain = parsed.netloc.replace('www.', '')
        return f"{domain} documentation"


def add_to_yaml(sites: List[Dict]) -> int:
    """Add new sites to llms-sites.yaml."""
    try:
        with open(CONFIG_FILE, 'r') as f:
            config = yaml.safe_load(f)

        existing_count = len(config.get('sites', []))

        for site in sites:
            config['sites'].append({
                'name': site['name'],
                'base_url': site['base_url'],
                'description': site['description']
            })

        # Sort by name
        config['sites'] = sorted(config['sites'], key=lambda x: x['name'])

        with open(CONFIG_FILE, 'w') as f:
            yaml.dump(config, f, default_flow_style=False, sort_keys=False, width=120)

        new_count = len(config['sites'])
        added = new_count - existing_count

        print(f"✓ Added {added} new sites to {CONFIG_FILE}")
        print(f"  Total sites: {existing_count} → {new_count}")

        return added

    except Exception as e:
        print(f"✗ Failed to update YAML: {e}", file=sys.stderr)
        return 0


def save_results(results: List[Dict], output_file: Path):
    """Save discovered sites to JSON file."""
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"✓ Saved {len(results)} sites to {output_file}")


def main():
    parser = argparse.ArgumentParser(
        description="Discover llms.txt sites using Google Search via Serper.dev"
    )
    parser.add_argument(
        '--add-to-yaml',
        action='store_true',
        help='Automatically add discovered sites to llms-sites.yaml'
    )
    parser.add_argument(
        '--limit',
        type=int,
        default=100,
        help='Max results per query (default: 100)'
    )
    parser.add_argument(
        '--max-pages',
        type=int,
        default=5,
        help='Max pages to fetch per query (default: 5)'
    )
    parser.add_argument(
        '--output',
        type=Path,
        default=OUTPUT_FILE,
        help='Output JSON file (default: discovered-serper-llms-txt.json)'
    )

    args = parser.parse_args()

    print("=" * 70)
    print("llms.txt Discovery via Serper.dev (Google Search)")
    print("=" * 70)
    print()

    if not SERPER_API_KEY:
        print("ERROR: SERPER_API_KEY environment variable not set")
        print("Set it with: export SERPER_API_KEY='your_key_here'")
        print("Get your key from: https://serper.dev/")
        return 1

    # Load existing sites
    existing_sites = load_existing_sites()
    print(f"Loaded {len(existing_sites)} existing sites from YAML")
    print()

    # Search queries that work with Serper
    # Note: Can't use filetype: or inurl: operators - Serper blocks them
    # Also can't use quoted strings - they trigger blocking
    queries = [
        '/llms.txt',
        'llms-full.txt',
        'llms.txt documentation ai',
        'llms.txt api reference',
        'llms.txt developer docs',
        'llmstxt',
        'llms.txt framework',
        'llms.txt library',
        'llms.txt sdk',
        'llms.txt platform',
        'llms.txt tool',
        'llms.txt python',
        'llms.txt javascript',
        'llms.txt typescript',
        'llms.txt api docs',
        'llms.txt getting started',
        'llms.txt tutorial',
        'llms.txt guide',
        'llms.txt reference',
        'llms.txt examples',
        'site:docs llms.txt',
        'site:developer llms.txt',
        'site:api llms.txt',
        'llms.txt machine learning',
        'llms.txt artificial intelligence',
        'llms.txt openai',
        'llms.txt anthropic',
        'llms.txt langchain',
        'llms.txt huggingface',
        'llms.txt vector database',
    ]

    all_results = []

    for query in queries:
        print(f"Query: '{query}'")
        print("-" * 70)
        results = search_serper(query, num=args.limit, max_pages=args.max_pages)
        all_results.extend(results)
        print()
        time.sleep(1)  # Rate limiting between queries

    # Deduplicate and process
    print("=" * 70)
    print("Processing Results")
    print("=" * 70)
    print()

    unique_results = dedupe_results(all_results, existing_sites)

    # Add metadata
    for result in unique_results:
        result['name'] = generate_site_name(result['base_url'])
        result['description'] = generate_description(
            result['title'],
            result['snippet'],
            result['base_url']
        )

    print(f"Total results: {len(all_results)}")
    print(f"Unique new sites: {len(unique_results)}")
    print()

    if unique_results:
        # Save to JSON
        save_results(unique_results, args.output)
        print()

        # Show top discoveries
        print("Discovered sites:")
        for i, site in enumerate(unique_results, 1):
            print(f"  {i:2d}. {site['name']}")
            print(f"      URL: {site['base_url']}")
            print(f"      Desc: {site['description']}")
            print()

        # Add to YAML if requested
        if args.add_to_yaml:
            print("=" * 70)
            print("Adding to YAML Configuration")
            print("=" * 70)
            print()
            added = add_to_yaml(unique_results)
            if added > 0:
                print()
                print(f"✓ Successfully added {added} new sites to {CONFIG_FILE}")
                print("  Run the scraper to download documentation:")
                print(f"  python3 update-scripts/llms-txt-scraper.py --workers 15")
        else:
            print("Tip: Use --add-to-yaml to automatically add these to the config")

        return 0
    else:
        print("⚠ No new sites discovered")
        return 1


if __name__ == "__main__":
    sys.exit(main())
