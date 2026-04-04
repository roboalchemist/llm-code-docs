# Source: https://docs.oxla.com/sql-reference/sql-clauses/set-operations/union.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxla.com/llms.txt
> Use this file to discover all available pages before exploring further.

# UNION

## UNION

### Overview

The `UNION` combines the result sets of 2 or more select statements, removing duplicate rows between the tables.

### Syntax

Below is the syntax of the `UNION`:

```sql  theme={null}
SELECT value1, value2, ... value_n
FROM table1
UNION
SELECT value1, value2, ... value_n
FROM table2;
```

The parameters from the syntax are explained below:

* `value1, value2, ... value_n`: The columns you wish to retrieve. You can also retrieve all the values using the `SELECT * FROM` query.

* `table1, table2`: The tables that you wish to retrieve records from.

<Tip>**Things to consider:**<br /> 1.  The data types of corresponding columns in the `SELECT` queries must be compatible. <br /> 2.  The order of columns is flexible as long as the columns in consecutive places are pairwise compatible. For example, you can do `SELECT col1, col2 FROM table1 UNION SELECT col2, col1 FROM table2`.</Tip>

### Example

Let's consider an example of the `UNION`. Assume we have a table called `employees` and another table called `contractors`. We want to retrieve a combined list of names from both tables, excluding duplicates:

```sql  theme={null}
CREATE TABLE employees (
    emp_id INT,
    emp_name TEXT
);

CREATE TABLE contractors (
    contractor_id INT,
    contractor_name TEXT
);

INSERT INTO employees VALUES
(1, 'John'),
(2, 'Alice'),
(3, 'Bob');

INSERT INTO contractors VALUES
(101, 'Alice'),
(102, 'Eve'),
(103, 'Tom');
```

Verifying inserted values by using the `SELECT` statement:

```sql  theme={null}
SELECT * FROM employees;
SELECT * FROM contractors;
```

```sql  theme={null}
emp_id | emp_name
--------+----------
      1 | John
      2 | Alice
      3 | Bob

 contractor_id | contractor_name
---------------+-----------------
           101 | Alice
           102 | Eve
           103 | Tom
```

Let’s combine the values from the tables:

```sql  theme={null}
SELECT emp_name FROM employees
UNION
SELECT contractor_name FROM contractors;
```

You will get the values of both tables, and there won’t be any duplicate values.

```sql  theme={null}
emp_name
----------
 Alice
 Bob
 Eve
 John
 Tom
```

The diagram below shows that the duplicate name "Alice" is represented only once in the output, fulfilling the requirement to avoid duplicate entries.

<img className="block dark:hidden" src="https://mintcdn.com/oxla/0Js4fLL2Ovp7KANj/assets/images/light/union/union-one-light.png?fit=max&auto=format&n=0Js4fLL2Ovp7KANj&q=85&s=f4401879d67660f2de71f908bcaf56c8" alt="" data-og-width="2075" width="2075" data-og-height="1408" height="1408" data-path="assets/images/light/union/union-one-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/oxla/0Js4fLL2Ovp7KANj/assets/images/light/union/union-one-light.png?w=280&fit=max&auto=format&n=0Js4fLL2Ovp7KANj&q=85&s=c94e24e2e93ad152864ffbdcf2e6414f 280w, https://mintcdn.com/oxla/0Js4fLL2Ovp7KANj/assets/images/light/union/union-one-light.png?w=560&fit=max&auto=format&n=0Js4fLL2Ovp7KANj&q=85&s=9b6cf65551541f8e2f9983419027f3f6 560w, https://mintcdn.com/oxla/0Js4fLL2Ovp7KANj/assets/images/light/union/union-one-light.png?w=840&fit=max&auto=format&n=0Js4fLL2Ovp7KANj&q=85&s=7ab5b221698bf3a9e6cfabf0926d0f40 840w, https://mintcdn.com/oxla/0Js4fLL2Ovp7KANj/assets/images/light/union/union-one-light.png?w=1100&fit=max&auto=format&n=0Js4fLL2Ovp7KANj&q=85&s=be6be496f809f8d140ee2de5069ad850 1100w, https://mintcdn.com/oxla/0Js4fLL2Ovp7KANj/assets/images/light/union/union-one-light.png?w=1650&fit=max&auto=format&n=0Js4fLL2Ovp7KANj&q=85&s=4f576859ecf2bd3bd3941d8964927d46 1650w, https://mintcdn.com/oxla/0Js4fLL2Ovp7KANj/assets/images/light/union/union-one-light.png?w=2500&fit=max&auto=format&n=0Js4fLL2Ovp7KANj&q=85&s=1b4fc4f8c0b0d5885ae2ed746031bf9c 2500w" />

<img className="hidden dark:block" src="https://mintcdn.com/oxla/scqzK0laaaAr3oxU/assets/images/dark/union/union-one-dark.png?fit=max&auto=format&n=scqzK0laaaAr3oxU&q=85&s=4bb9156c24db69ec2b32948882fb040e" alt="" data-og-width="2075" width="2075" data-og-height="1408" height="1408" data-path="assets/images/dark/union/union-one-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/oxla/scqzK0laaaAr3oxU/assets/images/dark/union/union-one-dark.png?w=280&fit=max&auto=format&n=scqzK0laaaAr3oxU&q=85&s=80863d70887da9056b67723387808156 280w, https://mintcdn.com/oxla/scqzK0laaaAr3oxU/assets/images/dark/union/union-one-dark.png?w=560&fit=max&auto=format&n=scqzK0laaaAr3oxU&q=85&s=5b7366e55fac4d279af7c88b53aa181b 560w, https://mintcdn.com/oxla/scqzK0laaaAr3oxU/assets/images/dark/union/union-one-dark.png?w=840&fit=max&auto=format&n=scqzK0laaaAr3oxU&q=85&s=15f27485bcf7096e26ee7edc0cb1d5a7 840w, https://mintcdn.com/oxla/scqzK0laaaAr3oxU/assets/images/dark/union/union-one-dark.png?w=1100&fit=max&auto=format&n=scqzK0laaaAr3oxU&q=85&s=57cffb4ed2b5c3b30ae5df0c58f04d0f 1100w, https://mintcdn.com/oxla/scqzK0laaaAr3oxU/assets/images/dark/union/union-one-dark.png?w=1650&fit=max&auto=format&n=scqzK0laaaAr3oxU&q=85&s=3f18640e9eb96690b15dd660a8c304ac 1650w, https://mintcdn.com/oxla/scqzK0laaaAr3oxU/assets/images/dark/union/union-one-dark.png?w=2500&fit=max&auto=format&n=scqzK0laaaAr3oxU&q=85&s=745ebb6917010ce6c447ef22cd40d735 2500w" />

## UNION ALL

### Overview

The `UNION ALL` combines the result sets of 2 or more select statements, returning all rows from the query and not removing duplicate rows between the tables.

### Syntax

Below is the syntax of the `UNION ALL`:

```sql  theme={null}
SELECT value1, value2, ... value_n
FROM tables
UNION ALL
SELECT value1, value2, ... value_n
FROM tables;
```

The parameters from the syntax are explained below:

* `value1, value2, ... value_n`: The columns you wish to retrieve. You can also retrieve all the values using the `SELECT * FROM` query.
* `table1, table2`: The tables that you wish to retrieve records from.

<Tip>**Things to consider:**<br /> 1. The data types of corresponding columns in the `SELECT` queries must be compatible. <br /> 2. The order of columns is flexible as long as the columns in consecutive places are pairwise compatible.</Tip>

### Example

Suppose you have two separate tables, `sales_2022` and `sales_2023`, containing sales data for different years. You want to combine the sales data from both tables to get a complete list of sales transactions without removing duplicates.

```sql  theme={null}
CREATE TABLE sales_2022 (
    transaction_id INT,
    product_name TEXT,
    sale_amount INT
);

CREATE TABLE sales_2023 (
    transaction_id INT,
    product_name TEXT,
    sale_amount INT
);

INSERT INTO sales_2022 VALUES
(1, 'Product A', 1000),
(2, 'Product B', 500),
(3, 'Product C', 750);

INSERT INTO sales_2023 VALUES
(4, 'Product A', 1200),
(5, 'Product D', 800),
(6, 'Product E', 950);
```

Verifying inserted values by using the `SELECT` statement:

```sql  theme={null}
SELECT * FROM sales_2022;
SELECT * FROM sales_2023;
```

```sql  theme={null}
transaction_id | product_name | sale_amount
----------------+--------------+-------------
              1 | Product A    |        1000
              2 | Product B    |         500
              3 | Product C    |         750

 transaction_id | product_name | sale_amount
----------------+--------------+-------------
              4 | Product A    |        1200
              5 | Product D    |         800
              6 | Product E    |         950
```

Let’s combine all values from the tables by using the `UNION ALL`:

```sql  theme={null}
SELECT product_name, sale_amount FROM sales_2022 UNION ALL SELECT product_name, sale_amount FROM sales_2023;
```

In this case, it will display all the values of the first table followed by all the contents of the second table.

```sql  theme={null}
product_name | sale_amount
--------------+-------------
 Product A    |        1000
 Product B    |         500
 Product C    |         750
 Product A    |        1200
 Product D    |         800
 Product E    |         950
```

The diagram illustrates that with the `UNION ALL`, all values are displayed, including the duplicate ones.&#x20;

<img className="block dark:hidden" src="https://mintcdn.com/oxla/0Js4fLL2Ovp7KANj/assets/images/light/union/union-two-light.png?fit=max&auto=format&n=0Js4fLL2Ovp7KANj&q=85&s=771bda62363bc880ed06ab8e92c8314b" alt="" data-og-width="2075" width="2075" data-og-height="1408" height="1408" data-path="assets/images/light/union/union-two-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/oxla/0Js4fLL2Ovp7KANj/assets/images/light/union/union-two-light.png?w=280&fit=max&auto=format&n=0Js4fLL2Ovp7KANj&q=85&s=5f6a02869928f42271b19fa1c136f557 280w, https://mintcdn.com/oxla/0Js4fLL2Ovp7KANj/assets/images/light/union/union-two-light.png?w=560&fit=max&auto=format&n=0Js4fLL2Ovp7KANj&q=85&s=83e17e8f34e1063a618a71b17c9a01ad 560w, https://mintcdn.com/oxla/0Js4fLL2Ovp7KANj/assets/images/light/union/union-two-light.png?w=840&fit=max&auto=format&n=0Js4fLL2Ovp7KANj&q=85&s=a04c385054a26088f5af7ce7b41ba04a 840w, https://mintcdn.com/oxla/0Js4fLL2Ovp7KANj/assets/images/light/union/union-two-light.png?w=1100&fit=max&auto=format&n=0Js4fLL2Ovp7KANj&q=85&s=db00ac8edadc88e2a5628eafba960604 1100w, https://mintcdn.com/oxla/0Js4fLL2Ovp7KANj/assets/images/light/union/union-two-light.png?w=1650&fit=max&auto=format&n=0Js4fLL2Ovp7KANj&q=85&s=a0e73b5be38a903646bffe35a4c7076c 1650w, https://mintcdn.com/oxla/0Js4fLL2Ovp7KANj/assets/images/light/union/union-two-light.png?w=2500&fit=max&auto=format&n=0Js4fLL2Ovp7KANj&q=85&s=a44603f7d696e446e46d87d214c2ff3e 2500w" />

<img className="hidden dark:block" src="https://mintcdn.com/oxla/scqzK0laaaAr3oxU/assets/images/dark/union/union-two-dark.png?fit=max&auto=format&n=scqzK0laaaAr3oxU&q=85&s=d23377ccb096b06c9542ade314111319" alt="" data-og-width="2075" width="2075" data-og-height="1408" height="1408" data-path="assets/images/dark/union/union-two-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/oxla/scqzK0laaaAr3oxU/assets/images/dark/union/union-two-dark.png?w=280&fit=max&auto=format&n=scqzK0laaaAr3oxU&q=85&s=4ff6da8b3883c98302112821526c0764 280w, https://mintcdn.com/oxla/scqzK0laaaAr3oxU/assets/images/dark/union/union-two-dark.png?w=560&fit=max&auto=format&n=scqzK0laaaAr3oxU&q=85&s=130886327af2c0e54b3fbe323135bfce 560w, https://mintcdn.com/oxla/scqzK0laaaAr3oxU/assets/images/dark/union/union-two-dark.png?w=840&fit=max&auto=format&n=scqzK0laaaAr3oxU&q=85&s=1a2a4752c67dab373dfc857be9e7fc95 840w, https://mintcdn.com/oxla/scqzK0laaaAr3oxU/assets/images/dark/union/union-two-dark.png?w=1100&fit=max&auto=format&n=scqzK0laaaAr3oxU&q=85&s=0c71fa7adf0cc2ed9513a887135460bc 1100w, https://mintcdn.com/oxla/scqzK0laaaAr3oxU/assets/images/dark/union/union-two-dark.png?w=1650&fit=max&auto=format&n=scqzK0laaaAr3oxU&q=85&s=c408ae57bdbbd04365f5b201fde91e7c 1650w, https://mintcdn.com/oxla/scqzK0laaaAr3oxU/assets/images/dark/union/union-two-dark.png?w=2500&fit=max&auto=format&n=scqzK0laaaAr3oxU&q=85&s=136084288f3ec81c52b413ac6f5cc2d2 2500w" />
