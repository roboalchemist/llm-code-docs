# Managing Devboxes

This documentation covers managing devboxes on the Namespace platform, including creation, deletion, monitoring, and configuration options.

## Machine Sizes

The platform offers four size tiers (S, M, L, XL) with burstable vCPU allocations:

- **S**: 4 cores, 8GB memory
- **M**: 8 cores, 16GB memory
- **L**: 16 cores, 32GB memory
- **XL**: 32 cores, 64GB memory

## Listing Devboxes

Users can list devboxes via CLI or through the dashboard:

- **CLI**: `devbox list` or `nsc list`
- **Dashboard**: cloud.namespace.so/workspace/devboxes

## Starting & Stopping

**Starting:**
Devboxes launch automatically when accessed.

**Stopping:**

- Via CLI: `devbox shutdown` or `nsc destroy <instance-id>`
- Via dashboard: Use the shutdown option

**Important**: Stopped devboxes retain all persistent storage.

## Auto-Stop Configuration

Idle timeout options range from 15 minutes to 8 hours. Idleness is detected by checking for:

- Active SSH connections
- Recent sessions
- Files in the `/.namespace/tasks` directory

## Deletion

Devboxes are permanently removed via:

```bash
devbox delete <instance-id>
nsc destroy <instance-id> [--force]
```

The `--force` flag bypasses confirmation prompts.

## Volume Management

Users can specify persistent volume size using:

```bash
--volume_size_gb <size>
```

## Spec File Creation

Non-interactive creation is possible using configuration files (YAML, JSON, TOML):

```bash
devbox create --from devbox.yaml
```

Configuration files can specify:

- Name
- Image
- Size
- Repository
- Access mode
- Idle timeout
- Tailscale integration

## Workspace Defaults

Admins can configure default settings for all new devboxes:

- Instance size
- Image
- Repository
- Access mode
- Idle timeout
- Tailscale integration

## Additional Features

The platform provides:

- Git configuration management
- GitHub CLI setup
- Resource monitoring with live metrics
- Site latency checking
- CLI self-updates
