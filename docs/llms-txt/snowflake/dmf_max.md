# Source: https://docs.snowflake.com/en/sql-reference/functions/dmf_max.md

Categories:
:   [Data metric functions](../functions-data-metric.md)

# MAX (system data metric function)

Returns the maximum value for the specified column in a table.

The MAX system data metric function is optimized to calculate the maximum value for a single column and provides greater performance when
compared to calling the [MAX](max.md) function.

This topic provides the syntax for calling the function directly. To learn how to associate the function with a table or view so it
runs at regular intervals, see [Associate a DMF](../../user-guide/data-quality-working.md).

## Syntax

```sqlsyntax
SNOWFLAKE.CORE.MAX(<query>)
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

Measure the maximum value for the `salary` column in a table:

```sqlexample
SELECT SNOWFLAKE.CORE.MAX(
  SELECT
    salary
  FROM hr.tables.empl_info);
```

```output
+------------------------------------------------------------+
| SNOWFLAKE.CORE.MAX(SELECT salary FROM hr.tables.empl_info) |
+------------------------------------------------------------+
| 325000                                                     |
+------------------------------------------------------------+
```
