# Source: https://docs.snowflake.com/en/sql-reference/functions/h3_cell_to_boundary.md

Categories:
:   [Geospatial functions](../functions-geospatial.md)

# H3_CELL_TO_BOUNDARY

Returns the [GEOGRAPHY](../data-types-geospatial.md) object representing the boundary of an
[H3](../data-types-geospatial.md) cell.

## Syntax

```sqlsyntax
H3_CELL_TO_BOUNDARY( <cell_id> )
```

## Arguments

`cell_id`
:   An INTEGER that represents the H3 cell ID ([index](https://h3geo.org/docs/core-library/h3Indexing)), or a VARCHAR that represents the cell ID in hexadecimal format.

## Returns

Returns a GEOGRAPHY object that represents the boundary of the H3 cell with the specified ID.

## Examples

The following example returns the GEOGRAPHY object that represents the boundary of the H3 cell containing the Brandenburg Gate.
The example specifies the H3 cell ID as an INTEGER value.

```sqlexample
SELECT H3_CELL_TO_BOUNDARY(613036919424548863);
```

```output
+-----------------------------------------+
| H3_CELL_TO_BOUNDARY(613036919424548863) |
|-----------------------------------------|
| {                                       |
|   "coordinates": [                      |
|     [                                   |
|       [                                 |
|         1.337146281884266e+01,          |
|         5.251934565725256e+01           |
|       ],                                |
|       [                                 |
|         1.336924966147084e+01,          |
|         5.251510220405509e+01           |
|       ],                                |
|       [                                 |
|         1.337455447449988e+01,          |
|         5.251214028989955e+01           |
|       ],                                |
|       [                                 |
|         1.338207263166664e+01,          |
|         5.251342164903257e+01           |
|       ],                                |
|       [                                 |
|         1.338428664751681e+01,          |
|         5.251766506194694e+01           |
|       ],                                |
|       [                                 |
|         1.337898164779325e+01,          |
|         5.252062715603375e+01           |
|       ],                                |
|       [                                 |
|         1.337146281884266e+01,          |
|         5.251934565725256e+01           |
|       ]                                 |
|     ]                                   |
|   ],                                    |
|   "type": "Polygon"                     |
| }                                       |
+-----------------------------------------+
```

The following example specifies the hexadecimal value of H3 cell ID as a VARCHAR to return the same coordinates as the previous
example.

```sqlexample
SELECT H3_CELL_TO_BOUNDARY('881F1D4887FFFFF');
```

```output
+----------------------------------------+
| H3_CELL_TO_BOUNDARY('881F1D4887FFFFF') |
|----------------------------------------|
| {                                      |
|   "coordinates": [                     |
|     [                                  |
|       [                                |
|         1.337146281884266e+01,         |
|         5.251934565725256e+01          |
|       ],                               |
|       [                                |
|         1.336924966147084e+01,         |
|         5.251510220405509e+01          |
|       ],                               |
|       [                                |
|         1.337455447449988e+01,         |
|         5.251214028989955e+01          |
|       ],                               |
|       [                                |
|         1.338207263166664e+01,         |
|         5.251342164903257e+01          |
|       ],                               |
|       [                                |
|         1.338428664751681e+01,         |
|         5.251766506194694e+01          |
|       ],                               |
|       [                                |
|         1.337898164779325e+01,         |
|         5.252062715603375e+01          |
|       ],                               |
|       [                                |
|         1.337146281884266e+01,         |
|         5.251934565725256e+01          |
|       ]                                |
|     ]                                  |
|   ],                                   |
|   "type": "Polygon"                    |
| }                                      |
+----------------------------------------+
```
