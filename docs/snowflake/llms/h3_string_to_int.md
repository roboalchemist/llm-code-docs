# Source: https://docs.snowflake.com/en/sql-reference/functions/h3_string_to_int.md

Categories:
:   [Geospatial functions](../functions-geospatial.md)

# H3_STRING_TO_INT

Converts an [H3](../data-types-geospatial.md) cell ID in hexadecimal format to an INTEGER value.

See also:
:   [H3_INT_TO_STRING](h3_int_to_string.md)

## Syntax

```sqlsyntax
H3_STRING_TO_INT( <cell_id> )
```

## Arguments

`cell_id`
:   A VARCHAR that represents the cell ID ([index](https://h3geo.org/docs/core-library/h3Indexing)) in hexadecimal format.

## Returns

Returns an INTEGER value that represents the H3 cell ID.

## Examples

The following example converts an H3 cell ID from hexadecimal format to an INTEGER value.

```sqlexample
SELECT H3_STRING_TO_INT('89283087033FFFF');
```

```output
+------------------------------------------------+
|            H3_STRING_TO_INT('89283087033FFFF') |
|------------------------------------------------|
|                             617700171168612351 |
+------------------------------------------------+
```
