# Source: https://buildkite.com/docs/platform/cli/reference/organization.md

# Buildkite CLI organization command

The `bk organization` command allows you to manage Buildkite organizations from the command line.

## Commands

| Command | Description |
| --- | --- |
| `bk organization list` | List configured organizations. |

## List organizations

List configured organizations.

```bash
bk organization list [flags]
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

List all configured organizations (JSON by default):

```bash
bk organization list
```

List organizations in text format:

```bash
bk organization list -o text
```
