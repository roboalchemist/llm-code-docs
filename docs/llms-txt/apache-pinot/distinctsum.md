# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/distinctsum.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/distinctsum.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/distinctsum.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/distinctsum.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/distinctsum.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/distinctsum.md

# Source: https://docs.pinot.apache.org/functions-1/distinctsum.md

# DISTINCTSUM

Returns the sum of distinct row values in a group

## Signature

`DISTINCTSUM(colName) or sum(distinct col)`

## Usage Examples

These examples are based on the [Batch Quick Start](https://docs.pinot.apache.org/basics/getting-started/quick-start#batch).

```sql
SELECT DISTINCTSUM(runs) AS VALUE
FROM baseballStats
```

| VALUE |
| ----- |
| 13922 |

```sql
SELECT SUM(DISTINCT AtBatting) AS VALUE
FROM baseballStats
```

| VALUE  |
| ------ |
| 244032 |
