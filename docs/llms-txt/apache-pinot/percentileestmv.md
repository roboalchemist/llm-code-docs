# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/percentileestmv.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/percentileestmv.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/percentileestmv.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/percentileestmv.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/percentileestmv.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/percentileestmv.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/percentileestmv.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/percentileestmv.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/percentileestmv.md

# Source: https://docs.pinot.apache.org/functions-1/percentileestmv.md

# percentileestmv

Returns the Nth percentile of the group using [Quantile Digest](https://github.com/airlift/airlift/blob/master/stats/src/main/java/io/airlift/stats/QuantileDigest.java) algorithm.

## Signature

> PERCENTILEESTMV(colName, N)

## Usage Examples

These examples are based on the [Hybrid Quick Start](https://docs.pinot.apache.org/basics/getting-started/quick-start#hybrid).

```sql
select PERCENTILEESTMV(DivLongestGTimes, 50) AS value
from airlineStats 
where arraylength(DivLongestGTimes) > 1
```

| value |
| ----- |
| 10    |

```sql
select PERCENTILEESTMV(DivLongestGTimes, 90) AS value
from airlineStats 
where arraylength(DivLongestGTimes) > 1
```

| value |
| ----- |
| 44    |

```sql
select PERCENTILEESTMV(DivLongestGTimes, 99.9) AS value
from airlineStats 
where arraylength(DivLongestGTimes) > 1
```

| value |
| ----- |
| 108   |
