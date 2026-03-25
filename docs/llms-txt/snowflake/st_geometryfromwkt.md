# Source: https://docs.snowflake.com/en/sql-reference/functions/st_geometryfromwkt.md

Categories:
:   [Geospatial functions](../functions-geospatial.md), [Conversion functions](../functions-conversion.md)

# ST_GEOMETRYFROMWKT

Parses a
[WKT (well-known text)](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry) or EWKT (extended well-known
text) input and returns a value of type [GEOMETRY](../data-types-geospatial.md).

Aliases:
:   ST_GEOMFROMWKT , ST_GEOMETRYFROMEWKT , ST_GEOMFROMEWKT , ST_GEOMETRYFROMTEXT , ST_GEOMFROMTEXT

See also:
:   [TO_GEOMETRY](to_geometry.md)

## Syntax

```sqlsyntax
ST_GEOMETRYFROMWKT( <varchar_expression> [ , <srid> ] [ , <allow_invalid> ] )

ST_GEOMFROMWKT( <varchar_expression> [ , <srid> ] [ , <allow_invalid> ] )

ST_GEOMETRYFROMEWKT( <varchar_expression> [ , <srid> ] [ , <allow_invalid> ] )

ST_GEOMFROMEWKT( <varchar_expression> [ , <srid> ] [ , <allow_invalid> ] )

ST_GEOMETRYFROMTEXT( <varchar_expression> [ , <srid> ] [ , <allow_invalid> ] )

ST_GEOMFROMTEXT( <varchar_expression> [ , <srid> ] [ , <allow_invalid> ] )
```

## Arguments

**Required:**

`varchar_expression`
:   The argument must be a string expression in WKT or EWKT that represents a valid geospatial object.

**Optional:**

`srid`
:   The integer value of the SRID to use.

`allow_invalid`
:   If TRUE, specifies that the function returns a GEOGRAPHY or GEOMETRY object, even when the input shape isn’t valid and
    can’t be repaired. For more information, see [Specifying how invalid geospatial shapes are handled](../data-types-geospatial.md).

## Returns

The function returns a value of type [GEOMETRY](../data-types-geospatial.md).

## Usage notes

* Issues an error if the input cannot be parsed as WKT or EWKT.
* For WKT input, if the `srid` argument is not specified, the resulting GEOMETRY object has the SRID set to 0.

## Examples

The following example returns the GEOMETRY object for a geospatial object described in EWKT format:

```sqlexample
-- Set the output format to EWKT
ALTER SESSION SET GEOMETRY_OUTPUT_FORMAT='EWKT';

SELECT ST_GEOMETRYFROMEWKT('SRID=32633;POINT(389866.35 5819003.03)');
```

```output
+---------------------------------------------------------------+
| ST_GEOMETRYFROMEWKT('SRID=32633;POINT(389866.35 5819003.03)') |
|---------------------------------------------------------------|
| SRID=32633;POINT(389866.35 5819003.03)                        |
+---------------------------------------------------------------+
```

The following example returns the GEOMETRY object for a geospatial object with a Z coordinate described in EWKT format:

```sqlexample
-- Set the output format to EWKT
ALTER SESSION SET GEOMETRY_OUTPUT_FORMAT='EWKT';

SELECT ST_GEOMETRYFROMEWKT('SRID=32633;POINTZ(389866.35 5819003.03 30)');
```

```output
+-------------------------------------------------------------------+
| ST_GEOMETRYFROMEWKT('SRID=32633;POINTZ(389866.35 5819003.03 30)') |
|-------------------------------------------------------------------|
| SRID=32633;POINTZ(389866.35 5819003.03 30)                        |
+-------------------------------------------------------------------+
```

In the next example, the input is in WKT format, and the function call specifies the SRID to use:

```sqlexample
-- Set the output format to EWKT
ALTER SESSION SET GEOMETRY_OUTPUT_FORMAT='EWKT';

SELECT ST_GEOMETRYFROMWKT('POINT(389866.35 5819003.03)', 4326);
```

```output
+----------------------------------------------------------+
| ST_GEOMETRYFROMWKT('POINT(389866.35 5819003.03)', 4326)  |
|----------------------------------------------------------|
| SRID=4326;POINT(389866.35 5819003.03)                    |
+----------------------------------------------------------+
```
