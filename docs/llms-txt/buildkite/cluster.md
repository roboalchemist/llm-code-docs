# Source: https://buildkite.com/docs/platform/cli/reference/cluster.md

# Buildkite CLI cluster command

The `bk cluster` command allows you to manage Buildkite organization clusters from the command line.

## Commands

| Command | Description |
| --- | --- |
| `bk cluster list` | List clusters. |
| `bk cluster view` | View cluster information. |

## List clusters

List clusters.

```bash
bk cluster list [flags]
```

### Flags

| Flag | Description |
| --- | --- |
| `-o`, `--output=""` | Output format. One of: json, yaml, text |
| `--debug` | Enable debug output for REST API calls |
| `--json` | Output as JSON |
| `--text` | Output as text |
| `--yaml` | Output as YAML |

### Examples

List all clusters:

```bash
bk cluster list
```

List clusters in JSON format:

```bash
bk cluster list -o json
```

## View a cluster

View cluster information.

```bash
bk cluster view <cluster-id> [flags]
```

### Arguments

| Argument | Description |
| --- | --- |
| `<cluster-id>` | Cluster ID to view |

### Flags

| Flag | Description |
| --- | --- |
| `-o`, `--output=""` | Output format. One of: json, yaml, text |
| `--debug` | Enable debug output for REST API calls |
| `--json` | Output as JSON |
| `--text` | Output as text |
| `--yaml` | Output as YAML |

### Examples

View a cluster:

```bash
bk cluster view my-cluster-id
```

View cluster in JSON format:

```bash
bk cluster view my-cluster-id -o json
```
