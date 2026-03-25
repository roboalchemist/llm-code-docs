# Source: https://docs.snowflake.com/en/sql-reference/functions/try_hex_decode_string.md

Categories:
:   [String & binary functions](../functions-string.md) (Encoding/Decoding)

# TRY_HEX_DECODE_STRING

A special version of [HEX_DECODE_STRING](hex_decode_string.md) that
returns a NULL value if an error occurs during decoding.

## Syntax

```sqlsyntax
TRY_HEX_DECODE_STRING(<input>)
```

## Arguments

`input`
:   A hex-encoded string expression. Typically the input was created by a
    call to [HEX_ENCODE](hex_encode.md).

## Returns

The returned value is a string (VARCHAR).

## Examples

This shows how to use the function:

> Create a table and data:
>
> > ```sqlexample
> > CREATE TABLE hex (v VARCHAR, hex_string VARCHAR, garbage VARCHAR);
> > INSERT INTO hex (v, hex_string, garbage)
> >   SELECT 'AaBb', HEX_ENCODE('AaBb'), '127';
> > ```
>
> Now run the query:
>
> > ```sqlexample
> > SELECT v, hex_string, TRY_HEX_DECODE_STRING(hex_string), TRY_HEX_DECODE_STRING(garbage) FROM hex;
> > ```
>
> Output:
>
> > ```sqlexample
> > +------+------------+-----------------------------------+--------------------------------+
> > | V    | HEX_STRING | TRY_HEX_DECODE_STRING(HEX_STRING) | TRY_HEX_DECODE_STRING(GARBAGE) |
> > |------+------------+-----------------------------------+--------------------------------|
> > | AaBb | 41614262   | AaBb                              | NULL                           |
> > +------+------------+-----------------------------------+--------------------------------+
> > ```
