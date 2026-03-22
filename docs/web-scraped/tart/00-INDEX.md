# Tart Documentation

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
