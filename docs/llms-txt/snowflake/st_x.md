# Source: https://docs.snowflake.com/en/sql-reference/functions/st_x.md

Categories:
:   [Geospatial functions](../functions-geospatial.md)

# ST_X

Returns the longitude (X coordinate) of a Point represented by a [GEOGRAPHY](../data-types-geospatial.md) or
[GEOMETRY](../data-types-geospatial.md) object.

## Syntax

```sqlsyntax
ST_X( <geography_or_geometry_expression> )
```

## Arguments

`geography_or_geometry_expression`
:   The argument must be an expression of the type GEOGRAPHY or GEOMETRY and must contain a Point.

## Returns

Returns a REAL value.

## Usage notes

* Issues an error if the argument is not a Point.

## Examples

### GEOGRAPHY examples

This shows a simple use of the ST_X and ST_Y functions with VARCHAR data:

> ```sqlexample
> SELECT ST_X(ST_MAKEPOINT(37.5, 45.5)), ST_Y(ST_MAKEPOINT(37.5, 45.5));
> +--------------------------------+--------------------------------+
> | ST_X(ST_MAKEPOINT(37.5, 45.5)) | ST_Y(ST_MAKEPOINT(37.5, 45.5)) |
> |--------------------------------+--------------------------------|
> |                           37.5 |                           45.5 |
> +--------------------------------+--------------------------------+
> ```

This shows use of the ST_X and ST_Y functions with NULL values:

> ```sqlexample
> SELECT
>     ST_X(ST_MAKEPOINT(NULL, NULL)), ST_X(NULL),
>     ST_Y(ST_MAKEPOINT(NULL, NULL)), ST_Y(NULL)
>     ;
> +--------------------------------+------------+--------------------------------+------------+
> | ST_X(ST_MAKEPOINT(NULL, NULL)) | ST_X(NULL) | ST_Y(ST_MAKEPOINT(NULL, NULL)) | ST_Y(NULL) |
> |--------------------------------+------------+--------------------------------+------------|
> |                           NULL |       NULL |                           NULL |       NULL |
> +--------------------------------+------------+--------------------------------+------------+
> ```
