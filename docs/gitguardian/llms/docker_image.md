# Source: https://docs.gitguardian.com/ggshield-docs/integrations/docker/docker_image.md

# Docker images

> `ggshield` docker scanning tool (`ggshield secret scan docker`) is used to
scan local docker images for secrets present in the image's creation process
(`dockerfile` and build arguments) and in the image's layers' filesystem.

## Prelude

`ggshield` docker scanning tool (`ggshield secret scan docker`) is used to
scan local docker images for secrets present in the image's creation process
(`dockerfile` and build arguments) and in the image's layers' filesystem.

`ggshield` is a wrapper around GitGuardian API for secrets detection that requires an API key to work.

If the image is not available locally on the user's machine, GitGuardian CLI
will attempt to pull the image using `docker pull <IMAGE_NAME>`.

## Preview

![docker preview](/img/internal-monitoring/integrate-sources/vcs-integrations/docker/docker-secret-scan-output.png)

## Usage

- `Docker`: scan a Docker image after exporting its filesystem and manifest with the `docker save` command.

  ```
  Usage: ggshield secret scan docker [OPTIONS] IMAGE_NAME

    ggshield will try to pull the image if it's not available locally
  Options:
    -h, --help  Show this message and exit.
  ```

Example: `ggshield secret scan docker gitguardian/ggshield`

## Example integration (GitHub Actions)

In this example integration we build and push the ggshield image on GitHub Actions and then
scan this image.

```yml
name: ci

on:
  push:
    branches:
      - 'master'

jobs:
  docker:
    runs-on: ubuntu-latest
    services:
      registry:
        image: registry:2
        ports:
          - 5000:5000

    container: gitguardian/ggshield:latest
    steps:
      - name: Checkout
        uses: actions/checkout@v2
      - name: Set up QEMU
        uses: docker/setup-qemu-action@v1
      - name: Set up Docker Buildx
        uses: docker/setup-buildx-action@v1
        with:
          driver-opts: network=host
      - name: Build and push to local registry
        uses: docker/build-push-action@v2
        with:
          context: .
          push: true
          tags: localhost:5000/gitguardian/ggshield:latest
      - name: Scan image
        run: |
          ggshield secret scan docker localhost:5000/gitguardian/ggshield:latest
```
