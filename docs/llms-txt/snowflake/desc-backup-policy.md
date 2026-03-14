# Source: https://docs.snowflake.com/en/sql-reference/sql/desc-backup-policy.md

# DESCRIBE BACKUP POLICY

Describes a specific [backup policy](../../user-guide/backups.md).

DESCRIBE can be abbreviated to DESC.

See also:
:   [CREATE BACKUP POLICY](create-backup-policy.md),
    [ALTER BACKUP POLICY](alter-backup-policy.md),
    [DROP BACKUP POLICY](drop-backup-policy.md),
    [SHOW BACKUP POLICIES](show-backup-policies.md)

## Syntax

```sqlsyntax
DESC[RIBE] BACKUP POLICY <name>
```

## Parameters

`name`
:   Specifies the identifier for the backup policy to describe. If the identifier contains spaces or special characters, the entire
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
> The backup policy is an object that’s inside a specific schema and database. Therefore, the policy
> gets replicated, dropped or undropped, and so on, when those operations are performed on the schema and database
> that contain it. If you can’t drop the backup policy because it’s associated with any backup sets,
> then you also can’t drop the schema or database containing the policy.

To determine whether a backup policy is associated with any backup sets, use the SHOW BACKUP SETS command.

## Output

| Column | Description |
| --- | --- |
| `created_on` | Timestamp backup policy was created. |
| `name` | Name of backup policy. |
| `database_name` | Name of database that contains the backup policy. |
| `schema_name` | Name of schema that contains the backup policy. |
| `owner` | Name of the role with the OWNERSHIP privilege on the backup policy. |
| `comment` | Comment for backup policy. |
| `schedule` | Schedule for backup creation. |
| `expire_after_days` | Number of days after backup creation when backup expires. |
| `has_retention_lock` | Indicates whether the policy includes a retention lock.  `Y` if policy has retention lock; `N` otherwise.  For more information, see [Retention lock](../../user-guide/backups.md). |
| `owner` | Name of the role with the OWNERSHIP privilege on the backup set. |
| `owner_role_type` | Type of role with the OWNERSHIP privilege on the backup policy. |

## Examples

Describe a backup policy:

```sqlexample
DESC BACKUP POLICY my_backup_policy;
```
