# Source: https://docs.snowflake.com/en/sql-reference/functions/cot.md

Categories:
:   [Numeric functions](../functions-numeric.md) (Trigonometric)

# COT

Computes the cotangent of its argument; the argument should be expressed in
radians.

## Syntax

```sqlsyntax
COT( <input_expr> )
```

## Arguments

`input_expr`
:   The value or expression to operate on. The data type must be FLOAT.

## Returns

This function returns a value of type FLOAT.

## Examples

```sqlexample
SELECT COT(0), COT(PI()/3), COT(RADIANS(90));
```

```output
+--------+--------------+------------------+
| COT(0) |  COT(PI()/3) | COT(RADIANS(90)) |
|--------+--------------+------------------|
|    inf | 0.5773502692 |  6.123233996e-17 |
+--------+--------------+------------------+
```
