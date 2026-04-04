# Source: https://docs.snowflake.com/en/sql-reference/functions/st_envelope.md

Categories:
:   [Geospatial functions](../functions-geospatial.md)

# ST_ENVELOPE

Returns the minimum bounding box (a rectangular “envelope”) that encloses a specified
[GEOGRAPHY](../data-types-geospatial.md) or [GEOMETRY](../data-types-geospatial.md) object.

## Syntax

```sqlsyntax
ST_ENVELOPE( <geography_or_geometry_expression> )
```

## Arguments

`geography_or_geometry_expression`
:   The argument must be of type GEOGRAPHY or GEOMETRY.

## Returns

The function returns a value of type [GEOGRAPHY](../data-types-geospatial.md) or [GEOMETRY](../data-types-geospatial.md)
that represents the minimum bounding box around the input object.

## Usage notes

* For GEOGRAPHY objects:

  * If `geography_expression` is a LineString that represents a meridian arc (an arc along a line of longitude),
    ST_ENVELOPE returns that LineString.
  * If `geography_expression` is a LineString that represents an arc on a parallel (an arc along a line of latitude)
    other than the equator, ST_ENVELOPE returns a Polygon that represents the bounding box for the arc.
  * If `geography_expression` is a single Point, ST_ENVELOPE returns that Point.
* For GEOMETRY objects:

  * In degenerate cases (e.g. where the input is a point or a vertical or horizontal line), the function may return a geometry of
    lower dimension (i.e. a Point or LineString).
  > * For GEOMETRY objects, the returned GEOMETRY object has the same SRID as the input.

## Examples

### GEOGRAPHY examples

The following example returns the minimum bounding box for a polygon:

> ```sqlexample
> SELECT ST_ENVELOPE(
>     TO_GEOGRAPHY(
>         'POLYGON((-122.306067 37.55412, -122.32328 37.561801, -122.325879 37.586852, -122.306067 37.55412))'
>     )
> ) as minimum_bounding_box_around_polygon;
> +-----------------------------------------------------------------------------------------------------------------------+
> | MINIMUM_BOUNDING_BOX_AROUND_POLYGON                                                                                   |
> |-----------------------------------------------------------------------------------------------------------------------|
> | POLYGON((-122.325879 37.55412,-122.306067 37.55412,-122.306067 37.586852,-122.325879 37.586852,-122.325879 37.55412)) |
> +-----------------------------------------------------------------------------------------------------------------------+
> ```

The following example passes in a LineString that represents a meridian arc. The function returns the same LineString, rather
than a Polygon.

> ```sqlexample
> SELECT ST_ENVELOPE(
>     TO_GEOGRAPHY(
>         'LINESTRING(-122.32328 37.561801, -122.32328 37.562001)'
>     )
> ) as minimum_bounding_box_around_meridian_arc;
> +-------------------------------------------------------+
> | MINIMUM_BOUNDING_BOX_AROUND_MERIDIAN_ARC              |
> |-------------------------------------------------------|
> | LINESTRING(-122.32328 37.561801,-122.32328 37.562001) |
> +-------------------------------------------------------+
> ```

The following example passes in a LineString that represents an arc on a parallel that is not the equator. The function
returns a Polygon that represents the bounding box:

> ```sqlexample
> SELECT ST_ENVELOPE(
>     TO_GEOGRAPHY(
>         'LINESTRING(-122.32328 37.561801,-122.32351 37.561801)'
>     )
> ) as minimum_bounding_box_around_arc_along_parallel;
> +---------------------------------------------------------------------------------------------------------------------+
> | MINIMUM_BOUNDING_BOX_AROUND_ARC_ALONG_PARALLEL                                                                      |
> |---------------------------------------------------------------------------------------------------------------------|
> | POLYGON((-122.32351 37.561801,-122.32328 37.561801,-122.32328 37.561801,-122.32351 37.561801,-122.32351 37.561801)) |
> +---------------------------------------------------------------------------------------------------------------------+
> ```

The following example passes in a single Point. The function returns the same Point:

> ```sqlexample
> SELECT ST_ENVELOPE(
>     TO_GEOGRAPHY(
>         'POINT(-122.32328 37.561801)'
>     )
> ) as minimum_bounding_box_around_point;
> +-----------------------------------+
> | MINIMUM_BOUNDING_BOX_AROUND_POINT |
> |-----------------------------------|
> | POINT(-122.32328 37.561801)       |
> +-----------------------------------+
> ```

### GEOMETRY examples
