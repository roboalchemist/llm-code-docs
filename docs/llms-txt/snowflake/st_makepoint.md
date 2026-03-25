# Source: https://docs.snowflake.com/en/sql-reference/functions/st_makepoint.md

Categories:
:   [Geospatial functions](../functions-geospatial.md)

# ST_MAKEPOINT , ST_POINT

Constructs a [GEOGRAPHY](../data-types-geospatial.md) object that represents a point with the specified longitude
and latitude.

See also:
:   [TO_GEOGRAPHY](to_geography.md)

## Syntax

```sqlsyntax
ST_MAKEPOINT( <longitude> , <latitude> )
```

## Arguments

`longitude`
:   A REAL that represents the longitude.

`latitude`
:   A REAL that represents the latitude.

## Returns

The function returns a value of type GEOGRAPHY.

## Usage notes

* ST_POINT is an alias for ST_MAKEPOINT.

## Examples

This shows a simple use of the ST_MAKEPOINT function:

> ```sqlexample
> SELECT ST_MAKEPOINT(37.5, 45.5);
> +--------------------------+
> | ST_MAKEPOINT(37.5, 45.5) |
> |--------------------------|
> | POINT(37.5 45.5)         |
> +--------------------------+
> ```
