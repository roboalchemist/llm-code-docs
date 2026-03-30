# Source: https://docs.snowflake.com/en/sql-reference/functions/dmf_min.md

Categories:
:   [Data metric functions](../functions-data-metric.md)

# MIN (system data metric function)

Returns the minimum value for the specified column in a table.

The MIN system data metric function is optimized to calculate the minimum value for a single column and provides greater performance when
compared to calling the [MIN](min.md) function.

This topic provides the syntax for calling the function directly. To learn how to associate the function with a table or view so it
runs at regular intervals, see [Associate a DMF](../../user-guide/data-quality-working.md).

## Syntax

```sqlsyntax
SNOWFLAKE.CORE.MIN(<query>)
```

## Arguments

`query`
:   Specifies a SQL query that projects a single column.

## Allowed data types

The column projected by the `query` must have one of the following data types:

* FLOAT
* NUMBER

## Returns

The function returns either a NUMBER or FLOAT value.

## Example

Measure the minimum value for the SALARY column in a table:

```sqlexample
SELECT SNOWFLAKE.CORE.MIN(
  SELECT
    salary
  FROM hr.tables.empl_info
);
```

```output
+------------------------------------------------------------+
| SNOWFLAKE.CORE.MIN(SELECT salary FROM hr.tables.empl_info) |
+------------------------------------------------------------+
| 60000                                                      |
+------------------------------------------------------------+
```
