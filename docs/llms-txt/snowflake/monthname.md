# Source: https://docs.snowflake.com/en/sql-reference/functions/monthname.md

Categories:
:   [Date & time functions](../functions-date-time.md)

# MONTHNAME

Returns the three-letter month name for the specified date or timestamp.

## Syntax

```sqlsyntax
MONTHNAME( <date_or_timestamp_expr> )
```

## Arguments

`date_or_timestamp_expr`
:   A date or a timestamp, or an expression that can be evaluated to a date or a timestamp.

## Returns

This function returns a value of type VARCHAR.

## Usage notes

To return the full month name instead of the three-letter month name, you can use the
[TO_CHAR](to_char.md) function with the [TO_DATE](to_date.md) or [TO_TIMESTAMP](to_timestamp.md)
function. The following example uses the TO_CHAR and TO_DATE functions to return the full month name for
the date `2025-01-01`:

```sqlexample
SELECT TO_CHAR(TO_DATE('2025-01-01'), 'MMMM') AS full_month_name;
```

```output
+-----------------+
| FULL_MONTH_NAME |
|-----------------|
| January         |
+-----------------+
```

## Examples

The following examples use the MONTHNAME function.

Return the three-letter month name of a date:

```sqlexample
SELECT MONTHNAME(TO_DATE('2025-01-01')) AS month;
```

```output
+-------+
| MONTH |
|-------|
| Jan   |
+-------+
```

Return the three-letter month name of a timestamp:

```sqlexample
SELECT MONTHNAME(TO_TIMESTAMP('2025-04-03 10:00')) AS month;
```

```output
+-------+
| MONTH |
|-------|
| Apr   |
+-------+
```

Return the three-letter month name of DATE values in a column.

First, create a table with a DATE column and insert various DATE values:

```sqlexample
CREATE OR REPLACE TABLE monthname_function_demo (d DATE);

INSERT INTO monthname_function_demo (d) VALUES
  ('2024-01-01'::DATE),
  ('2024-02-02'::DATE),
  ('2024-03-03'::DATE),
  ('2024-04-04'::DATE),
  ('2024-05-05'::DATE),
  ('2024-06-06'::DATE),
  ('2024-07-07'::DATE),
  ('2024-08-08'::DATE),
  ('2024-09-09'::DATE),
  ('2024-10-10'::DATE),
  ('2024-11-11'::DATE),
  ('2024-12-12'::DATE);
```

Use the MONTHNAME function in a query to return the three-letter month name of each
value in the `d` column:

```sqlexample
SELECT d,
       MONTHNAME(d) AS month
  FROM monthname_function_demo;
```

```output
+------------+-------+
| D          | MONTH |
|------------+-------|
| 2024-01-01 | Jan   |
| 2024-02-02 | Feb   |
| 2024-03-03 | Mar   |
| 2024-04-04 | Apr   |
| 2024-05-05 | May   |
| 2024-06-06 | Jun   |
| 2024-07-07 | Jul   |
| 2024-08-08 | Aug   |
| 2024-09-09 | Sep   |
| 2024-10-10 | Oct   |
| 2024-11-11 | Nov   |
| 2024-12-12 | Dec   |
+------------+-------+
```
