# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/div.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/div.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/div.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/div.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/div.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/div.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/div.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/div.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/div.md

# Source: https://docs.pinot.apache.org/functions-1/div.md

# DIV

Quotient of two values

## Signature

> DIV(col1, col2)

## Usage Examples

These examples are based on the [Batch Quick Start](https://docs.pinot.apache.org/basics/getting-started/quick-start#batch).

```sql
select homeRuns, numberOfGames, DIV(homeRuns, numberOfGames) AS total
from baseballStats 
WHERE teamID = 'ML1' 
AND yearID = 1956 
AND playerName = 'Henry Louis'
```

| homeRuns | numberOfGames | total               |
| -------- | ------------- | ------------------- |
| 26       | 153           | 0.16993464052287582 |
