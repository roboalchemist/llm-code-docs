# Source: https://docs.snowflake.com/en/sql-reference/functions/factorial.md

Categories:
:   [Numeric functions](../functions-numeric.md) (Exponent and Root)

# FACTORIAL

Computes the factorial of its input. The input argument must be an integer expression in the range of `0` to `33`.

## Syntax

```sqlsyntax
FACTORIAL( <integer_expr> )
```

## Examples

```sqlexample
SELECT FACTORIAL(0), FACTORIAL(1), FACTORIAL(5), FACTORIAL(10);

+--------------+--------------+--------------+---------------+
| FACTORIAL(0) | FACTORIAL(1) | FACTORIAL(5) | FACTORIAL(10) |
|--------------+--------------+--------------+---------------|
|            1 |            1 |          120 |       3628800 |
+--------------+--------------+--------------+---------------+
```
