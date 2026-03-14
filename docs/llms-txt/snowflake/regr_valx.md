# Source: https://docs.snowflake.com/en/sql-reference/functions/regr_valx.md

Categories:
:   [Conditional expression functions](../expressions-conditional.md)

# REGR_VALX

Returns NULL if the first argument is NULL; otherwise, returns the second argument.

Note that REGR_VALX is a NULL-preserving function, while the more commonly-used [NVL](nvl.md) is a NULL-replacing function.

## Syntax

```sqlsyntax
REGR_VALX( <y> , <x> )
```

## Arguments

`y`:
:   An expression that evaluates to type FLOAT or DECFLOAT or that can be cast to type FLOAT or DECFLOAT.

`x`:
:   An expression that evaluates to type FLOAT or DECFLOAT or that can be cast to type FLOAT or DECFLOAT.

> **Important:**
>
> Note the order of the arguments; y precedes x.

## Returns

If any of the input expressions is of type DECFLOAT, the returned type is DECFLOAT. Otherwise, the
returned type is FLOAT.

## Examples

Basic example:

> ```sqlexample
> SELECT REGR_VALX(NULL, 10), REGR_VALX(1, NULL), REGR_VALX(1, 10);
> +---------------------+--------------------+------------------+
> | REGR_VALX(NULL, 10) | REGR_VALX(1, NULL) | REGR_VALX(1, 10) |
> |---------------------+--------------------+------------------|
> |                NULL |               NULL |               10 |
> +---------------------+--------------------+------------------+
> ```

This example is similar to the preceding example, but shows more clearly that the convention is to pass the `Y`
value first. It also shows the difference between REGR_VALX and REGR_VALY:

> ```sqlexample
> CREATE TABLE xy (col_x DOUBLE, col_y DOUBLE);
> INSERT INTO xy (col_x, col_y) VALUES
>     (1.0, 2.0),
>     (3.0, NULL),
>     (NULL, 6.0);
> ```
>
> ```sqlexample
> SELECT col_y, col_x, REGR_VALX(col_y, col_x), REGR_VALY(col_y, col_x)
>     FROM xy;
> +-------+-------+-------------------------+-------------------------+
> | COL_Y | COL_X | REGR_VALX(COL_Y, COL_X) | REGR_VALY(COL_Y, COL_X) |
> |-------+-------+-------------------------+-------------------------|
> |     2 |     1 |                       1 |                       2 |
> |  NULL |     3 |                    NULL |                    NULL |
> |     6 |  NULL |                    NULL |                    NULL |
> +-------+-------+-------------------------+-------------------------+
> ```
