# Source: https://docs.oxla.com/sql-reference/sql-functions/string-functions/lower.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxla.com/llms.txt
> Use this file to discover all available pages before exploring further.

# LOWER

## Overview

The LOWER() function returns a given string, an expression, or values in a column in all lowercase letters. The syntax of the function is illustrated below:

```sql  theme={null}
LOWER(string)
```

It accepts input as a string and returns the text in the lowercase alphabet.

**Special Cases:** If there are characters in the input which are not of type string, they remain unaffected by the LOWER()function.

<Info>We support Unicode so that the ß is equivalent to the string ss.</Info>

## Examples

### #Case 1: Basic `LOWER()` function

The following basic query converts the given string in all lowercase alphabets:

```sql  theme={null}
SELECT LOWER('PostGreSQL');
```

The final output will be as follows:

```sql  theme={null}
+------------+
| lower      |
+------------+
| postgresql |
+------------+
```

### #Case 2: `LOWER()` function using columns

Let’s see how the `LOWER()` function works using an example with columns. We have a **personal\_details** table containing columns **id**, **first\_name**, **last\_name**, and **gender** of retail store employees.

```sql  theme={null}
CREATE TABLE personal_details (
  id int,
  first_name text,
  last_name text,
  gender text
);
INSERT INTO personal_details 
    (id, first_name, last_name, gender) 
VALUES 
    (1,'Mark','Wheeler','M'),
    (2,'Tom','Hanks','M'),
    (3,'Jane','Hopper','F'),
    (4,'Emily','Byers','F'),
    (5,'Lucas','Sinclair','M');
```

```sql  theme={null}
SELECT * FROM personal_details;
```

The above query will show the following table:

```sql  theme={null}
+-----+-------------+-------------+----------+
| id  | first_name  | last_name   | gender   |
+-----+-------------+-------------+----------+
| 1   | Mark        | Wheeler     | M        |
| 2   | Tom         | Hanks       | M        |
| 3   | Jane        | Hopper      | F        |
| 4   | Emily       | Byers       | F        |
| 5   | Lucas       | Sinclair    | M        |
+-----+-------------+-------------+----------+
```

Let’s assume that we want to convert the first and last names of employees with **id** numbers 2, 4, and 5 to all lowercase letters, which can be done using the following query:

```sql  theme={null}
SELECT first_name,last_name,LOWER(first_name),LOWER(last_name)
FROM personal_details
where id in (2, 4, 5);
```

The output displays the first and last names of employees with the specified ids in lowercase letters:

```sql  theme={null}
+------------+-------------+----------+----------+
| first_name | last_name   | lower    | lower    |
+------------+-------------+----------+----------+
| Tom        | Hanks       | tom      | hanks    |
| Emily      | Byers       | emily    | byers    |
| Lucas      | Sinclair    | lucas    | lucas    |
+------------+-------------+----------+----------+
```
