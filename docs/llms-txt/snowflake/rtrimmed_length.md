# Source: https://docs.snowflake.com/en/sql-reference/functions/rtrimmed_length.md

Categories:
:   [String & binary functions](../functions-string.md) (General)

# RTRIMMED_LENGTH

Returns the length of its argument, minus trailing whitespace, but including leading whitespace.

## Syntax

```sqlsyntax
RTRIMMED_LENGTH( <string_expr> )
```

## Usage notes

* Equivalent to `{fn LENGTH(str)}` in ODBC.
* Not equivalent to [LENGTH, LEN](length.md) in Snowflake.

## Examples

```sqlexample
SELECT RTRIMMED_LENGTH(' ABCD ');

+---------------------------+
| RTRIMMED_LENGTH(' ABCD ') |
|---------------------------|
|                         5 |
+---------------------------+
```
