# Source: https://docs.snowflake.com/en/sql-reference/functions/date_part.md

Categories:
:   [Date & time functions](../functions-date-time.md)

# DATE_PART

Extracts the specified date or time part from a date, time, or timestamp.

Alternatives:
:   [EXTRACT](extract.md) , [HOUR / MINUTE / SECOND](hour-minute-second.md) , [YEAR\* / DAY\* / WEEK\* / MONTH / QUARTER](year.md)

## Syntax

```sqlsyntax
DATE_PART( <date_or_time_part> , <date_time_or_timestamp_expr> )
```

```sqlsyntax
DATE_PART( <date_or_time_part> FROM <date_time_or_timestamp_expr> )
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

> **Tip:**
>
> To extract a full DATE or TIME value instead of a single part from a TIMESTAMP value, you can cast the
> TIMESTAMP value to a DATE or TIME value, respectively. For example:
>
> ```sqlexample
> SELECT '2025-04-08T23:39:20.123-07:00'::TIMESTAMP::DATE AS full_date_value;
> ```
>
> ```output
> +-----------------+
> | FULL_DATE_VALUE |
> |-----------------|
> | 2025-04-08      |
> +-----------------+
> ```
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

This shows a simple example of extracting part of a DATE:

```sqlexample
SELECT DATE_PART(quarter, '2024-04-08'::DATE);
```

```output
+----------------------------------------+
| DATE_PART(QUARTER, '2024-04-08'::DATE) |
|----------------------------------------|
|                                      2 |
+----------------------------------------+
```

This shows an example of extracting part of a TIMESTAMP:

```sqlexample
SELECT TO_TIMESTAMP(
  '2024-04-08T23:39:20.123-07:00') AS "TIME_STAMP1",
  DATE_PART(year, "TIME_STAMP1") AS "EXTRACTED YEAR";
```

```output
+-------------------------+----------------+
| TIME_STAMP1             | EXTRACTED YEAR |
|-------------------------+----------------|
| 2024-04-08 23:39:20.123 |           2024 |
+-------------------------+----------------+
```

This shows an example of converting a TIMESTAMP to the number of seconds since
the beginning of the [Unix epoch](https://en.wikipedia.org/wiki/Unix_time) (midnight January 1, 1970):

```sqlexample
SELECT TO_TIMESTAMP(
  '2024-04-08T23:39:20.123-07:00') AS "TIME_STAMP1",
  DATE_PART(epoch_second, "TIME_STAMP1") AS "EXTRACTED EPOCH SECOND";
```

```output
+-------------------------+------------------------+
| TIME_STAMP1             | EXTRACTED EPOCH SECOND |
|-------------------------+------------------------|
| 2024-04-08 23:39:20.123 |             1712619560 |
+-------------------------+------------------------+
```

This shows an example of converting a TIMESTAMP to the number of milliseconds since
the beginning of the [Unix epoch](https://en.wikipedia.org/wiki/Unix_time) (midnight January 1, 1970):

```sqlexample
SELECT TO_TIMESTAMP(
  '2024-04-08T23:39:20.123-07:00') AS "TIME_STAMP1",
  DATE_PART(epoch_millisecond, "TIME_STAMP1") AS "EXTRACTED EPOCH MILLISECOND";
```

```output
+-------------------------+-----------------------------+
| TIME_STAMP1             | EXTRACTED EPOCH MILLISECOND |
|-------------------------+-----------------------------|
| 2024-04-08 23:39:20.123 |               1712619560123 |
+-------------------------+-----------------------------+
```
