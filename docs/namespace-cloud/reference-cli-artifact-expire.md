<!-- Source: https://namespace.so/docs/reference/cli/artifact-expire -->

# nsc artifact expire

Expire an artifact.

`artifact expire` expires an [artifact](/docs/architecture/storage/artifact-storage) in this workspace,
marking it for deletion.

## Usage

```
$

```
nsc artifact expire <path> [--namespace <namespace>]
```
```

### Example

```
% nsc artifact expire target.txt
Expired target.txt (namespace main)
```

## Options

### --namespace <namespace>

Namespace of the artifact. Defaults to "main".

Last updated February 5, 2026
