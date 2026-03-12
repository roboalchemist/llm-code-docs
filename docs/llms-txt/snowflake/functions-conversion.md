# Source: https://docs.snowflake.com/en/sql-reference/functions-conversion.md

# Conversion functions

This family of functions can be used to convert an expression of any Snowflake data type to another data type.

## List of functions

| Sub-category | Function | Notes |
| --- | --- | --- |
| **Any data type** | [CAST , ::](functions/cast.md) |  |
| [TRY_CAST](functions/try_cast.md) | Error-handling version of CAST. |
| **Text/character/binary data types** | [TO_CHAR , TO_VARCHAR](functions/to_char.md) |  |
| [TO_BINARY](functions/to_binary.md) |  |
| [TRY_TO_BINARY](functions/try_to_binary.md) | Error-handling version to TO_BINARY. |
| **Numeric data types** | [TO_DECFLOAT](functions/to_decfloat.md) |  |
| [TO_DECIMAL , TO_NUMBER , TO_NUMERIC](functions/to_decimal.md) |  |
| [TO_DOUBLE](functions/to_double.md) |  |
| [TRY_TO_DECFLOAT](functions/try_to_decfloat.md) | Error-handling version of TO_DECFLOAT. |
| [TRY_TO_DECIMAL, TRY_TO_NUMBER, TRY_TO_NUMERIC](functions/try_to_decimal.md) | Error-handling versions of TO_DECIMAL, TO_NUMBER, and so on. |
| [TRY_TO_DOUBLE](functions/try_to_double.md) | Error-handling version of TO_DOUBLE. |
| **Boolean data type** | [TO_BOOLEAN](functions/to_boolean.md) |  |
| [TRY_TO_BOOLEAN](functions/try_to_boolean.md) | Error-handling version of TO_BOOLEAN. |
| **Date and time data types** | [TO_DATE , DATE](functions/to_date.md) |  |
| [TO_TIME , TIME](functions/to_time.md) |  |
| [TO_TIMESTAMP / TO_TIMESTAMP_\*](functions/to_timestamp.md) |  |
| [TRY_TO_DATE](functions/try_to_date.md) | Error-handling version of TO_DATE. |
| [TRY_TO_TIME](functions/try_to_time.md) | Error-handling version of TO_TIME. |
| [TRY_TO_TIMESTAMP / TRY_TO_TIMESTAMP_\*](functions/try_to_timestamp.md) | Error-handling versions of TO_TIMESTAMP, and so on. |
| **Semi-structured data types** | [TO_ARRAY](functions/to_array.md) |  |
| [TO_OBJECT](functions/to_object.md) |  |
| [TO_VARIANT](functions/to_variant.md) |  |
| **Geospatial data types** | [TO_GEOGRAPHY](functions/to_geography.md) |  |
| [TRY_TO_GEOGRAPHY](functions/try_to_geography.md) | Error-handling version of TO_GEOGRAPHY |
| [ST_GEOGFROMGEOHASH](functions/st_geogfromgeohash.md) |  |
| [ST_GEOGPOINTFROMGEOHASH](functions/st_geogpointfromgeohash.md) |  |
| [ST_GEOGRAPHYFROMWKB](functions/st_geographyfromwkb.md) |  |
| [ST_GEOGRAPHYFROMWKT](functions/st_geographyfromwkt.md) |  |
| [TO_GEOMETRY](functions/to_geometry.md) |  |
| [TRY_TO_GEOMETRY](functions/try_to_geometry.md) | Error-handling version of TO_GEOMETRY |
| [ST_GEOMETRYFROMWKB](functions/st_geometryfromwkb.md) |  |
| [ST_GEOMETRYFROMWKT](functions/st_geometryfromwkt.md) |  |

## Error-handling conversion functions

Conversion functions with a TRY_ prefix are special versions of their respective conversion functions. These functions return a NULL value instead of raising an error when the conversion cannot be performed:

* [TRY_CAST](functions/try_cast.md)
* [TRY_TO_BINARY](functions/try_to_binary.md)
* [TRY_TO_BOOLEAN](functions/try_to_boolean.md)
* [TRY_TO_DATE](functions/try_to_date.md)
* [TRY_TO_DECIMAL, TRY_TO_NUMBER, TRY_TO_NUMERIC](functions/try_to_decimal.md)
* [TRY_TO_DOUBLE](functions/try_to_double.md)
* [TRY_TO_GEOGRAPHY](functions/try_to_geography.md)
* [TRY_TO_GEOMETRY](functions/try_to_geometry.md)
* [TRY_TO_TIME](functions/try_to_time.md)
* [TRY_TO_TIMESTAMP / TRY_TO_TIMESTAMP_\*](functions/try_to_timestamp.md)

These functions only support string expressions (i.e. VARCHAR or CHAR data type) as input.

> **Important:**
>
> These error-handling conversion functions are optimized for situations where conversion errors are relatively infrequent:
>
> * If there are no (or very few) errors, they should result in no visible performance impact.
> * If there are a large number of conversion failures, using these functions can result in significantly slower performance. Also, when using them with the VARIANT type, some operations might result in reduced performance.

## Numeric formats in conversion functions

The functions
[TO_DECIMAL , TO_NUMBER , TO_NUMERIC](functions/to_decimal.md), and
[TO_DOUBLE](functions/to_double.md)
accept an optional parameter that specifies the format of the input string,
if the input expression evaluates to a string. For more information
about the values this parameter can have, see
[SQL format models](sql-format-models.md).

## Date and time formats in conversion functions

The following functions allow you to specify the expected date, time, or timestamp format to parse or produce a string:

* [TO_CHAR , TO_VARCHAR](functions/to_char.md)
* [TO_DATE , DATE](functions/to_date.md)
* [TRY_TO_DATE](functions/try_to_date.md)
* [TO_TIME , TIME](functions/to_time.md)
* [TRY_TO_TIME](functions/try_to_time.md)
* [TO_TIMESTAMP / TO_TIMESTAMP_\*](functions/to_timestamp.md)
* [TRY_TO_TIMESTAMP / TRY_TO_TIMESTAMP_\*](functions/try_to_timestamp.md)

You specify the format in an optional argument, using the following case-insensitive elements to describe the format:

| Format element | Description |
| --- | --- |
| `YYYY` | Four-digit [1] year. |
| `YY` | Two-digit [1] year, controlled by the [TWO_DIGIT_CENTURY_START](parameters.md) session parameter. For example, when set to `1980`, values of `79` and `80` are parsed as `2079` and `1980`, respectively. |
| `MM` | Two-digit [1] month (`01` = January, and so on). |
| `MON` | Abbreviated month name [2]. |
| `MMMM` | Full month name [2]. |
| `DD` | Two-digit [1] day of month (`01` through `31`). |
| `DY` | Abbreviated day of week. |
| `HH24` | Two digits [1] for hour (`00` through `23`). You must not specify `AM` / `PM`. |
| `HH12` | Two digits [1] for hour (`01` through `12`). You can specify `AM` / `PM`. |
| `AM` , `PM` | Ante meridiem (`AM`) / post meridiem (`PM`). Use this only with `HH12` (not with `HH24`). |
| `MI` | Two digits [1] for minute (`00` through `59`). |
| `SS` | Two digits [1] for second (`00` through `59`). |
| `FF[0-9]` | Fractional seconds with precision `0` (seconds) to `9` (nanoseconds), e.g. `FF`, `FF0`, `FF3`, `FF9`. Specifying `FF` is equivalent to `FF9` (nanoseconds). |
| `TZH:TZM` , `TZHTZM` , `TZH` | Two-digit [1] time zone hour and minute, offset from UTC. Can be prefixed by `+`/`-` for sign. |
| `UUUU` | Four-digit year in [ISO format](https://en.wikipedia.org/wiki/ISO_8601), which are negative for BCE years. |

[1] The number of digits describes the output produced when serializing values to text. When parsing text, Snowflake accepts up to the specified number of digits. For example, a day number can be one or two digits.

[2] For the MON format element, the output produced when serializing values to text is the abbreviated month name. For the MMMM format element, the output produced when serializing values to text is the full month name. When parsing text, Snowflake accepts the three-digit abbreviation or the full month name for both MON and MMMM. For example, “January” or “Jan”, “February” or “Feb”, and so on are accepted when parsing text.

> **Note:**
>
> * When a date-only format is used, the associated time is assumed to be midnight on that day.
> * Anything in the format between double quotes or other than the above elements is parsed/formatted without being interpreted.
> * For more details about valid ranges, number of digits, and best practices, see
>   [Additional information about using date, time, and timestamp formats](date-time-input-output.md).

### Usage notes

Anything in the format between double quotes or other than the above elements is parsed/formatted without being interpreted.

### Examples

Convert a string to a date using a specified input format of `dd/mm/yyyy`. The display format for dates in the output
is determined by the [DATE_OUTPUT_FORMAT](parameters.md) session parameter (default `YYYY-MM-DD`).

```sqlexample
SELECT TO_DATE('3/4/2024', 'dd/mm/yyyy');
```

```output
+-----------------------------------+
| TO_DATE('3/4/2024', 'DD/MM/YYYY') |
|-----------------------------------|
| 2024-04-03                        |
+-----------------------------------+
```

Convert a date to a string, and specify a [date output format](parameters.md)
of `mon dd, yyyy`.

```sqlexample
SELECT TO_VARCHAR('2024-04-05'::DATE, 'mon dd, yyyy');
```

```output
+------------------------------------------------+
| TO_VARCHAR('2024-04-05'::DATE, 'MON DD, YYYY') |
|------------------------------------------------|
| Apr 05, 2024                                   |
+------------------------------------------------+
```

## Binary formats in conversion functions

[TO_CHAR , TO_VARCHAR](functions/to_char.md), and [TO_BINARY](functions/to_binary.md) accept an optional
argument specifying the expected format to parse or produce a string.

The format can be one of the following strings (case-insensitive):

> * HEX
> * BASE64
> * UTF-8

For more information about these formats, see [Overview of supported binary formats](binary-input-output.md).

For examples of using these formats, see the Examples section of
[Binary input and output](binary-input-output.md).
