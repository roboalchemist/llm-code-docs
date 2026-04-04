# Source: https://docs.snowflake.com/en/sql-reference/functions/cosh.md

Categories:
:   [Numeric functions](../functions-numeric.md) (Trigonometric)

# COSH

Computes the hyperbolic cosine of its argument.

## Syntax

```sqlsyntax
COSH( <input_expr> )
```

## Arguments

`input_expr`
:   The value or expression to operate on. The data type must be FLOAT.

## Returns

This function returns a value of type FLOAT.

## Examples

```sqlexample
SELECT COSH(1.5);
```

```output
+-------------+
|   COSH(1.5) |
|-------------|
| 2.352409615 |
+-------------+
```
