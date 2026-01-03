#!/usr/bin/env python3
"""
Sentry Documentation Extractor
Clones the getsentry/sentry-docs repository and extracts all documentation.
Sentry is an error tracking and performance monitoring platform.
Output: docs/web-scraped/sentry/
"""

import os
import sys
import subprocess
import shutil
import tempfile
import re
from pathlib import Path

# Output directory
OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "web-scraped" / "sentry"


def run_command(cmd, cwd=None, timeout=300):
    """Run a shell command and return the result."""
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=timeout,
        )
        return result.returncode, result.stdout, result.stderr
    except subprocess.TimeoutExpired:
        print(f"Command timed out after {timeout} seconds: {cmd}")
        return 1, "", "Timeout"


def clean_mdx_to_markdown(content):
    """Convert MDX-specific syntax to standard Markdown."""
    # Remove import statements
    content = re.sub(r"^import\s+.*?from\s+['\"].*?['\"];?\s*\n", "", content, flags=re.MULTILINE)

    # Remove MDX-specific components like <Alert>, <DocsChangelog>, etc.
    # Keep opening tags as headers or simple text
    content = re.sub(r"<Alert[^>]*>", "", content)
    content = re.sub(r"</Alert>", "", content)
    content = re.sub(r"<DocsChangelog\s*/>", "[Documentation Changelog Component]", content)
    content = re.sub(r"<[A-Z][a-zA-Z]*[^>]*>", "", content)
    content = re.sub(r"</[A-Z][a-zA-Z]*>", "", content)

    # Remove sidebar_order and other frontmatter metadata (keep title and description)
    lines = content.split("\n")
    in_frontmatter = False
    frontmatter_lines = []
    rest_lines = []

    for line in lines:
        if line.strip() == "---":
            if not in_frontmatter:
                in_frontmatter = True
            else:
                in_frontmatter = False
                continue

        if in_frontmatter:
            # Keep title and description, remove other metadata
            if line.startswith("title:") or line.startswith("description:") or line.startswith("---"):
                frontmatter_lines.append(line)
        else:
            rest_lines.append(line)

    # Reconstruct content with cleaned frontmatter
    if frontmatter_lines:
        cleaned_content = "---\n" + "\n".join(frontmatter_lines) + "\n---\n" + "\n".join(rest_lines)
    else:
        cleaned_content = "\n".join(rest_lines)

    # Clean up excessive whitespace
    cleaned_content = re.sub(r"\n\n\n+", "\n\n", cleaned_content)

    return cleaned_content


def convert_mdx_to_md(mdx_file):
    """Convert an MDX file to Markdown by cleaning JSX/MDX syntax."""
    try:
        with open(mdx_file, "r", encoding="utf-8") as f:
            content = f.read()

        cleaned = clean_mdx_to_markdown(content)

        # Write back as .md file
        md_file = mdx_file.with_suffix(".md")
        with open(md_file, "w", encoding="utf-8") as f:
            f.write(cleaned)

        return True
    except Exception as e:
        print(f"Error converting {mdx_file}: {e}")
        return False


def extract_sentry_docs():
    """Clone the Sentry docs repository and extract documentation."""
    with tempfile.TemporaryDirectory() as tmpdir:
        repo_path = Path(tmpdir) / "sentry-docs"
        print(f"Cloning getsentry/sentry-docs repository to {repo_path}...")

        returncode, stdout, stderr = run_command(
            f"git clone --depth 1 https://github.com/getsentry/sentry-docs.git {repo_path}",
            timeout=300
        )

        if returncode != 0:
            print(f"Error cloning repository: {stderr}")
            return False

        # Check if docs folder exists
        docs_src = repo_path / "docs"
        if not docs_src.exists():
            print(f"Error: docs folder not found at {docs_src}")
            return False

        print(f"Cloned successfully. Extracting docs from {docs_src}...")

        # Remove output directory if it exists
        if OUTPUT_DIR.exists():
            shutil.rmtree(OUTPUT_DIR)

        # Copy docs folder
        shutil.copytree(docs_src, OUTPUT_DIR)
        print(f"Copied docs to {OUTPUT_DIR}")

        # Convert MDX files to Markdown
        print("Converting MDX files to Markdown...")
        mdx_files = list(OUTPUT_DIR.glob("**/*.mdx"))
        converted_count = 0

        for mdx_file in mdx_files:
            if convert_mdx_to_md(mdx_file):
                converted_count += 1

        print(f"Converted {converted_count} MDX files to Markdown")

        # Remove original MDX files (keep only .md files)
        for mdx_file in OUTPUT_DIR.glob("**/*.mdx"):
            mdx_file.unlink()

        print("Removed original MDX files")

        # Count final files
        md_files = list(OUTPUT_DIR.glob("**/*.md"))
        mdx_files_remaining = list(OUTPUT_DIR.glob("**/*.mdx"))

        print(f"Total markdown files: {len(md_files)}")
        print(f"Remaining MDX files: {len(mdx_files_remaining)}")

        return True


def main():
    """Main function."""
    print("=" * 70)
    print("Sentry Documentation Extractor")
    print("=" * 70)

    success = extract_sentry_docs()

    if success:
        print("\nSentry documentation extracted successfully!")
        return 0
    else:
        print("\nFailed to extract Sentry documentation.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
