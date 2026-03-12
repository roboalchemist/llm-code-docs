# Source: https://docs.snowflake.com/en/sql-reference/functions/atanh.md

Categories:
:   [Numeric functions](../functions-numeric.md) (Trigonometric)

# ATANH

Computes the inverse (arc) hyperbolic tangent of its argument.

## Syntax

```sqlsyntax
ATANH( <input_expr> )
```

## Arguments

`input_expr`
:   The value or expression to operate on. Must be a value between -1.0 and +1.0
    (inclusive). The data type must be FLOAT.

## Returns

This function returns a value of type FLOAT.

## Examples

```sqlexample
SELECT ATANH(0.9051482536);
```

```output
+---------------------+
| ATANH(0.9051482536) |
|---------------------|
|                 1.5 |
+---------------------+
```
