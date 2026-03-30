# Source: https://docs.snowflake.com/en/sql-reference/functions/mod.md

Categories:
:   [Numeric functions](../functions-numeric.md) (Rounding and Truncation)

# MOD

Returns the remainder of input `expr1` divided by input `expr2`.

Equivalent to the modulo [arithmetic operator](../operators-arithmetic.md) (for example, `expr1 % expr2`).

## Syntax

```sqlsyntax
MOD( <expr1> , <expr2> )
```

## Arguments

`expr1`
:   A numeric expression.

`expr2`
:   A numeric expression.

## Returns

Returns either an integer or a fixed-point decimal number.

## Usage notes

* Both `expr1` and `expr2` must be numeric expressions.
  They aren’t required to be integers.
* The returned value is the remainder from truncation-based division (rounding towards zero), not floor-based
  division (rounding down). Therefore, if `expr1` is negative, the returned value is negative. This
  behavior is different from some programming languages (such as Python), but consistent with standard SQL. For
  more information, see the [Modulo Wikipedia page](https://en.wikipedia.org/wiki/Modulo).

## Examples

The following example shows usage of the `MOD()` function on both integer
and non-integer values:

> ```sqlexample
> SELECT MOD(3, 2) AS mod1, MOD(4.5, 1.2) AS mod2;
> ```
>
> Output:
>
> ```sqlexample
> +------+------+
> | MOD1 | MOD2 |
> +------+------+
> |    1 |  0.9 |
> +------+------+
> ```
