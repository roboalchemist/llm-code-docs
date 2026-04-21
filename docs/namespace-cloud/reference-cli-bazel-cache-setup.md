<!-- Source: https://namespace.so/docs/reference/cli/bazel-cache-setup -->

# nsc cache bazel setup

Set up a remote Bazel cache.

Namespace provides high-performance Bazel caching with very low network latency between runners and the cache storage.
This allows your Bazel workflows to reuse build artifacts across runs, irrespective of your chosen granularity, significantly reducing build times.
`cache bazel setup` sets up a remote Bazel cache and generates a bazelrc to use it.

[Learn more about Bazel caching →](/docs/integrations/bazel)

## Usage

```
nsc cache bazel setup [--bazelrc <target bazelrc path>]
```

### Example

The following example creates a remote Bazel cache and uses it during a build invocation.

```
$ nsc cache bazel setup --bazelrc=/tmp/bazel-cache.bazelrc
```

Next, let's use the generated configuration

```
$ bazel --bazelrc=yourown.bazelrc --bazelrc=/tmp/bazel-cache.bazelrc build //...
```

## Options

### --bazelrc

If specified, write the bazelrc to this path.

Last updated March 5, 2026
