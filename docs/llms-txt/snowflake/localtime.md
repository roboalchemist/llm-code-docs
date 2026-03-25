# Source: https://docs.snowflake.com/en/sql-reference/functions/localtime.md

Categories:
:   [Context functions](../functions-context.md) (General)

# LOCALTIME

Returns the current time for the system.

ANSI-compliant alias for [CURRENT_TIME](current_time.md).

## Syntax

```sqlsyntax
LOCALTIME()

LOCALTIME
```

## Arguments

None.

## Returns

Returns a value of type [TIME](../data-types-datetime.md).

## Usage notes

* The setting of the [TIMEZONE](../parameters.md) parameter affects the return value. The returned time is
  in the time zone for the session.
* The display format for times in the output is determined by the [TIME_OUTPUT_FORMAT](../parameters.md)
  session parameter (default `HH24:MI:SS`).
* To comply with the ANSI standard, this function can be called without parentheses in SQL statements.

  However, if you are setting a [Snowflake Scripting variable](../../developer-guide/snowflake-scripting/variables.md)
  to an expression that calls the function (for example, `my_var := <function_name>();`), you must include the
  parentheses. For more information, see [the usage notes for context functions](../functions-context.md).
* Do not use the returned value for precise time ordering between concurrent queries (processed by the same virtual
  warehouse) because the queries might be serviced by different compute resources (in the warehouse).

## Examples

Show the current local time and local timestamp:

```sqlexample
SELECT LOCALTIME(), LOCALTIMESTAMP();
```

```output
+-------------+-------------------------------+
| LOCALTIME() | LOCALTIMESTAMP()              |
|-------------+-------------------------------|
| 15:32:45    | 2024-04-17 15:32:45.775 -0700 |
+-------------+-------------------------------+
```
