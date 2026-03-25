# Source: https://docs.snowflake.com/en/sql-reference/functions/dp_interval_high.md

Categories:
:   [Differential privacy functions](../functions-differential-privacy.md)

# DP_INTERVAL_HIGH

Returns the upper bound of the [noise interval](../../user-guide/diff-privacy/differential-privacy-analyst.md), which is used by differential privacy to help
analysts determine how much noise has been introduced into query results.

By default, there is a 95% confidence level that the actual value is equal to or smaller than the upper bound.

See also:
:   [DP_INTERVAL_LOW](dp_interval_low.md)

## Syntax

```sqlsyntax
DP_INTERVAL_HIGH( <aggregated_column> )
```

## Arguments

`aggregated_column`
:   Alias of a column that has been aggregated by the query.

## Returns

Returns an integer that is the upper bound of the noise interval.

If the table is not protected by differential privacy, returns NULL.

## Examples

To return the upper bound of the noise interval for the aggregation of the column `num_claims`:

```sqlexample
SELECT SUM(num_claims) AS sum_claims,
  DP_INTERVAL_HIGH(sum_claims)
  FROM t1;
```
