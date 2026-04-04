# Source: https://grafbase.com/docs/cli/commands/lint.md

# Grafbase Lint Command

Lints a GraphQL schema.

**Usage:**

```bash
grafbase lint [SCHEMA]
```

**Arguments:**

- `[SCHEMA]`: Path to the schema file to lint.

## Examples

Lint a schema file:

```bash
grafbase lint my-schema.graphql
```

Lint a schema from standard input:

```bash
grafbase introspect http://localhost:4000/graphql | grafbase lint
```