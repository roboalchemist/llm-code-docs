# Source: https://docs.snowflake.com/en/sql-reference/functions/convert_timezone.md

Categories:
:   [Date & time functions](../functions-date-time.md)

# CONVERT_TIMEZONE

Converts a timestamp to another time zone.

## Syntax

```sqlsyntax
CONVERT_TIMEZONE( <source_tz> , <target_tz> , <source_timestamp_ntz> )

CONVERT_TIMEZONE( <target_tz> , <source_timestamp> )
```

## Arguments

`source_tz`
:   String specifying the time zone for the input timestamp. Required for timestamps with no time zone (i.e. TIMESTAMP_NTZ).

`target_tz`
:   String specifying the time zone to which the input timestamp is converted.

`source_timestamp_ntz`
:   For the 3-argument version, string specifying the timestamp to convert (must be TIMESTAMP_NTZ).

`source_timestamp`
:   For the 2-argument version, string specifying the timestamp to convert (can be any timestamp variant, including TIMESTAMP_NTZ).

## Returns

Returns a value of type TIMESTAMP_NTZ, TIMESTAMP_TZ, or NULL:

* For the 3-argument version, returns a value of type TIMESTAMP_NTZ.
* For the 2-argument version, returns a value of type TIMESTAMP_TZ.
* If any argument is NULL, returns NULL.

## Usage notes

* The display format for timestamps in the output is determined by the
  [timestamp output format](../date-time-input-output.md) for the current
  session and the data type of the returned timestamp value.
* For the 3-argument version, the “wallclock” time in the result represents the same moment in time as the input “wallclock”
  in the input time zone, but in the target time zone.
* For the 2-argument version, the `source_timestamp` argument typically includes the time zone. If the value
  is of type TIMESTAMP_TZ, the time zone is taken from its value. Otherwise, the current session time zone is used.
* For `source_tz` and `target_tz`, you can specify a [time zone name](https://data.iana.org/time-zones/tzdb-2025b/zone1970.tab) or a [link name](https://data.iana.org/time-zones/tzdb-2025b/backward) from release
  2025b of the [IANA Time Zone Database](https://www.iana.org/time-zones) (for example, `America/Los_Angeles`, `Europe/London`, `UTC`,
  `Etc/GMT`, and so on).

  > **Note:**
  > * Time zone names are case-sensitive and must be enclosed in single quotes (e.g. `'UTC'`).
  > * Snowflake does not support the majority of timezone [abbreviations](https://en.wikipedia.org/wiki/List_of_time_zone_abbreviations) (e.g. `PDT`, `EST`, etc.) because a
  >   given abbreviation might refer to one of several different time zones. For example, `CST` might refer to Central
  >   Standard Time in North America (UTC-6), Cuba Standard Time (UTC-5), and China Standard Time (UTC+8).

## Examples

To use the default [timestamp output format](../date-time-input-output.md)
for the timestamps returned in the examples, unset the TIMESTAMP_OUTPUT_FORMAT parameter in the current session:

```sqlexample
ALTER SESSION UNSET TIMESTAMP_OUTPUT_FORMAT;
```

### Examples that specify a source time zone

The following examples use the 3-argument version of the CONVERT_TIMEZONE function and specify a `source_tz`
value. These examples return TIMESTAMP_NTZ values.

Convert a “wallclock” time in Los Angeles to the matching “wallclock” time in New York:

```sqlexample
SELECT CONVERT_TIMEZONE(
  'America/Los_Angeles',
  'America/New_York',
  '2024-01-01 14:00:00'::TIMESTAMP_NTZ
) AS conv;
```

```output
+-------------------------+
| CONV                    |
|-------------------------|
| 2024-01-01 17:00:00.000 |
+-------------------------+
```

Convert a “wallclock” time in Warsaw to the matching “wallclock” time in UTC:

```sqlexample
SELECT CONVERT_TIMEZONE(
  'Europe/Warsaw',
  'UTC',
  '2024-01-01 00:00:00'::TIMESTAMP_NTZ
) AS conv;
```

```output
+-------------------------+
| CONV                    |
|-------------------------|
| 2023-12-31 23:00:00.000 |
+-------------------------+
```

### Examples that do not specify a source time zone

The following examples use the 2-argument version of the CONVERT_TIMEZONE function. These examples return
TIMESTAMP_TZ values. Therefore, the returned values include an offset that shows the difference between
the timestamp’s time zone and Coordinated Universal Time (UTC). For example, the `America/Los_Angeles`
time zone has an offset of `-0700` to show that it is seven hours behind UTC.

Convert a string specifying a TIMESTAMP_TZ value to a different time zone:

```sqlexample
SELECT CONVERT_TIMEZONE(
  'America/Los_Angeles',
  '2024-04-05 12:00:00 +02:00'
) AS time_in_la;
```

```output
+-------------------------------+
| TIME_IN_LA                    |
|-------------------------------|
| 2024-04-05 03:00:00.000 -0700 |
+-------------------------------+
```

Show the current “wallclock” time in different time zones:

```sqlexample
SELECT
  CURRENT_TIMESTAMP() AS now_in_la,
  CONVERT_TIMEZONE('America/New_York', CURRENT_TIMESTAMP()) AS now_in_nyc,
  CONVERT_TIMEZONE('Europe/Paris', CURRENT_TIMESTAMP()) AS now_in_paris,
  CONVERT_TIMEZONE('Asia/Tokyo', CURRENT_TIMESTAMP()) AS now_in_tokyo;
```

```output
+-------------------------------+-------------------------------+-------------------------------+-------------------------------+
| NOW_IN_LA                     | NOW_IN_NYC                    | NOW_IN_PARIS                  | NOW_IN_TOKYO                  |
|-------------------------------+-------------------------------+-------------------------------+-------------------------------|
| 2024-06-12 08:52:53.114 -0700 | 2024-06-12 11:52:53.114 -0400 | 2024-06-12 17:52:53.114 +0200 | 2024-06-13 00:52:53.114 +0900 |
+-------------------------------+-------------------------------+-------------------------------+-------------------------------+
```
