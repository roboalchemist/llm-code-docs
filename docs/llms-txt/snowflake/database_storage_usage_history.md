# Source: https://docs.snowflake.com/en/sql-reference/organization-usage/database_storage_usage_history.md

# Source: https://docs.snowflake.com/en/sql-reference/account-usage/database_storage_usage_history.md

# Source: https://docs.snowflake.com/en/sql-reference/functions/database_storage_usage_history.md

Categories:
:   [Information Schema](../info-schema.md) , [Table functions](../functions-table.md)

# DATABASE_STORAGE_USAGE_HISTORY

This table function can be used to query the average daily storage usage, in bytes, for a single database (or all the databases in your account) within a specified date range. The results include:

* All data stored in tables and materialized views in the database(s).
* All historical data maintained in Fail-safe for the database(s).

> **Note:**
>
> This function returns storage usage within the last 6 months.

See also:
:   [STAGE_STORAGE_USAGE_HISTORY](stage_storage_usage_history.md) , [WAREHOUSE_METERING_HISTORY](warehouse_metering_history.md)

## Syntax

```sqlsyntax
DATABASE_STORAGE_USAGE_HISTORY(
      [ DATE_RANGE_START => <constant_expr> ]
      [, DATE_RANGE_END => <constant_expr> ]
      [, DATABASE_NAME => '<string>' ] )
```

## Arguments

All the arguments are optional.

`DATE_RANGE_START => constant_expr` , . `DATE_RANGE_END => constant_expr`
:   The date range, within the last 6 months, for which to retrieve database storage usage:

    * If an end date is not specified, [CURRENT_DATE](current_date.md) is used as the end of the range.
    * If a start date is not specified, `DATE_RANGE_END` is used as the start of the range (that is, the default is one day of storage usage).

    If the range falls outside the last 6 months, an error is returned.

`DATABASE_NAME => 'string'`
:   The name of the database to retrieve storage usage history for. Note that the database name must be enclosed in single quotes. Also, if the database name contains any spaces, mixed-case characters,
    or special characters, the name must be double-quoted within the single quotes (for example, `'"My DB"'` vs `'mydb'`).

    If no database is specified, data is returned for all the databases in your account.

## Usage notes

* Returns results only for the ACCOUNTADMIN role or any role that has been explicitly granted the MONITOR USAGE global privilege.
* To call an Information Schema table function, your session must have an INFORMATION_SCHEMA schema in use *or* the function name must be fully-qualified. For more details, see [Snowflake Information Schema](../info-schema.md).

## Output

The function returns the following columns:

| Column Name | Data Type | Description |
| --- | --- | --- |
| USAGE_DATE | DATE | Date of this storage usage record. |
| DATABASE_NAME | TEXT | Name of the database. |
| AVERAGE_DATABASE_BYTES | NUMBER | Number of bytes of database storage used, including bytes currently in Time Travel. |
| AVERAGE_FAILSAFE_BYTES | NUMBER | Number of bytes of Fail-safe storage used. |

If a database has been dropped and its data retention period has passed (that is, the database cannot be recovered using Time Travel), then the database name is reported as `DROPPED_id`, where `id` is an internally-generated identifier. This ID can be used to match entries across rows returned by the table function.

## Examples

Retrieve average daily storage usage for the past 10 days, per database, for all databases in your account:

```sqlexample
SELECT *
  FROM TABLE(INFORMATION_SCHEMA.DATABASE_STORAGE_USAGE_HISTORY(DATEADD('days',-10,CURRENT_DATE()),CURRENT_DATE()));
```
