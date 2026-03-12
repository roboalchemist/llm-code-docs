# Source: https://docs.snowflake.com/en/sql-reference/functions/sin.md

Categories:
:   [Numeric functions](../functions-numeric.md) (Trigonometric)

# SIN

Computes the sine of its argument; the argument should be expressed in
radians.

## Syntax

```sqlsyntax
SIN( <input_expr> )
```

## Arguments

`input_expr`
:   The value or expression to operate on. The value must be in
    radians, not degrees. The data type must be FLOAT.

## Returns

This function returns a value of type FLOAT.

## Examples

```sqlexample
SELECT SIN(0), SIN(PI()/3), SIN(RADIANS(90));
```

```output
+--------+--------------+------------------+
| SIN(0) |  SIN(PI()/3) | SIN(RADIANS(90)) |
|--------+--------------+------------------|
|      0 | 0.8660254038 |                1 |
+--------+--------------+------------------+
```
