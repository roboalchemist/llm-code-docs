# Source: https://docs.snowflake.com/en/sql-reference/account-usage/block_storage_snapshots.md

Schema:
:   [ACCOUNT_USAGE](../account-usage.md)

# BLOCK_STORAGE_SNAPSHOTS view

This Account Usage view displays a row for each [block storage snapshot](../../developer-guide/snowpark-container-services/block-storage-volume.md) in the account.

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| SNAPSHOT_ID | NUMBER | ID of the snapshot. |
| SNAPSHOT_NAME | VARCHAR | Name of the snapshot. |
| DATABASE_ID | VARCHAR | Internal, Snowflake-generated identifier of the database that the snapshot belongs to. |
| DATABASE_NAME | VARCHAR | Name of the database that the snapshot belongs to. |
| SCHEMA_ID | NUMBER | Internal, Snowflake-generated identifier of the schema that the snapshot belongs to. |
| SCHEMA_NAME | VARCHAR | Name of the schema that the snapshot belongs to. |
| SERVICE_ID | NUMBER | ID of the service for which the snapshot is created. |
| SERVICE_NAME | VARCHAR | Name of the service for which the snapshot is created. |
| VOLUME _NAME | VARCHAR | Volume from the specified service for which the snapshot is created. |
| INSTANCE | NUMBER | ID of the service instance for which the snapshot is created. |
| SIZE | NUMBER | Size in GB of the snapshot. |
| ENCRYPTION | VARCHAR | [Encryption type of the volume](../../developer-guide/snowpark-container-services/block-storage-volume.md) from which the snapshot was created. |
| COMMENT | VARCHAR | General comment about the snapshot. |
| OWNER | VARCHAR | Role that owns the snapshot. |
| OWNER_ROLE_TYPE | VARCHAR | The type of role that owns the snapshot. |
| CREATED_ON | TIMESTAMP_LTZ | Creation time of the snapshot. |
| LAST_ALTERED_ON | TIMESTAMP_LTZ | Last altered time of the snapshot. |
| DELETED_ON | TIMESTAMP_LTZ | Deletion time of the snapshot. |

## Usage notes

* Latency for the view might be up to 180 minutes (3 hours).

## Example

```sqlexample
SELECT *
FROM SNOWFLAKE.ACCOUNT_USAGE.BLOCK_STORAGE_SNAPSHOTS;
```
