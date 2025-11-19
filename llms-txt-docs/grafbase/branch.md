# Source: https://grafbase.com/docs/cli/commands/branch.md

# Grafbase Branch Command

Commands that lets you manage branches.

## Create a Branch

Creates a new branch.

**Usage:**

```bash
grafbase branch create <BRANCH_REF>
```

**Arguments:**

- `<BRANCH_REF>`: Branch reference that uses the format `account/graph@branch`.

## Remove a Branch

Removes a branch.

**Usage:**

```bash
grafbase branch remove <BRANCH_REF>
```

**Arguments:**

- `<BRANCH_REF>`: Branch reference that uses the format `account/graph@branch`.

## Examples

Create a branch:

```bash
grafbase branch create staging
```

Remove a branch:

```bash
grafbase branch remove staging
```