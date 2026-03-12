# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/arraydistinctint.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/arraydistinctint.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/arraydistinctint.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/arraydistinctint.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/arraydistinctint.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/arraydistinctint.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/arraydistinctint.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/arraydistinctint.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/arraydistinctint.md

# Source: https://docs.pinot.apache.org/functions-1/arraydistinctint.md

# arrayDistinctInt

Returns unique values in an array of ints.

## Signature

> arrayDistinctInt('colName')

## Usage Examples

These examples are based on the [Hybrid Quick Start](https://docs.pinot.apache.org/basics/getting-started/quick-start#hybrid).

```sql
select DivAirportIDs, 
       arrayDistinctInt(DivAirportIDs) AS unique
from airlineStats 
WHERE arraylength(DivAirportIDs) >= 2
limit 5
```

| DivAirportIDs | unique      |
| ------------- | ----------- |
| 15016,11066   | 15016,11066 |
| 10620,14869   | 10620,14869 |
| 13891,12892   | 13891,12892 |
| 12264,10397   | 12264,10397 |
| 11066,12892   | 11066,12892 |
