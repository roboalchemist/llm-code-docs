# Source: https://docs.snowflake.com/en/sql-reference/account-usage/data_quality_monitoring_usage_history.md

Schema:
:   [ACCOUNT_USAGE](../account-usage.md)

# DATA_QUALITY_MONITORING_USAGE_HISTORY view

The DATA_QUALITY_MONITORING_USAGE_HISTORY view in the ACCOUNT_USAGE schema records the daily credit consumption for data metric function
evaluations on tables in an account within the last 365 days (1 year).

See also:
:   [Introduction to data quality checks](../../user-guide/data-quality-intro.md)

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| START_TIME | TIMESTAMP_LTZ | Start of the specified time range. |
| END_TIME | TIMESTAMP_LTZ | End of the specified time range. |
| CREDITS_USED | NUMBER | Number of credits billed for data metric function evaluations on the table. |
| TABLE_ID | NUMBER | Internal/system-generated identifier for the table monitored by data metric functions. |
| TABLE_NAME | VARCHAR | Name of the table. |
| SCHEMA_ID | NUMBER | Internal/system-generated identifier for the schema that stores the table. |
| SCHEMA_NAME | VARCHAR | Name of the schema that stores the table. |
| DATABASE_ID | NUMBER | Internal/system-generated identifier for the database that stores the table. |
| DATABASE_NAME | VARCHAR | Name of the database that stores the table. |

## Usage notes

Latency for the view may be up to 180 minutes (3 hours).
