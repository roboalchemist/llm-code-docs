# Source: https://docs.snowflake.com/en/sql-reference/account-usage/snapshot_storage_usage.md

Schema:
:   [ACCOUNT_USAGE](../account-usage.md)

# SNAPSHOT_STORAGE_USAGE view — *Deprecated*

This Account Usage view provides information about storage usage for [snapshots](../../user-guide/backups.md).

> **Note:**
>
> The same tables might be included in multiple table snapshots, schema snapshots, and database snapshots.
> Therefore, the numbers of bytes shown in this view don’t entirely answer questions about how much storage
> you can save by deleting a snapshot or a snapshot set. The same data files might be retained as part of
> a different snapshot set.

## Columns

| Column name | Data type | Description |
| --- | --- | --- |
| SNAPSHOT_SET_ID | NUMBER | Internal system-generated identifier for the snapshot set. |
| SNAPSHOT_ID | VARCHAR | Internal system-generated identifier for the snapshot. |
| LOGICAL_BYTES | NUMBER | Number of bytes created when this snapshot is restored. |
| INCREMENTAL_BYTES_FROM_PREVIOUS_SNAPSHOT | NUMBER | Number of logical bytes of the micro-partitions that *are* in this snapshot, but *aren’t* in the previous snapshot within the same snapshot set.  For the oldest active snapshot in a snapshot set, this is 0. |
| DECREMENTAL_BYTES_FROM_PREVIOUS_SNAPSHOT | NUMBER | Number of logical bytes of the micro-partitions that *aren’t* in this snapshot, but *are* in the previous snapshot within the same snapshot set.  For the oldest active snapshot in a snapshot set, this is 0. |

## Usage notes

* Latency for the view may be up to 360 minutes (6 hours).
