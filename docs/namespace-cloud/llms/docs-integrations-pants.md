<!-- Source: https://namespace.so/docs/integrations/pants -->

# Pants integration

Pants is a popular build system for monorepos with multiple languages and frameworks.

Namespace delivers fast [Pants](https://www.pantsbuild.org/) caching with minimal network delays between build runners and cache storage.
This enables your Pants workflows to share and reuse build artifacts between different runs, regardless of how you've configured your build granularity, which substantially cuts down on overall build times.

## Getting started

To use Pants caching, you can produce a ready-to-use configuration using the [CLI](/docs/reference/cli/installation):

### Configure cache access

```
$

```
nsc cache pants setup --pants-toml=/tmp/pants.toml
```
```

This command generates short-term credentials, and sets up a Pants configuration file.

### Use the Pants cache

```
$

```
pants --pants-config-files="['/your/own/pants.toml', '/tmp/pants.toml']" test ::
```
```

As demonstrated, you can pass multiple configuration files allowing you to combine your existing configuration with Namespace cache access.

### GitHub Actions Example

```
jobs:

build:

runs-on: namespace-profile-default

steps:

- name: Setup Pants cache

run: |

nsc cache pants setup --pants-toml=/tmp/pants.toml

- name: Pants test

run: |

pants --pants-config-files="['/your/own/pants.toml', '/tmp/pants.toml']" test ::
```

The `pants.toml` path can be customized if you need to use a specific configuration file.

## How it works

The Pants remote caching solution employs a tiered caching approach, where the hot cache lives as close to the consumer (e.g. your CI job runner) as possible.
The cold caching tier is backed by our [high-performance artifact storage](/docs/architecture/storage/artifact-storage) and enables Pants to retain a vast amount of cached artifacts.

Access to the Pants cache is granted through short-lived secure credentials.

## Usage

Namespace accounts Pants cache usage in two categories:

- Pants cache storage
- Pants cache reads

For detailed billing information for each item as well as included amounts in your plans,
visit [the pricing page](https://namespace.so/pricing).

Last updated March 5, 2026
