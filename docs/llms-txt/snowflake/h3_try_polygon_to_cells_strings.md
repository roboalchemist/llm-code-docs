# Source: https://docs.snowflake.com/en/sql-reference/functions/h3_try_polygon_to_cells_strings.md

Categories:
:   [Geospatial functions](../functions-geospatial.md)

# H3_TRY_POLYGON_TO_CELLS_STRINGS

A special version of [H3_POLYGON_TO_CELLS_STRINGS](h3_polygon_to_cells_strings.md) that returns NULL if an error
occurs when it attempts to return an [array](../data-types-semistructured.md) of VARCHAR values of the
hexadecimal IDs of [H3](../data-types-geospatial.md) cells that have centroids contained by
a Polygon (specified by a [GEOGRAPHY](../data-types-geospatial.md) object).

## Syntax

```sqlsyntax
H3_TRY_POLYGON_TO_CELLS_STRINGS( <geography_polygon> , <target_resolution> )
```

## Arguments

`geography_polygon`
:   A GEOGRAPHY object that represents a Polygon.

`target_resolution`
:   An INTEGER between 0 and 15 (inclusive) that specifies the H3 [resolution](https://h3geo.org/docs/core-library/restable) that you want to use for the returned H3 cells.

    Specifying any other INTEGER value results in an error.

## Returns

Returns an array of VARCHAR values or NULL.

* If the function can perform a successful calculation, returns an array of VARCHAR values for the hexadecimal IDs
  of the H3 cells that have centroids contained in the specified input Polygon.
* If the function cannot perform a successful calculation, returns NULL without reporting an error.

## Usage notes

See [H3_POLYGON_TO_CELLS_STRINGS](h3_polygon_to_cells_strings.md) for the usage notes.

## Examples

The following example attempts to return an array of VARCHAR values of the hexadecimal IDs of
[H3](../data-types-geospatial.md) cells that have centroids contained by a Polygon (specified by
a [GEOGRAPHY](../data-types-geospatial.md) object). Because the array with the cells that cover
the given hexagon at the given resolution exceeds the allowed size limit, the function returns NULL.

```sqlexample
SELECT H3_TRY_POLYGON_TO_CELLS_STRINGS(
  TO_GEOGRAPHY('POLYGON((-108.959 40.948,
                         -109.015 37.077,
                         -102.117 36.956,
                         -102.134 40.953,
                         -108.959 40.948))'
              ), 15) AS h3_cells_in_polygon;
```

```output
+---------------------+
| H3_CELLS_IN_POLYGON |
|---------------------|
| NULL                |
+---------------------+
```

For examples that successfully return an array of IDs, see [H3_POLYGON_TO_CELLS_STRINGS](h3_polygon_to_cells_strings.md).
