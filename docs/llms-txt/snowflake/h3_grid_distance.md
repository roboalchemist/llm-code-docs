# Source: https://docs.snowflake.com/en/sql-reference/functions/h3_grid_distance.md

Categories:
:   [Geospatial functions](../functions-geospatial.md)

# H3_GRID_DISTANCE

Returns the distance between two [H3](../data-types-geospatial.md) cells specified by their IDs.

## Syntax

```sqlsyntax
H3_GRID_DISTANCE( <cell_id_1> , <cell_id_2> )
```

## Arguments

`cell_id_1`
:   An INTEGER that represents the H3 cell ID ([index](https://h3geo.org/docs/core-library/h3Indexing)), or a VARCHAR that represents the cell ID in hexadecimal format.

`cell_id_2`
:   An INTEGER that represents the H3 cell ID ([index](https://h3geo.org/docs/core-library/h3Indexing)), or a VARCHAR that represents the cell ID in hexadecimal format.

## Returns

Returns the INTEGER value that represents the distance in grid cells between the two H3 cells.

## Usage notes

The two input cell IDs must use the same resolution.

## Examples

The following example returns the distance (in terms of the number of grid cells) between two H3 cells. The example specifies the
H3 cell IDs as INTEGER values.

```sqlexample
SELECT H3_GRID_DISTANCE(617540519103561727, 617540519052967935);
```

```output
+----------------------------------------------------------+
| H3_GRID_DISTANCE(617540519103561727, 617540519052967935) |
|----------------------------------------------------------|
|                                                        5 |
+----------------------------------------------------------+
```

The following example specifies the hexadecimal values of the H3 cell IDs as VARCHAR values:

```sqlexample
SELECT H3_GRID_DISTANCE('891f1d48b93ffff', '891f1d4888fffff');
```

```output
+--------------------------------------------------------+
| H3_GRID_DISTANCE('891F1D48B93FFFF', '891F1D4888FFFFF') |
|--------------------------------------------------------|
|                                                      5 |
+--------------------------------------------------------+
```
