#!/usr/bin/env python3
"""
Simple RST to Markdown converter for Godot Engine documentation.

This handles common RST patterns found in the Godot docs:
- Headers (underlines with = - ~ etc)
- Code blocks (.. code-block::)
- Directives (.. note::, .. warning::, etc)
- Links and references
- Lists
"""

import re
from pathlib import Path


def convert_rst_to_markdown(rst_content: str) -> str:
    """Convert reStructuredText to Markdown."""

    lines = rst_content.split('\n')
    md_lines = []
    i = 0
    in_code_block = False
    in_directive = False
    directive_type = None

    while i < len(lines):
        line = lines[i]

        # Handle code blocks
        if '.. code-block::' in line:
            in_code_block = True
            # Extract language if specified
            parts = line.split('.. code-block::')
            if len(parts) > 1:
                lang = parts[1].strip()
                md_lines.append(f"```{lang}")
            else:
                md_lines.append("```")
            i += 1
            continue

        # Handle other directives (note, warning, tip, etc)
        if line.strip().startswith('.. '):
            directive_match = re.match(r'\.\.\s+(\w+)::', line)
            if directive_match:
                directive_type = directive_match.group(1)
                in_directive = True
                # Add directive as blockquote
                md_lines.append(f"> **{directive_type.upper()}**")
                i += 1
                continue

        # End code block if we see a blank line followed by non-indented content
        if in_code_block:
            if line.strip() == '':
                md_lines.append('```')
                in_code_block = False
                i += 1
                continue
            else:
                md_lines.append(line)
                i += 1
                continue

        # Handle directive content (indented lines after directive)
        if in_directive:
            if line.startswith('   ') or line.strip() == '':
                content = line.lstrip()
                if content:
                    md_lines.append(f"> {content}")
                else:
                    md_lines.append('>')
                i += 1
                continue
            else:
                in_directive = False
                directive_type = None

        # Check for RST headers (text followed by underline)
        if i + 1 < len(lines):
            next_line = lines[i + 1]
            if (line.strip() and next_line.strip() and
                all(c == next_line.strip()[0] for c in next_line.strip()) and
                len(next_line.strip()) >= len(line.strip())):

                underline_char = next_line.strip()[0]

                # Determine header level based on character
                header_map = {
                    '=': 1,
                    '-': 2,
                    '~': 3,
                    '^': 4,
                    '*': 5,
                    '+': 6,
                }

                level = header_map.get(underline_char, 2)
                md_lines.append(f"{'#' * level} {line.strip()}")
                i += 2  # Skip the underline
                continue

        # Handle inline code (backticks in RST become backticks in MD)
        # Convert ``text`` to `text`
        line = re.sub(r'``([^`]+)``', r'`\1`', line)

        # Handle references :ref:`label` -> [label]
        line = re.sub(r':ref:`([^`]+)`', r'[\1]', line)

        # Handle roles like :py:func:`name` -> `name`
        line = re.sub(r':\w+:(\w+):`([^`]+)`', r'`\2`', line)

        # Handle links :doc:`path/to/page` -> [page](path/to/page.md)
        def convert_doc_link(match):
            path = match.group(1)
            label = match.group(2) if match.group(2) else Path(path).stem
            if not path.endswith('.md'):
                path += '.md'
            return f'[{label}]({path})'

        line = re.sub(r':doc:`([^<>`]+)(?:\s*<([^>]+)>)?`', lambda m: convert_doc_link(m), line)

        # Handle external links `text <url>`_
        line = re.sub(r'`([^<>`]+)\s*<([^>]+)>`_', r'[\1](\2)', line)

        # Handle emphasis *text* -> *text* (already correct)
        # Handle strong **text** -> **text** (already correct)

        # Remove RST-specific comments
        if line.strip().startswith('.. '):
            if not ('code-block' in line or re.match(r'\.\.\s+\w+::', line)):
                i += 1
                continue

        md_lines.append(line)
        i += 1

    # Close any remaining code block
    if in_code_block:
        md_lines.append('```')

    return '\n'.join(md_lines)


def convert_rst_file(input_path: Path, output_path: Path) -> bool:
    """Convert a single RST file to Markdown."""
    try:
        with open(input_path, 'r', encoding='utf-8', errors='ignore') as f:
            rst_content = f.read()

        md_content = convert_rst_to_markdown(rst_content)

        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(md_content)

        return True
    except Exception as e:
        print(f"Error converting {input_path}: {e}")
        return False


def process_godot_docs():
    """Convert all RST files in godot-engine docs to Markdown."""

    repo_root = Path(__file__).parent.parent
    godot_docs = repo_root / "docs" / "github-scraped" / "godot-engine"

    if not godot_docs.exists():
        print(f"Error: {godot_docs} not found")
        return False

    print(f"Converting RST to Markdown in {godot_docs}...")

    rst_files = list(godot_docs.rglob("*.rst"))
    print(f"Found {len(rst_files)} RST files")

    converted = 0
    for rst_file in rst_files:
        # Create corresponding MD file
        md_file = rst_file.with_suffix('.md')

        if convert_rst_file(rst_file, md_file):
            converted += 1
            if converted % 100 == 0:
                print(f"  Converted {converted}/{len(rst_files)}...")

        # Remove the original RST file
        try:
            rst_file.unlink()
        except:
            pass

    print(f"\nConversion complete!")
    print(f"Converted {converted} files to Markdown")

    # Count final files
    md_files = list(godot_docs.rglob("*.md"))
    total_size = sum(f.stat().st_size for f in godot_docs.rglob("*") if f.is_file())

    print(f"Total Markdown files: {len(md_files)}")
    print(f"Total size: {total_size / 1024 / 1024:.2f} MB")

    return True


if __name__ == "__main__":
    import sys
    success = process_godot_docs()
    sys.exit(0 if success else 1)
