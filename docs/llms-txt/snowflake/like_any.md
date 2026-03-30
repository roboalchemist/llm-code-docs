# Source: https://docs.snowflake.com/en/sql-reference/functions/like_any.md

Categories:
:   [String & binary functions](../functions-string.md) (Matching/Comparison)

# LIKE ANY

Performs a case-sensitive comparison to match a string against any of one or more specified patterns.
Use this function in a WHERE clause to filter for matches. For case-insensitive matching, use ILIKE ANY
instead.

> **Tip:**
>
> You can use the search optimization service to improve the performance of queries that call this function.
> For details, see [Search optimization service](../../user-guide/search-optimization-service.md).

See also:
:   [[ NOT ] LIKE](like.md) , [ILIKE ANY](ilike_any.md)

## Syntax

```sqlsyntax
<subject> LIKE ANY (<pattern1> [, <pattern2> ... ] ) [ ESCAPE <escape_char> ]
```

## Arguments

**Required:**

`subject`
:   The string to compare to the pattern(s).

`pattern#`
:   The pattern(s) that the string is to be compared to. You must specify at least one pattern.

**Optional:**

`escape_char`
:   Character(s) inserted in front of a wildcard character to indicate that the wildcard should
    be interpreted as a regular character rather than as a wildcard.

## Returns

Returns a BOOLEAN value or NULL:

* Returns TRUE if there is a match.
* Returns FALSE if there isn’t a match.
* Returns NULL if any argument is NULL.

## Usage notes

* To include single quotes or other special characters in pattern matching, you can use a
  [backslash escape sequence](../data-types-text.md).
* NULL does not match NULL. In other words, if the subject is NULL and one of the patterns is NULL,
  that is not considered a match.
* You can use the [NOT](../operators-logical.md) logical operator before the `subject`
  to perform a case-sensitive comparison that returns TRUE if it does not match any of the specified patterns.
* SQL wildcards are supported in `pattern`:

  * An underscore (`_`) matches any single character.
  * A percent sign (`%`) matches any sequence of zero or more characters.
* Wildcards in `pattern` include newline characters (`n`) in `subject` as matches.
* The pattern is considered a match if the pattern matches the entire input string (subject). To match a sequence
  anywhere within a string, start and end the pattern with `%` (e.g. `%something%`).

* If the function is used with a subquery, the subquery should return a single row.

  For example, the following should be used only if the subquery returns a single row:

  ```sqlexample
  SELECT ...
    WHERE x LIKE ANY (SELECT ...)
  ```

* If you require more complex pattern matching than this function supports, you can use a
  [regular expression function](../functions-regexp.md) instead.

## Collation details

Only the `upper`, `lower`, and `trim` collation specifications are supported. Combinations with `upper`,
`lower`, and `trim` are also supported (for example, `upper-trim` and `lower-trim`), except for locale
combinations (for example, `en-upper`).

## Examples

Create a table that contains some strings:

```sqlexample
CREATE OR REPLACE TABLE like_example(name VARCHAR(20));
INSERT INTO like_example VALUES
    ('John  Dddoe'),
    ('Joe   Doe'),
    ('John_down'),
    ('Joe down'),
    ('Tom   Doe'),
    ('Tim down'),
    (null);
```

This query shows how to use patterns with wildcards (`%`) to find matches:

```sqlexample
SELECT *
  FROM like_example
  WHERE name LIKE ANY ('%Jo%oe%','T%e')
  ORDER BY name;
```

```output
+-------------+
| NAME        |
|-------------|
| Joe   Doe   |
| John  Dddoe |
| Tom   Doe   |
+-------------+
```

This query shows how to use an escape character to indicate that a character that is usually a wild card (`_`) should be
treated as a literal.

```sqlexample
SELECT *
  FROM like_example
  WHERE name LIKE ANY ('%J%h%^_do%', 'T%^%e') ESCAPE '^'
  ORDER BY name;
```

```output
+-----------+
| NAME      |
|-----------|
| John_down |
+-----------+
```
