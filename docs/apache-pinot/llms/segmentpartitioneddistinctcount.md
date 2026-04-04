# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/segmentpartitioneddistinctcount.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/segmentpartitioneddistinctcount.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/segmentpartitioneddistinctcount.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/segmentpartitioneddistinctcount.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/segmentpartitioneddistinctcount.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/segmentpartitioneddistinctcount.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/segmentpartitioneddistinctcount.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/segmentpartitioneddistinctcount.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/segmentpartitioneddistinctcount.md

# Source: https://docs.pinot.apache.org/functions-1/segmentpartitioneddistinctcount.md

# SEGMENTPARTITIONEDDISTINCTCOUNT

Returns the count of distinct values of a column when the column is pre-partitioned for each segment, where there is no common value within different segments. This function calculates the exact count of distinct values within the segment, then simply sums up the results from different segments to get the final result.

{% hint style="warning" %}
This function relies on the expression values being partitioned for each segment, where there are no common values within different segments.
{% endhint %}

## Signature

> SEGMENTPARTITIONEDDISTINCTCOUNT(colName)

## Usage Examples

These examples are based on the [Batch Quick Start](https://docs.pinot.apache.org/basics/getting-started/quick-start#batch).

```sql
select SEGMENTPARTITIONEDDISTINCTCOUNT(teamID) AS value
from baseballStats 
```

| value |
| ----- |
| 149   |
