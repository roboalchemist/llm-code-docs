# Source: https://docs.snowflake.com/en/sql-reference/functions/vector_truncate.md

Categories:
:   [Vector functions](../functions-vector.md)

# VECTOR_TRUNCATE

Truncates a [VECTOR](../data-types-vector.md) to a smaller dimension.

This function can also be called through the alias VECTOR_TRUNC.

See also:
:   [Vector Embeddings](../../user-guide/snowflake-cortex/vector-embeddings.md), [VECTOR_NORMALIZE](vector_normalize.md)

## Syntax

```sqlsyntax
VECTOR_TRUNCATE( <vector>, <dimension> )
```

## Arguments

`vector`
:   A single [VECTOR](../data-types-vector.md) value to truncate.

`dimension`
:   The number of elements that should be in the returned vector.

## Returns

Returns a VECTOR value with the same values and types for the first `dimension` entries, with the remainder discarded.

## Usage notes

* Returns NULL when any input is NULL.
* Using a `dimension` larger than the number of dimensions in the `vector` causes an error.
* Truncated vectors are not normalized.

## Examples

This example demonstrates truncating a 3-dimensional vector into a 2-dimensional vector:

```sqlexample
SELECT VECTOR_TRUNCATE([1, 2, 3]::VECTOR(INT, 3), 2);
```

```output
[1,2]
```

This example demonstrates truncating a vector produced by [EMBED_TEXT_768](../../user-guide/snowflake-cortex/vector-embeddings.md) for the text “Analytical databases are typically column-oriented rather than row-oriented” with the `snowflake-arctic-embed-m-v1.5` model from 768 elements to 256 elements:

```sqlexample
SELECT VECTOR_TRUNCATE(
    SNOWFLAKE.CORTEX.EMBED_TEXT_768(
        'snowflake-arctic-embed-m-v1.5',
        'Analytical databases are typically column-oriented rather than row-oriented'
    ),
    256)
;
```
