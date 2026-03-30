# Source: https://docs.snowflake.com/en/user-guide/search-optimization/substring-queries.md

# Speeding up substring and regular expression queries with search optimization

Search optimization can improve the performance of queries with predicates that search for substrings or use
regular expressions in text or semi-structured data. For details on how substring searches work with semi-structured
data, see [Speeding up queries of semi-structured data with search optimization](semi-structured-queries.md).

The following sections provide more information about search optimization support for substring and regular
expression queries:

* Enabling search optimization for substring and regular expression queries
* Supported predicates

## Enabling search optimization for substring and regular expression queries

To improve the performance of substring and regular expression queries on a table, use the
[ON SUBSTRING clause in the ALTER TABLE … ADD SEARCH OPTIMIZATION command](../../sql-reference/sql/alter-table.md)
for specific columns.

For example:

```sqlexample
ALTER TABLE mytable ADD SEARCH OPTIMIZATION ON SUBSTRING(mycol);
```

For more information, see [Enabling and disabling search optimization](enabling.md).

## Supported predicates

The search optimization service can improve the performance of queries with predicates that use:

* [LIKE](../../sql-reference/functions/like.md)
* [LIKE ANY](../../sql-reference/functions/like_any.md)
* [LIKE ALL](../../sql-reference/functions/like_all.md)
* [ILIKE](../../sql-reference/functions/ilike.md)
* [ILIKE ANY](../../sql-reference/functions/ilike_any.md)
* [CONTAINS](../../sql-reference/functions/contains.md)
* [ENDSWITH](../../sql-reference/functions/endswith.md)
* [STARTSWITH](../../sql-reference/functions/startswith.md)
* [SPLIT_PART](../../sql-reference/functions/split_part.md)
* [RLIKE](../../sql-reference/functions/rlike.md)
* [REGEXP](../../sql-reference/functions/regexp.md)
* [REGEXP_LIKE](../../sql-reference/functions/regexp_like.md)

The search optimization service can improve performance when searching for substrings that are five or more characters
long. (More selective substrings can result in better performance.) The search optimization service doesn’t
use search access paths for the following predicate because the substring is shorter than five characters:

```sqlexample
LIKE '%TEST%'
```

For the following predicate, the search optimization service can optimize this query, using search access paths to search for the
substrings for `SEARCH` and `OPTIMIZED`. However, search access paths are not used for `IS` because the substring is shorter
than five characters.

```sqlexample
LIKE '%SEARCH%IS%OPTIMIZED%'
```

For queries that use RLIKE, REGEXP, and REGEXP_LIKE against text:

* The `subject` argument must be a TEXT column in a table that has search optimization enabled.
* The `pattern` argument must be a string constant.

For regular expressions, the search optimization service works best when:

* The pattern contains at least one substring literal that is five or more characters long.
* The pattern specifies that the substring should appear at least once.

For example, the following pattern specifies that `string` should appear one or more times in the subject:

```sqlexample
RLIKE '(string)+'
```

The search optimization service can improve the performance of queries with the following patterns because each predicate
specifies that a substring of five or more characters must appear at least once. (Note that the first example uses a
[dollar-quoted string constant](../../sql-reference/data-types-text.md) to avoid escaping the backslash characters.)

```sqlexample
RLIKE $$.*email=[\w\.]+@snowflake\.com.*$$
```

```sqlexample
RLIKE '.*country=(Germany|France|Spain).*'
```

```sqlexample
RLIKE '.*phone=[0-9]{3}-?[0-9]{3}-?[0-9]{4}.*'
```

In contrast, search optimization does not use search access paths for queries with the following patterns:

* Patterns without any substrings:

  ```sqlexample
  RLIKE '.*[0-9]{3}-?[0-9]{3}-?[0-9]{4}.*'
  ```

* Patterns that only contain substrings shorter than five characters:

  ```sqlexample
  RLIKE '.*tel=[0-9]{3}-?[0-9]{3}-?[0-9]{4}.*'
  ```

* Patterns that use the alternation operator where one option is a substring shorter than five characters:

  ```sqlexample
  RLIKE '.*(option1|option2|opt3).*'
  ```

* Patterns in which the substring is optional:

  ```sqlexample
  RLIKE '.*[a-zA-z]+(string)?[0-9]+.*'
  ```

Even when the substring literals are shorter than five characters, the search optimization service can still improve query
performance if expanding the regular expression produces a substring literal that is five characters or longer.

For example, consider the pattern:

```output
.*st=(CA|AZ|NV).*(-->){2,4}.*
```

In this example:

* Although the substring literals (e.g. `st=`, `CA`, etc) are shorter than five characters, the search optimization service
  recognizes that the substring `st=CA`, `st=AZ`, or `st=NV` (each of which is five characters long) must appear in the text.
* Similarly, even though the substring literal `-->` is shorter than five characters, the search optimization service determines
  that the substring `-->-->` (which is longer than five characters) must appear in the text.

The search optimization service can use search access paths to match these substrings, which can improve the performance of the
query.
