# Source: https://docs.oxla.com/sql-reference/sql-clauses/set-operations/except.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxla.com/llms.txt
> Use this file to discover all available pages before exploring further.

# EXCEPT

## EXCEPT

### Overview

The `EXCEPT` combines the result sets of two or more tables and retrieves rows specific to the first `SELECT` statement but not present in the subsequent ones.

### Syntax

The syntax for the `EXCEPT` is as follows:

```sql  theme={null}
SELECT value1, value2, ... value_n
FROM table1
EXCEPT
SELECT value1, value2, ... value_n
FROM table2;
```

The parameters from the syntax are explained below:

* `value1, value2, ... value_n`: The columns you want to retrieve.
* `table1, table2`: The tables from which you wish to retrieve records.

### Example

Let's assume you have two tables: `vehicles` and `vehicles1`. You want to find the vehicle which was present in 2021 but is not present in 2022:

```sql  theme={null}
CREATE TABLE vehicles (
    vhc_id INT,
    vhc_name TEXT
);

CREATE TABLE vehicles1 (
    vhc_id INT,
    vhc_name TEXT
);

INSERT INTO vehicles VALUES
(1, 'Truck'),
(2, 'Car'),
(3, 'Motorcycle');

INSERT INTO vehicles1 VALUES
(2, 'Car'),
(3, 'Bus'),
(4, 'Motorcycle');
```

Display the tables with the query below:

```sql  theme={null}
SELECT * FROM vehicles;
SELECT * FROM vehicles1;
```

```sql  theme={null}
vhc_id |  vhc_name
--------+------------
      1 | Truck
      2 | Car
      3 | Motorcycle

 vhc_id |  vhc_name
--------+------------
      2 | Car
      3 | Bus
      4 | Motorcycle
```

Using the `EXCEPT` to find employees present in 2021 but not in 2022:

```sql  theme={null}
SELECT vhc_name FROM vehicles
EXCEPT
SELECT vhc_name FROM vehicles1;
```

The result will include the names of employees who were present in 2021 but are not present in 2022:

```sql  theme={null}
vhc_name
----------
 Truck
```

From the diagram below, we learn that the result is a list of vehicle names present in the first table (`vehicles`) but not found in the second table (`vehicles1`). In this case, the result is the vehicle name "Truck."

<img className="block dark:hidden" src="https://mintcdn.com/oxla/scqzK0laaaAr3oxU/assets/images/light/except/except-one-light.png?fit=max&auto=format&n=scqzK0laaaAr3oxU&q=85&s=b6ed121c0db8ca71143c2e9c6e65c14b" alt="" data-og-width="2075" width="2075" data-og-height="1409" height="1409" data-path="assets/images/light/except/except-one-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/oxla/scqzK0laaaAr3oxU/assets/images/light/except/except-one-light.png?w=280&fit=max&auto=format&n=scqzK0laaaAr3oxU&q=85&s=da4d4ee63f764d49d39743cfbc4d793a 280w, https://mintcdn.com/oxla/scqzK0laaaAr3oxU/assets/images/light/except/except-one-light.png?w=560&fit=max&auto=format&n=scqzK0laaaAr3oxU&q=85&s=47f29273c31030465cf03d221abd7563 560w, https://mintcdn.com/oxla/scqzK0laaaAr3oxU/assets/images/light/except/except-one-light.png?w=840&fit=max&auto=format&n=scqzK0laaaAr3oxU&q=85&s=a8e811afaf22cbb642612cd480c62991 840w, https://mintcdn.com/oxla/scqzK0laaaAr3oxU/assets/images/light/except/except-one-light.png?w=1100&fit=max&auto=format&n=scqzK0laaaAr3oxU&q=85&s=213b2015403c2aefb99274029a4ce9fb 1100w, https://mintcdn.com/oxla/scqzK0laaaAr3oxU/assets/images/light/except/except-one-light.png?w=1650&fit=max&auto=format&n=scqzK0laaaAr3oxU&q=85&s=e3c78904f31aca26ccb6f78388809de9 1650w, https://mintcdn.com/oxla/scqzK0laaaAr3oxU/assets/images/light/except/except-one-light.png?w=2500&fit=max&auto=format&n=scqzK0laaaAr3oxU&q=85&s=0a0deaf3575f29a09657e53d71f16e49 2500w" />

<img className="hidden dark:block" src="https://mintcdn.com/oxla/ONnYYkZc0LCcRiQR/assets/images/dark/except/except-one-dark.png?fit=max&auto=format&n=ONnYYkZc0LCcRiQR&q=85&s=4c7bf50a2a13a41fc100f503e534a941" alt="" data-og-width="2075" width="2075" data-og-height="1409" height="1409" data-path="assets/images/dark/except/except-one-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/oxla/ONnYYkZc0LCcRiQR/assets/images/dark/except/except-one-dark.png?w=280&fit=max&auto=format&n=ONnYYkZc0LCcRiQR&q=85&s=b520f9071db187a75c59e59395365d59 280w, https://mintcdn.com/oxla/ONnYYkZc0LCcRiQR/assets/images/dark/except/except-one-dark.png?w=560&fit=max&auto=format&n=ONnYYkZc0LCcRiQR&q=85&s=5656c2f9570cb6674f5d5d43b01f88ed 560w, https://mintcdn.com/oxla/ONnYYkZc0LCcRiQR/assets/images/dark/except/except-one-dark.png?w=840&fit=max&auto=format&n=ONnYYkZc0LCcRiQR&q=85&s=afd5a7794fd88a1d39ff1c08c893d33b 840w, https://mintcdn.com/oxla/ONnYYkZc0LCcRiQR/assets/images/dark/except/except-one-dark.png?w=1100&fit=max&auto=format&n=ONnYYkZc0LCcRiQR&q=85&s=3d8bfaf2d996143267ec30180da292ad 1100w, https://mintcdn.com/oxla/ONnYYkZc0LCcRiQR/assets/images/dark/except/except-one-dark.png?w=1650&fit=max&auto=format&n=ONnYYkZc0LCcRiQR&q=85&s=041410c9ec83638f73682f466e5fb0af 1650w, https://mintcdn.com/oxla/ONnYYkZc0LCcRiQR/assets/images/dark/except/except-one-dark.png?w=2500&fit=max&auto=format&n=ONnYYkZc0LCcRiQR&q=85&s=542c3827f007a9c966edaa9e45dae56f 2500w" />

## EXCEPT ALL

### Overview

The `EXCEPT ALL` allows you to find rows specific to the first `SELECT` statement while preserving duplicate entries.

### Syntax

The syntax for the `EXCEPT ALL` is similar to `EXCEPT`:

```sql  theme={null}
SELECT value1, value2, ... value_n
FROM table1
EXCEPT ALL
SELECT value1, value2, ... value_n
FROM table2;
```

The parameters from the syntax are explained below:

* `value1, value2, ... value_n`: The columns you want to retrieve.
* `table1, table2`: The tables from which you wish to retrieve records.

<Note>The data types of corresponding columns in the `SELECT` queries must be compatible.</Note>

### Example #1

You aim to identify customers who have bought products from one marketplace but have not purchased from another. Start by creating the tables and populating them with relevant data.

```sql  theme={null}
CREATE TABLE marketplace1_transactions (
    customer_id INT,
    product_id INT,
    amount FLOAT
);

CREATE TABLE marketplace2_transactions (
    customer_id INT,
    product_id INT,
    amount FLOAT
);

INSERT INTO marketplace1_transactions VALUES
(101, 1, 100.00),
(102, 2, 150.00),
(103, 3, 200.00),
(104, 1, 120.00);

INSERT INTO marketplace2_transactions VALUES
(102, 3, 180.00),
(103, 2, 160.00),
(105, 4, 90.00),
(106, 1, 110.00);
```

Display the tables using the query below:

```sql  theme={null}
SELECT * FROM marketplace1_transactions;
SELECT * FROM marketplace2_transactions;
```

```sql  theme={null}
customer_id | product_id | amount
-------------+------------+--------
         101 |          1 |    100
         102 |          2 |    150
         103 |          3 |    200
         104 |          1 |    120

 customer_id | product_id | amount
-------------+------------+--------
         102 |          3 |    180
         103 |          2 |    160
         105 |          4 |     90
         106 |          1 |    110
```

Using the `EXCEPT ALL` to find customers who have purchased products from one marketplace but not from the other:

```sql  theme={null}
SELECT customer_id FROM marketplace1_transactions
EXCEPT ALL
SELECT customer_id FROM marketplace2_transactions;
```

This result will show a `customer_id` who has only transacted in the first marketplace and has not engaged in any corresponding transactions in the second marketplace.

```sql  theme={null}
customer_id
-------------
         104
         101
```

The diagram below shows a list of customer-product pairs found in the first marketplace (`marketplace1_transactions`) but missing in the second marketplace (`marketplace2_transactions`).

<img className="block dark:hidden" src="https://mintcdn.com/oxla/scqzK0laaaAr3oxU/assets/images/light/except/except-two-light.png?fit=max&auto=format&n=scqzK0laaaAr3oxU&q=85&s=bf6f51f1a678b7cad5b90234cd18e3ad" alt="" data-og-width="2075" width="2075" data-og-height="1409" height="1409" data-path="assets/images/light/except/except-two-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/oxla/scqzK0laaaAr3oxU/assets/images/light/except/except-two-light.png?w=280&fit=max&auto=format&n=scqzK0laaaAr3oxU&q=85&s=aee5f3e5338e7bf253f6e694ab9a6f02 280w, https://mintcdn.com/oxla/scqzK0laaaAr3oxU/assets/images/light/except/except-two-light.png?w=560&fit=max&auto=format&n=scqzK0laaaAr3oxU&q=85&s=28c811dcaada4b87226e6dd250cc318a 560w, https://mintcdn.com/oxla/scqzK0laaaAr3oxU/assets/images/light/except/except-two-light.png?w=840&fit=max&auto=format&n=scqzK0laaaAr3oxU&q=85&s=d76149104c619e8ea605447d60cc872e 840w, https://mintcdn.com/oxla/scqzK0laaaAr3oxU/assets/images/light/except/except-two-light.png?w=1100&fit=max&auto=format&n=scqzK0laaaAr3oxU&q=85&s=bf286dc5c6b168ce88a14aee6684de1e 1100w, https://mintcdn.com/oxla/scqzK0laaaAr3oxU/assets/images/light/except/except-two-light.png?w=1650&fit=max&auto=format&n=scqzK0laaaAr3oxU&q=85&s=f04839ad445cc4f38104531dd28b9399 1650w, https://mintcdn.com/oxla/scqzK0laaaAr3oxU/assets/images/light/except/except-two-light.png?w=2500&fit=max&auto=format&n=scqzK0laaaAr3oxU&q=85&s=89ca3d0807abf02c21b66e65de86647f 2500w" />

<img className="hidden dark:block" src="https://mintcdn.com/oxla/ONnYYkZc0LCcRiQR/assets/images/dark/except/except-two-dark.png?fit=max&auto=format&n=ONnYYkZc0LCcRiQR&q=85&s=5125754a83b22dd88c9c10ec0095f8e3" alt="" data-og-width="2075" width="2075" data-og-height="1409" height="1409" data-path="assets/images/dark/except/except-two-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/oxla/ONnYYkZc0LCcRiQR/assets/images/dark/except/except-two-dark.png?w=280&fit=max&auto=format&n=ONnYYkZc0LCcRiQR&q=85&s=cfdd591aa268d025ebfb6cce7f2fb667 280w, https://mintcdn.com/oxla/ONnYYkZc0LCcRiQR/assets/images/dark/except/except-two-dark.png?w=560&fit=max&auto=format&n=ONnYYkZc0LCcRiQR&q=85&s=ab5d8537ea4551a76dc1044760d8a3a4 560w, https://mintcdn.com/oxla/ONnYYkZc0LCcRiQR/assets/images/dark/except/except-two-dark.png?w=840&fit=max&auto=format&n=ONnYYkZc0LCcRiQR&q=85&s=3c0b9fc017f69fd78b3b88e98212724f 840w, https://mintcdn.com/oxla/ONnYYkZc0LCcRiQR/assets/images/dark/except/except-two-dark.png?w=1100&fit=max&auto=format&n=ONnYYkZc0LCcRiQR&q=85&s=bd36e51adb7437515e80ee7399a99cf0 1100w, https://mintcdn.com/oxla/ONnYYkZc0LCcRiQR/assets/images/dark/except/except-two-dark.png?w=1650&fit=max&auto=format&n=ONnYYkZc0LCcRiQR&q=85&s=d210ed404c3b2572badee2a0504bad78 1650w, https://mintcdn.com/oxla/ONnYYkZc0LCcRiQR/assets/images/dark/except/except-two-dark.png?w=2500&fit=max&auto=format&n=ONnYYkZc0LCcRiQR&q=85&s=5fee678838410df20bf89097cbfdaa1a 2500w" />

### Example #2

Let’s create two tables, `left_array_values` and `right_array_values`, to hold sets of values.

```sql  theme={null}
CREATE TABLE left_array_values (
    value INT
);

CREATE TABLE right_array_values (
    value INT
);

INSERT INTO left_array_values VALUES (1), (1), (3);
INSERT INTO right_array_values VALUES (1), (2);
```

View the contents of the two arrays before performing the comparison.

```sql  theme={null}
SELECT * FROM left_array_values;
SELECT * FROM right_array_values;
```

Upon execution, the tables will appear as follows:

```sql  theme={null}
value
-------
     1
     1
     3

 value
-------
     1
     2
```

We will now use the `EXCEPT ALL` operation to compare the values within the arrays, focusing on unique elements while retaining duplicate entries.

```sql  theme={null}
SELECT value
FROM left_array_values
EXCEPT ALL
SELECT value
FROM right_array_values;
```

The `EXCEPT ALL` operation processes each element individually from both inputs at a time. The comparison occurs element-wise, leading to the inclusion of both 1 and 3 in the final result.

```sql  theme={null}
value
-------
     3
     1
```
