# nsc build

Construct container images through Namespace Remote Builders.

## Overview

The `nsc build` command creates and distributes container images. It accepts a PATH parameter representing the build context (the files involved in the build).

## Basic Usage

```bash
nsc build <PATH> [options]
```

## Key Capabilities

- Build and push container images
- Load images into your local Docker environment
- Build for multiple architectures simultaneously
- Pass environment variables during the build process

## Primary Options

| Option | Purpose |
|--------|---------|
| `-f <Dockerfile>` | Specify custom Dockerfile location |
| `-t <tag>` | Set image name/tag for any registry |
| `-n <name>` | Set image name/tag using your Workspace Registry |
| `--build-arg` | Provide build-time variables |
| `--platform` | Target specific OS/architecture combinations |
| `--push` | Upload results to registry |
| `--load` | Transfer single-platform builds to local Docker |
| `--secret` | Expose sensitive data during build |

## Example Usage

Build from the current directory and push to your Workspace Container Registry:

```bash
nsc build . --name app --push
```

Build with a custom Dockerfile:

```bash
nsc build . -f Dockerfile.prod --push
```

Build for multiple platforms:

```bash
nsc build . --platform linux/amd64,linux/arm64 --push
```

## Prerequisites

The command leverages your existing Docker credentials, so you must authenticate with `docker login` before pushing to external registries like GitHub Container Registry.

## Related Commands

- `nsc run` - Launch containers in ephemeral environments
- `nsc image build` - Build custom devbox images
