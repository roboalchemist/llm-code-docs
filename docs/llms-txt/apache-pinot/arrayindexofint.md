# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/arrayindexofint.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/arrayindexofint.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/arrayindexofint.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/arrayindexofint.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/arrayindexofint.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/arrayindexofint.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/arrayindexofint.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/arrayindexofint.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/arrayindexofint.md

# Source: https://docs.pinot.apache.org/functions-1/arrayindexofint.md

# arrayIndexOfInt

Finds the last index of the given value in the array starting at the given index.

## Signature

> arrayIndexOfInt('colName', valueToFind)

## Usage Examples

These examples are based on the [Hybrid Quick Start](https://docs.pinot.apache.org/basics/getting-started/quick-start#hybrid).

```sql
select DivAirportIDs, 
       arrayIndexOfInt(DivAirportIDs, 14683) AS index
from airlineStats 
WHERE arraylength(DivAirportIDs) >= 2
limit 5
```

| DivAirportIDs | index |
| ------------- | ----- |
| 13891,12892   | -1    |
| 14683,14683   | 0     |
| 12339,12339   | -1    |
| 13487,13930   | -1    |
| 13029,11292   | -1    |
