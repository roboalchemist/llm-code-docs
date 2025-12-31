# Source: https://grafbase.com/docs/cli/commands/schema-proposal.md

# Grafbase Schema Proposal Command

Manage schema proposals.

## Create a Schema Proposal

Creates a new schema proposal, and print its ID.

**Usage:**

```bash
grafbase schema-proposal create <GRAPH_REF> --name <NAME> [OPTIONS]
```

**Arguments:**

- `<GRAPH_REF>`: Graph reference that uses the format `account/graph@branch`.

**Options:**

- `--name <NAME>`: The name of the schema proposal.
- `--description <DESCRIPTION>`: An optional description for the schema proposal.
- `--subgraph-name <SUBGRAPH_NAME>`: The name of the subgraph to create an initial revision for.
- `--schema <SCHEMA_FILE>`: Path to the schema file for the initial revision.
- `--schema-stdin`: Read the schema for the initial revision from standard input.

## Edit a Schema Proposal

Edits an existing schema proposal.

**Usage:**

```bash
grafbase schema-proposal edit --schema-proposal-id <ID> --subgraph-name <SUBGRAPH_NAME> [OPTIONS]
```

**Options:**

- `--schema-proposal-id <ID>`: The ID of the schema proposal to edit.
- `--subgraph-name <SUBGRAPH_NAME>`: The name of the subgraph to edit.
- `--description <DESCRIPTION>`: An optional description for the edit.
- `--schema <SCHEMA_FILE>`: Path to the schema file for the edit.
- `--schema-stdin`: Read the schema for the edit from standard input.

## Examples

Create a new schema proposal:

```bash
grafbase schema-proposal create my-org/my-graph@main --name "My new feature"
```

Create a new schema proposal with an initial revision from a file:

```bash
grafbase schema-proposal create my-org/my-graph@main --name "My new feature" --subgraph-name "users" --schema users.graphql
```

Create a new schema proposal with an initial revision from stdin:

```bash
cat users.graphql | grafbase schema-proposal create my-org/my-graph@main --name "My new feature" --subgraph-name "users" --schema-stdin
```

Edit an existing schema proposal:

```bash
grafbase schema-proposal edit --schema-proposal-id "sp_123" --subgraph-name "users" --schema users.graphql
```