# Source: https://docs.oxla.com/sql-reference/sql-functions/window-functions/count.md

# Source: https://docs.oxla.com/sql-reference/sql-functions/aggregate-functions/count.md

# Source: https://docs.oxla.com/sql-reference/sql-functions/window-functions/count.md

# Source: https://docs.oxla.com/sql-reference/sql-functions/aggregate-functions/count.md

# Source: https://docs.oxla.com/sql-reference/sql-functions/window-functions/count.md

# Source: https://docs.oxla.com/sql-reference/sql-functions/aggregate-functions/count.md

# COUNT

## Overview

The `COUNT()` function allows you to retrieve the number of records that match a specific condition. It can be used with any data type supported by Oxla, and the output will be returned as a `BIGINT`.

<Info>The output will indicate the total number of rows in a table, regardless of the input types.</Info>

## Examples

In this example, we will use an orders table that stores details of the purchase transactions:

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

### Case #1: `COUNT()` with a single expression

The following example will return the number of all orders in the orders table:

```sql  theme={null}
SELECT COUNT(*) FROM orders;
```

The final result will be as follows:

```sql  theme={null}
+-------+
| count |
+-------+
| 11    |
+-------+
```

### Case #2: `COUNT()` with a `GROUP BY` clause

This example will combine the `COUNT()` function and the `GROUP BY` clause.

* The `GROUP BY` clause groups the orders based on the customer’s name.
* The `COUNT()` function counts the orders for each customer.

```sql  theme={null}
SELECT custname, COUNT (orderid)
FROM orders
GROUP BY custname;
```

It will display the output as shown below:

```sql  theme={null}
+-----------+--------+
| custname  | count  |
+-----------+--------+
| Aaron     | 3      |
| Alex      | 2      |
| Will      | 3      |
| Maya      | 3      |
+-----------+--------+
```

### Case #3: `COUNT()` with a `HAVING` clause

In this example, we combine the `COUNT()` function and the `HAVING` clause to apply a specific condition to find customers who have made more than two orders:

```sql  theme={null}
SELECT custname, COUNT (orderid)
FROM orders
GROUP BY custname
HAVING COUNT (orderid) > 2;
```

* The `GROUP BY` clause groups the orders based on the customer’s name.
* The `HAVING` clause will filter only customers with more than two order IDs.
* The `COUNT()` function counts the orders for each customer.

```sql  theme={null}
+-----------+--------+
| custname  | count  |
+-----------+--------+
| Aaron     | 3      |
| Will      | 3      |
| Maya      | 3      |
+-----------+--------+
```
