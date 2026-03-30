# Source: https://docs.snowflake.com/en/sql-reference/functions/tan.md

Categories:
:   [Numeric functions](../functions-numeric.md) (Trigonometric)

# TAN

Computes the tangent of its argument; the argument should be expressed in
radians.

## Syntax

```sqlsyntax
TAN( <input_expr> )
```

## Arguments

`input_expr`
:   The value or expression to operate on. The value must be in
    radians, not degrees. The data type must be FLOAT.

## Returns

This function returns a value of type FLOAT.

## Examples

```sqlexample
SELECT TAN(0), TAN(PI()/3), TAN(RADIANS(90));
```

```output
+--------+-------------+----------------------+
| TAN(0) | TAN(PI()/3) |     TAN(RADIANS(90)) |
|--------+-------------+----------------------|
|      0 | 1.732050808 | 1.63312393531954e+16 |
+--------+-------------+----------------------+
```
