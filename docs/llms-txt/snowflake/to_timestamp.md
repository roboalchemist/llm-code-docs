# Source: https://docs.snowflake.com/en/sql-reference/functions/to_timestamp.md

Categories:
:   [Conversion functions](../functions-conversion.md) , [Date & time functions](../functions-date-time.md)

# TO_TIMESTAMP / TO_TIMESTAMP_\*

Converts an input expression into the corresponding timestamp:

* TO_TIMESTAMP_LTZ (timestamp with local time zone)
* TO_TIMESTAMP_NTZ (timestamp with no time zone)
* TO_TIMESTAMP_TZ (timestamp with time zone)

> **Note:**
>
> TO_TIMESTAMP maps to one of the other timestamp functions, based on the
> [TIMESTAMP_TYPE_MAPPING](../parameters.md) session parameter. The parameter default is
> TIMESTAMP_NTZ, so TO_TIMESTAMP maps to TO_TIMESTAMP_NTZ by default.

See also:
:   [TRY_TO_TIMESTAMP / TRY_TO_TIMESTAMP_\*](try_to_timestamp.md) ,

    [AS_TIMESTAMP_\*](as_timestamp.md) , [IS_TIMESTAMP_\*](is_timestamp.md) ,

    [TO_DATE , DATE](to_date.md) , [TO_TIME , TIME](to_time.md)

## Syntax

```sqlsyntax
timestampFunction ( <numeric_expr> [ , <scale> ] )

timestampFunction ( <date_expr> )

timestampFunction ( <timestamp_expr> )

timestampFunction ( <string_expr> [ , <format> ] )

timestampFunction ( '<integer>' )

timestampFunction ( <variant_expr> )
```

Where:

> ```sqlsyntax
> timestampFunction ::=
>     TO_TIMESTAMP | TO_TIMESTAMP_LTZ | TO_TIMESTAMP_NTZ | TO_TIMESTAMP_TZ
> ```

## Arguments

**Required:**

One of:

> `numeric_expr`
> :   A number of seconds (if scale = 0 or is absent) or fractions of a second (e.g. milliseconds or nanoseconds)
> since the start of the Unix epoch (1970-01-01 00:00:00 UTC). If a non-integer decimal expression is input, the
> scale of the result is inherited.
>
> `date_expr`
> :   A date to be converted into a timestamp.
>
> `timestamp_expr`
> :   A timestamp to be converted into another timestamp (e.g. convert TIMESTAMP_LTZ to TIMESTAMP_NTZ).
>
> `string_expr`
> :   A string from which to extract a timestamp, for example `'2019-01-31 01:02:03.004'`.
>
> `'integer'`
> :   An expression that evaluates to a string containing an integer, for example `'15000000'`. Depending
> on the magnitude of the string, it can be interpreted as seconds, milliseconds, microseconds, or
> nanoseconds. For details, see the Usage Notes.
>
> `variant_expr`
> :   An expression of type VARIANT. The VARIANT must contain one of the following:
>
>     * A string from which to extract a timestamp.
>     * A timestamp.
>     * An integer that represents the number of seconds, milliseconds, microseconds, or nanoseconds.
>     * A string containing an integer that represents the number of seconds, milliseconds, microseconds, or nanoseconds.
>
>     Although TO_TIMESTAMP accepts a DATE value, it does not accept a DATE inside a VARIANT.

**Optional:**

`format`
:   Format specifier (only for `string_expr`). For more information, see [Date and time formats in conversion functions](../functions-conversion.md).

    The default value is the current value of the [TIMESTAMP_INPUT_FORMAT](../parameters.md) parameter (default
    [AUTO](../date-time-input-output.md)).

`scale`
:   Scale specifier (only for `numeric_expr`). If specified, defines the scale of the numbers provided. For example:

    * For seconds, scale = `0`.
    * For milliseconds, scale = `3`.
    * For microseconds, scale = `6`.
    * For nanoseconds, scale = `9`.

    Default: `0`

## Returns

The data type of the returned value is one of the TIMESTAMP data
types. By default, the data type is TIMESTAMP_NTZ. You can change
this by setting the session parameter [TIMESTAMP_TYPE_MAPPING](../parameters.md).

If the input is NULL, then the result is NULL.

## Usage notes

* This family of functions returns timestamp values, specifically:

  * For `string_expr`: A timestamp represented by a given string. If the string does not have a time component, midnight is used.
  * For `date_expr`: A timestamp representing midnight of a given day is used, according to the specific timestamp mapping (NTZ/LTZ/TZ) semantics.
  * For `timestamp_expr`: A timestamp with possibly different mapping than the source timestamp.
  * For `numeric_expr`: A timestamp representing the number of seconds (or fractions of a second) provided by the user. UTC time is always used to build the result.
  * For `variant_expr`:

    * If the VARIANT contains a JSON null value, the result is NULL.
    * If the VARIANT contains a timestamp value of the same kind as the result, this value is preserved as is.
    * If the VARIANT contains a timestamp value of a different kind, the conversion is done in the same way as from `timestamp_expr`.
    * If the VARIANT contains a string, conversion from a string value is performed (using automatic format).
    * If the VARIANT contains a number, conversion from `numeric_expr` is performed.

      > **Note:**
      >
      > When an INTEGER value is cast directly to TIMESTAMP_NTZ, the integer is treated as the number of seconds
      > since the beginning of the Linux epoch, and the local time zone is not taken into account. However, if the
      > INTEGER value is stored inside a VARIANT value, for example as shown below, then the conversion is indirect,
      > and is affected by the local time zone, even though the final result is TIMESTAMP_NTZ:
      >
      > ```sqlexample
      > SELECT TO_TIMESTAMP(31000000);
      > SELECT TO_TIMESTAMP(PARSE_JSON(31000000));
      > SELECT PARSE_JSON(31000000)::TIMESTAMP_NTZ;
      > ```
      >
      > The timestamp returned by the first query is different from the time returned by the second and
      > third queries.
      >
      > To convert independently of the local time zone, add an explicit cast to integer in the expression, as shown
      > below:
      >
      > ```sqlexample
      > SELECT TO_TIMESTAMP(31000000);
      > SELECT TO_TIMESTAMP(PARSE_JSON(31000000)::INT);
      > SELECT PARSE_JSON(31000000)::INT::TIMESTAMP_NTZ;
      > ```
      >
      > The timestamp returned by all three queries is the same. This applies whether casting to TIMESTAMP_NTZ or calling the
      > function TO_TIMESTAMP_NTZ. It also applies when calling TO_TIMESTAMP when the TIMESTAMP_TYPE_MAPPING parameter
      > is set to TIMESTAMP_NTZ.
      >
      > For an example with output, see the examples at the end of this topic.
  * If conversion is not possible, an error is returned.
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

This example shows that TO_TIMESTAMP_TZ creates a timestamp that contains a time
zone from the session, but the value from TO_TIMESTAMP_NTZ does not have a
time zone:

```sqlexample
ALTER SESSION SET TIMEZONE = 'America/Los_Angeles';
```

```sqlexample
SELECT TO_TIMESTAMP_TZ('2024-04-05 01:02:03');
```

```output
+----------------------------------------+
| TO_TIMESTAMP_TZ('2024-04-05 01:02:03') |
|----------------------------------------|
| 2024-04-05 01:02:03.000 -0700          |
+----------------------------------------+
```

```sqlexample
SELECT TO_TIMESTAMP_NTZ('2024-04-05 01:02:03');
```

```output
+-----------------------------------------+
| TO_TIMESTAMP_NTZ('2024-04-05 01:02:03') |
|-----------------------------------------|
| 2024-04-05 01:02:03.000                 |
+-----------------------------------------+
```

The following examples show how different formats can influence the parsing of an ambiguous date.
Assume that the [TIMESTAMP_TZ_OUTPUT_FORMAT](../parameters.md) is not set, so the
[TIMESTAMP_OUTPUT_FORMAT](../parameters.md) is used and is set to the default
(`YYYY-MM-DD HH24:MI:SS.FF3 TZHTZM`).

This example shows the results when the input format is `mm/dd/yyyy hh24:mi:ss` (month/day/year):

```sqlexample
SELECT TO_TIMESTAMP_TZ('04/05/2024 01:02:03', 'mm/dd/yyyy hh24:mi:ss');
```

```output
+-----------------------------------------------------------------+
| TO_TIMESTAMP_TZ('04/05/2024 01:02:03', 'MM/DD/YYYY HH24:MI:SS') |
|-----------------------------------------------------------------|
| 2024-04-05 01:02:03.000 -0700                                   |
+-----------------------------------------------------------------+
```

This example shows the results when the input format is `dd/mm/yyyy hh24:mi:ss` (day/month/year):

```sqlexample
SELECT TO_TIMESTAMP_TZ('04/05/2024 01:02:03', 'dd/mm/yyyy hh24:mi:ss');
```

```output
+-----------------------------------------------------------------+
| TO_TIMESTAMP_TZ('04/05/2024 01:02:03', 'DD/MM/YYYY HH24:MI:SS') |
|-----------------------------------------------------------------|
| 2024-05-04 01:02:03.000 -0700                                   |
+-----------------------------------------------------------------+
```

This example shows how to use a numeric input that represents approximately 40
years from midnight January 1, 1970 (the start of the Unix epoch). The scale
is not specified, so the default scale of `0` (seconds) is used.

```sqlexample
ALTER SESSION SET TIMESTAMP_OUTPUT_FORMAT = 'YYYY-MM-DD HH24:MI:SS.FF9 TZH:TZM';
```

```sqlexample
SELECT TO_TIMESTAMP_NTZ(40 * 365.25 * 86400);
```

```output
+---------------------------------------+
| TO_TIMESTAMP_NTZ(40 * 365.25 * 86400) |
|---------------------------------------|
| 2010-01-01 00:00:00.000               |
+---------------------------------------+
```

This example is similar to the preceding example, but provides the value as milliseconds
by specifying a scale value of `3`:

```sqlexample
SELECT TO_TIMESTAMP_NTZ(40 * 365.25 * 86400 * 1000 + 456, 3);
```

```output
+-------------------------------------------------------+
| TO_TIMESTAMP_NTZ(40 * 365.25 * 86400 * 1000 + 456, 3) |
|-------------------------------------------------------|
| 2010-01-01 00:00:00.456                               |
+-------------------------------------------------------+
```

This example shows how the results change when different scale values are specified for the same
numeric value:

```sqlexample
SELECT TO_TIMESTAMP(1000000000, 0) AS "Scale in seconds",
       TO_TIMESTAMP(1000000000, 3) AS "Scale in milliseconds",
       TO_TIMESTAMP(1000000000, 6) AS "Scale in microseconds",
       TO_TIMESTAMP(1000000000, 9) AS "Scale in nanoseconds";
```

```output
+-------------------------+-------------------------+-------------------------+-------------------------+
| Scale in seconds        | Scale in milliseconds   | Scale in microseconds   | Scale in nanoseconds    |
|-------------------------+-------------------------+-------------------------+-------------------------|
| 2001-09-09 01:46:40.000 | 1970-01-12 13:46:40.000 | 1970-01-01 00:16:40.000 | 1970-01-01 00:00:01.000 |
+-------------------------+-------------------------+-------------------------+-------------------------+
```

This example shows how the function determines the units to use (seconds, milliseconds, microseconds, or nanoseconds)
when the input is a string that contains an integer, based on the magnitude of the value.

Create and load the table with strings containing integers within different ranges:

```sqlexample
CREATE OR REPLACE TABLE demo1 (
  description VARCHAR,
  value VARCHAR -- string rather than bigint
);

INSERT INTO demo1 (description, value) VALUES
  ('Seconds',      '31536000'),
  ('Milliseconds', '31536000000'),
  ('Microseconds', '31536000000000'),
  ('Nanoseconds',  '31536000000000000');
```

Pass the strings to the function:

```sqlexample
SELECT description,
       value,
       TO_TIMESTAMP(value),
       TO_DATE(value)
  FROM demo1
  ORDER BY value;
```

```output
+--------------+-------------------+-------------------------+----------------+
| DESCRIPTION  | VALUE             | TO_TIMESTAMP(VALUE)     | TO_DATE(VALUE) |
|--------------+-------------------+-------------------------+----------------|
| Seconds      | 31536000          | 1971-01-01 00:00:00.000 | 1971-01-01     |
| Milliseconds | 31536000000       | 1971-01-01 00:00:00.000 | 1971-01-01     |
| Microseconds | 31536000000000    | 1971-01-01 00:00:00.000 | 1971-01-01     |
| Nanoseconds  | 31536000000000000 | 1971-01-01 00:00:00.000 | 1971-01-01     |
+--------------+-------------------+-------------------------+----------------+
```

The following example casts values to TIMESTAMP_NTZ. The example shows the difference in
behavior between using an integer and using a variant that contains an integer:

```sqlexample
SELECT 0::TIMESTAMP_NTZ, PARSE_JSON(0)::TIMESTAMP_NTZ, PARSE_JSON(0)::INT::TIMESTAMP_NTZ;
```

```output
+-------------------------+------------------------------+-----------------------------------+
| 0::TIMESTAMP_NTZ        | PARSE_JSON(0)::TIMESTAMP_NTZ | PARSE_JSON(0)::INT::TIMESTAMP_NTZ |
|-------------------------+------------------------------+-----------------------------------|
| 1970-01-01 00:00:00.000 | 1969-12-31 16:00:00.000      | 1970-01-01 00:00:00.000           |
+-------------------------+------------------------------+-----------------------------------+
```

The returned timestamps match for an integer and for a variant cast to an integer in the
first and third columns, but the returned timestamp is different for the variant that is not
cast to an integer in the second column. For more information, see
Usage notes.

This same behavior applies when calling the TO_TIMESTAMP_NTZ function:

```sqlexample
SELECT TO_TIMESTAMP_NTZ(0), TO_TIMESTAMP_NTZ(PARSE_JSON(0)), TO_TIMESTAMP_NTZ(PARSE_JSON(0)::INT);
```

```output
+-------------------------+---------------------------------+--------------------------------------+
| TO_TIMESTAMP_NTZ(0)     | TO_TIMESTAMP_NTZ(PARSE_JSON(0)) | TO_TIMESTAMP_NTZ(PARSE_JSON(0)::INT) |
|-------------------------+---------------------------------+--------------------------------------|
| 1970-01-01 00:00:00.000 | 1969-12-31 16:00:00.000         | 1970-01-01 00:00:00.000              |
+-------------------------+---------------------------------+--------------------------------------+
```
