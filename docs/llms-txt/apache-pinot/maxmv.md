# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/maxmv.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/maxmv.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/maxmv.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/maxmv.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/maxmv.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/maxmv.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/maxmv.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/maxmv.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/maxmv.md

# Source: https://docs.pinot.apache.org/functions-1/maxmv.md

# MAXMV

Get the maximum value in a group

## Signature

> MAXMV(colName)

## Usage Examples

These examples are based on the [Hybrid Quick Start](https://docs.pinot.apache.org/basics/getting-started/quick-start#hybrid).

```sql
select MAXMV(DivLongestGTimes) AS value
from airlineStats 
where arraylength(DivLongestGTimes) > 1
```

| value |
| ----- |
| 108   |
