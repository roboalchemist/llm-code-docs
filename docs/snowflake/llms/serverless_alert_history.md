# Source: https://docs.snowflake.com/en/sql-reference/account-usage/serverless_alert_history.md

# Source: https://docs.snowflake.com/en/sql-reference/functions/serverless_alert_history.md

Categories:
:   [Information Schema](../info-schema.md) , [Table functions](../functions-table.md)

# SERVERLESS_ALERT_HISTORY

This table function is used for querying the [serverless alert](../../user-guide/alerts.md) usage history. The
information returned by the function includes the alert name and credits consumed by the execution of each alert.

See also:
:   [SERVERLESS_ALERT_HISTORY view (ACCOUNT_USAGE)](../account-usage/serverless_alert_history.md)

## Syntax

```sqlsyntax
SERVERLESS_ALERT_HISTORY(
  [ DATE_RANGE_START => <constant_expr> ]
  [ , DATE_RANGE_END => <constant_expr> ]
  [ , ALERT_NAME => '<string>' ] )
```

## Arguments

All of the arguments are optional.

`DATE_RANGE_START => constant_expr` , . `DATE_RANGE_END => constant_expr`
:   Date/time range of the usage window:

    * If an end date is not specified, then [CURRENT_DATE](current_date.md) is used as the end of the range.
    * If a start date is not specified, then the range starts 10 minutes prior to the start of `DATE_RANGE_END` (that is, the
      default is to show the previous 10 minutes of the usage history). For example, if `DATE_RANGE_END`
      is [CURRENT_DATE](current_date.md), then the default `DATE_RANGE_START` is 11:50 PM on the previous day.

`ALERT_NAME => string`
:   The name of the alert for which to retrieve usage history. Only the usage data for the specified alert is returned.

    Note that the alert name must be enclosed in single quotes. Also, if the alert name contains any spaces, mixed-case characters,
    or special characters, the name must be double-quoted within the single quotes (e.g. `'"My Alert"'` vs `'myalert'`).

## Usage notes

* The table function returns results only for the ACCOUNTADMIN role or any role that has been explicitly granted the MONITOR
  USAGE global privilege.

  > **Note:**
  >
  > A role with the MONITOR USAGE privilege can view per-object credit usage, but not object names.
* When you call an Information Schema table function, the session must have an INFORMATION_SCHEMA schema in use or the
  function name must be fully-qualified. For more details, see [Snowflake Information Schema](../info-schema.md).
* The history is displayed in increments of 1 hour.

## Output

The function returns the following columns:

| Column Name | Data Type | Description |
| --- | --- | --- |
| START_TIME | TIMESTAMP_LTZ | Start of the specified time range. |
| END_TIME | TIMESTAMP_LTZ | End of the specified time range. |
| ALERT_NAME | TEXT | Name of the alert. |
| CREDITS_USED | TEXT | Number of credits billed for serverless alert usage during the START_TIME and END_TIME window. |

## Examples

Retrieve the usage history for a one-hour range for your account:

```sqlexample
SELECT *
  FROM TABLE(INFORMATION_SCHEMA.SERVERLESS_ALERT_HISTORY(
    DATE_RANGE_START=>'2024-10-08 19:00:00.000 -0700',
    DATE_RANGE_END=>'2024-10-08 20:00:00.000 -0700'));
```

Sample output:

```output
+-------------------------------+-------------------------------+------------+--------------+
| START_TIME                    | END_TIME                      | ALERT_NAME | CREDITS_USED |
|-------------------------------+-------------------------------+------------+--------------|
| 2024-10-08 04:16:22.000 -0700 | 2024-10-08 05:16:22.000 -0700 | A1         |  0.000286714 |
| 2024-10-08 05:16:22.000 -0700 | 2024-10-08 06:16:22.000 -0700 | A1         |  0.007001568 |
+-------------------------------+-------------------------------+------------+--------------+
```

Retrieve the history for the last 12 hours for your account:

```sqlexample
SELECT *
  FROM TABLE(INFORMATION_SCHEMA.SERVERLESS_ALERT_HISTORY(
    DATE_RANGE_START=>DATEADD(H, -12, CURRENT_TIMESTAMP)));
```

Retrieve the history for the past week for your account:

```sqlexample
SELECT *
  FROM TABLE(INFORMATION_SCHEMA.SERVERLESS_ALERT_HISTORY(
    DATE_RANGE_START=>DATEADD(D, -7, CURRENT_DATE),
    DATE_RANGE_END=>CURRENT_DATE));
```

Retrieve the usage history for the past week for a specified alert in your account:

```sqlexample
SELECT *
  FROM TABLE(INFORMATION_SCHEMA.SERVERLESS_ALERT_HISTORY(
    DATE_RANGE_START=>DATEADD(D, -7, CURRENT_DATE),
    DATE_RANGE_END=>CURRENT_DATE,
    ALERT_NAME=>'my_database.my_schema.my_alert'));
```
