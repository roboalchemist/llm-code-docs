# Source: https://docs.snowflake.com/en/sql-reference/functions/split.md

Categories:
:   [String & binary functions](../functions-string.md) (General)

# SPLIT

Splits a given string with a given separator and returns the result in an array of strings.

Contiguous split strings in the source string, or the presence of a split string at the beginning
or end of the source string, results in an empty string in the output. An empty separator string results
in an array containing only the source string. If either parameter is a NULL, a NULL is returned.

You can use functions and constructs that operate on [arrays](../data-types-semistructured.md) on the result,
such as [FLATTEN](flatten.md), [ARRAY_SIZE](array_size.md), and [access by index position](../data-types-semistructured.md).

See also:
:   [SPLIT_PART](split_part.md)

## Syntax

```sqlsyntax
SPLIT(<string>, <separator>)
```

## Arguments

`string`
:   Text to be split into parts.

`separator`
:   Text to split string by.

## Returns

The data type of the returned value is ARRAY.

## Collation details

This function doesn’t support the following collation specifications:

* `pi` (punctuation-insensitive).
* `cs-ai` (case-sensitive, accent-insensitive).

The values in the output array don’t include a collation specification and therefore don’t support further
collation operations.

## Examples

Split the localhost IP address `127.0.0.1` into an array consisting of each of the four parts:

```sqlexample
SELECT SPLIT('127.0.0.1', '.');
```

```output
+-------------------------+
| SPLIT('127.0.0.1', '.') |
|-------------------------|
| [                       |
|   "127",                |
|   "0",                  |
|   "0",                  |
|   "1"                   |
| ]                       |
+-------------------------+
```

Access the first element in the returned array by index position:

```sqlexample
SELECT SPLIT('127.0.0.1', '.')[0];
```

```output
+----------------------------+
| SPLIT('127.0.0.1', '.')[0] |
|----------------------------|
| "127"                      |
+----------------------------+
```

Split a string that contains vertical lines as separators, which returns output
that contains empty strings:

```sqlexample
SELECT SPLIT('|a||', '|');
```

```output
+--------------------+
| SPLIT('|A||', '|') |
|--------------------|
| [                  |
|   "",              |
|   "a",             |
|   "",              |
|   ""               |
| ]                  |
+--------------------+
```

Use the result of SPLIT to generate multiple records from a single string using the LATERAL FLATTEN construct.
[FLATTEN](flatten.md) is a table function that takes a VARIANT, OBJECT, or ARRAY column and produces a lateral view
(that is, an inline view that contains correlation referring to other tables that precede it in the FROM clause):

```sqlexample
CREATE TABLE split_test_names(first_name VARCHAR, children VARCHAR);

INSERT INTO split_test_names values
  ('Mark', 'Marky,Mike,Maria'),
  ('John', 'Johnny,Jane');

SELECT * FROM split_test_names;
```

```output
+------------+------------------+
| FIRST_NAME | CHILDREN         |
|------------+------------------|
| Mark       | Marky,Mike,Maria |
| John       | Johnny,Jane      |
+------------+------------------+
```

```sqlexample
SELECT first_name, C.value::STRING AS childname
  FROM split_test_names,
    LATERAL FLATTEN(INPUT=>SPLIT(children, ',')) C;
```

```output
+------------+-----------+
| FIRST_NAME | CHILDNAME |
|------------+-----------|
| Mark       | Marky     |
| Mark       | Mike      |
| Mark       | Maria     |
| John       | Johnny    |
| John       | Jane      |
+------------+-----------+
```
