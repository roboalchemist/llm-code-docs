# Source: https://docs.snowflake.com/en/sql-reference/functions/contains.md

Categories:
:   [String & binary functions](../functions-string.md) (Matching/Comparison)

# CONTAINS

Returns true if `expr1` contains `expr2`. Both expressions must be text or binary expressions.

> **Tip:**
>
> You can use the search optimization service to improve the performance of queries that call this function.
> For details, see [Search optimization service](../../user-guide/search-optimization-service.md).

## Syntax

```sqlsyntax
CONTAINS( <expr1> , <expr2> )
```

## Arguments

`expr1`
:   The string to search in.

`expr2`
:   The string to search for.

## Returns

Returns a BOOLEAN or NULL:

* Returns TRUE if `expr2` is found inside `expr1`.
* Returns FALSE if `expr2` is not found inside `expr1`.
* Returns NULL if either input expression is NULL.

## Usage notes

For comparisons that match a string against more than one specified pattern, you can use the following functions:

* [ILIKE ANY](ilike_any.md)
* [LIKE ALL](like_all.md)
* [LIKE ANY](like_any.md)

## Collation details

The [collation specifications](../collation.md) of all input arguments must be compatible.

This function does not support the following collation specifications:

* `pi` (punctuation-insensitive).
* `cs-ai` (case-sensitive, accent-insensitive).

## Examples

These examples use the CONTAINS function.

### Determine whether column values contain a string

Create a table with a single column that contains string values.

```sqlexample
CREATE OR REPLACE TABLE strings_test (s VARCHAR);

INSERT INTO strings_test values
  ('coffee'),
  ('ice tea'),
  ('latte'),
  ('tea'),
  (NULL);

SELECT * from strings_test;
```

```output
+---------+
| S       |
|---------|
| coffee  |
| ice tea |
| latte   |
| tea     |
| NULL    |
+---------+
```

Determine whether the values in column `s` contain the string `te`:

```sqlexample
SELECT * FROM strings_test WHERE CONTAINS(s, 'te');
```

```output
+---------+
| S       |
|---------|
| ice tea |
| latte   |
| tea     |
+---------+
```

### Use CONTAINS with collation

In the following example, CONTAINS returns different results for the same argument
values with different collation specifications.

```sqlexample
SELECT CONTAINS(COLLATE('ñ', 'en-ci-ai'), 'n'),
       CONTAINS(COLLATE('ñ', 'es-ci-ai'), 'n');
```

```output
+-----------------------------------------+-----------------------------------------+
| CONTAINS(COLLATE('Ñ', 'EN-CI-AI'), 'N') | CONTAINS(COLLATE('Ñ', 'ES-CI-AI'), 'N') |
|-----------------------------------------+-----------------------------------------|
| True                                    | False                                   |
+-----------------------------------------+-----------------------------------------+
```
