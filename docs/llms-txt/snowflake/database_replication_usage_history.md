# Source: https://docs.snowflake.com/en/sql-reference/account-usage/database_replication_usage_history.md

# Source: https://docs.snowflake.com/en/sql-reference/functions/database_replication_usage_history.md

Categories:
:   [Information Schema](../info-schema.md) , [Table functions](../functions-table.md)

# DATABASE_REPLICATION_USAGE_HISTORY

This table function can be used to query the replication history for a specified database within a specified date range. The information
returned by the function includes the database name, credits consumed, and bytes transferred for replication.

> **Note:**
>
> This function returns database replication usage activity within the last 14 days.

## Syntax

```sqlsyntax
DATABASE_REPLICATION_USAGE_HISTORY(
  [ DATE_RANGE_START => <constant_expr> ]
  [ , DATE_RANGE_END => <constant_expr> ]
  [ , DATABASE_NAME => '<string>' ] )
```

## Arguments

All the arguments are optional.

`DATE_RANGE_START => constant_expr` , . `DATE_RANGE_END => constant_expr`
:   The date/time range to display the database replication history:

    * If an end date is not specified, then [CURRENT_DATE](current_date.md) is used as the end of the range.
    * If a start date is not specified, then the range starts 10 minutes prior to the start of `DATE_RANGE_END` (i.e. the default
      is to show the previous 10 minutes of history).

    For example, if `DATE_RANGE_END` is CURRENT_DATE, then the default `DATE_RANGE_START` is 11:50 PM on the previous day.

`DATABASE_NAME => 'string'`
:   Database name. If specified, only shows the history for the specified database.

    If a name is not specified, then the results include the data for each database replicated within the specified time range.

## Output

The function returns the following elements in a JSON object:

| Column Name | Data Type | Description |
| --- | --- | --- |
| START_TIME | TIMESTAMP_LTZ | Start of the specified time range. |
| END_TIME | TIMESTAMP_LTZ | End of the specified time range. |
| DATABASE_NAME | TEXT | Name of the database. |
| CREDITS_USED | TEXT | Number of credits billed for database replication during the START_TIME and END_TIME window. |
| BYTES_TRANSFERRED | NUMBER | Number of bytes transferred for database replication during the START_TIME and END_TIME window. |

## Usage notes

* Returns results only for the ACCOUNTADMIN role or any role that has been explicitly granted the MONITOR USAGE global privilege.
* When calling an Information Schema table function, the session must have an INFORMATION_SCHEMA schema in use or the function name must be fully-qualified. For more details, see
  [Snowflake Information Schema](../info-schema.md).

## Examples

Retrieve the replication history for a 30 minute range for your account:

> ```sqlexample
> select database_name, credits_used, bytes_transferred
>   from table(information_schema.database_replication_usage_history(
>     date_range_start=>'2023-03-28 12:00:00.000 +0000',
>     date_range_end=>'2023-03-28 12:30:00.000 +0000'));
> ```

Retrieve the history for the last 12 hours for your account:

> ```sqlexample
> select database_name, credits_used, bytes_transferred
>   from table(information_schema.database_replication_usage_history(
>     date_range_start=>dateadd(H, -12, current_timestamp)));
> ```

Retrieve the history for the past week for your account:

> ```sqlexample
> select start_time, end_time, database_name, credits_used, bytes_transferred
>   from table(information_schema.database_replication_usage_history(
>     date_range_start=>dateadd(d, -7, current_date),
>     date_range_end=>current_date));
> ```

Retrieve the replication history for the past week for database `mydb` in your account:

> ```sqlexample
> select start_time, end_time, database_name, credits_used, bytes_transferred
>   from table(information_schema.database_replication_usage_history(
>     date_range_start=>dateadd(d, -7, current_date),
>     date_range_end=>current_date,
>     database_name=>'mydb'));
> ```
