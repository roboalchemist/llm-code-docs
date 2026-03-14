# Source: https://docs.snowflake.com/en/sql-reference/functions/dmf_duplicate_count.md

Categories:
:   [Data metric functions](../functions-data-metric.md)

# DUPLICATE_COUNT (system data metric function)

Returns the count of column values that have duplicates, including NULL values. If you specify more than one column argument, returns the
number of rows where the combination of the specified columns is duplicated.

If you want to specify more than one column argument, you can’t call the function directly. For an example of associating the function with
a table so you can specify multiple column arguments, see Examples.

## Syntax

```sqlsyntax
SNOWFLAKE.CORE.DUPLICATE_COUNT(<query>)
```

## Arguments

`query`
:   Specifies a SQL query that projects one or more columns.

## Allowed data types

The columns projected by the `query` must have one of the following data types:

* DATE
* FLOAT
* NUMBER
* TIMESTAMP_LTZ
* TIMESTAMP_NTZ
* TIMESTAMP_TZ
* VARCHAR

## Returns

The function returns a scalar value with a NUMBER data type.

## Example

Determine the number of duplicate US Social Security numbers in the `SSN` column:

```sqlexample
SELECT SNOWFLAKE.CORE.DUPLICATE_COUNT(
  SELECT
    ssn
  FROM hr.tables.empl_info
);
```

Associate the DMF with a table to determine the number of duplicates based on the combination of the `first_name` and `last_name`
columns:

```sqlexample
ALTER TABLE t
  ADD DATA METRIC FUNCTION SNOWFLAKE.CORE.DUPLICATE_COUNT
    ON (first_name, last_name);
```
