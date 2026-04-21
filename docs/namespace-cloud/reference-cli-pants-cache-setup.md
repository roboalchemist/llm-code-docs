<!-- Source: https://namespace.so/docs/reference/cli/pants-cache-setup -->

# nsc cache pants setup

Set up a remote cache for Pantsbuild.

Namespace provides high-performance remote caching with very low network latency between runners and the cache storage.
This allows your Pantsbuild workflows to reuse build artifacts across runs, irrespective of your chosen granularity, significantly reducing build times.
`cache pants setup` sets up a remote cache for Pantsbuild and generates a `pants.toml` to use it.

[Learn more about Pantsbuild caching →](/docs/integrations/pants)

## Usage

```
nsc cache pants setup [--pants-toml <target pants toml path>]
```

### Example

The following example creates a remote cache and uses it during a Pantsbuild invocation.

```
$ nsc cache pants setup --pants-toml=/tmp/pants.toml
```

Next, let's use the generated configuration

```
$ pants --pants-config-files="['/your/own/pants.toml', '/tmp/pants.toml', ...]" test ::
```

## Options

### --pants-toml

If specified, write the toml to this path.

Last updated March 5, 2026
