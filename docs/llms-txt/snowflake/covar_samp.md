# Source: https://docs.snowflake.com/en/sql-reference/functions/covar_samp.md

Categories:
:   [Aggregate functions](../functions-aggregation.md) (General) , [Window functions](../functions-window.md) (General)

# COVAR_SAMP

Returns the sample covariance for non-null pairs in a group. It is computed for non-null pairs using the following formula:

> `(SUM(x*y) - SUM(x) * SUM(y) / COUNT(*)) / (COUNT(*) - 1)`

Where `x` is the independent variable and `y` is the dependent variable.

See also:
:   [COVAR_POP](covar_pop.md) , [COUNT](count.md) , [SUM](sum.md)

## Syntax

**Aggregate function**

```sqlsyntax
COVAR_SAMP( y , x )
```

**Window function**

```sqlsyntax
COVAR_SAMP( y , x ) OVER ( [ PARTITION BY <expr1> ] )
```

## Usage notes

* DISTINCT is not supported for this function.

* When this function is called as a window function, it does not support:

  * An ORDER BY clause within the OVER clause.
  * Explicit window frames.

## Examples

```sqlexample
CREATE OR REPLACE TABLE aggr(k int, v decimal(10,2), v2 decimal(10, 2));
INSERT INTO aggr VALUES(1, 10, NULL);
INSERT INTO aggr VALUES(2, 10, 11), (2, 20, 22), (2, 25, NULL), (2, 30, 35);

SELECT k, COVAR_SAMP(v, v2) FROM aggr GROUP BY k;
```

```output
+---+-------------------+
| K | COVAR_SAMP(V, V2) |
|---+-------------------|
| 1 |              NULL |
| 2 |               120 |
+---+-------------------+
```
