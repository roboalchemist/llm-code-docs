# Source: https://docs.snowflake.com/en/sql-reference/functions/extract.md

Categories:
:   [Date & time functions](../functions-date-time.md)

# EXTRACT

Extracts the specified date or time part from a date, time, or timestamp.

> **Tip:**
>
> To extract the date from a timestamp, use the [TO_DATE](to_date.md) function.

Alternatives:
:   [DATE_PART](date_part.md) , [HOUR / MINUTE / SECOND](hour-minute-second.md) , [YEAR\* / DAY\* / WEEK\* / MONTH / QUARTER](year.md)

## Syntax

```sqlsyntax
EXTRACT( <date_or_time_part> FROM <date_time_or_timestamp_expr> )
```

```sqlsyntax
EXTRACT( <date_or_time_part> , <date_time_or_timestamp_expr> )
```

## Arguments

`date_or_time_part`
:   The unit of time. Must be one of the values listed in [Supported date and time parts](../functions-date-time.md) (e.g. `month`).
    The value can be a string literal or can be unquoted (for example, `'month'` or `month`).

    * When `date_or_time_part` is `week` (or any of its variations), the output is controlled by the [WEEK_START](../parameters.md) session parameter.
    * When `date_or_time_part` is `dayofweek` or `yearofweek` (or any of their variations), the output is controlled by the [WEEK_OF_YEAR_POLICY](../parameters.md) and [WEEK_START](../parameters.md) session parameters.

    For more information, including examples, see [Calendar weeks and weekdays](../functions-date-time.md).

`date_time_or_timestamp_expr`
:   A date, a time, or a timestamp, or an expression that can be evaluated to a date, a time, or a timestamp.

## Returns

Returns a value of NUMBER data type.

## Usage notes

Currently, when `date_or_timestamp_expr` is a DATE value, the following `date_or_time_part`
values are not supported:

* `epoch_millisecond`
* `epoch_microsecond`
* `epoch_nanosecond`

Other [date and time parts](../functions-date-time.md) (including `epoch_second`) are supported.

## Examples

Specify the `year` part to extract the year from a timestamp:

```sqlexample
SELECT EXTRACT(year FROM TO_TIMESTAMP('2024-04-10T23:39:20.123-07:00')) AS YEAR;
```

```output
+------+
| YEAR |
|------|
| 2024 |
+------+
```

Use EXTRACT with the [DECODE](decode.md) function and the `dayofweek` part to return the full name of the
current day of the week:

```sqlexample
SELECT DECODE(EXTRACT(dayofweek FROM SYSTIMESTAMP()),
  1, 'Monday',
  2, 'Tuesday',
  3, 'Wednesday',
  4, 'Thursday',
  5, 'Friday',
  6, 'Saturday',
  7, 'Sunday') AS DAYOFWEEK;
```

```output
+-----------+
| DAYOFWEEK |
|-----------|
| Thursday  |
+-----------+
```

> **Note:**
>
> The output depends on the value returned by the [SYSTIMESTAMP](systimestamp.md) function when you run the query. Also, you can use the
> [DAYNAME](dayname.md) function to extract the three-letter day-of-week name from the specified date or timestamp.
