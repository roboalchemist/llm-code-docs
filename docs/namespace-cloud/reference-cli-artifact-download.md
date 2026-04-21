<!-- Source: https://namespace.so/docs/reference/cli/artifact-download -->

# nsc artifact download

Download an artifact.

`artifact download` downloads an [artifact](/docs/architecture/storage/artifact-storage) for this workspace.
Currently, only single file downloads are supported.

## Usage

```
nsc artifact download <src> <dest> [--namespace <namespace>]
```

### Example

```
% nsc artifact download remote.txt local.txt
Downloaded remote.txt (namespace main) to local.txt
```

## Options

### --namespace <namespace>

Namespace of the artifact.

Last updated July 4, 2025
