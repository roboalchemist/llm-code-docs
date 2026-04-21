<!-- Source: https://namespace.so/docs/reference/github-actions/nscloud-setup-buildx-action -->

# namespacelabs/nscloud-setup-buildx-action

namespacelabs/nscloud-setup-buildx-action@v0

[namespacelabs/nscloud-setup-buildx-action](https://github.com/namespacelabs/nscloud-setup-buildx-action)
is a GitHub action that configures [Docker buildx](https://docs.docker.com/engine/reference/commandline/buildx/)
to use [Namespace Remote Builders](/docs/solutions/docker-builders).

## Prerequisites

In order to use `nscloud-setup-buildx-action`, you need to have access to Namespace.
The easiest way to ensure access is to run [namespacelabs/nscloud-setup](/docs/reference/github-actions/nscloud-setup) beforehand.

## Example

```
jobs:
  docker:
    runs-on: ubuntu-latest
    # These permissions are needed to interact with GitHub's OIDC Token endpoint.
    permissions:
      id-token: write
      contents: read
    steps:
      - uses: actions/checkout@v4
      - uses: namespacelabs/nscloud-setup@v0
      - name: Configure Docker to use Namespace Remote Builders
        uses: namespacelabs/nscloud-setup-buildx-action@v0
      - name: Build and push
        uses: docker/build-push-action@v5
        with:
          push: true
          tags: user/app:latest
```

## Options

### builder-name

*`string`* The name of the local Docker build driver to be configured.

Optional.

### load-to-docker

*`boolean`* Whether to load images to the local Docker engine.

Optional. Default is `true`.

### wait-for-builder

*`boolean`* If `true`, creates the build clusters eagerly and waits for them to be available.

Optional. Default is `false`.

### tag

*`string`* If set, select a named builder. Contact [support@namespace.so](mailto:support@namespace.so) to get access.

Optional.

## Outputs

`nscloud-setup-buildx-action` has no outputs.

Last updated February 13, 2026
