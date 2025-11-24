# Source: https://grafbase.com/docs/cli/commands/introspect.md

# Grafbase Introspect Command

Gets and displays the schema of a graph. Keep in mind that this command requires introspection to be enabled on the server.

**Usage:**

```bash
grafbase introspect [OPTIONS] <URL>
```

**Arguments:**

- `<URL>`: URL of the graph to introspect.

**Options:**

- `-H, --header [<HEADER>...]`: HTTP header to include in the introspection request.
- `--no-color`: Disable color output.

## Examples

Introspect a graph:

```bash
grafbase introspect http://localhost:4000/graphql
```

Introspect a graph with a custom header:

```bash
grafbase introspect --header "Authorization: Bearer asdf" http://localhost:4000/graphql
```