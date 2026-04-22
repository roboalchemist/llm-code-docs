<!-- Source: https://namespace.so/docs/integrations/docker-images -->

# Docker Images

Whether you are building, pushing or pulling Docker images - Namespace employs comprehensive optimizations to accelerate your work.

## Faster Docker image builds

Building Docker images can be one of the most time-consuming parts of your CI/CD pipeline.
[Namespace Docker Builders](/docs/solutions/docker-builders) offer high-performance cold builds, and come with maximum caching builtin - no additional setup required.

### From Namespace Runners

If your GitHub Actions [run on Namespace](/docs/solutions/github-actions), Remote Builders are [enabled by default](/docs/solutions/github-actions/docker-builds) and will immediately accelerate your builds.

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

### From anywhere

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
$

```
docker build . -t app:latest
```
```

## Caching image pulls

Container Image caching allows you to dramatically reduce container startup times.
When enabling this feature, both image layers and the often expensive unpacking are cached locally.
Container image caching is available for any compute instance running on Namespace.

### From GitHub Actions

When running your GitHub Actions on [Namespace runners](solutions/github-actions), cached image pulls are available directly from the UI.

#### Faster pulls with one click

To enable container image caching, simply check the corresponding option in your [runner profile configuration](https://cloud.namespace.so/workspace/actions/profiles).

![profile container image caching](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Frunnerprofilecontainerimages.8aef9878.png&w=1200&q=75)

That's it!
Repeated pulls of the same image will now complete in seconds rather than minutes.

### In-Network Registry Caching

Namespace maintains a transparent, in-network cache for public container registries, significantly improving pull performance for commonly used images.
Popular base images and frequently accessed containers are pre-cached within our network infrastructure, reducing pull times and eliminating redundant downloads across the internet.
This cache is automatically updated and managed to ensure you always receive the latest versions when needed.

## Private Image Registry

Private images using the [Namespace Container Registry](/docs/architecture/storage/container-registry) (nscr.io) are automatically distributed and cached throughout Namespace's network infrastructure reducing image pulls latency.

Using the [CLI](/docs/reference/cli/installation), you can configure access to nscr.io.

#### Configure your Docker

```
$

```
nsc docker login
```
```

The command above will update your local Docker configuration and print your container registry address (e.g. `nscr.io/8enum0hp1l5ii`).
If you want to obtain the address without updating your Docker configuration, run [`nsc workspace describe`](/docs/reference/cli/workspace-describe).

#### Build and push

```
$

```
docker build . -t nscr.io/8enum0hp1l5ii/app:latest --push
```
```

Last updated September 17, 2025
