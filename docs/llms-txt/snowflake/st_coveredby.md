# Source: https://docs.snowflake.com/en/sql-reference/functions/st_coveredby.md

Categories:
:   [Geospatial functions](../functions-geospatial.md)

# ST_COVEREDBY

Returns TRUE if no point in one geospatial object is outside another geospatial object. In other words:

* [GEOGRAPHY](../data-types-geospatial.md) object `g1` is outside GEOGRAPHY object `g2`.
* [GEOMETRY](../data-types-geospatial.md) object `g1` is outside GEOMETRY object `g2`.

This is equivalent to `ST_COVERS(g2, g1)`.

Although ST_COVEREDBY and ST_WITHIN might seem similar, the two functions have subtle differences. For details on the differences
between “covered by” and “within”, see the
[Dimensionally Extended 9-Intersection Model (DE-9IM)](https://en.wikipedia.org/wiki/DE-9IM).

> **Note:**
>
> This function does not support using a GeometryCollection or FeatureCollection as input values.

> **Tip:**
>
> You can use the search optimization service to improve the performance of queries that call this function.
> For details, see [Search optimization service](../../user-guide/search-optimization-service.md).

See also:
:   [ST_COVERS](st_covers.md) , [ST_WITHIN](st_within.md)

## Syntax

```sqlsyntax
ST_COVEREDBY( <geography_expression_1> , <geography_expression_2> )

ST_COVEREDBY( <geometry_expression_1> , <geometry_expression_2> )
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

This shows a simple use of the ST_COVEREDBY function:

> ```sqlexample
> create table geospatial_table_01 (g1 GEOGRAPHY, g2 GEOGRAPHY);
> insert into geospatial_table_01 (g1, g2) values
>     ('POLYGON((0 0, 3 0, 3 3, 0 3, 0 0))', 'POLYGON((1 1, 2 1, 2 2, 1 2, 1 1))');
> ```
>
> ```sqlexample
> SELECT ST_COVEREDBY(g1, g2)
>     FROM geospatial_table_01;
> +----------------------+
> | ST_COVEREDBY(G1, G2) |
> |----------------------|
> | False                |
> +----------------------+
> ```
