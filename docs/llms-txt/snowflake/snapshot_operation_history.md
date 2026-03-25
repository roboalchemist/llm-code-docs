# Source: https://docs.snowflake.com/en/sql-reference/organization-usage/snapshot_operation_history.md

# Source: https://docs.snowflake.com/en/sql-reference/account-usage/snapshot_operation_history.md

Schema:
:   [ACCOUNT_USAGE](../account-usage.md)

# SNAPSHOT_OPERATION_HISTORY view — *Deprecated*

This Account Usage view provides information about the snapshot operations that were performed for
[snapshot sets](../../user-guide/backups.md).
Snowflake returns one row for each operation performed on snapshots within snapshot sets over the last year.

## Columns

| Column name | Data type | Description |
| --- | --- | --- |
| START_TIME | TIMESTAMP_LTZ | The timestamp at which the snapshot operation started. |
| END_TIME | TIMESTAMP_LTZ | The timestamp at which the snapshot operation ended. |
| SNAPSHOT_SET_ID | NUMBER | The local snapshot set ID. |
| SNAPSHOT_ID | VARCHAR | The unique identifier of snapshot being worked on. |
| OPERATION_TYPE | VARCHAR | Could be one of the below operations:   *CREATE* EXPIRE *RESTORE* ADD_LEGAL_HOLD * REMOVE_LEGAL_HOLD |
| Query_ID | VARCHAR | Internal system-generated identifier for the SQL statement. |

## Usage notes

* Latency for the view may be up to 360 minutes (6 hours).
* Snowflake retains the history data for 365 days (approximately one year).
