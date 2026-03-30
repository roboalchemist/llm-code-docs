# Source: https://docs.snowflake.com/en/sql-reference/functions/h3_cell_to_children.md

Categories:
:   [Geospatial functions](../functions-geospatial.md)

# H3_CELL_TO_CHILDREN

Returns an [array](../data-types-semistructured.md) of the INTEGER IDs of the children of an
[H3](../data-types-geospatial.md) cell for a given resolution.

See also:
:   [H3_CELL_TO_CHILDREN_STRING](h3_cell_to_children_string.md) , [H3_CELL_TO_PARENT](h3_cell_to_parent.md)

## Syntax

```sqlsyntax
H3_CELL_TO_CHILDREN( <cell_id> , <target_resolution> )
```

## Arguments

`cell_id`
:   An INTEGER that represents the H3 cell ID ([index](https://h3geo.org/docs/core-library/h3Indexing)).

`target_resolution`
:   An INTEGER between 0 and 15 (inclusive) specifying the H3 [resolution](https://h3geo.org/docs/core-library/restable) that you want to use for the returned H3 cells.

    Specifying any other INTEGER value results in an error.

## Returns

Returns an array of the INTEGER values of the IDs of the children of an H3 cell at the specified target resolution.

## Examples

The following example returns an array of the IDs of the children of the H3 cell with the ID `613036919424548863`:

```sqlexample
SELECT H3_CELL_TO_CHILDREN(613036919424548863, 9);
```

```output
+--------------------------------------------+
| H3_CELL_TO_CHILDREN(613036919424548863, 9) |
|--------------------------------------------|
| [                                          |
|   617540519050084351,                      |
|   617540519050346495,                      |
|   617540519050608639,                      |
|   617540519050870783,                      |
|   617540519051132927,                      |
|   617540519051395071,                      |
|   617540519051657215                       |
| ]                                          |
+--------------------------------------------+
```
