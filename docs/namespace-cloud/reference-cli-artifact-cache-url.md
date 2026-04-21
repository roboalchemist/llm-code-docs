<!-- Source: https://namespace.so/docs/reference/cli/artifact-cache-url -->

# nsc artifact cache-url

Download an arbitrary URL using a pull-through cache.

`artifact cache-url` downloads the content from an arbitrary URL and caches it as an [artifact](/docs/architecture/storage/artifact-storage) for fast access.

If the content is already present in the artifact cache for the given URL it will be used instead.
The content at the URL is assumed to be immutable.

## Usage

```
nsc artifact cache-url <target url> --out <filename> [--max_age <duration>]
```

### Example

```
% nsc artifact cache-url https://namespace.so/robots.txt --out robots.txt
Downloaded to robots.txt
```

## Options

### --out <filename>

Filename to save the downloaded content at. Required.

### --max\_age <duration>

Redownload from source if the cached content is older than this duration.

Last updated July 4, 2025
