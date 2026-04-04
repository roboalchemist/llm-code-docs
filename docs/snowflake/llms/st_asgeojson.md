# Source: https://docs.snowflake.com/en/sql-reference/functions/st_asgeojson.md

Categories:
:   [Geospatial functions](../functions-geospatial.md)

# ST_ASGEOJSON

Given a value of type [GEOGRAPHY](../data-types-geospatial.md) or [GEOMETRY](../data-types-geospatial.md), return the
[GeoJSON](../data-types-geospatial.md) representation of that value.

## Syntax

```sqlsyntax
ST_ASGEOJSON( <geography_or_geometry_expression> )
```

## Arguments

`geography_or_geometry_expression`
:   The argument must be an expression of type GEOGRAPHY or GEOMETRY.

## Returns

An OBJECT in [GeoJSON](../data-types-geospatial.md) format.

## Usage notes

For GEOMETRY objects:

* The returned GEOMETRY object uses the same coordinate system as the input GEOMETRY object.

  Note that the GeoJSON specification requires that geometry be in the WGS84 coordinate system (SRID = 4326). However, the
  ST_ASGEOJSON function does not enforce this.
* The function does not add the SRID or any other CRS information to the output.

## Examples

### GEOGRAPHY examples

The following example demonstrates the ST_ASGEOJSON function:

> ```sqlexample
> create table geospatial_table (id INTEGER, g GEOGRAPHY);
> insert into geospatial_table values
>     (1, 'POINT(-122.35 37.55)'), (2, 'LINESTRING(-124.20 42.00, -120.01 41.99)');
> ```
>
> ```sqlexample
> select st_asgeojson(g)
>     from geospatial_table
>     order by id;
> +------------------------+
> | ST_ASGEOJSON(G)        |
> |------------------------|
> | {                      |
> |   "coordinates": [     |
> |     -122.35,           |
> |     37.55              |
> |   ],                   |
> |   "type": "Point"      |
> | }                      |
> | {                      |
> |   "coordinates": [     |
> |     [                  |
> |       -124.2,          |
> |       42               |
> |     ],                 |
> |     [                  |
> |       -120.01,         |
> |       41.99            |
> |     ]                  |
> |   ],                   |
> |   "type": "LineString" |
> | }                      |
> +------------------------+
> ```
>
> Casting the VARIANT output to VARCHAR results in the following:
>
> ```sqlexample
> select st_asgeojson(g)::varchar
>     from geospatial_table
>     order by id;
> +-------------------------------------------------------------------+
> | ST_ASGEOJSON(G)::VARCHAR                                          |
> |-------------------------------------------------------------------|
> | {"coordinates":[-122.35,37.55],"type":"Point"}                    |
> | {"coordinates":[[-124.2,42],[-120.01,41.99]],"type":"LineString"} |
> +-------------------------------------------------------------------+
> ```

### GEOMETRY examples

The following example demonstrates the ST_ASGEOJSON function with a GEOMETRY object as input:

> ```sqlexample
> SELECT ST_ASGEOJSON(TO_GEOMETRY('SRID=4326;LINESTRING(389866 5819003, 390000 5830000)')) AS geojson;
> ```
>
> ```none
> +------------------------+
> | GEOJSON                |
> |------------------------|
> |{                       |
> |  "coordinates": [      |
> |    [                   |
> |      389866,           |
> |      5819003           |
> |    ],                  |
> |    [                   |
> |      390000,           |
> |      5830000           |
> |    ]                   |
> |  ],                    |
> |  "type": "LineString"  |
> |}                       |
> +------------------------+
> ```
