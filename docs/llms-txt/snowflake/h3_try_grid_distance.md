# Source: https://docs.snowflake.com/en/sql-reference/functions/h3_try_grid_distance.md

Categories:
:   [Geospatial functions](../functions-geospatial.md)

# H3_TRY_GRID_DISTANCE

A special version of [H3_GRID_DISTANCE](h3_grid_distance.md) that returns NULL if an error occurs when it
attempts to return the distance between two [H3](../data-types-geospatial.md) cells.

## Syntax

```sqlsyntax
H3_TRY_GRID_DISTANCE( <cell_id_1> , <cell_id_2> )
```

## Arguments

`cell_id_1`
:   An INTEGER value that represents the H3 cell ID ([index](https://h3geo.org/docs/core-library/h3Indexing)), or a VARCHAR value that represents the cell ID
    in hexadecimal format.

`cell_id_2`
:   An INTEGER value that represents the H3 cell ID ([index](https://h3geo.org/docs/core-library/h3Indexing)), or a VARCHAR value that represents the cell ID
    in hexadecimal format.

## Returns

Returns an INTEGER value or NULL.

* If the function can perform a successful calculation, returns the INTEGER value that represents the distance in grid
  cells between the two H3 cells.
* If the grid distance cannot be calculated (for example, when two cells belong to non-neighboring
  [base cells](https://h3geo.org/docs/library/index/cell/)), returns NULL without reporting an error.

## Usage notes

See [H3_GRID_DISTANCE](h3_grid_distance.md) for the usage notes.

## Examples

The following example attempts to calculate the distance between two cells. Because the cells belong to non-neighboring
base cells, the function fails to calculate the distance and returns NULL.

```sqlexample
SELECT H3_TRY_GRID_DISTANCE(582046271372525567, 581883543651614719);
```

```output
+--------------------------------------------------------------+
| H3_TRY_GRID_DISTANCE(582046271372525567, 581883543651614719) |
|--------------------------------------------------------------|
|                                                         NULL |
+--------------------------------------------------------------+
```

For examples that successfully calculate the distance between two H3 cells, see [H3_GRID_DISTANCE](h3_grid_distance.md).
