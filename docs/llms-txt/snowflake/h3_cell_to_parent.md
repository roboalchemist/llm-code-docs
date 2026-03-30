# Source: https://docs.snowflake.com/en/sql-reference/functions/h3_cell_to_parent.md

Categories:
:   [Geospatial functions](../functions-geospatial.md)

# H3_CELL_TO_PARENT

Returns the ID of the parent of an [H3](../data-types-geospatial.md) cell for a given resolution. The ID is returned as
an INTEGER value (if an INTEGER value was provided as the input ID) or as a VARCHAR containing the hexadecimal ID (if the
hexadecimal ID was provided as the input ID).

See also:
:   [H3_CELL_TO_CHILDREN](h3_cell_to_children.md) , [H3_CELL_TO_CHILDREN_STRING](h3_cell_to_children_string.md)

## Syntax

```sqlsyntax
H3_CELL_TO_PARENT( <cell_id> , <target_resolution> )
```

## Arguments

`cell_id`
:   An INTEGER that represents the H3 cell ID ([index](https://h3geo.org/docs/core-library/h3Indexing)), or a VARCHAR that represents the cell ID in hexadecimal format.

`target_resolution`
:   An INTEGER between 0 and 15 (inclusive) specifying the H3 [resolution](https://h3geo.org/docs/core-library/restable) that you want to use for the returned H3 cell.

    Specifying any other INTEGER value results in an error.

## Returns

Returns the ID of the H3 parent cell at the specified target resolution. The ID is in one of the following formats:

* If `cell_id` is an INTEGER value, the function returns the ID as an INTEGER value.
* If `cell_id` is a VARCHAR value containing the hexadecimal ID, the function returns the hexadecimal ID as a VARCHAR
  value.

## Examples

The following example returns the H3 cell ID for the parent of the H3 cell with the ID `613036919424548863` (specified as an
INTEGER value):

```sqlexample
SELECT H3_CELL_TO_PARENT(613036919424548863, 7);
```

```output
+------------------------------------------+
| H3_CELL_TO_PARENT(613036919424548863, 7) |
|------------------------------------------|
|                       608533319805566975 |
+------------------------------------------+
```

The following example returns the H3 cell ID for the parent of the H3 cell with the ID `881F1D4887FFFFF` (specified as a
VARCHAR value):

```sqlexample
SELECT H3_CELL_TO_PARENT('881F1D4887FFFFF', 7);
```

```output
+-----------------------------------------+
| H3_CELL_TO_PARENT('881F1D4887FFFFF', 7) |
|-----------------------------------------|
|  871F1D488FFFFFF                        |
+-----------------------------------------+
```
