# Source: https://docs.snowflake.com/en/sql-reference/sql/desc-snapshot-set.md

# DESCRIBE SNAPSHOT SET

Describes a specific [snapshot set](../../user-guide/backups.md).

DESCRIBE can be abbreviated to DESC.

See also:
:   [CREATE SNAPSHOT SET — Deprecated](create-snapshot-set.md),
    [ALTER SNAPSHOT SET — Deprecated](alter-snapshot-set.md),
    [DROP SNAPSHOT SET — Deprecated](drop-snapshot-set.md),
    [SHOW SNAPSHOT SETS — Deprecated](show-snapshot-sets.md)

## Syntax

```sqlsyntax
DESC[RIBE] SNAPSHOT SET <name>
```

## Parameters

`name`
:   Specifies the identifier for the snapshot set to describe. If the identifier contains spaces or special characters, the entire
    string must be enclosed in double quotes. Identifiers enclosed in double quotes are also case-sensitive.

## Usage notes

* To post-process the output of this command, you can use the [pipe operator](../operators-flow.md)
  (`->>`) or the [RESULT_SCAN](../functions/result_scan.md) function. Both constructs treat the output as a
  result set that you can query.

  For example, you can use the pipe operator or RESULT_SCAN function to select specific columns from the SHOW
  command output or filter the rows.

  When you refer to the output columns, use [double-quoted identifiers](../identifiers-syntax.md) for
  the column names. For example, to select the output column `type`, specify `SELECT "type"`.

  You must use double-quoted identifiers because the output column names for SHOW commands are in lowercase.
  The double quotes ensure that the column names in the SELECT list or WHERE clause match the column names
  in the SHOW command output that was scanned.

## Output

| Column | Description |
| --- | --- |
| `created_on` | Timestamp that the snapshot set was created. |
| `name` | Name of the snapshot set. |
| `database_name` | Name of the database that contains the snapshot set. |
| `schema_name` | Name of the schema that contains the snapshot set. |
| `object_kind` | Type of the object that the snapshot set is snapshotting. |
| `object_name` | Name of the object that the snapshot set is snapshotting. |
| `object_database_name` | Name of the database that contains the object being snapshotted by this snapshot set. |
| `object_schema_name` | Name of the schema that contains the object being snapshotted by this snapshot set. |
| `snapshot_policy_name` | Name of the snapshot policy attached to this snapshot set. |
| `snapshot_policy_database_name` | Name of the database that contains the snapshot policy. |
| `snapshot_policy_schema_name` | Name of the schema that contains the snapshot policy. |
| `snapshot_policy_state` | Current state of the snapshot policy. |
| `owner_role` | Name of the role with the OWNERSHIP privilege on the snapshot set. |
| `owner_role_type` | Type of role with the OWNERSHIP privilege on the snapshot set. |
| `comment` | Comment for backup set. |

## Examples

Describe a snapshot set:

```sqlexample
DESC SNAPSHOT SET my_snapshot_set;
```
