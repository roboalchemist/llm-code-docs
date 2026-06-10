#!/usr/bin/env python3
"""
Fast local extraction - extracts all GitHub awesome list links from local repos.
"""

import re
import json
from pathlib import Path
from collections import Counter


GITHUB_LINK_PATTERN = re.compile(
    r'\[([^\]]*)\]\s*\(\s*https?://(?:www\.)?github\.com/([^/\s]+)/([^/\s#\)]+)',
    re.IGNORECASE
)


def extract_from_file(filepath: Path) -> list[tuple[str, str, str]]:
    """Extract GitHub links from a markdown file."""
    try:
        content = filepath.read_text()
    except:
        return []

    links = []
    for match in GITHUB_LINK_PATTERN.finditer(content):
        title, owner, repo = match.groups()
        repo = repo.split('#')[0].split('?')[0].rstrip('/')
        if repo and owner:
            links.append((title.strip(), owner, repo))
    return links


def is_awesome_name(name: str) -> bool:
    """Check if name suggests an awesome list."""
    name_lower = name.lower()
    indicators = ['awesome', 'curated', 'list', 'resources', 'bookmarks', 'collection']
    return any(ind in name_lower for ind in indicators)


def main():
    base = Path("/Users/joe/gitea/awesome-meta")

    # Find all markdown files in cloned repos
    all_links = []

    # Original seeds
    seed_dirs = [
        base / "sindresorhus-awesome",
        base / "bayandin-awesome",
    ]

    # Additional seeds
    seeds_dir = base / "seeds"
    if seeds_dir.exists():
        seed_dirs.extend(seeds_dir.iterdir())

    for repo_dir in seed_dirs:
        for md_file in repo_dir.rglob("*.md"):
            links = extract_from_file(md_file)
            source = f"{repo_dir.name}/{md_file.relative_to(repo_dir)}"
            for title, owner, repo in links:
                all_links.append({
                    "title": title,
                    "owner": owner,
                    "repo": repo,
                    "url": f"https://github.com/{owner}/{repo}",
                    "source": source,
                    "is_awesome": is_awesome_name(repo) or is_awesome_name(title)
                })

    # Dedupe by URL
    seen = set()
    unique_links = []
    for link in all_links:
        key = link["url"].lower()
        if key not in seen:
            seen.add(key)
            unique_links.append(link)

    # Separate awesome lists from other links
    awesome_links = [l for l in unique_links if l["is_awesome"]]
    other_links = [l for l in unique_links if not l["is_awesome"]]

    print(f"Total unique links found: {len(unique_links)}")
    print(f"  - Likely awesome lists: {len(awesome_links)}")
    print(f"  - Other links: {len(other_links)}")

    # Save results
    output = base / "output"
    output.mkdir(exist_ok=True)

    # All awesome lists
    with open(output / "awesome_from_seeds.json", "w") as f:
        json.dump({
            "total": len(awesome_links),
            "links": sorted(awesome_links, key=lambda x: x["url"].lower())
        }, f, indent=2)

    # Just URLs
    with open(output / "awesome_urls_from_seeds.txt", "w") as f:
        for link in sorted(awesome_links, key=lambda x: x["url"].lower()):
            f.write(f"{link['url']}\n")

    # Markdown list
    with open(output / "awesome_from_seeds.md", "w") as f:
        f.write("# Awesome Lists Discovered from Seeds\n\n")
        f.write(f"Total: {len(awesome_links)} awesome lists\n\n")
        for link in sorted(awesome_links, key=lambda x: x["title"].lower()):
            f.write(f"- [{link['title']}]({link['url']})\n")

    # Stats
    owner_counts = Counter(l["owner"].lower() for l in awesome_links)
    print(f"\nTop owners:")
    for owner, count in owner_counts.most_common(10):
        print(f"  {owner}: {count}")

    print(f"\nResults saved to {output}/")


if __name__ == "__main__":
    main()
