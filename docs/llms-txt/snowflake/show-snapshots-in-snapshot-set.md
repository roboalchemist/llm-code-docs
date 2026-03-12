# Source: https://docs.snowflake.com/en/sql-reference/sql/show-snapshots-in-snapshot-set.md

# SHOW SNAPSHOTS IN SNAPSHOT SET — *Deprecated*

Lists all the [snapshots](../../user-guide/backups.md) in a snapshot set.

See also:
:   [CREATE SNAPSHOT SET — Deprecated](create-snapshot-set.md),
    [ALTER SNAPSHOT SET — Deprecated](alter-snapshot-set.md),
    [SHOW SNAPSHOT SETS — Deprecated](show-snapshot-sets.md)

## Syntax

```sqlsyntax
SHOW SNAPSHOTS IN SNAPSHOT SET <name>
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

| Privilege | Notes |
| --- | --- |
| OWNERSHIP | You must have the OWNERSHIP privilege on the snapshot set to see the snapshots that it contains. |

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* The command returns a maximum of ten thousand records for the specified object type, as dictated by the access privileges for the role
  used to execute the command. Any records above the ten thousand records limit aren’t returned, even with a filter applied.

  To view results for which more than ten thousand records exist, query the corresponding view (if one exists) in the [Snowflake Information Schema](../info-schema.md).

## Output

| Column | Description |
| --- | --- |
| `created_on` | Timestamp snapshot is created. |
| `snapshot_id` | Snowflake-generated identifier of the snapshot. The snapshot ID is a UUID value, in the format returned by the [UUID_STRING](../functions/uuid_string.md) function. |
| `snapshot_set_name` | Name of snapshot set that contains the snapshot. |
| `database_name` | Name of database that contains the snapshot set. |
| `schema_name` | Name of schema that contains the snapshot set. |
| `expire_on` | Timestamp when the snapshot expires. |

## Examples

List all snapshots in snapshot set `t1_snapshots`:

```sqlexample
SHOW SNAPSHOTS IN SNAPSHOT SET t1_snapshots;
```

Show the creation date and snapshot ID for the oldest snapshot in snapshot set `t1_snapshots`:

```sqlexample
SHOW SNAPSHOTS IN SNAPSHOT SET t1_snapshots ->>
  SELECT "created_on", "snapshot_id" FROM $1
    ORDER BY "created_on" LIMIT 1;
```

Show the snapshot ID and the date and time when the final snapshot in snapshot set `t1_snapshots` will expire.
This example presumes that the snapshot policy doesn’t include a schedule, or the snapshot policy is suspended
for the snapshot set, so that no new snapshots are being added to the snapshot set. You’re just waiting for
all the existing snapshots to expire so that you can drop the snapshot set.

```sqlexample
SHOW SNAPSHOTS IN SNAPSHOT SET t1_snapshots ->>
  SELECT "expire_on", "snapshot_id" FROM $1
    ORDER BY "expire_on" DESC LIMIT 1;
```
