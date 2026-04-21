# CLI Reference - Overview

The `nsc` CLI tool is the command-line interface for managing Namespace Devboxes and instances. It's available for macOS, Linux, and Windows.

## Installation Methods

- **Homebrew (macOS/Linux)**: `brew install namespacelabs/namespace/nsc`
- **npm**: Available through npm package manager
- **Hermit**: Package manager option
- **Windows**: Native installation support
- **Linux**: Native installation support

## Maintenance

New versions of the `nsc` tool are released regularly. For users with Homebrew installations, update using:

```bash
brew upgrade nsc
```

## Core Commands

The CLI includes commands for:

- **Authentication**: login, workspace operations
- **Instance Management**: create, destroy, list, extend
- **Remote Access**: ssh, vnc, rdp, proxy
- **Kubernetes**: kubeconfig, kubectl
- **Docker**: docker login, docker attach, buildx operations
- **Build & Run**: build, run
- **Exposure & Ingress**: expose, expose-kubernetes
- **GitHub Profiles**: github-profile operations
- **Git & Volumes**: update-submodules, volume operations
- **Artifacts**: upload, download, expire
- **Registry**: list, describe, share operations
- **Build Caching**: bazel, gradle, pants, sccache setup
- **Secrets/Vault**: list, add, set, delete
- **Tokens**: create, list, revoke

## Getting Started

1. Install the CLI tool
2. Run `nsc login` to authenticate
3. Use `nsc create` to launch an instance
4. Connect via `nsc ssh <instance-id>`

## Documentation Structure

Detailed documentation for each command is available at `/docs/reference/cli/<command-name>`.
