# Source: https://docs.snowflake.com/en/sql-reference/organization-usage/snapshots.md

# Source: https://docs.snowflake.com/en/sql-reference/info-schema/snapshots.md

# Source: https://docs.snowflake.com/en/sql-reference/account-usage/snapshots.md

Schema:
:   [ACCOUNT_USAGE](../account-usage.md)

# SNAPSHOTS view — *Deprecated*

This Account Usage view provides information on [snapshots](../../user-guide/backups.md).

## Columns

| Column name | Data type | Description |
| --- | --- | --- |
| ID | VARCHAR | Snowflake-generated identifier of the snapshot.  Note: this is not the local ID, this is the globally unique UUID of the Snapshot. |
| SNAPSHOT_SET_ID | NUMBER | ID of snapshot set that contains the snapshot. |
| SNAPSHOT_SET_NAME | VARCHAR | Name of snapshot set that contains the snapshot. |
| SNAPSHOT_SET_SCHEMA_ID | NUMBER | ID of schema that the snapshot set belongs to. |
| SNAPSHOT_SET_SCHEMA | VARCHAR | Name of schema that the snapshot set belongs to. |
| SNAPSHOT_SET_CATALOG_ID | NUMBER | ID of database that the snapshot set belongs to. |
| SNAPSHOT_SET_CATALOG | VARCHAR | Name of database that the snapshot set belongs to. |
| CREATED | TIMESTAMP_LTZ | Timestamp at which snapshot was created. |
| DELETED | TIMESTAMP_LTZ | Timestamp at which the snapshot was deleted.  This column isn’t displayed by the SHOW command, because the SHOW command output doesn’t include deleted objects. |
| EXPIRATION_SCHEDULED_FOR | TIMESTAMP_LTZ | Timestamp at which snapshot will be expired and deleted. |
| IS_UNDER_LEGAL_HOLD | BOOLEAN | True if snapshot is under legal hold; False otherwise. |

## Usage notes

* Latency for the view may be up to 360 minutes (6 hours).
