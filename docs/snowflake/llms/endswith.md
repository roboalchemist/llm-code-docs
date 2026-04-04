# Source: https://docs.snowflake.com/en/sql-reference/functions/endswith.md

Categories:
:   [String & binary functions](../functions-string.md) (Matching/Comparison)

# ENDSWITH

Returns TRUE if the first expression ends with the second expression. Both expressions must be text or binary expressions.

> **Tip:**
>
> You can use the search optimization service to improve the performance of queries that call this function.
> For details, see [Search optimization service](../../user-guide/search-optimization-service.md).

## Syntax

```sqlsyntax
ENDSWITH( <expr1> , <expr2> )
```

## Arguments

`expr1`
:   The string to search in.

`expr2`
:   The string to search for at the end of `expr1`.

## Returns

Returns a BOOLEAN or NULL:

* Returns TRUE if `expr2` ends with `expr1`.
* Returns FALSE if `expr2` does not end with `expr1`.
* Returns NULL if either input expression is NULL.

## Collation details

The [collation specifications](../collation.md) of all input arguments must be compatible.

This function does not support the following collation specifications:

* `pi` (punctuation-insensitive).
* `cs-ai` (case-sensitive, accent-insensitive).

## Examples

These examples use the ENDSWITH function.

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

Determine whether the values in column `s` end with the string `te`:

```sqlexample
SELECT * FROM strings_test WHERE ENDSWITH(s, 'te');
```

```output
+-------+
| S     |
|-------|
| latte |
+-------+
```

### Use ENDSWITH with collation

In the following example, ENDSWITH returns different results for the same argument
values with different collation specifications.

```sqlexample
SELECT ENDSWITH(COLLATE('nñ', 'en-ci-ai'), 'n'),
       ENDSWITH(COLLATE('nñ', 'es-ci-ai'), 'n');
```

```output
+------------------------------------------+------------------------------------------+
| ENDSWITH(COLLATE('NÑ', 'EN-CI-AI'), 'N') | ENDSWITH(COLLATE('NÑ', 'ES-CI-AI'), 'N') |
|------------------------------------------+------------------------------------------|
| True                                     | False                                    |
+------------------------------------------+------------------------------------------+
```
