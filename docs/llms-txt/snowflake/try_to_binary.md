# Source: https://docs.snowflake.com/en/sql-reference/functions/try_to_binary.md

Categories:
:   [Conversion functions](../functions-conversion.md)

# TRY_TO_BINARY

A special version of [TO_BINARY](to_binary.md) that performs the same operation (i.e. converts an input expression to a binary value),
but with error handling support (i.e. if the conversion cannot be performed, it returns a NULL value instead of raising an error).

For more information, see:

* [Error-handling conversion functions](../functions-conversion.md).
* [TO_BINARY](to_binary.md).
* [Binary input and output](../binary-input-output.md).

## Syntax

```sqlsyntax
TRY_TO_BINARY( <string_expr> [, '<format>'] )
```

## Arguments

**Required:**

`string_expr`
:   A string expression.

**Optional:**

`format`
:   The binary format for conversion: HEX, BASE64, or UTF-8 (see [Binary input and output](../binary-input-output.md)). The default is the value of the
    BINARY_INPUT_FORMAT session parameter. If this parameter is not set, the
    default is HEX.

## Returns

Returns a value of type BINARY.

## Usage notes

* Only works for string expressions.
* If `format` is specified but is not HEX, BASE64, or UTF-8, the result will be a NULL value.

## Examples

This shows how to use the `TRY_TO_BINARY` function when loading
hex-encoded strings into a BINARY column:

> Create and fill a table:
>
> > ```sqlexample
> > CREATE TABLE strings (v VARCHAR, hex_encoded_string VARCHAR, b BINARY);
> > INSERT INTO strings (v) VALUES
> >     ('01'),
> >     ('A B'),
> >     ('Hello'),
> >     (NULL);
> > UPDATE strings SET hex_encoded_string = HEX_ENCODE(v);
> > UPDATE strings SET b = TRY_TO_BINARY(hex_encoded_string, 'HEX');
> > ```
>
> Query the table, calling TRY_TO_BINARY():
>
> > ```sqlexample
> > SELECT v, hex_encoded_string, TO_VARCHAR(b, 'UTF-8')
> >   FROM strings
> >   ORDER BY v
> >   ;
> > +-------+--------------------+------------------------+
> > | V     | HEX_ENCODED_STRING | TO_VARCHAR(B, 'UTF-8') |
> > |-------+--------------------+------------------------|
> > | 01    | 3031               | 01                     |
> > | A B   | 412042             | A B                    |
> > | Hello | 48656C6C6F         | Hello                  |
> > | NULL  | NULL               | NULL                   |
> > +-------+--------------------+------------------------+
> > ```
