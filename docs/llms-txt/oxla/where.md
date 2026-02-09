# Source: https://docs.oxla.com/sql-reference/sql-clauses/where.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxla.com/llms.txt
> Use this file to discover all available pages before exploring further.

# WHERE

## Overview

The `WHERE` clause returns a specific value from a table or multiple tables based on specified conditions. It will filter out records you do not want to be included and only returns the exact result when the condition is fulfilled.

## Syntax

The basic syntax of the WHERE clause is as follows −

```sql  theme={null}
SELECT column1, column2, ...
FROM table_name
WHERE [condition]
```

Let’s explore the above syntax:

* `SELECT column1, column2, ...` defines the columns where the records will be displayed.
* `FROM table_name` sets the table name where the records will be taken from.
* `WHERE [condition]`specifies the search condition using comparison or logical operators (e.g., `>`, `=`, `LIKE`)

<Check>It starts with the `FROM` clause **->** then it executes the `WHERE` condition **->** after that, it will `SELECT` the specified columns.</Check>

## Examples

Let’s assume that we have a table salary with records as follows:

```sql  theme={null}
CREATE TABLE salary (
  empid int,
  empname text,
  empdept text,
  empaddress text,
  empsalary int
);
INSERT INTO salary 
    (empid, empname, empdept, empaddress, empsalary) 
VALUES 
    (2001,'Paul','HR', 'California', null ),
    (2002,'Brandon','Product', 'Norway', 15000),
    (2003,'Bradley','Marketing', 'Texas', null),
    (2004,'Lisa','Marketing', 'Houston', 10000),
    (2005,'Emily','Marketing', 'Texas', 20000),
    (2006,'Bobby','Finance', 'Seattle', 20000),
    (2007,'Parker','Project', 'Texas', 45000);
```

```sql  theme={null}
SELECT * FROM salary;
```

It will create a table as shown below:

```sql  theme={null}
+--------+-----------+------------+-------------+------------+
| empid  | empname   |  empdept   | empaddress  | empsalary  |
+--------+-----------+------------+-------------+------------+
| 2001   | Paul      | HR         | California  | null       |  
| 2002   | Brandon   | Product    | Norway      | 15000      |
| 2003   | Bradley   | Marketing  | Texas       | null       |
| 2004   | Lisa      | Marketing  | Houston     | 10000      |
| 2005   | Emily     | Marketing  | Texas       | 20000      |
| 2006   | Bobby     | Finance    | Seattle     | 20000      |
| 2007   | Parker    | Project    | Texas       | 45000      |
+--------+-----------+------------+-------------+------------+
```

### #Case 1: WHERE clause with `=` Operator

Here we will be using the “equal” operator to look up the employee who works in the Marketing department:

```sql  theme={null}
SELECT empname, empdept
FROM salary
WHERE empdept = 'Marketing';
```

The above command will create the following result:

```sql  theme={null}
+------------+-------------+
| empname    | empdept     |
+------------+-------------+
| Bradley    | Marketing   |
| Emily      | Marketing   | 
| Lisa       | Marketing   |
+------------+-------------+
```

<Warning>The value defined in the `WHERE` clause’s condition is **case-sensitive**, so ensure that you specify the correct and precise value.</Warning>

### #Case 2: WHERE clause with `!=` Operator

Here we will be using the “not equal” operator to look up the employee who doesn’t live in Texas:

```sql  theme={null}
SELECT empname, empdept, empaddress
FROM salary
WHERE empaddress != 'Texas';
```

<Info>We can use the `<>` operator for another “not equal” operator.</Info>

The above query will give the following result:

```sql  theme={null}
+------------+------------+--------------+
| empname    | empdept    | empaddress   |
+------------+------------+--------------+
| Paul       | HR         | California   | 
| Brandon    | Product    | Norway       | 
| Lisa       | Marketing  | Houston      |
| Bobby      | Finance    | Seattle      |
+------------+------------+--------------+
```

<Warning>The value defined in the `WHERE` clause's condition is **case-sensitive**. If you set `texas` it will return all records from the salary table.</Warning>

### #Case 3: WHERE clause with `>` Operator

Here we will be using the “greater than” operator to figure out who has a salary above 20000:

```sql  theme={null}
SELECT empname, empdept, empsalary
FROM salary
WHERE empsalary > 20000;
```

<Info>We can use the `<` operator for a “less than” condition.</Info>

The output will let us know that Parker has a salary greater than 20000:

```sql  theme={null}
+------------+------------+-------------+
| empname    | empdept    | empsalary   |
+------------+------------+-------------+
| Parker     | Project    | 45000       | 
+------------+------------+-------------+
```

### #Case 4: WHERE clause with `<=` Operator

Here we will be using the “less than or equal to” operator to see who has a salary less than or equal to 15000:

```sql  theme={null}
SELECT empname, empdept, empsalary
FROM salary
WHERE empsalary <= '15000';
```

<Info>We can use the `>=` operator for a “greater than or equal to” condition.</Info>

The output will let us know that Brandon has a salary equal to 15000 and Lisa has a salary of less than 15000:

```sql  theme={null}
+------------+------------+-------------+
| empname    | empdept    | empsalary   |
+------------+------------+-------------+
| Brandon    | Product    | 15000       | 
| Lisa       | Marketing  | 10000       |
+------------+------------+-------------+
```

### #Case 5: WHERE clause with `LIKE` Operator

Here we will use the “like” operator to retrieve the employee whose first name starts with **Br**.

```sql  theme={null}
SELECT * FROM salary
WHERE empname LIKE 'Br%';
```

<Info>Do the reverse to get the result based on the last string, `%string`.</Info>

We will get an output where the above query fetches **Br**andon & **Br**adley.

```sql  theme={null}
+---------+------------+--------------+--------------+-----------+
| empid   | empname    | empdept     | empaddress   | empsalary  |
+---------+------------+-------------+--------------+------------+
| 2002    | Brandon    | Product     | Norway       | null       |
| 2003    | Bradley    | Marketing   | Texas        | 45000      |
+---------+------------+-------------+--------------+------------+
```

### #Case 6: WHERE clause with `IS NULL` Operator

Here we will use the “is null” operator to search for the employee who doesn’t have a salary value. It will return `true` and display the result set if a value is `NULL`; otherwise, it will return `false` with no result set.

```sql  theme={null}
SELECT * FROM salary
WHERE empsalary IS NULL;
```

The above command will create the following result:

```sql  theme={null}
+---------+------------+-------------+--------------+------------+
| empid   | empname    | empdept     | empaddress   | empsalary  |
+---------+------------+-------------+--------------+------------+
| 2001    | Paul       | HR          | California   | null       |
| 2003    | Brandon    | Product     | Norway       | null       |
+---------+------------+-------------+--------------+------------+
```
