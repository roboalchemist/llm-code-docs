# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/var_samp.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/plugin-reference/var_samp.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/plugin-reference/var_samp.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/plugin-reference/var_samp.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/plugin-reference/var_samp.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/plugin-reference/var_samp.md

# Source: https://docs.pinot.apache.org/release-1.4.0/configuration-reference/plugin-reference/var_samp.md

# Source: https://docs.pinot.apache.org/configuration-reference/plugin-reference/var_samp.md

# VAR\_SAMP

Returns the sample variance of a numerical column.

## Signatures

`VAR_SAMP(col1) -> double`

## Usage Examples

These examples are based on the [Batch Quick Start](https://docs.pinot.apache.org/basics/getting-started/quick-start#batch).

```sql
SELECT VAR_SAMP(numberOfGames) AS variance 
FROM baseballStats
```
