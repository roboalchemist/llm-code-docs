# Source: https://docs.snowflake.com/en/sql-reference/functions/bitmap_or_agg.md

Categories:
:   [Aggregate functions](../functions-aggregation.md) (Counting Distinct Values)

# BITMAP_OR_AGG

Returns a bitmap containing the results of a binary OR operation on the input bitmaps.

See also:
:   [Using Bitmaps to Compute Distinct Values for Hierarchical Aggregations](../../user-guide/querying-bitmaps-for-distinct-counts.md)

## Syntax

```sqlsyntax
BITMAP_OR_AGG( <bitmap> )
```

## Arguments

`bitmap`
:   A bitmap returned by the [BITMAP_CONSTRUCT_AGG](bitmap_construct_agg.md) or BITMAP_OR_AGG function.

## Returns

The function returns a bitmap containing the results of a binary OR operation on the input bitmaps.

## Examples

See [Using Bitmaps to Compute Distinct Values for Hierarchical Aggregations](../../user-guide/querying-bitmaps-for-distinct-counts.md).
