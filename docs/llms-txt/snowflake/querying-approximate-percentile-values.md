# Source: https://docs.snowflake.com/en/user-guide/querying-approximate-percentile-values.md

# Estimating Percentile Values

Snowflake uses an improved version of the t-Digest algorithm, a space and time efficient way of estimating approximate percentile
values in data sets.

## Overview

Snowflake provides an improved version of an implementation of the
[t-Digest algorithm papers](https://github.com/tdunning/t-digest/tree/master/docs/t-digest-paper) by Dunning and Ertl.
It has been implemented through the
[APPROX_PERCENTILE](../sql-reference/functions/approx_percentile.md) family of functions.

As documented, the algorithm has a constant relative error. Note that the algorithm has substantial empirical support, but no rigorous proof of any accuracy guarantees.

## SQL Functions

The following [Aggregate functions](../sql-reference/functions-aggregation.md) are provided for using t-Digest to approximate percentile values:

* [APPROX_PERCENTILE](../sql-reference/functions/approx_percentile.md): Returns an approximation of the desired percentile value.
* [APPROX_PERCENTILE_ACCUMULATE](../sql-reference/functions/approx_percentile_accumulate.md): Skips the final estimation step and, instead, returns the intermediate t-Digest state at the end of an aggregation.
* [APPROX_PERCENTILE_COMBINE](../sql-reference/functions/approx_percentile_combine.md): Combines (i.e. merges) multiple input states into a single output state.
* [APPROX_PERCENTILE_ESTIMATE](../sql-reference/functions/approx_percentile_estimate.md): Computes a percentile estimate of a t-Digest state produced by APPROX_PERCENTILE_ACCUMULATE or APPROX_PERCENTILE_COMBINE.

## Implementation Details

* The estimation uses a constant amount of space regardless of the size of the input.
* The t-Digest state is independent from the percentile value. This enables calculating the t-Digest state once, and then querying the state for multiple percentile values.
