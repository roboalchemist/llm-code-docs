# nsc run

Launch containers in ephemeral environments.

## Overview

The `nsc run` command creates temporary compute environments to run containerized workloads.

## Basic Usage

```bash
nsc run [--on <id>] --image <reference> [-p <ports>] [--ingress <rules>] [--name <name>] [--] [args]
```

## Essential Options

### --image <reference> (Required)

Specifies the OCI-compatible container image to run. Public registries are supported, as well as private images from `nscr.io`.

### -p <ports>

Exposes specified ports as public HTTPS endpoints with automatic TLS termination. Currently supports HTTP backend traffic only.

### --on <id>

Deploys containers to an existing environment rather than creating a new one, enabling shared networking between containers.

### --name <name>

Assigns a custom container name for observability and logging purposes.

### --volume <volume>

Attaches storage volumes using the format: `{cache|persistent}:{tag}:{mountpoint}:{size}`

### --duration

Sets lifespan for the ephemeral environment (e.g., `--duration 10m`)

### --ingress <rules>

Configures additional ingress routing rules, including authentication controls like `noauth` to disable authentication on specific routes.

## Additional Features

- `--enable_docker`: Permits Docker usage within containers
- `--wait`: Blocks until containers start
- `-o {json|plain}`: Controls output formatting

Arguments following `--` are passed directly to the container.

## Example Usage

```bash
# Run a simple container
nsc run --image ubuntu:latest

# Run and expose a port
nsc run --image nginx:latest -p 80:8080

# Run on existing instance
nsc run --on <instance-id> --image myapp:latest

# Run with custom duration
nsc run --image myapp:latest --duration 1h

# Pass arguments to container
nsc run --image ubuntu:latest -- bash -c "echo 'Hello World'"
```

## Related Commands

- `nsc create` - Creates a new instance
- `nsc build` - Builds container images
