# Source: https://docs.snowflake.com/en/sql-reference/functions/st_disjoint.md

Categories:
:   [Geospatial functions](../functions-geospatial.md)

# ST_DISJOINT

Returns TRUE if the two [GEOGRAPHY](../data-types-geospatial.md) objects or the two
[GEOMETRY](../data-types-geospatial.md) objects are disjoint (i.e. do not share any portion of space). ST_DISJOINT is
equivalent to NOT [ST_INTERSECTS(expr1, expr2)](st_intersects.md).

> **Note:**
>
> This function does not support using a GeometryCollection or FeatureCollection as input values.

See also:
:   [ST_INTERSECTS](st_intersects.md)

## Syntax

```sqlsyntax
ST_DISJOINT( <geography_expression_1> , <geography_expression_2> )

ST_DISJOINT( <geometry_expression_1> , <geometry_expression_2> )
```

## Arguments

`geography_expression_1`
:   A GEOGRAPHY object.

`geography_expression_2`
:   A GEOGRAPHY object.

`geometry_expression_1`
:   A GEOMETRY object.

`geometry_expression_2`
:   A GEOMETRY object.

## Returns

BOOLEAN.

## Usage notes

* For GEOMETRY objects, the function reports an error if the two input GEOMETRY objects have different SRIDs.

## Examples

### GEOGRAPHY examples

The following examples use the ST_DISJOINT function to determine if two geospatial objects are disjoint:

> ```sqlexample
> -- These two polygons are disjoint and do not intersect.
> SELECT ST_DISJOINT(
>     TO_GEOGRAPHY('POLYGON((0 0, 2 0, 2 2, 0 2, 0 0))'),
>     TO_GEOGRAPHY('POLYGON((3 3, 5 3, 5 5, 3 5, 3 3))')
>     );
> +---------------------------------------------------------+
> | ST_DISJOINT(                                            |
> |     TO_GEOGRAPHY('POLYGON((0 0, 2 0, 2 2, 0 2, 0 0))'), |
> |     TO_GEOGRAPHY('POLYGON((3 3, 5 3, 5 5, 3 5, 3 3))')  |
> |     )                                                   |
> |---------------------------------------------------------|
> | True                                                    |
> +---------------------------------------------------------+
> ```
>
> ```sqlexample
> -- These two polygons intersect and are not disjoint.
> SELECT ST_DISJOINT(
>     TO_GEOGRAPHY('POLYGON((0 0, 2 0, 2 2, 0 2, 0 0))'),
>     TO_GEOGRAPHY('POLYGON((1 1, 3 1, 3 3, 1 3, 1 1))')
>     );
> +---------------------------------------------------------+
> | ST_DISJOINT(                                            |
> |     TO_GEOGRAPHY('POLYGON((0 0, 2 0, 2 2, 0 2, 0 0))'), |
> |     TO_GEOGRAPHY('POLYGON((1 1, 3 1, 3 3, 1 3, 1 1))')  |
> |     )                                                   |
> |---------------------------------------------------------|
> | False                                                   |
> +---------------------------------------------------------+
> ```
