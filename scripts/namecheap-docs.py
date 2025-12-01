#!/usr/bin/env python3
"""
Namecheap API Documentation Scraper
Downloads the official Go SDK source files which contain API documentation.
Since Namecheap's website is behind Cloudflare, we extract docs from their GitHub SDK.
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path
import tempfile
import re

# GitHub repository for Namecheap Go SDK
SDK_REPO = "https://github.com/namecheap/go-namecheap-sdk.git"
SDK_BRANCH = "master"

# Files to extract (Go source files with API documentation)
GO_SOURCE_FILES = [
    "namecheap/namecheap.go",
    "namecheap/domains.go",
    "namecheap/domains_get_list.go",
    "namecheap/domains_get_info.go",
    "namecheap/domains_dns.go",
    "namecheap/domains_dns_get_hosts.go",
    "namecheap/domains_dns_get_list.go",
    "namecheap/domains_dns_set_hosts.go",
    "namecheap/domains_dns_set_custom.go",
    "namecheap/domains_dns_set_default.go",
    "namecheap/domains_ns.go",
    "namecheap/domains_ns_create.go",
    "namecheap/domains_ns_delete.go",
    "namecheap/domains_ns_get_info.go",
    "namecheap/domains_ns_update.go",
    "README.md",
    "CONTRIBUTING.md",
]


def clone_sdk(temp_dir: Path) -> bool:
    """Clone the Namecheap Go SDK repository."""
    print(f"Cloning {SDK_REPO}...")
    try:
        result = subprocess.run(
            ["git", "clone", "--depth", "1", "--branch", SDK_BRANCH, SDK_REPO, str(temp_dir)],
            capture_output=True,
            text=True,
            timeout=60
        )
        if result.returncode != 0:
            print(f"Error cloning: {result.stderr}")
            return False
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False


def go_to_markdown(content: str, filename: str) -> str:
    """Convert Go source file to markdown documentation format."""
    lines = content.split('\n')
    md_lines = []

    # Add header
    base_name = Path(filename).stem
    title = base_name.replace('_', ' ').title()
    md_lines.append(f"# Namecheap API: {title}")
    md_lines.append("")
    md_lines.append(f"Source: https://github.com/namecheap/go-namecheap-sdk/blob/master/{filename}")
    md_lines.append("")

    # Process the Go source
    in_struct = False
    struct_name = ""

    for line in lines:
        # Skip package and import statements for cleaner output
        if line.startswith('package ') or line.startswith('import '):
            continue
        if line.strip() == '(' or line.strip() == ')':
            continue
        if line.strip().startswith('"') and line.strip().endswith('"'):
            continue

        # Detect const blocks
        if line.startswith('const ('):
            md_lines.append("## Constants")
            md_lines.append("")
            md_lines.append("```go")
            md_lines.append(line)
            continue

        # Detect type definitions (structs)
        struct_match = re.match(r'^type (\w+) struct \{', line)
        if struct_match:
            struct_name = struct_match.group(1)
            in_struct = True
            md_lines.append(f"## Type: {struct_name}")
            md_lines.append("")
            md_lines.append("```go")
            md_lines.append(line)
            continue

        # Detect function definitions
        func_match = re.match(r'^func \((\w+) \*?(\w+)\) (\w+)\((.*?)\)', line)
        if func_match:
            receiver_var, receiver_type, func_name, params = func_match.groups()
            md_lines.append(f"## Method: {receiver_type}.{func_name}")
            md_lines.append("")
            md_lines.append("```go")
            md_lines.append(line)
            continue

        # Add line as-is
        md_lines.append(line)

    # Close any open code blocks
    result = '\n'.join(md_lines)

    # Clean up: ensure code blocks are properly closed
    open_blocks = result.count('```go') + result.count('```')
    if open_blocks % 2 != 0:
        result += "\n```"

    return result


def extract_docs(temp_dir: Path, output_dir: Path) -> int:
    """Extract documentation from SDK source files."""
    output_dir.mkdir(parents=True, exist_ok=True)

    successful = 0

    for file_path in GO_SOURCE_FILES:
        src_path = temp_dir / file_path

        if not src_path.exists():
            print(f"  Skipping (not found): {file_path}")
            continue

        # Read source file
        content = src_path.read_text(encoding='utf-8')

        # Determine output filename
        if file_path.endswith('.md'):
            # Keep markdown files as-is
            out_name = Path(file_path).name
            out_content = f"# Source: https://github.com/namecheap/go-namecheap-sdk/blob/master/{file_path}\n\n{content}"
        else:
            # Convert Go files to markdown
            out_name = Path(file_path).stem + ".md"
            out_content = go_to_markdown(content, file_path)

        # Write output
        out_path = output_dir / out_name
        out_path.write_text(out_content, encoding='utf-8')
        print(f"  Extracted: {out_name}")
        successful += 1

    return successful


def create_index(output_dir: Path):
    """Create an index file for all documentation."""
    index_content = """# Namecheap API Documentation

This documentation is extracted from the official [Namecheap Go SDK](https://github.com/namecheap/go-namecheap-sdk).

## Official Resources

- [Namecheap API Documentation](https://www.namecheap.com/support/api/intro/)
- [API Sandbox](https://www.sandbox.namecheap.com/)
- [Go SDK on GitHub](https://github.com/namecheap/go-namecheap-sdk)

## API Methods

### Domains
- `namecheap.domains.getList` - Returns list of domains for user
- `namecheap.domains.getInfo` - Get domain details

### DNS
- `namecheap.domains.dns.getHosts` - Get DNS host records
- `namecheap.domains.dns.getList` - Get DNS servers for domain
- `namecheap.domains.dns.setHosts` - Set DNS host records
- `namecheap.domains.dns.setCustom` - Set custom nameservers
- `namecheap.domains.dns.setDefault` - Set default Namecheap DNS

### Nameservers
- `namecheap.domains.ns.create` - Create nameserver
- `namecheap.domains.ns.delete` - Delete nameserver
- `namecheap.domains.ns.getInfo` - Get nameserver info
- `namecheap.domains.ns.update` - Update nameserver IP

## Authentication

All API calls require:
- `ApiUser` - Your Namecheap username
- `ApiKey` - Your API key (from account settings)
- `UserName` - Username on whose behalf the call is made
- `ClientIp` - Your whitelisted IP address

## Environments

- **Production**: `https://api.namecheap.com/xml.response`
- **Sandbox**: `https://api.sandbox.namecheap.com/xml.response`

## Files in this directory

"""

    # List all markdown files
    for md_file in sorted(output_dir.glob("*.md")):
        if md_file.name != "index.md":
            index_content += f"- [{md_file.stem}]({md_file.name})\n"

    (output_dir / "index.md").write_text(index_content, encoding='utf-8')
    print("  Created: index.md")


def main():
    """Main function."""
    print("=" * 60)
    print("Namecheap API Documentation Scraper")
    print("=" * 60)
    print(f"Source: {SDK_REPO}")
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "web-scraped" / "namecheap"

    print(f"Output: {output_dir}")
    print()

    # Create temp directory and clone
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = Path(temp_dir)

        if not clone_sdk(temp_path):
            print("Failed to clone SDK repository")
            sys.exit(1)

        print()
        print("Extracting documentation...")
        successful = extract_docs(temp_path, output_dir)

        print()
        print("Creating index...")
        create_index(output_dir)

    # Calculate total size
    total_size = sum(f.stat().st_size for f in output_dir.glob("*.md"))

    print()
    print("=" * 60)
    print("Summary")
    print("=" * 60)
    print(f"Files extracted: {successful + 1}")  # +1 for index
    print(f"Total size: {total_size:,} bytes ({total_size/1024:.1f} KB)")
    print(f"Output: {output_dir}")
    print()
    print("Done!")


if __name__ == "__main__":
    main()
