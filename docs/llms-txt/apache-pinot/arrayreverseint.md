# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/arrayreverseint.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/arrayreverseint.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/arrayreverseint.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/arrayreverseint.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/arrayreverseint.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/arrayreverseint.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/arrayreverseint.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/arrayreverseint.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/arrayreverseint.md

# Source: https://docs.pinot.apache.org/functions-1/arrayreverseint.md

# arrayReverseInt

Reverses array of ints.

## Signature

> arrayReverseInt('colName')

## Usage Examples

These examples are based on the [Hybrid Quick Start](https://docs.pinot.apache.org/basics/getting-started/quick-start#hybrid).

```sql
select DivAirportIDs, 
       arrayReverseInt(DivAirportIDs) AS reversedIds
from airlineStats 
WHERE arraylength(DivAirportIDs) >= 2
limit 5
```

| DivAirportIDs | reversedIds |
| ------------- | ----------- |
| 13891,12892   | 12892,13891 |
| 14683,14683   | 14683,14683 |
| 12339,12339   | 12339,12339 |
| 13487,13930   | 13930,13487 |
| 13029,11292   | 11292,13029 |
