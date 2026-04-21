<!-- Source: https://namespace.so/docs/architecture/compute/linux -->

# Linux

Run Linux on your choice of modern CPU architecture.
Namespace supports both AMD64 and ARM64 workloads on high-end processors, with shape options tuned for CI, container builds, and parallel compute.

## AMD64 Architecture

Our AMD64 instances use high-performance AMD EPYC CPUs optimized for compute-intensive workloads, including:

- CI/CD pipelines with intensive build processes
- Large-scale compilation workflows
- End-to-end browser testing

## ARM64 Architecture

Native ARM64 support is powered by AmpereOne processors. Apple M4 Pro support for Linux workloads is available as an early access.
This architecture excels at:

- Natively building and running ARM applications and containers
- Heavily multithreaded compute operations

## High-memory instances

For workloads requiring exceptional memory capacity like data processing and analytics pipelines, Namespace offers extended memory configurations:

- **80 GB, 96 GB, 112 GB, 128 GB** - Extended memory options
- **256 GB, 384 GB, 512 GB** - High-memory instances for specialized workloads

**Note:** High-memory instances (over 64 GB) require special access and may not be available on all subscription plans. Contact [support@namespace.so](mailto:support@namespace.so) to request access to high-memory configurations.

Last updated August 25, 2025
