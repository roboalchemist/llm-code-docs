# Source: https://docs.snowflake.com/en/sql-reference/functions/as_timestamp.md

Categories:
:   [Semi-structured and structured data functions](../functions-semistructured.md) (Cast)

# AS_TIMESTAMP_\*

Casts a [VARIANT](../data-types-semistructured.md) value to the respective
[timestamp](../data-types-datetime.md) value:

* AS_TIMESTAMP_LTZ (value with local time zone)
* AS_TIMESTAMP_NTZ (value with no time zone)
* AS_TIMESTAMP_TZ (value with time zone)

See also:
:   [AS_<object_type>](as.md) , [AS_DATE](as_date.md) , [AS_TIME](as_time.md)

## Syntax

```sqlsyntax
AS_TIMESTAMP_LTZ( <variant_expr> )

AS_TIMESTAMP_NTZ( <variant_expr> )

AS_TIMESTAMP_TZ( <variant_expr> )
```

## Arguments

`variant_expr`
:   An expression that evaluates to a value of type VARIANT.

## Returns

The function returns a value of a timestamp type or NULL:

* If the type of the value in the `variant_expr` argument is a timestamp type, the function returns a value of same timestamp type.

* If the type of the value in the `variant_expr` argument doesn’t match the type of the output
  value, the function returns NULL.
* If the `variant_expr` argument is NULL, the function returns NULL.

## Examples

Create a table and load data into it:

```sqlexample
CREATE OR REPLACE TABLE as_timestamp_example (timestamp1 VARIANT);

INSERT INTO as_timestamp_example (timestamp1)
  SELECT TO_VARIANT(TO_TIMESTAMP_NTZ('2024-10-10 12:34:56'));
```

Use the AS_TIMESTAMP_NTZ function in a query to cast a VARIANT value to a TIMESTAMP_NTZ value:

```sqlexample
SELECT AS_TIMESTAMP_NTZ(timestamp1) AS timestamp_value
  FROM as_timestamp_example;
```

```output
+-------------------------+
| TIMESTAMP_VALUE         |
|-------------------------|
| 2024-10-10 12:34:56.000 |
+-------------------------+
```
