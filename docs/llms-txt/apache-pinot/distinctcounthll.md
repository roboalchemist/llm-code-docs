# Source: https://docs.pinot.apache.org/release-0.10.0/configuration-reference/functions/distinctcounthll.md

# Source: https://docs.pinot.apache.org/release-0.11.0/configuration-reference/functions/distinctcounthll.md

# Source: https://docs.pinot.apache.org/release-0.12.0/configuration-reference/functions/distinctcounthll.md

# Source: https://docs.pinot.apache.org/release-0.12.1/configuration-reference/functions/distinctcounthll.md

# Source: https://docs.pinot.apache.org/release-1.0.0/configuration-reference/functions/distinctcounthll.md

# Source: https://docs.pinot.apache.org/release-1.1.0/configuration-reference/functions/distinctcounthll.md

# Source: https://docs.pinot.apache.org/release-1.2.0/configuration-reference/functions/distinctcounthll.md

# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/distinctcounthll.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/distinctcounthll.md

# Source: https://docs.pinot.apache.org/functions-1/distinctcounthll.md

# DISTINCTCOUNTHLL

Returns an approximate distinct count using *HyperLogLog*. It also takes an optional second argument to configure the *log2m* for the *HyperLogLog*.

For accurate distinct counting, see [DISTINCTCOUNT](https://docs.pinot.apache.org/functions-1/distinctcount). Review [DISTINCTCOUNTHLL considerations](#distinctcounthll-considerations) for your use case.

## Signature

> DISTINCTCOUNTHLL(colName, log2m)

## Usage Examples

These examples are based on the [Batch Quick Start](https://docs.pinot.apache.org/basics/getting-started/quick-start#batch).

```sql
select DISTINCTCOUNTHLL(teamID) AS value
from baseballStats 
```

| value |
| ----- |
| 158   |

```sql
select DISTINCTCOUNTHLL(teamID, 12) AS value
from baseballStats 
```

| value |
| ----- |
| 149   |

## **DISTINCTCOUNTHLL considerations**

* `DISTINCTCOUNTHLL()`is faster than `DISTINCTCOUNT()`if data is pre-aggregated at ingestion or aggregated at a server with enough records. This performance improvement increases when comparing large datasets.
* If very few records are pre-aggregated, `DISTINCTCOUNTHLL()`will not be as fast as `DISTINCTCOUNT()`because the serialized HLL size is larger than sending individual values.
* `DISTINCTCOUNTHLLPLUS()`provides more precise results than `DISTINCTCOUNTHLL()`with the same performance.
* `DISTINCTCOUNTSMARTHLL()`automatically shifts to HLL when reaching a threshold, and comes with some overhead.
* `DISTINCTCOUNTSMARTHLLPLUS()`automatically shifts to HLLPlus when reaching a threshold, and comes with some overhead.
