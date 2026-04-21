<!-- Source: https://namespace.so/docs/solutions/docker-builders -->

# Speed up your Docker Builds with Namespace

Enterprise-grade Docker build infrastructure that delivers unmatched performance and scalability for development teams.

## Why Namespace Builders?

[Reliable, consistent performance on best-in-class AMD EPYC and Apple M4 CPUs](/docs/architecture/compute)

[Maximum incremental caching shared workspace-wide with sub-second lookups](/docs/architecture/storage/cache-volumes)

[Build API / SDK for programmatic access and advanced integrations](https://buf.build/namespace/cloud/docs/main:namespace.cloud.builder.v1beta)

[High build fan-out through automatic horizontal and vertical scaling](/docs/solutions/docker-builders#how-it-works)

[Cost optimized with transparent pricing and custom plans for larger customers](/docs/workspaces/billing-and-limits)

[Enterprise ready SAML SSO, SCIM, SLAs, audit logs, external log & metric sinks](/docs/workspaces/access)

## Getting Started

#### Initialize access to Namespace

Using the [CLI](/docs/reference/cli/installation), log into your workspace.
If you're accessing Namespace from a cloud provider or your CI platform, we recommend to set up [workflow federation](/docs/federation) instead.

```
$

```
nsc login
```
```

#### Configure your Docker

Connect your local Docker CLI to use Namespace Builders for any build invocation.

```
$

```
nsc docker buildx setup --background --use
```
```

The command above registers Namespace as a remote driver with your local Docker.

#### Done!

Your builds will now run on Namespace:

```
$ docker build . -t app:latest
```

## How it works

Remote Builders deliver exceptional performance through purpose-built infrastructure, dynamic scaling and vertical integration.
When you issue a build, Namespace selects the best hardware and location to execute your build and provisions a builder within seconds.

- **Dedicated compute instances** starting at 16+ vCPU / 32+ GB RAM
- **NVMe SSD storage** with high IOPS for fast layer operations and dependency downloads
- **Native build performance** AMD64 builds on high-performance AMD EPYC CPUs  
  ARM64 builds on AmpereOne or Apple M4 Pros
- **Persistent build environments** with pre-warmed base images and high-throughput cache access

## Next Steps

**[Build Observability →](/docs/solutions/docker-builders/tracing-and-logs)** Monitor build performance and identify bottlenecks through build layer tracing and critical path analysis.

**[Private Container Registry →](/docs/solutions/docker-builders/registry)** Speed up image pulls from testing workflows by pushing your images to [nscr.io](/docs/architecture/storage/container-registry) to unlock automatic global distribution.

## Enterprise Support

Need to run hundreds of concurrent builds, dedicated capacity, or specialized support?
Our [support team](mailto:support@namespace.so) can provide dedicated consultation for complex build pipelines.

Last updated September 17, 2025
