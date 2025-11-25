# Source: https://docs.oxla.com/sql-reference/sql-functions/string-functions/concat.md

# CONCAT

## Overview

The `CONCAT()` function is used to concatenate one or more input values into a single result. It supports all data types in Oxla, except `TIMESTAMPTZ`, and the output will be returned as a concatenation of the input values.

**Special cases:** Returns `NULL` if there are no input rows or `NULL` values.

## Examples

### Case 1: Basic `CONCAT()` function

The below example uses the `CONCAT()` function to concatenate three values = into a single result:

```sql  theme={null}
SELECT CONCAT ('Oxla', '.', 'com') AS "Website";
```

The final result will be as follows:

```sql  theme={null}
+------------+
| Website    |
+------------+
| Oxla.com   |
+------------+
```

### Case 2: `CONCAT()` function using column

We have an example of a **payment** table that stores customer payment data.

```sql  theme={null}
CREATE TABLE payment (
  paymentid int,
  custFirstName text,
  custLastName text,
  product text,
  ordertotal int
);
INSERT INTO payment
    (paymentid, custFirstName, custLastName, product, ordertotal)
VALUES
    (9557451,'Alex','Drue','Latte',2.10),
    (9557421,'Lana','Rey','Latte',2.10),
    (9557411,'Tom','Hanks','Americano',1.85),
    (9557351,'Maya','Taylor','Cappuccino',2.45),
    (9557321,'Smith','Jay','Cappuccino',2.45),
    (9557311,'Will','Ritchie','Americano',1.85);
```

```sql  theme={null}
SELECT * FROM payment;
```

The above query will display the following table:

```sql  theme={null}
+------------+----------------+----------------+--------------+---------------+
| paymentid  | custFirstName  | custLastName   | product      | ordertotal    |
+------------+----------------+----------------+--------------+---------------+
| 9557451    | Alex           | Drue           | Latte        | 2.10          |
| 9557421    | Lana           | Rey            | Latte        | 2.10          |
| 9557411    | Tom            | Hanks          | Americano    | 1.85          |
| 9557351    | Maya           | Taylor         | Cappuccino   | 2.45          |
| 9557321    | Smith          | Jay            | Cappuccino   | 2.45          |
| 9557311    | Will           | Ritchie        | Americano    | 1.85          |
+------------+----------------+----------------+--------------+---------------+
```

The following query will concatenate values in the `custFirstName` and `custLastName` columns of the **payment** table:

```sql  theme={null}
SELECT CONCAT  (custFirstName, ' ', custLastName) AS "Customer Name"
FROM payment;
```

It will display an output where spaces separate the first and last names.

```sql  theme={null}
+-----------------+
| Customer Name   |
+-----------------+
| Tom Hanks       |
| Lana Rey        |
| Alex Drue       |
| Will Ritchie    |
| Smith Jay       |
| Maya Taylor     |
+-----------------+
```

### Case 3: CONCAT() function with NULL

We use the `CONCAT()` function in the following example to concatenate a string with a `NULL` value:

```sql  theme={null}
SELECT CONCAT('Talent Source ',NULL) AS "concat";
```

The result shows that the `CONCAT` function will skip the `NULL` value:

```sql  theme={null}
+------------------+
| concat           |
+------------------+
| Talent Source    |
+------------------+
```
