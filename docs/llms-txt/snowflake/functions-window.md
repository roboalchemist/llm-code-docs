# Source: https://docs.snowflake.com/en/sql-reference/functions-window.md

# Window functions

Window functions are analytic functions that you can use for various calculations such as running totals,
moving averages, and rankings.

For general syntax rules, see [Window function syntax and usage](functions-window-syntax.md). For syntax specific to
individual functions, go to the links in the following table.

| Sub-category | Notes |
| --- | --- |
| **General window** |  |
| [ANY_VALUE](functions/any_value.md) |  |
| [AVG](functions/avg.md) |  |
| [CONDITIONAL_CHANGE_EVENT](functions/conditional_change_event.md) |  |
| [CONDITIONAL_TRUE_EVENT](functions/conditional_true_event.md) |  |
| [CORR](functions/corr.md) |  |
| [COUNT](functions/count.md) |  |
| [COUNT_IF](functions/count_if.md) |  |
| [COVAR_POP](functions/covar_pop.md) |  |
| [COVAR_SAMP](functions/covar_samp.md) |  |
| [INTERPOLATE_BFILL, INTERPOLATE_FFILL, INTERPOLATE_LINEAR](functions/interpolate_bfill.md) |  |
| [LISTAGG](functions/listagg.md) | Uses WITHIN GROUP syntax. |
| [MAX](functions/max.md) |  |
| [MEDIAN](functions/median.md) |  |
| [MIN](functions/min.md) |  |
| [MODE](functions/mode.md) |  |
| [PERCENTILE_CONT](functions/percentile_cont.md) | Uses WITHIN GROUP syntax. |
| [PERCENTILE_DISC](functions/percentile_disc.md) | Uses WITHIN GROUP syntax. |
| [RATIO_TO_REPORT](functions/ratio_to_report.md) |  |
| [STDDEV, STDDEV_SAMP](functions/stddev.md) | STDDEV and STDDEV_SAMP are aliases. |
| [STDDEV_POP](functions/stddev_pop.md) |  |
| [SUM](functions/sum.md) |  |
| [VAR_POP](functions/var_pop.md) |  |
| [VAR_SAMP](functions/var_samp.md) |  |
| [VARIANCE_POP](functions/variance_pop.md) | Alias for [VAR_POP](functions/var_pop.md). |
| [VARIANCE , VARIANCE_SAMP](functions/variance.md) | Alias for [VAR_SAMP](functions/var_samp.md). |
| **Ranking** |  |
| [CUME_DIST](functions/cume_dist.md) |  |
| [DENSE_RANK](functions/dense_rank.md) |  |
| [FIRST_VALUE](functions/first_value.md) |  |
| [LAG](functions/lag.md) |  |
| [LAST_VALUE](functions/last_value.md) |  |
| [LEAD](functions/lead.md) |  |
| [NTH_VALUE](functions/nth_value.md) |  |
| [NTILE](functions/ntile.md) |  |
| [PERCENT_RANK](functions/percent_rank.md) | Supports only RANGE BETWEEN window frames without explicit offsets. |
| [RANK](functions/rank.md) |  |
| [ROW_NUMBER](functions/row_number.md) |  |
| **Bitwise aggregation** |  |
| [BITAND_AGG](functions/bitand_agg.md) |  |
| [BITOR_AGG](functions/bitor_agg.md) |  |
| [BITXOR_AGG](functions/bitxor_agg.md) |  |
| **Boolean aggregation** |  |
| [BOOLAND_AGG](functions/booland_agg.md) |  |
| [BOOLOR_AGG](functions/boolor_agg.md) |  |
| [BOOLXOR_AGG](functions/boolxor_agg.md) |  |
| **Hash** |  |
| [HASH_AGG](functions/hash_agg.md) |  |
| **Semi-structured data aggregation** |  |
| [ARRAY_AGG](functions/array_agg.md) |  |
| [OBJECT_AGG](functions/object_agg.md) |  |
| **Counting distinct values** |  |
| [ARRAY_UNION_AGG](functions/array_union_agg.md) |  |
| [ARRAY_UNIQUE_AGG](functions/array_unique_agg.md) |  |
| **Linear regression** |  |
| [REGR_AVGX](functions/regr_avgx.md) |  |
| [REGR_AVGY](functions/regr_avgy.md) |  |
| [REGR_COUNT](functions/regr_count.md) |  |
| [REGR_INTERCEPT](functions/regr_intercept.md) |  |
| [REGR_R2](functions/regr_r2.md) |  |
| [REGR_SLOPE](functions/regr_slope.md) |  |
| [REGR_SXX](functions/regr_sxx.md) |  |
| [REGR_SXY](functions/regr_sxy.md) |  |
| [REGR_SYY](functions/regr_syy.md) |  |
| **Statistics and probability** |  |
| [KURTOSIS](functions/kurtosis.md) |  |
| **Cardinality estimation** . (**using** [HyperLogLog](../user-guide/querying-approximate-cardinality.md)) |  |
| [APPROX_COUNT_DISTINCT](functions/approx_count_distinct.md) | Alias for [HLL](functions/hll.md). |
| [HLL](functions/hll.md) |  |
| [HLL_ACCUMULATE](functions/hll_accumulate.md) |  |
| [HLL_COMBINE](functions/hll_combine.md) |  |
| [HLL_ESTIMATE](functions/hll_estimate.md) | Not an aggregate function; uses scalar input from [HLL_ACCUMULATE](functions/hll_accumulate.md) or [HLL_COMBINE](functions/hll_combine.md). |
| [HLL_EXPORT](functions/hll_export.md) |  |
| [HLL_IMPORT](functions/hll_import.md) |  |
| **Similarity estimation** . (**using** [MinHash](../user-guide/querying-approximate-similarity.md)) |  |
| [APPROXIMATE_JACCARD_INDEX](functions/approximate_jaccard_index.md) | Alias for [APPROXIMATE_SIMILARITY](functions/approximate_similarity.md). |
| [APPROXIMATE_SIMILARITY](functions/approximate_similarity.md) |  |
| [MINHASH](functions/minhash.md) |  |
| [MINHASH_COMBINE](functions/minhash_combine.md) |  |
| **Frequency estimation** . (**using** [Space-Saving](../user-guide/querying-approximate-frequent-values.md)) |  |
| [APPROX_TOP_K](functions/approx_top_k.md) |  |
| [APPROX_TOP_K_ACCUMULATE](functions/approx_top_k_accumulate.md) |  |
| [APPROX_TOP_K_COMBINE](functions/approx_top_k_combine.md) |  |
| [APPROX_TOP_K_ESTIMATE](functions/approx_top_k_estimate.md) | Not an aggregate function; uses scalar input from [APPROX_TOP_K_ACCUMULATE](functions/approx_top_k_accumulate.md) or [APPROX_TOP_K_COMBINE](functions/approx_top_k_combine.md). |
| **Percentile estimation** . (**using** [t-Digest](../user-guide/querying-approximate-percentile-values.md)) |  |
| [APPROX_PERCENTILE](functions/approx_percentile.md) |  |
| [APPROX_PERCENTILE_ACCUMULATE](functions/approx_percentile_accumulate.md) |  |
| [APPROX_PERCENTILE_COMBINE](functions/approx_percentile_combine.md) |  |
| [APPROX_PERCENTILE_ESTIMATE](functions/approx_percentile_estimate.md) | Not an aggregate function; uses scalar input from [APPROX_PERCENTILE_ACCUMULATE](functions/approx_percentile_accumulate.md) or [APPROX_PERCENTILE_COMBINE](functions/approx_percentile_combine.md). |
