# Source: https://docs.snowflake.com/en/sql-reference/functions/haversine.md

Categories:
:   [Geospatial functions](../functions-geospatial.md)

# HAVERSINE

Calculates the great-circle distance in kilometers between two points on the
Earth’s surface, using the [Haversine formula](https://en.wikipedia.org/wiki/Haversine_formula).
The two points are specified by their latitude and longitude in decimal degrees.

> **Note:**
>
> Snowflake recommends using the [ST_DISTANCE](st_distance.md) function instead of the HAVERSINE function.
> The ST_DISTANCE function performs the calculation using values of geospatial types, which
> enables you to store geospatial data and use the [geospatial functions](../functions-geospatial.md)
> on the data. In addition, join predicates that use the ST_DISTANCE function perform better than join predicates
> that use the HAVERSINE function.

## Syntax

```sqlsyntax
HAVERSINE( <lat1>, <lon1>, <lat2>, <lon2> )
```

## Arguments

`lat1`
:   The latitude of the first point in decimal degrees.

`lon1`
:   The longitude of the first point in decimal degrees.

`lat2`
:   The latitude of the second point in decimal degrees.

`lon2`
:   The longitude of the second point in decimal degrees.

## Returns

This function returns a value of type FLOAT.

## Examples

The following example returns the geospatial distance in kilometers between New York and Los Angeles:

```sqlexample
SELECT HAVERSINE(
    40.7127,
    -74.0059,
    34.0500,
    -118.2500
  ) AS distance_in_kilometers;
```

```output
+------------------------+
| DISTANCE_IN_KILOMETERS |
|------------------------|
|         3936.385096389 |
+------------------------+
```

The following example is the same as the previous example, but it returns the geospatial distance
in meters instead of kilometers by multiplying the result by 1000:

```sqlexample
SELECT HAVERSINE(
    40.7127,
    -74.0059,
    34.0500,
    -118.2500
  ) * 1000 AS distance_in_meters;
```

```output
+--------------------+
| DISTANCE_IN_METERS |
|--------------------|
|   3936385.09638929 |
+--------------------+
```
