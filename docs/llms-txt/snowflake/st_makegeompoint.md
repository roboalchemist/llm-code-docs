# Source: https://docs.snowflake.com/en/sql-reference/functions/st_makegeompoint.md

Categories:
:   [Geospatial functions](../functions-geospatial.md)

# ST_MAKEGEOMPOINT , ST_GEOMPOINT

Constructs a [GEOMETRY](../data-types-geospatial.md) object that represents a Point with the specified longitude and latitude.

See also:
:   [TO_GEOMETRY](to_geometry.md)

## Syntax

```sqlsyntax
ST_MAKEGEOMPOINT( <longitude> , <latitude> )
```

## Arguments

`longitude`
:   A REAL that represents the longitude.

`latitude`
:   A REAL that represents the latitude.

## Returns

The function returns a value of type GEOMETRY.

## Usage notes

* ST_GEOMPOINT is an alias for ST_MAKEGEOMPOINT.

## Examples

For examples, see [Examples comparing the GEOGRAPHY and GEOMETRY data types](../data-types-geospatial.md). The examples use the
ST_GEOMPOINT alias.
