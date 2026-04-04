# Source: https://docs.snowflake.com/en/sql-reference/collation.md

# Source: https://docs.snowflake.com/en/sql-reference/functions/collation.md

Categories:
:   [String & binary functions](../functions-string.md)

# COLLATION

Returns the collation specification of the expression.

## Syntax

```sqlsyntax
COLLATION(<expression>)
```

## Arguments

`expression`
:   The expression for which you want to know the collation specification.
    Typically, this is a column name.

## Returns

Returns a VARCHAR value that contains the collation specification of the expression.

## Examples

This example shows how to get the collation specification of a specified column.

First, create the table and insert data:

```sqlexample
CREATE OR REPLACE TABLE collation1 (v VARCHAR COLLATE 'es');
INSERT INTO collation1 (v) VALUES ('ñ');
```

Second, show the collation of the column:

```sqlexample
SELECT COLLATION(v)
  FROM collation1;
```

```output
+--------------+
| COLLATION(V) |
|--------------|
| es           |
+--------------+
```
