# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/percentileest.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/percentileest.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/percentileest.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/percentileest.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/percentileest.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/percentileest.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/percentileest.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/percentileest.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/percentileest.md

# Source: https://docs.pinot.apache.org/functions-1/percentileest.md

# percentileest

Returns the Nth percentile of the group using [Quantile Digest](https://github.com/airlift/airlift/blob/master/stats/src/main/java/io/airlift/stats/QuantileDigest.java) algorithm.

## Signature

> percentileest(colName, percentile)

## Usage Examples

These examples are based on the [Batch Quick Start](https://docs.pinot.apache.org/basics/getting-started/quick-start#batch).

```sql
select percentileest(homeRuns, 50) AS value
from baseballStats 
```

| value |
| ----- |
| 0     |

```sql
select percentileest(homeRuns, 80) AS value
from baseballStats 
```

| value |
| ----- |
| 4     |

```sql
select percentileest(homeRuns, 99.9) AS value
from baseballStats 
```

| value |
| ----- |
| 46    |
