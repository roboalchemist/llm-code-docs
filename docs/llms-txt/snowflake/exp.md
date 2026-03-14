# Source: https://docs.snowflake.com/en/sql-reference/functions/exp.md

Categories:
:   [Numeric functions](../functions-numeric.md) (Exponent and Root)

# EXP

Computes Euler’s number `e` raised to a floating-point value.

## Syntax

```sqlsyntax
EXP( <input_expr> )
```

## Arguments

`input_expr`
:   The value or expression to operate on. The data type must be FLOAT or DECFLOAT.

## Returns

If the input expression is of type DECFLOAT, the returned type is DECFLOAT. Otherwise, the
returned type is FLOAT.

## Examples

> ```sqlexample
> SELECT EXP(1), EXP(LN(10));
> -------------+-------------+
>    EXP(1)    | EXP(LN(10)) |
> -------------+-------------+
>  2.718281828 | 10          |
> -------------+-------------+
> ```
