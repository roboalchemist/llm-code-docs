# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/arrayindexofstring.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/arrayindexofstring.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/arrayindexofstring.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/arrayindexofstring.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/arrayindexofstring.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/arrayindexofstring.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/arrayindexofstring.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/arrayindexofstring.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/arrayindexofstring.md

# Source: https://docs.pinot.apache.org/functions-1/arrayindexofstring.md

# arrayIndexOfString

Finds the last index of the given value in the array starting at the given index.

## Signature

> arrayIndexOfString('colName', valueToFind)

## Usage Examples

These examples are based on the [Hybrid Quick Start](https://docs.pinot.apache.org/basics/getting-started/quick-start#hybrid).

```sql
select DivTailNums, 
       arrayIndexOfString(DivTailNums, 'N7713A') AS index
from airlineStats 
WHERE arraylength(DivTailNums) >= 2
limit 5
```

| DivTailNums   | index |
| ------------- | ----- |
| N7713A,N7713A | 0     |
| N344AA,N344AA | -1    |
| N7713A,N7713A | 0     |
