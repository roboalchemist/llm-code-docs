#!/usr/bin/env python3
"""
Scraper for Tart documentation.
Tart is a macOS/Linux VM management tool for Apple Silicon.
Extracts documentation directly from the GitHub repository at https://github.com/cirruslabs/tart.

Official docs site: https://tart.run/ (MkDocs)
GitHub repo: https://github.com/cirruslabs/tart

Output: docs/web-scraped/tart/
"""

from pathlib import Path
from urllib.request import urlopen
import json

OUTPUT_DIR = Path(__file__).parent.parent / "docs" / "web-scraped" / "tart"

def download_file(url: str) -> str:
    """Download file from GitHub raw URL."""
    try:
        with urlopen(url, timeout=10) as response:
            return response.read().decode('utf-8')
    except Exception as e:
        print(f"Error downloading {url}: {e}")
        return ""

def create_output_dir():
    """Create output directory."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Created output directory: {OUTPUT_DIR}")

def fetch_readme():
    """Fetch and save README.md."""
    url = "https://raw.githubusercontent.com/cirruslabs/tart/main/README.md"
    content = download_file(url)

    if content:
        filepath = OUTPUT_DIR / "01-README.md"
        with open(filepath, 'w') as f:
            f.write("# Tart - macOS and Linux VMs on Apple Silicon\n\n")
            f.write("Source: https://github.com/cirruslabs/tart\n\n")
            f.write(content)
        print(f"✓ Saved README: {filepath}")
        return True
    return False

def fetch_quick_start():
    """Fetch quick start documentation."""
    url = "https://raw.githubusercontent.com/cirruslabs/tart/main/docs/quick-start.md"
    content = download_file(url)

    if content:
        filepath = OUTPUT_DIR / "02-QUICK-START.md"
        with open(filepath, 'w') as f:
            f.write("# Tart - Quick Start\n\n")
            f.write("Source: https://tart.run/quick-start\n\n")
            f.write(content)
        print(f"✓ Saved Quick Start: {filepath}")
        return True
    return False

def fetch_faq():
    """Fetch FAQ documentation."""
    url = "https://raw.githubusercontent.com/cirruslabs/tart/main/docs/faq.md"
    content = download_file(url)

    if content:
        filepath = OUTPUT_DIR / "03-FAQ.md"
        with open(filepath, 'w') as f:
            f.write("# Tart - Frequently Asked Questions\n\n")
            f.write("Source: https://tart.run/faq\n\n")
            f.write(content)
        print(f"✓ Saved FAQ: {filepath}")
        return True
    return False

def fetch_licensing():
    """Fetch licensing documentation."""
    url = "https://raw.githubusercontent.com/cirruslabs/tart/main/docs/licensing.md"
    content = download_file(url)

    if content:
        filepath = OUTPUT_DIR / "04-LICENSING.md"
        with open(filepath, 'w') as f:
            f.write("# Tart - Licensing\n\n")
            f.write("Source: https://tart.run/licensing\n\n")
            f.write(content)
        print(f"✓ Saved Licensing: {filepath}")
        return True
    return False

def fetch_integrations():
    """Fetch integration documentation."""
    integrations = [
        ("cirrus-cli", "Cirrus CLI Integration"),
        ("packer", "Packer Integration"),
        ("gitlab-runner", "GitLab Runner Integration"),
        ("buildkite", "Buildkite Integration"),
    ]

    integration_docs = "# Tart - Integration Guides\n\n"
    integration_docs += "Source: https://tart.run/integrations\n\n"
    integration_docs += "Integration guides for using Tart with popular CI/CD and VM management tools:\n\n"

    for file_name, title in integrations:
        url = f"https://raw.githubusercontent.com/cirruslabs/tart/main/docs/integrations/{file_name}.md"
        content = download_file(url)

        if content:
            # Remove the front matter/title if present and use our title
            lines = content.split('\n')
            # Skip first empty lines and title
            start_idx = 0
            for i, line in enumerate(lines):
                if line.startswith('# '):
                    start_idx = i + 1
                    break

            cleaned_content = '\n'.join(lines[start_idx:]).strip()
            integration_docs += f"## {title}\n\n"
            integration_docs += f"**Guide:** `docs/integrations/{file_name}.md`\n\n"
            integration_docs += cleaned_content + "\n\n"
            print(f"✓ Downloaded integration: {title}")
        else:
            print(f"✗ Failed to download integration: {title}")

    if integration_docs:
        filepath = OUTPUT_DIR / "05-INTEGRATIONS.md"
        with open(filepath, 'w') as f:
            f.write(integration_docs)
        print(f"✓ Saved integrations: {filepath}")
        return True
    return False

def create_index():
    """Create an index file."""
    index = """# Tart Documentation

**Project:** Tart - macOS and Linux VMs on Apple Silicon
**Repository:** https://github.com/cirruslabs/tart
**Official Website:** https://tart.run
**License:** FAIR License

## Overview

Tart is a command-line utility to manage macOS and Linux virtual machines on Apple Silicon (M1, M2, M3, M4). It provides:

- **Fast VM creation and cloning** - Create and clone VMs in seconds
- **Efficient storage** - Copy-on-write cloning with minimal disk usage
- **Networking** - Out-of-the-box support for VM networking
- **Integration** - Seamless integration with CI/CD systems, Packer, and more
- **Apple Silicon native** - Optimized for Apple Silicon performance

## Key Features

- **VM Management**: Create, clone, run, stop, and delete VMs
- **Networking**: Configure and manage VM network interfaces
- **Snapshots**: Create and manage VM snapshots for rollback
- **CI/CD Integration**: Native support for GitHub Actions, Cirrus CI, GitLab Runner, Buildkite
- **Packer Support**: Build VM images with Packer
- **RESTful API**: Control Tart via HTTP API
- **Pull Remote Images**: Automatically pull pre-built images from remote sources

## What's Included

1. **01-README.md** - Project overview and main repository documentation
2. **02-QUICK-START.md** - Installation instructions and getting started guide
3. **03-FAQ.md** - Frequently asked questions and troubleshooting
4. **04-LICENSING.md** - Licensing and legal information
5. **05-INTEGRATIONS.md** - Integration guides for Cirrus CI, Packer, GitLab Runner, Buildkite

## Quick Start

### Installation

```bash
brew install cirruslabs/tart/tart
```

### Create a VM

```bash
# Pull a base macOS image
tart pull ghcr.io/cirruslabs/macos-monterey:latest

# Clone and name it
tart clone ghcr.io/cirruslabs/macos-monterey:latest my-vm

# Run the VM
tart run my-vm
```

### Clone VMs

```bash
# Clone an existing VM
tart clone my-vm my-vm-clone
```

### Stop and Delete

```bash
# Stop a running VM
tart stop my-vm

# Delete a VM
tart delete my-vm
```

## Common Commands

```bash
# List all VMs
tart list

# Create a VM from scratch
tart create --disk-size 50G my-new-vm

# Get VM information
tart info my-vm

# Take a snapshot
tart snapshot create my-vm snapshot-1

# Restore from snapshot
tart snapshot restore my-vm snapshot-1

# Run with specific CPU/memory
tart run --cpus 4 --memory 8G my-vm

# SSH into VM
tart run my-vm --ssh

# Pull images from registry
tart pull ghcr.io/cirruslabs/ubuntu-sonoma:latest
```

## Networking

Tart VMs have automatic networking configuration:

- **Bridge Mode**: VMs appear on the same network as the host
- **NAT Mode**: VMs have private networking with port forwarding
- **Custom Networks**: Configure custom network bridges

See **05-INTEGRATIONS.md** for detailed networking configuration examples.

## Integration Guides

### Cirrus CI

Run Cirrus CI tasks on Tart VMs using the Cirrus CLI integration. See **05-INTEGRATIONS.md** for setup instructions.

### Packer

Build custom VM images with Packer. The Tart builder allows creating reproducible VM images.

### GitHub Actions

Use Tart with GitHub Actions for macOS CI/CD workflows.

### GitLab Runner

Deploy a Tart-based GitLab Runner for native macOS job execution.

### Buildkite

Run Buildkite agents on Tart VMs for CI/CD pipelines.

## Use Cases

- **CI/CD on Apple Silicon** - Run macOS builds natively on M-series Macs
- **Multi-VM Testing** - Create and manage multiple test environments
- **Development Environments** - Isolated VMs for different project versions
- **Virtual Machine Farming** - Run multiple VMs for parallel testing
- **Pre-built Image Distribution** - Share standardized VM images via registries

## Architecture

Tart uses Apple's Hypervisor framework for efficient VM management on Apple Silicon. VMs use:

- **QEMU** for x86_64 emulation (when needed)
- **Hypervisor.framework** for native Apple Silicon VMs
- **Copy-on-Write** (CoW) for efficient storage

## Links

- [Tart GitHub Repository](https://github.com/cirruslabs/tart)
- [Tart Official Website](https://tart.run)
- [Tart on Homebrew](https://github.com/cirruslabs/homebrew-tart)
- [Cirrus CI](https://cirrus-ci.org)
- [Packer Tart Builder](https://www.packer.io)

## Contributing

Contributions are welcome! See the GitHub repository for contribution guidelines.

## Support

For issues, questions, and discussions:
- GitHub Issues: https://github.com/cirruslabs/tart/issues
- GitHub Discussions: https://github.com/cirruslabs/tart/discussions
- Cirrus Community Slack: https://cirrus-ci.org
"""

    filepath = OUTPUT_DIR / "00-INDEX.md"
    with open(filepath, 'w') as f:
        f.write(index)
    print(f"✓ Created index: {filepath}")
    return True

def main():
    """Main scraper function."""
    print("Scraping Tart documentation...")
    print(f"Output directory: {OUTPUT_DIR}\n")

    create_output_dir()

    results = []
    results.append(("README", fetch_readme()))
    results.append(("Quick Start", fetch_quick_start()))
    results.append(("FAQ", fetch_faq()))
    results.append(("Licensing", fetch_licensing()))
    results.append(("Integrations", fetch_integrations()))
    results.append(("Index", create_index()))

    print("\n" + "="*50)
    print("Scraping Summary:")
    print("="*50)
    for name, success in results:
        status = "✓ Success" if success else "✗ Failed"
        print(f"{status}: {name}")

    success_count = sum(1 for _, s in results if s)
    total_count = len(results)
    print(f"\nTotal: {success_count}/{total_count} successful")
    print(f"Output saved to: {OUTPUT_DIR}")

    # List saved files
    if OUTPUT_DIR.exists():
        files = sorted(OUTPUT_DIR.glob("*.md"))
        print(f"\nFiles created: {len(files)}")
        for f in files:
            size = f.stat().st_size
            print(f"  - {f.name} ({size:,} bytes)")

    return success_count == total_count

if __name__ == "__main__":
    exit(0 if main() else 1)
