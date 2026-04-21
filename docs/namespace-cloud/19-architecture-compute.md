# Architecture - Compute Platform Overview

Namespace is a compute infrastructure provider offering cross-platform development environments with high-performance hardware.

## Core Offerings

The platform provides access to high-performance hardware across three operating systems:

- **Linux**: AMD64 and ARM64 architectures on AMD EPYC processors
- **macOS**: Apple M2 Pro or M4 Pro chips for native development
- **Windows**: AMD EPYC-based instances

## Key Features

Namespace emphasizes fast, reliable, and secure compute infrastructure designed for modern development needs. Notable capabilities include:

- Fast-booting isolated instances for rapid iteration
- GitHub Actions runner integration
- Docker remote builders
- SSH and VNC remote access
- Kubernetes support
- Container registry and artifact storage
- Comprehensive observability and monitoring

## Getting Started Options

The platform supports multiple integration paths:

- GitHub Actions workflows
- Docker build environments
- Custom API and SDK implementations

## Infrastructure Advantage

Namespace operates their own hardware to their own racks and manages their own networking, which enables higher consistency and better pricing than alternatives.

## Support and Services

The service includes:

- Dashboard tools for monitoring builds, usage, and registry management
- Extensive CLI tooling for local development workflows
- Enterprise features for larger organizations

## Available Operating Systems

- **Linux**: Most common for development
- **macOS**: For iOS/macOS native development
- **Windows**: For Windows-specific workloads

See the related architecture documentation for specific details on machine shapes, resource limits, SSH/remote access, and networking.
