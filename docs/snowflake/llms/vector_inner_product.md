# Source: https://docs.snowflake.com/en/sql-reference/functions/vector_inner_product.md

Categories:
:   [Vector functions](../functions-vector.md)

# VECTOR_INNER_PRODUCT

Computes the inner product of two [vectors](../../user-guide/snowflake-cortex/vector-embeddings.md).

The inner product (also known as the dot or scalar product) multiplies two vectors. The result represents the combined direction
of the two vectors. Similar vectors result in larger inner products than dissimilar ones.

See also:
:   [VECTOR_COSINE_SIMILARITY](vector_cosine_similarity.md) , [VECTOR_L1_DISTANCE](vector_l1_distance.md) , [VECTOR_L2_DISTANCE](vector_l2_distance.md) , [Vector Embeddings](../../user-guide/snowflake-cortex/vector-embeddings.md)

## Syntax

```sqlsyntax
VECTOR_INNER_PRODUCT( <vector>, <vector> )
```

## Arguments

`vector`
:   First [VECTOR](../data-types-vector.md) value.

`vector`
:   Second VECTOR value.

## Returns

Returns a REAL that is the inner product of the two vectors given as inputs.

## Usage notes

* Vector functions are optimized in a way that can reduce floating point precision. This function’s results have a margin of error up to `1e-4`.

## Examples

This example uses the VECTOR_INNER_PRODUCT function to determine which vectors in the table
are closest to each other between columns `a` and `b`:

```sqlexample
CREATE TABLE vectors (a VECTOR(FLOAT, 3), b VECTOR(FLOAT, 3));
INSERT INTO vectors SELECT [1.1,2.2,3]::VECTOR(FLOAT,3), [1,1,1]::VECTOR(FLOAT,3);
INSERT INTO vectors SELECT [1,2.2,3]::VECTOR(FLOAT,3), [4,6,8]::VECTOR(FLOAT,3);

-- Compute the pairwise inner product between columns a and b
SELECT VECTOR_INNER_PRODUCT(a, b) FROM vectors;
```

```output
+------+
| 6.3  |
|------|
| 41.2 |
+------+
```
