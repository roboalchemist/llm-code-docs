# Source: https://docs.oxla.com/sql-reference/sql-functions/math-functions/ceil.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxla.com/llms.txt
> Use this file to discover all available pages before exploring further.

# CEIL

## Overview

The `CEIL()` function returns the nearest positive or negative integer value greater than or equal to the provided decimal input number.

## Syntax

The syntax of the `CEIL()` function is as follows:

```sql  theme={null}
CEIL(x)
```

The `CEIL()` function requires one argument:

* `x`: A positive or a negative decimal number (or an expression that evaluates to a decimal number).

## Examples

### Case #1: Rounding up a positive decimal value

The following example demonstrates how the `CEIL() `function rounds up a positive decimal value:

```sql  theme={null}
SELECT CEIL (300.55);
```

As shown below, it will return 301, as it is the nearest integer value greater than 300.55.

```sql  theme={null}
+------+
| f    |
+------+
| 301  |
+------+
```

### Case #2: Rounding up a negative decimal value

The following example demonstrates how the `CEIL() `function rounds up a negative decimal value:

```sql  theme={null}
SELECT CEIL(-89.9) AS "Ceil";
```

The output of this statement will be -89, as -89 is the nearest integer value greater than or equal to -89.9, as shown below.

```sql  theme={null}
+-------+
| Ceil  |
+-------+
| -89   |
+-------+
```

### Case #3: Using the `CEIL()` function with a table

The following example demonstrates how the `CEIL()` function can be used with a table to round up the values in a specific column:

1. First, create a table called ***CeilRecords*** with the following query:

```sql  theme={null}
CREATE TABLE CeilRecords (numbers float);
  
INSERT INTO CeilRecords(numbers) 
VALUES 
    (-28.85),
    (-9.4),
    (0.87),
    (78.16),
    (42.16);
```

The above statement will create a table called **"CeilRecords"** with a column called **"numbers"** and insert 5 decimal values into it.

2. The statement below can be used to retrieve and round up the value for all records in the column \***numbers**:

```sql  theme={null}
SELECT *, CEIL(numbers) AS CeilValue FROM CeilRecords;
```

The final result will contain the following:

* A **numbers** column with initial decimal values.

* A **CeilValue** column with rounded-up integer values.

```sql  theme={null}
+---------+------------+
| numbers  | CeilValue  |
+---------+------------+
| -28.85  | -28        |
| -9.4    | -9         |
| 0.87    | 1          |
| 78.16   | 79         |
| 42.16   | 43         |
+---------+------------+
```
