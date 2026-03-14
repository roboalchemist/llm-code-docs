# Source: https://docs.snowflake.com/en/sql-reference/functions/dmf_null_count.md

Categories:
:   [Data metric functions](../functions-data-metric.md)

# NULL_COUNT (system data metric function)

Returns the total number of NULL values for the specified column in a table.

This topic provides the syntax for calling the function directly. To learn how to associate the function with a table or view so it
runs at regular intervals, see [Associate a DMF](../../user-guide/data-quality-working.md).

## Syntax

```sqlsyntax
SNOWFLAKE.CORE.NULL_COUNT(<query>)
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

The function returns a scalar value with a NUMBER data type.

## Usage notes

When you call a system DMF manually, you don’t need to specify whichever allowed data type you are using. You only need to specify the
query for the column that you want to measure. Snowflake matches the allowed data type for the function with the data type for the column.

## Example

Measure the number of NULL values for the SSN column (that is, US Social Security number):

```sqlexample
SELECT SNOWFLAKE.CORE.NULL_COUNT(
  SELECT
    ssn
  FROM hr.tables.empl_info
);
```

```output
+----------------------------------------------------------------+
| SNOWFLAKE.CORE.NULL_COUNT(SELECT ssn FROM hr.tables.empl_info) |
+----------------------------------------------------------------+
| 5                                                              |
+----------------------------------------------------------------+
```
