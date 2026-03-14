# Source: https://docs.snowflake.com/en/sql-reference/functions/st_centroid.md

Categories:
:   [Geospatial functions](../functions-geospatial.md)

# ST_CENTROID

Returns the Point representing the geometric center of a [GEOGRAPHY](../data-types-geospatial.md) or
[GEOMETRY](../data-types-geospatial.md) object.

## Syntax

```sqlsyntax
ST_CENTROID( <geography_or_geometry_expression> )
```

## Arguments

`geography_or_geometry_expression`
:   The argument must be an expression of type GEOGRAPHY or GEOMETRY.

## Returns

Returns a GEOGRAPHY or GEOMETRY object for the Point that represents geometric center of the input object.

## Usage notes

* Returns NULL if the input is NULL.
* If the input object is a GeometryCollection that contains different types of objects (Polygons, LineStrings, and Points),
  ST_CENTROID uses the type with the [highest dimension](st_dimension.md) to determine the geometric
  center. For example:

  * If the GeometryCollection contains Polygons, LineStrings, and Points, ST_CENTROID uses the Polygons and ignores the
    LineStrings and Points in the collection.
  * If the GeometryCollection contains LineStrings and Points, ST_CENTROID uses the LineStrings and ignores the Points in the
    collection.

* For GEOMETRY objects, the returned GEOMETRY object has the same SRID as the input.

## Examples

### GEOGRAPHY examples

The following example returns the Point that represents the geometric center of a LineString.

> ```sqlexample
> SELECT ST_CENTROID(
>     TO_GEOGRAPHY(
>         'LINESTRING(0 0, 0 -2)'
>     )
> ) as center_of_linestring;
> +----------------------+
> | CENTER_OF_LINESTRING |
> |----------------------|
> | POINT(0 -1)          |
> +----------------------+
> ```

The following example returns the Point that represents the geometric center of a Polygon.

> ```sqlexample
> SELECT ST_CENTROID(
>     TO_GEOGRAPHY(
>         'POLYGON((10 10, 10 20, 20 20, 20 10, 10 10))'
>     )
> ) as center_of_polygon;
> +------------------------+
> | CENTER_OF_POLYGON      |
> |------------------------|
> | POINT(15 15.014819855) |
> +------------------------+
> ```

The following example returns the Point that represents the geometric center of a GeometryCollection. This collection contains a
Polygon, LineString, and Point. ST_CENTROID only uses the Polygon (and ignores the LineString and Point) when determining the
geometric center.

> ```sqlexample
> SELECT ST_CENTROID(
>     TO_GEOGRAPHY(
>         'GEOMETRYCOLLECTION(POLYGON((10 10, 10 20, 20 20, 20 10, 10 10)), LINESTRING(0 0, 0 -2), POINT(50 -50))'
>     )
> ) as center_of_collection_with_polygons;
> +------------------------------------+
> | CENTER_OF_COLLECTION_WITH_POLYGONS |
> |------------------------------------|
> | POINT(15 15.014819855)             |
> +------------------------------------+
> ```

### GEOMETRY examples

The following example computes the centroid of a simple rectangular Polygon. Note how the result differs from the result when
using ST_CENTROID with a GEOGRAPHY object

> ```sqlexample
> SELECT ST_CENTROID(TO_GEOMETRY('POLYGON((10 10, 10 20, 20 20, 20 10, 10 10))'));
> ```
>
> ```none
> +--------------------------------------------------------------------------+
> | ST_CENTROID(TO_GEOMETRY('POLYGON((10 10, 10 20, 20 20, 20 10, 10 10))')) |
> |--------------------------------------------------------------------------|
> | POINT(15 15)                                                             |
> +--------------------------------------------------------------------------+
> ```
