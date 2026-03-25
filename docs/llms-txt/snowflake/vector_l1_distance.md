# Source: https://docs.snowflake.com/en/sql-reference/functions/vector_l1_distance.md

Categories:
:   [Vector functions](../functions-vector.md)

# VECTOR_L1_DISTANCE

Computes the L1 distance between two [vectors](../../user-guide/snowflake-cortex/vector-embeddings.md).

L1 distance, also known as the Taxicab or Manhattan distance, is a measure of
the distance between two points in a vector space. The distance is calculated by
taking the sum of the absolute value of the differences of vector elements. The
result is a value of zero or higher. If the distance is zero, the vectors
are identical. The larger the distance, the farther apart the vectors are.

See also:
:   [VECTOR_INNER_PRODUCT](vector_inner_product.md) , [VECTOR_L2_DISTANCE](vector_l2_distance.md) , [VECTOR_COSINE_SIMILARITY](vector_cosine_similarity.md) , [Vector Embeddings](../../user-guide/snowflake-cortex/vector-embeddings.md)

## Syntax

```sqlsyntax
VECTOR_L1_DISTANCE( <vector>, <vector> )
```

## Arguments

`vector`
:   The [VECTOR](../data-types-vector.md) value to calculate the distance from.

`vector`
:   The VECTOR value to calculate the distance to.

## Returns

Returns the L1 distance between the two input vectors as a [FLOAT](../data-types-numeric.md) value.

## Usage notes

* Vector functions are optimized in a way that can reduce floating point precision. This function’s results have a margin of error up to `1e-4`.

## Examples

This example uses the VECTOR_L1_DISTANCE function to determine which vectors in
the table are closest to each other between columns `a` and `b`:

```sqlexample
CREATE TABLE vectors (a VECTOR(FLOAT, 3), b VECTOR(FLOAT, 3));
INSERT INTO vectors SELECT [1.1,2.2,3]::VECTOR(FLOAT,3), [1,1,1]::VECTOR(FLOAT,3);
INSERT INTO vectors SELECT [1,2.2,3]::VECTOR(FLOAT,3), [4,6,8]::VECTOR(FLOAT,3);

SELECT VECTOR_L1_DISTANCE(a, b) FROM vectors;
```

```output
+--------------+
| 3.300000191  |
|--------------|
| 11.800000191 |
+--------------+
```
