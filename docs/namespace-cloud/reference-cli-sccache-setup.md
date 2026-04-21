<!-- Source: https://namespace.so/docs/reference/cli/sccache-setup -->

# nsc cache sccache setup

Set up a remote sccache cache.

`cache sccache setup` configures [sccache](https://github.com/mozilla/sccache) to use Namespace's high-performance remote caching and outputs the required environment variables.

## Usage

```
nsc cache sccache setup
```

### Example

```
$ nsc cache sccache setup
SCCACHE_WEBDAV_ENDPOINT=https://cache.namespace.so:8080
SCCACHE_WEBDAV_KEY_PREFIX=sccache/my-cache/
SCCACHE_WEBDAV_TOKEN=scc_token_abc123...
```

To use these in your build:

```
$ eval $(nsc cache sccache setup)
$ sccache --start-server
```

## Options

### --output, -o <format>

Output format. One of `plain` or `json`. Default is `plain`.

### --cache\_name <name>

A name for the cache.

### --site <site>

Site preference (e.g. `iad`, `fra`). If not set, determined automatically.

Last updated March 5, 2026
