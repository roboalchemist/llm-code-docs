# 0G Storage CLI

The 0G Storage CLI is your command-line gateway to interact directly with the 0G Storage network. It simplifies the process of uploading and downloading files while providing full control over your decentralized storage operations.

## Why Use the CLI?

- **Direct Control**: Manage data location and versioning with precision
- **Automation Ready**: Build scripts and cron jobs for regular operations
- **Full Feature Access**: Access all storage and KV operations from the terminal
- **Developer Friendly**: Perfect for integrating into your development workflow

:::tip Web-Based Alternative
For a quick and easy web interface, try the [0G Storage Web Tool](https://storagescan-galileo.0g.ai/tool) - perfect for one-off uploads and downloads.
:::

## Installation

### Prerequisites
- Go 1.18 or higher installed on your system
- Git for cloning the repository

### Setup Steps

**1. Clone the Repository**

```bash
git clone https://github.com/0gfoundation/0g-storage-client.git
cd 0g-storage-client
```

**2. Build the Binary**

```bash
go build
```

**3. Add to PATH** (Optional but recommended)

```bash