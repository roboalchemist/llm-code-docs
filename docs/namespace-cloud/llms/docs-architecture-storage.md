<!-- Source: https://namespace.so/docs/architecture/storage -->

# Storage

Namespace provides a variety of storage solutions that allow your instances to securely store and access required data.
All storage solutions maximize data proximity to avoid network transfers and ensure high throughput.

## Cache Volumes

[Cache Volumes](/docs/architecture/storage/cache-volumes) are local, NVME-backed storage that allows you to reuse cache artifacts from one instance in another.
They offer very high read/write performance, require no remote file transfers and work well in high fanout scenarios.

## Persistent Volumes

[Persistent Volumes](/docs/architecture/storage/persistent-volumes) provide durable block storage that is guaranteed to persist across instance lifetimes.
Data is automatically snapshotted on shutdown, and new volumes can be initialized from a specific snapshot.

## Container Registry

[nscr.io](/docs/architecture/storage/container-registry) is a fully managed container registry built atop the same technology as our high-performance [artifact storage](/docs/architecture/storage/artifact-storage).
It seamlessly integrates with Namespace products and requires zero configuration to start using it.

## Artifact Storage

Namespace maintains high-performance [artifact storage](/docs/architecture/storage/artifact-storage), ideal for workflow artifacts.
It is globally distributed, with transparent local caching.
Artifact storage offers highly-available, high throughput object storage that is seamlessly integrated with the rest of Namespace.
It is the backing technology behind our [Bazel cache](/docs/integrations/bazel) and [Turborepo](/docs/integrations/turborepo) integration.

## Secrets

You can store sensitive configuration data in your workspace by writing them to Namespace [Secrets](/docs/architecture/storage/secrets).
When creating an instance, you can inject secrets directly into the environment.

Last updated March 20, 2026
