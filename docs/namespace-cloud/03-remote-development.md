# Remote Development with Devboxes

This documentation explains how to connect to Namespace Devboxes from your local environment using SSH, terminal access, or integrated development environments.

## Overview

All connections to devboxes are tunneled securely through the Namespace API with no public IP addresses required.

## Connection Methods

### Terminal Access

**Direct SSH connection:**

```bash
devbox ssh main
```

**Standard SSH configuration:**

```bash
devbox configure-ssh main
```

After configuration, connect using standard SSH tools like `scp` and `rsync`, or connect via:

```bash
ssh main.devbox.namespace
```

**SSH key-based access:**

Provide your public SSH key during instance creation:

```bash
nsc create --ssh_key ~/.ssh/id_ed25519.pub
```

Native SSH connection format:

```bash
ssh <instance-id>@ssh.<region>.namespace.so
```

### IDE Integration

**VS Code and Cursor:**

- Connect via dashboard
- CLI: `devbox open-ide`

**JetBrains IDEs:**

- Connect through JetBrains Gateway

**Zed editor:**

- Native SSH support

## Port Forwarding

Enable port forwarding for local development workflows.

## Prerequisites

Before attempting connections, you need:

- Devbox CLI installed
- Authentication completed
- A running devbox instance

## Related Topics

- Persistent sessions
- Devbox lifecycle management
- Custom base images
