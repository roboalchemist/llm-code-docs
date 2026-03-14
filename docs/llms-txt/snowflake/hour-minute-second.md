# Source: https://docs.snowflake.com/en/sql-reference/functions/hour-minute-second.md

Categories:
:   [Date & time functions](../functions-date-time.md)

# HOUR / MINUTE / SECOND

Extracts the corresponding time part from a time or timestamp value.

These functions are alternatives to using the [DATE_PART](date_part.md) (or [EXTRACT](extract.md)) function with the
equivalent time part (see [Supported date and time parts](../functions-date-time.md)).

See also:
:   [YEAR\* / DAY\* / WEEK\* / MONTH / QUARTER](year.md)

## Syntax

```sqlsyntax
HOUR( <time_or_timestamp_expr> )

MINUTE( <time_or_timestamp_expr> )

SECOND( <time_or_timestamp_expr> )
```

## Arguments

`time_or_timestamp_expr`
:   A time or a timestamp, or an expression that can be evaluated to a time or a timestamp.

## Returns

This function returns a value of type NUMBER.

## Usage notes

| Function name | Time part extracted from time or timestamp | Possible values |
| --- | --- | --- |
| HOUR | Hour of the specified day | 0 to 23 |
| MINUTE | Minute of the specified hour | 0 to 59 |
| SECOND | Second of the specified minute | 0 to 59 |

> **Tip:**
>
> To extract a full TIME value from a TIMESTAMP value instead of a part, you can cast the
> TIMESTAMP value to a TIME value. For example:
>
> ```sqlexample
> SELECT '2025-04-08T23:39:20.123-07:00'::TIMESTAMP::TIME AS full_time_value;
> ```
>
> ```output
> +-----------------+
> | FULL_TIME_VALUE |
> |-----------------|
> | 23:39:20        |
> +-----------------+
> ```

## Examples

This example demonstrates the HOUR, MINUTE, and SECOND functions:

```sqlexample
SELECT '2025-04-08T23:39:20.123-07:00'::TIMESTAMP AS tstamp,
       HOUR(tstamp) AS "HOUR",
       MINUTE(tstamp) AS "MINUTE",
       SECOND(tstamp) AS "SECOND";
```

```output
+-------------------------+------+--------+--------+
| TSTAMP                  | HOUR | MINUTE | SECOND |
|-------------------------+------+--------+--------|
| 2025-04-08 23:39:20.123 |   23 |     39 |     20 |
+-------------------------+------+--------+--------+
```

For more examples, see [Working with date and time values](../date-time-examples.md).
