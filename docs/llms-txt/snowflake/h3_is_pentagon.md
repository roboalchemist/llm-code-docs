# Source: https://docs.snowflake.com/en/sql-reference/functions/h3_is_pentagon.md

Categories:
:   [Geospatial functions](../functions-geospatial.md)

# H3_IS_PENTAGON

Returns TRUE if the boundary of an [H3](../data-types-geospatial.md) cell represents a pentagon.

## Syntax

```sqlsyntax
H3_IS_PENTAGON( <cell_id> )
```

## Arguments

`cell_id`
:   An INTEGER value that represents the H3 cell ID ([index](https://h3geo.org/docs/core-library/h3Indexing)), or a VARCHAR value that represents the cell ID
    in hexadecimal format.

## Returns

Returns a BOOLEAN or NULL.

* The value is TRUE if the input represents a pentagon. Otherwise, returns FALSE.
* If the input is NULL, returns NULL without reporting an error.

## Examples

The following example specifies an integer that does not represent a pentagon.

```sqlexample
SELECT H3_IS_PENTAGON(613036919424548863);
```

```output
+------------------------------------+
| H3_IS_PENTAGON(613036919424548863) |
|------------------------------------|
| False                              |
+------------------------------------+
```

The following example specifies a hexadecimal string that represents a pentagon.

```sqlexample
SELECT H3_IS_PENTAGON('804dfffffffffff');
```

```output
+-----------------------------------+
| H3_IS_PENTAGON('804DFFFFFFFFFFF') |
|-----------------------------------|
| True                              |
+-----------------------------------+
```
