# Source: https://docs.snowflake.com/en/sql-reference/functions/md5.md

Categories:
:   [String & binary functions](../functions-string.md) (Checksum)

# MD5 , MD5_HEX

Returns a 32-character hex-encoded string containing the 128-bit MD5
message digest.

These functions are synonymous.

See also:
:   [MD5_BINARY](md5_binary.md), [MD5_NUMBER_LOWER64](md5_number_lower64.md), [MD5_NUMBER_UPPER64](md5_number_upper64.md)

## Syntax

```sqlsyntax
MD5(<msg>)

MD5_HEX(<msg>)
```

## Arguments

`msg`
:   A string expression, the message to be hashed.

## Returns

Returns a 32-character hex-encoded string.

## Usage notes

* Although the MD5\* functions were originally developed as cryptographic functions, they are now
  obsolete for cryptography and should not be used for that purpose. They can be used for other purposes
  (for example, as “checksum” functions to detect accidental data corruption).

  If you need to encrypt and decrypt data, use the following functions:

  * [ENCRYPT](encrypt.md) and [DECRYPT](decrypt.md)
  * [ENCRYPT_RAW](encrypt_raw.md) and [DECRYPT_RAW](decrypt_raw.md)

## Examples

```sqlexample
SELECT md5('Snowflake');

----------------------------------+
         MD5('SNOWFLAKE')         |
----------------------------------+
 edf1439075a83a447fb8b630ddc9c8de |
----------------------------------+
```
