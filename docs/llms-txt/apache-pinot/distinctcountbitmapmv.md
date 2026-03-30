# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/distinctcountbitmapmv.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/distinctcountbitmapmv.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/distinctcountbitmapmv.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/distinctcountbitmapmv.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/distinctcountbitmapmv.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/distinctcountbitmapmv.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/distinctcountbitmapmv.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/distinctcountbitmapmv.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/distinctcountbitmapmv.md

# Source: https://docs.pinot.apache.org/functions-1/distinctcountbitmapmv.md

# DISTINCTCOUNTBITMAPMV

Returns the count of distinct row values in a group. This function is accurate for an INT or dictionary encoded column, but approximate for other cases where hash codes are used in distinct counting and there may be hash collision.

## Signature

> DISTINCTCOUNTBITMAPMV(colName)

## Usage Examples

These examples are based on the [Hybrid Quick Start](https://docs.pinot.apache.org/basics/getting-started/quick-start#hybrid).

```sql
select DISTINCTCOUNTBITMAPMV(DivLongestGTimes) AS value
from airlineStats 
where arraylength(DivLongestGTimes) > 1
```

| value |
| ----- |
| 34    |

```sql
select DISTINCTCOUNTBITMAPMV(DivTailNums) AS value
from airlineStats 
where arraylength(DivTailNums) > 1
```

| value |
| ----- |
| 2     |
