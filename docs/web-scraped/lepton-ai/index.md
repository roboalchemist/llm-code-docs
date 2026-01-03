# Lepton AI Documentation Index

## Overview
Lepton AI is a containerized inference deployment platform with autoscaling capabilities.

**Official Documentation:** https://docs.nvidia.com/dgx-cloud/lepton/
**GitHub Repository:** https://github.com/leptonai/leptonai

## Documentation Sections

### Getting Started
- **Introduction** - Overview of DGX Cloud Lepton
- **Endpoint** - Deploy and manage AI model endpoints
- **Dev Pod** - Lightweight AI development environments
- **Batch Job** - Run one-off tasks and jobs
- **Node Group** - Manage compute node groups
- **Workspace** - Workspace setup and management

### Features
- **Endpoint Configurations** - Configure endpoint settings, autoscaling, access control
- **Create LLM Endpoint** - Deploy Large Language Models
- **Create NIM Endpoint** - Deploy NVIDIA NIM endpoints
- **Dev Pod Configurations** - Configure development pod settings
- **Batch Job Configurations** - Configure batch job parameters
- **Workspace Members** - Manage workspace access and permissions
- **Workspace Tokens** - Authentication tokens
- **Workspace Secrets** - Secret management

### Compute
- **Bring Your Own Compute** - Use your own infrastructure with Lepton

### Reference
- **Python SDK Reference** - API documentation and examples

### Repository
- **GitHub README** - Project overview and getting started
- **CONTRIBUTING** - Contributing guidelines

## Key Concepts

### Endpoint
A running instance of an AI model that exposes an HTTP server. Accessible via REST APIs with support for:
- Autoscaling based on traffic (QPM) or GPU utilization
- Access control (IP allowlist, tokens)
- Health checks and monitoring

### Dev Pod
Lightweight, container-based AI development environments for building and testing applications.
- Full web terminal access
- SSH support
- JupyterLab integration
- Starter kits for common workflows

### Batch Job
One-off tasks like model training or data processing that run to completion.
- Simple configuration
- Status tracking
- Automatic archiving after completion

### Bring Your Own Compute (BYOC)
Integrate your existing hardware infrastructure with Lepton's management platform.

## Quick Links

- **Main Documentation:** https://docs.nvidia.com/dgx-cloud/lepton/
- **GitHub:** https://github.com/leptonai/leptonai
- **Examples:** https://github.com/leptonai/examples
