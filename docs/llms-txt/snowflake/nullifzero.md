# Source: https://docs.snowflake.com/en/sql-reference/functions/nullifzero.md

Categories:
:   [Conditional expression functions](../expressions-conditional.md)

# NULLIFZERO

Returns NULL if the argument evaluates to `0`; otherwise, returns the argument.

## Syntax

```sqlsyntax
NULLIFZERO( <expr> )
```

## Arguments

`expr`
:   The input should be an expression that evaluates to a numeric value.

## Returns

If the value of the input expression is `0`, this returns NULL.
Otherwise, this returns the value of the input expression.

The data type of the return value is `NUMBER(p, s)` (if the input is a
[fixed-point number](../data-types-numeric.md)) or `DOUBLE` (if the
input is a [floating point number](../data-types-numeric.md)).

For fixed-point numbers, the exact values of ‘p’ (precision) and ‘s’ (scale) depend upon the input expression. For example,
if the input expression is 3.14159, then the data type of the output value will be `NUMBER(7, 5)`.

## Examples

The following examples show the output of the function for various input values:

> ```sqlexample
> SELECT NULLIFZERO(0);
> +---------------+
> | NULLIFZERO(0) |
> |---------------|
> |          NULL |
> +---------------+
> ```
>
> ```sqlexample
> SELECT NULLIFZERO(52);
> +----------------+
> | NULLIFZERO(52) |
> |----------------|
> |             52 |
> +----------------+
> ```
>
> ```sqlexample
> SELECT NULLIFZERO(3.14159);
> +---------------------+
> | NULLIFZERO(3.14159) |
> |---------------------|
> |             3.14159 |
> +---------------------+
> ```
