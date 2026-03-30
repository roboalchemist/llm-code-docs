# Source: https://docs.snowflake.com/en/sql-reference/functions/hll.md

Categories:
:   [Aggregate functions](../functions-aggregation.md) (Cardinality Estimation) , [Window functions](../functions-window.md)

# HLL

Uses HyperLogLog to return an approximation of the distinct cardinality of the input (i.e. `HLL(col1, col2, ... )` returns an approximation of `COUNT(DISTINCT col1, col2, ... )`).

For more information about HyperLogLog, see [Estimating the Number of Distinct Values](../../user-guide/querying-approximate-cardinality.md).

Aliases:
:   [APPROX_COUNT_DISTINCT](approx_count_distinct.md).

See also:
:   [HLL_ACCUMULATE](hll_accumulate.md) , [HLL_COMBINE](hll_combine.md) , [HLL_ESTIMATE](hll_estimate.md)

## Syntax

**Aggregate function**

```sqlsyntax
HLL( [ DISTINCT ] <expr1> [ , ... ] )

HLL(*)
```

**Window function**

```sqlsyntax
HLL( [ DISTINCT ] <expr1> [ , ... ] ) OVER ( [ PARTITION BY <expr2> ] )

HLL(*) OVER ( [ PARTITION BY <expr2> ] )
```

## Arguments

`expr1`
:   This is the expression for which you want to know the number of distinct values.

`expr2`
:   This is the optional expression used to group rows into partitions.

## Returns

The data type of the returned value is INTEGER.

## Usage notes

* `DISTINCT` can be included as an argument, but has no effect.
* For information about NULL values and aggregate functions, see [Aggregate functions and NULL values](../functions-aggregation.md).
* When this function is called as a window function, it does not support:

  * An ORDER BY clause within the OVER clause.
  * Explicit window frames.

## Examples

This example shows how to use HLL and its alias APPROX_COUNT_DISTINCT. This example calls
both `COUNT(DISTINCT i)` and `APPROX_COUNT_DISTINCT(i)` to emphasize
that the results of these two functions do not always match exactly.

The exact output from the following query might vary because APPROX_COUNT_DISTINCT() returns an approximation, not an exact value.

```sqlexample
SELECT COUNT(i), COUNT(DISTINCT i), APPROX_COUNT_DISTINCT(i), HLL(i)
  FROM sequence_demo;
```

```output
+----------+-------------------+--------------------------+--------+
| COUNT(I) | COUNT(DISTINCT I) | APPROX_COUNT_DISTINCT(I) | HLL(I) |
|----------+-------------------+--------------------------+--------|
|     1024 |              1024 |                     1007 |   1007 |
+----------+-------------------+--------------------------+--------+
```
