# Source: https://docs.pinot.apache.org/release-1.3.0/configuration-reference/functions/distinctcountsmarthll.md

# Source: https://docs.pinot.apache.org/release-1.4.0/functions-1/distinctcountsmarthll.md

# Source: https://docs.pinot.apache.org/functions-1/distinctcountsmarthll.md

# DISTINCTCOUNTSMARTHLL

## Signature

> DISTINCT\_COUNT\_SMART\_HLL(col\[, params])

* `col` (required): Name of the column to aggregate on.
* `params` (optional): Semicolon-separated parameter key-value pairs:
  * `threshold`: The threshold to convert the value set into a *HyperLogLog* (default *100\_000*).
  * `log2m`: *log2m* for the *HyperLogLog* (default *12*).
  * `dictThreshold`: Threshold for dictionary-encoded columns to switch from RoaringBitmap-based de-duplication to direct HyperLogLog aggregation; RoaringBitmap becomes more expensive than direct HLL for high-cardinality columns (default 100\_000). Use -1 or INT\_MAX to bypass this optimization.
* Example: `DISTINCT_COUNT_SMART_HLL(col, 'threshold=10000;log2m=8')`

## Usage Examples

These examples are based on the [Batch Quick Start](https://docs.pinot.apache.org/basics/getting-started/quick-start#batch).

## **DISTINCTCOUNTSMARTHLL considerations**

* `DISTINCTCOUNTHLL()`is faster than `DISTINCTCOUNT()`if data is pre-aggregated at ingestion or aggregated at a server with enough records. This performance improvement increases when comparing large datasets.
* If very few records are pre-aggregated, `DISTINCTCOUNTHLL()`will not be as fast as `DISTINCTCOUNT()`because the serialized HLL size is larger than sending individual values.
* `DISTINCTCOUNTHLLPLUS()`provides more precise results than `DISTINCTCOUNTHLL()`with the same performance.
* `DISTINCTCOUNTSMARTHLL()`automatically shifts to HLL when reaching a threshold, and comes with some overhead.
