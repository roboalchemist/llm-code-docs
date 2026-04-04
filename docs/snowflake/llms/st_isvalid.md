# Source: https://docs.snowflake.com/en/sql-reference/functions/st_isvalid.md

Categories:
:   [Geospatial functions](../functions-geospatial.md)

# ST_ISVALID

Returns TRUE if the specified [GEOGRAPHY](../data-types-geospatial.md) or
[GEOMETRY](../data-types-geospatial.md) object represents a
[valid shape](../data-types-geospatial.md). Examples of
invalid shapes include shapes with self-intersections and spikes.

## Syntax

```sqlsyntax
ST_ISVALID( <geography_or_geometry_expression> )
```

## Arguments

`geography_or_geometry_expression`
:   The argument must be an expression of type GEOGRAPHY or GEOMETRY.

## Returns

Returns a BOOLEAN value.

## Usage notes

* ST_ISVALID only checks for the validity of a shape. It doesn’t modify data. When constructing objects from
  spatial formats (such as WKT, WKB, EWKT, EWKB, or GeoJSON), conversion functions (for example, [TO_GEOGRAPHY](to_geography.md),
  [TO_GEOMETRY](to_geometry.md), [ST_GEOGRAPHYFROMWKT](st_geographyfromwkt.md), or [ST_GEOMETRYFROMWKT](st_geometryfromwkt.md)) parse input and by default
  attempt to validate or repair shapes. If a conversion function can’t repair a shape, it returns
  an error unless you accept invalid shapes.
* To ingest data that might be invalid (for example, data that you plan to correct later), specify TRUE for the
  additional `allow_invalid` argument when you call the conversion function to allow an invalid shape.
  You can then use the ST_ISVALID function to flag invalid rows in a table.
* Some geospatial functions might return an error or unusable results when given invalid shapes. Use the
  ST_ISVALID function to check validity. You can correct invalid shapes before performing spatial analytics.
* When shapes are invalid, simple corrections include buffering with a small positive or negative distance
  (for example, to remove tiny spikes or resolve self-intersections) and then rechecking validity using the
  ST_ISVALID function.

## Examples

The following examples use the ST_ISVALID function.

Determine whether a polygon is a valid shape:

```sqlexample
SELECT ST_ISVALID(
    TO_GEOGRAPHY('POLYGON((-93.086 37.557,-86.699 37.497,-93.198 35.123,-93.086 37.557))')
  ) AS is_valid;
```

```output
+----------+
| IS_VALID |
|----------|
| True     |
+----------+
```

```sqlexample
SELECT ST_ISVALID(
    TO_GEOGRAPHY( 'POLYGON((-92.799 37.601,-88.240 37.617,-92.733 36.198,-88.305 36.171,-92.799 37.601))', TRUE)
  ) AS is_valid;
```

```output
+----------+
| IS_VALID |
|----------|
| False    |
+----------+
```

Correct an invalid shape by using the [ST_BUFFER](st_buffer.md) function to add small buffer:

```sqlexample
WITH g AS (
  SELECT TO_GEOMETRY('POLYGON((0 0, 2 2, 2 0, 0 2, 0 0))', TRUE) AS geom
)
SELECT ST_ISVALID(geom) AS is_valid_before_buffer,
  ST_ISVALID(ST_BUFFER(geom, -0.001)) AS is_valid_after_buffer
  FROM g;
```

```output
+------------------------+-----------------------+
| IS_VALID_BEFORE_BUFFER | IS_VALID_AFTER_BUFFER |
|------------------------+-----------------------|
| False                  | True                  |
+------------------------+-----------------------+
```
