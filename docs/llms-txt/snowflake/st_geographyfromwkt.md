# Source: https://docs.snowflake.com/en/sql-reference/functions/st_geographyfromwkt.md

Categories:
:   [Geospatial functions](../functions-geospatial.md), [Conversion functions](../functions-conversion.md)

# ST_GEOGRAPHYFROMWKT

Parses a
[WKT (well-known text)](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry) or
[EWKT (extended well-known text)](../data-types-geospatial.md) input and returns a value of type
[GEOGRAPHY](../data-types-geospatial.md).

Aliases:
:   ST_GEOGFROMWKT , ST_GEOGRAPHYFROMEWKT , ST_GEOGFROMEWKT , ST_GEOGRAPHYFROMTEXT , ST_GEOGFROMTEXT

See also:
:   [TO_GEOGRAPHY](to_geography.md)

## Syntax

```sqlsyntax
ST_GEOGRAPHYFROMWKT( <varchar_expression> [ , <allow_invalid> ] )

ST_GEOGFROMWKT( <varchar_expression> [ , <allow_invalid> ] )

ST_GEOGRAPHYFROMEWKT( <varchar_expression> [ , <allow_invalid> ] )

ST_GEOGFROMEWKT( <varchar_expression> [ , <allow_invalid> ] )

ST_GEOGRAPHYFROMTEXT( <varchar_expression> [ , <allow_invalid> ] )

ST_GEOGFROMTEXT( <varchar_expression> [ , <allow_invalid> ] )
```

## Arguments

**Required:**

`varchar_expression`
:   The argument must be a string expression in WKT or EWKT that represents a valid geospatial object.

**Optional:**

`allow_invalid`
:   If TRUE, specifies that the function returns a GEOGRAPHY or GEOMETRY object, even when the input shape isn’t valid and
    can’t be repaired. For more information, see [Specifying how invalid geospatial shapes are handled](../data-types-geospatial.md).

## Returns

The function returns a value of type [GEOGRAPHY](../data-types-geospatial.md).

## Usage notes

* Issues an error if the input cannot be parsed as WKT or EWKT.
* Issues an error if the input format is EWKT and the SRID is not 4326.
  See the [note on EWKT and EWKB handling](../data-types-geospatial.md).

* For the coordinates in WKT, EWKT, and GeoJSON, longitude appears before latitude (for example, `POINT(lon lat)`).

## Examples

The following example returns the GEOGRAPHY object for a geospatial object described in WKT format:

> ```sqlexample
> -- Set the output format to WKT
> alter session set GEOGRAPHY_OUTPUT_FORMAT='WKT';
> ```
>
> ```sqlexample
> select ST_GEOGRAPHYFROMWKT('POINT(-122.35 37.55)');
> ```
>
> ```output
> +---------------------------------------------+
> | ST_GEOGRAPHYFROMWKT('POINT(-122.35 37.55)') |
> |---------------------------------------------|
> | POINT(-122.35 37.55)                        |
> +---------------------------------------------+
> ```

The following example returns the GEOGRAPHY object for a geospatial object with a Z coordinate described in WKT format:

> ```sqlexample
> -- Set the output format to WKT
> alter session set GEOGRAPHY_OUTPUT_FORMAT='WKT';
> ```
>
> ```sqlexample
> select ST_GEOGRAPHYFROMWKT('POINTZ(-122.35 37.55 30)');
> ```
>
> ```output
> +-------------------------------------------------+
> | ST_GEOGRAPHYFROMWKT('POINTZ(-122.35 37.55 30)') |
> |-------------------------------------------------|
> | POINTZ(-122.35 37.55 30)                        |
> +-------------------------------------------------+
> ```

The following example returns the GEOGRAPHY object for a geospatial object described in EWKT format:

> ```sqlexample
> -- Set the output format to EWKT
> alter session set GEOGRAPHY_OUTPUT_FORMAT='EWKT';
> ```
>
> ```sqlexample
> select ST_GEOGRAPHYFROMEWKT('SRID=4326;POINT(-122.35 37.55)');
> ```
>
> ```output
> +--------------------------------------------------------+
> | ST_GEOGRAPHYFROMEWKT('SRID=4326;POINT(-122.35 37.55)') |
> |--------------------------------------------------------|
> | SRID=4326;POINT(-122.35 37.55)                         |
> +--------------------------------------------------------+
> ```
