# Source: https://docs.snowflake.com/en/sql-reference/functions/dmf_stddev.md

Categories:
:   [Data metric functions](../functions-data-metric.md)

# STDDEV (system data metric function)

Returns the standard deviation value for the specified column in a table.

The STDDEV system data metric function is optimized to calculate the standard deviation for a single column and provides greater
performance when compared to calling the [STDDEV](stddev.md) function.

This topic provides the syntax for calling the function directly. To learn how to associate the function with a table or view so it
runs at regular intervals, see [Associate a DMF](../../user-guide/data-quality-working.md).

## Syntax

```sqlsyntax
SNOWFLAKE.CORE.STDDEV(<query>)
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

Measure the standard deviation value for the `salary` column in a table:

```sqlexample
SELECT SNOWFLAKE.CORE.STDDEV(
  SELECT
    salary
  FROM hr.tables.empl_info
);
```

```output
+------------------------------+
|       SNOWFLAKE.CORE.STDDEV( |
|                       SELECT |
|                       SALARY |
|     FROM HR.TABLES.EMPL_INFO |
|                            ) |
|------------------------------|
|               8407.615595399 |
+------------------------------+
```
