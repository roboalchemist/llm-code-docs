# Source: https://docs.oxla.com/sql-reference/sql-clauses/from/outer-join.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxla.com/llms.txt
> Use this file to discover all available pages before exploring further.

# OUTER JOIN

## Overview

The `OUTER JOIN` **or** `FULL OUTER JOIN` returns all the records from the selected fields between the two tables (left table & right table) whether the join condition is met or not.

### **Inner Join vs. Outer Join**

The most significant difference between an `INNER JOIN` and an `OUTER JOIN` is that the `INNER JOIN` only returns the information from both tables which are common and related to each other. The OUTER JOIN will return all rows (matched/unmatched) from both tables.

<Tip>We support table aliasing used in the OUTER JOIN clause.</Tip>

## Syntax

### Basic Syntax

```sql  theme={null}
SELECT column_1, column_2...
FROM table_1
FULL OUTER JOIN table_2
ON table_1.matching_field = table2.matching_field;
```

In the above syntax:

1. `SELECT column_1, column_2...` defines the **columns** from both tables where we want to display data.
2. `FROM table_1` represents the **left table** with table\_1 in the FROM clause.
3. `FULL OUTER JOIN table_2` represents the **right table** with table\_2 in the FULL OUTER JOIN condition.
4. `ON table_1.matching_field = table2.matching_field` sets the join condition after the **ON** keyword with the matching field between the two tables.&#x20;

### Syntax with an Alias

You can use an alias to refer to the table’s name. The results will stay the same. It only helps to write the query easier.

```sql  theme={null}
SELECT A.column_1, B.column_2...
FROM table_1 A //table_1 as A
FULL OUTER JOIN table_2 B //table_2 as B
ON A.matching_field = B.matching_field;
```

<Note>If there are no matched records from the joined tables, the `NULL` values will return in every column of the table that doesn’t have the matching record.</Note>

## Example

**departments table**

```sql  theme={null}
CREATE TABLE departments (
	department_id int,
	department_name text
);
INSERT INTO departments (department_id,department_name)
VALUES
	(1001, 'Sales'),
	(1002, 'Marketing'),
	(1003, 'HR'),
	(1004, 'Project'),
	(1005, 'Product');
```

```sql  theme={null}
SELECT * FROM departments;
```

It will create a **departments** table as shown below:

```sql  theme={null}
+----------------+------------------+
| department_id  | department_name  |
+----------------+------------------+
| 1001           | Sales            |
| 1002           | Marketing        |
| 1003           | HR               |
| 1004           | Project          |
| 1005           | Product          |
+----------------+------------------+
```

**employee table**

```sql  theme={null}
CREATE TABLE employee (
	employee_id int,
	employee_name text,
	dept_id int
);
INSERT INTO employee (
	employee_id,
	employee_name,
    dept_id
)
VALUES
	(2001,'Tony Stark', 1002),
	(2002,'Christian Bale', 1002),
	(2003,'Anne Hailey', 1003),
	(2004,'Wilson Cliff', 1004),
	(2005,'Susan Oh', 1001),
	(2006,'Julian Robert', 1001),
    (2007,'Gilbert Tom', null);
```

```sql  theme={null}
SELECT * FROM employee;
```

It will create an **employee** table as shown below:

```sql  theme={null}
+--------------+-------------------+------------+
| employee_id  | employee_name     | dept_id    |
+--------------+-------------------+------------+
| 2001         | Tony Stark        | 1002       |
| 2002         | Christian Bale    | 1002       |
| 2003         | Anne Hailey       | 1003       |
| 2004         | Wilson Cliff      | 1004       |
| 2005         | Susan Oh          | 1001       |
| 2006         | Julian Robert     | 1001       |
| 2007         | Gilbert Tom       | null       |
+--------------+-------------------+------------+
```

***

### Case 1: FULL OUTER JOIN

1\) Based on the above tables, we can write an `OUTER JOIN` query as follows:

```sql  theme={null}
SELECT employee_name, department_name
FROM departments
FULL OUTER JOIN employee
ON departments.department_id = employee.dept_id;
```

2\) The result will show every department with an employee and the employee who works under a specific department.

3\) It also includes every department that does not have any employees and the employees who do not belong to a specific department.

```sql  theme={null}
+-------------------+-------------------+
| employee_name     | department_name   |
+-------------------+-------------------+
| Julian Robert     | Sales             |
| Susan Oh          | Sales             |
| Christian Bale    | Marketing         |
| Tony Stark        | Marketing         |
| Anne Hailey       | HR                |
| Wilson Cliff      | Project           |
| Gilbert Tom       | null              |
| null              | Product           |
+-------------------+-------------------+
```

The following Venn diagram illustrates the FULL OUTER JOIN:

<img className="block dark:hidden" src="https://mintcdn.com/oxla/0Js4fLL2Ovp7KANj/assets/images/light/outerjoin/outerjoin-one-light.png?fit=max&auto=format&n=0Js4fLL2Ovp7KANj&q=85&s=34c1d3318dc6e7cd482f208e337a0d91" alt="" data-og-width="2075" width="2075" data-og-height="1409" height="1409" data-path="assets/images/light/outerjoin/outerjoin-one-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/oxla/0Js4fLL2Ovp7KANj/assets/images/light/outerjoin/outerjoin-one-light.png?w=280&fit=max&auto=format&n=0Js4fLL2Ovp7KANj&q=85&s=59ffed17f202ac0704b4278b79df36dd 280w, https://mintcdn.com/oxla/0Js4fLL2Ovp7KANj/assets/images/light/outerjoin/outerjoin-one-light.png?w=560&fit=max&auto=format&n=0Js4fLL2Ovp7KANj&q=85&s=a692633ed17f33b3e260baa86d90052d 560w, https://mintcdn.com/oxla/0Js4fLL2Ovp7KANj/assets/images/light/outerjoin/outerjoin-one-light.png?w=840&fit=max&auto=format&n=0Js4fLL2Ovp7KANj&q=85&s=c1bc345974743db82e124454b310a3d0 840w, https://mintcdn.com/oxla/0Js4fLL2Ovp7KANj/assets/images/light/outerjoin/outerjoin-one-light.png?w=1100&fit=max&auto=format&n=0Js4fLL2Ovp7KANj&q=85&s=fe05d18084a3d984f836f03a61e0fcc1 1100w, https://mintcdn.com/oxla/0Js4fLL2Ovp7KANj/assets/images/light/outerjoin/outerjoin-one-light.png?w=1650&fit=max&auto=format&n=0Js4fLL2Ovp7KANj&q=85&s=bb09d5a1ec7bc5d16d3af6b1cfea7336 1650w, https://mintcdn.com/oxla/0Js4fLL2Ovp7KANj/assets/images/light/outerjoin/outerjoin-one-light.png?w=2500&fit=max&auto=format&n=0Js4fLL2Ovp7KANj&q=85&s=ac999be9630f695bccd0ccfc115696de 2500w" />

<img className="hidden dark:block" src="https://mintcdn.com/oxla/ONnYYkZc0LCcRiQR/assets/images/dark/outerjoin/outerjoin-one-dark.png?fit=max&auto=format&n=ONnYYkZc0LCcRiQR&q=85&s=88a03975287a9aa48c87ca330d729c90" alt="" data-og-width="2075" width="2075" data-og-height="1409" height="1409" data-path="assets/images/dark/outerjoin/outerjoin-one-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/oxla/ONnYYkZc0LCcRiQR/assets/images/dark/outerjoin/outerjoin-one-dark.png?w=280&fit=max&auto=format&n=ONnYYkZc0LCcRiQR&q=85&s=e3a43a91f3496eb3d85ce89cabb4915b 280w, https://mintcdn.com/oxla/ONnYYkZc0LCcRiQR/assets/images/dark/outerjoin/outerjoin-one-dark.png?w=560&fit=max&auto=format&n=ONnYYkZc0LCcRiQR&q=85&s=c9535e15be94e6a33f5d317a9e5f58b2 560w, https://mintcdn.com/oxla/ONnYYkZc0LCcRiQR/assets/images/dark/outerjoin/outerjoin-one-dark.png?w=840&fit=max&auto=format&n=ONnYYkZc0LCcRiQR&q=85&s=ae354f2993a8833e0aa797568d4d2b29 840w, https://mintcdn.com/oxla/ONnYYkZc0LCcRiQR/assets/images/dark/outerjoin/outerjoin-one-dark.png?w=1100&fit=max&auto=format&n=ONnYYkZc0LCcRiQR&q=85&s=1502dfe2381f6918c4856e9a12aa4071 1100w, https://mintcdn.com/oxla/ONnYYkZc0LCcRiQR/assets/images/dark/outerjoin/outerjoin-one-dark.png?w=1650&fit=max&auto=format&n=ONnYYkZc0LCcRiQR&q=85&s=fbf88c24ab7841f29180445795c1c3b8 1650w, https://mintcdn.com/oxla/ONnYYkZc0LCcRiQR/assets/images/dark/outerjoin/outerjoin-one-dark.png?w=2500&fit=max&auto=format&n=ONnYYkZc0LCcRiQR&q=85&s=5c7d5789d6d5b408cb7a0393ca7de201 2500w" />

***

### Case 2: `FULL OUTER JOIN` with `WHERE` Clause

**a) Employee**

1. We can look up the department that does not have any employees by adding a `WHERE` clause and `NULL` as the following query:

```sql  theme={null}
SELECT employee_name, department_name
FROM departments
FULL OUTER JOIN employee
ON departments.department_id = employee.dept_id
WHERE employee_name IS NULL;
```

2. The result will indicate that the **Product** department doesn’t have any employees 👨🏻‍💼

```sql  theme={null}
+------------------+--------------------+
| employee_name    | department_name    |
+------------------+--------------------+
| null             | Product            |
+------------------+--------------------+
```

**b) Department**

1\) Let’s find out the employee who doesn’t belong to any department by adding a WHERE clause and NULL as the following query:

```sql  theme={null}
SELECT employee_name, department_name
FROM employee
FULL OUTER JOIN departments
ON employee.dept_id = departments.department_id
WHERE department_name IS NULL;
```

2\) The result will show that **Gilbert Tom** doesn’t belong to any department 👨🏻‍💼

```sql  theme={null}
+------------------+--------------------+
| employee_name    | department_name    |
+------------------+--------------------+
| Gilbert Tom      | null               |
+------------------+--------------------+
```

The following Venn diagram illustrates how the FULL OUTER JOIN works for the department and employee with a null value:

<img className="block dark:hidden" src="https://mintcdn.com/oxla/0Js4fLL2Ovp7KANj/assets/images/light/outerjoin/outerjoin-two-light.png?fit=max&auto=format&n=0Js4fLL2Ovp7KANj&q=85&s=56a58c629001a32e36efcb2b36af0d6d" alt="" data-og-width="2075" width="2075" data-og-height="1409" height="1409" data-path="assets/images/light/outerjoin/outerjoin-two-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/oxla/0Js4fLL2Ovp7KANj/assets/images/light/outerjoin/outerjoin-two-light.png?w=280&fit=max&auto=format&n=0Js4fLL2Ovp7KANj&q=85&s=760d1bd9ecdcc504f9e6bd326bf40827 280w, https://mintcdn.com/oxla/0Js4fLL2Ovp7KANj/assets/images/light/outerjoin/outerjoin-two-light.png?w=560&fit=max&auto=format&n=0Js4fLL2Ovp7KANj&q=85&s=ca8c39672d4483b5f944134f27e3f221 560w, https://mintcdn.com/oxla/0Js4fLL2Ovp7KANj/assets/images/light/outerjoin/outerjoin-two-light.png?w=840&fit=max&auto=format&n=0Js4fLL2Ovp7KANj&q=85&s=6977a607a113064f6f977dbb6a2fc8fd 840w, https://mintcdn.com/oxla/0Js4fLL2Ovp7KANj/assets/images/light/outerjoin/outerjoin-two-light.png?w=1100&fit=max&auto=format&n=0Js4fLL2Ovp7KANj&q=85&s=97e160a8f6e2fd32e22f2db1429f3997 1100w, https://mintcdn.com/oxla/0Js4fLL2Ovp7KANj/assets/images/light/outerjoin/outerjoin-two-light.png?w=1650&fit=max&auto=format&n=0Js4fLL2Ovp7KANj&q=85&s=6e4ef9e5cd3848d71f6be8089294d5b7 1650w, https://mintcdn.com/oxla/0Js4fLL2Ovp7KANj/assets/images/light/outerjoin/outerjoin-two-light.png?w=2500&fit=max&auto=format&n=0Js4fLL2Ovp7KANj&q=85&s=0ae1fe9d0fd08aec741b2b80c7f17838 2500w" />

<img className="hidden dark:block" src="https://mintcdn.com/oxla/ONnYYkZc0LCcRiQR/assets/images/dark/outerjoin/outerjoin-two-dark.png?fit=max&auto=format&n=ONnYYkZc0LCcRiQR&q=85&s=1f0e3a8fa281458b2303b10c4f3d9322" alt="" data-og-width="2075" width="2075" data-og-height="1409" height="1409" data-path="assets/images/dark/outerjoin/outerjoin-two-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/oxla/ONnYYkZc0LCcRiQR/assets/images/dark/outerjoin/outerjoin-two-dark.png?w=280&fit=max&auto=format&n=ONnYYkZc0LCcRiQR&q=85&s=6473337fb5fef3f2484f565be258cb11 280w, https://mintcdn.com/oxla/ONnYYkZc0LCcRiQR/assets/images/dark/outerjoin/outerjoin-two-dark.png?w=560&fit=max&auto=format&n=ONnYYkZc0LCcRiQR&q=85&s=06e9288b856313795d4b6ec66d6fb6b4 560w, https://mintcdn.com/oxla/ONnYYkZc0LCcRiQR/assets/images/dark/outerjoin/outerjoin-two-dark.png?w=840&fit=max&auto=format&n=ONnYYkZc0LCcRiQR&q=85&s=146d58f176082c38bd1bdb5091c49d6c 840w, https://mintcdn.com/oxla/ONnYYkZc0LCcRiQR/assets/images/dark/outerjoin/outerjoin-two-dark.png?w=1100&fit=max&auto=format&n=ONnYYkZc0LCcRiQR&q=85&s=edf7f3215d77f3ec6322e0389584168e 1100w, https://mintcdn.com/oxla/ONnYYkZc0LCcRiQR/assets/images/dark/outerjoin/outerjoin-two-dark.png?w=1650&fit=max&auto=format&n=ONnYYkZc0LCcRiQR&q=85&s=2f39013b37c197ff67d7b7d1aa785ef9 1650w, https://mintcdn.com/oxla/ONnYYkZc0LCcRiQR/assets/images/dark/outerjoin/outerjoin-two-dark.png?w=2500&fit=max&auto=format&n=ONnYYkZc0LCcRiQR&q=85&s=40d6e7c81cbf911ea41b694f8e93b708 2500w" />
