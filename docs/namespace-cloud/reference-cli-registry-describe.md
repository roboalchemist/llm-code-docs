<!-- Source: https://namespace.so/docs/reference/cli/registry-describe -->

# nsc registry describe

Get detailed information about a specific image.

`registry describe` shows detailed information about a container image in your workspace's private [Namespace Container Registry](/docs/architecture/storage/container-registry).

## Usage

```
nsc registry describe [image-reference]
```

### Example

```
$ nsc registry describe nscr.io/myapp:latest
Repository:  myapp
Digest:      sha256:abc123def456
Size:        256 MiB
Created At:  2024-01-15T10:30:00Z
Expires At:  2024-02-15T10:30:00Z
```

## Options

### --repository <name>

Repository name.

### --reference <ref>

Image reference (tag or digest).

### --output, -o <format>

Output format. One of `table` or `json`. Default is `table`.

Last updated February 13, 2026
