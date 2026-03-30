#!/home/gateway/miniconda3/bin/python
"""
Scraper for Bluetooth Mesh Profile v1.1 specification.
Fetches the single-page HTML spec from bluetooth.com CDN and splits into chapters.

DOM structure:
  body > div.bt-content > div.row > div.content-container > section.article
    > section.section (chapters 1-10, with UUID-based IDs)
    > h2.bridgehead (frontmatter: Revision History, Version History, Acknowledgments)
    > div.informaltable (frontmatter tables)

Source: https://www.bluetooth.com/wp-content/uploads/Files/Specification/HTML/MshPRT_v1.1/out/en/index-en.html
Output: docs/web-scraped/bluetooth-mesh-profile/
"""

import re
import shutil
import sys
from pathlib import Path

try:
    import requests
except ImportError:
    print("Error: requests not installed. Run: pip install requests")
    sys.exit(1)

try:
    from bs4 import BeautifulSoup
except ImportError:
    print("Error: beautifulsoup4 not installed. Run: pip install beautifulsoup4")
    sys.exit(1)

try:
    from markdownify import markdownify as md
except ImportError:
    print("Error: markdownify not installed. Run: pip install markdownify")
    sys.exit(1)

OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "web-scraped" / "bluetooth-mesh-profile"
SPEC_URL = "https://www.bluetooth.com/wp-content/uploads/Files/Specification/HTML/MshPRT_v1.1/out/en/index-en.html"
CACHE_PATH = Path("/tmp/btmesh.html")


def fetch_spec() -> str:
    """Fetch the full HTML spec (with local cache)."""
    if CACHE_PATH.exists() and CACHE_PATH.stat().st_size > 1_000_000:
        print(f"Using cached HTML from {CACHE_PATH}")
        return CACHE_PATH.read_text(errors='replace')

    print(f"Fetching spec from {SPEC_URL}")
    resp = requests.get(SPEC_URL, timeout=120, headers={
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
    })
    resp.raise_for_status()
    CACHE_PATH.write_text(resp.text)
    print(f"  Downloaded {len(resp.content) / 1024 / 1024:.1f} MB")
    return resp.text


def clean_markdown(text: str) -> str:
    """Clean up converted markdown."""
    # Remove trailing whitespace per line (may create new blank lines)
    text = '\n'.join(line.rstrip() for line in text.split('\n'))
    # Collapse any 2+ consecutive blank lines to a single blank line
    text = re.sub(r'\n\n\n+', '\n\n', text)
    # Normalize unordered list markers (+ to *)
    text = re.sub(r'^(\s*)\+ ', r'\1* ', text, flags=re.MULTILINE)
    # Ensure trailing newline
    text = text.strip() + '\n'
    return text


def section_to_markdown(section) -> str:
    """Convert an HTML section element to clean markdown."""
    result = md(
        str(section),
        heading_style="ATX",
        strip=['script', 'style', 'nav'],
        escape_asterisks=False,
        escape_underscores=False,
    )
    return clean_markdown(result)


def make_filename(title: str, index: int) -> str:
    """Generate a safe filename from a chapter title."""
    safe = re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')[:80]
    return f"{index:02d}-{safe}.md"


def main():
    print("=" * 70)
    print("Bluetooth Mesh Profile v1.1 Specification Scraper")
    print("=" * 70)

    html = fetch_spec()
    print(f"Parsing HTML ({len(html) / 1024 / 1024:.1f} MB)...")
    soup = BeautifulSoup(html, 'html.parser')

    # Navigate to the article section containing all content
    article = soup.find('section', class_='article')
    if not article:
        print("ERROR: Could not find section.article")
        sys.exit(1)

    # Extract chapter sections (direct children of article that are section.section)
    chapter_sections = [
        c for c in article.children
        if hasattr(c, 'name') and c.name == 'section' and 'section' in c.get('class', [])
    ]
    print(f"  Found {len(chapter_sections)} chapter sections")

    # Also collect frontmatter (h2.bridgehead elements and their associated tables)
    frontmatter_parts = []
    for child in article.children:
        if not hasattr(child, 'name') or not child.name:
            continue
        if child.name == 'h2' and 'bridgehead' in child.get('class', []):
            frontmatter_parts.append(str(child))
        elif child.name == 'div' and 'informaltable' in child.get('class', []):
            frontmatter_parts.append(str(child))
        elif child.name == 'p' and 'disclaimer' in child.get('class', []):
            frontmatter_parts.append(str(child))

    # Clear and recreate output directory
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    saved = []
    total_bytes = 0
    file_index = 0

    # Save frontmatter if substantial
    if frontmatter_parts:
        file_index += 1
        frontmatter_html = '\n'.join(frontmatter_parts)
        markdown = section_to_markdown(BeautifulSoup(frontmatter_html, 'html.parser'))
        if len(markdown) > 100:
            content = f"# Source: {SPEC_URL}\n\n{markdown}"
            filename = make_filename("frontmatter", file_index)
            filepath = OUTPUT_DIR / filename
            filepath.write_text(content, encoding='utf-8')
            size = len(content)
            total_bytes += size
            saved.append((filename, "Frontmatter", size))
            print(f"  [{len(saved):3d}] {filename} ({size / 1024:.1f} KB)")

    # Save each chapter section
    for section in chapter_sections:
        file_index += 1

        # Get the chapter title from the first heading
        heading = section.find(['h1', 'h2', 'h3', 'h4'])
        title = heading.get_text(strip=True) if heading else f"Chapter {file_index}"

        # Convert to markdown
        markdown = section_to_markdown(section)
        if len(markdown.strip()) < 50:
            print(f"  Skipping empty section: {title}")
            continue

        content = f"# Source: {SPEC_URL}\n\n{markdown}"
        filename = make_filename(title, file_index)
        filepath = OUTPUT_DIR / filename
        filepath.write_text(content, encoding='utf-8')
        size = len(content)
        total_bytes += size
        saved.append((filename, title, size))
        print(f"  [{len(saved):3d}] {filename} ({size / 1024:.1f} KB)")

    # Save INDEX.md
    index_path = OUTPUT_DIR / "INDEX.md"
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write("# Bluetooth Mesh Profile v1.1 Specification\n\n")
        f.write(f"Source: {SPEC_URL}\n\n")
        f.write("Bluetooth SIG official Mesh Profile specification covering mesh networking,\n")
        f.write("provisioning, security, transport, foundation models, proxy protocol, and GATT services.\n\n")
        f.write("## Contents\n\n")
        for fname, title, size in saved:
            f.write(f"- [{title}]({fname}) ({size / 1024:.1f} KB)\n")

    print(f"\nSaved {len(saved)} files + INDEX.md ({total_bytes / 1024:.0f} KB total)")
    print(f"Output: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
