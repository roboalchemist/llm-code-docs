# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/arrayunionint.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/arrayunionint.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/arrayunionint.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/arrayunionint.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/arrayunionint.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/arrayunionint.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/arrayunionint.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/arrayunionint.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/arrayunionint.md

# Source: https://docs.pinot.apache.org/functions-1/arrayunionint.md

# arrayUnionInt

Create a union of two arrays of ints.

## Signature

> arrayUnionInt('colName1', 'colName2')

## Usage Examples

These examples are based on the [Hybrid Quick Start](https://docs.pinot.apache.org/basics/getting-started/quick-start#hybrid).

```sql
select DivWheelsOffs, 
       DivWheelsOns,
       arrayUnionInt(DivWheelsOffs, DivWheelsOns) AS unionIds
from airlineStats 
WHERE arraylength(DivWheelsOffs) >= 2
limit 5
```

| DivWheelsOffs | DivWheelsOns | unionIds            |
| ------------- | ------------ | ------------------- |
| 1453,1731     | 1415,1623    | 1453,1731,1415,1623 |
| 1908,1758     | 1339,2310    | 1908,1758,1339,2310 |
| 1453,1731     | 1415,1623    | 1453,1731,1415,1623 |
| 1908,1758     | 1339,2310    | 1908,1758,1339,2310 |
