#!/usr/bin/env python3
"""
Comprehensive rTorrent documentation extractor.

Extracts from 4 GitHub repos:
1. rakshasa/rtorrent        -> docs/github-scraped/rtorrent/rakshasa-rtorrent/
2. rtorrent-community/rtorrent-docs -> docs/github-scraped/rtorrent/rtorrent-community/
3. rakshasa/rtorrent-doc   -> docs/github-scraped/rtorrent/rakshasa-rtorrent-doc/
4. pyroscope/rtorrent-ps   -> docs/github-scraped/rtorrent/rtorrent-ps/

Converts:
- doc/faq.xml (DocBook XML) -> FAQ markdown
- docs/*.rst (Sphinx RST) -> markdown
"""

import os
import re
import shutil
import subprocess
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
OUTPUT_BASE = BASE_DIR / "docs" / "github-scraped" / "rtorrent"

REPOS = {
    "rakshasa-rtorrent": {
        "url": "https://github.com/rakshasa/rtorrent.git",
        "clone_dir": "rtorrent-src",
        "subdir": "rakshasa-rtorrent",
    },
    "rtorrent-community": {
        "url": "https://github.com/rtorrent-community/rtorrent-docs.git",
        "clone_dir": "rtorrent-community-docs",
        "subdir": "rtorrent-community",
    },
    "rakshasa-rtorrent-doc": {
        "url": "https://github.com/rakshasa/rtorrent-doc.git",
        "clone_dir": "rtorrent-doc",
        "subdir": "rakshasa-rtorrent-doc",
    },
    "rtorrent-ps": {
        "url": "https://github.com/pyroscope/rtorrent-ps.git",
        "clone_dir": "rtorrent-ps",
        "subdir": "rtorrent-ps",
    },
}


# ---------------------------------------------------------------------------
# RST -> Markdown converter (lightweight, no external deps)
# ---------------------------------------------------------------------------

def rst_to_md(text: str) -> str:
    """Convert RST to Markdown with common patterns."""
    lines = text.splitlines()
    out = []
    in_code_block = False
    code_block_lines = []
    code_lang = ""

    for line in lines:
        # Skip RST bibliography/translation meta lines
        stripped = line.strip()
        if stripped.startswith(".."):
            # Could be a directive (code, image, etc.)
            if stripped.startswith(".. code-block::") or stripped.startswith(".. sourcecode::"):
                code_lang = stripped.split("::", 1)[1].strip()
                in_code_block = True
                code_block_lines = []
                continue
            elif stripped.startswith(".. include::") or stripped.startswith(".. _"):
                continue
            elif stripped.startswith(".. |") and stripped.endswith("|"):
                # Replace |variable| substitutions with placeholder
                var_name = stripped[3:].split("|")[0].strip()
                out.append(f"*{var_name}*")
                continue
            elif stripped.startswith(".."):
                continue

        if in_code_block:
            if line.strip() and not line.startswith(" " * 3) and not line.startswith("\t"):
                # End of code block
                out.append(f"```{code_lang}")
                out.extend(code_block_lines)
                out.append("```")
                out.append("")
                in_code_block = False
                code_block_lines = []
                code_lang = ""
                # Process this line normally
            else:
                code_block_lines.append(line.rstrip())
                continue

        # Heading patterns
        m = re.match(r"^((={3,}|-{3,}|_{3,}|\*{3,}|\\.{3,})\s*)$", stripped)
        if m and out and re.match(r"^[A-Za-z0-9 :`'\"<>.,!?/-]+$", out[-1].strip()):
            # This is an underline heading
            heading = out[-1].strip()
            level = 2 if len(m.group(1).strip()) >= 3 else 1
            out[-1] = f"{'#' * level} {heading}"
            continue

        # Bold/strong
        line = re.sub(r"\*\*(.+?)\*\*", r"**\1**", line)
        line = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"*\1*", line)
        # Inline literals/code
        line = re.sub(r"``(.+?)``", r"`\1`", line)
        # Links: `link text <url_>`_ -> [link text](url)
        line = re.sub(r"`(.+?) <(https?://[^>]+)>`_", r"[\1](\2)", line)
        line = re.sub(r"`(.+?) <(https?://[^>]+)>`__", r"[\1](\2)", line)
        # Standalone links
        line = re.sub(r"<(https?://[^>]+)>", r"\1", line)
        # Field lists -> bold labels
        line = re.sub(r":(author|copyright|date|version|title):\s*(.+)", r"**\1:** \2", line)
        line = re.sub(r":([a-z_-]+):\s*(.+)", r"**\1:** \2", line)
        # Numbered lists (RST style 1. -> 1.)
        line = re.sub(r"^(\s*)(\d+)\.\s+", r"\1\2. ", line)
        # Bullet lists
        line = re.sub(r"^(\s*)- ", r"\1- ", line)
        line = re.sub(r"^(\s*)\* ", r"\1- ", line)
        # Block quotes
        line = re.sub(r"^\s{3,}(.*)", r"> \1", line)
        # Horizontal rules
        line = re.sub(r"^---+$", "---", line)
        # RST class/style directives (skip)
        line = re.sub(r"^\s*\.\. start-with-literal::", "", line)

        out.append(line)

    if in_code_block:
        out.append("```")
        out.extend(code_block_lines)
        out.append("```")

    return "\n".join(out)


# ---------------------------------------------------------------------------
# DocBook XML -> Markdown converter (regex-based, handles DOCTYPE)
# ---------------------------------------------------------------------------

def docbook_xml_to_md(xml_path: Path) -> str:
    """Convert DocBook XML FAQ to readable Markdown using regex (handles DOCTYPE)."""
    content = xml_path.read_text()

    out = []
    out.append("# rTorrent Frequently Asked Questions\n")
    out.append("*User FAQ for Rakshasa's BitTorrent client.*\n")

    # Strip XML declaration and DOCTYPE
    content = re.sub(r"<![^>]*>", "", content)
    content = re.sub(r"<\?[^>]*\?>", "", content)

    # Extract article title
    m = re.search(r"<title[^>]*>([^<]+)</title>", content)
    if m:
        out.append(f"*{m.group(1)}*\n")

    # Split into qandaentry blocks
    blocks = re.split(r"<qandaentry>", content)
    for block in blocks[1:]:  # skip first (before first qandaentry)
        # Extract question
        q_match = re.search(r"<question[^>]*>\s*<para[^>]*>([^<]+(?:<[^>]+>[^<]*</[^>]+>)*[^<]*)</para>", block, re.DOTALL)
        if not q_match:
            q_match = re.search(r"<question[^>]*>\s*<para[^>]*>(.+?)</para>", block, re.DOTALL)
        # Extract answer (may have multiple paras)
        a_texts = re.findall(r"<answer[^>]*>\s*<para[^>]*>(.+?)</para>", block, re.DOTALL)

        if q_match:
            q_raw = q_match.group(1).strip()
            # Strip remaining tags
            q_text = re.sub(r"<[^>]+>", "", q_raw).strip()
            out.append(f"## {q_text}\n")
            for a_raw in a_texts:
                a_text = re.sub(r"<[^>]+>", "", a_raw).strip()
                out.append(f"{a_text}\n")
            out.append("")

    return "\n".join(out)


# ---------------------------------------------------------------------------
# Source: rakshasa/rtorrent
# ---------------------------------------------------------------------------

def extract_rakshasa_rtorrent(src_dir: Path, out_dir: Path):
    """Extract comprehensive docs from rakshasa/rtorrent."""
    print("  Extracting rakshasa/rtorrent...")

    doc_dir = src_dir / "doc"
    manual_dir = doc_dir / "manual"

    files = {
        # Markdown files from manual/
        **({
            f.name: f
            for f in manual_dir.glob("*.md")
        } if manual_dir.exists() else {}),
        # Root-level documentation
        "README.md": src_dir / "README.md",
        "INSTALL.md": src_dir / "INSTALL",
        # Config examples
        "rtorrent.rc-example.md": doc_dir / "rtorrent.rc-example",
        "rtorrent.rc-lua-example.md": doc_dir / "rtorrent.rc.lua-example",
        # FAQ
        "faq.md": None,  # handled specially
        # Debugging docs
        "debugging.md": doc_dir / "debugging",
        # Scripts
        "log_rtorrent.sh.md": doc_dir / "log_rtorrent.sh",
        "log_proc_vmmap.sh.md": doc_dir / "log_proc_vmmap.sh",
        "log_vmmap.sh.md": doc_dir / "log_vmmap.sh",
        "log_stats.plot.md": doc_dir / "log_stats.plot",
        # Valgrind
        "valgrind.commands.md": doc_dir / "valgrind.commands",
        "valgrind.suppression.md": doc_dir / "valgrind.suppression",
        # Perl script
        "rtorrent_fast_resume.pl.md": doc_dir / "rtorrent_fast_resume.pl",
        # torrent_data
        "torrent_data.md": doc_dir / "torrent_data",
    }

    # Copy files
    for dest_name, src_path in files.items():
        if src_path is None:
            continue  # handled specially
        if src_path.exists():
            shutil.copy2(src_path, out_dir / dest_name)

    # Convert faq.xml
    faq_xml = doc_dir / "faq.xml"
    if faq_xml.exists():
        faq_md = docbook_xml_to_md(faq_xml)
        (out_dir / "faq.md").write_text(faq_md)
        print(f"    faq.xml -> faq.md")

    # Copy plot/ scripts
    plot_dir = doc_dir / "plot"
    if plot_dir.exists():
        plot_out = out_dir / "plot"
        plot_out.mkdir(exist_ok=True)
        for f in plot_dir.glob("*"):
            shutil.copy2(f, plot_out / f.name)

    # Copy scripts/
    scripts_dir = doc_dir / "scripts"
    if scripts_dir.exists():
        scripts_out = out_dir / "scripts"
        shutil.copytree(scripts_dir, scripts_out, dirs_exist_ok=True)

    # Copy old/ man page sources
    old_dir = doc_dir / "old"
    if old_dir.exists():
        old_out = out_dir / "old"
        shutil.copytree(old_dir, old_out, dirs_exist_ok=True)

    # rtorrent.rc (no extension - actual config file)
    rt_rc = doc_dir / "rtorrent.rc"
    if rt_rc.exists():
        shutil.copy2(rt_rc, out_dir / "rtorrent.rc")


# ---------------------------------------------------------------------------
# Source: rtorrent-community/rtorrent-docs
# ---------------------------------------------------------------------------

def extract_rtorrent_community(src_dir: Path, out_dir: Path):
    """Extract docs from rtorrent-community/rtorrent-docs."""
    print("  Extracting rtorrent-community/rtorrent-docs...")

    docs_dir = src_dir / "docs"
    if not docs_dir.exists():
        print(f"    No docs/ folder found in {src_dir}")
        return

    # Copy README from root
    readme = src_dir / "README.md"
    if readme.exists():
        shutil.copy2(readme, out_dir / "README.md")

    # Convert RST files to Markdown
    rst_files = list(docs_dir.glob("*.rst"))
    print(f"    Found {len(rst_files)} RST files")

    for rst in rst_files:
        text = rst.read_text()
        md_text = rst_to_md(text)
        dest = out_dir / f"{rst.stem}.md"
        dest.write_text(md_text)
        print(f"    {rst.name} -> {rst.stem}.md")

    # Copy rtorrent.rc example
    rt_rc = docs_dir / "rtorrent.rc"
    if rt_rc.exists():
        shutil.copy2(rt_rc, out_dir / "rtorrent.rc")

    # Copy examples/ scripts
    examples_dir = docs_dir / "examples"
    if examples_dir.exists():
        examples_out = out_dir / "examples"
        shutil.copytree(examples_dir, examples_out, dirs_exist_ok=True)


# ---------------------------------------------------------------------------
# Source: rakshasa/rtorrent-doc
# ---------------------------------------------------------------------------

def extract_rakshasa_rtorrent_doc(src_dir: Path, out_dir: Path):
    """Extract wiki docs from rakshasa/rtorrent-doc."""
    print("  Extracting rakshasa/rtorrent-doc...")

    md_files = list(src_dir.glob("*.md"))
    print(f"    Found {len(md_files)} markdown files")
    for f in md_files:
        shutil.copy2(f, out_dir / f.name)
        print(f"    {f.name}")

    # Also check for any other docs
    for subdir in src_dir.iterdir():
        if subdir.is_dir() and not subdir.name.startswith("."):
            sub_out = out_dir / subdir.name
            shutil.copytree(subdir, sub_out, dirs_exist_ok=True)


# ---------------------------------------------------------------------------
# Source: pyroscope/rtorrent-ps
# ---------------------------------------------------------------------------

def extract_rtorrent_ps(src_dir: Path, out_dir: Path):
    """Extract docs from pyroscope/rtorrent-ps."""
    print("  Extracting pyroscope/rtorrent-ps...")

    docs_dir = src_dir / "docs"
    if not docs_dir.exists():
        print(f"    No docs/ folder found in {src_dir}")
        return

    # Copy README.rst from root
    readme = src_dir / "README.rst"
    if readme.exists():
        md_text = rst_to_md(readme.read_text())
        (out_dir / "README.md").write_text(md_text)

    # Convert RST files to Markdown
    rst_files = list(docs_dir.glob("*.rst"))
    print(f"    Found {len(rst_files)} RST files")

    for rst in rst_files:
        text = rst.read_text()
        md_text = rst_to_md(text)
        dest = out_dir / f"{rst.stem}.md"
        dest.write_text(md_text)
        print(f"    {rst.name} -> {rst.stem}.md")

    # Copy .md files as-is
    md_files = list(docs_dir.glob("*.md"))
    for f in md_files:
        shutil.copy2(f, out_dir / f.name)
        print(f"    {f.name} (copied)")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print("=" * 70)
    print("Comprehensive rTorrent Documentation Extractor")
    print("=" * 70)

    # Clean output base
    if OUTPUT_BASE.exists():
        shutil.rmtree(OUTPUT_BASE)
    OUTPUT_BASE.mkdir(parents=True, exist_ok=True)

    # Write master index
    index_md = [
        "# rTorrent Documentation Index",
        "",
        "This directory contains comprehensive rTorrent documentation scraped from",
        "multiple GitHub repositories.",
        "",
        "## Sources",
        "",
        "- **rakshasa/rtorrent** — Official rTorrent source repo (doc/, README, INSTALL)",
        "  -> `rakshasa-rtorrent/`",
        "- **rtorrent-community/rtorrent-docs** — Community rTorrent Handbook",
        "  -> `rtorrent-community/` (RST converted to Markdown)",
        "- **rakshasa/rtorrent-doc** — Wiki documentation",
        "  -> `rakshasa-rtorrent-doc/`",
        "- **pyroscope/rtorrent-ps** — Extended rTorrent-PS distribution docs",
        "  -> `rtorrent-ps/` (RST converted to Markdown)",
        "",
    ]
    (OUTPUT_BASE / "INDEX.md").write_text("\n".join(index_md))

    temp_root = Path(tempfile.gettempdir()) / "rtorrent-full-extract"
    if temp_root.exists():
        shutil.rmtree(temp_root)
    temp_root.mkdir()

    extractors = {
        "rakshasa-rtorrent": extract_rakshasa_rtorrent,
        "rtorrent-community": extract_rtorrent_community,
        "rakshasa-rtorrent-doc": extract_rakshasa_rtorrent_doc,
        "rtorrent-ps": extract_rtorrent_ps,
    }

    for name, extractor in extractors.items():
        repo = REPOS[name]
        clone_dir = temp_root / repo["clone_dir"]
        out_dir = OUTPUT_BASE / repo["subdir"]

        print(f"\n[{name}]")
        print(f"  Cloning {repo['url']}...")

        try:
            # Use full shallow clone for repos that need mixed file/directory content
            # (git sparse-checkout can't reliably mix files and directories)
            result = subprocess.run(
                ["git", "clone", "--depth", "1",
                 repo["url"], str(clone_dir)],
                capture_output=True, text=True, timeout=180
            )
            if result.returncode != 0:
                print(f"  ERROR cloning: {result.stderr}")
                continue

        except Exception as e:
            print(f"  ERROR: {e}")
            continue

        out_dir.mkdir(parents=True, exist_ok=True)
        extractor(clone_dir, out_dir)

    # Report results
    print("\n" + "=" * 70)
    print("Extraction complete!")
    total_files = 0
    total_size = 0
    for sub in sorted(OUTPUT_BASE.iterdir()):
        if sub.is_dir():
            files = list(sub.rglob("*"))
            md_count = len([f for f in files if f.is_file()])
            size = sum(f.stat().st_size for f in files if f.is_file())
            total_files += md_count
            total_size += size
            print(f"  {sub.name}/: {md_count} files, {size/1024:.1f} KB")

    print(f"\n  TOTAL: {total_files} files, {total_size/1024:.1f} KB")
    print(f"  Location: {OUTPUT_BASE}")

    # Cleanup
    if temp_root.exists():
        shutil.rmtree(temp_root)


if __name__ == "__main__":
    main()
