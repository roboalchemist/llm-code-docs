# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/count.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/count.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/count.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/count.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/count.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/count.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/count.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/count.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/count.md

# Source: https://docs.pinot.apache.org/functions-1/count.md

# count

Get the count of rows in a group

## Signature

> COUNT(colName)

## Usage Examples

These examples are based on the [Batch Quick Start](https://docs.pinot.apache.org/basics/getting-started/quick-start#batch).

```sql
select count(*) AS value
from baseballStats 
```

| value |
| ----- |
| 97889 |
