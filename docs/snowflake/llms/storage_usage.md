# Source: https://docs.snowflake.com/en/sql-reference/account-usage/storage_usage.md

Schemas:
:   [ACCOUNT_USAGE](../account-usage.md) , [READER_ACCOUNT_USAGE](../account-usage.md)

# STORAGE_USAGE view

This Account Usage view displays the average daily data storage usage, in bytes, within the last 365 days (1 year) across the entire account, including data in:

* Database tables.
* Files in all internal stages.

See also:
:   [DATABASE_STORAGE_USAGE_HISTORY view](database_storage_usage_history.md) , [STAGE_STORAGE_USAGE_HISTORY view](stage_storage_usage_history.md)

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| USAGE_DATE | DATE | Date of this storage usage record. The date is based on the local time zone. It is recommended that you change the query session to use the UTC time zone instead (for example, `ALTER SESSION SET TIMEZONE='UTC'`). |
| STORAGE_BYTES | NUMBER | Number of bytes of table storage used, including bytes currently in Time Travel. |
| STAGE_BYTES | NUMBER | Number of bytes of stage storage used by files in all internal stages (named, table, and user). |
| FAILSAFE_BYTES | NUMBER | Number of bytes of Fail-safe storage used. |
| HYBRID_TABLE_STORAGE_BYTES | NUMBER | Number of bytes of hybrid table storage used (data in the row store). |
| ARCHIVE_STORAGE_COOL_BYTES | NUMBER | Number of all bytes of table storage used in the COOL storage tier, including active bytes, Fail-safe bytes, Time Travel bytes, and bytes subject to [minimum storage duration charges](../../user-guide/storage-management/storage-lifecycle-policies-billing.md). |
| ARCHIVE_STORAGE_COLD_BYTES | NUMBER | Number of all bytes of table storage used in the COLD storage tier, including active bytes, Fail-safe bytes, Time Travel bytes, and bytes subject to [minimum storage duration charges](../../user-guide/storage-management/storage-lifecycle-policies-billing.md). |
| ARCHIVE_STORAGE_RETRIEVAL_TEMP_BYTES | NUMBER | Number of bytes used in the standard storage tier, during data retrieval from the COLD storage tier. |

## Usage notes

* In the ACCOUNT_USAGE schema, latency for the view is up to 120 minutes (2 hours).
* In the READER_ACCOUNT_USAGE schema, latency is up to 24 hours.
