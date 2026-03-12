# Source: https://docs.snowflake.com/en/sql-reference/functions/try_to_timestamp.md

Categories:
:   [Conversion functions](../functions-conversion.md)

# TRY_TO_TIMESTAMP / TRY_TO_TIMESTAMP_\*

A special version of [TO_TIMESTAMP / TO_TIMESTAMP_\*](to_timestamp.md) that performs the same operation (i.e. converts an input expression into a timestamp), but with error-handling support (i.e. if the conversion cannot be performed, it returns a NULL value instead of raising an error).

For more information, see [Error-handling conversion functions](../functions-conversion.md).

> **Note:**
>
> TRY_TO_TIMESTAMP maps to one of the other timestamp functions, based on the
> [TIMESTAMP_TYPE_MAPPING](../parameters.md) session parameter. The parameter default
> is TIMESTAMP_NTZ so TRY_TO_TIMESTAMP maps to TRY_TO_TIMESTAMP_NTZ by default.

See also:
:   [TO_TIMESTAMP / TO_TIMESTAMP_\*](to_timestamp.md)

## Syntax

```sqlsyntax
timestampFunction ( <string_expr> [, <format> ] )
timestampFunction ( '<integer>' )
```

Where:

> ```sqlsyntax
> timestampFunction ::=
>     TRY_TO_TIMESTAMP | TRY_TO_TIMESTAMP_LTZ | TRY_TO_TIMESTAMP_NTZ | TRY_TO_TIMESTAMP_TZ
> ```

## Arguments

**Required:**

One of:

> `string_expr`
> :   A string that can be evaluated to a TIMESTAMP (TIMESTAMP_NTZ, TIMESTAMP_LTZ, or TIMESTAMP_TZ).
>
> `'integer'`
> :   An expression that evaluates to a string containing an integer, for example `'15000000'`. Depending
> on the magnitude of the string, it can be interpreted as seconds, milliseconds, microseconds, or
> nanoseconds. For details, see the Usage Notes.

**Optional:**

`format`
:   Format specifier for `string_expr` or
    [AUTO](../date-time-input-output.md).
    For more information, see [Date and time formats in conversion functions](../functions-conversion.md).

    The default is the current value of the [TIMESTAMP_INPUT_FORMAT](../parameters.md)
    session parameter (default AUTO).

## Returns

The data type of the returned value is one of the TIMESTAMP data
types. By default, the data type is TIMESTAMP_NTZ. You can change
this by setting the session parameter [TIMESTAMP_TYPE_MAPPING](../parameters.md).

## Usage notes

* For timestamps with time zones, the setting of the [TIMEZONE](../parameters.md) parameter affects the return value. The returned
  timestamp is in the time zone for the session.
* The display format for timestamps in the output is determined by the timestamp output format that corresponds with the
  function ([TIMESTAMP_OUTPUT_FORMAT](../parameters.md), [TIMESTAMP_LTZ_OUTPUT_FORMAT](../parameters.md), [TIMESTAMP_NTZ_OUTPUT_FORMAT](../parameters.md),
  or [TIMESTAMP_TZ_OUTPUT_FORMAT](../parameters.md)).
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

* When you use the TO_TIMESTAMP_NTZ or TRY_TO_TIMESTAMP_NTZ function to convert a timestamp with time zone information, the time zone
  information is lost. If the timestamp is then converted back to a timestamp with time zone information (by using
  the TO_TIMESTAMP_TZ function for example), the time zone information is not recoverable.

## Examples

This example uses TRY_TO_TIMESTAMP:

```sqlexample
SELECT TRY_TO_TIMESTAMP('2024-01-15 12:30:00'), TRY_TO_TIMESTAMP('Invalid');
```

```output
+-----------------------------------------+-----------------------------+
| TRY_TO_TIMESTAMP('2024-01-15 12:30:00') | TRY_TO_TIMESTAMP('INVALID') |
|-----------------------------------------+-----------------------------|
| 2024-01-15 12:30:00.000                 | NULL                        |
+-----------------------------------------+-----------------------------+
```

See [TO_TIMESTAMP / TO_TIMESTAMP_\*](to_timestamp.md) for examples that convert an input expression to a timestamp.
