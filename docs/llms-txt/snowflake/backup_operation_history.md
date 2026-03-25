# Source: https://docs.snowflake.com/en/sql-reference/organization-usage/backup_operation_history.md

# Source: https://docs.snowflake.com/en/sql-reference/account-usage/backup_operation_history.md

Schema:
:   [ACCOUNT_USAGE](../account-usage.md)

# BACKUP_OPERATION_HISTORY view

This Account Usage view provides information about the backup operations that were performed for
[backup sets](../../user-guide/backups.md).
Snowflake returns one row for each operation performed on backups within backup sets over the last year.

## Columns

| Column name | Data type | Description |
| --- | --- | --- |
| START_TIME | TIMESTAMP_LTZ | The timestamp at which the backup operation started. |
| END_TIME | TIMESTAMP_LTZ | The timestamp at which the backup operation ended. |
| BACKUP_SET_ID | NUMBER | The local backup set ID. |
| BACKUP_ID | VARCHAR | The unique identifier of backup being worked on. |
| OPERATION_TYPE | VARCHAR | Could be one of the below operations:   *CREATE* EXPIRE *RESTORE* ADD_LEGAL_HOLD * REMOVE_LEGAL_HOLD |
| Query_ID | VARCHAR | Internal system-generated identifier for the SQL statement. |

## Usage notes

* Latency for the view may be up to 360 minutes (6 hours).
* Snowflake retains the history data for 365 days (approximately one year).
