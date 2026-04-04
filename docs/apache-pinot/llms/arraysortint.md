# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/arraysortint.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/arraysortint.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/arraysortint.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/arraysortint.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/arraysortint.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/arraysortint.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/arraysortint.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/arraysortint.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/arraysortint.md

# Source: https://docs.pinot.apache.org/functions-1/arraysortint.md

# arraySortInt

Sorts array of ints.

## Signature

> arraySortInt('colName')

## Usage Examples

These examples are based on the [Hybrid Quick Start](https://docs.pinot.apache.org/basics/getting-started/quick-start#hybrid).

```sql
select DivAirportIDs, 
       arraySortInt(DivAirportIDs) AS sortedIds
from airlineStats 
WHERE arraylength(DivAirportIDs) >= 2
limit 5
```

| DivAirportIDs | sortedIds   |
| ------------- | ----------- |
| 13891,12892   | 12892,13891 |
| 14683,14683   | 14683,14683 |
| 12339,12339   | 12339,12339 |
| 13198,10721   | 10721,13198 |
| 10721,12478   | 10721,12478 |
