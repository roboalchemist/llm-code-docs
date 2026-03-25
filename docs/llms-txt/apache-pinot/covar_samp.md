# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/covar_samp.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/covar_samp.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/covar_samp.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/covar_samp.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/covar_samp.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/covar_samp.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/covar_samp.md

# Source: https://docs.pinot.apache.org/functions-1/covar_samp.md

# COVAR\_SAMP

Returns the sample covariance between of 2 numerical columns.

<pre><code><strong>COVAR_SAMP(col1, col2) = COVAR_POP(col1, col2) * besselCorrection
</strong></code></pre>

## Signatures

`COVAR_SAMP(col1, col2) -> double`

## Usage Examples

These examples are based on the [Batch Quick Start](https://docs.pinot.apache.org/basics/getting-started/quick-start#batch).

```sql
SELECT COVAR_SAMP(numberOfGames, AtBatting) AS covariance 
FROM baseballStats
```

| covariance        |
| ----------------- |
| 8270.973200974102 |
