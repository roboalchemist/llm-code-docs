# Source: https://docs.snowflake.com/en/sql-reference/functions/md5_number.md

Categories:
:   [String & binary functions](../functions-string.md) (Checksum)

# MD5_NUMBER — *Obsoleted*

Returns the 128-bit MD5 message digest interpreted as a signed 128-bit big
endian number. This representation is useful for maximally efficient storage
and comparison of MD5 digests.

See also:
:   [MD5 , MD5_HEX](md5.md), [MD5_BINARY](md5_binary.md), [MD5_NUMBER_LOWER64](md5_number_lower64.md), [MD5_NUMBER_UPPER64](md5_number_upper64.md)

## Syntax

```sqlsyntax
MD5_NUMBER(<msg>)
```

## Arguments

`msg`
:   A string expression, the message to be hashed.

## Returns

A signed integer (`NUMERIC(38, 0)`).

This integer can be outside the range stored by `NUMERIC(38, 0)`, so this function has been obsoleted.

## Usage notes

Although the `MD5`, `MD5_BINARY`, and `MD5_NUMBER` functions
were originally developed as cryptographic functions, they are now
obsolete for cryptography and should not be used for that purpose.
They can be used for other purposes, for example as “checksum”
functions to detect accidental data corruption.

## Examples

```sqlexample
SELECT md5_number('Snowflake');

-----------------------------------------+
         MD5_NUMBER('SNOWFLAKE')         |
-----------------------------------------+
 -24002618010294540563082926240470284066 |
-----------------------------------------+
```
