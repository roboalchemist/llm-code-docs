#!/usr/bin/env python3
"""
SiYuan .sy to Markdown Converter

Converts SiYuan's JSON-based .sy files to clean Markdown.
"""

import json
import sys
from pathlib import Path
from typing import Optional


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


def convert_sy_file(input_path: Path, output_path: Optional[Path] = None) -> str:
    """Convert a .sy file to Markdown."""
    with open(input_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Strip any source header added by extraction script
    if content.startswith("# Source:"):
        lines = content.split("\n", 2)
        if len(lines) > 2:
            content = lines[2]

    try:
        data = json.loads(content)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON in {input_path}: {e}")

    markdown = convert_node_to_markdown(data)

    if output_path:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(markdown)

    return markdown


def convert_directory(input_dir: Path, output_dir: Path) -> dict:
    """Convert all .sy files in a directory to Markdown."""
    stats = {"converted": 0, "errors": 0, "skipped": 0}

    for sy_file in input_dir.rglob("*.sy"):
        relative = sy_file.relative_to(input_dir)
        output_file = output_dir / relative.with_suffix(".md")

        try:
            convert_sy_file(sy_file, output_file)
            stats["converted"] += 1
            print(f"  Converted: {relative}")
        except Exception as e:
            stats["errors"] += 1
            print(f"  Error: {relative} - {e}")

    return stats


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Usage: siyuan_to_md.py <input> [output]")
        print("  input: .sy file or directory containing .sy files")
        print("  output: output .md file or directory (optional)")
        sys.exit(1)

    input_path = Path(sys.argv[1])
    output_path = Path(sys.argv[2]) if len(sys.argv) > 2 else None

    if not input_path.exists():
        print(f"Error: {input_path} does not exist")
        sys.exit(1)

    if input_path.is_file():
        if output_path is None:
            output_path = input_path.with_suffix(".md")

        try:
            convert_sy_file(input_path, output_path)
            print(f"Converted: {input_path} -> {output_path}")
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)

    elif input_path.is_dir():
        if output_path is None:
            output_path = input_path.parent / f"{input_path.name}_md"

        print(f"Converting directory: {input_path}")
        print(f"Output directory: {output_path}")
        print()

        stats = convert_directory(input_path, output_path)

        print()
        print(f"Converted: {stats['converted']}")
        print(f"Errors: {stats['errors']}")


if __name__ == "__main__":
    main()
