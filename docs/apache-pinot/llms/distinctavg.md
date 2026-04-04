# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/distinctavg.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/distinctavg.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/distinctavg.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/distinctavg.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/distinctavg.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/distinctavg.md

# Source: https://docs.pinot.apache.org/functions-1/distinctavg.md

# DISTINCTAVG

Returns the average of distinct row values in a group

## Signature

`DISTINCTAVG(colName) or avg(distinct col)`

## Usage Examples

These examples are based on the [Batch Quick Start](https://docs.pinot.apache.org/basics/getting-started/quick-start#batch).

```sql
SELECT DISTINCTAVG(runs) AS VALUE
FROM baseballStats
```

| VALUE             |
| ----------------- |
| 83.36526946107784 |

```sql
SELECT AVG(DISTINCT AtBatting) AS VALUE
FROM baseballStats
```

| VALUE             |
| ----------------- |
| 349.1158798283262 |
