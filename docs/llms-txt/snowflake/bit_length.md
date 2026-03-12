# Source: https://docs.snowflake.com/en/sql-reference/functions/bit_length.md

Categories:
:   [String & binary functions](../functions-string.md) (General)

# BIT_LENGTH

Returns the length of a string or binary value in bits.

Snowflake doesn’t use fractional bytes so length is always calculated as 8 \* [OCTET_LENGTH](octet_length.md).

## Syntax

```sqlsyntax
BIT_LENGTH(<string_or_binary>)
```

## Arguments

`string_or_binary`
:   The string or binary value for which the length is returned.

## Examples

This shows use of the `BIT_LENGTH` function on both string and BINARY values:

> > ```sqlexample
> > CREATE TABLE bl (v VARCHAR, b BINARY);
> > INSERT INTO bl (v, b) VALUES
> >    ('abc', NULL),
> >    ('\u0394', X'A1B2');
> > ```
>
> Query the data:
>
> > ```sqlexample
> > SELECT v, b, BIT_LENGTH(v), BIT_LENGTH(b) FROM bl ORDER BY v;
> > +-----+------+---------------+---------------+
> > | V   | B    | BIT_LENGTH(V) | BIT_LENGTH(B) |
> > |-----+------+---------------+---------------|
> > | abc | NULL |            24 |          NULL |
> > | Δ   | A1B2 |            16 |            16 |
> > +-----+------+---------------+---------------+
> > ```
