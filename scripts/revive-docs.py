#!/usr/bin/env python3
"""
Scraper for Revive Go linter documentation.
Source: https://revive.run/
Output: docs/web-scraped/revive/

Revive is a fast, configurable linter for Go with 60+ style rules.
It's a modern replacement for the deprecated golint.
"""
import requests
from pathlib import Path
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import re
import sys

OUTPUT_DIR = Path("/home/nuc2/github/llm-code-docs/docs/web-scraped/revive")
BASE_URL = "https://revive.run"
DOCS_URL = f"{BASE_URL}/docs"

# Create output directory
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def clean_html_to_markdown(html_content):
    """Convert HTML to basic markdown format."""
    # Remove script and style elements
    for script in html_content(["script", "style"]):
        script.decompose()

    text = html_content.get_text()

    # Clean up whitespace
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)

    return text

def fetch_page(url):
    """Fetch a page and return BeautifulSoup object."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return BeautifulSoup(response.content, 'html.parser')
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

def extract_docs_pages():
    """Extract all documentation pages from revive.run/docs."""
    print("Fetching Revive documentation index...")

    soup = fetch_page(DOCS_URL)
    if not soup:
        print("Failed to fetch documentation index")
        return []

    # Find all documentation links - revive.run appears to be a Gatsby site
    # Look for internal links in nav and content
    pages = set()

    # Find all links that start with /docs/
    for link in soup.find_all('a', href=True):
        href = link.get('href', '')
        if href.startswith('/docs/'):
            # Extract the page path
            pages.add(href)

    # Add common documentation pages we know should exist
    common_pages = [
        '/docs/',
        '/docs/introduction',
        '/docs/getting-started',
        '/docs/configuration',
        '/docs/rules',
        '/docs/formatters',
    ]

    for page in common_pages:
        pages.add(page)

    # Convert to full URLs
    full_urls = [urljoin(BASE_URL, page) for page in pages]

    return list(set(full_urls))

def scrape_documentation():
    """Scrape all documentation pages from revive.run."""
    print(f"Output directory: {OUTPUT_DIR}")

    # First, get the homepage to understand structure
    print("\nFetching homepage...")
    homepage = fetch_page(BASE_URL)
    if homepage:
        homepage_content = clean_html_to_markdown(homepage)
        with open(OUTPUT_DIR / "index.md", "w") as f:
            f.write(f"# Revive - Fast Go Linter\n\n")
            f.write(f"Source: {BASE_URL}\n\n")
            f.write(homepage_content)
        print("✓ Created index.md")

    # Fetch documentation pages
    print("\nFetching documentation pages...")
    pages = extract_docs_pages()

    if not pages:
        print("No documentation pages found automatically, creating manual structure...")
        pages = [
            f"{DOCS_URL}/",
            f"{DOCS_URL}/getting-started",
            f"{DOCS_URL}/configuration",
            f"{DOCS_URL}/rules",
            f"{DOCS_URL}/formatters",
        ]

    page_count = 0
    for url in pages:
        if not url.startswith(DOCS_URL):
            continue

        print(f"Fetching {url}...")
        soup = fetch_page(url)

        if not soup:
            continue

        # Extract page title
        title = soup.find('h1')
        title_text = title.get_text(strip=True) if title else "Documentation"

        # Extract main content
        main_content = soup.find(['main', 'article', 'div.content'])
        if not main_content:
            main_content = soup.body

        content = clean_html_to_markdown(main_content)

        # Create filename from URL
        path_parts = urlparse(url).path.strip('/').split('/')
        filename = '_'.join(filter(None, path_parts)) + '.md'
        if not filename.startswith('docs'):
            filename = 'docs_' + filename

        if filename == 'docs_.md':
            filename = 'docs_home.md'

        # Write markdown file
        filepath = OUTPUT_DIR / filename
        with open(filepath, "w") as f:
            f.write(f"# {title_text}\n\n")
            f.write(f"Source: {url}\n\n")
            f.write(content)

        print(f"✓ Created {filename}")
        page_count += 1

    print(f"\nScraped {page_count} pages")

    # Create a comprehensive README about Revive
    create_comprehensive_readme()

def create_comprehensive_readme():
    """Create a comprehensive README about Revive."""
    readme_content = """# Revive - Fast Go Linter Documentation

## Overview

**Revive** is a fast, configurable linter for Go with 60+ style rules. It serves as a modern replacement for the deprecated `golint`, providing flexible static code analysis for Go projects.

- **Official Website**: https://revive.run
- **GitHub Repository**: https://github.com/mgechev/revive
- **Primary Language**: Go
- **Purpose**: Static code analysis and linting

## Key Features

- **Fast**: Highly performant linting written in Go
- **Configurable**: Extensive customization via TOML configuration files
- **60+ Rules**: Comprehensive set of built-in style and code quality rules
- **Drop-in Replacement**: Direct replacement for the deprecated golint
- **Multiple Output Formats**: Support for various formatter options
- **Custom Rules**: Ability to define and integrate custom linting rules
- **Integration**: Works with golangci-lint and other Go tooling

## Getting Started

### Installation

```bash
# Using go install (recommended)
go install github.com/mgechev/revive@latest

# Using Docker
docker run ghcr.io/mgechev/revive:latest

# Manual binary download
# Visit https://github.com/mgechev/revive/releases
```

### Basic Usage

```bash
# Lint current directory
revive ./...

# Lint with specific config
revive -config revive.toml ./...

# Use specific formatter
revive -formatter json ./...

# Exclude files
revive -exclude file1.go -exclude file2.go ./...
```

## Configuration

Revive uses TOML configuration files (typically named `revive.toml` or `.revive.toml`).

### Configuration Example

```toml
# Enable all rules by default
ignoreFailures = false

# Comma-separated list of rules to enable
enableAllRules = false

# Rules configuration
[rule.blank-imports]
enabled = true

[rule.context-keys-type]
enabled = true

[rule.cyclomatic]
enabled = true
arguments = [3]

[rule.early-return]
enabled = true

[rule.error-naming]
enabled = true

[rule.error-return]
enabled = true
```

### Default Configuration

Revive provides a default configuration file (`defaults.toml`) with sensible defaults for most projects. You can customize this by creating a `revive.toml` file in your project root.

## Available Rules

Revive includes 60+ built-in rules covering:

- **Code Quality**: cyclomatic complexity, cognitive complexity, nesting levels
- **Naming Conventions**: variable naming, function naming, package naming
- **Error Handling**: proper error returns, unused error values
- **Best Practices**: early return, blank imports, context usage
- **Documentation**: exported function documentation, comment formatting
- **Performance**: unused parameters, inefficient code patterns
- **Style**: code formatting, consistency, readability

See the official documentation for the complete list of rules and their configurations.

## Output Formatters

Revive supports multiple output formats:

- **Default**: Human-readable text format
- **JSON**: Structured JSON output for tool integration
- **SARIF**: Standard analysis result interchange format
- **Checkstyle**: XML format compatible with CI/CD tools
- **Tab**: Tab-separated values for script processing

Example:
```bash
revive -formatter json ./... > lint-results.json
revive -formatter sarif ./... > results.sarif
```

## Integration with Other Tools

### golangci-lint

Revive is integrated into golangci-lint, making it easy to use within your existing Go toolchain:

```bash
golangci-lint run
# Uses revive as one of the configured linters
```

### IDE Integration

- **GoLand**: Native support via Revive configuration
- **VS Code**: Via Go extension with Revive support
- **Vim**: Via vim-go or similar plugins

### CI/CD Integration

Revive can be easily integrated into your CI/CD pipeline:

```yaml
# GitHub Actions example
- name: Run Revive Linter
  run: |
    go install github.com/mgechev/revive@latest
    revive -config revive.toml -formatter sarif ./... > results.sarif

- name: Upload SARIF results
  uses: github/codeql-action/upload-sarif@v2
  with:
    sarif_file: results.sarif
```

## Configuration Best Practices

1. **Start with defaults**: Use the default configuration as a base
2. **Customize incrementally**: Enable/disable rules as needed for your project
3. **Document your choices**: Add comments to your revive.toml explaining why certain rules are configured
4. **Team agreement**: Ensure team consensus on linting rules
5. **Version control**: Commit revive.toml to ensure consistent linting across developers

## Troubleshooting

### Rule not enabled

Check that the rule is:
1. Listed in your `revive.toml` with `enabled = true`
2. Not in the exclude list
3. Spelled correctly

### Performance issues

If Revive runs slowly:
1. Check for unnecessary exclusions
2. Consider using rule filtering for development
3. Enable only the rules your project needs

### Configuration not applied

- Ensure the config file is named correctly (`revive.toml` or `.revive.toml`)
- Use the `-config` flag to explicitly specify the configuration file path
- Check for TOML syntax errors in your configuration

## Command-Line Flags

Key command-line options:

```
-config FILE           Path to config file
-formatter STRING      Output formatter (default: "default")
-exclude PATTERN       Exclude files/paths
-ignore RULE           Disable specific rules
-enable-all-rules      Enable all available rules
-max-open-files INT    Maximum open files
-tmp-dir DIR          Temporary directory for analysis
```

## Resources

- **Official Website**: https://revive.run
- **GitHub Repository**: https://github.com/mgechev/revive
- **Issue Tracker**: https://github.com/mgechev/revive/issues
- **Discussions**: https://github.com/mgechev/revive/discussions
- **Releases**: https://github.com/mgechev/revive/releases

## Related Tools

- **golangci-lint**: Comprehensive Go linter that includes Revive
- **gofmt**: Go code formatter
- **go vet**: Official Go analysis tool
- **staticcheck**: Additional static analysis for Go

## Version Information

Revive is actively maintained and regularly updated. Check the GitHub releases page for the latest version and changelog.

---

*Documentation source: https://revive.run and https://github.com/mgechev/revive*
"""

    with open(OUTPUT_DIR / "README.md", "w") as f:
        f.write(readme_content)

    print("✓ Created comprehensive README.md")

def create_index_yaml_entry():
    """Create index entry for revive documentation."""
    entry = """
  - name: revive
    type: web-scraped
    source_url: https://revive.run
    description: Fast configurable linter for Go with 60+ style rules, replacement for deprecated golint
    path: docs/web-scraped/revive
    file_count: 0
    size_bytes: 0
    updated: 2025-01-06
"""
    print("\nIndex entry (add to index.yaml):")
    print(entry)

if __name__ == "__main__":
    try:
        scrape_documentation()
        create_index_yaml_entry()
        print("\n✓ Revive documentation scraped successfully!")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
