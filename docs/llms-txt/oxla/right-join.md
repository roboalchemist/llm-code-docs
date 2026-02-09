# Source: https://docs.oxla.com/sql-reference/sql-clauses/from/right-join.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxla.com/llms.txt
> Use this file to discover all available pages before exploring further.

# RIGHT JOIN

## Overview

The `RIGHT JOIN` returns **all** matching records from the right table combined with the left table. Even if there are no match records in the left table, the `RIGHT JOIN` will still return a row in the result, but with `NULL` in each column from the left table.

<Tip>We support table aliasing used in the `RIGHT JOIN` clause.</Tip>

## Syntax

### a) Basic Syntax

```sql  theme={null}
SELECT column_1, column_2...
FROM table_1
RIGHT JOIN table_2
ON table_1.matching_field = table2.matching_field;
```

In the above syntax:

1. `SELECT column_1, column_2...` defines the **columns** from both tables where we want to display data.
2. `FROM table_1`, defines the **left table** with table\_1 in the FORM clause.
3. `RIGHT JOIN table_2` defines the **right table** with table\_2 in the RIGHT JOIN condition.
4. `ON table_1.matching_field = table2.matching_field` sets the join condition after the **ON** keyword with the matching field between the two tables.

### b) Syntax with an Alias

You can use an alias to refer to the table’s name. The results will stay the same. It only helps to write the query easier.

```sql  theme={null}
SELECT A.column_1, B.column_2...
FROM table_1 A //table_1 as A
RIGHT JOIN table_2 B //table_2 as B
ON A.matching_field = B.matching_field;
```

## Example

**customer table**

```sql  theme={null}
CREATE TABLE customer (
  id int NOT NULL,
  customer_name text
);

INSERT INTO customer
    (id, customer_name)
VALUES
    (201011,'James'),
    (200914,'Harry'),
    (201029,'Ellie'),
    (201925,'Mary');
```

```sql  theme={null}
SELECT * FROM customer;
```

It will create a table as shown below:

```sql  theme={null}
+-----------+----------------+
| id        | customer_name  |
+-----------+----------------+
| 201011    | James          |
| 200914    | Harry          |
| 201029    | Ellie          |
| 201925    | Mary           |
+-----------+----------------+
```

**orders table**

```sql  theme={null}
CREATE TABLE orders (
  order_id int NOT NULL,
  order_date date,
  order_amount int,
  customer_id int
);

INSERT INTO orders
    (order_id, order_date, order_amount, customer_id)
VALUES
    (181893,'2021-10-08',3000,201029),
    (181894,'2021-11-18',2000,201029),
    (181891,'2021-10-08',9000,201011),
    (181892,'2021-10-08',7000,201925),
    (181897,'2021-10-08',6000,null),
    (181899,'2021-10-08',4500,201011);
```

```sql  theme={null}
SELECT * FROM orders;
```

It will create a table as shown below:

```sql  theme={null}
+------------+------------------+---------------+-------------+
| order_id   | order_date       | order_amount  | customer_id |
+------------+------------------+---------------+-------------+
| 181893     | 2021-10-08       | 3000          | 201029      |
| 181894     | 2021-11-18       | 2000          | 201029      |
| 181891     | 2021-09-10       | 9000          | 201011      |
| 181892     | 2021-10-10       | 7000          | 201925      |
| 181897     | 2022-05-27       | 6700          | null        |
| 181899     | 2021-07-22       | 4500          | 201011      |
+------------+------------------+---------------+-------------+
```

***

1. Based on the above tables, we can write a `RIGHT JOIN` query as follows:

```sql  theme={null}
SELECT customer_name, order_date, order_amount
FROM customer
RIGHT JOIN orders
ON customer.id = orders.customer_id;
```

* The **customer**= left table and the **orders** = right table.
* Then it combines the values from the **orders** table using the **customer\_id** and matches the records using the **id** column from the **customer** table.
* If the records are equal, a new row will be created with `customer_name` and `order_amount` columns as defined in the `SELECT` clause.
* **ELSE** will still create a new row with a `NULL` value from the left table (**customer**).

2. The above query will give the following result:

```sql  theme={null}
+------------------+----------------+-----------------+
| customer_name    | order_date     | order_amount    |
+------------------+----------------+-----------------+
| James            | 2021-09-10     | 9000            |
| James            | 2021-07-22     | 4500            |
| Ellie            | 2021-10-08     | 3000            |
| Ellie            | 2021-11-18     | 2000            |
| Mary             | 2021-10-10     | 7000            |
| null             | 2022-05-27     | 6700            |
+------------------+----------------+-----------------+
```

Based on the data from the **customer** and **orders** tables:

* The order id: `181893` matches the customer: `Ellie.`
* The order id: `181894` matches the customer: `Ellie`.
* The order id: `181891` matches the customer: `James`.
* The order id: `181899` matches the customer: `James`.
* The order id: `181892` matches the customer: `Mary`.
* The order id: `181897` doesn’t match with any customer. Thus the customer\_name column is filled with: `null`.

<Info>A **customer** can have zero or many **orders**. An item from **orders** belongs to zero or one **customer**.</Info>

The following Venn diagram illustrates the `RIGHT JOIN`:

<img className="block dark:hidden" src="https://mintcdn.com/oxla/0Js4fLL2Ovp7KANj/assets/images/light/rightjoin/rightjoin-light.png?fit=max&auto=format&n=0Js4fLL2Ovp7KANj&q=85&s=b753a16f351e9f2d3e955816b8d5e49d" alt="" data-og-width="1822" width="1822" data-og-height="1409" height="1409" data-path="assets/images/light/rightjoin/rightjoin-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/oxla/0Js4fLL2Ovp7KANj/assets/images/light/rightjoin/rightjoin-light.png?w=280&fit=max&auto=format&n=0Js4fLL2Ovp7KANj&q=85&s=945bff1055c19243ea7b5af4e2738387 280w, https://mintcdn.com/oxla/0Js4fLL2Ovp7KANj/assets/images/light/rightjoin/rightjoin-light.png?w=560&fit=max&auto=format&n=0Js4fLL2Ovp7KANj&q=85&s=4186e58b95915dda9808e38b0eb87ba6 560w, https://mintcdn.com/oxla/0Js4fLL2Ovp7KANj/assets/images/light/rightjoin/rightjoin-light.png?w=840&fit=max&auto=format&n=0Js4fLL2Ovp7KANj&q=85&s=2d0bc384da7798e458f1b1ae92fb43c7 840w, https://mintcdn.com/oxla/0Js4fLL2Ovp7KANj/assets/images/light/rightjoin/rightjoin-light.png?w=1100&fit=max&auto=format&n=0Js4fLL2Ovp7KANj&q=85&s=cba2a45f66d969be18fea390cbc4b0f7 1100w, https://mintcdn.com/oxla/0Js4fLL2Ovp7KANj/assets/images/light/rightjoin/rightjoin-light.png?w=1650&fit=max&auto=format&n=0Js4fLL2Ovp7KANj&q=85&s=ce0e06c6e9b78dae7e30bdee001fa270 1650w, https://mintcdn.com/oxla/0Js4fLL2Ovp7KANj/assets/images/light/rightjoin/rightjoin-light.png?w=2500&fit=max&auto=format&n=0Js4fLL2Ovp7KANj&q=85&s=cd44744bb561f57af575d9dab34a6044 2500w" />

<img className="hidden dark:block" src="https://mintcdn.com/oxla/ONnYYkZc0LCcRiQR/assets/images/dark/rightjoin/rightjoin-dark.png?fit=max&auto=format&n=ONnYYkZc0LCcRiQR&q=85&s=8f4d2f5a2ac5e5cfa45e62d241000693" alt="" data-og-width="1822" width="1822" data-og-height="1409" height="1409" data-path="assets/images/dark/rightjoin/rightjoin-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/oxla/ONnYYkZc0LCcRiQR/assets/images/dark/rightjoin/rightjoin-dark.png?w=280&fit=max&auto=format&n=ONnYYkZc0LCcRiQR&q=85&s=b47fc41ec973740c403950ba0557b367 280w, https://mintcdn.com/oxla/ONnYYkZc0LCcRiQR/assets/images/dark/rightjoin/rightjoin-dark.png?w=560&fit=max&auto=format&n=ONnYYkZc0LCcRiQR&q=85&s=b4613c72a5ae5d246b17bdcaab28bb5b 560w, https://mintcdn.com/oxla/ONnYYkZc0LCcRiQR/assets/images/dark/rightjoin/rightjoin-dark.png?w=840&fit=max&auto=format&n=ONnYYkZc0LCcRiQR&q=85&s=b24e955d9fabcda58cdef156c356b5f6 840w, https://mintcdn.com/oxla/ONnYYkZc0LCcRiQR/assets/images/dark/rightjoin/rightjoin-dark.png?w=1100&fit=max&auto=format&n=ONnYYkZc0LCcRiQR&q=85&s=66541e19fb3d5360a09aefd25c897dba 1100w, https://mintcdn.com/oxla/ONnYYkZc0LCcRiQR/assets/images/dark/rightjoin/rightjoin-dark.png?w=1650&fit=max&auto=format&n=ONnYYkZc0LCcRiQR&q=85&s=3ab1046d0ddfb231b9c690ff5dd94479 1650w, https://mintcdn.com/oxla/ONnYYkZc0LCcRiQR/assets/images/dark/rightjoin/rightjoin-dark.png?w=2500&fit=max&auto=format&n=ONnYYkZc0LCcRiQR&q=85&s=90b23b68fef7688147ebdcdf714d2c01 2500w" />
