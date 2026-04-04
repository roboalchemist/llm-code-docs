# Source: https://docs.snowflake.com/en/sql-reference/functions/st_geompointfromgeohash.md

Categories:
:   [Geospatial functions](../functions-geospatial.md)

# ST_GEOMPOINTFROMGEOHASH

Returns a [GEOMETRY](../data-types-geospatial.md) object for the point that represents center of a
[geohash](https://en.wikipedia.org/wiki/Geohash).

See also:
:   [ST_GEOHASH](st_geohash.md), [ST_GEOMFROMGEOHASH](st_geomfromgeohash.md)

## Syntax

```sqlsyntax
ST_GEOMPOINTFROMGEOHASH( <geohash> )
```

## Arguments

`geohash`
:   The argument must be a geohash.

## Returns

Returns a value of type [GEOMETRY](../data-types-geospatial.md) that represents the point that is the
center of the geohash.

## Examples

The following example returns the GEOMETRY object for the point at the center of a geohash:

```sqlexample
SELECT ST_GEOMPOINTFROMGEOHASH('9q9j8ue2v71y5zzy0s4q')
  AS geometry_center_point_of_geohash;
```

```output
+----------------------------------+
| GEOMETRY_CENTER_POINT_OF_GEOHASH |
|----------------------------------|
| {                                |
|   "coordinates": [               |
|     -1.223061000000001e+02,      |
|     3.755416199999996e+01        |
|   ],                             |
|   "type": "Point"                |
| }                                |
+----------------------------------+
```
