# Source: https://docs.snowflake.com/en/user-guide/backups.md

# Source: https://docs.snowflake.com/en/sql-reference/organization-usage/backups.md

# Source: https://docs.snowflake.com/en/sql-reference/info-schema/backups.md

# Source: https://docs.snowflake.com/en/sql-reference/account-usage/backups.md

Schema:
:   [ACCOUNT_USAGE](../account-usage.md)

# BACKUPS view

This Account Usage view provides information on [backups](../../user-guide/backups.md).

## Columns

| Column name | Data type | Description |
| --- | --- | --- |
| ID | VARCHAR | Snowflake-generated identifier of the backup.  Note: this is not the local ID, this is the globally unique UUID of the Backup. |
| BACKUP_SET_ID | NUMBER | ID of backup set that contains the backup. |
| BACKUP_SET_NAME | VARCHAR | Name of backup set that contains the backup. |
| BACKUP_SET_SCHEMA_ID | NUMBER | ID of schema that the backup set belongs to. |
| BACKUP_SET_SCHEMA | VARCHAR | Name of schema that the backup set belongs to. |
| BACKUP_SET_CATALOG_ID | NUMBER | ID of database that the backup set belongs to. |
| BACKUP_SET_CATALOG | VARCHAR | Name of database that the backup set belongs to. |
| CREATED | TIMESTAMP_LTZ | Timestamp at which backup was created. |
| DELETED | TIMESTAMP_LTZ | Timestamp at which the backup was deleted.  This column isn’t displayed by the SHOW command, because the SHOW command output doesn’t include deleted objects. |
| EXPIRATION_SCHEDULED_FOR | TIMESTAMP_LTZ | Timestamp at which backup will be expired and deleted. |
| IS_UNDER_LEGAL_HOLD | BOOLEAN | True if backup is under legal hold; False otherwise. |

## Usage notes

* Latency for the view may be up to 360 minutes (6 hours).
