# Source: https://docs.snowflake.com/en/sql-reference/functions/h3_grid_disk.md

Categories:
:   [Geospatial functions](../functions-geospatial.md)

# H3_GRID_DISK

Returns an [array](../data-types-semistructured.md) of the IDs of the [H3](../data-types-geospatial.md) cells that
are within the k-distance from the specified cell. The IDs in the returned ARRAY are INTEGER values (if an INTEGER
value was provided as the input ID) or VARCHAR values containing the hexadecimal IDs (if a hexadecimal ID was provided
as the input ID).

## Syntax

```sqlsyntax
H3_GRID_DISK( <cell_id> , <k_value> )
```

## Arguments

`cell_id`
:   An INTEGER that represents the H3 cell ID ([index](https://h3geo.org/docs/core-library/h3Indexing)), or a VARCHAR that represents the cell ID in hexadecimal format.

`k_value`
:   An INTEGER that represents the grid distance. You must specify a non-negative value.

## Returns

Returns an ARRAY of the IDs of H3 cells that are within the distance `k_value` from the cell specified by
`cell_id`. The IDs are in one of the following formats:

* If `cell_id` is an INTEGER value, the function returns the IDs as INTEGER values.
* If `cell_id` is a VARCHAR value containing the hexadecimal ID, the function returns the hexadecimal IDs as VARCHAR
  values.

## Examples

The following example returns an ARRAY of the IDs of H3 cells within the grid distance of 1 from the cell with the ID
`617540519050084351` (specified as an INTEGER value).

```sqlexample
SELECT H3_GRID_DISK(617540519050084351, 1);
```

```output
+-------------------------------------+
| H3_GRID_DISK(617540519050084351, 1) |
|-------------------------------------|
| [                                   |
|   617540519050084351,               |
|   617540519051657215,               |
|   617540519050608639,               |
|   617540519050870783,               |
|   617540519050346495,               |
|   617540519051395071,               |
|   617540519051132927                |
| ]                                   |
+-------------------------------------+
```

The following example returns an ARRAY of the IDs of H3 cells within the grid distance of 1 from the cell with the ID
`891f1d48863ffff` (specified as a VARCHAR value).

```sqlexample
SELECT H3_GRID_DISK('891f1d48863ffff', 1);
```

```output
+------------------------------------+
| H3_GRID_DISK('891F1D48863FFFF', 1) |
|------------------------------------|
| [                                  |
|   "891f1d48863ffff",               |
|   "891f1d4887bffff",               |
|   "891f1d4886bffff",               |
|   "891f1d4886fffff",               |
|   "891f1d48867ffff",               |
|   "891f1d48877ffff",               |
|   "891f1d48873ffff"                |
| ]                                  |
+------------------------------------+
```
