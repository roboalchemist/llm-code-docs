# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/arraycontainsint.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/arraycontainsint.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/arraycontainsint.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/arraycontainsint.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/arraycontainsint.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/arraycontainsint.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/arraycontainsint.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/arraycontainsint.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/arraycontainsint.md

# Source: https://docs.pinot.apache.org/functions-1/arraycontainsint.md

# arrayContainsInt

Checks if int value exists in array.

## Signature

> arrayContainsInt('colName', valueToFind)

## Usage Examples

These examples are based on the [Hybrid Quick Start](https://docs.pinot.apache.org/basics/getting-started/quick-start#hybrid).

```sql
select DivAirportIDs, 
       arrayContainsInt(DivAirportIDs, 14683) AS containsValue
from airlineStats 
WHERE arraylength(DivAirportIDs) >= 2
limit 5
```

| DivAirportIDs | containsValue |
| ------------- | ------------- |
| 13891,12892   | false         |
| 14683,14683   | true          |
| 12339,12339   | false         |
| 13487,13930   | false         |
| 13029,11292   | false         |
