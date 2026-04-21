<!-- Source: https://namespace.so/docs/reference/cli/artifact-describe -->

# nsc artifact describe

Describe an artifact's metadata.

`artifact describe` displays metadata about a previously uploaded artifact.

## Usage

```
nsc artifact describe <path>
```

### Example

```
$ nsc artifact describe build-outputs/app.tar.gz
Path:      build-outputs/app.tar.gz
Namespace: main
Size:      342 KiB
Status:    AVAILABLE
Created:   2024-01-15T10:30:00Z
Expires:   2024-02-15T10:30:00Z
```

## Options

### --namespace <namespace>

Namespace of the artifact. Default is `main`.

### --output, -o <format>

Output format. One of `plain` or `json`. Default is `plain`.

Last updated February 13, 2026
