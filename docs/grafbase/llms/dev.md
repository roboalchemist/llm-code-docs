# Source: https://grafbase.com/docs/cli/commands/dev.md

# Grafbase Dev Command

Start the Grafbase local development environment.

**Usage:**

```bash
grafbase dev [OPTIONS]
```

**Options:**

- `-c, --config <CONFIG>`: The path of the configuration file. Defaults to `grafbase.toml`.
- `-g, --graph-ref <GRAPH_REF>`: Graph reference following the format `org/graph@branch`. It is optional, and only necessary if you want to include subgraphs from an existing graph.
- `-p, --port <PORT>`: The port to listen on.

## Examples

Start the local dev environment with a graph from the Grafbase Delivery Network:

```bash
grafbase dev --graph-ref my-org/my-graph@main
```

To override a subgraph, add the following to your configuration file:

```toml
[subgraphs.products]
introspection_url = "http://localhost:4000/graphql"
```

```bash
grafbase dev --graph-ref my-org/my-graph@main --config grafbase.toml
```

The dev command will start a server on `http://localhost:5000/graphql` and a Local UI on `http://localhost:5000/` to load in the browser. The command will load all the subgraphs from `my-org/my-graph@main` together with the local overrides, composing a federated schema.

All changes to the subgraph will be automatically registered to the federated schema. The server will also reload the schema when subgraphs change.

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

If port 5000 is not available, you can run the server on a different port:

```bash
grafbase dev --graph-ref my-org/my-graph@main --port 4000
```

The dev command accepts a configuration file to customize the server. In this example we define a [hooks](https://grafbase.com/docs/gateway/configuration/hooks) WebAssembly file to be loaded by the gateway:

```toml
[hooks]
location = "target/wasm32-wasip2/release/hooks.wasm"
```

Run the dev server with the custom configuration:

```bash
grafbase dev --graph-ref my-org/my-graph@main --config grafbase.toml
```

## MCP

You can enable the MCP server in the configuration file:

```toml
[mcp]
enabled = true
```