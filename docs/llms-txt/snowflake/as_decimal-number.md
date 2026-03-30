# Source: https://docs.snowflake.com/en/sql-reference/functions/as_decimal-number.md

Categories:
:   [Semi-structured and structured data functions](../functions-semistructured.md) (Cast)

# AS_DECIMAL , AS_NUMBER

Casts a [VARIANT](../data-types-semistructured.md) value to a fixed-point [NUMBER](../data-types-numeric.md) value, with optional precision and scale.
This function doesn’t cast floating-point values.

AS_DECIMAL is a synonym for AS_NUMBER.

The [DECIMAL](../data-types-numeric.md) data type is synonymous with the NUMBER data type.

See also:
:   [AS_<object_type>](as.md) , [AS_DOUBLE , AS_REAL](as_double-real.md) , [AS_INTEGER](as_integer.md)

## Syntax

```sqlsyntax
AS_DECIMAL( <variant_expr> [ , <precision> [ , <scale> ] ] )

AS_NUMBER( <variant_expr> [ , <precision> [ , <scale> ] ] )
```

## Arguments

`variant_expr`
:   An expression that evaluates to a value of type VARIANT.

`precision`
:   The number of significant digits of the decimal number to store.

    The default is `38`.

`scale`
:   The number of significant digits after the decimal point.

    The default is `0`.

## Returns

The function returns a value of type NUMBER or NULL:

* If the type of the value in the `variant_expr` argument is DECIMAL or NUMBER, the function returns a value of type NUMBER.

* If the type of the value in the `variant_expr` argument doesn’t match the type of the output
  value, the function returns NULL.
* If the `variant_expr` argument is NULL, the function returns NULL.

## Usage notes

When reducing scale, this function rounds the result, which can cause out-of-range errors.

## Examples

Create a table and load data into it:

```sqlexample
CREATE OR REPLACE TABLE as_number_example (number1 VARIANT);

INSERT INTO as_number_example (number1)
  SELECT TO_VARIANT(TO_NUMBER(2.34, 6, 3));
```

Use the AS_NUMBER function in a query to cast a VARIANT value to a NUMBER value:

```sqlexample
SELECT AS_NUMBER(number1, 6, 3) number_value
  FROM as_number_example;
```

```output
+--------------+
| NUMBER_VALUE |
|--------------|
|        2.340 |
+--------------+
```
