# Source: https://docs.snowflake.com/en/sql-reference/functions/avg.md

Categories:
:   [Aggregate functions](../functions-aggregation.md) (General) , [Window functions](../functions-window.md) (General, Window Frame)

# AVG

Returns the average of non-NULL records. If all records inside a group are NULL, the function returns NULL.

## Syntax

**Aggregate function**

```sqlsyntax
AVG( [ DISTINCT ] <expr1> )
```

**Window function**

```sqlsyntax
AVG( [ DISTINCT ] <expr1> ) OVER (
                                 [ PARTITION BY <expr2> ]
                                 [ ORDER BY <expr3> [ { ASC | DESC } ] [ NULLS { FIRST | LAST } ] [ <window_frame> ] ]
                                 )
```

For detailed `window_frame` syntax, see [Window function syntax and usage](../functions-window-syntax.md).

## Arguments

`expr1`
:   This is an expression that evaluates to a numeric data type (INTEGER, FLOAT, DECIMAL, etc.).

`expr2`
:   This is the optional expression to partition by.

`expr3`
:   This is the optional expression to order by within each partition.

## Usage notes

* When passed a VARCHAR expression, this function implicitly casts the input to floating point values. If the cast
  cannot be performed, an error is returned.

* When this function is called as a window function with an OVER clause that contains an ORDER BY clause:

  * A window frame is required. If no window frame is specified explicitly, the following implied window frame is used:

    `RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW`

    For more information about window frames, including syntax, usage notes, and examples, see [Window function syntax and usage](../functions-window-syntax.md).
  * Using the keyword DISTINCT inside the window function is prohibited and results in a compile-time error.

## Examples

Setup:

```sqlexample
CREATE OR REPLACE TABLE avg_example (int_col INT, d DECIMAL(10,5), s1 VARCHAR(10), s2 VARCHAR(10));

INSERT INTO avg_example VALUES
  (1, 1.1, '1.1', 'one'),
  (1, 10, '10', 'ten'),
  (2, 2.4, '2.4', 'two'),
  (2, NULL, NULL, 'NULL'),
  (3, NULL, NULL, 'NULL'),
  (NULL, 9.9, '9.9', 'nine');
```

Show the data:

```sqlexample
SELECT *
  FROM avg_example
  ORDER BY int_col, d;
```

```output
+---------+----------+------+------+
| INT_COL |        D | S1   | S2   |
|---------+----------+------+------|
|       1 |  1.10000 | 1.1  | one  |
|       1 | 10.00000 | 10   | ten  |
|       2 |  2.40000 | 2.4  | two  |
|       2 |     NULL | NULL | NULL |
|       3 |     NULL | NULL | NULL |
|    NULL |  9.90000 | 9.9  | nine |
+---------+----------+------+------+
```

Calculate the average of the columns that are numeric or that can be converted to numbers:

```sqlexample
SELECT AVG(int_col), AVG(d)
  FROM avg_example;
```

```output
+--------------+---------------+
| AVG(INT_COL) |        AVG(D) |
|--------------+---------------|
|     1.800000 | 5.85000000000 |
+--------------+---------------+
```

Combine AVG with GROUP BY to calculate the averages of different groups:

```sqlexample
SELECT int_col, AVG(d), AVG(s1)
  FROM avg_example
  GROUP BY int_col
  ORDER BY int_col;
```

```output
+---------+---------------+---------+
| INT_COL |        AVG(D) | AVG(S1) |
|---------+---------------+---------|
|       1 | 5.55000000000 |    5.55 |
|       2 | 2.40000000000 |    2.4  |
|       3 |          NULL |    NULL |
|    NULL | 9.90000000000 |    9.9  |
+---------+---------------+---------+
```

Use as a simple window function:

```sqlexample
SELECT
    int_col,
    AVG(int_col) OVER (PARTITION BY int_col)
  FROM avg_example
  ORDER BY int_col;
```

```output
+---------+-----------------------------------------+
| INT_COL | AVG(INT_COL) OVER(PARTITION BY INT_COL) |
|---------+-----------------------------------------|
|       1 |                                   1.000 |
|       1 |                                   1.000 |
|       2 |                                   2.000 |
|       2 |                                   2.000 |
|       3 |                                   3.000 |
|    NULL |                                    NULL |
+---------+-----------------------------------------+
```
