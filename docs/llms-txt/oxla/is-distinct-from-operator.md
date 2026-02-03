# Source: https://docs.oxla.com/sql-reference/sql-functions/boolean-functions/is-distinct-from-operator.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxla.com/llms.txt
> Use this file to discover all available pages before exploring further.

# IS DISTINCT FROM Operator

## Overview

The `IS DISTINCT FROM` operator compares two values, considering them distinct even when both are `NULL`. It returns `TRUE` if the two values are different and `FALSE` if they are the same, including the case where both values are `NULL`.&#x20;

## Syntax

The syntax for the operator is as follows:

```sql  theme={null}
value1 IS DISTINCT FROM value2
```

Where:

* `value1` is the first value for comparison.
* `value2` is the second value for comparison.

## Examples

### Case #1: Basic Usage

Consider the following example where we compare two values:

**Example 1**

```sql  theme={null}
SELECT NULL IS DISTINCT FROM NULL AS "Result";
```

The above query will return the following output:

```sql  theme={null}
 Result 
--------
 f
```

**Example 2**

```sql  theme={null}
SELECT 10 IS DISTINCT FROM 20 AS "Result";
```

The above query will return the following output:

```sql  theme={null}
 Result 
--------
 t
```

**Example 3**

```sql  theme={null}
SELECT 10 IS DISTINCT FROM 10 AS "Result";    
```

The above query will return the following output:

```sql  theme={null}
 Result 
--------
 f
```

### Case #2: Comparing NULL Values

In this example, we'll compare `NULL` values using the `IS DISTINCT FROM` operator:

**Example 1**

```sql  theme={null}
SELECT NULL IS DISTINCT FROM 10 AS "Result";  
```

The above query will return the following output:

```sql  theme={null}
 Result 
--------
 t
```

**Example 2**

```sql  theme={null}
SELECT 10 IS DISTINCT FROM NULL AS "Result";
```

The above query will return the following output:

```sql  theme={null}
 Result 
--------
 t
```

### Case #3: Tracking Inventory Variations

Suppose we have a table named `inventory_changes` that tracks changes in the quantities of products in a warehouse. The table has the following structure:

```sql  theme={null}
CREATE TABLE inventory_changes (
  product_id INT,
  change_date DATE,
  change_quantity INT
);

INSERT INTO inventory_changes VALUES
(101, '2023-08-01', 50),
(102, '2023-08-01', 0),
(101, '2023-08-02', -15),
(103, '2023-08-03', 30),
(102, '2023-08-04', 0);
```

We want to retrieve records where the change quantity is distinct from zero. In this scenario, the `IS DISTINCT FROM` operator can be used.

```sql  theme={null}
SELECT *
FROM inventory_changes
WHERE change_quantity IS DISTINCT FROM 0;
```

The result of the query will not include the 0 values as shown below:

```sql  theme={null}
 product_id | change_date | change_quantity 
------------+-------------+-----------------
        101 | 2023-08-01  |              50
        101 | 2023-08-02  |             -15
        103 | 2023-08-03  |              30
```
