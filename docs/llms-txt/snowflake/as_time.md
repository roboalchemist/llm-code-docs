# Source: https://docs.snowflake.com/en/sql-reference/functions/as_time.md

Categories:
:   [Semi-structured and structured data functions](../functions-semistructured.md) (Cast)

# AS_TIME

Casts a [VARIANT](../data-types-semistructured.md) value to a [TIME](../data-types-datetime.md) value. This function does not convert values of
other data types, including timestamps, to TIME values.

See also:
:   [AS_<object_type>](as.md)

    [AS_DATE](as_date.md) , [AS_TIMESTAMP_\*](as_timestamp.md)

## Syntax

```sqlsyntax
AS_TIME( <variant_expr> )
```

## Arguments

`variant_expr`
:   An expression that evaluates to a value of type VARIANT.

## Returns

The function returns a value of type TIME or NULL:

* If the type of the value in the `variant_expr` argument is TIME, the function returns a value of type TIME.

* If the type of the value in the `variant_expr` argument doesn’t match the type of the output
  value, the function returns NULL.
* If the `variant_expr` argument is NULL, the function returns NULL.

## Examples

Create a table and load data into it:

```sqlexample
CREATE OR REPLACE TABLE as_time_example (time1 VARIANT);

INSERT INTO as_time_example (time1)
  SELECT TO_VARIANT(TO_TIME('12:34:56'));
```

Use the AS_TIME function in a query to cast a VARIANT value to a TIME value:

```sqlexample
SELECT AS_TIME(time1) AS time_value
  FROM as_time_example;
```

```output
+------------+
| TIME_VALUE |
|------------|
| 12:34:56   |
+------------+
```
