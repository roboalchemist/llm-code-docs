# Source: https://docs.snowflake.com/en/sql-reference/functions/dmf_blank_percent.md

Categories:
:   [Data metric functions](../functions-data-metric.md)

# BLANK_PERCENT (system data metric function)

Returns the percentage of column values that are blank for the specified column in a table.

This topic provides the syntax for calling the function directly. To learn how to associate the function with a table or view so it
runs at regular intervals, see [Associate a DMF](../../user-guide/data-quality-working.md).

## Syntax

```sqlsyntax
SNOWFLAKE.CORE.BLANK_PERCENT(<query>)
```

## Arguments

`query`
:   Specifies a SQL query that projects a single column.

## Allowed data types

The column projected by the `query` must have the VARCHAR data type.

## Returns

The function returns a NUMBER value.

## Example

Measure the percentage of blank fields for the SSN column (US social security number):

> ```sqlexample
> SELECT SNOWFLAKE.CORE.BLANK_PERCENT(
>   SELECT
>     ssn
>   FROM hr.tables.empl_info
> );
> ```
>
> ```output
> +-------------------------------------------------------------------+
> | SNOWFLAKE.CORE.BLANK_PERCENT(SELECT ssn FROM hr.tables.empl_info) |
> +-------------------------------------------------------------------+
> | 1                                                                 |
> +-------------------------------------------------------------------+
> ```
