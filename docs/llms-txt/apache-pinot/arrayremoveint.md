# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/arrayremoveint.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/arrayremoveint.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/arrayremoveint.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/arrayremoveint.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/arrayremoveint.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/arrayremoveint.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/arrayremoveint.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/arrayremoveint.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/arrayremoveint.md

# Source: https://docs.pinot.apache.org/functions-1/arrayremoveint.md

# arrayRemoveInt

Removes value from array of ints.

## Signature

> arrayRemoveInt('colName', value)

## Usage Examples

These examples are based on the [Hybrid Quick Start](https://docs.pinot.apache.org/basics/getting-started/quick-start#hybrid).

```sql
select DivAirportIDs, 
       arrayRemoveInt(DivAirportIDs, 12892) AS value
from airlineStats 
WHERE arraylength(DivAirportIDs) >= 2
AND arrayContainsInt(DivAirportIDs, 12892) = 1
limit 5
```

| DivAirportIDs | value |
| ------------- | ----- |
| 13891,12892   | 13891 |
| 13198,12892   | 13198 |
| 11066,12892   | 11066 |
| 13198,12892   | 13198 |
| 13891,12892   | 13891 |
