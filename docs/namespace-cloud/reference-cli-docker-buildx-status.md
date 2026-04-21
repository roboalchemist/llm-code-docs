<!-- Source: https://namespace.so/docs/reference/cli/docker-buildx-status -->

# nsc docker buildx status

Status information for the local Namespace buildx context.

`docker buildx status` displays the current status of the Namespace remote buildx builder.

## Usage

```
nsc docker buildx status
```

### Example

```
$ nsc docker buildx status
Platform: linux/amd64
  Status:     ready
  Instance:   85a32emcg99ii
  Requests:   42
 
Platform: linux/arm64
  Status:     ready
  Instance:   h9am86n6gi25m
  Requests:   38
```

## Options

### --output, -o <format>

Output format. One of `plain` or `json`. Default is `plain`.

### --name <builder-name>

The name of the buildx builder to check. Default is `nsc-remote`.

Last updated February 13, 2026
