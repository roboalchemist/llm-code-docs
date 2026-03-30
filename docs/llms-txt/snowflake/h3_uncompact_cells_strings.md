# Source: https://docs.snowflake.com/en/sql-reference/functions/h3_uncompact_cells_strings.md

Categories:
:   [Geospatial functions](../functions-geospatial.md)

# H3_UNCOMPACT_CELLS_STRINGS

Returns an [array](../data-types-semistructured.md) of [VARIANT](../data-types-semistructured.md) values
that contain the VARCHAR hexadecimal IDs of [H3](../data-types-geospatial.md)
cells at the specified resolution that cover the same area as the H3 cells in the input.

## Syntax

```sqlsyntax
H3_UNCOMPACT_CELLS_STRINGS( <array_of_cell_ids> , <target_resolution> )
```

## Arguments

`array_of_cell_ids`
:   An array of VARIANT values that contain VARCHAR hexadecimal values that represent H3 cell IDs ([indexes](https://h3geo.org/docs/core-library/h3Indexing)).

`target_resolution`
:   An INTEGER value between 0 and 15 (inclusive) specifying the H3 [resolution](https://h3geo.org/docs/core-library/restable) that you want to use for the returned H3 cells.

    Specifying any other INTEGER value results in an error.

## Returns

Returns a value of the ARRAY data type or NULL.

* If the input is an array of VARIANT values that contain VARCHAR hexadecimal values, returns an array of VARIANT values
  that contain the VARCHAR hexadecimal values that represent the set of H3 cells at the specified resolution.
* If the input is NULL, returns NULL without reporting an error.

## Usage notes

* All of the VARCHAR hexadecimal values in the input must represent valid H3 cells.
* The input cells cannot have a higher resolution than the resolution specified in the
  `target_resolution` argument.

## Examples

The following example returns an uncompacted set of H3 cells that represent valid H3 cell IDs
and a target resolution of `10`.

```sqlexample
SELECT H3_UNCOMPACT_CELLS_STRINGS(
  [
    '8a2a1072339ffff',
    '892a1072377ffff'
  ],
  10
) AS uncompacted;
```

```output
+----------------------+
| UNCOMPACTED          |
|----------------------|
| [                    |
|   "8a2a1072339ffff", |
|   "8a2a10723747fff", |
|   "8a2a1072374ffff", |
|   "8a2a10723757fff", |
|   "8a2a1072375ffff", |
|   "8a2a10723767fff", |
|   "8a2a1072376ffff", |
|   "8a2a10723777fff"  |
| ]                    |
+----------------------+
```
