# Source: https://grafbase.com/docs/cli/commands/subgraphs.md

# Grafbase Subgraph Command

List all subgraphs of a branch.

**Usage:**

```bash
grafbase subgraph list <GRAPH_REF>
```

**Arguments:**

- `<BRANCH_REF>`: Graph reference that uses the format `account/graph@branch`.

## Remove a Subgraph

Removes a subgraph.

**Usage:**

```bash
grafbase subgraph remove <GRAPH_REF> <SUBGRAPH_NAME>
```

**Arguments:**

- `<GRAPH_REF>`: Branch reference that uses the format `account/graph@branch`.
- `<SUBGRAPH_NAME>`: Name of the subgraph to remove.

## Examples

List subgraphs:

```bash
grafbase subgraph list my-org/my-graph@main
```

Remove a subgraph:

```bash
grafbase subgraph remove my-org/my-graph@main my-subgraph
```