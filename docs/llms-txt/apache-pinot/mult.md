# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/mult.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/mult.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/mult.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/mult.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/mult.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/mult.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/mult.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/mult.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/mult.md

# Source: https://docs.pinot.apache.org/functions-1/mult.md

# mult

Product of at least two values

## Signature

> MULT(col1, col2, col3...)

## Usage Examples

These examples are based on the [Batch Quick Start](https://docs.pinot.apache.org/basics/getting-started/quick-start#batch).

```sql
select homeRuns, baseOnBalls, MULT(homeRuns, baseOnBalls) AS total
from baseballStats 
WHERE teamID = 'ML1' 
AND yearID = 1956 
AND playerName = 'Henry Louis'
```

| homeRuns | baseOnBalls | total |
| -------- | ----------- | ----- |
| 26       | 37          | 962   |
