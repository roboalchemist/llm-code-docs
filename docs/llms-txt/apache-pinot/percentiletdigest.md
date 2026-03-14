# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/percentiletdigest.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/percentiletdigest.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/percentiletdigest.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/percentiletdigest.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/percentiletdigest.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/percentiletdigest.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/percentiletdigest.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/percentiletdigest.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/percentiletdigest.md

# Source: https://docs.pinot.apache.org/functions-1/percentiletdigest.md

# percentiletdigest

Returns the Nth percentile of the group using [T-digest algorithm](https://raw.githubusercontent.com/tdunning/t-digest/master/docs/t-digest-paper/histo.pdf). An optional compression\_factor can be specified to control the accuracy with a tradeoff in memory usage (i.e. higher compression\_factor gives better accuracy but takes more memory). The default compression\_factor is 100.

## Signature

> PERCENTILETDIGEST(colName, percentile)
>
> PERCENTILETDIGEST(colName, percentile, compression\_factor)

## Usage Examples

These examples are based on the [Batch Quick Start](https://docs.pinot.apache.org/basics/getting-started/quick-start#batch).

```sql
select PERCENTILETDIGEST(homeRuns, 50, 1000) AS value
from baseballStats 
```

| value |
| ----- |
| 0     |

```sql
select PERCENTILETDIGEST(homeRuns, 80) AS value
from baseballStats 
```

| value              |
| ------------------ |
| 3.6571905392487856 |

```sql
select PERCENTILETDIGEST(homeRuns, 99.9) AS value
from baseballStats 
```

| value             |
| ----------------- |
| 46.26787306220119 |
