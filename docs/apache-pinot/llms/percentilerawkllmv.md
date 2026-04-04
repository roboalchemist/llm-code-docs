# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/percentilerawkllmv.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/percentilerawkllmv.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/percentilerawkllmv.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/percentilerawkllmv.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/percentilerawkllmv.md

# Source: https://docs.pinot.apache.org/functions-1/percentilerawkllmv.md

# percentilerawkllmv

Variant of the `PERCENTILERAWKLL` aggregation function which accepts multi-value columns. Values in the given column are 'flattened' before aggregation.

## Signature

> PercentileRAWKLLMV(column, percentile) -> Double

* `column` (required): Name of the column to aggregate on.
* `percentile` (required): Percentile value to be calculated \[0..100]. For raw versions of the function, this value is used for ordering (ORDER BY).

## Usage Examples

```sql
select percentileKLLMV(ArrOfInts, 90) as value
from MyTable
```

| sketch   |
| -------- |
| BQEPC... |
