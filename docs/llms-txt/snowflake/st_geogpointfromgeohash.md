# Source: https://docs.snowflake.com/en/sql-reference/functions/st_geogpointfromgeohash.md

Categories:
:   [Geospatial functions](../functions-geospatial.md), [Conversion functions](../functions-conversion.md)

# ST_GEOGPOINTFROMGEOHASH

Returns a [GEOGRAPHY](../data-types-geospatial.md) object for the Point that represents the center of a
[geohash](st_geohash.md).

See also:
:   [ST_GEOHASH](st_geohash.md), [ST_GEOGFROMGEOHASH](st_geogfromgeohash.md)

## Syntax

```sqlsyntax
ST_GEOGPOINTFROMGEOHASH( <geohash> )
```

## Arguments

`geohash`
:   The argument must be a geohash.

## Returns

The function returns a value of type [GEOGRAPHY](../data-types-geospatial.md) that represents the Point that is
the center of the geohash.

## Examples

The following example returns the GEOGRAPHY object for the Point at the center of a geohash:

> ```sqlexample
> SELECT ST_GEOGPOINTFROMGEOHASH('9q9j8ue2v71y5zzy0s4q')
>     AS geography_center_point_of_geohash;
> +-----------------------------------+
> | GEOGRAPHY_CENTER_POINT_OF_GEOHASH |
> |-----------------------------------|
> | {                                 |
> |   "coordinates": [                |
> |     -1.223060999999999e+02,       |
> |     3.755416200000003e+01         |
> |   ],                              |
> |   "type": "Point"                 |
> | }                                 |
> +-----------------------------------+
> ```
