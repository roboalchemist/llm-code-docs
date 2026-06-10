#!/usr/bin/env python3
"""
Awesome List Crawler - Recursively discovers all awesome lists starting from seed repos.
"""

import re
import json
import time
import os
from pathlib import Path
from urllib.parse import urlparse
from collections import deque
from dataclasses import dataclass, asdict
from typing import Optional
import subprocess


@dataclass
class AwesomeRepo:
    """Represents an awesome list repository."""
    owner: str
    name: str
    url: str
    title: Optional[str] = None
    description: Optional[str] = None
    depth: int = 0  # How many hops from seed
    parent: Optional[str] = None  # Which repo linked to this one


class AwesomeCrawler:
    """Crawls GitHub to discover awesome lists."""

    # Pattern to match GitHub repo links in markdown
    GITHUB_LINK_PATTERN = re.compile(
        r'\[([^\]]+)\]\s*\(\s*https?://(?:www\.)?github\.com/([^/\s]+)/([^/\s#\)]+)',
        re.IGNORECASE
    )

    # Pattern for raw GitHub URLs
    RAW_GITHUB_PATTERN = re.compile(
        r'https?://(?:raw\.)?github(?:usercontent)?\.com/([^/]+)/([^/]+)',
        re.IGNORECASE
    )

    def __init__(self, output_dir: Path, max_depth: int = 3, delay: float = 0.5):
        self.output_dir = Path(output_dir)
        self.max_depth = max_depth
        self.delay = delay
        self.visited: set[str] = set()
        self.repos: dict[str, AwesomeRepo] = {}
        self.queue: deque[tuple[str, str, int, str]] = deque()  # (owner, name, depth, parent)
        self.failed: list[str] = []

    def repo_key(self, owner: str, name: str) -> str:
        """Generate unique key for a repo."""
        return f"{owner.lower()}/{name.lower()}"

    def extract_links_from_markdown(self, content: str) -> list[tuple[str, str, str]]:
        """Extract GitHub repo links from markdown content.

        Returns list of (title, owner, repo_name) tuples.
        """
        links = []
        for match in self.GITHUB_LINK_PATTERN.finditer(content):
            title, owner, repo = match.groups()
            # Clean up repo name (remove #readme, etc)
            repo = repo.split('#')[0].split('?')[0].rstrip('/')
            if repo and owner:
                links.append((title.strip(), owner, repo))
        return links

    def fetch_readme(self, owner: str, name: str) -> Optional[str]:
        """Fetch README content for a repo using curl."""
        readme_names = ['README.md', 'readme.md', 'Readme.md', 'README.MD', 'readme.markdown']

        for readme_name in readme_names:
            url = f"https://raw.githubusercontent.com/{owner}/{name}/HEAD/{readme_name}"
            try:
                result = subprocess.run(
                    ['curl', '-sL', '--connect-timeout', '10', '--max-time', '30', '-f', url],
                    capture_output=True,
                    text=True,
                    timeout=35
                )
                if result.returncode == 0 and result.stdout:
                    return result.stdout
            except subprocess.TimeoutExpired:
                continue
            except Exception:
                continue

        # Try master/main branches explicitly
        for branch in ['main', 'master']:
            for readme_name in readme_names[:2]:
                url = f"https://raw.githubusercontent.com/{owner}/{name}/{branch}/{readme_name}"
                try:
                    result = subprocess.run(
                        ['curl', '-sL', '--connect-timeout', '10', '--max-time', '30', '-f', url],
                        capture_output=True,
                        text=True,
                        timeout=35
                    )
                    if result.returncode == 0 and result.stdout:
                        return result.stdout
                except:
                    continue

        return None

    def is_likely_awesome_list(self, owner: str, name: str, title: str = "") -> bool:
        """Heuristic to determine if a repo is likely an awesome list."""
        name_lower = name.lower()
        title_lower = title.lower()

        # Strong indicators
        if 'awesome' in name_lower:
            return True
        if 'awesome' in title_lower:
            return True
        if name_lower.startswith('awesome-'):
            return True

        # Weaker indicators - these might be awesome lists
        weak_indicators = [
            'curated', 'list', 'resources', 'collection', 'bookmarks'
        ]
        for indicator in weak_indicators:
            if indicator in name_lower or indicator in title_lower:
                return True

        return False

    def crawl_local_file(self, filepath: Path, depth: int = 0, parent: str = "seed") -> list[tuple[str, str, str]]:
        """Extract links from a local markdown file."""
        content = filepath.read_text()
        return self.extract_links_from_markdown(content)

    def add_to_queue(self, owner: str, name: str, depth: int, parent: str, title: str = ""):
        """Add a repo to the crawl queue if not already visited."""
        key = self.repo_key(owner, name)
        if key not in self.visited and depth <= self.max_depth:
            if self.is_likely_awesome_list(owner, name, title):
                self.queue.append((owner, name, depth, parent))
                self.visited.add(key)
                return True
        return False

    def process_repo(self, owner: str, name: str, depth: int, parent: str) -> int:
        """Process a single repo, extracting links and adding to queue.

        Returns number of new repos found.
        """
        key = self.repo_key(owner, name)
        print(f"[{depth}] Processing: {owner}/{name}")

        content = self.fetch_readme(owner, name)
        if not content:
            print(f"  -> Failed to fetch README")
            self.failed.append(f"{owner}/{name}")
            return 0

        links = self.extract_links_from_markdown(content)
        new_count = 0

        # Store this repo
        self.repos[key] = AwesomeRepo(
            owner=owner,
            name=name,
            url=f"https://github.com/{owner}/{name}",
            depth=depth,
            parent=parent
        )

        # Add discovered links to queue
        for title, link_owner, link_name in links:
            if self.add_to_queue(link_owner, link_name, depth + 1, key, title):
                new_count += 1

        print(f"  -> Found {len(links)} links, {new_count} new awesome lists")
        return new_count

    def crawl(self, seeds: list[tuple[str, str]]):
        """Run the crawler starting from seed repos."""
        # Add seeds to queue
        for owner, name in seeds:
            self.add_to_queue(owner, name, 0, "seed", "Awesome")

        total_processed = 0
        while self.queue:
            owner, name, depth, parent = self.queue.popleft()

            self.process_repo(owner, name, depth, parent)
            total_processed += 1

            # Progress update
            if total_processed % 10 == 0:
                print(f"\n=== Progress: {total_processed} processed, {len(self.queue)} queued ===\n")

            # Rate limiting
            time.sleep(self.delay)

        print(f"\n=== Crawl Complete ===")
        print(f"Total repos discovered: {len(self.repos)}")
        print(f"Failed fetches: {len(self.failed)}")

    def save_results(self):
        """Save crawl results to files."""
        self.output_dir.mkdir(exist_ok=True)

        # Save as JSON
        json_path = self.output_dir / "awesome_lists.json"
        with open(json_path, 'w') as f:
            data = {
                "total": len(self.repos),
                "repos": [asdict(r) for r in self.repos.values()]
            }
            json.dump(data, f, indent=2)
        print(f"Saved JSON to {json_path}")

        # Save as simple list of URLs
        urls_path = self.output_dir / "awesome_urls.txt"
        with open(urls_path, 'w') as f:
            for repo in sorted(self.repos.values(), key=lambda r: r.url.lower()):
                f.write(f"{repo.url}\n")
        print(f"Saved URLs to {urls_path}")

        # Save categorized by depth
        depth_path = self.output_dir / "awesome_by_depth.md"
        with open(depth_path, 'w') as f:
            f.write("# Awesome Lists by Discovery Depth\n\n")
            max_depth = max(r.depth for r in self.repos.values()) if self.repos else 0
            for d in range(max_depth + 1):
                repos_at_depth = [r for r in self.repos.values() if r.depth == d]
                f.write(f"\n## Depth {d} ({len(repos_at_depth)} repos)\n\n")
                for r in sorted(repos_at_depth, key=lambda x: x.url.lower()):
                    f.write(f"- [{r.owner}/{r.name}]({r.url})\n")
        print(f"Saved depth report to {depth_path}")

        # Save failed fetches
        if self.failed:
            failed_path = self.output_dir / "failed_fetches.txt"
            with open(failed_path, 'w') as f:
                for repo in self.failed:
                    f.write(f"{repo}\n")
            print(f"Saved failed fetches to {failed_path}")


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Crawl GitHub for awesome lists')
    parser.add_argument('--max-depth', type=int, default=2,
                       help='Maximum crawl depth (default: 2)')
    parser.add_argument('--delay', type=float, default=0.3,
                       help='Delay between requests in seconds (default: 0.3)')
    parser.add_argument('--output', type=str, default='output',
                       help='Output directory (default: output)')
    args = parser.parse_args()

    # Seed repos
    seeds = [
        ("sindresorhus", "awesome"),
        ("bayandin", "awesome-awesomeness"),
        # Additional large awesome lists
        ("brillout", "awesome-react-components"),
        ("vinta", "awesome-python"),
        ("gribouille", "awesome-python"),
        ("dzharii", "awesome-typescript"),
        ("avelino", "awesome-go"),
        ("awesome-selfhosted", "awesome-selfhosted"),
        ("numetriclabz", "awesome-db"),
        ("officialrajdeepsingh", "awesome-nextjs"),
        ("bytefer", "awesome-nextjs"),
    ]

    crawler = AwesomeCrawler(
        output_dir=Path(args.output),
        max_depth=args.max_depth,
        delay=args.delay
    )

    print(f"Starting crawl with max_depth={args.max_depth}")
    print(f"Seeds: {seeds}")
    print()

    crawler.crawl(seeds)
    crawler.save_results()


if __name__ == "__main__":
    main()
