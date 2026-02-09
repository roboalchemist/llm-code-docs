#!/usr/bin/env python3
"""
SiYuan Documentation Extractor
Downloads SiYuan documentation from GitHub repository and converts .sy files to Markdown.
SiYuan is a privacy-first, self-hosted personal knowledge management system with Markdown editing,
block-level references, and local-first data storage.
"""

import json
import os
import sys
import shutil
import tempfile
from pathlib import Path
import subprocess

# Repository configuration
REPO_URL = "https://github.com/siyuan-note/user-guide-en_US.git"
REPO_BRANCH = "master"
SOURCE_DOCS_FOLDER = "."


def extract_text_from_node(node: dict) -> str:
    """Recursively extract text content from a node."""
    node_type = node.get("Type", "")

    # Direct text content
    if node_type == "NodeText":
        return node.get("Data", "")

    # Code span content
    if node_type == "NodeCodeSpanContent":
        return node.get("Data", "")

    # Link - extract text and destination
    if node_type == "NodeLink":
        link_text = ""
        link_dest = ""
        for child in node.get("Children", []):
            child_type = child.get("Type", "")
            if child_type == "NodeLinkText":
                link_text = child.get("Data", "")
            elif child_type == "NodeLinkDest":
                link_dest = child.get("Data", "")
        return f"[{link_text}]({link_dest})"

    # Inline code
    if node_type == "NodeCodeSpan":
        content = ""
        for child in node.get("Children", []):
            if child.get("Type") == "NodeCodeSpanContent":
                content = child.get("Data", "")
                break
        return f"`{content}`"

    # Keyboard shortcut
    if node_type == "NodeKbd":
        content = ""
        for child in node.get("Children", []):
            if child.get("Type") == "NodeText":
                content += child.get("Data", "")
        return f"<kbd>{content}</kbd>"

    # Emphasis (italic)
    if node_type == "NodeEmphasis":
        content = "".join(extract_text_from_node(c) for c in node.get("Children", []))
        return f"*{content}*"

    # Strong (bold)
    if node_type == "NodeStrong":
        content = "".join(extract_text_from_node(c) for c in node.get("Children", []))
        return f"**{content}**"

    # Strikethrough
    if node_type == "NodeStrikethrough":
        content = "".join(extract_text_from_node(c) for c in node.get("Children", []))
        return f"~~{content}~~"

    # Mark (highlight)
    if node_type == "NodeMark":
        content = "".join(extract_text_from_node(c) for c in node.get("Children", []))
        return f"=={content}=="

    # Block reference
    if node_type == "NodeBlockRef":
        ref_text = ""
        for child in node.get("Children", []):
            if child.get("Type") == "NodeBlockRefText":
                ref_text = child.get("Data", "")
                break
        return ref_text if ref_text else "[block reference]"

    # Skip marker nodes
    if node_type in ("NodeHeadingC8hMarker", "NodeOpenBracket", "NodeCloseBracket",
                     "NodeOpenParen", "NodeCloseParen", "NodeCodeSpanOpenMarker",
                     "NodeCodeSpanCloseMarker", "NodeKbdOpenMarker", "NodeKbdCloseMarker",
                     "NodeEmA6kOpenMarker", "NodeEmA6kCloseMarker",
                     "NodeStrongA6kOpenMarker", "NodeStrongA6kCloseMarker"):
        return ""

    # Recurse into children
    if "Children" in node:
        return "".join(extract_text_from_node(c) for c in node["Children"])

    return ""


def convert_node_to_markdown(node: dict, indent: int = 0) -> str:
    """Convert a SiYuan node to Markdown."""
    node_type = node.get("Type", "")
    result = []

    # Document - extract title and process children
    if node_type == "NodeDocument":
        title = node.get("Properties", {}).get("title", "")
        if title:
            result.append(f"# {title}\n")
        for child in node.get("Children", []):
            md = convert_node_to_markdown(child, indent)
            if md:
                result.append(md)
        return "\n".join(result)

    # Heading
    if node_type == "NodeHeading":
        level = node.get("HeadingLevel", 1)
        text = extract_text_from_node(node)
        return f"{'#' * level} {text}\n"

    # Paragraph
    if node_type == "NodeParagraph":
        text = extract_text_from_node(node)
        if text.strip():
            return f"{text}\n"
        return ""

    # List
    if node_type == "NodeList":
        list_data = node.get("ListData", {})
        is_ordered = list_data.get("Typ") == 1
        items = []
        num = list_data.get("Start", 1) or 1
        for child in node.get("Children", []):
            if child.get("Type") == "NodeListItem":
                item_md = convert_list_item(child, indent, is_ordered, num)
                if item_md:
                    items.append(item_md)
                if is_ordered:
                    num += 1
        return "\n".join(items) + "\n" if items else ""

    # Code block
    if node_type == "NodeCodeBlock":
        lang = ""
        code = ""
        for child in node.get("Children", []):
            child_type = child.get("Type", "")
            if child_type == "NodeCodeBlockFenceInfoMarker":
                lang = child.get("CodeBlockInfo", "")
            elif child_type == "NodeCodeBlockCode":
                code = child.get("Data", "")
        return f"```{lang}\n{code}```\n"

    # Blockquote
    if node_type == "NodeBlockquote":
        lines = []
        for child in node.get("Children", []):
            child_md = convert_node_to_markdown(child, indent)
            if child_md:
                for line in child_md.strip().split("\n"):
                    lines.append(f"> {line}")
        return "\n".join(lines) + "\n" if lines else ""

    # Table
    if node_type == "NodeTable":
        return convert_table(node)

    # Thematic break (horizontal rule)
    if node_type == "NodeThematicBreak":
        return "---\n"

    # Math block
    if node_type == "NodeMathBlock":
        content = ""
        for child in node.get("Children", []):
            if child.get("Type") == "NodeMathBlockContent":
                content = child.get("Data", "")
                break
        return f"$$\n{content}\n$$\n"

    # HTML block
    if node_type == "NodeHTMLBlock":
        return node.get("Data", "") + "\n"

    # Super block (container) - just process children
    if node_type == "NodeSuperBlock":
        children_md = []
        for child in node.get("Children", []):
            md = convert_node_to_markdown(child, indent)
            if md:
                children_md.append(md)
        return "\n".join(children_md)

    # Default: try to extract text if has children
    if "Children" in node:
        children_md = []
        for child in node.get("Children", []):
            md = convert_node_to_markdown(child, indent)
            if md:
                children_md.append(md)
        return "\n".join(children_md)

    return ""


def convert_list_item(node: dict, indent: int, is_ordered: bool, num: int) -> str:
    """Convert a list item node to Markdown."""
    prefix = "  " * indent
    marker = f"{num}." if is_ordered else "-"

    lines = []
    first_para = True

    for child in node.get("Children", []):
        child_type = child.get("Type", "")

        if child_type == "NodeParagraph":
            text = extract_text_from_node(child)
            if text.strip():
                if first_para:
                    lines.append(f"{prefix}{marker} {text}")
                    first_para = False
                else:
                    lines.append(f"{prefix}  {text}")

        elif child_type == "NodeList":
            # Nested list
            list_data = child.get("ListData", {})
            nested_ordered = list_data.get("Typ") == 1
            nested_num = list_data.get("Start", 1) or 1
            for nested_child in child.get("Children", []):
                if nested_child.get("Type") == "NodeListItem":
                    nested_md = convert_list_item(nested_child, indent + 1, nested_ordered, nested_num)
                    if nested_md:
                        lines.append(nested_md)
                    if nested_ordered:
                        nested_num += 1

        else:
            # Other content
            md = convert_node_to_markdown(child, indent + 1)
            if md:
                lines.append(f"{prefix}  {md.strip()}")

    return "\n".join(lines)


def convert_table(node: dict) -> str:
    """Convert a table node to Markdown."""
    rows = []

    for child in node.get("Children", []):
        if child.get("Type") == "NodeTableHead":
            for row_node in child.get("Children", []):
                if row_node.get("Type") == "NodeTableRow":
                    cells = []
                    for cell in row_node.get("Children", []):
                        if cell.get("Type") == "NodeTableCell":
                            cells.append(extract_text_from_node(cell))
                    if cells:
                        rows.append("| " + " | ".join(cells) + " |")
                        rows.append("|" + "|".join(["---"] * len(cells)) + "|")

        elif child.get("Type") == "NodeTableRow":
            cells = []
            for cell in child.get("Children", []):
                if cell.get("Type") == "NodeTableCell":
                    cells.append(extract_text_from_node(cell))
            if cells:
                rows.append("| " + " | ".join(cells) + " |")

    return "\n".join(rows) + "\n" if rows else ""


def convert_sy_to_markdown(sy_content: str, source_url: str) -> str:
    """Convert .sy JSON content to Markdown with source header."""
    try:
        data = json.loads(sy_content)
    except json.JSONDecodeError:
        return None

    markdown = convert_node_to_markdown(data)
    if markdown:
        # Add source header
        header = f"<!-- Source: {source_url} -->\n\n"
        return header + markdown
    return None


def clone_repository(temp_dir, repo_url, branch):
    """Clone the repository to a temporary directory."""
    try:
        print(f"  Cloning repository: {repo_url}")
        clone_path = Path(temp_dir) / "siyuan"

        result = subprocess.run(
            ["git", "clone", "--depth", "1", "--branch", branch, repo_url, str(clone_path)],
            capture_output=True,
            text=True,
            timeout=300
        )

        if result.returncode != 0:
            print(f"    -> Error cloning repository: {result.stderr}")
            return None

        print(f"    -> Repository cloned successfully")
        return clone_path

    except subprocess.TimeoutExpired:
        print(f"    -> Timeout cloning repository")
        return None
    except Exception as e:
        print(f"    -> Error cloning repository: {e}")
        return None


def process_documentation(source_dir, output_dir):
    """Process .sy files and convert to Markdown."""
    try:
        docs_source = Path(source_dir) / SOURCE_DOCS_FOLDER

        if not docs_source.exists():
            print(f"    -> Documentation folder not found: {docs_source}")
            return False

        # Create output directory
        output_dir.mkdir(parents=True, exist_ok=True)

        converted = 0
        skipped = 0

        # Process all .sy files
        for item in docs_source.rglob("*.sy"):
            if item.name.startswith('.'):
                continue

            relative_path = item.relative_to(docs_source)
            source_url = f"https://github.com/siyuan-note/user-guide-en_US/blob/{REPO_BRANCH}/{relative_path}"

            # Read and convert
            with open(item, 'r', encoding='utf-8', errors='ignore') as f:
                sy_content = f.read()

            markdown = convert_sy_to_markdown(sy_content, source_url)

            if markdown:
                # Output as .md file
                output_file = output_dir / relative_path.with_suffix(".md")
                output_file.parent.mkdir(parents=True, exist_ok=True)

                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(markdown)

                converted += 1
                print(f"    -> Converted: {relative_path.with_suffix('.md')}")
            else:
                skipped += 1

        print(f"\n    Converted: {converted}, Skipped: {skipped}")
        return True

    except Exception as e:
        print(f"    -> Error processing documentation: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """Main function to extract SiYuan documentation."""
    print("=" * 70)
    print("SiYuan Documentation Extractor (with .sy to Markdown conversion)")
    print("=" * 70)
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "github-scraped" / "siyuan"

    print(f"Repository: {REPO_URL}")
    print(f"Branch: {REPO_BRANCH}")
    print(f"Output directory: {output_dir}")
    print()

    # Create temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # Clone repository
        print("Cloning repository...")
        repo_path = clone_repository(temp_dir, REPO_URL, REPO_BRANCH)

        if not repo_path:
            print("\nError: Failed to clone repository")
            sys.exit(1)

        # Process documentation
        print("\nConverting .sy files to Markdown...")

        # Remove existing output directory if it exists
        if output_dir.exists():
            print(f"  Removing existing output directory: {output_dir}")
            shutil.rmtree(output_dir)

        if not process_documentation(repo_path, output_dir):
            print("\nError: Failed to process documentation")
            sys.exit(1)

    # Verify extraction
    print("\nVerifying extraction...")
    if not output_dir.exists():
        print("  Error: Output directory was not created")
        sys.exit(1)

    md_files = list(output_dir.glob("**/*.md"))
    total_size = sum(f.stat().st_size for f in md_files)

    print(f"  Total Markdown files: {len(md_files)}")
    print(f"  Total size: {total_size:,} bytes ({total_size/1024:.1f} KB)")

    if len(md_files) == 0:
        print("\n  Warning: No files found in output directory")
        sys.exit(1)

    # List main files
    print("\n  Sample documentation files:")
    for md_file in sorted(md_files)[:10]:
        file_size = md_file.stat().st_size
        print(f"    - {md_file.relative_to(output_dir)} ({file_size:,} bytes)")

    if len(md_files) > 10:
        print(f"    ... and {len(md_files) - 10} more files")

    print()
    print("=" * 70)
    print("Extraction Complete")
    print("=" * 70)
    print(f"Output: {output_dir}")
    print()


if __name__ == "__main__":
    main()
