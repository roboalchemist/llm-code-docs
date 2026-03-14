# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/percentilemv.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/percentilemv.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/percentilemv.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/percentilemv.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/percentilemv.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/percentilemv.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/percentilemv.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/percentilemv.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/percentilemv.md

# Source: https://docs.pinot.apache.org/functions-1/percentilemv.md

# percentilemv

Returns the Nth percentile of the group where N is a decimal number between 0 and 100 inclusive

## Signature

> PERCENTILEMV(colName, N)

## Usage Examples

These examples are based on the [Hybrid Quick Start](https://docs.pinot.apache.org/basics/getting-started/quick-start#hybrid).

```sql
select PERCENTILEMV(DivLongestGTimes, 50) AS value
from airlineStats 
where arraylength(DivLongestGTimes) > 1
```

| value |
| ----- |
| 10    |

```sql
select PERCENTILEMV(DivLongestGTimes, 90) AS value
from airlineStats 
where arraylength(DivLongestGTimes) > 1
```

| value |
| ----- |
| 44    |

```sql
select PERCENTILEMV(DivLongestGTimes, 99.9) AS value
from airlineStats 
where arraylength(DivLongestGTimes) > 1
```

| value |
| ----- |
| 108   |
