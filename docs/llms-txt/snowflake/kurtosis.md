# Source: https://docs.snowflake.com/en/sql-reference/functions/kurtosis.md

Categories:
:   [Aggregate functions](../functions-aggregation.md) (General) , [Window function syntax and usage](../functions-window-syntax.md)

# KURTOSIS

Returns the sample excess kurtosis of non-NULL records. If all records inside a group are NULL, the function returns NULL.

The following formula is used to compute the sample excess kurtosis:

\[(n \* (n+1))/((n-1) \* (n-2) \* (n-3)) \* (n \* m_4/(k_2)^2) - 3 \* (n-1)^2 / ((n-2) \* (n-3))\]

where:

* \(n\) denotes the number of non-NULL records.
* \(m_4\) denotes the sample fourth central moment.
* \(k_2\) denotes the symmetric unbiased estimator of the variance.

## Syntax

**Aggregate function**

```sqlsyntax
KURTOSIS( <expr> )
```

**Window function**

```sqlsyntax
KURTOSIS( <expr> ) OVER ( [ PARTITION BY <expr2> ] )
```

## Arguments

`expr`
:   An expression that evaluates to a numeric data type (such as INTEGER, FLOAT, DECIMAL).

`expr2`
:   An expression that defines the individual groups or windows.

## Returns

Returns DOUBLE if the input data type is DOUBLE/FLOAT.

Returns DECIMAL if the input data type is another numeric data type.

## Usage notes

* For inputs with fewer than four records, KURTOSIS returns NULL.

* When this function is called as a window function, it does not support:

  * An ORDER BY clause within the OVER clause.
  * Explicit window frames.

## Examples

Create a table and insert some rows:

```sqlexample
CREATE OR REPLACE TABLE aggr(k INT, v DECIMAL(10,2), v2 DECIMAL(10, 2));

INSERT INTO aggr VALUES
  (1, 10, null),
  (2, 10, 12),
  (2, 20, 22),
  (2, 25, null),
  (2, 30, 35);
```

Select all the data from the table:

```sqlexample
SELECT * FROM aggr
  ORDER BY k, v;
```

```output
+---+-------+-------+
| K |     V |    V2 |
|---+-------+-------|
| 1 | 10.00 |  NULL |
| 2 | 10.00 | 12.00 |
| 2 | 20.00 | 22.00 |
| 2 | 25.00 |  NULL |
| 2 | 30.00 | 35.00 |
+---+-------+-------+
```

Return the KURTOSIS value for each column:

```sqlexample
SELECT KURTOSIS(k), KURTOSIS(v), KURTOSIS(v2)
  FROM aggr;
```

```output
+----------------+-----------------+--------------+
|    KURTOSIS(K) |     KURTOSIS(V) | KURTOSIS(V2) |
|----------------+-----------------+--------------|
| 5.000000000000 | -2.324218750000 |         NULL |
+----------------+-----------------+--------------+
```
