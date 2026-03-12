# Source: https://docs.snowflake.com/en/sql-reference/account-usage/archive_storage_data_retrieval_usage_history.md

Schema:
:   [ACCOUNT_USAGE](../account-usage.md)

# ARCHIVE_STORAGE_DATA_RETRIEVAL_USAGE_HISTORY view

This Account Usage view displays a history of archived data retrieval (in bytes) for your
account over the past 12 months (one year).

## Columns

| Column name | Data type | Description |
| --- | --- | --- |
| START_TIME | TIMESTAMP_LTZ | The date and beginning of the hour (in the local time zone) in which the usage took place. |
| END_TIME | TIMESTAMP_LTZ | The date and end of the hour (in the local time zone) in which the usage took place. |
| OBJECT_TYPE | VARCHAR | The type of the retrieved object; for example, `TABLE`. |
| OBJECT_ID | NUMBER | Internal or system-generated identifier for the retrieved object. |
| OBJECT_NAME | VARCHAR | Name of the retrieved object. |
| SCHEMA_ID | NUMBER | Internal, Snowflake-generated identifier of the schema for the retrieved object. |
| SCHEMA_NAME | VARCHAR | Name of the schema for the retrieved object. |
| DATABASE_ID | NUMBER | Internal, Snowflake-generated identifier of the database for the retrieved object. |
| DATABASE_NAME | VARCHAR | Name of the database for the retrieved object. |
| BYTES | NUMBER | Bytes retrieved from archive storage. |
| ARCHIVE_STORAGE_TIER | VARCHAR | The archive storage tier from which Snowflake retrieved the object; for example, `COOL` or `COLD`. |

## Usage notes

* Latency for the view is up to 1 hour.
* The view contains historical data for the past 12 months (one year).
* For cost information related to data retrieval from archive storage,
  see [billing for storage lifecycle policies](../../user-guide/storage-management/storage-lifecycle-policies-billing.md).
