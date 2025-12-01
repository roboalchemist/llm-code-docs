#!/usr/bin/env python3
"""
Namecheap API Documentation Scraper
Downloads documentation from both Go and Python SDKs.
Since Namecheap's website is behind Cloudflare, we extract docs from GitHub.
"""

import sys
import subprocess
from pathlib import Path
import tempfile
import re

# SDK configurations
SDKS = {
    "namecheap-go": {
        "repo": "https://github.com/namecheap/go-namecheap-sdk.git",
        "branch": "master",
        "description": "Official Go SDK for Namecheap API",
        "files": [
            "README.md",
            "CONTRIBUTING.md",
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
        ],
    },
    "namecheap-python": {
        "repo": "https://github.com/adriangalilea/namecheap-python.git",
        "branch": "main",
        "description": "Modern Python SDK with CLI and TUI tools",
        "files": [
            "README.md",
            "CLI.md",
            "examples/README.md",
            "examples/quickstart.py",
            "src/namecheap/__init__.py",
            "src/namecheap/client.py",
            "src/namecheap/models.py",
            "src/namecheap/errors.py",
            "src/namecheap/_api/domains.py",
            "src/namecheap/_api/dns.py",
            "src/namecheap/_api/users.py",
        ],
    },
}


def clone_repo(repo_url: str, branch: str, temp_dir: Path) -> bool:
    """Clone a repository."""
    print(f"  Cloning {repo_url}...")
    try:
        result = subprocess.run(
            ["git", "clone", "--depth", "1", "--branch", branch, repo_url, str(temp_dir)],
            capture_output=True,
            text=True,
            timeout=60
        )
        if result.returncode != 0:
            print(f"  Error cloning: {result.stderr}")
            return False
        return True
    except Exception as e:
        print(f"  Error: {e}")
        return False


def source_to_markdown(content: str, filename: str, repo_url: str) -> str:
    """Convert source file to markdown with proper formatting."""
    ext = Path(filename).suffix

    # Determine language for code blocks
    lang_map = {".go": "go", ".py": "python"}
    lang = lang_map.get(ext, "")

    # Build GitHub URL
    github_url = repo_url.replace(".git", "") + f"/blob/main/{filename}"
    if "go-namecheap-sdk" in repo_url:
        github_url = repo_url.replace(".git", "") + f"/blob/master/{filename}"

    base_name = Path(filename).stem
    title = base_name.replace('_', ' ').replace('-', ' ').title()

    md = f"# {title}\n\n"
    md += f"Source: {github_url}\n\n"

    if ext in [".go", ".py"]:
        md += f"```{lang}\n{content}\n```\n"
    else:
        md += content

    return md


def extract_docs(temp_dir: Path, output_dir: Path, files: list, repo_url: str) -> int:
    """Extract documentation from source files."""
    output_dir.mkdir(parents=True, exist_ok=True)

    successful = 0

    for file_path in files:
        src_path = temp_dir / file_path

        if not src_path.exists():
            print(f"    Skipping (not found): {file_path}")
            continue

        content = src_path.read_text(encoding='utf-8')

        # Determine output filename (flatten paths)
        if file_path.endswith('.md'):
            if '/' in file_path:
                out_name = file_path.replace('/', '-')
            else:
                out_name = file_path
            # Add source header to markdown files
            github_url = repo_url.replace(".git", "")
            branch = "main" if "namecheap-python" in repo_url else "master"
            out_content = f"# Source: {github_url}/blob/{branch}/{file_path}\n\n{content}"
        else:
            out_name = Path(file_path).stem + ".md"
            out_content = source_to_markdown(content, file_path, repo_url)

        out_path = output_dir / out_name
        out_path.write_text(out_content, encoding='utf-8')
        print(f"    Extracted: {out_name}")
        successful += 1

    return successful


def create_index(output_dir: Path, sdk_name: str, sdk_config: dict):
    """Create an index file for documentation."""
    repo_url = sdk_config["repo"].replace(".git", "")
    description = sdk_config["description"]

    index_content = f"""# Namecheap API Documentation ({sdk_name})

{description}

## Source Repository

- GitHub: {repo_url}

## Official Namecheap Resources

- [Namecheap API Documentation](https://www.namecheap.com/support/api/intro/)
- [API Sandbox](https://www.sandbox.namecheap.com/)

## API Methods

### Domains
- `namecheap.domains.getList` - Returns list of domains for user
- `namecheap.domains.getInfo` - Get domain details
- `namecheap.domains.check` - Check domain availability

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
- `ApiUser` / `api_user` - Your Namecheap username
- `ApiKey` / `api_key` - Your API key (from account settings)
- `UserName` / `username` - Username on whose behalf the call is made
- `ClientIp` / `client_ip` - Your whitelisted IP address

## Environments

- **Production**: `https://api.namecheap.com/xml.response`
- **Sandbox**: `https://api.sandbox.namecheap.com/xml.response`

## Files in this directory

"""

    for md_file in sorted(output_dir.glob("*.md")):
        if md_file.name != "index.md":
            index_content += f"- [{md_file.stem}]({md_file.name})\n"

    (output_dir / "index.md").write_text(index_content, encoding='utf-8')
    print(f"    Created: index.md")


def main():
    """Main function."""
    print("=" * 60)
    print("Namecheap API Documentation Scraper")
    print("=" * 60)

    script_dir = Path(__file__).parent.parent
    base_output_dir = script_dir / "docs" / "web-scraped"

    total_files = 0

    for sdk_name, sdk_config in SDKS.items():
        print(f"\n{sdk_name}:")
        print(f"  {sdk_config['description']}")

        output_dir = base_output_dir / sdk_name

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)

            if not clone_repo(sdk_config["repo"], sdk_config["branch"], temp_path):
                print(f"  Failed to clone {sdk_name}")
                continue

            print("  Extracting documentation...")
            count = extract_docs(temp_path, output_dir, sdk_config["files"], sdk_config["repo"])

            print("  Creating index...")
            create_index(output_dir, sdk_name, sdk_config)

            total_files += count + 1  # +1 for index

            # Calculate size
            total_size = sum(f.stat().st_size for f in output_dir.glob("*.md"))
            print(f"  Size: {total_size:,} bytes ({total_size/1024:.1f} KB)")

    print("\n" + "=" * 60)
    print("Summary")
    print("=" * 60)
    print(f"Total files: {total_files}")
    print(f"Output directories:")
    for sdk_name in SDKS:
        print(f"  - docs/web-scraped/{sdk_name}/")
    print("\nDone!")


if __name__ == "__main__":
    main()
