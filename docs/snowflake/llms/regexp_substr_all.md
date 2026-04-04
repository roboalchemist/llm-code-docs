# Source: https://docs.snowflake.com/en/sql-reference/functions/regexp_substr_all.md

Categories:
:   [String functions (regular expressions)](../functions-regexp.md)

# REGEXP_SUBSTR_ALL

Returns an [ARRAY](../data-types-semistructured.md) that contains all substrings that match a
[regular expression](../functions-regexp.md) within a string.

Aliases:
:   REGEXP_EXTRACT_ALL

## Syntax

```sqlsyntax
REGEXP_SUBSTR_ALL( <subject> ,
                   <pattern>
                     [ , <position>
                       [ , <occurrence>
                         [ , <regex_parameters>
                           [ , <group_num> ]
                         ]
                       ]
                     ]
)
```

## Arguments

**Required:**

`subject`
:   The string to search for matches.

`pattern`
:   Pattern to match.

    For guidelines on specifying patterns, see [String functions (regular expressions)](../functions-regexp.md).

**Optional:**

`position`
:   Number of characters from the beginning of the string where the function starts searching for matches.
    The value must be a positive integer.

    Default: `1` (the search for a match starts at the first character on the left)

`occurrence`
:   Specifies the first occurrence of the pattern from which to start returning matches.

    The function skips the first `occurrence - 1` matches. For example, if there are 5 matches and
    you specify `3` for the `occurrence` argument, the function ignores the first two matches and
    returns the third, fourth, and fifth matches.

    Default: `1`

`regex_parameters`
:   String of one or more characters that specifies the parameters used for searching for matches. Supported values:

    | Parameter | Description |
    | --- | --- |
    | `c` | Case-sensitive matching |
    | `i` | Case-insensitive matching |
    | `m` | Multi-line mode |
    | `e` | Extract submatches |
    | `s` | Single-line mode POSIX wildcard character `.` matches `\n` |

    Default: `c`

    For more information, see [Specifying the parameters for the regular expression](../functions-regexp.md).

    > **Note:**
    >
    > By default, REGEXP_SUBSTR_ALL returns the entire matching part of the subject.
    > However, if the `e` parameter is specified, REGEXP_SUBSTR_ALL returns the
    > part of the subject that matches the first group in the pattern.
    > If `e` is specified but a `group_num` is not also specified, then the `group_num`
    > defaults to 1 (the first group). If there is no sub-expression in the pattern, REGEXP_SUBSTR_ALL behaves as
    > if `e` was not set. For examples that use `e`, see Examples in this topic.

`group_num`
:   Specifies which group to extract. Groups are specified by using parentheses in
    the regular expression.

    If a `group_num` is specified, Snowflake allows extraction even if the `'e'` option was not
    also specified. The `'e'` is implied.

    Snowflake supports up to 1024 groups.

    For examples that use `group_num`, see the Examples in this topic.

## Returns

The function returns a value of type ARRAY. The array contains an element for each matching substring.

The function returns an empty array if no match is found.

The function returns NULL in the following cases:

* Any argument is NULL.
* You specify `group_num` and the pattern doesn’t specify a grouping with that number. For example, if the
  pattern specifies only one group (for example, `a(b)c`), and you use `2` as `group_num`, the function returns
  NULL.

## Usage notes

For additional information on using regular expressions, see [String functions (regular expressions)](../functions-regexp.md).

## Collation details

Arguments with collation specifications currently aren’t supported.

## Examples

The pattern in the following example matches a lowercase “a” followed by a digit. The example returns an ARRAY that contains all
of the matches:

```sqlexample
SELECT REGEXP_SUBSTR_ALL('a1_a2a3_a4A5a6', 'a[[:digit:]]') AS matches;
```

```output
+---------+
| MATCHES |
|---------|
| [       |
|   "a1", |
|   "a2", |
|   "a3", |
|   "a4", |
|   "a6"  |
| ]       |
+---------+
```

The following example starts finding matches from the second character in the string (`2`):

```sqlexample
SELECT REGEXP_SUBSTR_ALL('a1_a2a3_a4A5a6', 'a[[:digit:]]', 2) AS matches;
```

```output
+---------+
| MATCHES |
|---------|
| [       |
|   "a2", |
|   "a3", |
|   "a4", |
|   "a6"  |
| ]       |
+---------+
```

The following example starts returning matches from the third occurrence of the pattern in the string (`3`):

```sqlexample
SELECT REGEXP_SUBSTR_ALL('a1_a2a3_a4A5a6', 'a[[:digit:]]', 1, 3) AS matches;
```

```output
+---------+
| MATCHES |
|---------|
| [       |
|   "a3", |
|   "a4", |
|   "a6"  |
| ]       |
+---------+
```

The following example performs a case-insensitive match (`i`):

```sqlexample
SELECT REGEXP_SUBSTR_ALL('a1_a2a3_a4A5a6', 'a[[:digit:]]', 1, 1, 'i') AS matches;
```

```output
+---------+
| MATCHES |
|---------|
| [       |
|   "a1", |
|   "a2", |
|   "a3", |
|   "a4", |
|   "A5", |
|   "a6"  |
| ]       |
+---------+
```

The following example performs a case-insensitive match and returns the part of the string that matches the first group (`ie`):

```sqlexample
SELECT REGEXP_SUBSTR_ALL('a1_a2a3_a4A5a6', '(a)([[:digit:]])', 1, 1, 'ie') AS matches;
```

```output
+---------+
| MATCHES |
|---------|
| [       |
|   "a",  |
|   "a",  |
|   "a",  |
|   "a",  |
|   "A",  |
|   "a"   |
| ]       |
+---------+
```

The following example demonstrates that the function returns an empty array when no matches are found:

```sqlexample
SELECT REGEXP_SUBSTR_ALL('a1_a2a3_a4A5a6', 'b') AS matches;
```

```output
+---------+
| MATCHES |
|---------|
| []      |
+---------+
```

This example shows how to retrieve each second word in a string from the first, second, and third
matches of a two-word pattern in which the first word is `A`.

First, create a table and insert data:

```sqlexample
CREATE OR REPLACE TABLE test_regexp_substr_all (string1 VARCHAR);;
INSERT INTO test_regexp_substr_all (string1) VALUES ('A MAN A PLAN A CANAL');
```

Run the query:

```sqlexample
SELECT REGEXP_SUBSTR_ALL(string1, 'A\\W+(\\w+)', 1, 1, 'e', 1) AS result1,
       REGEXP_SUBSTR_ALL(string1, 'A\\W+(\\w+)', 1, 2, 'e', 1) AS result2,
       REGEXP_SUBSTR_ALL(string1, 'A\\W+(\\w+)', 1, 3, 'e', 1) AS result3
  FROM test_regexp_substr_all;
```

```output
+-----------+-----------+-----------+
| RESULT1   | RESULT2   | RESULT3   |
|-----------+-----------+-----------|
| [         | [         | [         |
|   "MAN",  |   "PLAN", |   "CANAL" |
|   "PLAN", |   "CANAL" | ]         |
|   "CANAL" | ]         |           |
| ]         |           |           |
+-----------+-----------+-----------+
```

This example shows how to retrieve the first, second, and third groups within each occurrence of the pattern
in a string. In this case, the returned values are each individual letter of each matched word in each group.

```sqlexample
SELECT REGEXP_SUBSTR_ALL(string1, 'A\\W+(\\w)(\\w)(\\w)', 1, 1, 'e', 1) AS result1,
       REGEXP_SUBSTR_ALL(string1, 'A\\W+(\\w)(\\w)(\\w)', 1, 1, 'e', 2) AS result2,
       REGEXP_SUBSTR_ALL(string1, 'A\\W+(\\w)(\\w)(\\w)', 1, 1, 'e', 3) AS result3
  FROM test_regexp_substr_all;
```

```output
+---------+---------+---------+
| RESULT1 | RESULT2 | RESULT3 |
|---------+---------+---------|
| [       | [       | [       |
|   "M",  |   "A",  |   "N",  |
|   "P",  |   "L",  |   "A",  |
|   "C"   |   "A"   |   "N"   |
| ]       | ]       | ]       |
+---------+---------+---------+
```
