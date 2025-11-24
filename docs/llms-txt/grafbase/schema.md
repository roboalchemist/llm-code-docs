# Source: https://grafbase.com/docs/cli/commands/schema.md

# Grafbase Schema Command

Fetch a schema from the Grafbase schema registry.

**Usage:**

```bash
grafbase schema [OPTIONS] <GRAPH_REF>
```

**Arguments:**

- `<GRAPH_REF>`: Graph reference that uses the format `org/graph@branch`.

**Options:**

- `--name <SUBGRAPH_NAME>`: Subgraph name to fetch. If not provided, the federated graph schema is fetched.

## Examples

Fetch the schema of a subgraph:

```bash
grafbase schema --name users my-org/my-graph@main
```

Fetch the schema of a federated graph:

```bash
grafbase schema my-org/my-graph@main
```