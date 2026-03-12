# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/minmaxrange.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/minmaxrange.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/minmaxrange.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/minmaxrange.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/minmaxrange.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/minmaxrange.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/minmaxrange.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/minmaxrange.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/minmaxrange.md

# Source: https://docs.pinot.apache.org/functions-1/minmaxrange.md

# minmaxrange

Returns the `max` - `min` value in a group

## Signature

> MINMAXRANGE(colName)

## Usage Examples

These examples are based on the [Batch Quick Start](https://docs.pinot.apache.org/basics/getting-started/quick-start#batch).

```sql
select MINMAXRANGE(yearID) AS value
from baseballStats 
```

| value |
| ----- |
| 142   |
