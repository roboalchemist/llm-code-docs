# Source: https://docs.snowflake.com/en/sql-reference/functions/try_to_date.md

Categories:
:   [Conversion functions](../functions-conversion.md) , [Date & time functions](../functions-date-time.md)

# TRY_TO_DATE

A special version of the [TO_DATE](to_date.md) function
that performs the same operation (i.e. converts an input expression to a date), but
with error-handling support (i.e. if the conversion cannot be performed, it returns a
NULL value instead of raising an error).

For more information, see [Error-handling conversion functions](../functions-conversion.md).

See also:
:   [TO_DATE , DATE](to_date.md)

## Syntax

```sqlsyntax
TRY_TO_DATE( <string_expr> [, <format> ] )
TRY_TO_DATE( '<integer>' )
```

## Arguments

**Required:**

One of:

> `string_expr`
> :   String from which to extract a date. For example: `'2024-01-31'`.
>
> `'integer'`
> :   An expression that evaluates to a string containing an integer. For example: `'15000000'`. Depending
> on the magnitude of the string, it can be interpreted as seconds, milliseconds, microseconds, or
> nanoseconds. For details, see the Usage notes for this function.

**Optional:**

`format`
:   Date format specifier for `string_expr` or
    [AUTO](../date-time-input-output.md),
    which specifies that Snowflake should automatically detect the format to use. For more information,
    see [Date and time formats in conversion functions](../functions-conversion.md).

    The default is the current value of the [DATE_INPUT_FORMAT](../parameters.md)
    session parameter (default `AUTO`).

## Returns

The data type of the returned value is DATE.

## Usage notes

* The display format for dates in the output is determined by the [DATE_OUTPUT_FORMAT](../parameters.md)
  session parameter (default `YYYY-MM-DD`).
* If the format of the input parameter is a string that contains an integer:

  * After the string is converted to an integer, the integer is treated as a number of seconds, milliseconds,
    microseconds, or nanoseconds after the start of the Unix epoch (1970-01-01 00:00:00.000000000 UTC).

    * If the integer is less than 31536000000 (the number of milliseconds in a year), then the value is treated as
      a number of seconds.
    * If the value is greater than or equal to 31536000000 and less than 31536000000000, then the value is treated
      as milliseconds.
    * If the value is greater than or equal to 31536000000000 and less than 31536000000000000, then the value is
      treated as microseconds.
    * If the value is greater than or equal to 31536000000000000, then the value is
      treated as nanoseconds.
  * If more than one row is evaluated (for example, if the input is the column name of a table that contains more than
    one row), each value is examined independently to determine if the value represents seconds, milliseconds, microseconds, or
    nanoseconds.

## Examples

The following example uses the TRY_TO_DATE function:

```sqlexample
SELECT
  TRY_TO_DATE('2024-05-10') AS valid_date,
  TRY_TO_DATE('Invalid') AS invalid_date;
```

```output
+------------+--------------+
| VALID_DATE | INVALID_DATE |
|------------+--------------|
| 2024-05-10 | NULL         |
+------------+--------------+
```

See [TO_DATE , DATE](to_date.md) for examples that convert an input expression to a date.
