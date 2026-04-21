# nsc logs

Retrieve and display logs from Kubernetes instances and their workloads.

## Overview

The tool outputs logs to standard output and supports real-time streaming or historical log retrieval for Kubernetes instances only.

## Basic Usage

```bash
nsc logs <instance-id> [-n <namespace>] [-p <pod>] [-c <container>] [--since <duration>] [-f] [--raw]
```

## Key Options

| Flag | Purpose |
|------|---------|
| `-n <namespace>` | Filter logs to a specific Kubernetes namespace |
| `-p <pod>` | Limit output to a particular pod |
| `-c <container>` | Target a specific container within a pod |
| `-f` | Stream logs continuously from the current moment |
| `--since <duration>` | Show logs from a relative timepoint (e.g., "42m") |
| `--raw` | Display logs without namespace/pod/container labels |
| `--source` | Specify log source (kubernetes or containerd) |
| `--all` | Include system-level Kubernetes logs |

## Usage Examples

Create an instance and view kube-system namespace logs:

```bash
$ nsc create
$ nsc logs 1lf2ol9ioulce -n kube-system
```

Stream logs in real-time:

```bash
$ nsc logs 1lf2ol9ioulce -n kube-system -f
```

View logs from a specific pod:

```bash
nsc logs <instance-id> -n my-namespace -p my-pod
```

View logs from a specific container:

```bash
nsc logs <instance-id> -n my-namespace -p my-pod -c my-container
```

## Important Notes

This command works exclusively with Kubernetes instances created via `nsc create` (instances with k3s enabled).
