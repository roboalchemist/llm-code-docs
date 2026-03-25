# Source: https://docs.snowflake.com/en/sql-reference/account-usage/postgres_storage_usage_history.md

Schema:
:   [ACCOUNT_USAGE](../account-usage.md)

# POSTGRES_STORAGE_USAGE_HISTORY view

This Account Usage view can be used to query the hourly storage used in byte-months for [Postgres instances](../../user-guide/snowflake-postgres/about.md)
in the account for the last 365 days (1 year). The data includes all data stored on the instance.

## Columns

The following table provides definitions for the POSTGRES_STORAGE_USAGE_HISTORY view columns.

| Column name | Data type | Description |
| --- | --- | --- |
| START_TIME | TIMESTAMP_LTZ | The date and beginning of the hour (in the local time zone) in which the usage took place. |
| END_TIME | TIMESTAMP_LTZ | The date and end of the hour (in the local time zone) in which the usage took place. |
| TOTAL_BYTE_MONTHS_STANDARD | NUMBER | Number of byte-months of standard storage used by Postgres instances. |
| TOTAL_BYTE_MONTHS_HA | NUMBER | Number of byte-months of high-availability storage used by Postgres instances. |

## Usage notes

* The maximum latency for this view is three hours.
* The POSTGRES_STORAGE_USAGE_HISTORY view and the Snowsight cost management tools can return different daily storage usage
  values. This discrepancy is caused by the methods used to determine storage usage. To determine these values, the
  POSTGRES_STORAGE_USAGE_HISTORY view uses the current session’s [TIMEZONE](../parameters.md) parameter and the Snowsight cost
  management tools use Coordinated Universal Time (UTC). To resolve any discrepancies, Snowflake recommends setting the TIMEZONE
  parameter to UTC.
