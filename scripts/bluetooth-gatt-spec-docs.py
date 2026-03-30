#!/usr/bin/env python3
"""
Scraper for the Bluetooth Core Specification Part G — Generic Attribute Profile (GATT).

Fetches the single-page HTML spec from bluetooth.com and splits it into logical
section files based on the top-level numbered chapters (section numbers 1–N).
HTML is converted to clean Markdown using markdownify.

Output: ~/github/llm-code-docs/docs/web-scraped/bluetooth-gatt-spec/
"""

import re
import sys
from pathlib import Path

import requests
from bs4 import BeautifulSoup, Tag
import markdownify as md_lib

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

SOURCE_URL = (
    "https://www.bluetooth.com/wp-content/uploads/Files/Specification/HTML/"
    "Core-54/out/en/host/generic-attribute-profile--gatt-.html"
)

OUTPUT_DIR = Path.home() / "github/llm-code-docs/docs/web-scraped/bluetooth-gatt-spec"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
}


# ---------------------------------------------------------------------------
# Markdownify customisation
# ---------------------------------------------------------------------------

class GattMarkdownConverter(md_lib.MarkdownConverter):
    """
    Custom converter that normalises headings for the Bluetooth spec HTML.

    The spec uses h3 for the Part G title, h4 for top-level chapters,
    h5 for subsections, h6 for sub-subsections.  We remap these so that
    each output file starts with a single # heading.
    """

    # Remap tag level → ATX heading depth
    _HEADING_MAP = {3: 1, 4: 2, 5: 3, 6: 4}

    def convert_hN(self, n, el, text, parent_tags):
        level = self._HEADING_MAP.get(n, n)
        hashes = "#" * level
        return f"\n\n{hashes} {text.strip()}\n\n"

    def convert_img(self, el, text, parent_tags):
        alt = el.get("alt", "image")
        src = el.get("src", "")
        return f"\n\n![{alt}]({src})\n\n"


def html_to_md(html_fragment: str) -> str:
    """Convert an HTML fragment string to clean Markdown."""
    md = GattMarkdownConverter(
        heading_style=md_lib.ATX,
        bullets="-",
        strip=["script", "style"],
    ).convert(html_fragment)

    # Collapse 3+ consecutive blank lines to 2
    md = re.sub(r"\n{3,}", "\n\n", md)
    return md.strip()


# ---------------------------------------------------------------------------
# Section extraction
# ---------------------------------------------------------------------------

def extract_section_title(section_el: Tag) -> tuple:
    """
    Return (number, title) for a section element.

    The spec heading structure is:
      div.titlepage > div > div.title > hN.title
        > span.formal-number + span.formal-label-delimiter + span.formal-title
    """
    titlepage = section_el.find("div", class_="titlepage", recursive=False)
    if not titlepage:
        return "", ""

    heading = titlepage.find(["h1", "h2", "h3", "h4", "h5", "h6"])
    if not heading:
        return "", ""

    number_span = heading.find("span", class_="formal-number")
    title_span = heading.find("span", class_="formal-title")

    number = number_span.get_text(strip=True) if number_span else ""
    title = title_span.get_text(strip=True) if title_span else heading.get_text(strip=True)

    return number.strip(), title.strip()


def slugify(text: str) -> str:
    """Turn a title string into a safe filename component."""
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = text.strip("-")
    return text[:60]


# ---------------------------------------------------------------------------
# Main scraper
# ---------------------------------------------------------------------------

def fetch_html(url: str) -> str:
    print(f"Fetching {url} ...")
    resp = requests.get(url, headers=HEADERS, timeout=60)
    resp.raise_for_status()
    print(f"  -> {resp.status_code}, {len(resp.content):,} bytes")
    return resp.text


def strip_chrome(soup: BeautifulSoup) -> None:
    """Remove site navigation, headers, footers, and search cruft."""
    for selector_class in [
        "site-header", "skipnav", "breadcrumb", "search-results",
        "pager", "site-footer", "navbar",
    ]:
        for el in soup.find_all(class_=selector_class):
            el.decompose()

    for id_ in ["top-pager", "bottom-pager", "navbar"]:
        el = soup.find(id=id_)
        if el:
            el.decompose()

    for tag in soup.find_all(["header", "footer", "nav"]):
        tag.decompose()


def parse_chapters(soup: BeautifulSoup) -> tuple:
    """
    Locate the Part G section wrapper and extract direct-child chapter sections.

    Returns:
        (part_g_section, chapters, preamble_html)
    where chapters is a list of dicts with keys: number, title, el.
    """
    content_div = soup.find(id="topic-content")
    if not content_div:
        raise ValueError("Could not find #topic-content in the HTML")

    # The outermost section is the Part G publication wrapper
    part_g_section = content_div.find("section", class_="reused-publication")
    if not part_g_section:
        part_g_section = content_div.find("section")
    if not part_g_section:
        raise ValueError("Could not find the Part G section wrapper")

    # Collect preamble content (before the first child section)
    preamble_parts = []
    chapters = []

    for child in part_g_section.children:
        if not isinstance(child, Tag):
            continue
        if child.name == "section":
            number, title = extract_section_title(child)
            if title:
                chapters.append({"number": number, "title": title, "el": child})
        else:
            preamble_parts.append(str(child))

    preamble_html = "".join(preamble_parts)
    return part_g_section, chapters, preamble_html


def write_file(
    output_dir: Path,
    filename: str,
    html_fragment: str,
    source_url: str,
) -> Path:
    """Convert HTML fragment to markdown and write the output file."""
    md_content = html_to_md(html_fragment)
    full_content = f"# Source: {source_url}\n\n{md_content}\n"

    filepath = output_dir / filename
    filepath.write_text(full_content, encoding="utf-8")
    print(f"  Wrote {filename} ({len(full_content):,} chars, {len(md_content.splitlines())} lines)")
    return filepath


def main():
    output_dir = OUTPUT_DIR
    output_dir.mkdir(parents=True, exist_ok=True)

    # 1. Fetch
    html = fetch_html(SOURCE_URL)

    # 2. Parse
    print("Parsing HTML ...")
    soup = BeautifulSoup(html, "html.parser")
    strip_chrome(soup)

    part_g_section, chapters, preamble_html = parse_chapters(soup)
    print(f"Found {len(chapters)} top-level chapters")

    written_files = []

    # 3. Write preamble (Part G abstract / titlepage).
    # preamble_html already contains the titlepage div as a direct child of part_g_section,
    # so we use it as-is without re-adding titlepage.
    if preamble_html.strip():
        fp = write_file(output_dir, "00-preamble.md", preamble_html, SOURCE_URL)
        written_files.append(fp)

    # 4. Write each chapter
    for idx, chapter in enumerate(chapters, start=1):
        number = chapter["number"]
        title = chapter["title"]
        el = chapter["el"]

        title_slug = slugify(title)
        filename = f"{idx:02d}-{title_slug}.md"
        print(f"  Processing chapter {number} — {title}")

        fp = write_file(output_dir, filename, str(el), SOURCE_URL)
        written_files.append(fp)

    print(f"\nDone. {len(written_files)} files written to {output_dir}/")
    return written_files


if __name__ == "__main__":
    main()
