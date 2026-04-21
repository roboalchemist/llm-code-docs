# nsc create

Initialize a new ephemeral Namespace instance.

## Overview

The `nsc create` command creates ephemeral Namespace instances with isolated Kubernetes environments by default (using k3s).

## Basic Usage

```bash
nsc create [options]
```

## What It Does

- Creates instances with configurable machine specifications
- Returns a unique instance ID for reference
- Sets automatic expiration deadlines

## Machine Configuration

Supports flexible CPU/memory combinations:

- **CPUs**: [2, 4, 8, 16, 32]
- **RAM**: [2, 4, 8, 16, 32, 64, 80, 96, 112, 128, 256, 384, 512]

Enables cross-architecture deployment (e.g., `linux/arm64:2x8`)

Availability depends on your plan and concurrency limits.

## Key Options

| Flag | Purpose |
|------|---------|
| `--machine_type` | Specify CPU/memory configuration and OS/architecture |
| `--output_to <path>` | Save instance ID to file for automation |
| `--wait_kube_system` | Wait for Kubernetes system namespace readiness |
| `--duration` | Set ephemeral environment lifespan (e.g., "10m") |
| `--bare` | Create minimal environment without Kubernetes |
| `--volume` | Attach cache or persistent storage volumes |
| `--label` | Add metadata annotations visible in web UI |
| `--ssh_key` | Provide SSH public key for native SSH access |

## Experimental Features

Advanced users can enable disk images and containerd shims through a JSON configuration file passed via `--experimental_from`.

## Example Usage

```bash
nsc create
nsc create --machine_type 8x16
nsc create --duration 2h
nsc create --volume persistent:mydata:/data:10
```
