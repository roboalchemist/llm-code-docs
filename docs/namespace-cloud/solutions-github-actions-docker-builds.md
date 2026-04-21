<!-- Source: https://namespace.so/docs/solutions/github-actions/docker-builds -->

# Optimizing Docker Build Performance

Building Docker images can be one of the most time-consuming parts of your CI/CD pipeline.
Namespace runners are designed to dramatically accelerate your Docker builds through intelligent build distribution, advanced caching, and seamless integration with your existing workflows.

## Quick Start: Instant Performance Gains

*No configuration changes required*

The fastest way to speed up your Docker builds is to simply switch to Namespace runners.
Remote Builders are enabled by default and will immediately accelerate your builds.

```
jobs:
  build:
    runs-on: namespace-profile-default # was: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        # No docker/setup-buildx-action or docker/setup-qemu-action required!
      - name: Build and push
        uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          tags: my-registry/my-app:latest
```

**Note**: If your workflow uses `docker/setup-buildx-action`, you need to [remove or replace](/docs/solutions/github-actions/docker-builds#skip-setup-buildx) it.

That's it! Your builds are now running on high-performance Remote Builders with advanced caching.

## Understanding Remote Builders: Your Build Acceleration Engine

### How Remote Builders Transform Your Workflow

[Remote Builders](/docs/solutions/docker-builders) fundamentally change how Docker builds work in your CI/CD pipeline:

- **Scale independently**: Massive parallel compute power regardless of your runner size
- **Cost optimization**: Use smaller, cheaper runners while getting maximum build performance
- **Zero configuration**: Every Docker command automatically benefits from remote acceleration
- **Universal compatibility**: Works with `docker build`, `docker/build-push-action`, and any Docker-based tooling

### Monitoring Your Accelerated Builds

Every build launched from your runners appears in the interface providing direct access to detailed logs, timing metrics, and performance analytics.

![Container Builds](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fcontainer-builds.7d9275bb.png&w=640&q=75)![Build Tracing](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fbuildtrace.c35385df.png&w=828&q=75)

This visibility helps you understand exactly how much time Remote Builders are saving.
When looking at a slow build step, you can directly jump into the logs to understand which work was performed.

![build layer performance tracing](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Ftracing.b7ce532c.png&w=1200&q=75)

Head to [Build Observability →](/docs/solutions/docker-builders/tracing-and-logs) to learn how to monitor build performance and identify bottlenecks.

## Seamless Private Registry Integration

Your builds get instant access to your private container registry at [nscr.io](/docs/architecture/storage/container-registry) with zero setup required.
Authentication is handled automatically.

#### Push to your private registry

```
- name: Build and push to private registry
  uses: docker/build-push-action@v5
  with:
    context: .
    push: true
    tags: ${{ env.NSC_CONTAINER_REGISTRY }}/my-app:${{ github.sha }}
```

#### Pull from your private registry

```
- name: Use base image from private registry
  run: docker pull ${{ env.NSC_CONTAINER_REGISTRY }}/my-app:${{ github.sha }}
```

You can find a tag overview with history and usage statistics for pushed images in the [dashboard](https://cloud.namespace.so/workspace/registry).

![container image registry](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fregistry.d437e4a0.png&w=1200&q=75)

## When to Choose Local Caching

While Remote Builders provide the best performance for most scenarios, in-runner builders (locally cached) excel when building massive images (10GB+).
Keeping the build local skips network transfer time.

With runner profilesWith runner labels

To enable this feature, just open the [runner profile](https://cloud.namespace.so/workspace/actions/profiles) configuration and add a cache volume. Next, select `Locally cached` for your Docker builds.

![locally cached Docker build configuration](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fin-runner-builder.7d07d80c.png&w=1080&q=75)

#### Caveats

- Build caching using "local caching" is not shared with Remote Builders; each
  repository uses its own separate cache.
- Although multi-platform builds are supported, only builds of the same platform
  as the runner itself, will experience native performance.

#### Billing

Using local caching does not lead to any additional compute usage beyond
the runner's execution time itself. In order to make use of the feature,
including logging and tracing, each build made with local caching
counts towards the total build usage.

## Enterprise Build Scaling

Need to run hundreds of concurrent builds? Namespace supports full-fanout builds that can handle enterprise-scale build volumes without performance degradation.

- **Automatic scaling**: Remote Builders support automatic scale-out to match your build volume
- **No queue bottlenecks**: Parallel processing ensures builds start immediately
- **Dedicated compute**: With dedicated Namespace compute, you get a fully consistent build performance experience

Contact [support@namespace.so](mailto:support@namespace.so) to discuss custom scaling configurations for your build volume requirements.

## Migrating from GitHub Actions

### Remove setup-buildx-action

Because Namespace runners are configured out of the box to use Remote Builders, there is no need to set up or configure buildx separately.
In fact, running `docker/setup-buildx-action` will overwrite the default configuration and prevent you from using Remote Builders.

You can just remove `docker/setup-buildx-action` from your workflow entirely,  
or replace it with `namespacelabs/nscloud-setup-buildx-action`:

```
- name: Set up Docker Buildx

-   

uses: docker/setup-buildx-action@v3

+   

uses: namespacelabs/nscloud-setup-buildx-action@v0

- uses: docker/build-push-action@v5

with:

context: .
```

### QEMU is not required

Multi-platform builds using Remote Builders don't use emulation for AMD64 and ARM64 builds, instead building on these platforms natively.
This results in much better performance for multi-platform builds, and also means there is no need to set up QEMU.

When using Remote Builders, you can safely remove `docker/setup-qemu-action`, too:

```
steps:

- uses: docker/setup-qemu-action@v3

- uses: docker/setup-buildx-action@v3

- uses: docker/build-push-action@v5

with:

context: .
```

### Skip GitHub Actions Caching

Traditional CI/CD requires complex caching strategies, but Namespace's build infrastructure makes this unnecessary.
Namespace build solutions include maximum layer caching out of the box.
Using traditional GitHub actions caching like `cache-from`/`cache-to`
is superfluous when using Namespace builders and typically adds delays through remote file operations.

You can remove them from your workflow definition:

```
- uses: docker/build-push-action@v5

with:

context: .

cache-from: type=registry,ref=user/app:buildcache

cache-to: type=registry,ref=user/app:buildcache,mode=max
```

#### What This Means for You

- **No cache configuration**: Remove complex caching logic from your workflows
- **Faster cold starts**: Even first builds benefit from shared layer caches
- **Consistent performance**: Cache hit rates are optimized automatically

### Optimize cache mounts

A common strategy to improve your build performance is the adoption of [build cache mounts](https://docs.docker.com/build/cache/optimize/#use-cache-mounts), allowing you to persist cache data across container builds and reduce build times significantly.

With Namespace, your builds run in a shared, remote, high-performance builder by default - unlike on GitHub runners, where your docker builds run inside the runner.
This sharing means that you’ll see more cache hits across different builds, and hence faster builds.

Cache mounts allow multi-writer access by default.
Some tools (e.g. apt) need exclusive access to its data.
To achieve this, you can select `sharing=locked` which makes concurrent builds wait for another.

```
RUN --mount=type=cache,target=/var/cache/apt,sharing=locked \
    --mount=type=cache,target=/var/lib/apt,sharing=locked \
    apt update && apt-get --no-install-recommends install -y gcc
```

Last updated August 18, 2025
