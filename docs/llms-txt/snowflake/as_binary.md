# Source: https://docs.snowflake.com/en/sql-reference/functions/as_binary.md

Categories:
:   [Semi-structured and structured data functions](../functions-semistructured.md) (Cast)

# AS_BINARY

Casts a [VARIANT](../data-types-semistructured.md) value to a [BINARY](../data-types-text.md) value.

See also:
:   [AS_<object_type>](as.md)

## Syntax

```sqlsyntax
AS_BINARY( <variant_expr> )
```

## Arguments

`variant_expr`
:   An expression that evaluates to a value of type VARIANT.

## Returns

The function returns a value of type BINARY or NULL:

* If the type of the value in the `variant_expr` argument is BINARY, the function returns a value of type BINARY.

* If the type of the value in the `variant_expr` argument doesn’t match the type of the output
  value, the function returns NULL.
* If the `variant_expr` argument is NULL, the function returns NULL.

## Examples

Create a table and load data into it:

```sqlexample
CREATE OR REPLACE TABLE as_binary_example (binary1 VARIANT);

INSERT INTO as_binary_example (binary1)
  SELECT TO_VARIANT(TO_BINARY('F0A5'));
```

Use the AS_BINARY function in a query to cast a VARIANT value to a BINARY value:

```sqlexample
SELECT AS_BINARY(binary1) AS binary_value
  FROM as_binary_example;
```

```output
+--------------+
| BINARY_VALUE |
|--------------|
| F0A5         |
+--------------+
```
