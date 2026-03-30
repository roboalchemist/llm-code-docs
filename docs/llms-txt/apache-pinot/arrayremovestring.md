# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/arrayremovestring.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/arrayremovestring.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/arrayremovestring.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/arrayremovestring.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/arrayremovestring.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/arrayremovestring.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/arrayremovestring.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/arrayremovestring.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/arrayremovestring.md

# Source: https://docs.pinot.apache.org/functions-1/arrayremovestring.md

# arrayRemoveString

Removes value from array of strings.

## Signature

> arrayRemoveString('colName', value)

## Usage Examples

These examples are based on the [Hybrid Quick Start](https://docs.pinot.apache.org/basics/getting-started/quick-start#hybrid).

```sql
select RandomAirports, 
       arrayRemoveString(RandomAirports, 'SEA') AS value
from airlineStats 
WHERE arraylength(RandomAirports) BETWEEN 2 AND 4
limit 5
```

| DivAirportIDs   | value       |
| --------------- | ----------- |
| SEA,PSC         | PSC         |
| SEA,PSC,PHX,MSY | PSC,PHX,MSY |
| SEA,PSC,PHX,MSY | PSC,PHX,MSY |
| SEA,PSC         | PSC         |
| SEA,PSC         | PSC         |
