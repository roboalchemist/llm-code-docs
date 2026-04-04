# Source: https://docs.snowflake.com/en/sql-reference/sql/drop-snapshot-set.md

# DROP SNAPSHOT SET — *Deprecated*

Deletes a [snapshot](../../user-guide/backups.md) set.

See also:
:   [CREATE SNAPSHOT SET — Deprecated](create-snapshot-set.md),
    [ALTER SNAPSHOT SET — Deprecated](alter-snapshot-set.md),
    [SHOW SNAPSHOT SETS — Deprecated](show-snapshot-sets.md)

## Syntax

```sqlsyntax
DROP SNAPSHOT SET <name>
```

## Parameters

`name`
:   Specifies the identifier for the snapshot set.

    If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes.
    Identifiers enclosed in double quotes are also case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| OWNERSHIP | Snapshot set | The role used to modify the snapshot policy for a snapshot set must have the OWNERSHIP privilege on the set. |

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

> **Important:**
>
> If the snapshot policy has a retention lock applied to it, and there are any
> unexpired snapshots in the snapshot set, then you can’t delete the snapshot set.
> In that case, you must wait for all the snapshots in the set to expire.
> This restriction applies even to privileged roles such as ACCOUNTADMIN, and to Snowflake support.
> For that reason, be careful when specifying retention lock and a long expiration
> period in a snapshot policy.
>
> You also can’t drop a snapshot set if any of the snapshots it contains have a legal hold applied.

## Examples

Delete the snapshot set `t1_snapshots`:

```sqlexample
DROP SNAPSHOT SET t1_snapshots;
```
