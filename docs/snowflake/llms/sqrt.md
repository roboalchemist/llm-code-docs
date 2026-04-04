# Source: https://docs.snowflake.com/en/sql-reference/functions/sqrt.md

Categories:
:   [Numeric functions](../functions-numeric.md) (Exponent and Root)

# SQRT

Returns the square-root of a non-negative numeric expression.

## Syntax

```sqlsyntax
SQRT(expr)
```

## Returns

If the input expression is of type DECFLOAT, the returned type is DECFLOAT. Otherwise, the
returned type is FLOAT.

## Examples

```sqlexample
SELECT x, sqrt(x) FROM tab;

--------+-------------+
   x    |   sqrt(x)   |
--------+-------------+
 0      | 0           |
 2      | 1.414213562 |
 10     | 3.16227766  |
 [NULL] | [NULL]      |
--------+-------------+
```
