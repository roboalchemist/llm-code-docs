# Source: https://docs.snowflake.com/en/sql-reference/functions/vector_max.md

Categories:
:   [Vector functions](../functions-vector.md) , [Aggregate functions](../functions-aggregation.md)

# VECTOR_MAX

Computes the element-wise maximum of [vectors](../../user-guide/snowflake-cortex/vector-embeddings.md) in an aggregate. Returns a vector where
each element is the maximum of the corresponding elements across all input vectors.

See also:
:   [VECTOR_SUM](vector_sum.md) , [VECTOR_MIN](vector_min.md) , [VECTOR_AVG](vector_avg.md) , [MAX](max.md), [Vector Embeddings](../../user-guide/snowflake-cortex/vector-embeddings.md)

## Syntax

```sqlsyntax
VECTOR_MAX( <vector_column> )
```

## Arguments

`vector_column`
:   A column containing [VECTOR](../data-types-vector.md) values. All vectors in the column must have the same element type and dimension.

## Returns

Returns a VECTOR value with the same element type and dimension as the input vectors. Each element in the result vector is the maximum of the corresponding elements across all input vectors.

## Usage notes

* NULL values are ignored in the aggregation.
* If all values in the group are NULL, the function returns NULL.
* All input vectors in the column must have the same dimension and element type.
* Vector functions are optimized in a way that can reduce floating point precision. This function’s results have a margin of error up to `1e-4`.

## Examples

This example demonstrates computing the element-wise maximum of vectors:

```sqlexample
CREATE OR REPLACE TABLE vector_data (
  id INT,
  category VARCHAR,
  embedding VECTOR(FLOAT, 3)
);

INSERT INTO vector_data
SELECT 1, 'A', [1.5, 8.0, 3.2]::VECTOR(FLOAT, 3)
UNION ALL SELECT 2, 'A', [4.1, 2.5, 6.7]::VECTOR(FLOAT, 3)
UNION ALL SELECT 3, 'B', [2.0, 1.0, 4.0]::VECTOR(FLOAT, 3)
UNION ALL SELECT 4, 'B', [3.0, 2.0, 1.0]::VECTOR(FLOAT, 3);

-- Compute maximum for each category
SELECT category, VECTOR_MAX(embedding) AS max_vector
  FROM vector_data
  GROUP BY category
  ORDER BY category;
```

```output
+----------+------------------+
| CATEGORY | MAX_VECTOR       |
+----------+------------------+
| A        | [4.1, 8.0, 6.7] |
| B        | [3.0, 2.0, 4.0] |
+----------+------------------+
```

This example shows scalar aggregation (no GROUP BY):

```sqlexample
SELECT VECTOR_MAX(embedding) AS overall_max
  FROM vector_data;
```

```output
+------------------+
| OVERALL_MAX      |
+------------------+
| [4.1, 8.0, 6.7]  |
+------------------+
```
