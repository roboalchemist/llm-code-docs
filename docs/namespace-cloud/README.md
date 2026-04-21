# Namespace Cloud Documentation

Complete documentation for Namespace Devboxes and cloud development environments.

## Overview

Namespace provides managed cloud development environments with enterprise-grade performance and intelligent lifecycle management. This documentation covers:

- Managing devboxes and ephemeral instances
- Remote development and IDE integration
- CLI reference for the `nsc` tool
- Architecture and infrastructure details
- Custom images and environment configuration

## Quick Start

1. [Introduction](01-introduction.md) - Overview and key concepts
2. Install the CLI: `brew install namespacelabs/namespace/nsc`
3. Authenticate: `nsc login`
4. Create an instance: `nsc create`
5. Connect: `nsc ssh <instance-id>`

## Core Documentation

### Devbox Management

- [Managing Devboxes](02-managing-devboxes.md) - Creating, stopping, and configuring instances
- [Remote Development](03-remote-development.md) - SSH, IDE integration, and connection methods
- [Sessions](04-sessions.md) - Persistent terminal environments
- [Custom Images](05-custom-images.md) - Creating Dockerfile-based base images

### CLI Reference

- [CLI Overview](06-cli-reference-overview.md)
- [Authentication](07-cli-version.md), [08-cli-login.md](08-cli-login.md)
- **Instance Management**: [create](10-cli-create.md), [destroy](11-cli-destroy.md), [list](12-cli-list.md), [extend](13-cli-extend.md)
- **Remote Access**: [ssh](14-cli-ssh.md), [logs](15-cli-logs.md), [top](16-cli-top.md)
- **Containers**: [build](17-cli-build.md), [run](18-cli-run.md)
- **Workspace**: [workspace-describe](09-cli-workspace-describe.md)

### Architecture

- [Compute Platform Overview](19-architecture-compute.md)
- [SSH and Remote Access](20-architecture-ssh-remote-access.md)
- [Machine Shapes](21-architecture-machine-shapes.md)
- [Resource Limits](22-architecture-resource-limits.md)

## Common Workflows

### Create and Connect to a Devbox

```bash
# Authenticate
nsc login

# Create an instance
nsc create

# Connect via SSH
nsc ssh <instance-id>
```

### Run a Container

```bash
# Build an image
nsc build . --name myapp --push

# Run the container
nsc run --image myapp --duration 1h
```

### Set Up Custom Development Environment

1. Create a Dockerfile with your tools
2. Build a custom image: `nsc image build . --name my-team/golang`
3. Create devboxes from that image: `nsc create --image my-team/golang`

### Connect via IDE

```bash
# Open in VS Code
nsc ssh <instance-id>

# Or use dashboard for IDE integration
```

## Environment Details

- **Runtime**: Linux AMD64
- **CLI Support**: macOS, Linux, Windows
- **Enterprise**: SAML SSO, SCIM, audit logs available

## Support

For additional help or questions about Namespace Devboxes, visit the support section at https://namespace.so/support
