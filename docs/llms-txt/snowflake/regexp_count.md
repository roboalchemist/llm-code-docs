# Source: https://docs.snowflake.com/en/sql-reference/functions/regexp_count.md

Categories:
:   [String functions (regular expressions)](../functions-regexp.md)

# REGEXP_COUNT

Returns the number of times that a [pattern](../functions-regexp.md) occurs in a string.

## Syntax

```sqlsyntax
REGEXP_COUNT( <subject> ,
              <pattern>
                [ , <position>
                  [ , <parameters> ]
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

`parameters`
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

## Returns

Returns a value of type NUMBER. Returns NULL if any argument is NULL.

## Usage notes

See the [General usage notes](../functions-regexp.md) for regular expression functions.

## Collation details

Arguments with collation specifications currently aren’t supported.

## Examples

The following example counts occurrences of the word `was`. You can use the `\b` metacharacter to indicate
a word boundary. In the following example, matching begins at the first character in the string `w` and
ends at the last character in the string `s`, and so doesn’t match words that contain the string (such
as `washing`):

```sqlexample
SELECT REGEXP_COUNT('It was the best of times, it was the worst of times',
                    '\\bwas\\b',
                    1) AS result;
```

```output
+--------+
| RESULT |
|--------|
|      2 |
+--------+
```

The following example uses the `i` parameter for case-insensitive matching of the character `e`:

```sqlexample
SELECT REGEXP_COUNT('Excelence', 'e', 1, 'i') AS e_in_excelence;
```

```output
+----------------+
| E_IN_EXCELENCE |
|----------------|
|              4 |
+----------------+
```

The following example illustrates overlapping occurrences. Create a table and insert data:

```sqlexample
CREATE OR REPLACE TABLE overlap (id NUMBER, a STRING);
INSERT INTO overlap VALUES (1,',abc,def,ghi,jkl,');
INSERT INTO overlap VALUES (2,',abc,,def,,ghi,,jkl,');

SELECT * FROM overlap;
```

```output
+----+----------------------+
| ID | A                    |
|----+----------------------|
|  1 | ,abc,def,ghi,jkl,    |
|  2 | ,abc,,def,,ghi,,jkl, |
+----+----------------------+
```

Run a query that uses REGEXP_COUNT to count the number of times that the following pattern
is found in each row: a punctuation mark followed by digits and letters, followed by a
punctuation mark.

```sqlexample
SELECT id,
       REGEXP_COUNT(a,
                    '[[:punct:]][[:alnum:]]+[[:punct:]]',
                    1,
                    'i') AS result
  FROM overlap;
```

```output
+----+--------+
| ID | RESULT |
|----+--------|
|  1 |      2 |
|  2 |      4 |
+----+--------+
```

The remaining examples use the data in the following table:

```sqlexample
CREATE OR REPLACE TABLE regexp_count_demo (dt DATE, messages VARCHAR);

INSERT INTO regexp_count_demo (dt, messages) VALUES
  ('10-AUG-2025','ER-6842,LG-230,LG-150,ER-3379,ER-6210'),
  ('11-AUG-2025','LG-272,LG-605,LG-683,ER-5577'),
  ('12-AUG-2025','ER-2207,LG-551,LG-826,ER-6842');

SELECT * FROM regexp_count_demo;
```

```output
+------------+---------------------------------------+
| DT         | MESSAGES                              |
|------------+---------------------------------------|
| 2025-08-10 | ER-6842,LG-230,LG-150,ER-3379,ER-6210 |
| 2025-08-11 | LG-272,LG-605,LG-683,ER-5577          |
| 2025-08-12 | ER-2207,LG-551,LG-826,ER-6842         |
+------------+---------------------------------------+
```

The following query returns the total number of messages for each day by searching for the delimiter (`,`) and
adding one to the total:

```sqlexample
SELECT dt,
       REGEXP_COUNT(messages, ',') + 1 AS message_count
  FROM regexp_count_demo;
```

```output
+------------+---------------+
| DT         | MESSAGE_COUNT |
|------------+---------------|
| 2025-08-10 |             5 |
| 2025-08-11 |             4 |
| 2025-08-12 |             4 |
+------------+---------------+
```

Assume that errors always begin with `ER` followed by a hyphen and a four-digit number. The following
query counts the number of errors for each day:

```sqlexample
SELECT dt,
       REGEXP_COUNT(messages, '\\bER-[0-9]{4}') AS number_of_errors
  FROM regexp_count_demo;
```

```output
+------------+------------------+
| DT         | NUMBER_OF_ERRORS |
|------------+------------------|
| 2025-08-10 |                3 |
| 2025-08-11 |                1 |
| 2025-08-12 |                2 |
+------------+------------------+
```
