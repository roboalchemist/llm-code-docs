# Source: https://docs.snowflake.com/en/sql-reference/functions/acos.md

Categories:
:   [Numeric functions](../functions-numeric.md) (Trigonometric)

# ACOS

Computes the inverse cosine (arc cosine) of its input; the result is a number in the interval `[0, pi]`.

## Syntax

```sqlsyntax
ACOS( <input_expr> )
```

## Arguments

`input_expr`
:   The value or expression to operate on. Must be greater than or equal to -1.0 and
    less than or equal to +1.0. The data type must be FLOAT.

## Returns

This function returns a value of type FLOAT.

Returns the arc cosine in radians (not degrees) as a value in the range `[0, pi]`.

## Examples

```sqlexample
SELECT ACOS(0), ACOS(0.5), ACOS(1);
```

```output
+-------------+-------------+---------+
|     ACOS(0) |   ACOS(0.5) | ACOS(1) |
|-------------+-------------+---------|
| 1.570796327 | 1.047197551 |       0 |
+-------------+-------------+---------+
```
