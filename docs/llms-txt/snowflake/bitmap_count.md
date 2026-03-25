# Source: https://docs.snowflake.com/en/sql-reference/functions/bitmap_count.md

Categories:
:   [Aggregate functions](../functions-aggregation.md) (Counting Distinct Values)

# BITMAP_COUNT

Given a bitmap that represents the set of distinct values for a column, returns the number of distinct value.

See also:
:   [Using Bitmaps to Compute Distinct Values for Hierarchical Aggregations](../../user-guide/querying-bitmaps-for-distinct-counts.md)

## Syntax

```sqlsyntax
BITMAP_COUNT( <bitmap> )
```

## Arguments

`bitmap`
:   This expression must evaluate to a bitmap returned by the [BITMAP_CONSTRUCT_AGG](bitmap_construct_agg.md) or [BITMAP_OR_AGG](bitmap_or_agg.md) functions.

## Returns

The function returns the number of distinct values in a column, as represented by the bits set in the input bitmap.

## Examples

See [Using Bitmaps to Compute Distinct Values for Hierarchical Aggregations](../../user-guide/querying-bitmaps-for-distinct-counts.md).
