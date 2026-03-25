# Source: https://docs.snowflake.com/en/sql-reference/functions/st_srid.md

Categories:
:   [Geospatial functions](../functions-geospatial.md)

# ST_SRID

Returns the SRID (spatial reference system identifier) of a [GEOGRAPHY](../data-types-geospatial.md) or
[GEOMETRY](../data-types-geospatial.md) object.

Currently, for any value of the GEOGRAPHY type, only SRID 4326 is supported and is returned.

## Syntax

```sqlsyntax
ST_SRID( <geography_or_geometry_expression> )
```

## Arguments

`geography_or_geometry_expression`
:   The argument must be an expression of type GEOGRAPHY or GEOMETRY.

## Returns

Returns a value of type NUMBER(4,0).

## Usage notes

* Returns NULL if the input is NULL.

## Examples

### GEOGRAPHY examples

This shows a simple use of the ST_SRID function:

> ```sqlexample
> SELECT ST_SRID(ST_MAKEPOINT(37.5, 45.5));
> +-----------------------------------+
> | ST_SRID(ST_MAKEPOINT(37.5, 45.5)) |
> |-----------------------------------|
> |                              4326 |
> +-----------------------------------+
> ```

This shows use of the ST_SRID function with NULL values:

> ```sqlexample
> SELECT ST_SRID(ST_MAKEPOINT(NULL, NULL)), ST_SRID(NULL);
> +-----------------------------------+---------------+
> | ST_SRID(ST_MAKEPOINT(NULL, NULL)) | ST_SRID(NULL) |
> |-----------------------------------+---------------|
> |                              NULL |          NULL |
> +-----------------------------------+---------------+
> ```
