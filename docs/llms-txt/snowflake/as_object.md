# Source: https://docs.snowflake.com/en/sql-reference/functions/as_object.md

Categories:
:   [Semi-structured and structured data functions](../functions-semistructured.md) (Cast)

# AS_OBJECT

Casts a [VARIANT](../data-types-semistructured.md) value to an [OBJECT](../data-types-semistructured.md) value.

See also:
:   [AS_<object_type>](as.md) , [AS_ARRAY](as_array.md)

## Syntax

```sqlsyntax
AS_OBJECT( <variant_expr> )
```

## Arguments

`variant_expr`
:   An expression that evaluates to a value of type VARIANT.

## Returns

The function returns a value of type OBJECT or NULL:

* If the type of the value in the `variant_expr` argument is OBJECT, the function returns a value of type OBJECT.

* If the type of the value in the `variant_expr` argument doesn’t match the type of the output
  value, the function returns NULL.
* If the `variant_expr` argument is NULL, the function returns NULL.

## Usage notes

* This function doesn’t support a [structured type](../data-types-structured.md) as an input argument.

## Examples

Create a table and load data into it:

```sqlexample
CREATE OR REPLACE TABLE as_object_example (object1 VARIANT);

INSERT INTO as_object_example (object1)
  SELECT TO_VARIANT(TO_OBJECT(PARSE_JSON('{"Tree": "Pine"}')));
```

Use the AS_OBJECT function in a query to cast a VARIANT value to an OBJECT value:

```sqlexample
SELECT AS_OBJECT(object1) AS object_value
  FROM as_object_example;
```

```output
+------------------+
| OBJECT_VALUE     |
|------------------|
| {                |
|   "Tree": "Pine" |
| }                |
+------------------+
```
