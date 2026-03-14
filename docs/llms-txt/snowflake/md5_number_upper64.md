# Source: https://docs.snowflake.com/en/sql-reference/functions/md5_number_upper64.md

Categories:
:   [String & binary functions](../functions-string.md) (Checksum)

# MD5_NUMBER_UPPER64

Calculates the 128-bit MD5 message digest, interprets it as a signed 128-bit big endian number, and returns the upper 64 bits of
the number as an unsigned integer. This representation is useful for maximally efficient storage and comparison of MD5 digests.

See also:
:   [MD5 , MD5_HEX](md5.md), [MD5_BINARY](md5_binary.md), [MD5_NUMBER_LOWER64](md5_number_lower64.md)

## Syntax

```sqlsyntax
MD5_NUMBER_UPPER64(<msg>)
```

## Arguments

`msg`
:   A string expression, the message to be hashed.

## Returns

A 64 bit unsigned integer that represents the upper 64 bits of the message digest.

## Usage notes

* Although the MD5\* functions were originally developed as cryptographic functions, they are now
  obsolete for cryptography and should not be used for that purpose. They can be used for other purposes
  (for example, as “checksum” functions to detect accidental data corruption).

  If you need to encrypt and decrypt data, use the following functions:

  * [ENCRYPT](encrypt.md) and [DECRYPT](decrypt.md)
  * [ENCRYPT_RAW](encrypt_raw.md) and [DECRYPT_RAW](decrypt_raw.md)

## Examples

```sqlexample
select md5_number_upper64('Snowflake');

+---------------------------------+
| MD5_NUMBER_UPPER64('SNOWFLAKE') |
|---------------------------------|
|            17145559544104499780 |
+---------------------------------+
```
