# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/stddev_samp.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/plugin-reference/stddev_samp.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/plugin-reference/stddev_samp.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/plugin-reference/stddev_samp.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/plugin-reference/stddev_samp.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/plugin-reference/stddev_samp.md

# Source: https://docs.pinot.apache.org/release-1.4.0/configuration-reference/plugin-reference/stddev_samp.md

# Source: https://docs.pinot.apache.org/configuration-reference/plugin-reference/stddev_samp.md

# STDDEV\_SAMP

Returns the sample standard deviation of a numerical column.

## Signatures

`STDDEV_SAMP(col1) -> double`

## Usage Examples

These examples are based on the [Batch Quick Start](https://docs.pinot.apache.org/basics/getting-started/quick-start#batch).

```sql
SELECT STDDEV_SAMP(numberOfGames) AS stddev 
FROM baseballStats
```
