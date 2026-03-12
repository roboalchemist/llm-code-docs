# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/arrayslicestring.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/arrayslicestring.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/arrayslicestring.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/arrayslicestring.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/arrayslicestring.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/arrayslicestring.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/arrayslicestring.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/arrayslicestring.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/arrayslicestring.md

# Source: https://docs.pinot.apache.org/functions-1/arrayslicestring.md

# arraySliceString

Returns the values in the array between the start and end positions.

## Signature

> arraySliceString('colName', start, end)

## Usage Examples

These examples are based on the [Hybrid Quick Start](https://docs.pinot.apache.org/basics/getting-started/quick-start#hybrid).

```sql
select FlightNum, 
       arraySliceString(RandomAirports, 0, 2) AS airports, 
       RandomAirports
from airlineStats 
WHERE arraylength(RandomAirports) BETWEEN 2 AND 4
limit 5
```

| FlightNum | airports | RandomAirports  |
| --------- | -------- | --------------- |
| 671       | SEA,PSC  | SEA,PSC,PHX,MSY |
| 1767      | SEA,PSC  | SEA,PSC,PHX     |
| 2522      | SEA,PSC  | SEA,PSC         |
| 424       | SEA,PSC  | SEA,PSC,PHX,MSY |
| 3162      | SEA,PSC  | SEA,PSC,PHX,MSY |
