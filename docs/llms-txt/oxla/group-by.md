# Source: https://docs.oxla.com/sql-reference/sql-clauses/group-by.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxla.com/llms.txt
> Use this file to discover all available pages before exploring further.

# GROUP BY

## Overview

The `GROUP BY` clause returns a group of records from a table or multiple tables with the same values as the specified columns.&#x20;

The result of the `GROUP BY` clause returns a single row for each value of the column.

<Note>You can use [aggregate functions](/sql-reference/sql-functions/aggregate-functions/overview) such as `COUNT()`, `MAX()`, `MIN()`, `SUM()`, etc., to perform the operations on the grouped values in the `SELECT` statement.</Note>

## Syntax

<Warning>Ensure the column you are using to group is available in the column list.</Warning>

### a) Basic syntax

The basic syntax of the `GROUP BY` clause is as follows −

```sql  theme={null}
SELECT
column_1, column_2, aggregate_function(column_3)
FROM
table_name
GROUP BY
column_1, column_2,...;
```

Let’s explore the above syntax:

* `SELECT column_1, column_2, aggregate_function(column_3)` defines the columns you want to group (`column_1, column_2`) and the column that you want to apply an aggregate function to (`column_3`).
* `FROM table_name` defines the table where the data comes from.
* `GROUP BY column_1, column_2,...;` lists the columns that you want to group in the `GROUP BY` clause.

<Info>The column specified in the `SELECT` command must also appear in the `GROUP BY` clause.</Info>

### b) Syntax with `WHERE` clause

Please take note that the `GROUP BY` clause must precisely appear after the `WHERE` clause, as shown below:

```sql  theme={null}
SELECT
column_1, column_2, aggregate_function(column_3)
FROM
table_name
WHERE
conditions
GROUP BY
column_1, column_2,...;
```

## Examples

Let’s assume that we have two tables here, the customer table and the orders table:

**customer table**

```sql  theme={null}
CREATE TABLE customer (
  cust_id int,
  cust_name text
);
INSERT INTO customer 
    (cust_id, cust_name) 
VALUES 
    (11001, 'Maya'),
    (11003, 'Ricky'),
    (11009, 'Sean'),
    (11008, 'Chris'),
    (11002, 'Emily'),
    (11005, 'Rue'),
    (11007, 'Tom'),
    (11006, 'Casey');
```

```sql  theme={null}
SELECT * FROM customer;
```

It will create a table as shown below:

```sql  theme={null}
+-----------+------------+
| cust_id   | cust_name  |
+-----------+------------+
| 11001     | Maya       |
| 11003     | Ricky      |
| 11009     | Sean       |
| 11008     | Chris      |
| 11002     | Emily      |
| 11005     | Rue        |
| 11007     | Tom        |
| 11006     | Casey      |
+-----------+------------+
```

| orders table |
| ------------ |

```sql  theme={null}
CREATE TABLE orders (
  order_id int,
  order_date date,
  order_prod text,
  order_qty int,
  order_price int,
  cust_id int
);
INSERT INTO orders 
    (order_id, order_date, order_prod, order_qty, order_price, cust_id) 
VALUES 
    (999191, '2021-01-08','Butter', 1, 4000, 11001),
    (999192, '2021-09-30','Sugar', 1, 10000, 11002),
    (999193, '2021-04-17','Sugar', 1, 10000, 11009),
    (999194, '2021-08-29','Flour', 4, 20000, 11006),
    (999195, '2021-05-04','Sugar', 2, 20000, 11008),
    (999196, '2021-07-27','Butter', 2, 8000, 11006),
    (999197, '2021-10-30','Flour', 2, 10000, 11001),
    (999198, '2021-12-18','Flour', 2, 10000, 11007);
```

```sql  theme={null}
SELECT * FROM orders;
```

It will create a table as shown below:

```sql  theme={null}
+------------+--------------+--------------+-------------+---------------+-----------+
| order_id   | order_date   | order_prod   | order_qty   | order_price   | cust_id   |
+------------+--------------+--------------+-------------+---------------+-----------+
| 999191     | 2021-01-08   | Butter       | 1           |  4000         | 11001     |
| 999192     | 2021-09-30   | Sugar        | 1           | 10000         | 11002     |
| 999193     | 2021-04-17   | Sugar        | 1           | 10000         | 11009     |
| 999194     | 2021-08-29   | Flour        | 4           | 20000         | 11006     |
| 999195     | 2021-05-04   | Sugar        | 2           | 20000         | 11008     |
| 999196     | 2021-07-27   | Butter       | 2           | 8000          | 11006     |
| 999197     | 2021-10-30   | Flour        | 2           | 10000         | 11001     |
| 999198     | 2021-12-18   | Flour        | 2           | 10000         | 11007     |
+------------+--------------+--------------+-------------+---------------+-----------+
```

### #Case 1: Basic `GROUP BY`

Here we will get all product names by grouping them using the products ordered from the **orders** table:

```sql  theme={null}
SELECT order_prod
FROM orders
GROUP BY order_prod;
```

The query above will return the output as below:

```sql  theme={null}
+--------------+
| order_prod   |
+--------------+
| flour        |
| sugar        |
| butter       |
+--------------+
```

### #Case 2: `GROUP BY` on Multiple Columns

The following example uses multiple columns in the `GROUP BY` clause:

```sql  theme={null}
SELECT order_id, order_prod
FROM orders
GROUP BY order_id, order_prod;
```

The above query will create the following result:

```sql  theme={null}
+-----------+--------------+
| order_id  | order_prod   |
+-----------+--------------+
| 999194    | flour        |
| 999191    | butter       |
| 999196    | flour        |
| 999192    | sugar        |
| 999195    | butter       |
| 999198    | sugar        |
| 999193    | flour        |
| 999197    | sugar        |
+-----------+--------------+
```

### #Case 3: `GROUP BY` with Aggregate Functions

For this example, we will calculate the total amount each customer has paid for their orders. We will use one of the aggregate functions, i.e., the `SUM()` function.

```sql  theme={null}
SELECT cust_id, SUM (order_price)
FROM orders
GROUP BY cust_id;
```

The query above will return the output as shown below:

```sql  theme={null}
+-----------+----------+
| cust_id   | sum      |
+-----------+----------+
| 11009     | 10000    |
| 11007     | 10000    |
| 11006     | 28000    |
| 11002     | 10000    |
| 11001     | 14000    |
| 11008     | 20000    |
+-----------+----------+
```

### #Case 4: `GROUP BY` with `JOIN` Condition

Unlike the previous example, the following query joins the orders table with the customer table and groups customers by their names. Here we will use `COUNT()` as the aggregate function to count the number of products each customer has purchased.

```sql  theme={null}
SELECT C.cust_name, COUNT (order_prod)
FROM orders O
JOIN customer C ON O.cust_id = C.cust_id
GROUP BY C.cust_name;
```

The above command will create the following result:

```sql  theme={null}
+------------+---------+
| cust_name  | count   |
+------------+---------+
| Tom        | 1       |
| Chris      | 1       |
| Casey      | 2       |
| Maya       | 2       |
| Sean       | 1       |
| Emily      | 1       |
+------------+---------+
```

### #Case 5: `GROUP BY` with Date Data Type

The `order_date` column uses a `DATE` data type. In this example, we will group the order’s quantity and total price by dates using the `DATE()` function.

```sql  theme={null}
SELECT DATE(order_date), order_qty, SUM(order_price)
FROM orders
GROUP BY order_qty, DATE(order_date);
```

The above query will generate the following result:

```sql  theme={null}
+---------------+------------+---------+
| date          | order_qty  | sum     |
+---------------+------------+---------+
| 2021-07-27    | 2          | 8000    |
| 2021-08-29    | 4          | 20000   |
| 2021-04-17    | 1          | 10000   |
| 2021-09-30    | 1          | 10000   |
| 2021-05-04    | 2          | 20000   |
| 2021-01-08    | 1          | 4000    |
| 2021-12-18    | 2          | 10000   |
| 2021-10-30    | 2          | 10000   |
+---------------+------------+---------+
```
