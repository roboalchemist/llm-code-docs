# Source: https://docs.snowflake.com/en/sql-reference/functions/asinh.md

Categories:
:   [Numeric functions](../functions-numeric.md) (Trigonometric)

# ASINH

Computes the inverse (arc) hyperbolic sine of its argument.

## Syntax

```sqlsyntax
ASINH( <input_expr> )
```

## Arguments

`input_expr`
:   The value or expression to operate on. The data type must be FLOAT.

## Returns

This function returns a value of type FLOAT.

## Examples

```sqlexample
SELECT ASINH(2.129279455);
```

```output
+--------------------+
| ASINH(2.129279455) |
|--------------------|
|                1.5 |
+--------------------+
```
