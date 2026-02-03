# Source: https://docs.oxla.com/sql-reference/sql-functions/other-functions/nullif.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxla.com/llms.txt
> Use this file to discover all available pages before exploring further.

# nullif()

## Overview

The `NULLIF()` function allows us to replace a given value with null if it matches a specific criterion.&#x20;

## Syntax

The following illustrates the syntax of the `NULLIF` function:

```sql  theme={null}
NULLIF(argument_1,argument_2);
```

From the syntax above, we learn that the `NULLIF` function takes two arguments:

* The first argument is the value we want to evaluate
* The second argument is the value we want to treat as null if the first argument matches it

<Tip>**The Output**: <br /> If the first argument matches the second argument, the `NULLIF()` function returns **NULL**. Otherwise, it returns the first argument as-is.</Tip>

## Examples

### Case #1: Handling Equal Values

In this case, the `NULLIF` function is used to compare the values 4 and 4.&#x20;

```sql  theme={null}
SELECT NULLIF (4, 4);
```

The result will be `NULL` since the two values being compared are equal (4 = 4).

```sql  theme={null}
 if 
----
   
```

### Case #2: Handing Different Values

In this example, we want to use the `NULLIF` function to manage different values.

```sql  theme={null}
SELECT NULLIF (9, 0);
```

The result will be `9` because the second value in the `NULLIF` function is 0 (The two values are not equal).

```sql  theme={null}
 if 
----
  9
```

### Case #3: String Comparison

In this case, the `NULLIF` function compares the strings 'L' and 'O'.

```sql  theme={null}
SELECT NULLIF ('L', 'O');
```

The result will be `L` because the two strings being compared ('L' and 'O') are not equal. Therefore, the function returns the first string.

```sql  theme={null}
 if 
----
 L
```

### Case #4: Handling Default Values

Suppose we have an `employees` table with columns for `name` and `salary`. This query retrieves employee names and their adjusted salaries, where a salary of 0 is replaced with NULL:

```sql  theme={null}
CREATE TABLE employees (
    name TEXT,
    salary INT
);

INSERT INTO employees (name, salary)
VALUES
    ('John', 50000),
    ('Jane', 0),
    ('Roy', 0),
    ('NEil', 0),
    ('Michael', 75000);
```

Display the records of the table:

```sql  theme={null}
SELECT * FROM employees;
```

```sql  theme={null}
  name   | salary 
---------+--------
 John    |  50000
 Jane    |      0
 Roy     |      0
 NEil    |      0
 Michael |  75000
```

This query retrieves employee names and their adjusted salaries, where a salary of 0 is replaced with NULL:

```sql  theme={null}
SELECT name, NULLIF(salary, 0) AS adjusted_salary
FROM employees;
```

The `NULLIF` function checks if the `salary` value is 0. If it is, the function returns NULL - otherwise, it returns the original `salary` value.&#x20;

```sql  theme={null}
  name   | adjusted_salary 
---------+-----------------
 John    |           50000
 Jane    |                
 Roy     |                
 NEil    |                
 Michael |           75000
```

### Case #5: Avoiding Division by Zero

Suppose we have a `fractions` table with columns, a `numerator` and a `denominator`.&#x20;

```sql  theme={null}
CREATE TABLE fractions (
    numerator INT,
    denominator INT
);

INSERT INTO fractions (numerator, denominator)
VALUES
    (10, 2),
    (20, 0),
    (15, 3),
    (75, 0),
    (15, 3);
```

Display the table using the `SELECT` statement:

```sql  theme={null}
SELECT * FROM fractions;
```

```sql  theme={null}
 numerator | denominator 
-----------+-------------
        10 |           2
        20 |           0
        15 |           3
        75 |           0
        15 |           3
```

Here, the `NULLIF` function is applied to the `denominator` column. If the `denominator` is 0, the function returns NULL, avoiding division by zero.

```sql  theme={null}
SELECT numerator, denominator, numerator / NULLIF(denominator, 0) AS "result" FROM fractions;
```

The result is shown in the result column.&#x20;

```sql  theme={null}
 numerator | denominator | result 
-----------+-------------+--------
        10 |           2 |      5
        20 |           0 |       
        15 |           3 |      5
        75 |           0 |       
        15 |           3 |      5
```
