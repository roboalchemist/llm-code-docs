# Source: https://grafbase.com/docs/cli/commands/publish.md

# Grafbase Publish Command

Publishes a subgraph schema.

**Usage:**

```bash
grafbase publish [OPTIONS] --name <SUBGRAPH_NAME> --url <URL> <GRAPH_REF>
```

**Arguments:**

- `<GRAPH_REF>`: Graph reference that uses the format `account/graph@branch`.

**Options:**

- `--name <SUBGRAPH_NAME>`: Subgraph name to publish.
- `--schema <SCHEMA_PATH>`: Path to the schema file to publish. If this is not provided, the schema will be read from standard input.
- `--url <URL>`: The URL to the GraphQL endpoint of the subgraph.
- `-m, --message <MESSAGE>`: Commit message for the schema change.

## Examples

Introspect a remote graph and publish the schema from standard input:

```bash
grafbase introspect http://localhost:4000/graphql \
    | grafbase publish \
        --name users \
        --url http://localhost:4000/graphql \
        --message "Adds name field to the User type" \
        my-org/my-graph@main
```

Publish a schema file:

```bash
grafbase publish \
    --name users \
    --url http://localhost:4000/graphql \
    --message "Adds name field to the User type" \
    --schema users.graphql \
    my-org/my-graph@main
```