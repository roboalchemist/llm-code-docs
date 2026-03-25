# Source: https://docs.snowflake.com/en/sql-reference/functions/bitmap_construct_agg.md

Categories:
:   [Aggregate functions](../functions-aggregation.md) (Counting Distinct Values)

# BITMAP_CONSTRUCT_AGG

Returns a bitmap with bits set for each distinct value in a group.

See also:
:   [Using Bitmaps to Compute Distinct Values for Hierarchical Aggregations](../../user-guide/querying-bitmaps-for-distinct-counts.md)

## Syntax

```sqlsyntax
BITMAP_CONSTRUCT_AGG( <relative_position> )
```

## Arguments

`relative_position`
:   The relative position of a bit for a value (returned by the [BITMAP_BIT_POSITION](bitmap_bit_position.md) function).

## Returns

The function returns a BINARY value that is a bitmap with bits set for each distinct value in a group.

## Examples

See [Using Bitmaps to Compute Distinct Values for Hierarchical Aggregations](../../user-guide/querying-bitmaps-for-distinct-counts.md).
