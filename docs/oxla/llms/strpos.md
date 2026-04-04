# Source: https://docs.oxla.com/sql-reference/sql-functions/string-functions/strpos.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxla.com/llms.txt
> Use this file to discover all available pages before exploring further.

# STRPOS

## Overview

The `STRPOS()` is used to return the position from where the substring (the second argument) is matched with the string (the first argument).

```sql  theme={null}
STRPOS(string, substring)
```

The input and return must be of type `string`.

**Special cases:**

* Returns `NULL` if there are no input rows or `NULL` values.
* If the `substring` is not found in the string, then the `STRPOS()` function will return 0.

## Examples

### Case 1: Basic `STRPOS()` function

In the example below, we will find the **ut** (substring) position in the **computer** (string):

```sql  theme={null}
SELECT STRPOS('computer', 'ut') AS "Position of ut";
```

We can see that **ut** is located at the fifth character of the **computer**:

```sql  theme={null}
+-----------------+
| Position of ut  |
+-----------------+
| 5               |
+-----------------+
```

### Case 2: STRPOS() function using column

We have a **listofwords** table where it stores the word data.

```sql  theme={null}
CREATE TABLE listofwords (
  words text
);
INSERT INTO listofwords 
    (words) 
VALUES 
    ('corral'),
    ('traditionally'),
    ('real'),
    ('communal'),
    ('challenge'),
    ('fall'),
    ('wall'),
    ('gallop'),
    ('albatross');
```

```sql  theme={null}
SELECT * FROM listofwords;
```

The above query will show the following table:

```sql  theme={null}
+----------------+
| words          |
+----------------+
| corral         |
| traditionally  | 
| real           | 
| communal       | 
| challenge      | 
| fall           | 
| wall           | 
| gallop         | 
| albatross      | 
+----------------+
```

The following query will display the words and a position of a specific substring = ‘**al**’ using the `STRPOS()` function:

```sql  theme={null}
SELECT words, STRPOS(words, 'al') AS "Position of al"
FROM listofwords;
```

The result will display the **al** position of different words:

```sql  theme={null}
+----------------+------------------+
| words          | Position of al   |
+----------------+------------------+
| corral         | 5                |
| traditionally  | 10               |
| real           | 3                |
| communal       | 7                |
| challenge      | 3                |
| fall           | 2                |
| wall           | 2                |
| gallop         | 2                |
| albatross      | 1                |
+----------------+------------------+
```
