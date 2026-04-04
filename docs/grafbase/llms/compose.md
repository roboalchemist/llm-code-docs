# Source: https://grafbase.com/docs/cli/commands/compose.md

# Grafbase Compose Command

Compose a federated schema from your subgraphs and print the resulting schema to stdout.

**Usage:**

```bash
grafbase compose [OPTIONS]
```

**Options:**

- `-c, --config <CONFIG>`: The path of the configuration file. Defaults to `grafbase.toml`.
- `-g, --graph-ref <GRAPH_REF>`: Graph reference following the format `org/graph@branch`. It is optional, and only necessary if you want to include subgraphs from an existing graph.

## Examples

Compose a federated schema from a subgraph in the Grafbase platform:

```bash
grafbase compose --graph-ref my-org/my-graph@main
```

To override a subgraph, add the following to your configuration file:

```toml
[subgraphs.products]
introspection_url = "http://localhost:4000/graphql"
```

```bash
grafbase compose --graph-ref my-org/my-graph@main --config grafbase.toml
```

The compose command will gather all subgraphs from `my-org/my-graph@main` together with any local overrides, compose them into a federated schema, and print the result to stdout.

Note that the `--graph-ref` argument is optional. If you do not provide a graph ref, only the local subgraphs (defined in your configuration file) will be included.

To add introspection headers add the following to the configuration file:

```toml
[subgraphs.products.introspection_headers]
authorization = "Bearer {{ env.PRODUCTS_ACCESS_TOKEN }}"
```

To provide the schema path add the following to the configuration file:

```toml
[subgraphs.products]
schema_path = "/path/to/products.graphql"
```

You can redirect the output to a file:

```bash
grafbase compose --graph-ref my-org/my-graph@main > federated-schema.graphql
```

The compose command accepts a configuration file to customize the composition process:

```bash
grafbase compose --graph-ref my-org/my-graph@main --config grafbase.toml
```

Unlike the `dev` command, `compose` only generates the federated schema and does not start a server or UI.