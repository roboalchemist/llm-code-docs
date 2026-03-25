# Source: https://docs.snowflake.com/en/sql-reference/functions/st_covers.md

Categories:
:   [Geospatial functions](../functions-geospatial.md)

# ST_COVERS

Returns TRUE if no point in one geospatial object is outside of another geospatial object. In other words:

* [GEOGRAPHY](../data-types-geospatial.md) object `g2` is outside GEOGRAPHY object `g1`.
* [GEOMETRY](../data-types-geospatial.md) object `g2` is outside GEOMETRY object `g1`.

ST_COVERS is similar to, but subtly different from, ST_CONTAINS. For details on the differences between “covers” and “contains”,
see the [Dimensionally Extended 9-Intersection Model (DE-9IM)](https://en.wikipedia.org/wiki/DE-9IM).

Although ST_COVERS and ST_CONTAINS might seem similar, the two functions have subtle differences. For details on the differences
between “covers” and “contains”, see the
[Dimensionally Extended 9-Intersection Model (DE-9IM)](https://en.wikipedia.org/wiki/DE-9IM).

> **Note:**
>
> This function does not support using a GeometryCollection or FeatureCollection as input values.

> **Tip:**
>
> You can use the search optimization service to improve the performance of queries that call this function.
> For details, see [Search optimization service](../../user-guide/search-optimization-service.md).

See also:
:   [ST_CONTAINS](st_contains.md) , [ST_COVEREDBY](st_coveredby.md)

## Syntax

```sqlsyntax
ST_COVERS( <geography_expression_1> , <geography_expression_2> )

ST_COVERS( <geometry_expression_1> , <geometry_expression_2> )
```

## Arguments

`geography_expression_1`
:   A GEOGRAPHY object that is not a GeometryCollection or FeatureCollection.

`geography_expression_2`
:   A GEOGRAPHY object that is not a GeometryCollection or FeatureCollection.

`geometry_expression_1`
:   A GEOMETRY object that is not a GeometryCollection or FeatureCollection.

`geometry_expression_2`
:   A GEOMETRY object that is not a GeometryCollection or FeatureCollection.

## Returns

BOOLEAN.

## Usage notes

* For GEOMETRY objects, the function reports an error if the two input GEOMETRY objects have different SRIDs.

## Examples

### GEOGRAPHY examples

This shows a simple use of the ST_COVERS function:

> ```sqlexample
> create table geospatial_table_01 (g1 GEOGRAPHY, g2 GEOGRAPHY);
> insert into geospatial_table_01 (g1, g2) values
>     ('POLYGON((0 0, 3 0, 3 3, 0 3, 0 0))', 'POLYGON((1 1, 2 1, 2 2, 1 2, 1 1))');
> ```
>
> ```sqlexample
> SELECT ST_COVERS(g1, g2)
>     FROM geospatial_table_01;
> +-------------------+
> | ST_COVERS(G1, G2) |
> |-------------------|
> | True              |
> +-------------------+
> ```

### GEOMETRY examples

The query below shows several examples of using ST_COVERS. Note how the Polygon covers (but does not
[contain](st_contains.md)) a LineString on its border.

> ```sqlexample
> SELECT ST_COVERS(poly, poly_inside),
>        ST_COVERS(poly, poly),
>        ST_COVERS(poly, line_on_boundary),
>        ST_COVERS(poly, line_inside)
>   FROM (SELECT TO_GEOMETRY('POLYGON((-2 0, 0 2, 2 0, -2 0))') AS poly,
>                TO_GEOMETRY('POLYGON((-1 0, 0 1, 1 0, -1 0))') AS poly_inside,
>                TO_GEOMETRY('LINESTRING(-1 1, 0 2, 1 1)') AS line_on_boundary,
>                TO_GEOMETRY('LINESTRING(-2 0, 0 0, 0 1)') AS line_inside);
> ```
>
> ```none
> +------------------------------+----------------------+----------------------------------+-----------------------------+
> | ST_COVERS(POLY, POLY_INSIDE) | ST_COVERS(POLY,POLY) | ST_COVERS(POLY,LINE_ON_BOUNDARY) | ST_COVERS(POLY,LINE_INSIDE) |
> |------------------------------+----------------------+----------------------------------+-----------------------------|
> | True                         | True                 | True                             | True                        |
> +------------------------------+----------------------+----------------------------------+-----------------------------+
> ```
