<!-- Source: https://namespace.so/docs/integrations/bazel -->

# Bazel integration

Bazel is a popular build system optimized for polyglot, large monorepos.

Namespace provides high-performance [Bazel](https://bazel.build) caching with
very low network latency between runners and the cache storage. This allows your
Bazel workflows to reuse build artifacts across runs, irrespective of your
chosen granularity, significantly reducing build times.

Bazel caching is particularly effective for:

- Build steps that are time-consuming to execute but produce relatively small outputs
- Projects where compilation is typically slow, such as Rust and C++ codebases
- Workflows that can benefit from cross-invocation artifact reuse

Since the cache is shared, local builds can also benefit from artifacts already cached by CI — and vice versa.

## Getting started

Bazel caching is a paid add-on. In order to enable it for your workspace contact [our sales team](mailto:sales@namespace.so).
You can produce a ready-to-use configuration using the [CLI](/docs/reference/cli/installation):

#### Configure cache access

```
$

```
nsc cache bazel setup --bazelrc /etc/bazel.bazelrc
```
```

This command generates short-term credentials, and sets up a `bazelrc` configuration file.

#### Use the Bazel cache

```
$

```
bazel --bazelrc=/etc/bazel.bazelrc test //..
```
```

You can pass multiple configuration files by setting `--bazelrc` repeatedly, allowing you to combine your existing configuration with Namespace cache access.
See [Bazel's documentation](https://bazel.build/run/bazelrc) for granularity control options.

### GitHub Actions Example

#### Configure cache access

When using Namespace runners, you can enable Bazel caching directly in your [profile configuration](https://cloud.namespace.so/workspace/actions/profiles).

![bazel cache dialog](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fbazel-caching.d7d0b0db.png&w=1200&q=75)

#### Use the Bazel cache

In your workflow, you only need to select the corresponding profile. Bazel is already configured to use the Namespace cache.

```
jobs:
  build:
    runs-on: namespace-profile-with-bazel
  steps:
    - name: Bazel test
      run: bazel test //..
```

## How it works

The Bazel caching solution employs a tiered caching approach, where the hot cache lives as close to the consumer (e.g. your CI job runner) as possible.
The cold caching tier is backed by our [high-performance artifact storage](/docs/architecture/storage/artifact-storage) and enables Bazel to retain a vast amount of cached artifacts.

Access to the Bazel cache is granted through short-lived secure credentials.

## Usage

Namespace accounts Bazel cache usage in two categories:

- Bazel cache storage
- Bazel cache reads

For detailed billing information for each item as well as included amounts in your plans,
visit [the pricing page](https://namespace.so/pricing).

## What's next?

Namespace is highly invested in accelerating Bazel builds through a deeper framework integration.
Next up is the ability to horizontally scale your Bazel builds through remote execution on Namespace compute.
[Reach out](mailto:support@namespace.so) to sign up for early access.

Last updated March 5, 2026
