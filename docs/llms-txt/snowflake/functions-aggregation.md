# Source: https://docs.snowflake.com/en/sql-reference/functions-aggregation.md

# Aggregate functions

Aggregate functions operate on values across rows to perform mathematical calculations such as sum, average, counting, minimum/maximum values, standard
deviation, and estimation, as well as some non-mathematical operations.

An aggregate function takes multiple rows (actually, zero, one, or more rows) as input and produces a single output.
In contrast, scalar functions take one row as input and produce one row (one value) as output.

An aggregate function always returns exactly one row, even when the input contains zero rows. Typically, if
the input contains zero rows, the output is NULL. However, an aggregate function could return `0`, an empty string, or
some other value when passed zero rows.

## List of functions (by sub-category)

| Function Name | Notes |
| --- | --- |
| **General Aggregation** |  |
| [ANY_VALUE](functions/any_value.md) |  |
| [AVG](functions/avg.md) |  |
| [CORR](functions/corr.md) |  |
| [COUNT](functions/count.md) |  |
| [COUNT_IF](functions/count_if.md) |  |
| [COVAR_POP](functions/covar_pop.md) |  |
| [COVAR_SAMP](functions/covar_samp.md) |  |
| [LISTAGG](functions/listagg.md) |  |
| [MAX](functions/max.md) |  |
| [MAX_BY](functions/max_by.md) |  |
| [MEDIAN](functions/median.md) |  |
| [MIN](functions/min.md) |  |
| [MIN_BY](functions/min_by.md) |  |
| [MODE](functions/mode.md) |  |
| [PERCENTILE_CONT](functions/percentile_cont.md) | Uses different syntax than the other aggregate functions. |
| [PERCENTILE_DISC](functions/percentile_disc.md) | Uses different syntax than the other aggregate functions. |
| [STDDEV, STDDEV_SAMP](functions/stddev.md) | STDDEV and STDDEV_SAMP are aliases. |
| [STDDEV_POP](functions/stddev_pop.md) |  |
| [SUM](functions/sum.md) |  |
| [VAR_POP](functions/var_pop.md) |  |
| [VAR_SAMP](functions/var_samp.md) |  |
| [VARIANCE_POP](functions/variance_pop.md) | Alias for [VAR_POP](functions/var_pop.md). |
| [VARIANCE , VARIANCE_SAMP](functions/variance.md) | Alias for [VAR_SAMP](functions/var_samp.md). |
| **Bitwise Aggregation** |  |
| [BITAND_AGG](functions/bitand_agg.md) |  |
| [BITOR_AGG](functions/bitor_agg.md) |  |
| [BITXOR_AGG](functions/bitxor_agg.md) |  |
| **Boolean Aggregation** |  |
| [BOOLAND_AGG](functions/booland_agg.md) |  |
| [BOOLOR_AGG](functions/boolor_agg.md) |  |
| [BOOLXOR_AGG](functions/boolxor_agg.md) |  |
| **Hash** |  |
| [HASH_AGG](functions/hash_agg.md) |  |
| **Semi-structured Data Aggregation** |  |
| [ARRAY_AGG](functions/array_agg.md) |  |
| [OBJECT_AGG](functions/object_agg.md) |  |
| **Linear Regression** |  |
| [REGR_AVGX](functions/regr_avgx.md) |  |
| [REGR_AVGY](functions/regr_avgy.md) |  |
| [REGR_COUNT](functions/regr_count.md) |  |
| [REGR_INTERCEPT](functions/regr_intercept.md) |  |
| [REGR_R2](functions/regr_r2.md) |  |
| [REGR_SLOPE](functions/regr_slope.md) |  |
| [REGR_SXX](functions/regr_sxx.md) |  |
| [REGR_SXY](functions/regr_sxy.md) |  |
| [REGR_SYY](functions/regr_syy.md) |  |
| **Statistics and Probability** |  |
| [KURTOSIS](functions/kurtosis.md) |  |
| [SKEW](functions/skew.md) |  |
| **Counting Distinct Values** |  |
| [ARRAY_UNION_AGG](functions/array_union_agg.md) |  |
| [ARRAY_UNIQUE_AGG](functions/array_unique_agg.md) |  |
| [BITMAP_BIT_POSITION](functions/bitmap_bit_position.md) |  |
| [BITMAP_BUCKET_NUMBER](functions/bitmap_bucket_number.md) |  |
| [BITMAP_COUNT](functions/bitmap_count.md) |  |
| [BITMAP_CONSTRUCT_AGG](functions/bitmap_construct_agg.md) |  |
| [BITMAP_OR_AGG](functions/bitmap_or_agg.md) |  |
| **Cardinality Estimation** . (**using** [HyperLogLog](../user-guide/querying-approximate-cardinality.md)) |  |
| [APPROX_COUNT_DISTINCT](functions/approx_count_distinct.md) | Alias for [HLL](functions/hll.md). |
| [DATASKETCHES_HLL](functions/datasketches_hll.md) |  |
| [DATASKETCHES_HLL_ACCUMULATE](functions/datasketches_hll_accumulate.md) |  |
| [DATASKETCHES_HLL_COMBINE](functions/datasketches_hll_combine.md) |  |
| [DATASKETCHES_HLL_ESTIMATE](functions/datasketches_hll_estimate.md) | Not an aggregate function; uses scalar input from [DATASKETCHES_HLL_ACCUMULATE](functions/datasketches_hll_accumulate.md) or [DATASKETCHES_HLL_COMBINE](functions/datasketches_hll_combine.md). |
| [HLL](functions/hll.md) |  |
| [HLL_ACCUMULATE](functions/hll_accumulate.md) |  |
| [HLL_COMBINE](functions/hll_combine.md) |  |
| [HLL_ESTIMATE](functions/hll_estimate.md) | Not an aggregate function; uses scalar input from [HLL_ACCUMULATE](functions/hll_accumulate.md) or [HLL_COMBINE](functions/hll_combine.md). |
| [HLL_EXPORT](functions/hll_export.md) |  |
| [HLL_IMPORT](functions/hll_import.md) |  |
| **Similarity Estimation** . (**using** [MinHash](../user-guide/querying-approximate-similarity.md)) |  |
| [APPROXIMATE_JACCARD_INDEX](functions/approximate_jaccard_index.md) | Alias for [APPROXIMATE_SIMILARITY](functions/approximate_similarity.md). |
| [APPROXIMATE_SIMILARITY](functions/approximate_similarity.md) |  |
| [MINHASH](functions/minhash.md) |  |
| [MINHASH_COMBINE](functions/minhash_combine.md) |  |
| **Frequency Estimation** . (**using** [Space-Saving](../user-guide/querying-approximate-frequent-values.md)) |  |
| [APPROX_TOP_K](functions/approx_top_k.md) |  |
| [APPROX_TOP_K_ACCUMULATE](functions/approx_top_k_accumulate.md) |  |
| [APPROX_TOP_K_COMBINE](functions/approx_top_k_combine.md) |  |
| [APPROX_TOP_K_ESTIMATE](functions/approx_top_k_estimate.md) | Not an aggregate function; uses scalar input from [APPROX_TOP_K_ACCUMULATE](functions/approx_top_k_accumulate.md) or [APPROX_TOP_K_COMBINE](functions/approx_top_k_combine.md). |
| **Percentile Estimation** . (**using** [t-Digest](../user-guide/querying-approximate-percentile-values.md)) |  |
| [APPROX_PERCENTILE](functions/approx_percentile.md) |  |
| [APPROX_PERCENTILE_ACCUMULATE](functions/approx_percentile_accumulate.md) |  |
| [APPROX_PERCENTILE_COMBINE](functions/approx_percentile_combine.md) |  |
| [APPROX_PERCENTILE_ESTIMATE](functions/approx_percentile_estimate.md) | Not an aggregate function; uses scalar input from [APPROX_PERCENTILE_ACCUMULATE](functions/approx_percentile_accumulate.md) or [APPROX_PERCENTILE_COMBINE](functions/approx_percentile_combine.md). |
| **Aggregation Utilities** |  |
| [GROUPING](functions/grouping.md) | Not an aggregate function, but can be used in conjunction with aggregate functions to determine the level of aggregation for a row produced by a [GROUP BY](constructs/group-by.md) query. |
| [GROUPING_ID](functions/grouping_id.md) | Alias for [GROUPING](functions/grouping.md). |
| **AI Functions** |  |
| [AI_AGG](functions/ai_agg.md) |  |
| [AI_SUMMARIZE_AGG](functions/ai_summarize_agg.md) |  |
| **Vector Aggregation** |  |
| [VECTOR_AVG](functions/vector_avg.md) |  |
| [VECTOR_MAX](functions/vector_max.md) |  |
| [VECTOR_MIN](functions/vector_min.md) |  |
| [VECTOR_SUM](functions/vector_sum.md) |  |
| **Semantic views** |  |
| [AGG](functions/agg.md) |  |

## Introductory example

The following example illustrates the difference between an aggregate function ([AVG](functions/avg.md)) and a scalar function ([COS](functions/cos.md)). The scalar function returns one output row for each input
row, while the aggregate function returns one output row for multiple input rows:

Create a table and populate it with values:

```sqlexample
CREATE TABLE simple (x INTEGER, y INTEGER);
INSERT INTO simple (x, y) VALUES
    (10, 20),
    (20, 44),
    (30, 70);
```

Query the table:

```sqlexample
SELECT x, y
    FROM simple
    ORDER BY x,y;
```

```output
+----+----+
|  X |  Y |
|----+----|
| 10 | 20 |
| 20 | 44 |
| 30 | 70 |
+----+----+
```

The scalar function returns one output row for each input row.

```sqlexample
SELECT COS(x)
    FROM simple
    ORDER BY x;
```

```output
+---------------+
|        COS(X) |
|---------------|
| -0.8390715291 |
|  0.4080820618 |
|  0.1542514499 |
+---------------+
```

The aggregate function returns one output row for multiple input rows:

```sqlexample
SELECT SUM(x)
    FROM simple;
```

```output
+--------+
| SUM(X) |
|--------|
|     60 |
+--------+
```

## Aggregate functions and NULL values

Some aggregate functions ignore NULL values. For example, [AVG](functions/avg.md) calculates the average of values `1`, `5`, and `NULL` to be `3`,
based on the following formula:

> `(1 + 5) / 2 = 3`

In both the numerator and the denominator, only the two non-NULL values are used.

If all of the values passed to the aggregate function are NULL, then the aggregate function returns NULL.

Some aggregate functions can be passed more than one column. For example:

```sqlexample
SELECT COUNT(col1, col2) FROM table1;
```

In these instances, the aggregate function ignores a row if any individual column is NULL.

For example, in the following query, [COUNT](functions/count.md) returns `1`, not `4`, because three of the four rows contain at least one NULL
value in the selected columns:

Create a table and populate it with values:

```sqlexample
CREATE OR REPLACE TABLE test_null_aggregate_functions (x INT, y INT);
INSERT INTO test_null_aggregate_functions (x, y) VALUES
  (1, 2),         -- No NULLs.
  (3, NULL),      -- One but not all columns are NULL.
  (NULL, 6),      -- One but not all columns are NULL.
  (NULL, NULL);   -- All columns are NULL.
```

Query the table:

```sqlexample
SELECT COUNT(x, y) FROM test_null_aggregate_functions;
```

```output
+-------------+
| COUNT(X, Y) |
|-------------|
|           1 |
+-------------+
```

If [SUM](functions/sum.md) is called with an expression that references two or more columns, and if one or more of those columns
is NULL, then the expression evaluates to NULL, and the row is ignored:

```sqlexample
SELECT SUM(x + y) FROM test_null_aggregate_functions;
```

```output
+------------+
| SUM(X + Y) |
|------------|
|          3 |
+------------+
```

This behavior differs from the behavior of [GROUP BY](constructs/group-by.md), which does not discard rows when some columns are NULL:

```sqlexample
SELECT x AS X_COL, y AS Y_COL
  FROM test_null_aggregate_functions
  GROUP BY x, y;
```

```output
+-------+-------+
| X_COL | Y_COL |
|-------+-------|
|     1 |     2 |
|     3 |  NULL |
|  NULL |     6 |
|  NULL |  NULL |
+-------+-------+
```
