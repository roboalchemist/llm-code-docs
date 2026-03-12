# Source: https://docs.snowflake.com/en/sql-reference/functions/h3_polygon_to_cells.md

Categories:
:   [Geospatial functions](../functions-geospatial.md)

# H3_POLYGON_TO_CELLS

Returns an [array](../data-types-semistructured.md) of INTEGER values of the IDs of [H3](../data-types-geospatial.md)
cells that have centroids contained by a Polygon (specified by a [GEOGRAPHY](../data-types-geospatial.md) object).

See also:
:   [H3_POLYGON_TO_CELLS_STRINGS](h3_polygon_to_cells_strings.md) , [H3_COVERAGE](h3_coverage.md)

## Syntax

```sqlsyntax
H3_POLYGON_TO_CELLS( <geography_polygon> , <target_resolution> )
```

## Arguments

`geography_polygon`
:   A GEOGRAPHY object that represents a Polygon.

`target_resolution`
:   An INTEGER between 0 and 15 (inclusive) that specifies the H3 [resolution](https://h3geo.org/docs/core-library/restable) that you want to use for the returned H3 cells.

    Specifying any other INTEGER value results in an error.

## Returns

Returns an array of INTEGER values for the IDs of the H3 cells that have centroids contained in the specified input Polygon.

## Usage notes

* The function uses planar approximation, which treats points on the Earth’s surface as if they were connected by straight lines,
  rather than curved arcs. If you need a spherical approximation, use [H3_COVERAGE](h3_coverage.md) instead.
* A cell is considered to be within the Polygon if its centroid is contained by the Polygon.
* When you apply [FLATTEN](flatten.md) to the array returned by the function,
  [cast](../data-type-conversion.md) each value explicitly to an integer.

## Examples

The following example returns an ARRAY of the IDs of H3 cells that have centroids contained in the specified Polygon.

```sqlexample
SELECT H3_POLYGON_TO_CELLS(
  TO_GEOGRAPHY(
    'POLYGON((-122.481889 37.826683,-122.479487 37.808548,-122.474150 37.808904,-122.476510 37.826935,-122.481889 37.826683))'
  ),
  9) AS h3_cells_in_polygon;
```

```output
+-----------------------+
| H3_CELLS_IN_POLYGON   |
|-----------------------|
| [                     |
|   617700171176476671, |
|   617700171168874495, |
|   617700171177525247, |
|   617700171167563775, |
|   617700171225497599, |
|   617700171188011007, |
|   617700171168350207, |
|   617700171168612351, |
|   617700171167825919  |
| ]                     |
+-----------------------+
```
