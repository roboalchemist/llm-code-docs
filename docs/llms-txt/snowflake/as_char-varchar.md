# Source: https://docs.snowflake.com/en/sql-reference/functions/as_char-varchar.md

Categories:
:   [Semi-structured and structured data functions](../functions-semistructured.md) (Cast)

# AS_CHAR , AS_VARCHAR

Casts a [VARIANT](../data-types-semistructured.md) value to a [VARCHAR](../data-types-text.md) value. This function
only converts [CHAR](../data-types-text.md) and VARCHAR values.

The AS_CHAR and AS_VARCHAR functions are synonymous.

The CHAR data type is synonymous with the VARCHAR data type, except for its default length.

See also:
:   [AS_<object_type>](as.md)

## Syntax

```sqlsyntax
AS_CHAR( <variant_expr> )

AS_VARCHAR( <variant_expr> )
```

## Arguments

`variant_expr`
:   An expression that evaluates to a value of type VARIANT.

## Returns

The function returns a value of type VARCHAR or NULL:

* If the type of the value in the `variant_expr` argument is CHAR or VARCHAR, the function returns a value of type VARCHAR.

* If the type of the value in the `variant_expr` argument doesn’t match the type of the output
  value, the function returns NULL.
* If the `variant_expr` argument is NULL, the function returns NULL.

## Examples

Create a table and load data into it:

```sqlexample
CREATE OR REPLACE TABLE as_varchar_example (varchar1 VARIANT);

INSERT INTO as_varchar_example (varchar1)
  SELECT TO_VARIANT('My VARCHAR value');
```

Use the AS_VARCHAR function in a query to cast a VARIANT value to a VARCHAR value:

```sqlexample
SELECT AS_VARCHAR(varchar1) varchar_value
  FROM as_varchar_example;
```

```output
+------------------+
| VARCHAR_VALUE    |
|------------------|
| My VARCHAR value |
+------------------+
```
