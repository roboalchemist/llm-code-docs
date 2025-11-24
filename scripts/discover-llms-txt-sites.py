#!/usr/bin/env python3
"""
Automated llms.txt Site Discovery

Uses multiple search APIs to find sites with llms.txt files:
- Brave Search API
- Exa AI
- Tavily
- Serper (Google)
- GitHub CLI search

Usage:
    python3 discover-llms-txt-sites.py [--output OUTPUT_FILE] [--limit N]
"""

import argparse
import base64
import json
import os
import re
import subprocess
import sys
import time
from collections import defaultdict
from pathlib import Path
from typing import List, Dict, Set
from urllib.parse import urlparse

import requests
import yaml

# API Keys from environment
BRAVE_API_KEY = os.getenv('BRAVE_API_KEY')
EXA_API_KEY = os.getenv('EXA_API_KEY')
TAVILY_API_KEY = os.getenv('TAVILY_API_KEY')
SERPER_API_KEY = os.getenv('SERPER_API_KEY')

# Configuration
SCRIPT_DIR = Path(__file__).parent
REPO_ROOT = SCRIPT_DIR.parent
CONFIG_FILE = SCRIPT_DIR / "llms-sites.yaml"


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


def extract_base_url(llms_txt_url: str) -> str:
    """Extract base URL from llms.txt URL."""
    # Remove /llms.txt or /llms-full.txt
    base = llms_txt_url.replace('/llms.txt', '').replace('/llms-full.txt', '')

    # Ensure trailing slash
    if not base.endswith('/'):
        base += '/'

    return base


def normalize_url(url: str) -> str:
    """Normalize URL for comparison."""
    parsed = urlparse(url)
    # Remove www prefix for comparison
    domain = parsed.netloc.replace('www.', '')
    return f"{parsed.scheme}://{domain}{parsed.path}".rstrip('/')


def search_brave(query: str, count: int = 20, max_pages: int = 5) -> List[Dict]:
    """
    Search using Brave Search API with pagination.

    Rate limits (Free tier):
    - 1 query/second
    - 2,000 queries/month
    """
    if not BRAVE_API_KEY:
        print("⚠ Brave API key not found", file=sys.stderr)
        return []

    results = []
    per_page = 20  # Brave max per request
    retry_delay = 2  # Initial retry delay for rate limit backoff

    try:
        print(f"  Brave: Searching '{query}' (up to {max_pages} pages)...")

        for page in range(max_pages):
            offset = page * per_page
            if offset >= count:
                break

            # Respect 1 query/second rate limit for free tier
            if page > 0:
                time.sleep(1.1)  # 1.1 seconds to be safe

            try:
                response = requests.get(
                    'https://api.search.brave.com/res/v1/web/search',
                    headers={'X-Subscription-Token': BRAVE_API_KEY},
                    params={'q': query, 'count': per_page, 'offset': offset},
                    timeout=30
                )

                # Handle rate limiting
                if response.status_code == 429:
                    print(f"    ⚠ Rate limit hit on page {page + 1}, stopping pagination for this query", file=sys.stderr)
                    break

                response.raise_for_status()

                data = response.json()
                page_results = data.get('web', {}).get('results', [])

                if not page_results:
                    break  # No more results

                for item in page_results:
                    url = item.get('url', '')
                    if '/llms.txt' in url or '/llms-full.txt' in url:
                        results.append({
                            'url': url,
                            'title': item.get('title', ''),
                            'description': item.get('description', ''),
                            'source': 'brave'
                        })

            except requests.exceptions.HTTPError as e:
                if e.response.status_code == 429:
                    print(f"    ⚠ Rate limit exceeded (429), skipping remaining pages", file=sys.stderr)
                    break
                raise

        print(f"    ✓ Found {len(results)} results")
    except Exception as e:
        print(f"    ✗ Brave search failed: {e}", file=sys.stderr)

    return results


def search_exa(query: str, num_results: int = 50) -> List[Dict]:
    """
    Search using Exa AI API.

    Rate limits vary by plan.
    API uses x-api-key header (not Authorization).
    """
    if not EXA_API_KEY:
        print("⚠ Exa API key not found", file=sys.stderr)
        return []

    results = []
    try:
        print(f"  Exa: Searching '{query}'...")
        response = requests.post(
            'https://api.exa.ai/search',
            headers={
                'x-api-key': EXA_API_KEY,
                'Content-Type': 'application/json'
            },
            json={
                'query': query,
                'numResults': min(num_results, 10),  # Free tier limit
                'type': 'auto'
            },
            timeout=30
        )
        response.raise_for_status()

        data = response.json()
        for item in data.get('results', []):
            url = item.get('url', '')
            if '/llms.txt' in url or '/llms-full.txt' in url:
                results.append({
                    'url': url,
                    'title': item.get('title', ''),
                    'description': item.get('snippet', '')[:200] if item.get('snippet') else '',
                    'source': 'exa'
                })

        print(f"    ✓ Found {len(results)} results")
    except Exception as e:
        print(f"    ✗ Exa search failed: {e}", file=sys.stderr)

    return results


def search_tavily(query: str, max_results: int = 20) -> List[Dict]:
    """
    Search using Tavily API.

    Rate limits vary by plan.
    Max 5 results on free tier.
    """
    if not TAVILY_API_KEY:
        print("⚠ Tavily API key not found", file=sys.stderr)
        return []

    results = []
    try:
        print(f"  Tavily: Searching '{query}'...")
        response = requests.post(
            'https://api.tavily.com/search',
            headers={'Content-Type': 'application/json'},
            json={
                'api_key': TAVILY_API_KEY,
                'query': query,
                'max_results': min(max_results, 5),  # Free tier limit
                'search_depth': 'basic',
                'include_raw_content': False,
                'include_answer': False
            },
            timeout=30
        )
        response.raise_for_status()

        data = response.json()
        for item in data.get('results', []):
            url = item.get('url', '')
            if '/llms.txt' in url or '/llms-full.txt' in url:
                results.append({
                    'url': url,
                    'title': item.get('title', ''),
                    'description': item.get('content', '')[:200],
                    'source': 'tavily'
                })

        print(f"    ✓ Found {len(results)} results")
    except Exception as e:
        print(f"    ✗ Tavily search failed: {e}", file=sys.stderr)

    return results


def search_serper(query: str, num: int = 100, max_pages: int = 3) -> List[Dict]:
    """
    Search using Serper API (Google) with pagination.

    Note: Serper blocks certain search operators like 'inurl:' and 'filetype:'
    Rate limits vary by plan.
    """
    if not SERPER_API_KEY:
        print("⚠ Serper API key not found", file=sys.stderr)
        return []

    results = []
    per_page = 100  # Serper max per request

    try:
        print(f"  Serper: Searching '{query}' (up to {max_pages} pages)...")

        for page in range(max_pages):
            if page * per_page >= num:
                break

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

            # Handle query restrictions
            if response.status_code == 400:
                error_data = response.json()
                if 'Query not allowed' in error_data.get('message', ''):
                    print(f"    ⚠ Serper doesn't allow this query (contains restricted operators)", file=sys.stderr)
                    break  # Skip remaining pages for this query
                response.raise_for_status()
            elif response.status_code != 200:
                response.raise_for_status()

            data = response.json()
            page_results = data.get('organic', [])

            if not page_results:
                break  # No more results

            for item in page_results:
                url = item.get('link', '')
                if '/llms.txt' in url or '/llms-full.txt' in url:
                    results.append({
                        'url': url,
                        'title': item.get('title', ''),
                        'description': item.get('snippet', ''),
                        'source': 'serper'
                    })

            time.sleep(1)  # Rate limiting between pages

        print(f"    ✓ Found {len(results)} results")
    except Exception as e:
        print(f"    ✗ Serper search failed: {e}", file=sys.stderr)

    return results


def search_github_cli() -> List[Dict]:
    """Search GitHub for llms.txt using gh CLI."""
    results = []

    try:
        print("  GitHub CLI: Searching for llms.txt files...")

        # Search for code containing llms.txt URLs
        queries = [
            'llms.txt path:README.md',
            'llms-full.txt path:README.md',
            '"llms.txt" "llmstxt" path:README',
            'awesome-llms-txt'
        ]

        for query in queries:
            try:
                # Use gh search code
                cmd = ['gh', 'search', 'code', query, '--limit', '50', '--json', 'path,repository,url']
                proc = subprocess.run(cmd, capture_output=True, text=True, timeout=30)

                if proc.returncode == 0:
                    data = json.loads(proc.stdout)

                    # Fetch the actual content of README files
                    for item in data:
                        repo = item.get('repository', {}).get('nameWithOwner', '')
                        file_path = item.get('path', '')

                        if repo and 'README' in file_path.upper():
                            # Get raw content
                            raw_cmd = ['gh', 'api', f'/repos/{repo}/contents/{file_path}', '--jq', '.content']
                            raw_proc = subprocess.run(raw_cmd, capture_output=True, text=True, timeout=15)

                            if raw_proc.returncode == 0:
                                content = base64.b64decode(raw_proc.stdout).decode('utf-8', errors='ignore')

                                # Extract llms.txt URLs
                                url_pattern = r'https?://[^\s\)\]]+/llms(?:-full)?\.txt'
                                for match in re.finditer(url_pattern, content):
                                    results.append({
                                        'url': match.group(0),
                                        'title': f'Found in {repo}',
                                        'description': f'Discovered in GitHub repository {repo}',
                                        'source': 'github-cli'
                                    })

                            time.sleep(0.5)  # Rate limiting

                time.sleep(1)
            except subprocess.TimeoutExpired:
                print(f"    ⚠ Timeout searching for '{query}'", file=sys.stderr)
            except Exception as e:
                print(f"    ⚠ Error searching '{query}': {e}", file=sys.stderr)

        # Also check known awesome lists directly
        known_repos = [
            'thedaviddias/llms-txt-hub',
            'SecretiveShell/Awesome-llms-txt',
            'krish-adi/llmstxt-site'
        ]

        for repo in known_repos:
            try:
                cmd = ['gh', 'api', f'/repos/{repo}/contents/README.md', '--jq', '.content']
                proc = subprocess.run(cmd, capture_output=True, text=True, timeout=15)

                if proc.returncode == 0:
                    content = base64.b64decode(proc.stdout).decode('utf-8', errors='ignore')

                    url_pattern = r'https?://[^\s\)\]]+/llms(?:-full)?\.txt'
                    for match in re.finditer(url_pattern, content):
                        results.append({
                            'url': match.group(0),
                            'title': f'Found in {repo}',
                            'description': f'From awesome list {repo}',
                            'source': 'github-cli'
                        })
            except Exception as e:
                print(f"    ⚠ Error fetching {repo}: {e}", file=sys.stderr)

        print(f"    ✓ Found {len(results)} results")
    except Exception as e:
        print(f"    ✗ GitHub CLI search failed: {e}", file=sys.stderr)

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

        # Skip if we've already seen this in results
        if normalized in seen:
            continue

        seen.add(normalized)
        result['base_url'] = base_url
        unique.append(result)

    return unique


def generate_site_name(base_url: str, title: str) -> str:
    """Generate a kebab-case name for the site."""
    parsed = urlparse(base_url)

    # Try to extract meaningful name from domain
    domain = parsed.netloc.replace('www.', '')
    domain_parts = domain.split('.')

    # Use subdomain or domain name
    if len(domain_parts) > 2 and domain_parts[0] not in ['docs', 'api', 'developer', 'developers']:
        name = domain_parts[0]
    else:
        name = domain_parts[0] if domain_parts[0] != 'docs' else domain_parts[1] if len(domain_parts) > 1 else domain_parts[0]

    # Add path if meaningful
    path = parsed.path.strip('/').replace('/', '-')
    if path and path not in ['docs', 'documentation', 'api']:
        name = f"{name}-{path}"

    # Sanitize
    name = re.sub(r'[^a-z0-9-]', '', name.lower())
    name = re.sub(r'-+', '-', name).strip('-')

    return name or 'unknown'


def generate_description(title: str, description: str, base_url: str) -> str:
    """Generate a brief description from available info."""
    if title and len(title) > 10:
        return title[:100]
    elif description and len(description) > 10:
        return description[:100]
    else:
        parsed = urlparse(base_url)
        domain = parsed.netloc.replace('www.', '')
        return f"{domain} documentation"


def save_results(results: List[Dict], output_file: Path):
    """Save discovered sites to JSON file."""
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"\n✓ Saved {len(results)} new sites to {output_file}")


def main():
    parser = argparse.ArgumentParser(
        description="Discover llms.txt-compliant sites using multiple search APIs"
    )
    parser.add_argument(
        '--output',
        type=Path,
        default=REPO_ROOT / 'discovered-llms-txt-sites.json',
        help='Output JSON file (default: discovered-llms-txt-sites.json)'
    )
    parser.add_argument(
        '--limit',
        type=int,
        default=100,
        help='Max results per search API (default: 100)'
    )
    parser.add_argument(
        '--max-pages',
        type=int,
        default=5,
        help='Max pages to fetch per API (default: 5, increases total results)'
    )
    parser.add_argument(
        '--queries',
        nargs='+',
        default=['inurl:/llms.txt filetype:txt', 'llms-full.txt', 'llms.txt documentation'],
        help='Search queries to use'
    )

    args = parser.parse_args()

    print("=" * 70)
    print("llms.txt Site Discovery")
    print("=" * 70)
    print(f"Output: {args.output}")
    print(f"Limit: {args.limit} results per API")
    print(f"Max pages: {args.max_pages} per API (total up to {args.limit * args.max_pages} results)")
    print(f"Queries: {args.queries}")
    print()

    # Load existing sites
    existing_sites = load_existing_sites()
    print(f"Loaded {len(existing_sites)} existing sites from YAML\n")

    # Collect results from all sources
    all_results = []

    for query in args.queries:
        print(f"Query: '{query}'")
        print("-" * 70)

        # Run searches sequentially to avoid rate limits
        all_results.extend(search_brave(query, count=args.limit, max_pages=args.max_pages))
        time.sleep(1)

        all_results.extend(search_exa(query, num_results=args.limit))
        time.sleep(1)

        all_results.extend(search_tavily(query, max_results=min(args.limit, 20)))
        time.sleep(1)

        all_results.extend(search_serper(query, num=args.limit, max_pages=args.max_pages))
        time.sleep(1)

        print()

    # GitHub search (once, not per query)
    print("Searching GitHub repositories...")
    print("-" * 70)
    all_results.extend(search_github_cli())
    print()

    # Deduplicate
    print("=" * 70)
    print("Processing Results")
    print("=" * 70)
    unique_results = dedupe_results(all_results, existing_sites)

    # Add metadata
    for result in unique_results:
        result['name'] = generate_site_name(result['base_url'], result['title'])
        result['description'] = generate_description(
            result['title'],
            result['description'],
            result['base_url']
        )

    print(f"Total results found: {len(all_results)}")
    print(f"Unique new sites: {len(unique_results)}")

    # Group by source
    by_source = defaultdict(int)
    for result in unique_results:
        by_source[result['source']] += 1

    print("\nBy source:")
    for source, count in sorted(by_source.items()):
        print(f"  {source}: {count}")

    # Save results
    if unique_results:
        save_results(unique_results, args.output)

        print("\nTop 10 discovered sites:")
        for i, site in enumerate(unique_results[:10], 1):
            print(f"  {i}. {site['name']} ({site['base_url']})")
    else:
        print("\n⚠ No new sites discovered")

    return 0 if unique_results else 1


if __name__ == "__main__":
    sys.exit(main())
