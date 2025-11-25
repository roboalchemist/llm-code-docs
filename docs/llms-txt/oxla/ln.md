# Source: https://docs.oxla.com/sql-reference/sql-functions/math-functions/ln.md

# LN

## Overview

`LN()` will return the exponential value of its argument, which is recognized as the input parameter's natural logarithm.&#x20;

<Note>**Info:**<br /> The logarithm doesn’t take negative numbers or 0.</Note>

## \*yntax

The syntax of the `LN()` function is described as follows.

```sql  theme={null}
LN (x)
```

`x`:  A positive or a negative number (or an expression that evaluates to a number).

## Examples

### Case #1: Basic LN() function

The example below shows that `LN()` function will return the natural logarithm of the number **7,87653**.

```sql  theme={null}
SELECT LN(7.87653);
```

The final result is as follows.

```sql  theme={null}
+-------------+
| f           |
+-------------+
| 2.0638874   |
+-------------+
```

### Case #2: Using LN() Function With a Table

In the following example, we will combine `LN()` function with `CREATE TABLE` statement. Therefore we can obtain natural logarithmic values of a specific column.

1. Create a new table named **LNTable** containing the **initValue** column with an integer value.

```sql  theme={null}
CREATE TABLE LNtable(initValue int);
INSERT INTO LNtable(initValue)
VALUES (75), (18), (28);
```

2. Run the following query to get the logarithm output of the column:

```sql  theme={null}
SELECT * ,LN(initValue) AS lnValue FROM LNtable;
```

3. It will return the initial value with its natural logarithm value.

* **initValue** column with the initial integer values.
* **lnValue** column with the natural logarithm values.

```sql  theme={null}
+------------+---------------------------+
| initValue  | lnValue                   |
+------------+---------------------------+
| 75         | 4.31748811353631          |
| 18         | 2.8903717578961645        |
| 28         | 3.332204510175204         |
+------------+---------------------------+
```
