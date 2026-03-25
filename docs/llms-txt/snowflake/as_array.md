# Source: https://docs.snowflake.com/en/sql-reference/functions/as_array.md

Categories:
:   [Semi-structured and structured data functions](../functions-semistructured.md) (Cast)

# AS_ARRAY

Casts a [VARIANT](../data-types-semistructured.md) value to an [ARRAY](../data-types-semistructured.md) value.

See also:
:   [AS_<object_type>](as.md) , [AS_OBJECT](as_object.md)

## Syntax

```sqlsyntax
AS_ARRAY( <variant_expr> )
```

## Arguments

`variant_expr`
:   An expression that evaluates to a value of type VARIANT.

## Returns

The function returns a value of type ARRAY or NULL:

* If the type of the value in the `variant_expr` argument is ARRAY, the function returns a value of type ARRAY.

* If the type of the value in the `variant_expr` argument doesn’t match the type of the output
  value, the function returns NULL.
* If the `variant_expr` argument is NULL, the function returns NULL.

## Usage notes

* This function doesn’t support a [structured type](../data-types-structured.md) as an input argument.

## Examples

Create a table and load data into it:

```sqlexample
CREATE OR REPLACE TABLE as_array_example (
  array1 VARIANT,
  array2 VARIANT);

INSERT INTO as_array_example (array1, array2)
  SELECT
    TO_VARIANT(TO_ARRAY('Example')),
    TO_VARIANT(ARRAY_CONSTRUCT('Array-like', 'example'));
```

Use the AS_ARRAY function in a query to cast a VARIANT value to ARRAY values:

```sqlexample
SELECT AS_ARRAY(array1) AS array1,
       AS_ARRAY(array2) AS array2
  FROM as_array_example;
```

```output
+-------------+-----------------+
| ARRAY1      | ARRAY2          |
|-------------+-----------------|
| [           | [               |
|   "Example" |   "Array-like", |
| ]           |   "example"     |
|             | ]               |
+-------------+-----------------+
```
