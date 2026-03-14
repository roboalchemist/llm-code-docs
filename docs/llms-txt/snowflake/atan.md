# Source: https://docs.snowflake.com/en/sql-reference/functions/atan.md

Categories:
:   [Numeric functions](../functions-numeric.md) (Trigonometric)

# ATAN

Computes the inverse tangent (arc tangent) of its argument; the result is a number in the interval `[-pi, pi]`.

## Syntax

```sqlsyntax
ATAN( <input_expr> )
```

## Arguments

`input_expr`
:   The value or expression to operate on. The data type must be FLOAT.

## Returns

This function returns a value of type FLOAT.

Returns the arc tangent in radians (not degrees) in the range `[-pi, pi]`.

## Examples

```sqlexample
SELECT ATAN(1);
```

```output
+--------------+
|      ATAN(1) |
|--------------|
| 0.7853981634 |
+--------------+
```
