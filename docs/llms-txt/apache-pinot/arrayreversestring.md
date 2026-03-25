# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/arrayreversestring.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/arrayreversestring.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/arrayreversestring.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/arrayreversestring.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/arrayreversestring.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/arrayreversestring.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/arrayreversestring.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/arrayreversestring.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/arrayreversestring.md

# Source: https://docs.pinot.apache.org/functions-1/arrayreversestring.md

# arrayReverseString

Reverses array of strings.

## Signature

> arrayReverseString('colName')

## Usage Examples

These examples are based on the [Hybrid Quick Start](https://docs.pinot.apache.org/basics/getting-started/quick-start#hybrid).

```sql
select FlightNum, 
       arrayReverseString(RandomAirports) AS reversedAirports, 
       RandomAirports
from airlineStats 
WHERE arraylength(RandomAirports) BETWEEN 2 AND 4
limit 5
```

| FlightNum | reversedAirports | RandomAirports  |
| --------- | ---------------- | --------------- |
| 1206      | PSC,SEA          | SEA,PSC         |
| 5300      | PSC,SEA          | SEA,PSC         |
| 3359      | MSY,PHX,PSC,SEA  | SEA,PSC,PHX,MSY |
| 1023      | PHX,PSC,SEA      | SEA,PSC,PHX     |
| 963       | MSY,PHX,PSC,SEA  | SEA,PSC,PHX,MSY |
