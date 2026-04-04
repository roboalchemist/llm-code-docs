# Source: https://docs.snowflake.com/en/sql-reference/account-usage/backup_storage_usage.md

Schema:
:   [ACCOUNT_USAGE](../account-usage.md)

# BACKUP_STORAGE_USAGE view

This Account Usage view provides information about storage usage for [backups](../../user-guide/backups.md).

> **Note:**
>
> The same tables might be included in multiple table backups, schema backups, and database backups.
> Therefore, the numbers of bytes shown in this view don’t entirely answer questions about how much storage
> you can save by deleting a backup or a backup set. The same data files might be retained as part of
> a different backup set.

## Columns

| Column name | Data type | Description |
| --- | --- | --- |
| BACKUP_SET_ID | NUMBER | Internal system-generated identifier for the backup set. |
| BACKUP_ID | VARCHAR | Internal system-generated identifier for the backup. |
| LOGICAL_BYTES | NUMBER | Number of bytes created when this backup is restored. |
| INCREMENTAL_BYTES_FROM_PREVIOUS_BACKUP | NUMBER | Number of logical bytes of the micro-partitions that *are* in this backup, but *aren’t* in the previous backup within the same backup set.  For the oldest active backup in a backup set, this is 0. |
| DECREMENTAL_BYTES_FROM_PREVIOUS_BACKUP | NUMBER | Number of logical bytes of the micro-partitions that *aren’t* in this backup, but *are* in the previous backup within the same backup set.  For the oldest active backup in a backup set, this is 0. |

## Usage notes

* Latency for the view may be up to 360 minutes (6 hours).
