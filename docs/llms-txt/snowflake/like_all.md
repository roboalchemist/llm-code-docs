# Source: https://docs.snowflake.com/en/sql-reference/functions/like_all.md

Categories:
:   [String & binary functions](../functions-string.md) (Matching/Comparison)

# LIKE ALL

Performs a case-sensitive comparison to match a string against all of one or more specified patterns.
Use this function in a WHERE clause to filter for matches.

> **Tip:**
>
> You can use the search optimization service to improve the performance of queries that call this function.
> For details, see [Search optimization service](../../user-guide/search-optimization-service.md).

See also:
:   [[ NOT ] LIKE](like.md)

## Syntax

```sqlsyntax
<subject> LIKE ALL (<pattern1> [, <pattern2> ... ] ) [ ESCAPE <escape_char> ]
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

  For example, the following should be used only if the subquery returns
  a single row:

  ```sqlexample
  SELECT ...
    WHERE x LIKE ALL (SELECT ...)
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
CREATE OR REPLACE TABLE like_all_example(name VARCHAR(20));
INSERT INTO like_all_example VALUES
    ('John  Dddoe'),
    ('Joe   Doe'),
    ('John_do%wn'),
    ('Joe down'),
    ('Tom   Doe'),
    ('Tim down'),
    (null);
```

This query shows how to use patterns with wildcards (`%`) to find matches:

```sqlexample
SELECT *
  FROM like_all_example
  WHERE name LIKE ALL ('%Jo%oe%','J%e')
  ORDER BY name;
```

```output
+-------------+
| NAME        |
|-------------|
| Joe   Doe   |
| John  Dddoe |
+-------------+
```

This query shows that all patterns need to match for a successful result:

```sqlexample
SELECT *
  FROM like_all_example
  WHERE name LIKE ALL ('%Jo%oe%','J%n')
  ORDER BY name;
```

```output
+------+
| NAME |
|------|
+------+
```

This query shows how to use an escape character to indicate that characters that are usually wild cards (`_` and `%`)
should be treated as literals.

```sqlexample
SELECT *
  FROM like_all_example
  WHERE name LIKE ALL ('%J%h%^_do%', 'J%^%wn') ESCAPE '^'
  ORDER BY name;
```

```output
+------------+
| NAME       |
|------------|
| John_do%wn |
+------------+
```
