# Source: https://docs.snowflake.com/en/sql-reference/functions/h3_get_resolution.md

Categories:
:   [Geospatial functions](../functions-geospatial.md)

# H3_GET_RESOLUTION

Returns the resolution of an [H3](../data-types-geospatial.md) cell.

## Syntax

```sqlsyntax
H3_GET_RESOLUTION( <cell_id> )
```

## Arguments

`cell_id`
:   An INTEGER that represents the H3 cell ID ([index](https://h3geo.org/docs/core-library/h3Indexing)), or a VARCHAR that represents the cell ID in hexadecimal format.

## Returns

Returns an INTEGER value between 0 and 15, which represents the resolution of the input H3 cell.

## Examples

The following example returns the resolution of the H3 cell with the ID `617540519050084351`. The example specifies the H3
cell ID as an INTEGER value.

```sqlexample
SELECT H3_GET_RESOLUTION(617540519050084351);
```

```output
+---------------------------------------+
| H3_GET_RESOLUTION(617540519050084351) |
|---------------------------------------|
|                                     9 |
+---------------------------------------+
```

The following example specifies the hexadecimal value of H3 cell ID (`89283087033ffff`) as a VARCHAR to return the resolution
of the cell.

```sqlexample
SELECT H3_GET_RESOLUTION('89283087033ffff');
```

```output
+--------------------------------------+
| H3_GET_RESOLUTION('89283087033FFFF') |
|--------------------------------------|
|                                    9 |
+--------------------------------------+
```
