# Source: https://docs.oxla.com/sql-reference/sql-functions/math-functions/sign.md

# SIGN

## Overview

The `SIGN()` function returns a sign of an argument. The returned values are -1 if the argument is less than zero, 1 if the argument is greater than zero, 0 if the argument is equal to zero.

## Syntax

The syntax for the `SIGN() `function is as follows:

```sql  theme={null}
SIGN(x)
```

The `SIGN()` function requires one argument:

* `x`: an expression that evaluates to a number.

## Examples

### Case #1: Sign of a number

The following example demonstrates how the `SIGN()` function can be used to obtain the sign of a number:

```sql  theme={null}
SELECT
    SIGN(0.1) AS "SIGN(0.1)",
    SIGN(999) AS "SIGN(999)",
    SIGN(0) AS "SIGN(0)",
    SIGN(-0) AS "SIGN(-0)";
```

The query will return the signs of the passed arguments:

```sql  theme={null}
 SIGN(0.1) | SIGN(999) | SIGN(0) | SIGN(-0)
-----------+-----------+---------+----------
         1 |         1 |       0 |        0

```

Note: `-0` is accepted as an argument and is equal to zero

### Case #2: SIGN() function with an expression

The following example demonstrates how the `SIGN()` function can be used with an expression:

```sql  theme={null}
SELECT SIGN(100 - 200);
```

will return the sign of the expression evaluation:

```sql  theme={null}
 sign
------
   -1
------
```

### Case #3: Using the SIGN() function with a table

The following example demonstrates how the `SIGN()` function can be used with a table to obtain the absolute values of all numbers in a specific column:

1. Create a table signTable containing an ***value*** column with some positive, negative and equal to zero values:

```sql  theme={null}
CREATE TABLE signTable(value float);

INSERT INTO signTable(value)
VALUES 
(1000),
(-200),
(0),
(0.22),
(-12.3),
(-0.0);
```

2. Use the following query to find the sign of all inserted values:

```sql  theme={null}
SELECT value, SIGN(value) AS sign
FROM signTable;
```

3. The result will be as follows::

```sql  theme={null}
 value | sign
-------+------
  1000 |    1
  -200 |   -1
     0 |    0
  0.22 |    1
 -12.3 |   -1
    -0 |    0
```
