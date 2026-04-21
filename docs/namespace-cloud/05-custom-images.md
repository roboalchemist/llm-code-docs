# Custom Base Images for Devboxes

This documentation explains how to create and manage custom base images for Namespace Devboxes using Dockerfiles.

## Purpose

Pre-package development tools, runtimes, and dependencies into custom base images so devboxes start with everything pre-installed.

## Dockerfile Approach

Create a standard Dockerfile with Ubuntu 24.04 as the base:

```dockerfile
FROM ubuntu:24.04

# Install development tools
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    curl \
    wget \
    vim \
    && rm -rf /var/lib/apt/lists/*

# Create non-root user
RUN useradd -m -s /bin/bash devuser

# Install team-specific tools (example: Go)
RUN curl -fsSL https://golang.org/dl/go1.21.linux-amd64.tar.gz | tar -C /usr/local -xz

USER devuser
WORKDIR /home/devuser
```

## Building Images

Build and publish images to your workspace:

```bash
devbox image build ./my-image --name=my-team/golang
```

For Dockerfiles in different locations (monorepo structures):

```bash
devbox image build . -f path/to/Dockerfile --name=my-team/golang
```

## Optimization

After building, Namespace automatically converts images into an optimized disk format, enabling fast boot times measured in seconds rather than minutes.

## Creating Devboxes from Custom Images

### Via CLI

```bash
devbox create --image=my-team/golang
```

### Via Dashboard

Select the custom image when creating a new devbox.

## Image Management

### List images

```bash
devbox image list
```

### Update images

Rebuild with the same name to update an existing image.

### Expire images

Prevent new devbox creation while preserving existing ones:

```bash
devbox image expire my-team/golang
```

## Important Notes

Custom images are optional—most teams can use Namespace's managed base images instead. Only create custom images when you need team-specific tools or dependencies.
