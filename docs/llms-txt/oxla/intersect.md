# Source: https://docs.oxla.com/sql-reference/sql-clauses/set-operations/intersect.md

# INTERSECT

## INTERSECT

### Overview

The `INTERSECT` combines the result sets of two or more `SELECT` statements, retrieving only the common rows between them. Unlike `UNION`, which combines all rows and removes duplicates, `INTERSECT` focuses on returning rows that appear in all `SELECT` statements.

### Syntax

The syntax for the `INTERSECT` is as follows:

```sql  theme={null}
SELECT value1, value2, ... value_n
FROM table1
INTERSECT
SELECT value1, value2, ... value_n
FROM table2;
```

The parameters from the syntax are explained below:

* `value1, value2, ... value_n`: The columns you want to retrieve. You can also use `SELECT * FROM` to retrieve all columns.
* `table1, table2`: The tables from which you wish to retrieve records.

<Note>The data types of corresponding columns must be compatible.</Note>

### Example

Suppose you have two tables: `customers_old` and `customers_new`, containing customer data for different periods. You want to find the customers who are present in both tables:

```sql  theme={null}
CREATE TABLE customers_old (
    customer_id INT,
    customer_name TEXT
);

CREATE TABLE customers_new (
    customer_id INT,
    customer_name TEXT
);

INSERT INTO customers_old VALUES
(1, 'Alice'),
(2, 'Bob'),
(3, 'Charlie');

INSERT INTO customers_new VALUES
(2, 'Bob'),
(3, 'Charlie'),
(4, 'David');
```

Viewing the inserted values:

```sql  theme={null}
SELECT * FROM customers_old;
SELECT * FROM customers_new;
```

```sql  theme={null}
customer_id | customer_name
-------------+---------------
           1 | Alice
           2 | Bob
           3 | Charlie

 customer_id | customer_name
-------------+---------------
           2 | Bob
           3 | Charlie
           4 | David
```

Now, let’s combine common customers using the `INTERSECT`:

```sql  theme={null}
SELECT customer_name FROM customers_old
INTERSECT
SELECT customer_name FROM customers_new;
```

The result will include only the names that appear in both tables:&#x20;

```sql  theme={null}
customer_name
---------------
 Bob
 Charlie
```

The picture displays a list of customer names that appear in both tables. Only "Bob" and "Charlie" are found in both tables and shown as INTERSECT's final result.

<img className="block dark:hidden" src="https://mintcdn.com/oxla/0Js4fLL2Ovp7KANj/assets/images/light/intersect/intersect-one-light.png?fit=max&auto=format&n=0Js4fLL2Ovp7KANj&q=85&s=0ebd2e5b6cf048213703529520651ad1" alt="" data-og-width="2075" width="2075" data-og-height="1408" height="1408" data-path="assets/images/light/intersect/intersect-one-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/oxla/0Js4fLL2Ovp7KANj/assets/images/light/intersect/intersect-one-light.png?w=280&fit=max&auto=format&n=0Js4fLL2Ovp7KANj&q=85&s=17d33c6fe94781c7526e77e6a19cf06c 280w, https://mintcdn.com/oxla/0Js4fLL2Ovp7KANj/assets/images/light/intersect/intersect-one-light.png?w=560&fit=max&auto=format&n=0Js4fLL2Ovp7KANj&q=85&s=860e43c9fe92cfd2e2bb9f239ebe8cae 560w, https://mintcdn.com/oxla/0Js4fLL2Ovp7KANj/assets/images/light/intersect/intersect-one-light.png?w=840&fit=max&auto=format&n=0Js4fLL2Ovp7KANj&q=85&s=f0f8b71c8c35c1660a7f3a217b49726e 840w, https://mintcdn.com/oxla/0Js4fLL2Ovp7KANj/assets/images/light/intersect/intersect-one-light.png?w=1100&fit=max&auto=format&n=0Js4fLL2Ovp7KANj&q=85&s=d510003ba6f2a9bf77f99c65b1cd0465 1100w, https://mintcdn.com/oxla/0Js4fLL2Ovp7KANj/assets/images/light/intersect/intersect-one-light.png?w=1650&fit=max&auto=format&n=0Js4fLL2Ovp7KANj&q=85&s=0c81b9fe0438c0f19ecaab3a752f8304 1650w, https://mintcdn.com/oxla/0Js4fLL2Ovp7KANj/assets/images/light/intersect/intersect-one-light.png?w=2500&fit=max&auto=format&n=0Js4fLL2Ovp7KANj&q=85&s=fc5b50f20a80bf8c527ef033b74a6b4a 2500w" />

<img className="hidden dark:block" src="https://mintcdn.com/oxla/ONnYYkZc0LCcRiQR/assets/images/dark/intersect/intersect-one-dark.png?fit=max&auto=format&n=ONnYYkZc0LCcRiQR&q=85&s=56c16437ff963f1a7f7377a9b4dd3c23" alt="" data-og-width="2075" width="2075" data-og-height="1408" height="1408" data-path="assets/images/dark/intersect/intersect-one-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/oxla/ONnYYkZc0LCcRiQR/assets/images/dark/intersect/intersect-one-dark.png?w=280&fit=max&auto=format&n=ONnYYkZc0LCcRiQR&q=85&s=91c1b6e05820d7919b416154232d9a68 280w, https://mintcdn.com/oxla/ONnYYkZc0LCcRiQR/assets/images/dark/intersect/intersect-one-dark.png?w=560&fit=max&auto=format&n=ONnYYkZc0LCcRiQR&q=85&s=9b2ed3833f1000dbf20a11ec98342989 560w, https://mintcdn.com/oxla/ONnYYkZc0LCcRiQR/assets/images/dark/intersect/intersect-one-dark.png?w=840&fit=max&auto=format&n=ONnYYkZc0LCcRiQR&q=85&s=bd9e63ad31c5821c7e2f395beb96c1e4 840w, https://mintcdn.com/oxla/ONnYYkZc0LCcRiQR/assets/images/dark/intersect/intersect-one-dark.png?w=1100&fit=max&auto=format&n=ONnYYkZc0LCcRiQR&q=85&s=ee70c8ce30dfd1b2b5dda4cb5818857c 1100w, https://mintcdn.com/oxla/ONnYYkZc0LCcRiQR/assets/images/dark/intersect/intersect-one-dark.png?w=1650&fit=max&auto=format&n=ONnYYkZc0LCcRiQR&q=85&s=70ff5dc1a8b47d8fb286cce2bdb6e059 1650w, https://mintcdn.com/oxla/ONnYYkZc0LCcRiQR/assets/images/dark/intersect/intersect-one-dark.png?w=2500&fit=max&auto=format&n=ONnYYkZc0LCcRiQR&q=85&s=55b190c56c528b9107f140e97127542c 2500w" />

## INTERSECT ALL

### Overview

The `INTERSECT ALL` retrieves all common rows between two or more tables, including duplicates.

This means that if a row appears multiple times in any of the `SELECT` statements, it will be included in the final result set multiple times.

### Syntax

The syntax for `INTERSECT ALL` is similar to `INTERSECT`:

```sql  theme={null}
SELECT value1, value2, ... value_n
FROM tables
INTERSECT ALL
SELECT value1, value2, ... value_n
FROM tables;
```

The parameters from the syntax are explained below:

* `value1, value2, ... value_n`: The columns you wish to retrieve. You can also retrieve all the values using the `SELECT * FROM` query.
* `table1, table2`: The tables from which you want to retrieve records.

<Note>The data types of corresponding columns in the `SELECT` queries must be compatible.</Note>

### Example

Let’s create three tables of products from different years. You want to find the common products among all three categories, including duplicates.

```sql  theme={null}
CREATE TABLE products_electronics2021 (
    product_id INT,
    product_name TEXT
);

CREATE TABLE products_electronics2022 (
    product_id INT,
    product_name TEXT
);

CREATE TABLE products_electronics2023 (
    product_id INT,
    product_name TEXT
);

INSERT INTO products_electronics2021 VALUES
(1, 'Laptop'),
(2, 'Phone'),
(3, 'Tablet'),
(4, 'Headphones');

INSERT INTO products_electronics2022 VALUES
(2, 'TV'),
(3, 'Printer'),
(4, 'Monitor'),
(5, 'Phone');

INSERT INTO products_electronics2023 VALUES
(3, 'Laptop'),
(4, 'Phone'),
(5, 'Oven'),
(6, 'AC');
```

Display the tables using the query below:

```sql  theme={null}
SELECT * FROM products_electronics2021;
SELECT * FROM products_electronics2022;
SELECT * FROM products_electronics2023;
```

```sql  theme={null}
product_id | product_name
------------+--------------
          1 | Laptop
          2 | Phone
          3 | Tablet
          4 | Headphones

 product_id | product_name
------------+--------------
          2 | TV
          3 | Printer
          4 | Monitor
          5 | Phone

 product_id | product_name
------------+--------------
          3 | Laptop
          4 | Phone
          5 | Oven
          6 | AC
```

Then, combine common products from all three categories using the `INTERSECT ALL`:

```sql  theme={null}
SELECT product_name FROM products_electronics2021
INTERSECT ALL
SELECT product_name FROM products_electronics2022
INTERSECT ALL
SELECT product_name FROM products_electronics2023;
```

The result will include the products that are common among all three categories, including duplicates:

```sql  theme={null}
product_name
--------------
 Phone
```

The illustration shows a list of product names common to all three years, including duplicates. In this case, the result is the product name "Phone," which appears across all three tables.

<img className="block dark:hidden" src="https://mintcdn.com/oxla/0Js4fLL2Ovp7KANj/assets/images/light/intersect/intersect-two-light.png?fit=max&auto=format&n=0Js4fLL2Ovp7KANj&q=85&s=9c72ec83ac6f3670354e1e453f9b576b" alt="" data-og-width="2075" width="2075" data-og-height="2287" height="2287" data-path="assets/images/light/intersect/intersect-two-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/oxla/0Js4fLL2Ovp7KANj/assets/images/light/intersect/intersect-two-light.png?w=280&fit=max&auto=format&n=0Js4fLL2Ovp7KANj&q=85&s=74a9f2d1e3012996d9e32a62f3591457 280w, https://mintcdn.com/oxla/0Js4fLL2Ovp7KANj/assets/images/light/intersect/intersect-two-light.png?w=560&fit=max&auto=format&n=0Js4fLL2Ovp7KANj&q=85&s=b930534d467509042f55ca09615128c0 560w, https://mintcdn.com/oxla/0Js4fLL2Ovp7KANj/assets/images/light/intersect/intersect-two-light.png?w=840&fit=max&auto=format&n=0Js4fLL2Ovp7KANj&q=85&s=a715da104bd0de99b463d4cf25550809 840w, https://mintcdn.com/oxla/0Js4fLL2Ovp7KANj/assets/images/light/intersect/intersect-two-light.png?w=1100&fit=max&auto=format&n=0Js4fLL2Ovp7KANj&q=85&s=7ab4955c13ef47aeb1e9ceeb4c8d75e9 1100w, https://mintcdn.com/oxla/0Js4fLL2Ovp7KANj/assets/images/light/intersect/intersect-two-light.png?w=1650&fit=max&auto=format&n=0Js4fLL2Ovp7KANj&q=85&s=5e24c0a84f1209c1322298866d569268 1650w, https://mintcdn.com/oxla/0Js4fLL2Ovp7KANj/assets/images/light/intersect/intersect-two-light.png?w=2500&fit=max&auto=format&n=0Js4fLL2Ovp7KANj&q=85&s=feba7edf2553e30bee4d21b93a522ed7 2500w" />

<img className="hidden dark:block" src="https://mintcdn.com/oxla/ONnYYkZc0LCcRiQR/assets/images/dark/intersect/intersect-two-dark.png?fit=max&auto=format&n=ONnYYkZc0LCcRiQR&q=85&s=77314c300736c36c04b33b578165ef06" alt="" data-og-width="2075" width="2075" data-og-height="2287" height="2287" data-path="assets/images/dark/intersect/intersect-two-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/oxla/ONnYYkZc0LCcRiQR/assets/images/dark/intersect/intersect-two-dark.png?w=280&fit=max&auto=format&n=ONnYYkZc0LCcRiQR&q=85&s=e02b1622f1475f1f37b4875c551004f6 280w, https://mintcdn.com/oxla/ONnYYkZc0LCcRiQR/assets/images/dark/intersect/intersect-two-dark.png?w=560&fit=max&auto=format&n=ONnYYkZc0LCcRiQR&q=85&s=0311c2a70e233efaa287491518ea36cd 560w, https://mintcdn.com/oxla/ONnYYkZc0LCcRiQR/assets/images/dark/intersect/intersect-two-dark.png?w=840&fit=max&auto=format&n=ONnYYkZc0LCcRiQR&q=85&s=1dca9e129f9bde5b2e05f7d87e1cdca4 840w, https://mintcdn.com/oxla/ONnYYkZc0LCcRiQR/assets/images/dark/intersect/intersect-two-dark.png?w=1100&fit=max&auto=format&n=ONnYYkZc0LCcRiQR&q=85&s=cb505c27f55036f8fb536ad50132f8dc 1100w, https://mintcdn.com/oxla/ONnYYkZc0LCcRiQR/assets/images/dark/intersect/intersect-two-dark.png?w=1650&fit=max&auto=format&n=ONnYYkZc0LCcRiQR&q=85&s=b2ccd6712db6ce8139a034029ed4caf8 1650w, https://mintcdn.com/oxla/ONnYYkZc0LCcRiQR/assets/images/dark/intersect/intersect-two-dark.png?w=2500&fit=max&auto=format&n=ONnYYkZc0LCcRiQR&q=85&s=fc2237cc093046b487433505292601fa 2500w" />
