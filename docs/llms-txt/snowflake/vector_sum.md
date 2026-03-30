# Source: https://docs.snowflake.com/en/sql-reference/functions/vector_sum.md

Categories:
:   [Vector functions](../functions-vector.md) , [Aggregate functions](../functions-aggregation.md)

# VECTOR_SUM

Computes the element-wise sum of [vectors](../../user-guide/snowflake-cortex/vector-embeddings.md) in an aggregate. Returns a vector where
each element is the sum of the corresponding elements across all input vectors.

See also:
:   [VECTOR_MIN](vector_min.md) , [VECTOR_MAX](vector_max.md) , [VECTOR_AVG](vector_avg.md) , [SUM](sum.md), [Vector Embeddings](../../user-guide/snowflake-cortex/vector-embeddings.md)

## Syntax

```sqlsyntax
VECTOR_SUM( <vector_column> )
```

## Arguments

`vector_column`
:   A column containing [VECTOR](../data-types-vector.md) values. All vectors in the column must have the same element type and dimension.

## Returns

Returns a VECTOR value with the same element type and dimension as the input vectors. Each element in the result vector is the sum of the corresponding elements across all input vectors.

## Usage notes

* NULL values are ignored in the aggregation.
* If all values in the group are NULL, the function returns NULL.
* All input vectors in the column must have the same dimension and element type.
* Vector functions are optimized in a way that can reduce floating point precision. This function’s results have a margin of error up to `1e-4`.

## Examples

This example demonstrates computing the element-wise sum of vectors:

```sqlexample
CREATE OR REPLACE TABLE vector_data (
  id INT,
  category VARCHAR,
  embedding VECTOR(FLOAT, 3)
);

INSERT INTO vector_data
SELECT 1, 'A', [1.0, 2.0, 3.0]::VECTOR(FLOAT, 3)
UNION ALL SELECT 2, 'A', [4.0, 5.0, 6.0]::VECTOR(FLOAT, 3)
UNION ALL SELECT 3, 'B', [2.0, 1.0, 4.0]::VECTOR(FLOAT, 3)
UNION ALL SELECT 4, 'B', [3.0, 2.0, 1.0]::VECTOR(FLOAT, 3);

-- Compute sum for each category
SELECT category, VECTOR_SUM(embedding) AS sum_vector
  FROM vector_data
  GROUP BY category
  ORDER BY category;
```

```output
+----------+------------------+
| CATEGORY | SUM_VECTOR       |
+----------+------------------+
| A        | [5.0, 7.0, 9.0]  |
| B        | [5.0, 3.0, 5.0]  |
+----------+------------------+
```

This example shows scalar aggregation (no GROUP BY):

```sqlexample
SELECT VECTOR_SUM(embedding) AS total_sum
  FROM vector_data;
```

```output
+--------------------+
| TOTAL_SUM          |
+--------------------+
| [10.0, 10.0, 14.0] |
+--------------------+
```
