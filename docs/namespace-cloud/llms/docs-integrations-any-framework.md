<!-- Source: https://namespace.so/docs/integrations/any-framework -->

# Integrating any framework

Namespace maintains direct integrations with common developer tooling and frameworks.
But even when your tooling is not natively supported yet, you can configure your tooling to benefit from Namespace's caching solutions with a few simple steps.

## Using Cache Volumes

[Cache Volumes](/docs/architecture/storage/cache-volumes) offer unparalleled performance for your cache artifacts.
They are provisioned as a mount with full read/write access, allowing you to retain arbitrary files and directories in the cache.

### From GitHub Actions

To get started with Cache Volumes from [Namespace runners](/docs/solutions/github-actions) you need to enable caching in your [Runner Profile](https://cloud.namespace.so/workspace/actions/profiles) and add [`nscloud-cache-action`](/docs/reference/github-actions/nscloud-cache-action) to your workflow.

`nscloud-cache-action` has native caching support for many common
frameworks. In case your framework is not integrated yet, you can still cache arbitrary paths in
your GitHub Actions workflows, making it compatible with virtually any toolchain. To get started,
simply research the cache location of your framework and instruct Namespace to cache this path.

```
name: Build with Namespace Cache
on: [push, pull_request]
 
jobs:
  build:
    runs-on: namespace-profile-webbuilder
    steps:
      - uses: actions/checkout@v4
 
      - name: Setup Namespace Cache
        uses: namespacelabs/nscloud-cache-action@v1
        with:
          path: |
            ~/.npm
            ~/.cache/yarn
 
      - name: Install dependencies
        run: npm install
 
      - name: Build application
        run: npm run build
```

## Using Cache Mounts

[Namespace Docker Builders](/docs/solutions/docker-builders) offer high-performance cold builds, and come with maximum caching builtin - no additional setup required.

You can still optimize your build definition to also benefit from partial cache hits in case your build inputs change.
A common strategy to improve your build performance is the adoption of [build cache mounts](https://docs.docker.com/build/cache/optimize/#use-cache-mounts), allowing you to persist cache data across container builds and reduce build times significantly.

### Framework-Specific Examples

#### Python with pip

This example copies `requirements.txt` first, to ensure that code changes do not lead to a cache miss.
In case dependencies are added to `requirements.txt`, the usage of the cache mount ensures that the pip cache is retained across builds.

```
FROM python:3.11-slim
WORKDIR /app
 
# Install dependencies with cache
COPY requirements.txt .
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --no-deps -r requirements.txt
 
# Copy and build application
COPY . .
RUN --mount=type=cache,target=/app/.cache \
    python setup.py build
```

#### APT packages

You can retain the APT package cache in your Docker cache by mounting `/var/cache/apt` and `/var/lib/apt`.
Apt needs exclusive access to its data.
To achieve this, you can select `sharing=locked` which makes concurrent builds wait for another.

```
RUN --mount=type=cache,target=/var/cache/apt,sharing=locked \
    --mount=type=cache,target=/var/lib/apt,sharing=locked \
    apt update && apt-get --no-install-recommends install -y gcc
```

#### Go Applications

For Go applications, it is recommended to copy `go.mod` and `go.sum` first, to ensure that code changes do not lead to a cache miss.
In case dependencies are added, the usage of the cache mount ensures that the go module cache is kept.

```
FROM golang:1.21-alpine
WORKDIR /app
 
# Copy go mod files
COPY go.mod go.sum ./
 
# Download dependencies with cache
RUN --mount=type=cache,target=/go/pkg/mod \
    --mount=type=cache,target=/root/.cache/go-build \
    go mod download
 
# Build application
COPY . .
RUN --mount=type=cache,target=/go/pkg/mod \
    --mount=type=cache,target=/root/.cache/go-build \
    go build -o main .
```

## Using the HTTP Cache API

If your build tool supports HTTP-based remote caching, you can integrate it with Namespace's managed build cache using the [HTTP Cache API](https://buf.build/namespace/cloud/docs/main:namespace.cloud.integrations.httpcache.v1beta).

The `EnsureHttpCache` RPC provisions a cache and returns a WebDAV endpoint URL with short-lived credentials (username/password):

```
$ grpcurl -H "Authorization: Bearer $NSC_TOKEN" \
    global.namespaceapis.com:443 \
    namespace.cloud.integrations.httpcache.v1beta.HttpCacheService/EnsureHttpCache \
    -d '{"name": "my-cache"}'
```

```
{
	"cacheEndpointUrl": "https://httpcache.ord.namespaceapis.com/my-cache",
	"username": "token",
	"password": "nsc_...",
	"expiresAt": "2026-03-05T17:00:00Z",
	"site": "ord"
}
```

The returned endpoint supports standard HTTP methods — you can store and retrieve cache artifacts using `PUT` and `GET` with basic auth:

```
# Store an artifact
$ curl -u "token:$CACHE_PASSWORD" \
    -X PUT --upload-file build-output.tar.gz \
    "https://httpcache.ord.namespaceapis.com/my-cache/my-key"
 
# Retrieve an artifact
$ curl -u "token:$CACHE_PASSWORD" \
    -o build-output.tar.gz \
    "https://httpcache.ord.namespaceapis.com/my-cache/my-key"
```

This approach works with any tool that supports HTTP PUT/GET for caching, such as [sccache](/docs/integrations/sccache) (WebDAV) or custom build scripts.

## What's next?

The Namespace team provides expert consultation to help you optimize your cache strategy and achieve maximum performance benefits.
Reach out to [support@namespace.so](mailto:support@namespace.so) to talk to one of our engineers and learn about best practices and upcoming integrations.

Last updated March 5, 2026
