# Source: https://docs.snowflake.com/en/sql-reference/functions/sinh.md

Categories:
:   [Numeric functions](../functions-numeric.md) (Trigonometric)

# SINH

Computes the hyperbolic sine of its argument.

## Syntax

```sqlsyntax
SINH( <input_expr> )
```

## Arguments

`input_expr`
:   The value or expression to operate on. The data type must be FLOAT.

## Returns

This function returns a value of type FLOAT.

## Examples

```sqlexample
SELECT SINH(1.5);
```

```output
+-------------+
|   SINH(1.5) |
|-------------|
| 2.129279455 |
+-------------+
```
