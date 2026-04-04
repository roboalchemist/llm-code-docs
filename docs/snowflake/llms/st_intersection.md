# Source: https://docs.snowflake.com/en/sql-reference/functions/st_intersection.md

Categories:
:   [Geospatial functions](../functions-geospatial.md)

# ST_INTERSECTION

Given two input GEOGRAPHY objects, returns a GEOGRAPHY object that represents the shape containing the set of points that are
common to both input objects (i.e. the intersection of the two objects).

See also:
:   [ST_INTERSECTION_AGG](st_intersection_agg.md) , [ST_UNION](st_union.md) , [ST_DIFFERENCE](st_difference.md) , [ST_SYMDIFFERENCE](st_symdifference.md)

## Syntax

```sqlsyntax
ST_INTERSECTION( <geography_expression_1> , <geography_expression_2> )
```

## Arguments

`geography_expression_1`
:   A GEOGRAPHY object.

`geography_expression_2`
:   A GEOGRAPHY object.

## Returns

The function returns a value of type GEOGRAPHY.

## Usage notes

* If any vertex of one input object is on the boundary of the other input object (excluding the vertices), the output might or
  might not include that vertex point.

  For example, suppose that `geography_expression_1` is `POINT(1 1)` and `geography_expression_2` is
  `LINESTRING(1 0, 1 2)`. In this case, `geography_expression_1` is on the boundary of `geography_expression_2`
  but is not a vertex of it.

  In this example, the expected output is `POINT(1 1)`, but the actual output might be an empty geography (represented by NULL).

  To help to detect and work around these cases, one potential idea is to use [ST_DWITHIN](st_dwithin.md) to
  determine if the minimum distance between the two input objects is `0`. For example, you can check if a point lies on top of a
  LineString by checking if the minimum distance between the two objects is zero:

  > ```sqlexample
  > SELECT TO_GEOGRAPHY('POLYGON((0 0, 1 0, 2 1, 1 2, 2 3, 1 4, 0 4, 0 0))') AS polygon,
  >        TO_GEOGRAPHY('POINT(0 2)') AS point,
  >        ST_DWITHIN(polygon, point, 0) AS point_is_on_top_of_polygon,
  >        ST_INTERSECTION(polygon, point);
  > ```

  This statement produces the following output:

  > ```none
  > +--------------------------------------------+------------+----------------------------+---------------------------------+
  > | POLYGON                                    | POINT      | POINT_IS_ON_TOP_OF_POLYGON | ST_INTERSECTION(POLYGON, POINT) |
  > |--------------------------------------------+------------+----------------------------+---------------------------------|
  > | POLYGON((0 0,1 0,2 1,1 2,2 3,1 4,0 4,0 0)) | POINT(0 2) | True                       | NULL                            |
  > +--------------------------------------------+------------+----------------------------+---------------------------------+
  > ```

  The function is not guaranteed to produce normalized and/or minimal results. For example, an output could consist of a
  LineString containing several points that actually forms just one straight segment.

## Examples

The following example returns a GEOGRAPHY object that represents the intersection of two input GEOGRAPHY objects:

> ```sqlexample
> ALTER SESSION SET GEOGRAPHY_OUTPUT_FORMAT = 'WKT';
>
> SELECT ST_INTERSECTION(
>   TO_GEOGRAPHY('POLYGON((0 0, 1 0, 2 1, 1 2, 2 3, 1 4, 0 4, 0 0))'),
>   TO_GEOGRAPHY('POLYGON((3 0, 3 4, 2 4, 1 3, 2 2, 1 1, 2 0, 3 0))'))
> AS intersection_of_objects;
> ```

This example produces the following output:

> ```none
> +-----------------------------------------------------------------------------------------------------------------------------------------+
> | INTERSECTION_OF_OBJECTS                                                                                                                 |
> |-----------------------------------------------------------------------------------------------------------------------------------------|
> | MULTIPOLYGON(((1.5 0.5000571198,2 1,1.5 1.500171359,1 1,1.5 0.5000571198)),((1.5 2.500285599,2 3,1.5 3.500399839,1 3,1.5 2.500285599))) |
> +-----------------------------------------------------------------------------------------------------------------------------------------+
> ```

The following images illustrate the differences in the areas that represent the input and output objects:

| Input | Output |
| --- | --- |
|  |  |
