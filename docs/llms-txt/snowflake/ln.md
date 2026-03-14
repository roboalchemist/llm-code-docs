# Source: https://docs.snowflake.com/en/sql-reference/functions/ln.md

Categories:
:   [Numeric functions](../functions-numeric.md) (Logarithmic)

# LN

Returns the natural logarithm of a numeric expression.

## Syntax

```sqlsyntax
LN(<expr>)
```

## Returns

If the input expression is of type DECFLOAT, the returned type is DECFLOAT. Otherwise, the
returned type is FLOAT.

## Examples

```sqlexample
SELECT x, ln(x) FROM tab;

--------+-------------+
   X    |    LN(X)    |
--------+-------------+
 1      | 0           |
 10     | 2.302585093 |
 100    | 4.605170186 |
 [NULL] | [NULL]      |
--------+-------------+
```
