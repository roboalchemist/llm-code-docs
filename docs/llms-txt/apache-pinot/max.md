# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/max.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/max.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/max.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/max.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/max.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/max.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/max.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/max.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/max.md

# Source: https://docs.pinot.apache.org/functions-1/max.md

# max

Get the maximum value in a group

## Signature

> MAX(colName)

## Usage Examples

These examples are based on the [Batch Quick Start](https://docs.pinot.apache.org/basics/getting-started/quick-start#batch).

```sql
select max(homeRuns) AS value
from baseballStats 
```

| value |
| ----- |
| 73    |
