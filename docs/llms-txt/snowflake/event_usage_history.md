# Source: https://docs.snowflake.com/en/sql-reference/account-usage/event_usage_history.md

Schema:
:   [ACCOUNT_USAGE](../account-usage.md)

# EVENT_USAGE_HISTORY view

This view can be used to query the history of data loaded into Snowflake event tables within the last 365 days (1 year).

The view displays the history of data loaded and credits billed for your entire Snowflake account.

For more information about event tables, refer to [Event table overview](../../developer-guide/logging-tracing/event-table-setting-up.md).

For more information about logging and tracing, refer to [Logging, tracing, and metrics](../../developer-guide/logging-tracing/logging-tracing-overview.md).

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| START_TIME | TIMESTAMP_LTZ | Start of the time range (in the UTC time zone) in which data loading took place. |
| END_TIME | TIMESTAMP_LTZ | End of the time range (in the UTC time zone) in which data loading took place. |
| CREDITS_USED | NUMBER | Number of credits billed for loading data into the event table during the START_TIME and END_TIME window. |
| BYTES_INGESTED | NUMBER | Number of bytes of data loaded during the START_TIME and END_TIME window. |

## Usage notes

Latency for the view may be up to 180 minutes (3 hours).
