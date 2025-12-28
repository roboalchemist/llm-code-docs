#!/usr/bin/env python3
"""
tmux Documentation Scraper
Downloads the tmux manpage from OpenBSD and converts it to LLM-optimized markdown.
tmux is a terminal multiplexer for managing multiple terminal sessions.
"""

import os
import sys
import requests
from pathlib import Path
import time
import re
import subprocess
from bs4 import BeautifulSoup

# tmux manpage URL
TMUX_URL = "https://man.openbsd.org/OpenBSD-current/man1/tmux.1"

def parse_manpage_to_markdown(html_content, url):
    """Convert OpenBSD manpage HTML to well-structured markdown."""
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the main content area
    main = soup.find('main') or soup.find('body')
    if not main:
        raise ValueError("Could not find main content in HTML")

    markdown_lines = [f"# tmux(1) - Terminal Multiplexer", ""]
    markdown_lines.append(f"**Source**: {url}")
    markdown_lines.append("")
    markdown_lines.append("**Manual Page for tmux - OpenBSD Current**")
    markdown_lines.append("")

    current_section = None

    # Process the manpage structure
    for element in main.find_all(['h1', 'h2', 'p', 'dl', 'pre', 'div']):
        # Headers
        if element.name in ['h1', 'h2']:
            section_name = element.get_text().strip()
            if section_name and section_name not in ['tmux(1)', 'TMUX(1)']:
                current_section = section_name
                level = '#' * (2 if element.name == 'h1' else 3)
                markdown_lines.append("")
                markdown_lines.append(f"{level} {section_name}")
                markdown_lines.append("")

        # Paragraphs
        elif element.name == 'p':
            text = element.get_text().strip()
            if text:
                markdown_lines.append(text)
                markdown_lines.append("")

        # Definition lists (used for options/commands)
        elif element.name == 'dl':
            for dt, dd in zip(element.find_all('dt'), element.find_all('dd')):
                # Definition term (command/option)
                term = dt.get_text().strip()
                if term:
                    markdown_lines.append(f"**{term}**")

                # Definition description
                desc = dd.get_text().strip()
                if desc:
                    # Indent the description
                    for line in desc.split('\n'):
                        if line.strip():
                            markdown_lines.append(f"  {line.strip()}")
                    markdown_lines.append("")

        # Code blocks / Examples
        elif element.name == 'pre':
            code = element.get_text().strip()
            if code:
                markdown_lines.append("```")
                markdown_lines.append(code)
                markdown_lines.append("```")
                markdown_lines.append("")

    # Clean up extra blank lines
    markdown = '\n'.join(markdown_lines)
    markdown = re.sub(r'\n{3,}', '\n\n', markdown)

    return markdown.strip()


def clean_pandoc_markdown(markdown):
    """Clean up pandoc-generated markdown to be more LLM-friendly."""

    # Remove pandoc div/span artifacts
    markdown = re.sub(r'^:::.*$', '', markdown, flags=re.MULTILINE)
    markdown = re.sub(r'\{[^}]*\}', '', markdown)  # Remove {.class} attributes
    markdown = re.sub(r'\{#[^}]*\}', '', markdown)  # Remove {#id} anchors

    # Clean up navigation/header junk from the page
    lines = markdown.split('\n')
    clean_lines = []
    skip_until_name = True

    for line in lines:
        # Start capturing after we see "TMUX(1)" or "NAME"
        if 'TMUX(1)' in line or '## NAME' in line or '# NAME' in line:
            skip_until_name = False
            if '## NAME' in line or '# NAME' in line:
                clean_lines.append(line)
            continue

        if skip_until_name:
            continue

        # Skip navigation/form elements
        if any(skip in line for skip in ['Manual Page Search', 'All Sections', 'OpenBSD-current',
                                           'man', 'apropos', 'Search query', 'Manual header']):
            continue

        # Skip table formatting artifacts
        if re.match(r'^[-\s]+$', line):
            continue

        clean_lines.append(line)

    markdown = '\n'.join(clean_lines)

    # Convert escaped characters
    markdown = markdown.replace('\\[', '[').replace('\\]', ']')
    markdown = markdown.replace("\\'", "'")

    # Clean up excessive whitespace
    markdown = re.sub(r'\n{3,}', '\n\n', markdown)
    markdown = re.sub(r' {2,}', ' ', markdown)

    # Fix headers that might have extra formatting
    markdown = re.sub(r'^(#+)\s*\[([^\]]+)\].*$', r'\1 \2', markdown, flags=re.MULTILINE)

    return markdown.strip()


def pandoc_convert(html_content):
    """Use pandoc to convert HTML to markdown."""
    try:
        result = subprocess.run(
            ['pandoc', '-f', 'html', '-t', 'markdown', '--wrap=none'],
            input=html_content,
            capture_output=True,
            text=True,
            timeout=30
        )
        if result.returncode == 0:
            return result.stdout
        return None
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return None


def download_manpage(url, output_path):
    """Download tmux manpage and convert to markdown."""
    try:
        print(f"Downloading tmux manpage from: {url}")

        response = requests.get(url, timeout=30)
        response.raise_for_status()

        # Use pandoc to convert
        pandoc_output = pandoc_convert(response.text)

        if pandoc_output:
            # Clean up pandoc output
            markdown = clean_pandoc_markdown(pandoc_output)

            # Add header
            header = [
                "# tmux(1) - Terminal Multiplexer",
                "",
                f"**Source**: {url}",
                "",
                "**OpenBSD Manual Page - Current Version**",
                "",
                "---",
                "",
            ]
            markdown = '\n'.join(header) + markdown
        else:
            print("  -> Pandoc failed, using fallback parser")
            markdown = parse_manpage_to_markdown(response.text, url)

        # Create directory if needed
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # Write markdown file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(markdown)

        print(f"  -> Saved: {output_path}")
        print(f"  -> Size: {len(markdown):,} bytes ({len(markdown)/1024:.1f} KB)")

        return True

    except requests.exceptions.RequestException as e:
        print(f"  -> Error downloading {url}: {e}")
        return False
    except Exception as e:
        print(f"  -> Error processing {url}: {e}")
        import traceback
        traceback.print_exc()
        return False


def extract_key_sections(markdown_content, output_dir):
    """
    Extract key sections into separate files for easier LLM access.
    """
    sections = {
        'key-bindings': {
            'marker': 'DEFAULT KEY BINDINGS',
            'content': []
        },
        'commands': {
            'marker': 'CLIENTS AND SESSIONS',
            'content': []
        },
        'options': {
            'marker': 'OPTIONS',
            'content': []
        },
    }

    lines = markdown_content.split('\n')
    current_section = None
    capture_depth = 0

    for i, line in enumerate(lines):
        # Check if we're entering a section
        for section_key, section_data in sections.items():
            if section_data['marker'] in line and line.startswith('##'):
                current_section = section_key
                capture_depth = line.count('#')
                sections[section_key]['content'].append(line)
                continue

        # Check if we're exiting a section
        if current_section and line.startswith('#'):
            header_depth = len(line) - len(line.lstrip('#'))
            if header_depth <= capture_depth and i > 0:
                current_section = None
                continue

        # Capture content
        if current_section:
            sections[section_key]['content'].append(line)

    # Write extracted sections
    for section_key, section_data in sections.items():
        if section_data['content']:
            section_file = output_dir / f"{section_key}.md"
            content = '\n'.join(section_data['content'])
            with open(section_file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  -> Extracted: {section_key}.md ({len(section_data['content'])} lines)")


def main():
    """Main function to download tmux documentation."""
    print("=" * 60)
    print("tmux Documentation Scraper")
    print("=" * 60)
    print(f"Source: {TMUX_URL}")
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "web-scraped" / "tmux"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Output directory: {output_dir}")
    print()

    start_time = time.time()

    # Download main manpage
    main_output = output_dir / "tmux-manpage.md"
    success = download_manpage(TMUX_URL, main_output)

    if success:
        # Read the generated markdown
        with open(main_output, 'r', encoding='utf-8') as f:
            markdown = f.read()

        # Extract focused sections
        print()
        print("Extracting focused sections...")
        extract_key_sections(markdown, output_dir)

    elapsed = time.time() - start_time

    print()
    print("=" * 60)
    print("Download Summary")
    print("=" * 60)

    if success:
        print("✓ Successfully downloaded tmux documentation")

        # Calculate total size
        total_size = sum(f.stat().st_size for f in output_dir.glob("*.md"))
        file_count = len(list(output_dir.glob("*.md")))

        print(f"Files created: {file_count}")
        print(f"Total size: {total_size:,} bytes ({total_size/1024:.1f} KB)")
        print(f"Time: {elapsed:.1f} seconds")
        print(f"Output: {output_dir}")
        print()
        print("Documentation ready for LLM consumption!")
        sys.exit(0)
    else:
        print("✗ Failed to download tmux documentation")
        sys.exit(1)


if __name__ == "__main__":
    main()
