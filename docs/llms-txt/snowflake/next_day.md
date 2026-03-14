# Source: https://docs.snowflake.com/en/sql-reference/functions/next_day.md

Categories:
:   [Date & time functions](../functions-date-time.md)

# NEXT_DAY

Returns the date of the first specified day of week (DOW) that occurs after the input date.

See also:
:   [LAST_DAY](last_day.md) , [PREVIOUS_DAY](previous_day.md)

## Syntax

```sqlsyntax
NEXT_DAY( <date_or_timetamp_expr> , <dow_string> )
```

## Arguments

`date_or_timestamp_expr`
:   A date or a timestamp, or an expression that can be evaluated to a date or a timestamp.

`dow_string`
:   Specifies the day of week used to calculate the date for the next day. The value can be a string literal or an expression that returns a string. The string
    must start with the first two characters (case-insensitive) of the day name:

    > * `su` (Sunday)
    > * `mo` (Monday)
    > * `tu` (Tuesday)
    > * `we` (Wednesday)
    > * `th` (Thursday)
    > * `fr` (Friday)
    > * `sa` (Saturday)

    Any leading spaces and trailing characters, including spaces, in the string are ignored.

## Returns

This function returns a value of type DATE, even if `date_or_timetamp_expr` is a timestamp.

## Examples

Return the date of the next Friday that occurs after the current date:

```sqlexample
SELECT CURRENT_DATE() AS "Today's Date",
       NEXT_DAY("Today's Date", 'Friday') AS "Next Friday";
```

```output
+--------------+-------------+
| Today's Date | Next Friday |
|--------------+-------------|
| 2025-05-06   | 2025-05-09  |
+--------------+-------------+
```

Your output will be different because the example uses the [CURRENT_DATE](current_date.md) function.
