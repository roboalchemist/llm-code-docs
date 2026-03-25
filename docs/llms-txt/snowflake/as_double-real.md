# Source: https://docs.snowflake.com/en/sql-reference/functions/as_double-real.md

Categories:
:   [Semi-structured and structured data functions](../functions-semistructured.md) (Cast)

# AS_DOUBLE , AS_REAL

Casts a [VARIANT](../data-types-semistructured.md) value to a [floating-point value](../data-types-numeric.md).

AS_DOUBLE is a synonym for AS_REAL.

The [DOUBLE and REAL](../data-types-numeric.md) data types are synonymous with the FLOAT data type.

See also:
:   [AS_<object_type>](as.md) , [AS_DECIMAL , AS_NUMBER](as_decimal-number.md) , [AS_INTEGER](as_integer.md)

## Syntax

```sqlsyntax
AS_DOUBLE( <variant_expr> )

AS_REAL( <variant_expr> )
```

## Arguments

`variant_expr`
:   An expression that evaluates to a value of type VARIANT.

## Returns

The function returns a floating-point value or NULL:

* If the type of the value in the `variant_expr` argument is a floating-point value, the function returns the floating-point value.

* If the type of the value in the `variant_expr` argument doesn’t match the type of the output
  value, the function returns NULL.
* If the `variant_expr` argument is NULL, the function returns NULL.

## Examples

Create a table and load data into it:

```sqlexample
CREATE OR REPLACE TABLE as_double_example (double1 VARIANT);

INSERT INTO as_double_example (double1)
  SELECT TO_VARIANT(TO_DOUBLE(1.23));
```

Use the AS_DOUBLE function in a query to cast a VARIANT value to a DOUBLE value:

```sqlexample
SELECT AS_DOUBLE(double1) double_value
  FROM as_double_float_example;
```

```output
+--------------+
| DOUBLE_VALUE |
|--------------|
|         1.23 |
+--------------+
```
