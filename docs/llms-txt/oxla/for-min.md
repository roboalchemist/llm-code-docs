# Source: https://docs.oxla.com/sql-reference/sql-functions/aggregate-functions/for-min.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxla.com/llms.txt
> Use this file to discover all available pages before exploring further.

# FOR_MIN()

## Overview

The `FOR_MIN()` function is used to search for a minimum in a specific column and return a value related to that minimum from another column.

## Syntax

```sql  theme={null}
FOR_MIN(metric, value)
```

## Arguments

* `metric`: must be one of the following data types: `INT`, `LONG`, `FLOAT`, `DOUBLE`, `DATE` or `TIMESTAMP`
* `value`: can be any data type except `TEXT`

The `FOR_MIN()` function returns `NULL` in the following situations:

* There are no input rows
* The `metric` column contains only `NULL` values
* The `value` corresponding to the metric minimum value is `NULL`

This function also returns `NaN` (not-a-number) if the input contains a `NaN`.

## Examples

For the needs of this section, we will use a `payment` table that stores customer payment records, including any applied discounts:

```sql  theme={null}
CREATE TABLE payments (
  paymentid int,
  customer_name text,
  price real,
  discount real);

INSERT INTO
  payments (paymentid, customer_name, price, discount)
VALUES
  (1, 'Alex', 280.12, 0.1),
  (2, NULL, 35.75, NULL),
  (3, 'Alex', 45.1, 0.05),
  (4, 'Alex', NULL, 0.4),
  (5, 'John', NULL, 0.1),
  (6, 'Bob', 50.45, 0.07),
  (7, 'Bob', 120.5, 0.0);
```

To view the `payments` table content, run the following query:

```sql  theme={null}
SELECT * FROM payments;
```

```sql  theme={null}
 paymentid | customer_name | price  | discount 
-----------+---------------+--------+----------
         1 | Alex          | 280.12 |      0.1
         2 |               |  35.75 |         
         3 | Alex          |   45.1 |     0.05
         4 | Alex          |        |      0.4
         5 | John          |        |      0.1
         6 | Bob           |  50.45 |     0.07
         7 | Bob           |  120.5 |        0
(7 rows)
```

### `FOR_MIN()` basic usage

To determine the price associated with the lowest discount applied across all payments, use the following query:

```sql  theme={null}
SELECT FOR_MIN(discount, price) AS for_lowest_discount FROM payments;
```

This query returns the following output:

```sql  theme={null}
 for_lowest_discount 
---------------------
               120.5
(1 row)
```

### `FOR_MIN()` with `GROUP BY` clause

To determine the discount associated with the lowest price paid by each customer, we will use the `GROUP BY` clause with `FOR_MIN()` function:

```sql  theme={null}
SELECT customer_name,
  FOR_MIN(price, discount) AS discount
FROM payments
GROUP BY customer_name;
```

This query returns the following output:

```sql  theme={null}
customer_name | discount
---------------+----------
 Bob           |     0.07
 Alex          |     0.05
               |
 John          |
(4 rows)
```
