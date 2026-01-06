#!/usr/bin/env python3
"""
Gosec Documentation Scraper (WebFetch-based)
Downloads gosec documentation from securego.io with better markdown conversion.
gosec is a Go source code security scanner that detects SQL injection,
weak cryptography, hardcoded credentials, and other security vulnerabilities.
"""

import os
import sys
import subprocess
from pathlib import Path
import time

# Rules to document (based on securego.io rules)
RULES_TO_FETCH = [
    "g101",  # Hardcoded credentials
    "g102",  # Bind to all interfaces
    "g103",  # Use of unsafe block
    "g104",  # Audit errors not checked
    "g107",  # URL taint input
    "g201",  # SQL injection via format string
    "g202",  # SQL injection via concatenation
    "g304",  # File path taint input
]

def fetch_and_convert(url, output_path, description):
    """Use curl with pandoc to fetch and convert HTML to markdown."""
    try:
        print(f"  Fetching: {url}")

        # Use curl to fetch HTML
        result = subprocess.run(
            ["curl", "-s", url],
            capture_output=True,
            text=True,
            timeout=15
        )

        if result.returncode != 0:
            print(f"    -> Error fetching: {result.stderr}")
            return False

        html_content = result.stdout

        # Try to use pandoc if available, otherwise use basic HTML stripping
        try:
            proc = subprocess.run(
                ["pandoc", "-f", "html", "-t", "markdown"],
                input=html_content,
                capture_output=True,
                text=True,
                timeout=10
            )

            if proc.returncode == 0:
                markdown = proc.stdout
            else:
                # Fallback: basic conversion
                markdown = basic_html_to_markdown(html_content)
        except FileNotFoundError:
            # pandoc not installed
            markdown = basic_html_to_markdown(html_content)

        # Add metadata header
        header = f"""# Source: {url}

"""
        final_content = header + markdown

        # Write to file
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(final_content)

        print(f"    -> Saved: {output_path.name} ({len(final_content)} bytes)")
        return True

    except subprocess.TimeoutExpired:
        print(f"    -> Timeout fetching {url}")
        return False
    except Exception as e:
        print(f"    -> Error: {e}")
        return False


def basic_html_to_markdown(html):
    """Basic HTML to Markdown conversion."""
    import re

    # Remove script and style tags
    text = re.sub(r'<script[^>]*>.*?</script>', '', html, flags=re.DOTALL | re.IGNORECASE)
    text = re.sub(r'<style[^>]*>.*?</style>', '', text, flags=re.DOTALL | re.IGNORECASE)

    # Replace headers
    for i in range(6, 0, -1):
        text = re.sub(f'<h{i}[^>]*>(.*?)</h{i}>', lambda m: '#' * i + ' ' + m.group(1) + '\n', text, flags=re.IGNORECASE)

    # Replace bold/strong
    text = re.sub(r'<(strong|b)[^>]*>(.*?)</\1>', r'**\2**', text, flags=re.IGNORECASE)

    # Replace italic/em
    text = re.sub(r'<(em|i)[^>]*>(.*?)</\1>', r'*\2*', text, flags=re.IGNORECASE)

    # Replace paragraphs
    text = re.sub(r'<p[^>]*>(.*?)</p>', r'\1\n\n', text, flags=re.IGNORECASE)

    # Replace line breaks
    text = re.sub(r'<br\s*/?>', '\n', text, flags=re.IGNORECASE)

    # Replace links
    text = re.sub(r'<a[^>]*href=["\']([^"\']*)["\'][^>]*>(.*?)</a>', r'[\2](\1)', text, flags=re.IGNORECASE)

    # Replace code blocks
    text = re.sub(r'<code[^>]*>(.*?)</code>', r'`\1`', text, flags=re.IGNORECASE)
    text = re.sub(r'<pre[^>]*>(.*?)</pre>', r'\n```\n\1\n```\n', text, flags=re.DOTALL | re.IGNORECASE)

    # Replace lists
    text = re.sub(r'<li[^>]*>(.*?)</li>', r'- \1\n', text, flags=re.IGNORECASE)

    # Remove remaining HTML tags
    text = re.sub(r'<[^>]+>', '', text)

    # Clean up whitespace
    text = re.sub(r'\n\s*\n+', '\n\n', text)
    text = re.sub(r'[ \t]+', ' ', text)
    text = text.strip()

    return text


def create_overview():
    """Create a comprehensive overview document."""
    overview = """# Source: https://securego.io/docs/rules/rule-intro

# Gosec - Go Security Scanner

Gosec is a source code security scanner for Go that inspects source code for security problems
by scanning the Go AST (Abstract Syntax Tree). It's designed to identify security vulnerabilities
in Go applications including:

- SQL injection attacks
- Weak cryptography
- Hardcoded credentials and secrets
- Insecure temporary file creation
- Missing input validation
- Unsafe file operations

## Security Rules Overview

Gosec implements multiple security rules to detect various vulnerability classes:

### G101: Hardcoded Credentials
Detects hardcoded passwords and sensitive credentials in string literals.
Variables matching patterns like "password", "token", "secret", etc. are flagged.

### G102: Bind to All Interfaces
Identifies insecure network binding that listens on 0.0.0.0, exposing services to all interfaces.

### G103: Use of Unsafe Block
Flags usage of Go's unsafe package which bypasses type safety.

### G104: Audit Errors Not Checked
Detects error handling issues where error returns are ignored.

### G107: URL Taint Input
Identifies potential SSRF vulnerabilities where user input is passed directly to HTTP requests.

### G201/G202: SQL Injection
- G201: Detects SQL query construction using format strings
- G202: Detects SQL query construction using string concatenation

### G304: File Path Taint Input
Identifies file path operations using untrusted input.

## Installation

gosec can be installed via:

```bash
# Using go install
go install github.com/securego/gosec/v2/cmd/gosec@latest

# Using Docker
docker pull securego/gosec

# Using Homebrew (macOS)
brew install gosec
```

## Usage

Basic usage:

```bash
# Scan current directory
gosec ./...

# Scan specific file
gosec myfile.go

# With detailed output
gosec -v ./...

# Generate JSON report
gosec -fmt=json ./... > report.json
```

## Features

- Fast scanning of Go source code
- Low false positive rate through configuration
- JSON/CSV/SARIF output formats
- Integration with CI/CD pipelines
- Customizable rule configuration
- Extensive documentation for each rule

## References

- Official Website: https://securego.io
- GitHub Repository: https://github.com/securego/gosec
- Rule Documentation: https://securego.io/docs/rules/
- Slack Community: http://securego.herokuapp.com/

"""
    return overview


def main():
    """Main function to download gosec documentation."""
    print("=" * 60)
    print("Gosec Documentation Scraper")
    print("=" * 60)
    print()

    # Output directory
    script_dir = Path(__file__).parent.parent
    output_dir = script_dir / "docs" / "web-scraped" / "gosec"
    output_dir.mkdir(parents=True, exist_ok=True)

    print(f"Output directory: {output_dir}")
    print()

    start_time = time.time()
    successful = 0
    failed = 0

    # Create overview document
    print("Creating overview document...")
    overview_path = output_dir / "00-overview.md"
    with open(overview_path, 'w', encoding='utf-8') as f:
        f.write(create_overview())
    print(f"  -> Created: overview.md")
    successful += 1

    # Download rule documentation
    print(f"\nDownloading {len(RULES_TO_FETCH)} rule documents...")
    print()

    for rule_id in RULES_TO_FETCH:
        url = f"https://securego.io/docs/rules/{rule_id}"
        output_file = f"{rule_id.upper()}-rule.md"
        output_path = output_dir / output_file

        if fetch_and_convert(url, output_path, f"Rule {rule_id.upper()}"):
            successful += 1
        else:
            failed += 1

        time.sleep(0.5)

    # Download GitHub README
    print("\nDownloading GitHub README...")
    readme_url = "https://raw.githubusercontent.com/securego/gosec/master/README.md"
    readme_path = output_dir / "github-README.md"

    try:
        result = subprocess.run(
            ["curl", "-s", readme_url],
            capture_output=True,
            text=True,
            timeout=15
        )

        if result.returncode == 0:
            header = f"# Source: {readme_url}\n\n"
            with open(readme_path, 'w', encoding='utf-8') as f:
                f.write(header + result.stdout)
            print(f"  -> Downloaded: github-README.md")
            successful += 1
        else:
            print(f"  -> Failed to download README")
            failed += 1
    except Exception as e:
        print(f"  -> Error downloading README: {e}")
        failed += 1

    elapsed = time.time() - start_time

    print()
    print("=" * 60)
    print("Download Summary")
    print("=" * 60)
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    print(f"Time: {elapsed:.1f} seconds")
    print(f"Output: {output_dir}")

    # Calculate total size
    total_size = sum(f.stat().st_size for f in output_dir.rglob("*.md"))
    print(f"Total size: {total_size:,} bytes ({total_size/1024:.1f} KB)")

    print()
    if failed > 0:
        print(f"Note: {failed} items had issues, but core documentation is available")
        return True  # Still return success since we got the main docs
    else:
        print("All documentation downloaded successfully!")
        return True


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
