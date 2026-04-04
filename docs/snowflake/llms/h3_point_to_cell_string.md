# Source: https://docs.snowflake.com/en/sql-reference/functions/h3_point_to_cell_string.md

Categories:
:   [Geospatial functions](../functions-geospatial.md)

# H3_POINT_TO_CELL_STRING

Returns the hexadecimal value of an [H3](../data-types-geospatial.md) cell ID for a Point (specified by a
[GEOGRAPHY](../data-types-geospatial.md) object) at a given resolution.

See also:
:   [H3_POINT_TO_CELL](h3_point_to_cell.md) , [H3_CELL_TO_POINT](h3_cell_to_point.md)

## Syntax

```sqlsyntax
H3_POINT_TO_CELL_STRING( <geography_point> , <target_resolution> )
```

## Arguments

`geography_point`
:   A GEOGRAPHY object that represents a Point.

`target_resolution`
:   An INTEGER between 0 and 15 (inclusive) that specifies the H3 [resolution](https://h3geo.org/docs/core-library/restable) that you want to use for the returned H3 cell.

    Specifying any other INTEGER value results in an error.

## Returns

Returns an VARCHAR value that corresponds to the hexadecimal H3 cell ID for the given location and resolution.

## Examples

The following example returns the hexadecimal H3 cell ID for the Brandenburg Gate at resolution 8.

```sqlexample
SELECT H3_POINT_TO_CELL_STRING(ST_POINT(13.377704, 52.516262), 8);
```

```output
+------------------------------------------------------------+
| H3_POINT_TO_CELL_STRING(ST_POINT(13.377704, 52.516262), 8) |
|------------------------------------------------------------|
|  881F1D4887FFFFF                                           |
+------------------------------------------------------------+
```

The following example demonstrates that you cannot specify a resolution outside of 0 through 15.

```sqlexample
SELECT H3_POINT_TO_CELL_STRING(ST_POINT(13.377704, 52.516262), 18);
```

```output
100410 (P0000): Invalid H3 resolution value: 18. Resolution must be between 0 (coarsest) and 15 (finest).
```
