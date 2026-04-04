# Source: https://docs.snowflake.com/en/sql-reference/functions/pi.md

Categories:
:   [Numeric functions](../functions-numeric.md) (Trigonometric)

# PI

Returns the value of pi as a floating-point value.

## Syntax

```sqlsyntax
PI()
```

## Returns

This function returns a value of type FLOAT.

## Examples

```sqlexample
SELECT PI();
```

```output
+-------------+
|        PI() |
|-------------|
| 3.141592654 |
+-------------+
```
