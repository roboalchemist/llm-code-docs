# Source: https://docs.snowflake.com/en/sql-reference/functions/st_asewkb.md

Categories:
:   [Geospatial functions](../functions-geospatial.md)

# ST_ASEWKB

Given a value of type [GEOGRAPHY](../data-types-geospatial.md) or [GEOMETRY](../data-types-geospatial.md), return the
binary representation of that value in
[EWKB (extended well-known binary)](../data-types-geospatial.md) format.

See also:
:   [ST_ASWKB](st_aswkb.md)

## Syntax

```sqlsyntax
ST_ASEWKB( <geography_or_geometry_expression> )
```

## Arguments

`geography_or_geometry_expression`
:   The argument must be an expression of type GEOGRAPHY or GEOMETRY.

## Returns

A value of type BINARY.

## Usage notes

* For GEOGRAPHY objects, the SRID in the return value is always 4326. See
  the [note on EWKT handling](../data-types-geospatial.md).
* To return the output in WKB format, use [ST_ASWKB](st_aswkb.md) instead.

## Examples

### GEOGRAPHY examples

The following example demonstrates the ST_ASEWKB function. For the EWKB output, it is assumed that the [BINARY_OUTPUT_FORMAT](../parameters.md)
parameter is set to `HEX` (the default value for the parameter).

> ```sqlexample
> create table geospatial_table (id INTEGER, g GEOGRAPHY);
> insert into geospatial_table values
>     (1, 'POINT(-122.35 37.55)'), (2, 'LINESTRING(-124.20 42.00, -120.01 41.99)');
> ```
>
> ```sqlexample
> select st_asewkb(g)
>     from geospatial_table
>     order by id;
> +--------------------------------------------------------------------------------------------+
> | ST_ASEWKB(G)                                                                               |
> |--------------------------------------------------------------------------------------------|
> | 0101000020E61000006666666666965EC06666666666C64240                                         |
> | 0102000020E610000002000000CDCCCCCCCC0C5FC00000000000004540713D0AD7A3005EC01F85EB51B8FE4440 |
> +--------------------------------------------------------------------------------------------+
> ```

### GEOMETRY examples

The example below demonstrates how to use the ST_ASEWKB function. The example returns the EWKB representations of two geometries
that have different SRIDs.

> ```sqlexample
> CREATE OR REPLACE TABLE geometry_table (g GEOMETRY);
> INSERT INTO geometry_table VALUES
>   ('SRID=4326;POINT(-122.35 37.55)'),
>   ('SRID=0;LINESTRING(0.75 0.75, -10 20)');
>
> SELECT ST_ASEWKB(g) FROM geometry_table;
> ```
>
> ```none
> +--------------------------------------------------------------------------------------------+
> | ST_ASEWKB(G)                                                                               |
> |--------------------------------------------------------------------------------------------|
> | 0101000020E61000006666666666965EC06666666666C64240                                         |
> | 01020000200000000002000000000000000000E83F000000000000E83F00000000000024C00000000000003440 |
> +--------------------------------------------------------------------------------------------+
> ```
