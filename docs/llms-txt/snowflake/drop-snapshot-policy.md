# Source: https://docs.snowflake.com/en/sql-reference/sql/drop-snapshot-policy.md

# DROP SNAPSHOT POLICY — *Deprecated*

Deletes a [snapshot](../../user-guide/backups.md) policy.

See also:
:   [CREATE SNAPSHOT POLICY — Deprecated](create-snapshot-policy.md),
    [ALTER SNAPSHOT POLICY — Deprecated](alter-snapshot-policy.md),
    [SHOW SNAPSHOT POLICIES — Deprecated](show-snapshot-policies.md)

## Syntax

```sqlsyntax
DROP SNAPSHOT POLICY <name>
```

## Parameters

`name`
:   Specifies the identifier for the snapshot policy.

    If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes.
    Identifiers enclosed in double quotes are also case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| OWNERSHIP | Snapshot policy | The role used to delete a snapshot policy must have the OWNERSHIP privilege on the policy. |

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

A snapshot policy can’t be deleted if it is attached to any snapshot set.

## Examples

Delete the snapshot policy `hourly_snapshot_policy`:

```sqlexample
DROP SNAPSHOT POLICY hourly_snapshot_policy;
```
