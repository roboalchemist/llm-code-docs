# Source: https://docs.oxla.com/resources/oxla-vs-postgresql.md

# Oxla vs. PostgreSQL

## Functions

### Mathematical

A mathematical function operates on input values provided as arguments and returns a numeric value as the operation's output.

| **Mathematical** | **Description**                                                                                          | **Example**           | **Available in Oxla** |
| ---------------- | -------------------------------------------------------------------------------------------------------- | --------------------- | --------------------- |
| ABS              | Returns the absolute value of a number.                                                                  | `SELECT  ABS(-11);`   | Available             |
| CEIL             | Returns the value after rounding up any positive or negative value to the nearest largest integer.       | `SELECT CEIL(53.7);`  | Available             |
| FLOOR            | Returns the value after rounding up any positive or negative decimal value as smaller than the argument. | `SELECT FLOOR(53.6);` | Available             |
| LN               | Returns the natural logarithm of a given number.                                                         | `SELECT LN(3);`       | Available             |
| RANDOM           | Returns the random value between 0 and 1.                                                                | `SELECT RANDOM();`    | Available             |
| SQRT             | Returns the square root of a given positive number.                                                      | `SELECT SQRT(225);`   | Available             |

### Trigonometric

| **Trigonometric** | **Description**                           | **Example**        | **Available in Oxla** |
| ----------------- | ----------------------------------------- | ------------------ | --------------------- |
| SIN               | Returns the sine of the specified radian. | `SELECT sin(0.2);` | Available             |

## Operators

### Mathematical Operators

Below is a list of mathematical operators available in PostgreSQL:

| **Operator** | **Description** | **Example**       | **Result** | **Available in Oxla** |
| ------------ | --------------- | ----------------- | ---------- | --------------------- |
| `+`          | Addition        | `SELECT 5 + 8;`   | `13`       | Available             |
| `-`          | Subtraction     | `SELECT 2 - 3;`   | `\-1`      | Available             |
| `-`          | Negation        | `SELECT -4;`      | `\-4`      | Available             |
|              |                 | `SELECT -(-4);`   | `4`        | Available             |
|              |                 | `SELECT 5+(-2);`  | `3`        | Available             |
|              |                 | `SELECT 5-(-2);`  | `7`        | Available             |
| `*`          | Multiplication  | `SELECT 3 * 3;`   | `9`        | Available             |
| `/`          | Division        | `SELECT 10 / 2;`  | `5`        | Available             |
| `%`          | Modulo          | `SELECT 20 % 3;`  | `2`        | Available             |
| `&`          | Bitwise AND     | `SELECT 91 & 15;` | `11`       | Available             |
| `#`          | Bitwise XOR     | `SELECT 17 # 5;`  | `20`       | Available             |

### JSON Operators

Oxla supports operators for handling JSON data. One such operator is:

#### Equal Operator (`=`)

This operator checks if two JSON values are identical. In Oxla, this operator is order-sensitive which means that for two JSON objects to be considered equal, their key-value pairs must appear in the exact same order.

```sql  theme={null}
SELECT '{"a":1, "b":"c"}'::json = '{"b":"c", "a":1}'::json;
```

**Result**

```sql  theme={null}
 ?column? 
----------
 f
(1 row)
```

<Note>In PostgreSQL, this operator is not order-sensitive, so the order of key-value pairs does not affect the comparison result.</Note>

## Behaviors Difference

### Output Header

Missing function name in output header, PostgreSQL shows the function name, like in this example:

```sql  theme={null}
SELECT COS(0),LN(1);
```

```sql  theme={null}
cos  | ln 
-----+-----
 1   | 0
```

Oxla does not show the function name, like in this example:

```sql  theme={null}
SELECT COS(0),LN(1);
```

```sql  theme={null}
 f | f_1 
---+-----
 1 | 0
```

### ABS Output

Differences are also found in the ABS function, where there are differences in decimal results. The example below will return the absolute value of -1.0

```sql  theme={null}
SELECT ABS(-1.0);
```

It returns 1 in Oxla, while in PostgreSQL, it produces 1.0

## Errors Difference

| **Functions** | **Input**             | **Output - Oxla**       | **Output - PostgreSQL**                                   |
| ------------- | --------------------- | ----------------------- | --------------------------------------------------------- |
| LN            | `LN(0)`               | *Infinity*              | *ERROR: cannot take the logarithm of zero*                |
|               | `LN(0.0)`             | *Infinity*              | *ERROR: cannot take the logarithm of zero*                |
| LOG10         | `LOG10(-1)`           | *NaN*                   | *ERROR: cannot take logarithm of a negative number*       |
| SQRT          | `SQRT(-1)`            | *input is out of range* | *ERROR: cannot take the square root of a negative number* |
| SIN           | `SELECT sin(pi()/2);` | *unknown function pi*   | working as expected                                       |
