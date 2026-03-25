# Source: https://docs.snowflake.com/en/sql-reference/functions-vector.md

# Vector functions

Snowflake provides both similarity and element-wise aggregation functions for the [VECTOR](data-types-vector.md) data type. These functions allow for finding vectors nearest to a source vector, used for semantic search and fine-tuning generative responses from LLMs and generative AI.

Similarity functions operate on two VECTOR arguments of equal element type and dimension, computing the specified metric. Snowflake provides the following vector similarity functions:

> * [VECTOR_INNER_PRODUCT](functions/vector_inner_product.md)
> * [VECTOR_L1_DISTANCE](functions/vector_l1_distance.md)
> * [VECTOR_L2_DISTANCE](functions/vector_l2_distance.md)
> * [VECTOR_COSINE_SIMILARITY](functions/vector_cosine_similarity.md)

Vector manipulation functions take an existing vector and return a new vector with different properties, such as truncation or normalization. Snowflake provides the following vector manipulation functions:

> * [VECTOR_TRUNCATE](functions/vector_truncate.md)
> * [VECTOR_NORMALIZE](functions/vector_normalize.md)

Vector aggregate functions operate on columns of VECTOR values to perform element-wise mathematical operations such as sum, average, minimum, and maximum across all vectors in a group. Snowflake provides the following vector aggregation functions:

> * [VECTOR_SUM](functions/vector_sum.md)
> * [VECTOR_MIN](functions/vector_min.md)
> * [VECTOR_MAX](functions/vector_max.md)
> * [VECTOR_AVG](functions/vector_avg.md)

> **Note:**
>
> Vector functions on Snowflake are optimized in a way that can reduce floating point precision. These functions have a margin of error up to `1e-4`.

## List of functions

| Function Name | Notes |
| --- | --- |
| [VECTOR_INNER_PRODUCT](functions/vector_inner_product.md) |  |
| [VECTOR_L1_DISTANCE](functions/vector_l1_distance.md) |  |
| [VECTOR_L2_DISTANCE](functions/vector_l2_distance.md) |  |
| [VECTOR_COSINE_SIMILARITY](functions/vector_cosine_similarity.md) | Not supported in Snowpark API. |
| [VECTOR_TRUNCATE](functions/vector_truncate.md) |  |
| [VECTOR_NORMALIZE](functions/vector_normalize.md) |  |
| [VECTOR_SUM](functions/vector_sum.md) |  |
| [VECTOR_MIN](functions/vector_min.md) |  |
| [VECTOR_MAX](functions/vector_max.md) |  |
| [VECTOR_AVG](functions/vector_avg.md) |  |
