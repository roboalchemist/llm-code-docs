<!-- Source: https://namespace.so/docs/reference/cli/artifact-upload -->

# nsc artifact upload

Upload an artifact.

`artifact upload` uploads an [artifact](/docs/architecture/storage/artifact-storage) for this workspace.
Currently, only single file uploads are supported.

## Usage

```
$

```
nsc artifact upload <src> <dest> [--namespace <namespace>]
```
```

### Example

```
% nsc artifact upload text.txt target.txt
Uploaded text.txt to target.txt (namespace main)
```

## Options

### --expires\_in <duration>

Sets the expiration time for the artifact. By default, artifacts do not expire. The duration is specified as a time duration string (e.g., "72h", "30m", "1h30m").
Valid time units are "ns" (nanoseconds), "us" or "µs" (microseconds), "ms" (milliseconds), "s" (seconds), "m" (minutes), and "h" (hours).

### --namespace <namespace>

Target namespace of the artifact.

Last updated October 10, 2025
