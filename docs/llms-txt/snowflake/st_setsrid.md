# Source: https://docs.snowflake.com/en/sql-reference/functions/st_setsrid.md

Categories:
:   [Geospatial functions](../functions-geospatial.md)

# ST_SETSRID

Returns a [GEOMETRY](../data-types-geospatial.md) object that has its SRID (spatial reference system identifier) set to the
specified value.

Use this function to change the SRID without affecting the coordinates of the object. If you also need to
[change the coordinates to match the new SRS (spatial reference system)](../data-types-geospatial.md), use
[ST_TRANSFORM](st_transform.md) instead.

## Syntax

```sqlsyntax
ST_SETSRID( <geometry_expression> , <srid> )
```

## Arguments

`geometry_expression`
:   The argument must be an expression of type GEOMETRY.

`srid`
:   The SRID to set in the returned GEOMETRY object.

## Returns

The function returns a value of type GEOMETRY.

## Usage notes

## Examples

The following example creates and returns a GEOMETRY object that uses the SRID 4326:

> ```sqlexample
> ALTER SESSION SET GEOMETRY_OUTPUT_FORMAT='EWKT';
>
> SELECT ST_SETSRID(TO_GEOMETRY('POINT(13 51)'), 4326);
>
> +-----------------------------------------------+
> | ST_SETSRID(TO_GEOMETRY('POINT(13 51)'), 4326) |
> |-----------------------------------------------|
> | SRID=4326;POINT(13 51)                        |
> +-----------------------------------------------+
> ```
