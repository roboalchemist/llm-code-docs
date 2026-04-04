# Source: https://docs.snowflake.com/en/sql-reference/functions/acosh.md

Categories:
:   [Numeric functions](../functions-numeric.md) (Trigonometric)

# ACOSH

Computes the inverse (arc) hyperbolic cosine of its input.

## Syntax

```sqlsyntax
ACOSH( <input_expr> )
```

## Arguments

`input_expr`
:   The value or expression to operate on. Must be greater than or equal to 1.0.
    The data type must be FLOAT.

## Returns

This function returns a value of type FLOAT.

## Examples

```sqlexample
SELECT ACOSH(2.352409615);
```

```output
+--------------------+
| ACOSH(2.352409615) |
|--------------------|
|                1.5 |
+--------------------+
```
