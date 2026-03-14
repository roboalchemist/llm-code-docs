# Source: https://docs.snowflake.com/en/sql-reference/functions/try_to_double.md

Categories:
:   [Conversion functions](../functions-conversion.md)

# TRY_TO_DOUBLE

A special version of [TO_DOUBLE](to_double.md) that performs the same operation (that is,
converts an input expression to a double-precision floating-point number), but
with error-handling support (that is, if the conversion can’t be performed, it
returns a NULL value instead of raising an error).

For more information, see [Error-handling conversion functions](../functions-conversion.md).

## Syntax

```sqlsyntax
TRY_TO_DOUBLE( <string_expr> [, '<format>' ] )
```

## Arguments

`expr`
:   An expression of a character type.

`format`
:   If the expression evaluates to a string, then the function accepts
    an optional format model. Format models are described at
    [SQL format models](../sql-format-models.md). The format model
    specifies the format of the input string, not the format of the
    output value.

## Usage notes

* The function only accepts string expressions.
* Strings are converted as decimal integer or fractional numbers,
  scientific notation and special values (**nan**, **inf**, **infinity**)
  are accepted.

## Returns

This function returns a value of FLOAT data type.

If there is a conversion error, the function returns NULL.

## Examples

This example uses the TRY_TO_DOUBLE function:

```sqlexample
SELECT TRY_TO_DOUBLE('3.1415926'), TRY_TO_DOUBLE('Invalid');
```

```output
+----------------------------+--------------------------+
| TRY_TO_DOUBLE('3.1415926') | TRY_TO_DOUBLE('INVALID') |
|----------------------------+--------------------------|
|                  3.1415926 |                     NULL |
+----------------------------+--------------------------+
```

For additional examples, see [TO_DOUBLE](to_double.md).
