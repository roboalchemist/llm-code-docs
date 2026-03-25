# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/distinctsummv.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/distinctsummv.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/distinctsummv.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/distinctsummv.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/distinctsummv.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/distinctsummv.md

# Source: https://docs.pinot.apache.org/functions-1/distinctsummv.md

# DISTINCTSUMMV

Returns the sum of the distinct row values in a group

## Signature

> DISTINCTSUMMV(colName)

### Usage Examples <a href="#usage-examples" id="usage-examples"></a>

These examples are based on the [Hybrid Quick Start](https://docs.pinot.apache.org/basics/getting-started/quick-start#hybrid).

```sql
SELECT DISTINCTSUMMV(DivLongestGTimes) AS VALUE
FROM airlineStats
WHERE arraylength(DivLongestGTimes) > 1
```

| VALUE |
| ----- |
| 1134  |
