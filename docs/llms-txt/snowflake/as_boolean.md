# Source: https://docs.snowflake.com/en/sql-reference/functions/as_boolean.md

Categories:
:   [Semi-structured and structured data functions](../functions-semistructured.md) (Cast)

# AS_BOOLEAN

Casts a [VARIANT](../data-types-semistructured.md) value to a [BOOLEAN](../data-types-logical.md) value.

See also:
:   [AS_<object_type>](as.md)

## Syntax

```sqlsyntax
AS_BOOLEAN( <variant_expr> )
```

## Arguments

`variant_expr`
:   An expression that evaluates to a value of type VARIANT.

## Returns

The function returns a value of type BOOLEAN or NULL:

* If the type of the value in the `variant_expr` argument is BOOLEAN, the function returns a value of type BOOLEAN.

* If the type of the value in the `variant_expr` argument doesn’t match the type of the output
  value, the function returns NULL.
* If the `variant_expr` argument is NULL, the function returns NULL.

## Examples

Create a table and load data into it:

```sqlexample
CREATE OR REPLACE TABLE as_boolean_example (
  boolean1 VARIANT,
  boolean2 VARIANT);

INSERT INTO as_boolean_example (boolean1, boolean2)
  SELECT
    TO_VARIANT(TO_BOOLEAN(TRUE)),
    TO_VARIANT(TO_BOOLEAN(FALSE));
```

Use the AS_BOOLEAN function in a query to cast VARIANT values to BOOLEAN values:

```sqlexample
SELECT AS_BOOLEAN(boolean1) boolean_true,
       AS_BOOLEAN(boolean2) boolean_false
  FROM as_boolean_example;
```

```output
+--------------+---------------+
| BOOLEAN_TRUE | BOOLEAN_FALSE |
|--------------+---------------|
| True         | False         |
+--------------+---------------+
```
