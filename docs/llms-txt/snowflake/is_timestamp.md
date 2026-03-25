# Source: https://docs.snowflake.com/en/sql-reference/functions/is_timestamp.md

Categories:
:   [Semi-structured and structured data functions](../functions-semistructured.md) (Type Predicates)

# IS_TIMESTAMP_\*

Verifies whether a [VARIANT](../data-types-semistructured.md) argument contains the respective
[timestamp](../data-types-datetime.md) value:

* IS_TIMESTAMP_LTZ (value with local time zone).
* IS_TIMESTAMP_NTZ (value with no time zone).
* IS_TIMESTAMP_TZ (value with time zone).

See also:
:   [IS_<object_type>](is.md) , [IS_DATE , IS_DATE_VALUE](is_date-value.md) , [IS_TIME](is_time.md)

## Syntax

```sqlsyntax
IS_TIMESTAMP_LTZ( <variant_expr> )

IS_TIMESTAMP_NTZ( <variant_expr> )

IS_TIMESTAMP_TZ( <variant_expr> )
```

## Arguments

`variant_expr`
:   An expression that evaluates to a value of type VARIANT.

## Returns

Returns a BOOLEAN value or NULL.

* Returns TRUE if the VARIANT value contains a timestamp. Otherwise, returns FALSE.
* If the input is NULL, returns NULL without reporting an error.

## Examples

Show all timestamps in a VARIANT column, with the output using the time zone specified for the session.

> **Note:**
>
> The output format for the time zone is set using a parameter:
>
> * The [TIMESTAMP_LTZ_OUTPUT_FORMAT](../parameters.md) parameter sets the format for TIMESTAMP_LTZ values.
> * The [TIMESTAMP_NTZ_OUTPUT_FORMAT](../parameters.md) parameter sets the format for TIMESTAMP_NTZ values.
> * The [TIMESTAMP_TZ_OUTPUT_FORMAT](../parameters.md) parameter sets the format for TIMESTAMP_TZ values.

In these examples, the local time zone is US Pacific Standard Time (-08:00 relative to GMT/UCT).

Create and load a table with various date and time values in a VARIANT column:

```sqlexample
CREATE OR REPLACE TABLE vardttm (v VARIANT);
```

```sqlexample
INSERT INTO vardttm SELECT TO_VARIANT(TO_DATE('2024-02-24'));
INSERT INTO vardttm SELECT TO_VARIANT(TO_TIME('20:57:01.123456789+07:00'));
INSERT INTO vardttm SELECT TO_VARIANT(TO_TIMESTAMP('2023-02-24 12:00:00.456'));
INSERT INTO vardttm SELECT TO_VARIANT(TO_TIMESTAMP_LTZ('2022-02-24 13:00:00.123 +01:00'));
INSERT INTO vardttm SELECT TO_VARIANT(TO_TIMESTAMP_NTZ('2021-02-24 14:00:00.123 +01:00'));
INSERT INTO vardttm SELECT TO_VARIANT(TO_TIMESTAMP_TZ('2020-02-24 15:00:00.123 +01:00'));
```

Use the [TYPEOF](typeof.md) function in a query to show the data types of the values stored in the VARIANT column `v`:

```sqlexample
SELECT v, TYPEOF(v) AS type FROM vardttm;
```

```output
+---------------------------------+---------------+
| V                               | TYPE          |
|---------------------------------+---------------|
| "2024-02-24"                    | DATE          |
| "20:57:01"                      | TIME          |
| "2023-02-24 12:00:00.456"       | TIMESTAMP_NTZ |
| "2022-02-24 04:00:00.123 -0800" | TIMESTAMP_LTZ |
| "2021-02-24 14:00:00.123"       | TIMESTAMP_NTZ |
| "2020-02-24 15:00:00.123 +0100" | TIMESTAMP_TZ  |
+---------------------------------+---------------+
```

Show the TIMESTAMP_NTZ values in the data by using the IS_TIMESTAMP_NTZ function in a WHERE clause:

```sqlexample
SELECT * FROM vardttm WHERE IS_TIMESTAMP_NTZ(v);
```

```output
+---------------------------+
| V                         |
|---------------------------|
| "2023-02-24 12:00:00.456" |
| "2021-02-24 14:00:00.123" |
+---------------------------+
```

Show the TIMESTAMP_LTZ values in the data by using the IS_TIMESTAMP_LTZ function in a WHERE clause:

```sqlexample
SELECT * FROM vardttm WHERE IS_TIMESTAMP_LTZ(v);
```

```output
+---------------------------------+
| V                               |
|---------------------------------|
| "2022-02-24 04:00:00.123 -0800" |
+---------------------------------+
```

Show the TIMESTAMP_TZ values in the data by using the IS_TIMESTAMP_TZ function in a WHERE clause:

```sqlexample
SELECT * FROM vardttm WHERE IS_TIMESTAMP_TZ(v);
```

```output
+---------------------------------+
| V                               |
|---------------------------------|
| "2020-02-24 15:00:00.123 +0100" |
+---------------------------------+
```
