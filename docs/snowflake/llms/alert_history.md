# Source: https://docs.snowflake.com/en/sql-reference/organization-usage/alert_history.md

# Source: https://docs.snowflake.com/en/sql-reference/account-usage/alert_history.md

# Source: https://docs.snowflake.com/en/sql-reference/functions/alert_history.md

Categories:
:   [Information Schema](../info-schema.md) , [Table functions](../functions-table.md)

# ALERT_HISTORY

This INFORMATION_SCHEMA table function can be used to query the history of [alerts](../../user-guide/alerts.md) within a specified
date range. The function returns the history of alerts for your entire Snowflake account or a specified alert.

You can also access this information through the ALERT_HISTORY view in the ACCOUNT_USAGE schema. For details on the differences
between the view and table function, refer to [Differences between Account Usage and Information Schema](../account-usage.md).

> **Note:**
>
> This function returns alert executions within the last 7 days or the next scheduled execution within the next 8 days.

## Syntax

```sqlsyntax
ALERT_HISTORY(
      [ SCHEDULED_TIME_RANGE_START => <constant_expr> ]
      [, SCHEDULED_TIME_RANGE_END => <constant_expr> ]
      [, RESULT_LIMIT => <integer> ]
      [, ALERT_NAME => '<string>' ] )
```

## Arguments

All the arguments are optional.

`SCHEDULED_TIME_RANGE_START => constant_expr` , . `SCHEDULED_TIME_RANGE_END => constant_expr`
:   Time range (in TIMESTAMP_LTZ format), within the last 7 days, in which the evaluation of the condition for the alert was
    scheduled.

    * If `SCHEDULED_TIME_RANGE_END` is not specified, the function returns those alerts that have already completed, are
      currently running, or are scheduled in the future.
    * If `SCHEDULED_TIME_RANGE_END` is [CURRENT_TIMESTAMP](current_timestamp.md), the function returns those alerts
      that have already completed or are currently running. Note that an alert that is executed immediately prior to the current
      time may still be identified as scheduled.

    > **Note:**
    >
    > If no start or end time is specified, the most recent alerts are returned, up to the specified RESULT_LIMIT value.

    If the time range does not fall within the last 7 days, an error is returned.

`RESULT_LIMIT => integer`
:   A number specifying the maximum number of rows returned by the function.

    If the number of matching rows is greater than this limit, the alert executions with the most recent timestamp are returned, up
    to the specified limit.

    Range: `1` to `10000`

    Default: `100`.

`ALERT_NAME => string`
:   A case-insensitive string specifying an alert. Only non-qualified alert names are supported. Only executions of the specified
    alert are returned. Note that if multiple alerts have the same name, the function returns the history for each of these alerts.

## Usage notes

* Returns results only for the ACCOUNTADMIN role, the alert owner (i.e. the role with the OWNERSHIP privilege on the alert).
* This function returns a maximum of 10,000 rows, set in the `RESULT_LIMIT` argument value. The default value is `100`.

  Note that when the ALERT_HISTORY function is queried, its alert name, time range, and result limit arguments are applied
  first followed by the WHERE and LIMIT clause, respectively, if specified. In addition, the ALERT_HISTORY function
  returns records in descending SCHEDULED_TIME order. Alerts that are completed (i.e. with a SUCCEEDED, FAILED, or CANCELLED
  state) tend to be scheduled earlier, so they are generally returned later in order in the search results.

  In practice, if you have many alerts running in your account, the results returned by the function could include fewer than
  expected completed alerts or only scheduled alerts, especially if the RESULT_LIMIT value is relatively low. To query the history
  of alerts that have already run, Snowflake recommends using a combination of the
  `SCHEDULED_TIME_RANGE_START => constant_expr` and/or `SCHEDULED_TIME_RANGE_END => constant_expr` arguments.
* When calling an Information Schema table function, the session must have an INFORMATION_SCHEMA schema in use or the
  function name must be fully-qualified. For more details, see [Snowflake Information Schema](../info-schema.md).
* This function can return all executions run in the past 7 days or the next scheduled execution within the next 8 days.

## Output

The ALERT_HISTORY table function produces one row for each alert execution. Each row contains the following columns:

| Column Name | Data Type | Description |
| --- | --- | --- |
| NAME | VARCHAR | Name of the alert. |
| DATABASE_NAME | VARCHAR | Name of the database that contains the alert. |
| SCHEMA_NAME | VARCHAR | Name of the schema that contains the alert. |
| CONDITION | VARCHAR | The text of the SQL statement that serves as the condition for the alert. |
| CONDITION_QUERY_ID | VARCHAR | Internal/system-generated identifier for the SQL statement executed as the condition of the alert. |
| ACTION | VARCHAR | The text of the SQL statement that serves as the action for the alert. |
| ACTION_QUERY_ID | VARCHAR | Internal/system-generated identifier for the SQL statement executed as the action of the alert. |
| STATE | VARCHAR | Status of the alert. This can be one of the following:   *SCHEDULED: The alert will execute at the time specified by the SCHEDULED_TIME column. This status does not apply to   [alerts on new data](../../user-guide/alerts.md).* EXECUTING: The condition or action of the alert is currently executing. *FAILED: The alert failed. Either the alert condition or alert action encountered an error that prevented it from being   executed.* CANCELLED: The alert execution was cancelled (e.g. when the alert is suspended). *CONDITION_FALSE: The condition was evaluated successfully but returned no data. As a result, the action was not executed.   This status does not apply to [alerts on new data](../../user-guide/alerts.md).* CONDITION_FAILED: The evaluation of the condition failed. For details on the failure, check the SQL_ERROR_CODE and   SQL_ERROR_MESSAGE columns. *ACTION_FAILED: The condition was evaluated successfully, but the execution of the action failed. For details on the   failure, check the SQL_ERROR_CODE and SQL_ERROR_MESSAGE columns.* TRIGGERED: The condition was evaluated successfully, and the action was executed successfully. |
| SQL_ERROR_CODE | NUMBER | Error code, if the alert returned an error or failed to execute (e.g. if the current user did not have privileges to execute the alert). |
| SQL_ERROR_MESSAGE | VARCHAR | Error message, if the alert returned an error. |
| SCHEDULED_TIME | TIMESTAMP_LTZ | Time when the scheduled alert is/was scheduled to start running.  Note that we make a best effort to ensure absolute precision, but only guarantee that alerts do not execute *before* the scheduled time. |
| COMPLETED_TIME | TIMESTAMP_LTZ | Time when the alert completed, or NULL if SCHEDULED_TIME is in the future or if the alert is still running. |
| SCHEDULED_FROM | VARCHAR | Specifies what initiated the alert. The column contains one of the following values:   *`SCHEDULE`: The alert was scheduled to run normally, as described in the SCHEDULE clause of   [CREATE ALERT](../sql/create-alert.md).* `EXECUTE ALERT`: The alert was scheduled to run using [EXECUTE ALERT](../sql/execute-alert.md). * `TRIGGER`: The [alert on new data](../../user-guide/alerts.md) was run because the underlying table or view   contains new data. |

## Examples

See [Monitoring the execution of alerts](../../user-guide/alerts.md).
