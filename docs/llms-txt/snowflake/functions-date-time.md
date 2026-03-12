# Source: https://docs.snowflake.com/en/sql-reference/functions-date-time.md

# Date & time functions

This family of functions can be used to construct, convert, extract, or modify date, time, and timestamp data.

## List of functions

| Sub-category | Function | Notes |
| --- | --- | --- |
| **Construction** | [DATE_FROM_PARTS](functions/date_from_parts.md) |  |
| [TIME_FROM_PARTS](functions/time_from_parts.md) |  |
| [TIMESTAMP_FROM_PARTS](functions/timestamp_from_parts.md) |  |
| **Extraction** | [DATE_PART](functions/date_part.md) | Accepts all date and time parts (see Supported date and time parts). |
| [DAYNAME](functions/dayname.md) |  |
| [EXTRACT](functions/extract.md) | Alternative for [DATE_PART](functions/date_part.md). |
| [HOUR / MINUTE / SECOND](functions/hour-minute-second.md) | Alternative for [DATE_PART](functions/date_part.md). |
| [LAST_DAY](functions/last_day.md) | Accepts relevant date parts (see Supported date and time parts). |
| [MONTHNAME](functions/monthname.md) |  |
| [NEXT_DAY](functions/next_day.md) |  |
| [PREVIOUS_DAY](functions/previous_day.md) |  |
| [YEAR\* / DAY\* / WEEK\* / MONTH / QUARTER](functions/year.md) | Alternative for [DATE_PART](functions/date_part.md). |
| **Addition/subtraction** | [ADD_MONTHS](functions/add_months.md) |  |
| [DATEADD](functions/dateadd.md) | Accepts relevant date and time parts (see Supported date and time parts). |
| [DATEDIFF](functions/datediff.md) | Accepts relevant date and time parts (see Supported date and time parts). |
| [MONTHS_BETWEEN](functions/months_between.md) |  |
| [TIMEADD](functions/timeadd.md) | Alias for [DATEADD](functions/dateadd.md). |
| [TIMEDIFF](functions/timediff.md) | Alias for [DATEDIFF](functions/datediff.md). |
| [TIMESTAMPADD](functions/timestampadd.md) | Alias for [DATEADD](functions/dateadd.md). |
| [TIMESTAMPDIFF](functions/timestampdiff.md) | Alias for [DATEDIFF](functions/datediff.md). |
| **Truncation** | [DATE_TRUNC](functions/date_trunc.md) | Accepts relevant date and time parts (see Supported date and time parts). |
| [TIME_SLICE](functions/time_slice.md) | Allows a time to be “rounded” to the start of an evenly-spaced interval. |
| [TRUNCATE, TRUNC](functions/trunc2.md) | Alternative for [DATE_TRUNC](functions/date_trunc.md). |
| **Conversion** | [TO_DATE , DATE](functions/to_date.md) | Supports conversions based on string, timestamp, and VARIANT expressions. Supports integers for conversions based on the beginning of the Unix epoch. |
| [TO_TIME , TIME](functions/to_time.md) | Supports conversions based on string, timestamp, and VARIANT expressions. Supports integers for conversions based on the beginning of the Unix epoch. |
| [TO_TIMESTAMP / TO_TIMESTAMP_\*](functions/to_timestamp.md) | Supports conversions based on string, date, timestamp, and VARIANT expressions. Supports numeric expressions and integers for conversions based on the beginning of the Unix epoch. |
| **Time zone** | [CONVERT_TIMEZONE](functions/convert_timezone.md) |  |
| **Alerts** | [LAST_SUCCESSFUL_SCHEDULED_TIME](functions/last_successful_scheduled_time.md) |  |
| [SCHEDULED_TIME](functions/scheduled_time.md) |  |

## Output formats

Several date and time functions return date, time, and timestamp values. The following session parameters
determine the format of the output returned by these functions:

* The display format for times is determined by the [TIME_OUTPUT_FORMAT](parameters.md)
  session parameter (default `HH24:MI:SS`).
* The display format for dates is determined by the [DATE_OUTPUT_FORMAT](parameters.md)
  session parameter (default `YYYY-MM-DD`).
* The display format for timestamps is determined by the timestamp data type returned by the function.
  The following session parameters set the output format for different timestamp data types:

  * [TIMESTAMP_LTZ_OUTPUT_FORMAT](parameters.md)
  * [TIMESTAMP_NTZ_OUTPUT_FORMAT](parameters.md)
  * [TIMESTAMP_TZ_OUTPUT_FORMAT](parameters.md)
  * [TIMESTAMP_OUTPUT_FORMAT](parameters.md)

For more information, see [Date and time input and output formats](date-time-input-output.md).

## Supported date and time parts

Certain functions (as well as their appropriate aliases and alternatives) accept a date or time part as an argument. The following two
tables list the parts (case-insensitive) that you can use with these functions.

| Date parts | Abbreviations / variations | DATEADD | DATEDIFF | DATE_PART | DATE_TRUNC | LAST_DAY |
| --- | --- | --- | --- | --- | --- | --- |
| `year` | `y` , `yy` , `yyy` , `yyyy` , `yr` , `years` , `yrs` | ✔ | ✔ | ✔ | ✔ | ✔ |
| `month` | `mm` , `mon` , `mons` , `months` | ✔ | ✔ | ✔ | ✔ | ✔ |
| `day` | `d` , `dd` , `days`, `dayofmonth` | ✔ | ✔ | ✔ | ✔ |  |
| `dayofweek` [1] | `weekday` , `dow` , `dw` |  |  | ✔ |  |  |
| `dayofweek_iso` [2] | `dayofweekiso` , `weekday_iso` , `dow_iso` , `dw_iso` |  |  | ✔ |  |  |
| `dayofyear` | `yearday` , `doy` , `dy` |  |  | ✔ |  |  |
| `week` [1] | `w` , `wk` , `weekofyear` , `woy` , `wy` | ✔ | ✔ | ✔ | ✔ | ✔ |
| `week_iso` [2] | `weekiso` , `weekofyeariso` , `weekofyear_iso` |  |  | ✔ |  |  |
| `quarter` | `q` , `qtr` , `qtrs` , `quarters` | ✔ | ✔ | ✔ | ✔ | ✔ |
| `yearofweek` [1] |  |  |  | ✔ |  |  |
| `yearofweekiso` [2] |  |  |  | ✔ |  |  |

[1] For usage details, see the next section, which describes how Snowflake handles calendar weeks and weekdays.

[2] Not controlled by the WEEK_START and WEEK_OF_YEAR_POLICY session parameters, as described in the next section.

| Time Parts | Abbreviations / Variations | DATEADD | DATEDIFF | DATE_PART | DATE_TRUNC | LAST_DAY |
| --- | --- | --- | --- | --- | --- | --- |
| `hour` | `h` , `hh` , `hr` , `hours` , `hrs` | ✔ | ✔ | ✔ | ✔ |  |
| `minute` | `m` , `mi` , `min` , `minutes` , `mins` | ✔ | ✔ | ✔ | ✔ |  |
| `second` | `s` , `sec` , `seconds` , `secs` | ✔ | ✔ | ✔ | ✔ |  |
| `millisecond` | `ms` , `msec` , `milliseconds` | ✔ | ✔ |  | ✔ |  |
| `microsecond` | `us` , `usec` , `microseconds` | ✔ | ✔ |  | ✔ |  |
| `nanosecond` | `ns` , `nsec` , `nanosec` , `nsecond` , `nanoseconds` , `nanosecs` , `nseconds` | ✔ | ✔ | ✔ | ✔ |  |
| `epoch_second` | `epoch` , `epoch_seconds` |  |  | ✔ |  |  |
| `epoch_millisecond` | `epoch_milliseconds` |  |  | ✔ |  |  |
| `epoch_microsecond` | `epoch_microseconds` |  |  | ✔ |  |  |
| `epoch_nanosecond` | `epoch_nanoseconds` |  |  | ✔ |  |  |
| `timezone_hour` | `tzh` |  |  | ✔ |  |  |
| `timezone_minute` | `tzm` |  |  | ✔ |  |  |

## Calendar weeks and weekdays

The behavior of week-related functions in Snowflake is controlled by the [WEEK_START](parameters.md) and [WEEK_OF_YEAR_POLICY](parameters.md) session parameters. An important aspect of understanding how these
parameters interact is the concept of ISO weeks.

### ISO weeks

As defined in the [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) standard (for dates and time formats), ISO weeks always start on Monday and “belong” to the year that contains the Thursday of
that week. This means that a day in one year might belong to a week in a different year:

* For days in early January, the WOY (week of the year) value can be 52 or 53 (i.e. the day belongs to the last week in the previous year).
* For days in late December, the WOY value can be 1 (i.e. the day belongs to the first week in the next year).

Snowflake provides a special set of week-related date functions (and equivalent data parts) whose behavior is consistent with the ISO week semantics:
[DAYOFWEEKISO, WEEKISO, and YEAROFWEEKISO](functions/year.md).

These functions (and date parts) disregard the session parameters (i.e. they always follow the ISO semantics).

For details about how the other week-related date functions are handled, see the following sections:

* First day of the week
* First and last weeks of the year
* Examples

### First day of the week

Most week-related functions are controlled only by the [WEEK_START](parameters.md) session parameter. The function results differ depending on how this parameter is set:

| Function | Parameter set to `0` (default / legacy behavior) | Parameter set to `1` - `7` (Monday - Sunday) |
| --- | --- | --- |
| [DAYOFWEEK](functions/year.md) | Returns `0` (Sunday) to `6` (Saturday). | Returns `1` (defined first day of the week) to `7` (last day of the week relative to the defined first day). |
| [DATE_TRUNC](functions/date_trunc.md) (with a `WEEK` part) | Truncates the input week to start on Monday. | Truncates the input week to start on the defined first day of the week. |
| [LAST_DAY](functions/last_day.md) (with a `WEEK` part) | Returns the Sunday of the input week. | Returns the last day of the input week relative to the defined first day of the week. |
| [DATEDIFF](functions/datediff.md) (with a `WEEK` part) | Calculated using weeks starting on Monday. | Calculated using weeks starting on the defined first day of the week. |

> **Tip:**
>
> The default value for the parameter is `0`, which preserves the legacy Snowflake behavior (ISO-like semantics).
> However, we recommend changing this value to explicitly control the resulting behavior of the functions. The most common
> scenario is to set the parameter to `1`.

### First and last weeks of the year

The [WEEK_OF_YEAR_POLICY](parameters.md) session parameter controls how the [WEEK and YEAROFWEEK](functions/year.md) functions behave.
The parameter can have two values:

* `0`: The affected week-related functions use semantics similar to the ISO semantics, in which a week belongs to a given year
  if at least 4 days of that week are in that year. This means that all the weeks have 7 days, but the first days of January and the
  last days of December might belong to a week in a different year. For this reason, both the [YEAROFWEEK and YEAROFWEEKISO](functions/year.md)
  functions can provide the year that the week belongs to.
* `1`: January 1 always starts the first week of the year, and December 31 is always in the last week of the year. This means
  that the first week and last week in the year might have fewer than 7 days.

This behavior is also influenced by the start day of the week, as controlled by the value set for the [WEEK_START](parameters.md) session parameter:

* `0` or `1`: The behavior is equivalent to the ISO week semantics, with the week starting on Monday.
* `2` to `7`: The “4 days” logic is preserved, but the first day of the week is different.

> **Tip:**
>
> The default value for both parameters is `0`, which preserves the legacy Snowflake behavior (ISO-like semantics). However,
> we recommend changing these values to explicitly control the resulting behavior of the functions. The most common scenario is
> to set both parameters to `1`.

### Examples

These examples query the same set of date functions, but with different values set for the [WEEK_OF_YEAR_POLICY](parameters.md)
and [WEEK_START](parameters.md) session parameters to illustrate how they influence the results of the functions.

The examples use the following data:

```sqlexample
CREATE OR REPLACE TABLE week_examples (d DATE);

INSERT INTO week_examples VALUES
  ('2016-12-30'),
  ('2016-12-31'),
  ('2017-01-01'),
  ('2017-01-02'),
  ('2017-01-03'),
  ('2017-01-04'),
  ('2017-01-05'),
  ('2017-12-30'),
  ('2017-12-31');
```

#### Controlling the first day of the week

Setting WEEK_START to `0` (legacy behavior) or `1` (Monday) does not have a significant effect, as illustrated in the following two examples:

```sqlexample
ALTER SESSION SET WEEK_START = 0;

SELECT d "Date",
       DAYNAME(d) "Day",
       DAYOFWEEK(d) "DOW",
       DATE_TRUNC('week', d) "Trunc Date",
       DAYNAME("Trunc Date") "Trunc Day",
       LAST_DAY(d, 'week') "Last DOW Date",
       DAYNAME("Last DOW Date") "Last DOW Day",
       DATEDIFF('week', '2017-01-01', d) "Weeks Diff from 2017-01-01 to Date"
  FROM week_examples;
```

```output
+------------+-----+-----+------------+-----------+---------------+--------------+------------------------------------+
| Date       | Day | DOW | Trunc Date | Trunc Day | Last DOW Date | Last DOW Day | Weeks Diff from 2017-01-01 to Date |
|------------+-----+-----+------------+-----------+---------------+--------------+------------------------------------|
| 2016-12-30 | Fri |   5 | 2016-12-26 | Mon       | 2017-01-01    | Sun          |                                  0 |
| 2016-12-31 | Sat |   6 | 2016-12-26 | Mon       | 2017-01-01    | Sun          |                                  0 |
| 2017-01-01 | Sun |   0 | 2016-12-26 | Mon       | 2017-01-01    | Sun          |                                  0 |
| 2017-01-02 | Mon |   1 | 2017-01-02 | Mon       | 2017-01-08    | Sun          |                                  1 |
| 2017-01-03 | Tue |   2 | 2017-01-02 | Mon       | 2017-01-08    | Sun          |                                  1 |
| 2017-01-04 | Wed |   3 | 2017-01-02 | Mon       | 2017-01-08    | Sun          |                                  1 |
| 2017-01-05 | Thu |   4 | 2017-01-02 | Mon       | 2017-01-08    | Sun          |                                  1 |
| 2017-12-30 | Sat |   6 | 2017-12-25 | Mon       | 2017-12-31    | Sun          |                                 52 |
| 2017-12-31 | Sun |   0 | 2017-12-25 | Mon       | 2017-12-31    | Sun          |                                 52 |
+------------+-----+-----+------------+-----------+---------------+--------------+------------------------------------+
```

```sqlexample
ALTER SESSION SET WEEK_START = 1;

SELECT d "Date",
       DAYNAME(d) "Day",
       DAYOFWEEK(d) "DOW",
       DATE_TRUNC('week', d) "Trunc Date",
       DAYNAME("Trunc Date") "Trunc Day",
       LAST_DAY(d, 'week') "Last DOW Date",
       DAYNAME("Last DOW Date") "Last DOW Day",
       DATEDIFF('week', '2017-01-01', d) "Weeks Diff from 2017-01-01 to Date"
  FROM week_examples;
```

```output
+------------+-----+-----+------------+-----------+---------------+--------------+------------------------------------+
| Date       | Day | DOW | Trunc Date | Trunc Day | Last DOW Date | Last DOW Day | Weeks Diff from 2017-01-01 to Date |
|------------+-----+-----+------------+-----------+---------------+--------------+------------------------------------|
| 2016-12-30 | Fri |   5 | 2016-12-26 | Mon       | 2017-01-01    | Sun          |                                  0 |
| 2016-12-31 | Sat |   6 | 2016-12-26 | Mon       | 2017-01-01    | Sun          |                                  0 |
| 2017-01-01 | Sun |   7 | 2016-12-26 | Mon       | 2017-01-01    | Sun          |                                  0 |
| 2017-01-02 | Mon |   1 | 2017-01-02 | Mon       | 2017-01-08    | Sun          |                                  1 |
| 2017-01-03 | Tue |   2 | 2017-01-02 | Mon       | 2017-01-08    | Sun          |                                  1 |
| 2017-01-04 | Wed |   3 | 2017-01-02 | Mon       | 2017-01-08    | Sun          |                                  1 |
| 2017-01-05 | Thu |   4 | 2017-01-02 | Mon       | 2017-01-08    | Sun          |                                  1 |
| 2017-12-30 | Sat |   6 | 2017-12-25 | Mon       | 2017-12-31    | Sun          |                                 52 |
| 2017-12-31 | Sun |   7 | 2017-12-25 | Mon       | 2017-12-31    | Sun          |                                 52 |
+------------+-----+-----+------------+-----------+---------------+--------------+------------------------------------+
```

* With WEEK_START set to `0`, the DOW for Sunday is `0`.
* With WEEK_START set to `1`, the DOW for Sunday is `7`.

The results differ more significantly if WEEK_START is set to any day other than Monday. For example, setting the parameter to `3` (Wednesday) changes the results of all the week-related functions (columns 3 through 8):

```sqlexample
ALTER SESSION SET WEEK_START = 3;

SELECT d "Date",
       DAYNAME(d) "Day",
       DAYOFWEEK(d) "DOW",
       DATE_TRUNC('week', d) "Trunc Date",
       DAYNAME("Trunc Date") "Trunc Day",
       LAST_DAY(d, 'week') "Last DOW Date",
       DAYNAME("Last DOW Date") "Last DOW Day",
       DATEDIFF('week', '2017-01-01', d) "Weeks Diff from 2017-01-01 to Date"
  FROM week_examples;
```

```output
+------------+-----+-----+------------+-----------+---------------+--------------+------------------------------------+
| Date       | Day | DOW | Trunc Date | Trunc Day | Last DOW Date | Last DOW Day | Weeks Diff from 2017-01-01 to Date |
|------------+-----+-----+------------+-----------+---------------+--------------+------------------------------------|
| 2016-12-30 | Fri |   3 | 2016-12-28 | Wed       | 2017-01-03    | Tue          |                                  0 |
| 2016-12-31 | Sat |   4 | 2016-12-28 | Wed       | 2017-01-03    | Tue          |                                  0 |
| 2017-01-01 | Sun |   5 | 2016-12-28 | Wed       | 2017-01-03    | Tue          |                                  0 |
| 2017-01-02 | Mon |   6 | 2016-12-28 | Wed       | 2017-01-03    | Tue          |                                  0 |
| 2017-01-03 | Tue |   7 | 2016-12-28 | Wed       | 2017-01-03    | Tue          |                                  0 |
| 2017-01-04 | Wed |   1 | 2017-01-04 | Wed       | 2017-01-10    | Tue          |                                  1 |
| 2017-01-05 | Thu |   2 | 2017-01-04 | Wed       | 2017-01-10    | Tue          |                                  1 |
| 2017-12-30 | Sat |   4 | 2017-12-27 | Wed       | 2018-01-02    | Tue          |                                 52 |
| 2017-12-31 | Sun |   5 | 2017-12-27 | Wed       | 2018-01-02    | Tue          |                                 52 |
+------------+-----+-----+------------+-----------+---------------+--------------+------------------------------------+
```

#### Controlling the year and days for the first/last weeks of the year

The following example sets both parameters to `0` to follow ISO-like semantics (i.e. week starts on Monday and all weeks have 7 days):

```sqlexample
ALTER SESSION SET WEEK_OF_YEAR_POLICY=0, WEEK_START=0;

SELECT d "Date",
       DAYNAME(d) "Day",
       WEEK(d) "WOY",
       WEEKISO(d) "WOY (ISO)",
       YEAROFWEEK(d) "YOW",
       YEAROFWEEKISO(d) "YOW (ISO)"
  FROM week_examples;
```

```output
+------------+-----+-----+-----------+------+-----------+
| Date       | Day | WOY | WOY (ISO) |  YOW | YOW (ISO) |
|------------+-----+-----+-----------+------+-----------|
| 2016-12-30 | Fri |  52 |        52 | 2016 |      2016 |
| 2016-12-31 | Sat |  52 |        52 | 2016 |      2016 |
| 2017-01-01 | Sun |  52 |        52 | 2016 |      2016 |
| 2017-01-02 | Mon |   1 |         1 | 2017 |      2017 |
| 2017-01-03 | Tue |   1 |         1 | 2017 |      2017 |
| 2017-01-04 | Wed |   1 |         1 | 2017 |      2017 |
| 2017-01-05 | Thu |   1 |         1 | 2017 |      2017 |
| 2017-12-30 | Sat |  52 |        52 | 2017 |      2017 |
| 2017-12-31 | Sun |  52 |        52 | 2017 |      2017 |
+------------+-----+-----+-----------+------+-----------+
```

The next example illustrates the effect of keeping WEEK_OF_YEAR_POLICY set to `0`, but changing WEEK_START to `3` (Wednesday):

```sqlexample
ALTER SESSION SET WEEK_OF_YEAR_POLICY=0, WEEK_START=3;

SELECT d "Date",
       DAYNAME(d) "Day",
       WEEK(d) "WOY",
       WEEKISO(d) "WOY (ISO)",
       YEAROFWEEK(d) "YOW",
       YEAROFWEEKISO(d) "YOW (ISO)"
  FROM week_examples;
```

```output
+------------+-----+-----+-----------+------+-----------+
| Date       | Day | WOY | WOY (ISO) |  YOW | YOW (ISO) |
|------------+-----+-----+-----------+------+-----------|
| 2016-12-30 | Fri |  53 |        52 | 2016 |      2016 |
| 2016-12-31 | Sat |  53 |        52 | 2016 |      2016 |
| 2017-01-01 | Sun |  53 |        52 | 2016 |      2016 |
| 2017-01-02 | Mon |  53 |         1 | 2016 |      2017 |
| 2017-01-03 | Tue |  53 |         1 | 2016 |      2017 |
| 2017-01-04 | Wed |   1 |         1 | 2017 |      2017 |
| 2017-01-05 | Thu |   1 |         1 | 2017 |      2017 |
| 2017-12-30 | Sat |  52 |        52 | 2017 |      2017 |
| 2017-12-31 | Sun |  52 |        52 | 2017 |      2017 |
+------------+-----+-----+-----------+------+-----------+
```

* 2016 now has 53 weeks (instead of 52).
* WOY for Jan 1st, 2017 moves to week 53 (from 52).
* WOY for Jan 2nd and 3rd, 2017 moves to week 53 (from 1).
* YOW for Jan 2nd and 3rd, 2017 moves to 2016 (from 2017).
* WOY (ISO) and YOW (ISO) are not affected by the parameter change.

The last two examples set WEEK_OF_YEAR_POLICY to `1` and set WEEK_START first to `1` (Monday) and then `3` (Wednesday):

```sqlexample
ALTER SESSION SET WEEK_OF_YEAR_POLICY=1, WEEK_START=1;

SELECT d "Date",
       DAYNAME(d) "Day",
       WEEK(d) "WOY",
       WEEKISO(d) "WOY (ISO)",
       YEAROFWEEK(d) "YOW",
       YEAROFWEEKISO(d) "YOW (ISO)"
  FROM week_examples;
```

```output
+------------+-----+-----+-----------+------+-----------+
| Date       | Day | WOY | WOY (ISO) |  YOW | YOW (ISO) |
|------------+-----+-----+-----------+------+-----------|
| 2016-12-30 | Fri |  53 |        52 | 2016 |      2016 |
| 2016-12-31 | Sat |  53 |        52 | 2016 |      2016 |
| 2017-01-01 | Sun |   1 |        52 | 2017 |      2016 |
| 2017-01-02 | Mon |   2 |         1 | 2017 |      2017 |
| 2017-01-03 | Tue |   2 |         1 | 2017 |      2017 |
| 2017-01-04 | Wed |   2 |         1 | 2017 |      2017 |
| 2017-01-05 | Thu |   2 |         1 | 2017 |      2017 |
| 2017-12-30 | Sat |  53 |        52 | 2017 |      2017 |
| 2017-12-31 | Sun |  53 |        52 | 2017 |      2017 |
+------------+-----+-----+-----------+------+-----------+
```

```sqlexample
ALTER SESSION SET week_of_year_policy=1, week_start=3;

SELECT d "Date",
       DAYNAME(d) "Day",
       WEEK(d) "WOY",
       WEEKISO(d) "WOY (ISO)",
       YEAROFWEEK(d) "YOW",
       YEAROFWEEKISO(d) "YOW (ISO)"
  FROM week_examples;
```

```output
+------------+-----+-----+-----------+------+-----------+
| Date       | Day | WOY | WOY (ISO) |  YOW | YOW (ISO) |
|------------+-----+-----+-----------+------+-----------|
| 2016-12-30 | Fri |  53 |        52 | 2016 |      2016 |
| 2016-12-31 | Sat |  53 |        52 | 2016 |      2016 |
| 2017-01-01 | Sun |   1 |        52 | 2017 |      2016 |
| 2017-01-02 | Mon |   1 |         1 | 2017 |      2017 |
| 2017-01-03 | Tue |   1 |         1 | 2017 |      2017 |
| 2017-01-04 | Wed |   2 |         1 | 2017 |      2017 |
| 2017-01-05 | Thu |   2 |         1 | 2017 |      2017 |
| 2017-12-30 | Sat |  53 |        52 | 2017 |      2017 |
| 2017-12-31 | Sun |  53 |        52 | 2017 |      2017 |
+------------+-----+-----+-----------+------+-----------+
```

* With WEEK_OF_YEAR_POLICY set to `1` and WEEK_START set to `1` (Monday):

  * WOY for `2017-01-01` is `1`.
  * Week 1 consists of 1 day.
  * Week 2 starts on `Mon`.

  This usage scenario is generally the most common.
* With WEEK_OF_YEAR_POLICY set to `1` and WEEK_START set to `3` (Wednesday):

  * WOY for 2017-01-01 is still `1`.
  * Week 1 consists of 3 days.
  * Week 2 starts on `Wed`.

In both examples, WOY (ISO) and YOW (ISO) are not affected by the parameter change.
