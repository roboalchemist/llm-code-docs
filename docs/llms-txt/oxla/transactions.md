# Source: https://docs.oxla.com/sql-reference/transactions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxla.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Transactions

## Overview

The transactions are supported only on the syntax level to allow integration with tools that requires it. While the syntax is accepted, all the queries are executed immediately and with no transactional guarantees.

## Commands

These commands are used to manage transactions:

### BEGIN

Initiates a new transaction by calling one of the syntax below.

<CodeGroup>
  ```sql BEGIN theme={null}
  BEGIN;
  ```

  ```sql BEGIN TRANSACTION theme={null}
  BEGIN TRANSACTION;
  ```
</CodeGroup>

### COMMIT

Saves the changes made in a transaction to the database. It simply ends the transaction.
<br /> Call one of the syntax below.

<CodeGroup>
  ```sql COMMIT theme={null}
  COMMIT;
  ```

  ```sql END TRANSACTION theme={null}
  END TRANSACTION;
  ```
</CodeGroup>

### ROLLBACK

In Oxla, when you issue a ROLLBACK command, it doesn't undo changes made in the current transaction. It simply finishes the transaction without any rollback action.

```sql  theme={null}
ROLLBACK;
```

## Example

1. Let's define a table named `products` with columns: `product_name`, `price`, and `stock_quantity`.

```sql  theme={null}
CREATE TABLE productsnew(
    product_name TEXT,
    price INT,
    stock_quantity INT
);
```

Upon successful creation, you will get the output below.

```sql  theme={null}
CREATE
```

2. Next, we want to insert product data into the `products` table.

<Info>
  * Transactions can only contain either multiple `SELECT` statements or a single non-SELECT one
  * The `INSERT` statement is executed immediately without waiting for the transaction to finish or a `COMMIT` to be issued
</Info>

```sql  theme={null}
BEGIN;
INSERT INTO productsnew(product_name, price, stock_quantity) VALUES ('Tab', 8000, 20);
```

By exectuing the code above, you will get the following output:

```sql  theme={null}
BEGIN
INSERT 0 1
```

3. View the changes by displaying the products table:

```sql  theme={null}
SELECT * FROM productsnew;
COMMIT;
```

The product data is now added to the table.

```sql  theme={null}
 product_name | price | stock_quantity 
--------------+-------+----------------
 Harddisk     | 12000 |             14
(1 row)

COMMIT
```
