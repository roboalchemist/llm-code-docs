<!-- Source: https://namespace.so/docs/architecture/networking/performance -->

# Network Performance Optimizations

Beyond selecting [best-in-class compute](/docs/architecture/compute) only, Namespace provides advanced network performance optimizations designed to deliver superior speed, reliability, and efficiency for your development workloads.
This page explains the key networking features that ensure optimal performance across DNS resolution, container registry operations, and network connectivity.

## DNS Resolution

Namespace implements intelligent DNS management to ensure fast and reliable name resolution for all your workloads.

### DNS Performance and Reliability

Namespace maintains high-performance DNS caches across our infrastructure to minimize resolution latency.
Frequently accessed domain names are cached at multiple layers, reducing the time required for DNS lookups and improving overall application performance.
This caching system automatically manages cache invalidation to ensure accuracy while maximizing performance benefits.

DNS resolution in Namespace is designed to survive unreliable external nameservers.
Our DNS infrastructure includes multiple fallback mechanisms and intelligent retry logic, ensuring that temporary outages or performance issues with external DNS providers don't impact your workloads.
If primary nameservers become unavailable, the system automatically routes requests through alternative pathways to maintain consistent resolution capabilities.

### Custom DNS Configuration

Namespace supports injection of custom DNS resolution configurations on a per-tenant basis.
This allows organizations to configure specific DNS settings, custom nameservers, or internal domain resolution rules that are automatically applied to their workloads.
Custom configurations can include private domain mappings, specific upstream resolvers, or specialized DNS policies required for your organization's infrastructure.

## Container Registry Performance

Namespace optimizes container image operations through intelligent caching and distribution mechanisms.

### In-Network Public Registry Cache

Namespace maintains a transparent, in-network cache for public container registries, significantly improving pull performance for commonly used images.
Popular base images and frequently accessed containers are pre-cached within our network infrastructure, reducing pull times and eliminating redundant downloads across the internet.
This cache is automatically updated and managed to ensure you always receive the latest versions when needed.

### Private Image Distribution

Private images using the [Namespace Container Registry](/docs/architecture/storage/container-registry) (nscr.io) are automatically distributed and cached throughout Namespace's network infrastructure.
When you push images to nscr.io, they are intelligently replicated across multiple network locations to ensure fast access regardless of where your workloads are running.
This distributed caching system reduces latency for private image pulls and improves overall deployment performance.

## Network Traffic Management

Namespace provides sophisticated traffic management capabilities to ensure your workloads observe consistent and reliable network performance.
In particular, our traffic shaping mechanisms prevent any single workload from consuming excessive bandwidth and impacting others.
This increases consistency and ensures predictable behavior for network-intensive applications.

## Optimized Network Routing

Namespace maintains strategic network partnerships and infrastructure investments to provide optimal routing for external services.
These dedicated connections bypass traditional internet routing, providing lower latency, higher reliability, and improved performance when accessing partner services.
Direct peering eliminates many of the potential bottlenecks and routing inefficiencies that can occur with standard internet connectivity.

Through our partnership with Docker Hub, Namespace customers experience no rate limits when pulling from Docker Hub (only standard abuse prevention limits apply).

## Support and Configuration

Network performance optimizations are automatically enabled for all Namespace workspaces.
For questions about network performance or to discuss custom networking requirements for enterprise deployments, contact our [support team](mailto:support@namespace.so).

Our team can provide detailed performance metrics, assist with custom DNS configurations, and help optimize network settings for your specific use cases.

Last updated September 22, 2025
