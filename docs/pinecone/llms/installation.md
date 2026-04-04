# Source: https://docs.pinecone.io/reference/cli/installation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinecone.io/llms.txt
> Use this file to discover all available pages before exploring further.

# CLI installation

<Note>
  This feature is in [public preview](/release-notes/feature-availability).
</Note>

This document describes how to install the Pinecone CLI on your local machine.

## Platforms

Pinecone's CLI is available for the following platforms:

* **macOS**: Intel (x86\_64) and Apple Silicon (ARM64)
* **Linux**: x86\_64, ARM64, and i386 architectures
* **Windows**: x86\_64 and i386 architectures

## Installation

### Homebrew (macOS)

The most convenient way to install the CLI on Mac:

```bash  theme={null}
brew tap pinecone-io/tap
brew install pinecone-io/tap/pinecone
```

To upgrade to the latest version:

```bash  theme={null}
brew update
brew upgrade pinecone
```

### Direct download (all platforms)

Pre-built binaries for all supported platforms are available on the [GitHub Releases page](https://github.com/pinecone-io/cli/releases).

### Build from source

To build from source, see the [CONTRIBUTING.md](https://github.com/pinecone-io/cli/blob/main/CONTRIBUTING.md) file for detailed instructions. To build from source, you need Go v1.23+.
