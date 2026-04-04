# Source: https://docs.oxla.com/sql-reference/sql-functions/window-functions/avg.md

# Source: https://docs.oxla.com/sql-reference/sql-functions/aggregate-functions/avg.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxla.com/llms.txt
> Use this file to discover all available pages before exploring further.

# AVG

## Overview

The `AVG()` function lets you calculate the average value of records. The input and return types we support can be seen in the table below:

| Input type         | Return type        |
| ------------------ | ------------------ |
| `INTEGER`          | `DOUBLE PRECISION` |
| `BIGINT`           | `DOUBLE PRECISION` |
| `REAL`             | `DOUBLE PRECISION` |
| `DOUBLE PRECISION` | `DOUBLE PRECISION` |

<Info>If the input type is 32-bit, then the result will be 64-bit</Info>

**Special cases:** Returns NaN if the input contains a NaN.

## Examples

In this example, we will use an **orders** table that stores details of the purchase transactions:

```sql  theme={null}
CREATE TABLE orders (
    orderid int,
    custname text,
    orderproduct text,
    ordertotal real
);
INSERT INTO orders (orderid, custname, orderproduct, ordertotal)
VALUES
(9557411, 'Maya', 'Jeans', 10.5),
(9557421, 'Aaron', 'T-Shirt', 9.2),
(9557451, 'Alex', 'Hat', 10.8),
(9557311, 'Will', 'Hat', 8.5),
(9557321, 'Will', 'T-Shirt', 12.15),
(9557351, 'Maya', 'T-Shirt', 9.5),
(9557221, 'Maya', 'Jeans', 11.02),
(9557251, 'Alex', 'Jeans', 11.09),
(9557231, 'Aaron', 'Hat', 14.56),
(9557281, 'Aaron', 'Hat', 12.15),
(9557291, 'Will', 'T-Shirt', 13.1);
```

```sql  theme={null}
SELECT * FROM orders;
```

The above query will show the following table:

```sql  theme={null}
+----------+-----------+---------------+-------------+
| orderid  | custname  | orderproduct  | ordertotal  |
+----------+-----------+---------------+-------------+
| 9557411  | Maya      | Jeans         | 10.5        |
| 9557421  | Aaron     | T-Shirt       | 9.2         |
| 9557451  | Alex      | Hat           | 10.8        |
| 9557311  | Will      | Hat           | 8.5         |
| 9557321  | Will      | T-Shirt       | 12.15       |
| 9557351  | Maya      | T-Shirt       | 9.5         |
| 9557221  | Maya      | Jeans         | 11.02       |
| 9557251  | Alex      | Jeans         | 11.09       |
| 9557231  | Aaron     | Hat           | 14.56       |
| 9557281  | Aaron     | Hat           | 12.15       |
| 9557291  | Will      | T-Shirt       | 13.1        |
+----------+-----------+---------------+-------------+
```

### AVG() with a single expression

In the first example, we want to calculate the average amount of all orders that customers have paid:

```sql  theme={null}
SELECT AVG(ordertotal) AS "Order Total Average"
FROM orders;
```

It will return the following output:

```sql  theme={null}
+---------------------+
| Order Total Average |
+---------------------+
| 11.142727331681685  |
+---------------------+
```

### AVG() with a GROUP BY clause

The following example uses the `AVG()` function and `GROUP BY` clause to calculate the average amount paid by each customer:

* First, the `GROUP BY` clause divides orders into groups based on customers

* Then, the `AVG` function is applied to each group.

```sql  theme={null}
SELECT custname AS "Customer", AVG (ordertotal) AS "Total Price Average"
FROM orders
GROUP BY custname;
```

It will display the output as shown below:

```sql  theme={null}
+-----------+----------------------+
| Customer  | Total Price Average  |
+-----------+----------------------+
| Aaron     | 11.96999994913737    |
| Alex      | 10.945000171661377   |
| Will      | 11.25                |
| Maya      | 10.34000015258789    |
+-----------+----------------------+
```

You can use the cast operator like`::NUMERIC(10,2)` to add two decimal numbers after the comma:

```sql  theme={null}
SELECT custname AS "Customer", AVG (ordertotal)::NUMERIC(10,2) AS "Total Price Average"
FROM orders
GROUP BY custname;
```

The result will trim and round two numbers after the comma:

```sql  theme={null}
+-----------+----------------------+
| Customer  | Total Price Average  |
+-----------+----------------------+
| Aaron     | 11.97                |
| Alex      | 10.95                |
| Will      | 11.25                |
| Maya      | 10.34                |
+-----------+----------------------+
``
```
