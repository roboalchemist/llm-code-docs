<!-- Source: https://namespace.so/docs/reference/cli/registry-list -->

# nsc registry list

List images or repositories in the registry.

`registry list` lists container images or repositories in your workspace's private [Namespace Container Registry](/docs/architecture/storage/container-registry).

## Usage

```
nsc registry list [repository]
```

### Example

List all repositories:

```
$ nsc registry list --repositories
Repository Name       Last Push
myapp                 2024-01-15T10:30:00Z
backend-service       2024-01-14T15:45:30Z
```

List images in a repository:

```
$ nsc registry list myapp
Image Reference                          Size      Created
nscr.io/myapp:latest@sha256:abc123...    256 MiB   2024-01-15T10:30:00Z
nscr.io/myapp:v1.2.3@sha256:def456...   248 MiB   2024-01-14T15:45:30Z
```

## Options

### --repositories

List repositories instead of images.

### --repository <name>

Filter images by repository name.

### --include\_deleted

Include deleted images in results.

### --limit <count>

The maximum number of images or repositories to list.

### --output, -o <format>

Output format. One of `table` or `json`. Default is `table`.

Last updated February 13, 2026
