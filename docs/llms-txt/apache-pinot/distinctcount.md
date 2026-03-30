# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/distinctcount.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/distinctcount.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/distinctcount.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/distinctcount.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/distinctcount.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/distinctcount.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/distinctcount.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/distinctcount.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/distinctcount.md

# Source: https://docs.pinot.apache.org/functions-1/distinctcount.md

# DISTINCTCOUNT

Returns the count of distinct row values in a group.

{% hint style="info" %}
`DISTINCTCOUNTHLL()`is faster than `DISTINCTCOUNT()`if data is pre-aggregated at ingestion or aggregated at a server with enough records. This performance improvement increases when comparing large datasets.

If very few records are pre-aggregated, `DISTINCTCOUNT()`is faster than `DISTINCTCOUNTHLL()`because the serialized HLL size is larger than sending individual values.
{% endhint %}

## Signature

> DISTINCTCOUNT(colName)

## Usage Examples

These examples are based on the [Batch Quick Start](https://docs.pinot.apache.org/basics/getting-started/quick-start#batch).

```sql
select DISTINCTCOUNT(league) AS value
from baseballStats 
```

| value |
| ----- |
| 7     |

```sql
select DISTINCTCOUNT(teamID) AS value
from baseballStats 
```

| value |
| ----- |
| 149   |
