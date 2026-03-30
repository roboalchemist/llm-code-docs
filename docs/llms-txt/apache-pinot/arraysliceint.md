# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/arraysliceint.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/arraysliceint.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/arraysliceint.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/arraysliceint.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/arraysliceint.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/arraysliceint.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/arraysliceint.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/arraysliceint.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/arraysliceint.md

# Source: https://docs.pinot.apache.org/functions-1/arraysliceint.md

# arraySliceInt

Returns the values in the array between the start and end positions.

## Signature

> arraySliceInt('colName', start, end)

## Usage Examples

These examples are based on the [Hybrid Quick Start](https://docs.pinot.apache.org/basics/getting-started/quick-start#hybrid).

```sql
select FlightNum, 
       arraySliceInt(DivAirportIDs, 0, 1) AS airports, 
      DivAirportIDs
from airlineStats 
WHERE arraylength(DivAirportIDs) >= 2
limit 5
```

| FlightNum | airports | DivAirportIDs |
| --------- | -------- | ------------- |
| 1531      | 13891    | 13891,12892   |
| 19        | 14683    | 14683,14683   |
| 829       | 12339    | 12339,12339   |
| 24        | 13198    | 13198,10721   |
| 548       | 10721    | 10721,12478   |
