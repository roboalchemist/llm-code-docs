# Source: https://docs.snowflake.com/en/sql-reference/functions/md5_binary.md

Categories:
:   [String & binary functions](../functions-string.md) (Checksum)

# MD5_BINARY

Returns a 16-byte `BINARY` value containing the 128-bit MD5 message digest.

See also:
:   [MD5 , MD5_HEX](md5.md), [MD5_NUMBER_LOWER64](md5_number_lower64.md), [MD5_NUMBER_UPPER64](md5_number_upper64.md)

## Syntax

```sqlsyntax
MD5_BINARY(<msg>)
```

## Arguments

`msg`
:   A string expression, the message to be hashed.

## Returns

Returns a 16-byte `BINARY` value containing the MD5 message digest.

## Usage notes

* Although the MD5\* functions were originally developed as cryptographic functions, they are now
  obsolete for cryptography and should not be used for that purpose. They can be used for other purposes
  (for example, as “checksum” functions to detect accidental data corruption).

  If you need to encrypt and decrypt data, use the following functions:

  * [ENCRYPT](encrypt.md) and [DECRYPT](decrypt.md)
  * [ENCRYPT_RAW](encrypt_raw.md) and [DECRYPT_RAW](decrypt_raw.md)

## Examples

The example below shows a simple example of using the function. Note that
although the output is a 16-byte binary string, by default SNOWSQL displays
binary values as a series of hexadecimal digits, so the output below appears
as 32 hexadecimal digits, not as 16 one-byte characters.

> ```sqlexample
> SELECT md5_binary('Snowflake');
> +----------------------------------+
> | MD5_BINARY('SNOWFLAKE')          |
> |----------------------------------|
> | EDF1439075A83A447FB8B630DDC9C8DE |
> +----------------------------------+
> ```

This example demonstrates using the function to insert into a table that
contains a column of type `BINARY`.

> Create and fill a table:
>
> > ```sqlexample
> > CREATE TABLE binary_demo (b BINARY);
> > INSERT INTO binary_demo (b) SELECT MD5_BINARY('Snowflake');
> > ```
>
> Output:
>
> > ```sqlexample
> > SELECT TO_VARCHAR(b, 'HEX') AS hex_representation
> >     FROM binary_demo;
> > +----------------------------------+
> > | HEX_REPRESENTATION               |
> > |----------------------------------|
> > | EDF1439075A83A447FB8B630DDC9C8DE |
> > +----------------------------------+
> > ```
