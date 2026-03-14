# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/arrayunionstring.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/arrayunionstring.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/arrayunionstring.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/arrayunionstring.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/arrayunionstring.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/arrayunionstring.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/arrayunionstring.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/arrayunionstring.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/arrayunionstring.md

# Source: https://docs.pinot.apache.org/functions-1/arrayunionstring.md

# arrayUnionString

Create a union of two arrays of strings.

## Signature

> arrayUnionString('colName1', 'colName2')

## Usage Examples

These examples are based on the [Hybrid Quick Start](https://docs.pinot.apache.org/basics/getting-started/quick-start#hybrid).

```sql
select DivTailNums, 
       DivAirports,
       arrayUnionString(DivTailNums, DivAirports) AS unionIds
from airlineStats 
WHERE arraylength(DivTailNums) >= 2
limit 5
```

| DivTailNums   | DivAirports | unionIds       |
| ------------- | ----------- | -------------- |
| N7713A,N7713A | IND,IND     | N7713A,IND     |
| N344AA,N344AA | MCI,BOS     | N344AA,MCI,BOS |
| N7713A,N7713A | IND,IND     | N7713A,IND     |
| N344AA,N344AA | MCI,BOS     | N344AA,MCI,BOS |
