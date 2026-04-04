# Source: https://docs.snowflake.com/en/sql-reference/account-usage/hybrid_table_usage_history.md

Schema:
:   [ACCOUNT_USAGE](../account-usage.md)

# HYBRID_TABLE_USAGE_HISTORY view

> **Note:**
>
> As of March 1, 2026, Snowflake no longer bills customers for hybrid table requests;
> however, you can still query this view to see historical consumption data.
> Any new data in the view as of March 1, 2026, will not be billed to customers.

This Account Usage view displays consumption of hybrid table requests
(serverless compute resources), in terms of credits billed for
your entire Snowflake account, within the last 365 days (1 year).

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| OBJECT_TYPE | TEXT | Type of object referenced for scope of consumption: `ACCOUNT` for hybrid tables in your account. |
| OBJECT_ID | NUMBER | Internal identifier of object referenced for scope of consumption: `NULL` because scope of consumption for hybrid tables is tracked at the account level. |
| OBJECT_NAME | TEXT | Name of object referenced for scope of consumption: `NULL` because scope of consumption for hybrid tables is tracked at the account level. |
| START_TIME | TIMESTAMP_LTZ | Date and start time (in the local time zone) when usage of hybrid tables occurred. |
| END_TIME | TIMESTAMP_LTZ | Date and end time (in the local time zone) when usage of hybrid tables occurred. |
| CREDITS_USED | NUMBER | Number of credits used for hybrid table requests between the values for `START_TIME` and `END_TIME`. |

## Usage notes

* Latency for the view may be up to 180 minutes (3 hours).
* This view may return usage data that is slightly inconsistent with metrics
  returned in [METERING_DAILY_HISTORY view](metering_daily_history.md) and
  [METERING_HISTORY view](metering_history.md). The discrepancy in the
  calculation of credits used is due to rounding during division.

## Examples

The following queries return the total number of credits used by hybrid tables in your
account over specific periods of time.

The first query returns credits used for all time (the past year):

```sqlexample
SELECT SUM(credits_used) AS total_credits
  FROM SNOWFLAKE.ACCOUNT_USAGE.HYBRID_TABLE_USAGE_HISTORY;
```

The second query returns credits used over the past 5 days. Alternatively, you could specify some number
of weeks or months:

```sqlexample
SELECT SUM(credits_used) AS total_credits
  FROM SNOWFLAKE.ACCOUNT_USAGE.HYBRID_TABLE_USAGE_HISTORY
  WHERE start_time >= DATEADD(day, -5, CURRENT_TIMESTAMP());
```
