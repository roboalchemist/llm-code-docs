# Source: https://docs.snowflake.com/en/sql-reference/functions/current_date.md

Categories:
:   [Context functions](../functions-context.md) (General)

# CURRENT_DATE

Returns the current date of the system.

## Syntax

```sqlsyntax
CURRENT_DATE()

CURRENT_DATE
```

## Arguments

None.

## Returns

The function returns a value of type [DATE](../data-types-datetime.md).

## Usage notes

* The setting of the [TIMEZONE](../parameters.md) parameter affects the return value. The returned date is
  in the time zone for the session.
* The display format for dates in the output is determined by the [DATE_OUTPUT_FORMAT](../parameters.md)
  session parameter (default `YYYY-MM-DD`).
* To comply with the ANSI standard, this function can be called without parentheses in SQL statements.

  However, if you are setting a [Snowflake Scripting variable](../../developer-guide/snowflake-scripting/variables.md)
  to an expression that calls the function (for example, `my_var := CURRENT_DATE();`), you must include the
  parentheses. For more information, see [the usage notes for context functions](../functions-context.md).

## Examples

Show the current date, time, and timestamp:

```sqlexample
SELECT CURRENT_DATE(), CURRENT_TIME(), CURRENT_TIMESTAMP();
```

```output
+----------------+----------------+-------------------------------+
| CURRENT_DATE() | CURRENT_TIME() | CURRENT_TIMESTAMP()           |
|----------------+----------------+-------------------------------|
| 2024-04-18     | 07:47:37       | 2024-04-18 07:47:37.084 -0700 |
+----------------+----------------+-------------------------------+
```
