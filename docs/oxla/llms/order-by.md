# Source: https://docs.oxla.com/sql-reference/sql-clauses/order-by.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxla.com/llms.txt
> Use this file to discover all available pages before exploring further.

# ORDER BY

## Overview

The `ORDER BY` clause is used to sort rows of the result received from a `SELECT` statement, which retrieves records from one or more tables.

## Syntax

The following illustrates the syntax of the `ORDER BY` clause:

```sql  theme={null}
SELECT columns
FROM table_name
ORDER BY sort_expression1 [ASC | DESC];
```

### Parameters

* `columns`: columns that you wish to retrieve
* `table_name`: table that you want to retrieve records from.
* `ORDER BY`: expression used to order the results
* `ASC` or `DESC`: optional parameter to specify the order in which the results should be returned, either ascending or descending. Default is set to `ASC`

## Examples

We will use the table called **salaryemp** as an example. In order to create the table, please run the query below:

```sql  theme={null}
CREATE TABLE salaryemp  
(  
    emp_id int,
    emp_name text,   
    emp_div text,   
    emp_sal int
);  

INSERT INTO salaryemp   
VALUES
(1002, 'Mike', 'Marketing', 6000),  
(1003, 'Sean', 'Marketing', 6500),  
(1004, 'Victor', 'Finance', 7000),  
(1005, 'Lewis', 'Sales', 5500),  
(1006, 'David', 'Marketing', 8000),
(1007, 'Omar', 'Finance', 8000),
(1008, 'Meghan', 'Finance', 7500),  
(1009, 'Harry', 'Operations', 4500),  
(1010, 'Steve', 'Marketing', 6800),   
(1011, 'David', 'Sales', 8200);
```

To verify that the values have been inserted successfully, retrieve the results by executing the following code:

```sql  theme={null}
SELECT * FROM salaryemp;
```

```sql  theme={null}
+-----------+------------+----------------+-------------+
| emp_id    | emp_name   | emp_div        | emp_sal     |
+-----------+------------+----------------+-------------+
| 1002      | Mike       | Marketing      | 6000        | 
| 1003      | Sean       | Marketing      | 6500        |
| 1004      | Victor     | Finance        | 7000        |
| 1005      | Lewis      | Sales          | 5500        |
| 1006      | David      | Marketing      | 8000        |
| 1007      | Meghan     | Finance        | 7500        |
| 1008      | Harry      | Operations     | 4500        |
| 1009      | Steve      | Marketing      | 6800        |
| 1010      | Omar       | Finance        | 8000        |
| 1011      | David      | Sales          | 8200        |
+-----------+------------+----------------+-------------+
```

### Using `ORDER BY` in ascending order

This example uses the `ORDER BY` clause to sort employees by their division:

```sql  theme={null}
SELECT emp_name, emp_div
FROM salaryemp
ORDER BY emp_div;
```

The above query will provide you with the following output:

```sql  theme={null}
+------------+----------------+
| emp_name   | emp_div        |
+------------+----------------+
| Victor     | Finance        |
| Omar       | Finance        |
| Meghan     | Finance        |
| Mike       | Marketing      |
| Sean       | Marketing      |
| David      | Marketing      |
| Steve      | Marketing      |
| Harry      | Operations     |
| Lewis      | Sales          |
| David      | Sales          |
+------------+----------------+
```

### Using `ORDER BY` in descending order

The following statement selects the employee name and employee salary from the **salaryemp** table and sorts the records in the `emp_sal` column in descending order:

```sql  theme={null}
SELECT * FROM salaryemp
ORDER BY emp_sal DESC;
```

The result of the query is as follows:

```sql  theme={null}
+-----------+------------+----------------+-------------+
| emp_id    | emp_name   | emp_div        | emp_sal     |
+-----------+------------+----------------+-------------+
| 1011      | David      | Sales          | 8200        |
| 1006      | David      | Marketing      | 8000        |
| 1010      | Omar       | Finance        | 8000        |
| 1007      | Meghan     | Finance        | 7500        |
| 1004      | Victor     | Finance        | 7000        |
| 1009      | Steve      | Marketing      | 6800        |
| 1003      | Sean       | Marketing      | 6500        |
| 1002      | Mike       | Marketing      | 6000        | 
| 1005      | Lewis      | Sales          | 5500        |
| 1008      | Harry      | Operations     | 4500        |
+-----------+------------+----------------+-------------+
```

### Using `ORDER BY` with both ASC & DESC parameters

The following statement selects all records from the **salaryemp** table and sorts the rows by employee salary in ascending order and employee division in descending order:

```sql  theme={null}
SELECT * FROM salaryemp
ORDER BY emp_sal ASC, emp_div DESC;
```

After implementing the above command, we will get the following output:

```sql  theme={null}
+-----------+------------+----------------+-------------+
| emp_id    | emp_name   | emp_div        | emp_sal     |
+-----------+------------+----------------+-------------+
| 1009      | Harry      | Operations     | 4500        |
| 1005      | Lewis      | Sales          | 5500        |
| 1002      | Mike       | Marketing      | 6000        |
| 1003      | Sean       | Marketing      | 6500        |
| 1009      | Steve      | Marketing      | 6800        |
| 1004      | Victor     | Finance        | 7000        |
| 1007      | Meghan     | Finance        | 7500        |
| 1006      | David      | Marketing      | 8000        |
| 1010      | Omar       | Finance        | 8000        |
| 1011      | David      | Sales          | 8200        |
+-----------+------------+----------------+-------------+
```

### Using `ORDER BY` with `TEXT` data types

In this example we are going to create to small tables with above mentioned data types:

```sql  theme={null}
CREATE TABLE strings  
(  
    column1 text
);  

INSERT INTO strings   
VALUES ('A'), ('B'), ('a'), ('b');

CREATE TABLE texts  
(  
    column1 TEXT
);  

INSERT INTO texts   
VALUES ('A'), ('B'), ('a'), ('b');
```

When using the `ORDER BY` clause with these types of data, records with uppercase letters will be sorted lexicographically first, followed by records with lowercase letters.

```sql  theme={null}
SELECT * FROM strings ORDER BY column1;
SELECT * FROM texts ORDER BY column1;
```

```sql  theme={null}
 column1 
---------
 A
 B
 a
 b
```

### Using `ORDER BY` with `INTERVAL` data type

For this example, we'll create a new table called `interval_data`:

```sql  theme={null}
CREATE TABLE interval_data (
    duration INTERVAL
);

INSERT INTO interval_data (duration)
VALUES 
    (INTERVAL '1 month 30 days 20 hours'),
    (INTERVAL '2 months 20 hours'),
    (INTERVAL '1 month 30 days 19 hours'),
    (INTERVAL '2 months 1 hours');
```

`ORDER BY` on `INTERVAL` column will sort the values by their leading most significant time unit.
In this case `months`. First are all `1 month` values, then all `2 months` values.

```sql  theme={null}
SELECT * FROM interval_data ORDER BY duration;
```

```sql  theme={null}
        duration        
------------------------
 1 mon 30 days 19:00:00
 1 mon 30 days 20:00:00
 2 mons 01:00:00
 2 mons 20:00:00
```

It works the same for other time units, such as `hours` and `days`.

```sql  theme={null}
INSERT INTO interval_data (duration)
VALUES 
    (INTERVAL '24 hours 5 minutes'),
    (INTERVAL '1 day 5 minutes'),
    (INTERVAL '1 day 2 minutes');
```

```sql  theme={null}
SELECT * FROM interval_data ORDER BY duration;
```

```sql  theme={null}
        duration        
------------------------
 24:05:00
 1 day 00:02:00
 1 day 00:05:00
 1 mon 30 days 19:00:00
 1 mon 30 days 20:00:00
 2 mons 01:00:00
 2 mons 20:00:00
```
