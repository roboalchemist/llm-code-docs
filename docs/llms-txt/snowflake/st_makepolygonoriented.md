# Source: https://docs.snowflake.com/en/sql-reference/functions/st_makepolygonoriented.md

Categories:
:   [Geospatial functions](../functions-geospatial.md)

# ST_MAKEPOLYGONORIENTED

Constructs a [GEOGRAPHY](../data-types-geospatial.md) object that represents a Polygon without holes. The function uses the
specified LineString as the outer loop.

This function does not attempt to correct the orientation of the loop, thus allowing for the creation of Polygons that span more
than half of the globe. In contrast, [ST_MAKEPOLYGON](st_makepolygon.md) inverts the orientation of
those large shapes.

See also:
:   [TO_GEOGRAPHY](to_geography.md), [ST_MAKEPOLYGON](st_makepolygon.md)

## Syntax

```sqlsyntax
ST_MAKEPOLYGONORIENTED( <geography_expression> )
```

## Arguments

`geography_expression`
:   A GEOGRAPHY object that represents a LineString in which the last point is the same as the first (i.e. a loop).

## Returns

The function returns a value of type GEOGRAPHY.

## Usage notes

* The lines of the Polygon must form a loop. In other words, the last Point in the sequence of Points defining the LineString
  must be the same Point as the first Point in the sequence.
* As you follow along the loop, the inside of the Polygon should be on the left, and the outside of the Polygon should be on the
  right.

## Examples

The following example demonstrates how to use the ST_MAKEPOLYGONORIENTED function. The sequence of Points below defines a
great circle rectangular area one degree wide and two degrees high. The lower left corner of the Polygon starts at the equator (latitude)
and Greenwich (longitude). The last Point in the sequence is the same as the first Point, which completes the loop.

The example passes the GEOGRAPHY object for the Polygon to the [ST_AREA](st_area.md) function to return the area of the Polygon.

```sqlexample
SELECT ST_AREA(
  ST_MAKEPOLYGONORIENTED(
    TO_GEOGRAPHY('LINESTRING(0.0 0.0, 1.0 0.0, 1.0 2.0, 0.0 2.0, 0.0 0.0)')
  )
) AS area_of_polygon;

+------------------+
|  AREA_OF_POLYGON |
|------------------|
| 24724306355.5504 |
+------------------+
```

The following example is the same shape but has the opposite orientation. As indicated by the difference in the area of the
Polygon, the Polygon represents the entire globe except for that previous shape.

```sqlexample
SELECT ST_AREA(
  ST_MAKEPOLYGONORIENTED(
    TO_GEOGRAPHY('LINESTRING(0.0 0.0, 0.0 2.0, 1.0 2.0, 1.0 0.0, 0.0 0.0)')
  )
) AS area_of_polygon;

+-----------------+
| AREA_OF_POLYGON |
|-----------------|
| 510041348811633 |
+-----------------+
```
