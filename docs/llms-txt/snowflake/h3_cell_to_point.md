# Source: https://docs.snowflake.com/en/sql-reference/functions/h3_cell_to_point.md

Categories:
:   [Geospatial functions](../functions-geospatial.md)

# H3_CELL_TO_POINT

Returns the [GEOGRAPHY](../data-types-geospatial.md) object representing the Point that is the centroid of an
[H3](../data-types-geospatial.md) cell.

See also:
:   [H3_POINT_TO_CELL](h3_point_to_cell.md) , [H3_POINT_TO_CELL_STRING](h3_point_to_cell_string.md)

## Syntax

```sqlsyntax
H3_CELL_TO_POINT( <cell_id> )
```

## Arguments

`cell_id`
:   An INTEGER that represents the H3 cell ID ([index](https://h3geo.org/docs/core-library/h3Indexing)), or a VARCHAR that represents the cell ID in hexadecimal format.

## Returns

Returns a GEOGRAPHY object for the Point that represents the centroid of the H3 cell with the specified ID.

## Examples

The following example returns the GEOGRAPHY object for the Point that represents the centroid of the H3 cell containing the
Brandenburg Gate. The example specifies the H3 cell ID as an INTEGER value.

```sqlexample
SELECT H3_CELL_TO_POINT(613036919424548863);
```

```output
+--------------------------------------+
| H3_CELL_TO_POINT(613036919424548863) |
|--------------------------------------|
| {                                    |
|   "coordinates": [                   |
|     1.337676791184706e+01,           |
|     5.251638386722465e+01            |
|   ],                                 |
|   "type": "Point"                    |
| }                                    |
+--------------------------------------+
```

The following example specifies the hexadecimal value of the H3 cell ID as a VARCHAR to return the same coordinates as the previous
example.

```sqlexample
SELECT H3_CELL_TO_POINT('881F1D4887FFFFF');
```

```output
+-------------------------------------+
| H3_CELL_TO_POINT('881F1D4887FFFFF') |
|-------------------------------------|
| {                                   |
|   "coordinates": [                  |
|     1.337676791184706e+01,          |
|     5.251638386722465e+01           |
|   ],                                |
|   "type": "Point"                   |
| }                                   |
+-------------------------------------+
```
