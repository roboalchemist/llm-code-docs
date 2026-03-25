# Source: https://docs.snowflake.com/en/sql-reference/sql/desc-snapshot-policy.md

# DESCRIBE SNAPSHOT POLICY

Describes a specific [snapshot policy](../../user-guide/backups.md).

DESCRIBE can be abbreviated to DESC.

See also:
:   [CREATE SNAPSHOT POLICY — Deprecated](create-snapshot-policy.md),
    [ALTER SNAPSHOT POLICY — Deprecated](alter-snapshot-policy.md),
    [DROP SNAPSHOT POLICY — Deprecated](drop-snapshot-policy.md),
    [SHOW SNAPSHOT POLICIES — Deprecated](show-snapshot-policies.md)

## Syntax

```sqlsyntax
DESC[RIBE] SNAPSHOT POLICY <name>
```

## Parameters

`name`
:   Specifies the identifier for the snapshot policy to describe. If the identifier contains spaces or special characters, the entire
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

> **Note:**
>
> The snapshot policy is an object that’s inside a specific schema and database. Therefore, the policy
> gets replicated, dropped or undropped, and so on, when those operations are performed on the schema and database
> that contain it. If you can’t drop the snapshot policy because it’s associated with any snapshot sets,
> then you also can’t drop the schema or database containing the policy.

To determine whether a snapshot policy is associated with any snapshot sets, use the SHOW SNAPSHOT SETS command.

## Output

| Column | Description |
| --- | --- |
| `created_on` | Timestamp snapshot policy was created. |
| `name` | Name of snapshot policy. |
| `database_name` | Name of database that contains the snapshot policy. |
| `schema_name` | Name of schema that contains the snapshot policy. |
| `owner` | Name of the role with the OWNERSHIP privilege on the snapshot policy. |
| `comment` | Comment for snapshot policy. |
| `schedule` | Schedule for snapshot creation. |
| `expire_after_days` | Number of days after snapshot creation when snapshot expires. |
| `has_retention_lock` | Indicates whether the policy includes a retention lock.  `Y` if policy has retention lock; `N` otherwise.  For more information, see [Retention lock](../../user-guide/backups.md). |
| `owner` | Name of the role with the OWNERSHIP privilege on the snapshot set. |
| `owner_role_type` | Type of role with the OWNERSHIP privilege on the snapshot policy. |

## Examples

Describe a snapshot policy:

```sqlexample
DESC SNAPSHOT POLICY my_snapshot_policy;
```
