# Source: https://docs.snowflake.com/en/sql-reference/functions/is_date-value.md

Categories:
:   [Semi-structured and structured data functions](../functions-semistructured.md) (Type Predicates)

# IS_DATE , IS_DATE_VALUE

Returns TRUE if its [VARIANT](../data-types-semistructured.md) argument contains a [DATE](../data-types-datetime.md) value.

IS_DATE and IS_DATE_VALUE are synonymous.

See also:
:   [IS_<object_type>](is.md) , [IS_TIME](is_time.md) , [IS_TIMESTAMP_\*](is_timestamp.md)

## Syntax

```sqlsyntax
IS_DATE( <variant_expr> )

IS_DATE_VALUE( <variant_expr> )
```

## Arguments

`variant_expr`
:   An expression that evaluates to a value of type VARIANT.

## Returns

Returns a BOOLEAN value or NULL.

* Returns TRUE if the VARIANT value contains a DATE value. Otherwise, returns FALSE.
* If the input is NULL, returns NULL without reporting an error.

## Examples

Return all of the DATE values in a VARIANT column.

> **Note:**
>
> The output format for date values is set using the [DATE_OUTPUT_FORMAT](../parameters.md) parameter.
> The default setting is `YYYY-MM-DD`.

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

Show the DATE values in the data by using the IS_DATE function in a WHERE clause. Only the DATE value
is returned in the output. The TIME and TIMESTAMP values aren’t returned.

```sqlexample
SELECT v FROM vardttm WHERE IS_DATE(v);
```

```output
+--------------+
| V            |
|--------------|
| "2024-02-24" |
+--------------+
```
