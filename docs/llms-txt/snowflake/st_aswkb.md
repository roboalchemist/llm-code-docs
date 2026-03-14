# Source: https://docs.snowflake.com/en/sql-reference/functions/st_aswkb.md

Categories:
:   [Geospatial functions](../functions-geospatial.md)

# ST_ASWKB , ST_ASBINARY

Given a value of type [GEOGRAPHY](../data-types-geospatial.md) or [GEOMETRY](../data-types-geospatial.md), return the
binary representation of that value in
[WKB (well-known binary)](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry#Well-known_binary) format.

See also:
:   [ST_ASEWKB](st_asewkb.md)

## Syntax

Use one of the following:

```sqlsyntax
ST_ASWKB( <geography_or_geometry_expression> )

ST_ASBINARY( <geography_or_geometry_expression> )
```

## Arguments

`geography_or_geometry_expression`
:   The argument must be an expression of type GEOGRAPHY or GEOMETRY.

## Returns

A value of type BINARY.

## Usage notes

* ST_ASBINARY is an alias for ST_ASWKB.
* To return the output in EWKB format, use [ST_ASEWKB](st_asewkb.md) instead.

## Examples

### GEOGRAPHY examples

The following example demonstrates the ST_ASWKB function. For the WKB output, it is assumed that the [BINARY_OUTPUT_FORMAT](../parameters.md)
parameter is set to `HEX` (the default value for the parameter).

> ```sqlexample
> create table geospatial_table (id INTEGER, g GEOGRAPHY);
> insert into geospatial_table values
>     (1, 'POINT(-122.35 37.55)'), (2, 'LINESTRING(-124.20 42.00, -120.01 41.99)');
> ```
>
> ```sqlexample
> select st_aswkb(g)
>     from geospatial_table
>     order by id;
> +------------------------------------------------------------------------------------+
> | ST_ASWKB(G)                                                                        |
> |------------------------------------------------------------------------------------|
> | 01010000006666666666965EC06666666666C64240                                         |
> | 010200000002000000CDCCCCCCCC0C5FC00000000000004540713D0AD7A3005EC01F85EB51B8FE4440 |
> +------------------------------------------------------------------------------------+
> ```

### GEOMETRY examples

The example below demonstrates how to use the ST_ASEWKB function. The example returns the EWKB representations of two geometries.

> ```sqlexample
> CREATE OR REPLACE TABLE geometry_table (g GEOMETRY);
> INSERT INTO geometry_table VALUES
>   ('POINT(-122.35 37.55)'), ('LINESTRING(0.75 0.75, -10 20)');
>
> SELECT ST_ASWKB(g) FROM geometry_table;
> ```
>
> ```none
> +------------------------------------------------------------------------------------+
> | ST_ASWKB(G)                                                                        |
> |------------------------------------------------------------------------------------|
> | 01010000006666666666965EC06666666666C64240                                         |
> | 010200000002000000000000000000E83F000000000000E83F00000000000024C00000000000003440 |
> +------------------------------------------------------------------------------------+
> ```
