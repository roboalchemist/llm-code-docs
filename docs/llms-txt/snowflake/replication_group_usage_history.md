# Source: https://docs.snowflake.com/en/sql-reference/organization-usage/replication_group_usage_history.md

# Source: https://docs.snowflake.com/en/sql-reference/account-usage/replication_group_usage_history.md

# Source: https://docs.snowflake.com/en/sql-reference/functions/replication_group_usage_history.md

Categories:
:   [Information Schema](../info-schema.md) , [Table functions](../functions-table.md)

# REPLICATION_GROUP_USAGE_HISTORY

Returns the replication usage history for secondary replication or failover groups within the last 14 days.

## Syntax

```sqlsyntax
REPLICATION_GROUP_USAGE_HISTORY(
   [ DATE_RANGE_START => <constant_expr> ]
   [, DATE_RANGE_END => <constant_expr> ]
   [, REPLICATION_GROUP_NAME => '<string>' ] )
```

## Arguments

All the arguments are optional.

`DATE_RANGE_START => constant_expr` , . `DATE_RANGE_END => constant_expr`
:   The date/time range, within the last 2 weeks, for which to retrieve the data load history:

    * If an end date is not specified, then [CURRENT_TIMESTAMP](current_timestamp.md) is used as the end of the range.
    * If a start date is not specified, then the range starts 12 hours prior to the `DATE_RANGE_END`

`REPLICATION_GROUP_NAME => string`
:   A string specifying a replication or failover group. Only replication operations for the specified group are returned.

## Output

The function returns the following columns:

| Column Name | Data Type | Description |
| --- | --- | --- |
| START_TIME | TIMESTAMP_LTZ | Start of the specified time range. |
| END_TIME | TIMESTAMP_LTZ | End of the specified time range. |
| REPLICATION_GROUP_NAME | TEXT | Name of the replication group. |
| CREDITS_USED | TEXT | Number of credits billed for replication during the START_TIME and END_TIME window. |
| BYTES_TRANSFERRED | NUMBER | Number of bytes transferred for replication during the START_TIME and END_TIME window. |

## Usage notes

* Returns results only for the ACCOUNTADMIN role or any role that has been explicitly granted the MONITOR USAGE global privilege.
* Returns results only for a secondary replication or failover group in the current account.
* When calling an Information Schema table function, the session must have an INFORMATION_SCHEMA schema in use or the function name
  must be fully-qualified. For more details, see [Snowflake Information Schema](../info-schema.md).

## Examples

Retrieve the replication usage history for the last 7 days:

> ```sqlexample
> SELECT START_TIME, END_TIME, REPLICATION_GROUP_NAME, CREDITS_USED, BYTES_TRANSFERRED
>   FROM TABLE(information_schema.replication_group_usage_history(date_range_start=>dateadd('day', -7, current_date())));
> ```

Retrieve the replication usage history for the last 7 days for replication group `myrg`:

> ```sqlexample
> SELECT START_TIME, END_TIME, REPLICATION_GROUP_NAME, CREDITS_USED, BYTES_TRANSFERRED
>   FROM TABLE(information_schema.replication_group_usage_history(
>     date_range_start => dateadd('day', -7, current_date()),
>     replication_group_name => 'myrg'
> ));
> ```
