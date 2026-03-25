# Source: https://docs.snowflake.com/en/sql-reference/functions/unicode.md

Categories:
:   [String & binary functions](../functions-string.md) (General)

# UNICODE

Returns the Unicode code point for the first Unicode character in a string. If the string is empty, a value of `0` is returned.

See also:

> [ASCII](ascii.md) , [CHAR](chr.md)

## Syntax

```sqlsyntax
UNICODE( <input> )
```

## Arguments

`input`
:   The string for which the Unicode code point for the first character in the string is returned.

## Examples

This example demonstrates the function behavior for single ASCII and Unicode characters, as well as special cases, such as multi-character strings, empty strings,
and `NULL` values. It also demonstrates how the UNICODE and [CHAR](chr.md) functions interact:

```sqlexample
SELECT column1, UNICODE(column1), CHAR(UNICODE(column1))
FROM values('a'), ('\u2744'), ('cde'), (''), (null);

+---------+------------------+------------------------+
| COLUMN1 | UNICODE(COLUMN1) | CHAR(UNICODE(COLUMN1)) |
|---------+------------------+------------------------|
| a       |               97 | a                      |
| ❄       |            10052 | ❄                      |
| cde     |               99 | c                      |
|         |                0 |                        |
| NULL    |             NULL | NULL                   |
+---------+------------------+------------------------+
```
