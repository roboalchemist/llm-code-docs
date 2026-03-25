# Source: https://docs.snowflake.com/en/sql-reference/functions/strtok_split_to_table.md

Categories:
:   [String & binary functions](../functions-string.md) (General) , [Table functions](../functions-table.md)

# STRTOK_SPLIT_TO_TABLE

Tokenizes a string with the given set of delimiters and flattens the results into rows.

See also:
:   [STRTOK](strtok.md), [STRTOK_TO_ARRAY](strtok_to_array.md)

## Syntax

```sqlsyntax
STRTOK_SPLIT_TO_TABLE(<string> [,<delimiter_list>])
```

## Arguments

**Required:**

`string`
:   Text to be tokenized.

**Optional:**

`delimiter_list`
:   Optional set of delimiters. The default value is a single space character.

## Output

This function returns the following columns:

| Column name | Data type | Description |
| --- | --- | --- |
| SEQ | NUMBER | A unique sequence number associated with the input record. The sequence is not guaranteed to be gap-free or ordered. in any particular way. |
| INDEX | NUMBER | The one-based index of the element. |
| VALUE | VARCHAR | The value of the element of the flattened array. |

> **Note:**
>
> The query can also access the columns of the original (correlated) table that served as the source of data for this function. If a single row
> from the original table resulted in multiple rows in the flattened view, the values in this input row are replicated to match the number of
> rows produced by this function.

## Examples

Here is a simple example on constant input.

```sqlexample
SELECT table1.value
  FROM TABLE(STRTOK_SPLIT_TO_TABLE('a.b', '.')) AS table1
  ORDER BY table1.value;
```

```output
+-------+
| VALUE |
|-------|
| a     |
| b     |
+-------+
```

Create a table and insert data:

```sqlexample
CREATE OR REPLACE TABLE splittable_strtok (v VARCHAR);
INSERT INTO splittable_strtok (v) VALUES ('a b'), ('cde'), ('f|g'), ('');
SELECT * FROM splittable_strtok;
```

```output
+-----+
| V   |
|-----|
| a b |
| cde |
| f|g |
|     |
+-----+
```

You can use the [LATERAL](../constructs/join-lateral.md) keyword with the STRTOK_SPLIT_TO_TABLE function
so that the function executes on each row of the `splittable_strtok` table as a correlated table:

```sqlexample
SELECT *
  FROM splittable_strtok, LATERAL STRTOK_SPLIT_TO_TABLE(splittable_strtok.v, ' ')
  ORDER BY SEQ, INDEX;
```

```output
+-----+-----+-------+-------+
| V   | SEQ | INDEX | VALUE |
|-----+-----+-------+-------|
| a b |   1 |     1 | a     |
| a b |   1 |     2 | b     |
| cde |   2 |     1 | cde   |
| f|g |   3 |     1 | f|g   |
+-----+-----+-------+-------+
```

This example is the same as the preceding, except that it specifies multiple delimiters:

```sqlexample
SELECT *
  FROM splittable_strtok, LATERAL STRTOK_SPLIT_TO_TABLE(splittable_strtok.v, ' |')
  ORDER BY SEQ, INDEX;
```

```output
+-----+-----+-------+-------+
| V   | SEQ | INDEX | VALUE |
|-----+-----+-------+-------|
| a b |   1 |     1 | a     |
| a b |   1 |     2 | b     |
| cde |   2 |     1 | cde   |
| f|g |   3 |     1 | f     |
| f|g |   3 |     2 | g     |
+-----+-----+-------+-------+
```

Create another table that contains authors in one column and some of their book titles in another column. In the table
data, the book titles might be separated by a comma or a semi-colon:

```sqlexample
CREATE OR REPLACE TABLE authors_books_test2 (author VARCHAR, titles VARCHAR);
INSERT INTO authors_books_test2 (author, titles) VALUES
  ('Nathaniel Hawthorne', 'The Scarlet Letter ; The House of the Seven Gables;The Blithedale Romance'),
  ('Herman Melville', 'Moby Dick,The Confidence-Man');
SELECT * FROM authors_books_test2;
```

```output
+---------------------+---------------------------------------------------------------------------+
| AUTHOR              | TITLES                                                                    |
|---------------------+---------------------------------------------------------------------------|
| Nathaniel Hawthorne | The Scarlet Letter ; The House of the Seven Gables;The Blithedale Romance |
| Herman Melville     | Moby Dick,The Confidence-Man                                              |
+---------------------+---------------------------------------------------------------------------+
```

Use the LATERAL keyword and the SPLIT_TO_TABLE function to run a query that returns a separate row for each title.
In addition, use the [TRIM](trim.md) function to remove leading and trailing spaces from the titles. Note that the SELECT
list includes the fixed `value` column that is returned by the function:

```sqlexample
SELECT author, TRIM(value) AS title
  FROM authors_books_test2, LATERAL STRTOK_SPLIT_TO_TABLE(titles, ',;')
  ORDER BY author;
```

```output
+---------------------+-------------------------------+
| AUTHOR              | TITLE                         |
|---------------------+-------------------------------|
| Herman Melville     | Moby Dick                     |
| Herman Melville     | The Confidence-Man            |
| Nathaniel Hawthorne | The Scarlet Letter            |
| Nathaniel Hawthorne | The House of the Seven Gables |
| Nathaniel Hawthorne | The Blithedale Romance        |
+---------------------+-------------------------------+
```
