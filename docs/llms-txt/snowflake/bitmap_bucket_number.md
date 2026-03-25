# Source: https://docs.snowflake.com/en/sql-reference/functions/bitmap_bucket_number.md

Categories:
:   [Aggregate functions](../functions-aggregation.md) (Counting Distinct Values)

# BITMAP_BUCKET_NUMBER

Given a numeric value, returns an identifier (“bucket number”) for the bitmap containing the bit that represents the value..

See also:
:   [Using Bitmaps to Compute Distinct Values for Hierarchical Aggregations](../../user-guide/querying-bitmaps-for-distinct-counts.md)

## Syntax

```sqlsyntax
BITMAP_BUCKET_NUMBER( <numeric_expr> )
```

## Arguments

`numeric_expr`
:   This expression must evaluate to a data type that can be cast to NUMBER.

## Returns

The function returns a number that identifies the bitmap containing the bit that represents the value.

## Examples

See [Using Bitmaps to Compute Distinct Values for Hierarchical Aggregations](../../user-guide/querying-bitmaps-for-distinct-counts.md).
