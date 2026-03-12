# Source: https://docs.snowflake.com/en/sql-reference/functions/to_geography.md

Categories:
:   [Geospatial functions](../functions-geospatial.md), [Conversion functions](../functions-conversion.md)

# TO_GEOGRAPHY

Parses an input and returns a value of type [GEOGRAPHY](../data-types-geospatial.md).

See also:
:   [TRY_TO_GEOGRAPHY](try_to_geography.md) , [ST_GEOGRAPHYFROMWKB](st_geographyfromwkb.md) , [ST_GEOGRAPHYFROMWKT](st_geographyfromwkt.md)

## Syntax

Use one of the following:

```sqlsyntax
TO_GEOGRAPHY( <varchar_expression> [ , <allow_invalid> ] )

TO_GEOGRAPHY( <binary_expression> [ , <allow_invalid> ] )

TO_GEOGRAPHY( <variant_expression> [ , <allow_invalid> ] )

TO_GEOGRAPHY( <geometry_expression> [ , <allow_invalid> ] )
```

## Arguments

**Required:**

`varchar_expression`
:   The argument must be a string expression that represents a valid geometric object in one of the following formats:

    * WKT (well-known text).
    * WKB (well-known binary) in hexadecimal format (without a leading `0x`).
    * EWKT (extended well-known text).
    * EWKB (extended well-known binary) in hexadecimal format (without a leading `0x`).
    * GeoJSON.

`binary_expression`
:   The argument must be a binary expression in WKB or EWKB format.

`variant_expression`
:   The argument must be an OBJECT in GeoJSON format.

`geometry_expression`
:   The argument must be an expression of type GEOMETRY with the SRID 4326.

**Optional:**

`allow_invalid`
:   If TRUE, specifies that the function returns a GEOGRAPHY or GEOMETRY object, even when the input shape isn’t valid and
    can’t be repaired. For more information, see [Specifying how invalid geospatial shapes are handled](../data-types-geospatial.md).

## Returns

The function returns a value of type [GEOGRAPHY](../data-types-geospatial.md).

## Usage notes

* Issues an error if the input cannot be parsed as one of the supported formats (WKT, WKB, EWKT, EWKB, GeoJSON).
* Issues an error if the input format is EWKT or EWKB and the SRID is not 4326.
  See the [note on EWKT and EWKB handling](../data-types-geospatial.md).
* To construct a GEOGRAPHY object from WKT or EWKT input, you can also use [ST_GEOGRAPHYFROMWKT](st_geographyfromwkt.md).
* To construct a GEOGRAPHY object from WKB or EWKB input, you can also use [ST_GEOGRAPHYFROMWKB](st_geographyfromwkb.md).

* For the coordinates in WKT, EWKT, and GeoJSON, longitude appears before latitude (for example, `POINT(lon lat)`).

## Examples

This shows a simple use of the TO_GEOGRAPHY function with VARCHAR data:

> ```sqlexample
> select TO_GEOGRAPHY('POINT(-122.35 37.55)');
> ```
>
> ```output
> +--------------------------------------+
> | TO_GEOGRAPHY('POINT(-122.35 37.55)') |
> |--------------------------------------|
> | POINT(-122.35 37.55)                 |
> +--------------------------------------+
> ```

The following example returns the GEOGRAPHY object for a geospatial object with a Z coordinate described in WKT format:

> ```sqlexample
> select TO_GEOGRAPHY('POINTZ(-122.35 37.55 30)');
> ```
>
> ```output
> +------------------------------------------+
> | TO_GEOGRAPHY('POINTZ(-122.35 37.55 30)') |
> |------------------------------------------|
> | POINTZ(-122.35 37.55 30)                 |
> +------------------------------------------+
> ```
