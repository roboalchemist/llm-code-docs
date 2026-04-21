# nsc destroy

Terminate a Namespace instance by its ID.

## Basic Usage

```bash
nsc destroy <instance-id> [--force]
```

## Description

This command removes a Namespace instance permanently.

## Options

**--force**: Bypasses the confirmation prompt when destroying the instance, allowing the operation to proceed without user confirmation.

## Example Usage

```bash
nsc destroy h9am86n6gi25m
nsc destroy h9am86n6gi25m --force
```

## Related Commands

- `nsc create` - Creates a new instance
- `nsc list` - Lists instances
- `nsc extend` - Extends instance lifetime
