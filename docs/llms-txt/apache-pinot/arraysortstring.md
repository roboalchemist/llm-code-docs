# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/arraysortstring.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/arraysortstring.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/arraysortstring.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/arraysortstring.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/arraysortstring.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/arraysortstring.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/arraysortstring.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/arraysortstring.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/arraysortstring.md

# Source: https://docs.pinot.apache.org/functions-1/arraysortstring.md

# arraySortString

Sorts array of strings.

## Signature

> arraySortString('colName')

## Usage Examples

These examples are based on the [Hybrid Quick Start](https://docs.pinot.apache.org/basics/getting-started/quick-start#hybrid).

```sql
select FlightNum, 
       arraySortString(RandomAirports) AS sortedAirports, 
       RandomAirports
from airlineStats 
WHERE arraylength(RandomAirports) BETWEEN 2 AND 4
limit 5
```

| FlightNum | sortedAirports  | RandomAirports  |
| --------- | --------------- | --------------- |
| 3846      | PSC,SEA         | SEA,PSC         |
| 3635      | MSY,PHX,PSC,SEA | SEA,PSC,PHX,MSY |
| 429       | MSY,PHX,PSC,SEA | SEA,PSC,PHX,MSY |
| 1206      | PSC,SEA         | SEA,PSC         |
| 5300      | PSC,SEA         | SEA,PSC         |
