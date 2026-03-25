# Source: https://docs.snowflake.com/en/sql-reference/sql/show-backups-in-backup-set.md

# SHOW BACKUPS IN BACKUP SET

Lists all the [backups](../../user-guide/backups.md) in a backup set.

See also:
:   [CREATE BACKUP SET](create-backup-set.md),
    [ALTER BACKUP SET](alter-backup-set.md),
    [SHOW BACKUP SETS](show-backup-sets.md)

## Syntax

```sqlsyntax
SHOW BACKUPS IN BACKUP SET <name>
  [ LIMIT <rows> ]
```

## Parameters

`name`
:   Specifies the identifier for the backup set.

    If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes.
    Identifiers enclosed in double quotes are also case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

`LIMIT rows`
:   Optionally limits the maximum number of rows returned, while also enabling “pagination” of the results. The actual number of rows
    returned might be less than the specified limit. For example, the number of existing objects is less than the specified limit.

    Default: No value (no limit is applied to the output)

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Notes |
| --- | --- |
| OWNERSHIP | You must have the OWNERSHIP privilege on the backup set to see the backups that it contains. |

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
| `created_on` | Timestamp when the backup is created. |
| `backup_id` | Snowflake-generated identifier of the backup. The backup ID is a UUID value, in the format returned by the [UUID_STRING](../functions/uuid_string.md) function. |
| `backup_set_name` | Name of backup set that contains the backup. |
| `database_name` | Name of database that contains the backup set. |
| `schema_name` | Name of schema that contains the backup set. |
| `expire_on` | Timestamp when the backup expires. |

## Examples

List all backups in backup set `t1_backups`:

```sqlexample
SHOW BACKUPS IN BACKUP SET t1_backups;
```

Show the creation date and backup ID for the oldest backup in backup set `t1_backups`:

```sqlexample
SHOW BACKUPS IN BACKUP SET t1_backups ->>
  SELECT "created_on", "backup_id" FROM $1
    ORDER BY "created_on" LIMIT 1;
```

Show the backup ID and the date and time when the final backup in backup set `t1_backups` will expire.
This example presumes that the backup policy doesn’t include a schedule, or the backup policy is suspended
for the backup set, so that no new backups are being added to the backup set. You’re just waiting for
all the existing backups to expire so that you can drop the backup set.

```sqlexample
SHOW BACKUPS IN BACKUP SET t1_backups ->>
  SELECT "expire_on", "backup_id" FROM $1
    ORDER BY "expire_on" DESC LIMIT 1;
```
