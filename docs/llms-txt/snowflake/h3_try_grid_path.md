# Source: https://docs.snowflake.com/en/sql-reference/functions/h3_try_grid_path.md

Categories:
:   [Geospatial functions](../functions-geospatial.md)

# H3_TRY_GRID_PATH

A special version of [H3_GRID_PATH](h3_grid_path.md) that returns NULL if an error occurs when it
attempts to return an array of VARIANT values that contain the IDs of the
[H3](../data-types-geospatial.md) cells that represent the line between two cells.

## Syntax

```sqlsyntax
H3_TRY_GRID_PATH( <cell_id_1> , <cell_id_2> )
```

## Arguments

`cell_id_1`
:   An INTEGER value that represents the H3 cell ID ([index](https://h3geo.org/docs/core-library/h3Indexing)), or a VARCHAR value that represents the cell ID
    in hexadecimal format.

`cell_id_2`
:   An INTEGER value that represents the H3 cell ID ([index](https://h3geo.org/docs/core-library/h3Indexing)), or a VARCHAR value that represents the cell ID
    in hexadecimal format.

## Returns

Returns a value of the ARRAY data type or NULL.

* If the function performs a successful calculation, returns an array of VARIANT values that contain the IDs of H3 cells
  that represent the line between the cells specified by `cell_id_1` and `cell_id_2`. For information about
  the format of the IDs, see [H3_GRID_PATH](h3_grid_path.md).
* If the line cannot be calculated (for example, when two cells belong to non-neighboring
  [base cells](https://h3geo.org/docs/library/index/cell/)), returns NULL without reporting an error.

## Usage notes

See [H3_GRID_PATH](h3_grid_path.md) for the usage notes.

## Examples

The following example attempts to return a line between two cells. Because the cells belong to non-neighboring
base cells, the function fails to return the line and returns NULL.

```sqlexample
SELECT H3_TRY_GRID_PATH('813d7ffffffffff', '81343ffffffffff');
```

```output
+--------------------------------------------------------+
| H3_TRY_GRID_PATH('813D7FFFFFFFFFF', '81343FFFFFFFFFF') |
|--------------------------------------------------------|
| NULL                                                   |
+--------------------------------------------------------+
```

For examples that successfully calculate the path between two H3 cells, see [H3_GRID_PATH](h3_grid_path.md).
