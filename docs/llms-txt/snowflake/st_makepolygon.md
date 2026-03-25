# Source: https://docs.snowflake.com/en/sql-reference/functions/st_makepolygon.md

Categories:
:   [Geospatial functions](../functions-geospatial.md)

# ST_MAKEPOLYGON , ST_POLYGON

Constructs a [GEOGRAPHY](../data-types-geospatial.md) or [GEOMETRY](../data-types-geospatial.md) object that represents
a Polygon without holes. The function uses the specified LineString as the outer loop.

This function corrects the orientation of the loop to prevent the creation of Polygons that span more than half of the globe. In
contrast, [ST_MAKEPOLYGONORIENTED](st_makepolygonoriented.md) doesn’t attempt to correct the orientation of the loop.

See also:
:   [TO_GEOGRAPHY](to_geography.md) , [TO_GEOMETRY](to_geometry.md) , [ST_MAKEPOLYGONORIENTED](st_makepolygonoriented.md)

## Syntax

```sqlsyntax
ST_MAKEPOLYGON( <geography_or_geometry_expression> )
```

## Arguments

`geography_or_geometry_expression`
:   A GEOGRAPHY or GEOMETRY object that represents a LineString in which the last point is the same as the first (i.e. a
    loop).

## Returns

The function returns a value of type GEOGRAPHY or GEOMETRY.

## Usage notes

* The lines of the Polygon must form a loop. In other words, the last Point in the sequence of Points defining the LineString
  must be the same Point as the first Point in the sequence.
* ST_POLYGON is an alias for ST_MAKEPOLYGON.

* For GEOMETRY objects, the returned GEOMETRY object has the same SRID as the input.

## Examples

### GEOGRAPHY examples

This shows a simple use of the ST_MAKEPOLYGON function. The sequence of points below defines a great circle
rectangular area 1 degree wide and 2 degrees high, with the lower left corner of the polygon starting at the
equator (latitude) and Greenwich (longitude). The last point in the sequence is the same as the first point,
which completes the loop.

> ```sqlexample
> SELECT ST_MAKEPOLYGON(
>    TO_GEOGRAPHY('LINESTRING(0.0 0.0, 1.0 0.0, 1.0 2.0, 0.0 2.0, 0.0 0.0)')
>    ) AS polygon1;
> +--------------------------------+
> | POLYGON1                       |
> |--------------------------------|
> | POLYGON((0 0,1 0,1 2,0 2,0 0)) |
> +--------------------------------+
> ```

### GEOMETRY examples

This shows a simple use of the ST_MAKEPOLYGON function.

> ```sqlexample
> SELECT ST_MAKEPOLYGON(
>   TO_GEOMETRY('LINESTRING(0.0 0.0, 1.0 0.0, 1.0 2.0, 0.0 2.0, 0.0 0.0)')
>   ) AS polygon;
> ```
>
> ```none
> +--------------------------------+
> | POLYGON                        |
> |--------------------------------|
> | POLYGON((0 0,1 0,1 2,0 2,0 0)) |
> +--------------------------------+
> ```
