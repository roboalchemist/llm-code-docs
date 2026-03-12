# Source: https://docs.snowflake.com/en/sql-reference/functions/dmf_avg.md

Categories:
:   [Data metric functions](../functions-data-metric.md)

# AVG (system data metric function)

Returns the average value for the specified column in a table.

The AVG system data metric function is optimized to calculate the average value for a single column and provides greater performance when
compared to calling the [AVG](avg.md) function.

This topic provides the syntax for calling the function directly. To learn how to associate the function with a table or view so it
runs at regular intervals, see [Associate a DMF](../../user-guide/data-quality-working.md).

## Syntax

```sqlsyntax
SNOWFLAKE.CORE.AVG(<query>)
```

## Arguments

`query`
:   Specifies a SQL query that projects a single column.

## Allowed data types

The column projected by the `query` must have one of the following data types:

* FLOAT
* NUMBER

## Returns

The function returns a NUMBER value.

## Example

Measure the average value for the `salary` column in a table:

```sqlexample
SELECT SNOWFLAKE.CORE.AVG(
  SELECT
    salary
  FROM hr.tables.empl_info
);
```

```output
+------------------------------------------------------------+
| SNOWFLAKE.CORE.AVG(SELECT salary FROM hr.tables.empl_info) |
+------------------------------------------------------------+
| 137000                                                     |
+------------------------------------------------------------+
```
