# Source: https://docs.snowflake.com/en/sql-reference/functions/replication_group_refresh_history.md

# Source: https://docs.snowflake.com/en/sql-reference/organization-usage/replication_group_refresh_history.md

# Source: https://docs.snowflake.com/en/sql-reference/account-usage/replication_group_refresh_history.md

Schema:
:   [ACCOUNT_USAGE](../account-usage.md)

# REPLICATION_GROUP_REFRESH_HISTORY view

This Account Usage view can be used to query the refresh history for a specified
[replication or failover group](../../user-guide/account-replication-intro.md).

See also:
:   [REPLICATION_GROUP_REFRESH_HISTORY, REPLICATION_GROUP_REFRESH_HISTORY_ALL](../functions/replication_group_refresh_history.md) (Information Schema table function)

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| REPLICATION_GROUP_NAME | VARCHAR | Name of the secondary replication or failover group. |
| REPLICATION_GROUP_ID | NUMBER | Internal/system-generated identifier for the replication or failover group. |
| PHASE_NAME | VARCHAR | Current phase in the replication operation. For the list of phases, see the Usage notes. |
| START_TIME | TIMESTAMP_LTZ | Time when the replication operation began. |
| END_TIME | TIMESTAMP_LTZ | Time when the replication operation finished, if applicable. `NULL` if it is in progress. |
| JOB_UUID | VARCHAR | Query ID for the refresh job. |
| TOTAL_BYTES | VARIANT | A JSON object that provides detailed information about refreshed databases:   *`totalBytesToReplicate`: Total number of bytes expected to be replicated.* `bytesUploaded`: Actual number of bytes uploaded. *`bytesDownloaded`: Actual number of bytes downloaded.* `databases`: List of JSON objects containing the following fields for each member database:    + `name`: Name of the database.   + `totalBytesToReplicate`: Total bytes expected to be replicated for the database. |
| OBJECT_COUNT | VARIANT | A JSON object that provides detailed information about refreshed objects:   *`totalObjects`: Total number of objects in the replication or failover group.* `completedObjects`: Total number of objects completed. * `objectTypes`: List of JSON objects containing the following fields for each type:    + `objectType`: Type of object (for example users, roles, grants, warehouses, schemas, tables, columns, etc).   + `totalObjects`: Total number of objects of this type in the replication or failover group.   + `completedObjects`: Total number of objects of this type that were completed. |
| PRIMARY_SNAPSHOT_TIMESTAMP | TIMESTAMP_LTZ | Timestamp when the primary snapshot was created. |
| ERROR | VARIANT | NULL if the refresh operation is successful. If the refresh operation fails, returns a JSON object that provides detailed information about the error:   *`errorCode`: Error code of the failure.* `errorMessage`: Error message of the failure. |

## Usage notes

* Latency for the view may be up to 180 minutes (three hours).

  To view real-time refresh progress, use the [REPLICATION_GROUP_REFRESH_HISTORY, REPLICATION_GROUP_REFRESH_HISTORY_ALL](../functions/replication_group_refresh_history.md) table function.

* Results are only returned for secondary failover or replication groups in the current account (the target account).
* The following is the list of phases in the order processed:

  | # | Phase name | Description |
  | --- | --- | --- |
  | 1 | `SECONDARY_SYNCHRONIZING_MEMBERSHIP` | The secondary replication or failover group receives information from the primary group about the objects included in the group, and updates its membership metadata. |
  | 2 | `SECONDARY_UPLOADING_INVENTORY` | The secondary replication or failover group sends an inventory of its objects in the target account to the primary group. |
  | 3 | `PRIMARY_UPLOADING_METADATA` | The primary replication or failover group creates a snapshot of metadata in the source account and sends it to the secondary group. |
  | 4 | `PRIMARY_UPLOADING_DATA` | The primary replication or failover group copies the files the secondary group needs to reconcile any deltas between the objects in the source and target accounts. |
  | 5 | `SECONDARY_DOWNLOADING_METADATA` | The secondary replication or failover group applies the snapshot of the metadata that was sent by the primary. The metadata updates are not applied atomically and instead applied over time. |
  | 6 | `SECONDARY_DOWNLOADING_DATA` | The secondary replication or failover group copies the files sent by the primary group to the target account. |
  | 7 | `COMPLETED` / `FAILED` / `CANCELED` | Refresh operation status. |

## Examples

To retrieve the refresh history for the secondary failover group `myfg`, execute the following statement:

```sqlexample
SELECT phase_name, start_time, end_time,
       total_bytes, object_count, error
  FROM SNOWFLAKE.ACCOUNT_USAGE.REPLICATION_GROUP_REFRESH_HISTORY
  WHERE replication_group_name = 'MYFG';
```

To retrieve the last refresh record for each replication or failover group, execute the following statement:

```sqlexample
SELECT replication_group_name, phase_name,
       start_time, end_time,
       total_bytes, object_count, error,
       ROW_NUMBER() OVER (
         PARTITION BY replication_group_name
         ORDER BY end_time DESC
       ) AS row_num
  FROM SNOWFLAKE.ACCOUNT_USAGE.REPLICATION_GROUP_REFRESH_HISTORY
  QUALIFY row_num = 1;
```
