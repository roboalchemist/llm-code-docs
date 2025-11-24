# Source: https://grafbase.com/docs/cli/commands/check.md

# Grafbase Check Command

Checks a graph to locate validation, composition, and breaking change errors.

**Usage:**

```bash
grafbase check [OPTIONS] --name <SUBGRAPH_NAME> <GRAPH_REF>
```

**Arguments:**

- `<GRAPH_REF>`: Graph reference that uses the format `organization/graph@branch`.

**Options:**

- `--name <SUBGRAPH_NAME>`: Subgraph name to check.
- `--schema <SCHEMA_FILE>`: Path to the schema file to check. If this is not provided, the schema will be read from standard input.

## Examples

Check a subgraph schema file:

```bash
grafbase check --name my-subgraph --schema my-subgraph.graphql my-org/my-graph@main
```

Check a subgraph schema from standard input:

```bash
grafbase introspect http://localhost:4000/graphql | grafbase check --name my-subgraph my-org/my-graph@main
```