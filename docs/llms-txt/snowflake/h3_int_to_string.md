# Source: https://docs.snowflake.com/en/sql-reference/functions/h3_int_to_string.md

Categories:
:   [Geospatial functions](../functions-geospatial.md)

# H3_INT_TO_STRING

Converts the INTEGER value of an [H3](../data-types-geospatial.md) cell ID to hexadecimal format.

See also:
:   [H3_STRING_TO_INT](h3_string_to_int.md)

## Syntax

```sqlsyntax
H3_INT_TO_STRING( <cell_id> )
```

## Arguments

`cell_id`
:   An INTEGER value that represents the cell ID ([index](https://h3geo.org/docs/core-library/h3Indexing)).

## Returns

Returns the H3 cell ID in hexadecimal format.

## Examples

The following example converts the INTEGER value of an H3 cell ID to hexadecimal format.

```sqlexample
SELECT H3_INT_TO_STRING(617700171168612351);
```

```output
+------------------------------------------------+
|          H3_INT_TO_STRING(617700171168612351)  |
|------------------------------------------------|
|                                89283087033FFFF |
+------------------------------------------------+
```
