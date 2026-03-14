# Source: https://docs.snowflake.com/en/sql-reference/functions/abs.md

Categories:
:   [Numeric functions](../functions-numeric.md) (Rounding and Truncation)

# ABS

Returns the absolute value of a numeric expression.

## Syntax

```sqlsyntax
ABS( <num_expr> )
```

## Examples

```sqlexample
SELECT column1, abs(column1)
    FROM (values (0), (1), (-2), (3.5), (-4.5), (null));
+---------+--------------+
| COLUMN1 | ABS(COLUMN1) |
|---------+--------------|
|     0.0 |          0.0 |
|     1.0 |          1.0 |
|    -2.0 |          2.0 |
|     3.5 |          3.5 |
|    -4.5 |          4.5 |
|    NULL |         NULL |
+---------+--------------+
```
