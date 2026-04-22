<!-- Source: https://namespace.so/docs/solutions/docker-builders/registry -->

# Container Registry

Your builds get direct access to your private container registry at [nscr.io](/docs/architecture/storage/container-registry).
This seamless integration eliminates the complexity of registry authentication while providing enterprise-grade performance and global availability.

## From Namespace instances

*No configuration changes required*

When running your CI on Namespace, access to nscr.io is already configured.
Each Namespace workload embeds short-lived credentials that grant direct access to the container registry.

```
$

```
docker pull nscr.io/<workspace-id>/app:latest
```
```

Your workspace identifier can be found in the [Dashboard](https://cloud.namespace.so/workspace/settings).

## Local Docker integration

Using the [CLI](/docs/reference/cli/installation), you can also configure your local Docker to access nscr.io.

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

## Observability

Our [Dashboard](https://cloud.namespace.so/workspace/registry) provides a holistic overview over the images that you have pushed to nscr.io.
You can understand access patterns per tag, and the evolution of image sizes over time.

![container image registry](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fregistry.42be4003.png&w=1200&q=75)

When looking at a single image tag, you can see the historic versions, and which are still being pulled today.
For multi-platform images, you can also understand how much each platform contributes to the combined image size.

![multi arch image](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fregistry-multi-arch.af3b8948.png&w=1200&q=75)

## Build and Push in One Command

When doing quick image iterations, our [CLI](/docs/reference/cli/installation) offers a [simple command](/docs/reference/cli/build) to build and push an image without reconfiguring your local Docker client.

#### Build and push

```
$

```
nsc build . --name app --push
```
```

That's it! With a single command, you've built an image using a high-performance, remote builder and pushed it to nscr.io.

## Access Controls

Images pushed to nscr.io are shared with your workspace by default, allowing for frictionless collaboration.

[More information on Workspace access](/docs/workspaces/access)

### Public Access

In order to share an image publicly, the following command can be used:

```
$

```
nsc registry share <image-reference>
```
```

The image is then available publicly at `public.nscr.io/<id>:latest`. Alternatively, one can provide a custom suffix:

```
$

```
nsc registry share <image-reference> --suffix <suffix>
```
```

which makes the image available publicly at `public.nscr.io/<id>/test:latest`.

## Expiration

By default, images pushed to the Namespace container registry do not expire and are kept indefinitely.

### Single image expiration

Single images can be set to expire at a certain point in time. Once the image expires, it will no longer be served and does not consume any storage.

```
$

```
nsc registry update-image-expiration <image-reference> --expire-at <timestamp>
```
```

For instance, to expire the image `nscr.io/8enum0hp1l5ii/nginx@sha256:b493d48364afe44d11c0165cf470a4164d1e2609911ef998be868d46ade3de4e` on the 24th of December of 2024 the command would look like this:

```
$

```
nsc registry update-image-expiration nginx@sha256:b493d48364afe44d11c0165cf470a4164d1e2609911ef998be868d46ade3de4e --expire-at 2024-12-24T00:00:00Z
```
```

To ensure a minimum lifetime of an image use the `ensure-minimum` flag.

```
$

```
nsc registry update-image-expiration <image-reference> --ensure-minimum <duration>
```
```

For programmatic access to the image expiration API check out our [public container registry API](https://buf.build/namespace/cloud/docs/main:namespace.cloud.registry.v1beta).

### Default image expiration

The default expiration policy for newly created images can be adjusted as follows:

```
$

```
nsc registry policy set --default_expiration <duration>
```
```

To query the current default expiration use:

```
$

```
nsc registry policy get
```
```

### Repository-specific expiration

You can also set an expiration policy for a specific repository, overriding the default:

```
$

```
nsc registry policy set --repository <repository> --default_expiration <duration>
```
```

To query the current policy for a specific repository:

```
$

```
nsc registry policy get --repository <repository>
```
```

To expire container images retroactively [reach out to our customer support](mailto:support@namespace.so).
For programmatic access to the image expiration API check out our [public container registry API](https://buf.build/namespace/cloud/docs/main:namespace.cloud.registry.v1beta).

Last updated March 16, 2026
