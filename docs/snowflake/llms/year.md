# Source: https://docs.snowflake.com/en/sql-reference/functions/year.md

Categories:
:   [Date & time functions](../functions-date-time.md)

# YEAR\* / DAY\* / WEEK\* / MONTH / QUARTER

Extracts the corresponding date part from a date or timestamp.

These functions are alternatives to using the [DATE_PART](date_part.md) (or [EXTRACT](extract.md)) function with the
equivalent date part (see [Supported date and time parts](../functions-date-time.md)).

See also:
:   [HOUR / MINUTE / SECOND](hour-minute-second.md)

## Syntax

```sqlsyntax
YEAR( <date_or_timestamp_expr> )

YEAROFWEEK( <date_or_timestamp_expr> )
YEAROFWEEKISO( <date_or_timestamp_expr> )

DAY( <date_or_timestamp_expr> )

DAYOFMONTH( <date_or_timestamp_expr> )
DAYOFWEEK( <date_or_timestamp_expr> )
DAYOFWEEKISO( <date_or_timestamp_expr> )
DAYOFYEAR( <date_or_timestamp_expr> )

WEEK( <date_or_timestamp_expr> )

WEEKOFYEAR( <date_or_timestamp_expr> )
WEEKISO( <date_or_timestamp_expr> )

MONTH( <date_or_timestamp_expr> )

QUARTER( <date_or_timestamp_expr> )
```

## Arguments

`date_or_timestamp_expr`
:   A date or a timestamp, or an expression that can be evaluated to a date or a timestamp.

## Returns

This function returns a value of type NUMBER.

## Usage notes

| Function name | Date part extracted from input date or timestamp | Possible values |
| --- | --- | --- |
| YEAR | Year | Any valid year (for example, 2025) |
| YEAROFWEEK [1] | Year that the extracted week belongs to | Any valid year (for example, 2025) |
| YEAROFWEEKISO | Year that the extracted week belongs to using [ISO semantics](../functions-date-time.md) | Any valid year (for example, 2025) |
| DAY , DAYOFMONTH | Day (number) of the month | 1 to 31 |
| DAYOFWEEK [1] | Day (number) of the week dictated by [session parameters](../functions-date-time.md) | 0 to 7 |
| DAYOFWEEKISO | Day (number) of the week using [ISO semantics](../functions-date-time.md) | 1 to 7 |
| DAYOFYEAR | Day (number) of the year | 1 to 366 |
| WEEK , WEEKOFYEAR [1] | Week (number) of the year | 1 to 54 |
| WEEKISO | Week (number) of the year using [ISO semantics](../functions-date-time.md) | 1 to 53 |
| MONTH | Month (number) of the year | 1 to 12 |
| QUARTER | Quarter (number) of the year | 1 to 4 |

[1] Results dictated by the values set for the WEEK_OF_YEAR_POLICY and/or WEEK_START session parameters.

For details about ISO semantics and the parameter, see [Calendar weeks and weekdays](../functions-date-time.md).

## Examples

The following example demonstrates the use of the functions YEAR, QUARTER, MONTH, DAY, DAYOFWEEK,
and DAYOFYEAR:

```sqlexample
SELECT '2025-04-11T23:39:20.123-07:00'::TIMESTAMP AS tstamp,
       YEAR(tstamp) AS "YEAR",
       QUARTER(tstamp) AS "QUARTER OF YEAR",
       MONTH(tstamp) AS "MONTH",
       DAY(tstamp) AS "DAY",
       DAYOFMONTH(tstamp) AS "DAY OF MONTH",
       DAYOFYEAR(tstamp) AS "DAY OF YEAR";
```

```output
+-------------------------+------+-----------------+-------+-----+--------------+-------------+
| TSTAMP                  | YEAR | QUARTER OF YEAR | MONTH | DAY | DAY OF MONTH | DAY OF YEAR |
|-------------------------+------+-----------------+-------+-----+--------------+-------------|
| 2025-04-11 23:39:20.123 | 2025 |               2 |     4 |  11 |           11 |         101 |
+-------------------------+------+-----------------+-------+-----+--------------+-------------+
```

The following example demonstrates the use of the functions WEEK, WEEKISO, WEEKOFYEAR, YEAROFWEEK, and
YEAROFWEEKISO. The session parameter [WEEK_OF_YEAR_POLICY](../parameters.md) is set to `1`, so that the first week
of the year is the week that contains January 1st of that year.

```sqlexample
ALTER SESSION SET WEEK_OF_YEAR_POLICY = 1;
```

```sqlexample
SELECT '2016-01-02T23:39:20.123-07:00'::TIMESTAMP AS tstamp,
       WEEK(tstamp) AS "WEEK",
       WEEKISO(tstamp) AS "WEEK ISO",
       WEEKOFYEAR(tstamp) AS "WEEK OF YEAR",
       YEAROFWEEK(tstamp) AS "YEAR OF WEEK",
       YEAROFWEEKISO(tstamp) AS "YEAR OF WEEK ISO";
```

```output
+-------------------------+------+----------+--------------+--------------+------------------+
| TSTAMP                  | WEEK | WEEK ISO | WEEK OF YEAR | YEAR OF WEEK | YEAR OF WEEK ISO |
|-------------------------+------+----------+--------------+--------------+------------------|
| 2016-01-02 23:39:20.123 |    1 |       53 |            1 |         2016 |             2015 |
+-------------------------+------+----------+--------------+--------------+------------------+
```

The following example also demonstrates the use of the functions WEEK, WEEKISO, WEEKOFYEAR, YEAROFWEEK, and
YEAROFWEEKISO. The session parameter WEEK_OF_YEAR_POLICY is set to indicate that the first week
of the year is the first week of the year that contains at least four days from that year. In this example,
the week December 27, 2015 through January 2, 2016 is considered the last week of 2015, not the first week
of 2016. Even though the week contains Friday January 1, 2016, less than half of the week is in 2016.

```sqlexample
ALTER SESSION SET WEEK_OF_YEAR_POLICY = 0;
```

```sqlexample
SELECT '2016-01-02T23:39:20.123-07:00'::TIMESTAMP AS tstamp,
       WEEK(tstamp) AS "WEEK",
       WEEKISO(tstamp) AS "WEEK ISO",
       WEEKOFYEAR(tstamp) AS "WEEK OF YEAR",
       YEAROFWEEK(tstamp) AS "YEAR OF WEEK",
       YEAROFWEEKISO(tstamp) AS "YEAR OF WEEK ISO";
```

```output
+-------------------------+------+----------+--------------+--------------+------------------+
| TSTAMP                  | WEEK | WEEK ISO | WEEK OF YEAR | YEAR OF WEEK | YEAR OF WEEK ISO |
|-------------------------+------+----------+--------------+--------------+------------------|
| 2016-01-02 23:39:20.123 |   53 |       53 |           53 |         2015 |             2015 |
+-------------------------+------+----------+--------------+--------------+------------------+
```

The following example demonstrates the use of the functions DAYOFWEEK and DAYOFWEEKISO.
The session parameter [WEEK_START](../parameters.md) is set to indicate that the week starts on Sunday.

```sqlexample
ALTER SESSION SET WEEK_START = 7;
```

The timestamp in the following query is for April 5, 2025, which was a Saturday. The DAYOFWEEK function
returns `7` for Saturday, because the first day of the week is set to Sunday. The DAYOFWEEKISO function
returns `6` because the first day of the week using ISO semantics is Monday. For more information about ISO
semantics and the WEEK_START parameter, see [Calendar weeks and weekdays](../functions-date-time.md).

```sqlexample
SELECT '2025-04-05T23:39:20.123-07:00'::TIMESTAMP AS tstamp,
       DAYOFWEEK(tstamp) AS "DAY OF WEEK",
       DAYOFWEEKISO(tstamp) AS "DAY OF WEEK ISO";
```

```output
+-------------------------+-------------+-----------------+
| TSTAMP                  | DAY OF WEEK | DAY OF WEEK ISO |
|-------------------------+-------------+-----------------|
| 2025-04-05 23:39:20.123 |           7 |               6 |
+-------------------------+-------------+-----------------+
```

The following example also demonstrates the use of the functions DAYOFWEEK and DAYOFWEEKISO.
The session parameter WEEK_START is set to indicate that the week starts on Monday.

```sqlexample
ALTER SESSION SET WEEK_START = 1;
```

```sqlexample
SELECT '2025-04-05T23:39:20.123-07:00'::TIMESTAMP AS tstamp,
       DAYOFWEEK(tstamp) AS "DAY OF WEEK",
       DAYOFWEEKISO(tstamp) AS "DAY OF WEEK ISO";
```

```output
+-------------------------+-------------+-----------------+
| TSTAMP                  | DAY OF WEEK | DAY OF WEEK ISO |
|-------------------------+-------------+-----------------|
| 2025-04-05 23:39:20.123 |           6 |               6 |
+-------------------------+-------------+-----------------+
```

For more examples, see [Working with date and time values](../date-time-examples.md).

For more detailed examples of the week-related functions (DAYOFWEEK, WEEK, WEEKOFYEAR, YEAROFWEEK, and so on),
see [Calendar weeks and weekdays](../functions-date-time.md).
