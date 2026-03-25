# Source: https://docs.snowflake.com/en/sql-reference/functions/corr.md

Categories:
:   [Aggregate functions](../functions-aggregation.md) (General) , [Window functions](../functions-window.md) (General)

# CORR

Returns the correlation coefficient for non-null pairs in a group. It is computed for non-null pairs using the following formula:

> `COVAR_POP(y, x) / (STDDEV_POP(x) * STDDEV_POP(y))`

Where `x` is the independent variable and `y` is the dependent variable.

See also:
:   [COVAR_POP](covar_pop.md) , [STDDEV_POP](stddev_pop.md)

## Syntax

Syntax when used as an aggregate function:

```sqlsyntax
CORR( y , x )
```

Syntax when used as a window function:

```sqlsyntax
CORR( y , x ) OVER ( [ PARTITION BY <expr3> ] )
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

SELECT * FROM aggr;
```

```output
+---+-------+-------+
| K |     V |    V2 |
|---+-------+-------|
| 1 | 10.00 |  NULL |
| 2 | 10.00 | 11.00 |
| 2 | 20.00 | 22.00 |
| 2 | 25.00 |  NULL |
| 2 | 30.00 | 35.00 |
+---+-------+-------+
```

```sqlexample
SELECT k, CORR(v, v2) FROM aggr GROUP BY k;
```

```output
+---+--------------+
| K |  CORR(V, V2) |
|---+--------------|
| 1 |         NULL |
| 2 | 0.9988445981 |
+---+--------------+
```
