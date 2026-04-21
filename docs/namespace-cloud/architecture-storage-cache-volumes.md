<!-- Source: https://namespace.so/docs/architecture/storage/cache-volumes -->

# Cache Volumes

Namespace Cache Volumes provide high-performance storage that can be attached to compute instances to accelerate your development workflows.
Built on local NVMe storage, Cache Volumes are designed to handle the demanding I/O requirements of modern CI/CD pipelines and development environments.

[Learn how to use Cache Volumes](/docs/solutions/github-actions/caching)

## Multi-Writer Safety

Cache Volumes can safely be accessed concurrently, allowing multiple runners to read and write cache data simultaneously.
When you request a Cache Volume, Namespace creates a fork of the most recent cache version.
Each compute instance receives its own private copy of the Cache Volume as it existed at the time of the last successful cache commit.

## Lifecycle Management

Cache Volumes follow a "last write wins" model for version management:

- **First Request**: Creates an empty cache volume as the initial version
- **Subsequent Requests**: New instances receive forks of the most recent committed version
- **Successful Completion**: When an instance terminates cleanly (exit code 0), its cache state becomes the new parent version
- **Failed Instances**: Cache changes from failed instances are automatically discarded

There may be multiple versions of a Cache Volume alive at the same time.

## Naming and Access Control

Cache Volumes are identified by unique tags that govern access across your workspace.
Any compute instance can request access to a Cache Volume by specifying its tag, making it easy to share cached data across different workflows and jobs.
Each tag maintains a versioned history of cache states, with Namespace automatically selecting the most appropriate version for new instances.

## Sizing and Storage Management

### Dynamic Sizing

When requesting a Cache Volume, you specify a minimum space requirement.
Namespace ensures your instance always has at least that amount of available space, but the actual volume size grows dynamically based on cached content.

- **Configuration**: 50GB Cache Volume
- **First instance**: Starts with 50GB free space (0GB used)
- **After storing 10GB**: Volume contains 10GB used, 40GB free
- **Second instance**: Receives 60GB volume (10GB used from cache, 50GB free as requested)

### Cache Reset Scenario

Cache Volumes provide the cache size you ask for.
Your Cache Volumes keep growing as the amount of cached data increases.
Once the content exceeds the cache size, that volume will not be used - leading to a cache miss:

- **Configuration**: 50GB Cache Volume
- **Existing cache**: 20GB of content
- **First instance**: receives a 70GB volume (20GB used + 50GB free)
- **After storing 31GB**: Volume contains 51GB used, 19GB free
- **Second instance**: Receives an empty 50GB volume (cache miss - cache contents exceeded the configured limit)

### Cache Hits and Misses

Namespace consistently provisions Cache Volumes with close to zero impact on startup latency.
To achieve this, there may be rare scenarios of cache misses, to avoid delaying the startup.
Namespace prefers the latest version over older versions.
If this fails, stale cache versions are preferred over cache misses.

Applications using Cache Volumes should not assume that the cache contents match exactly the last committed version.

### Garbage Collection

Namespace employs intelligent garbage collection strategies to maintain optimal cache performance and prevent uncontrolled growth that could lead to cache misses.
Current garbage collection policies:

- Docker Image caching
- Local build caching
- Bazel caching

For specialized garbage collection requirements, contact our [support team](mailto:support@namespace.so).

## Usage

Namespace accounts Cache Volume usage in two categories:

- Cache storage
- Cache snapshot usage

Any cache volume tag consumes storage usage proportional to the requested size of the volume.
In case of a cache hit, Namespace accounts the snapshot usage of the cache as the lifetime of the attached instance times the size of the cache volume.
This gives a measurement in GB-hours. For example, if an instance runs for one hour with a 100 GB cache volume attached, the billable metric will be 100 GB-hours.
If an instance runs for 3 hours with a 50 GB cache volume attached, the metric would be 150 GB-hours. You can analyze your cache volume usage in the [dashboard](https://cloud.namespace.so/workspace/usage?focus=storage).

To limit the storage cost associated with cache volumes, Namespace automatically expires unused caches after 14 days.
This limit is configurable.
To evict a cache ahead of its expiration, you can release it from the [dashboard](https://cloud.namespace.so/workspace/storage).

### Example for GitHub runners

- **Configuration**: [runner profile](/docs/solutions/github-actions#configure-your-runners) with 50GB cache
- **First run**: cache storage accounting begins, adds 50GB-days per day.
- **Second run**: cache hit, runs for 10 minutes -> accounts for 500 GB-minutes.
- **Third run**: cache miss -> does not count towards cache usage.
- **Another repository**: If the same profile is used for a different repository, the cache is separate and usage is accounted separately.

## API Access

Cache volumes can be managed programmatically via the
[StorageService API](https://buf.build/namespace/cloud/docs/main:namespace.cloud.compute.v1beta),
which provides RPCs for listing volumes and tag summaries, and destroying cache volume tags.

Last updated March 20, 2026
