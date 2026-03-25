# Source: https://docs.snowflake.com/en/sql-reference/functions/as_integer.md

Categories:
:   [Semi-structured and structured data functions](../functions-semistructured.md) (Cast)

# AS_INTEGER

Casts a [VARIANT](../data-types-semistructured.md) value to an [INTEGER](../data-types-numeric.md). The function does
not cast non-integer values.

The INTEGER data type is synonymous with the [NUMBER](../data-types-numeric.md) data type, except that precision
and scale can’t be specified for INTEGER values.

See also:
:   [AS_<object_type>](as.md)

    [AS_DECIMAL , AS_NUMBER](as_decimal-number.md) , [AS_DOUBLE , AS_REAL](as_double-real.md)

## Syntax

```sqlsyntax
AS_INTEGER( <variant_expr> )
```

## Arguments

`variant_expr`
:   An expression that evaluates to a value of type VARIANT.

## Returns

The function returns a value of type INTEGER or NULL:

* If the type of the value in the `variant_expr` argument is INTEGER, the function returns a value of type INTEGER.

* If the type of the value in the `variant_expr` argument doesn’t match the type of the output
  value, the function returns NULL.
* If the `variant_expr` argument is NULL, the function returns NULL.

## Examples

Create a table and load data into it:

```sqlexample
CREATE OR REPLACE TABLE as_integer_example (integer1 VARIANT);

INSERT INTO as_integer_example (integer1)
  SELECT TO_VARIANT(15);
```

Use the AS_INTEGER function in a query to cast a VARIANT value to an INTEGER value:

```sqlexample
SELECT AS_INTEGER(integer1) AS integer_value
  FROM as_integer_example;
```

```output
+---------------+
| INTEGER_VALUE |
|---------------|
|            15 |
+---------------+
```
