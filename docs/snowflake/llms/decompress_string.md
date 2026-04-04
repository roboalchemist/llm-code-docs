# Source: https://docs.snowflake.com/en/sql-reference/functions/decompress_string.md

Categories:
:   [String & binary functions](../functions-string.md) (Compression/Decompression)

# DECOMPRESS_STRING

Decompresses the compressed `BINARY` input parameter to a string.

See also:
:   [COMPRESS](compress.md) , [DECOMPRESS_BINARY](decompress_binary.md)

## Syntax

```sqlsyntax
DECOMPRESS_STRING(<input>, <method>)
```

## Arguments

**Required:**

`input`
:   A `BINARY` value (or expression) with data that was compressed using one
    of the compression methods specified in [COMPRESS](compress.md).

`method`
:   The compression method originally used to compress the `input`.
    See [COMPRESS](compress.md) for a list of compression
    methods.

    The `DECOMPRESS_STRING` method, unlike the `COMPRESS` method, does
    not require you to specify the compression level. If you do specify
    the compression level, `DECOMPRESS_STRING` ignores it and uses the
    actual compression level.

## Returns

A string with decompressed data.

## Usage notes

* If the compression method is unknown or invalid, the query fails.
* The compression method name (e.g. `ZLIB`) is case insensitive.
* If you use `DECOMPRESS_STRING` to decompress a compressed `BINARY`
  value, rather than a compressed string value, you do
  not necessarily get an error; instead, the function attempts to treat
  the `BINARY` value as a sequence of hexadecimal digits and then attempts
  to convert those hexadecimal digits into printable characters. Snowflake
  recommends that you use the [DECOMPRESS_BINARY](decompress_binary.md) function to decompress
  compressed data if the original data was `BINARY`.

## Examples

This shows how to compress a string and then decompress back to the original
value.

```sqlexample
SELECT COMPRESS('Snowflake', 'SNAPPY');
+---------------------------------+
| COMPRESS('SNOWFLAKE', 'SNAPPY') |
|---------------------------------|
| 0920536E6F77666C616B65          |
+---------------------------------+
```

```sqlexample
SELECT DECOMPRESS_STRING(TO_BINARY('0920536E6F77666C616B65', 'HEX'), 'SNAPPY');
+-------------------------------------------------------------------------+
| DECOMPRESS_STRING(TO_BINARY('0920536E6F77666C616B65', 'HEX'), 'SNAPPY') |
|-------------------------------------------------------------------------|
| Snowflake                                                               |
+-------------------------------------------------------------------------+
```
