# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/distinctavgmv.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/distinctavgmv.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/distinctavgmv.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/distinctavgmv.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/distinctavgmv.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/distinctavgmv.md

# Source: https://docs.pinot.apache.org/functions-1/distinctavgmv.md

# DISTINCTAVGMV

Returns the average of distinct row values in a group

## Signature

> DISTINCTAVGMV(colName)

## Usage Examples

These examples are based on the [Hybrid Quick Start](https://docs.pinot.apache.org/basics/getting-started/quick-start#hybrid).

```sql
SELECT DISTINCTAVGMV(DivLongestGTimes) AS VALUE
FROM airlineStats
WHERE arraylength(DivLongestGTimes) > 1
```

| VALUE |
| ----- |
| 32.4  |
