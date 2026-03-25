# Source: https://docs.snowflake.com/en/sql-reference/functions/h3_cell_to_children_string.md

Categories:
:   [Geospatial functions](../functions-geospatial.md)

# H3_CELL_TO_CHILDREN_STRING

Returns an [array](../data-types-semistructured.md) of the VARCHAR values containing the hexadecimal IDs of the children of an
[H3](../data-types-geospatial.md) cell for a given resolution.

See also:
:   [H3_CELL_TO_CHILDREN](h3_cell_to_children.md) , [H3_CELL_TO_PARENT](h3_cell_to_parent.md)

## Syntax

```sqlsyntax
H3_CELL_TO_CHILDREN_STRING( <cell_id> , <target_resolution> )
```

## Arguments

`cell_id`
:   A VARCHAR that represents the H3 cell ID ([index](https://h3geo.org/docs/core-library/h3Indexing)) in hexadecimal format.

`target_resolution`
:   An INTEGER between 0 and 15 (inclusive) specifying the H3 [resolution](https://h3geo.org/docs/core-library/restable) that you want to use for the returned H3 cells.

    Specifying any other INTEGER value results in an error.

## Returns

Returns an array of the VARCHAR values of the hexadecimal IDs of the children of an H3 cell at the specified target resolution.

## Examples

The following example returns an array of the IDs (in hexadecimal format) of the children of the H3 cell with the ID
`881F1D4887FFFFF` (in hexadecimal format):

```sqlexample
SELECT H3_CELL_TO_CHILDREN_STRING('881F1D4887FFFFF', 9);
```

```output
+--------------------------------------------------+
| H3_CELL_TO_CHILDREN_STRING('881F1D4887FFFFF', 9) |
|--------------------------------------------------|
| [                                                |
|   "891f1d48863ffff",                             |
|   "891f1d48867ffff",                             |
|   "891f1d4886bffff",                             |
|   "891f1d4886fffff",                             |
|   "891f1d48873ffff",                             |
|   "891f1d48877ffff",                             |
|   "891f1d4887bffff"                              |
| ]                                                |
+--------------------------------------------------+
```
