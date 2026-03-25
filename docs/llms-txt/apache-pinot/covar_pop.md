# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/covar_pop.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/covar_pop.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/covar_pop.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/covar_pop.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/covar_pop.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/covar_pop.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/covar_pop.md

# Source: https://docs.pinot.apache.org/functions-1/covar_pop.md

# COVAR\_POP

Returns the population covariance between of 2 numerical columns.

<pre><code><strong>COVAR_POP(col1, col2) = E[col1 * col2] - E[col1]E[col2]
</strong></code></pre>

## Signatures

`COVAR_POP(col1, col2) -> double`

## Usage Examples

These examples are based on the [Batch Quick Start](https://docs.pinot.apache.org/basics/getting-started/quick-start#batch).

```sql
SELECT COVAR_POP(numberOfGames, hits) AS covariance 
FROM baseballStats
```

| covariance        |
| ----------------- |
| 2314.249154477403 |
