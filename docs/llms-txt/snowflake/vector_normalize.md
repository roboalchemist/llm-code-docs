# Source: https://docs.snowflake.com/en/sql-reference/functions/vector_normalize.md

Categories:
:   [Vector functions](../functions-vector.md)

# VECTOR_NORMALIZE

Normalizes a [VECTOR](../data-types-vector.md) in the L2 vector space, giving its elements values in the range of [0,1] and giving it a magnitude of 1.

See also:
:   [Vector Embeddings](../../user-guide/snowflake-cortex/vector-embeddings.md), [VECTOR_TRUNCATE](vector_truncate.md)

## Syntax

```sqlsyntax
VECTOR_NORMALIZE( <vector> )
```

## Arguments

`vector`
:   A single VECTOR value to normalize.

## Returns

Returns a VECTOR normalized to the L2 space, with values of type [FLOAT](../data-types-numeric.md).

## Usage notes

* Returns NULL when the input is NULL.
* Vector functions are optimized in a way that can reduce floating point precision. This function’s results have a margin of error up to `1e-4`.

## Examples

This example demonstrates normalizing the vector `[1, 2, 3]`:

```sqlexample
SELECT VECTOR_NORMALIZE([1, 2, 3]::VECTOR(INT, 3));
```

```output
[0.267261, 0.534522, 0.801784]
```

This example shows how to re-normalize a truncated vector. The original vector is produced by [EMBED_TEXT_768](../../user-guide/snowflake-cortex/vector-embeddings.md) with the `snowflake-arctic-embed-m-v1.5` model, and then truncated to 256 elements. The truncated vector is then normalized:

```sqlexample
VECTOR_NORMALIZE(
    VECTOR_TRUNCATE(
        SNOWFLAKE.CORTEX.EMBED_TEXT_768(
            'snowflake-arctic-embed-m-v1.5',
            'Analytical databases are typically column-oriented rather than row-oriented'
        ),
        256
    )
);
```
