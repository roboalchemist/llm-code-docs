# Source: https://docs.snowflake.com/en/release-notes/2026/other/2026-01-29-datasketches-functions-ga.md

# Jan 29, 2026: Apache DataSketches functions (*General availability*)

The following Apache Datasketches functions are now generally available and are no longer in Preview:

| Function subcategory | New function | Description |
| --- | --- | --- |
| Cardinality estimation | [DATASKETCHES_HLL](../../../sql-reference/functions/datasketches_hll.md) | Returns an approximation of the distinct cardinality of the input (that is, `DATASKETCHES_HLL(col1)` returns an approximation of `COUNT(DISTINCT col1)`). |
| Cardinality estimation | [DATASKETCHES_HLL_ACCUMULATE](../../../sql-reference/functions/datasketches_hll_accumulate.md) | Returns the sketch at the end of aggregation. |
| Cardinality estimation | [DATASKETCHES_HLL_COMBINE](../../../sql-reference/functions/datasketches_hll_combine.md) | Combines (merges) input sketches into a single output sketch. |
| Cardinality estimation | [DATASKETCHES_HLL_ESTIMATE](../../../sql-reference/functions/datasketches_hll_estimate.md) | Returns the cardinality estimate for the given sketch. |
