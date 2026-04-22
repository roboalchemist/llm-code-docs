<!-- Source: https://namespace.so/docs/integrations/turborepo -->

# Turborepo caching

Turborepo is a popular build system optimized for Javascript and TypeScript.

Namespace has first-class support for high-performance
[turborepo](https://turbo.build) caching. Caches are backed by storage systems
running alongside your jobs, for maximum network bandwidth and storage
performance.

## Getting started with GitHub Actions

To use turborepo caching, you can simply add Namespace's [`setup-turbocache`](/docs/reference/github-actions/setup-turbocache) to your workspace:

```
jobs:

build:

runs-on: namespace-profile-default

steps:

- name: Checkout code

uses: actions/checkout@v4

- name: Set up caching

uses: namespace-actions/setup-turbocache@v0

- name: Go turbo

run: turbo build
```

## Configuration

By default, caching is performed to a single shared storage `main`. But you can isolate your caches by specifying a separate team (in turbo parlance):

```
jobs:

build:

runs-on: namespace-profile-default

steps:

- name: Checkout code

uses: actions/checkout@4

- name: Set up caching

uses: namespace-actions/setup-turbocache@v0

with:

team: secondary

- name: Go turbo

run: turbo build
```

## Using from your local workstation

You can also use Namespace's turborepo cache from your local machine.
Since the cache is shared, local builds benefit from artifacts already cached by CI — and vice versa.

First, [install the Namespace CLI](/docs/reference/cli/installation). Then create a token with access to turborepo:

```
nsc token create --name turborepo-token --expires_in 7d --user \
  --grant '{"resource_type":"cache/turborepo","resource_id":"*","actions":["read","write"]}'
```

You can configure the expiration up to 90 days.

Then set the following environment variables:

```
export TURBO_API=turbo.cache.ord.namespaceapis.com
export TURBO_TEAM=main
export TURBO_TOKEN="<token, starts with nsrt_>"
```

`TURBO_TEAM` can be any string, and can be used to split caches between different projects.

Alternatively, you can run:

```
turbo login --manual
```

This will ask for the same values, but stores the URL and team in your `turbo.json`.

## Usage

Namespace accounts Turborepo cache usage in two categories:

- Turborepo cache storage
- Turborepo cache reads

For detailed billing information for each item as well as included amounts in your plans,
visit [the pricing page](https://namespace.so/pricing).

Last updated March 12, 2026
