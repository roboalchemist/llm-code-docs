# Source: https://docs.snowflake.com/en/sql-reference/functions/tanh.md

Categories:
:   [Numeric functions](../functions-numeric.md) (Trigonometric)

# TANH

Computes the hyperbolic tangent of its argument.

## Syntax

```sqlsyntax
TANH( <real_expr> )
```

## Arguments

`input_expr`
:   The value or expression to operate on. The data type must be FLOAT.

## Returns

This function returns a value of type FLOAT.

## Examples

```sqlexample
SELECT TANH(1.5);
```

```output
+--------------+
|    TANH(1.5) |
|--------------|
| 0.9051482536 |
+--------------+
```
