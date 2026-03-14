# Source: https://docs.snowflake.com/en/sql-reference/functions/dmf_null_percent.md

Categories:
:   [Data metric functions](../functions-data-metric.md)

# NULL_PERCENT (system data metric function)

Returns the percentage of columns values that are NULL for the specified column in a table.

This topic provides the syntax for calling the function directly. To learn how to associate the function with a table or view so it
runs at regular intervals, see [Associate a DMF](../../user-guide/data-quality-working.md).

## Syntax

```sqlsyntax
SNOWFLAKE.CORE.NULL_PERCENT(<query>)
```

## Arguments

`query`
:   Specifies a SQL query that projects a single column.

## Allowed data types

The column projected by the `query` must have one of the following data types:

* DATE
* FLOAT
* NUMBER
* TIMESTAMP_LTZ
* TIMESTAMP_NTZ
* TIMESTAMP_TZ
* VARCHAR

## Returns

The function returns a NUMBER value.

## Example

Measure the percent of NULL values for the SSN column (i.e. US social security number):

```sqlexample
SELECT SNOWFLAKE.CORE.NULL_PERCENT(
  SELECT
    ssn
  FROM hr.tables.empl_info
);
```

```output
+----------------------------------------------------------------+
| SNOWFLAKE.CORE.NULL_COUNT(SELECT ssn FROM hr.tables.empl_info) |
+----------------------------------------------------------------+
| 1                                                              |
+----------------------------------------------------------------+
```
