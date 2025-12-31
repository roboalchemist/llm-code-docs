# Source: https://docs.oxla.com/sql-reference/sql-functions/string-functions/replace.md

# REPLACE()

## Overview

The `REPLACE()` function looks for and replaces a substring with a new one in a string. This function is often used to update the outdated or spelling mistakes in data that require an amendment.

<Info>Oxla also supports the [`REGEXP_REPLACE()`](/sql-reference/sql-functions/string-functions/regex/regexp-replace) function. It enables you to search and replace a substring that matches with a POSIX regular expression</Info>

## Syntax

The syntax for `REPLACE()` function is as follows:

```sql  theme={null}
REPLACE(string, old_substring, new_substring)
```

<Warning>The `REPLACE()` function performs a case-sensitive replacement</Warning>

### Parameters

The syntax requires three parameters, explained below:

* `string`: string that you want to replace
* `old_substring`: substring that you want to replace (all parts will be replaced if it appears multiple times in the string)
* `new_substring`: new substring that will replace the old one

## Examples

### Basic usage

In this example we will focus on a basic usage of the `REPLACE()` function, so we can understand on real example how it works.

```sql  theme={null}
SELECT REPLACE ('NewDatabase', 'New', 'Oxla');
```

The `REPLACE()` function will find all occurrences of the 'New' substring in the 'NewDatabase' string and replace it with the 'Oxla' substring, producing the following output:

```sql  theme={null}
+---------------------+
| f                   |
+---------------------+
| OxlaDatabase        |
+---------------------+
```

### Replacing specified values in a table

This example shows how to replace the values of a specific column in a table. For the needs of this example, we will create a new table named **extracurriculars** with **club** and **category** columns and insert the values into the respective columns.

```sql  theme={null}
CREATE TABLE hobby (
  club text,
  category text
);
INSERT INTO hobby 
    (club, category) 
VALUES 
    ('Bridge','group'),
    ('Painting','individual'),
    ('Basketball','group'),
    ('Volleyball','group');
```

Once that is done, we can retrieve all values from the table using the following query:

```sql  theme={null}
SELECT * FROM hobby;
```

```sql  theme={null}
+------------+---------------+
| club       | category      |
+------------+---------------+
| Bridge     | group         |
| Painting   | individual    |
| Basketball | group         |
| Volleyball | group         |
+--------------+-------------+
```

What we would do here is to replace the **'group'** values in the **category** column with **'sports'**:

````sql  theme={null}
SELECT REPLACE(category, 'group', 'sports') from hobby;
``` 

```sql
+--------------+
| f            |
+--------------+
| sports       |
| individual   |
| sports       |
| sports       |
+--------------+
````

### Removing a substring from a stirng

In the following example, we will show how to remove a substring from a string using the `REPLACE()` function. In this case we want to find all occurences of 'Friends' substring in 'Hello Friends' string and get rid of it:

```sql  theme={null}
SELECT REPLACE('Hello Friends', 'Friends', '');
```

```sql  theme={null}
+-----------+
| f         |
+-----------+
| Hello     |
+-----------+
```

### Replacing multiple patterns

The following example uses the `REPLACE()` function to replace multiple patterns of the given string:

```sql  theme={null}
SELECT REPLACE(REPLACE(REPLACE(REPLACE('2*[9-5]/{4+8}', '[', '('), ']', ')'), '{', '('), '}', ')');
```

We can see that the `REPLACE()` function is called multiple times to replace the corresponding string as specified:

* **`[]`** into **`()`**
* **`{}`** into **`()`**

```sql  theme={null}
+------------------+
| f                |
+------------------+
| 2*(9-5)/(4-8)    |
+------------------+
```
