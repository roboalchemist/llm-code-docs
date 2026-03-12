# Source: https://docs.snowflake.com/en/sql-reference/functions/approx_percentile_estimate.md

Categories:
:   [Aggregate functions](../functions-aggregation.md) (Percentile Estimation) , [Window function syntax and usage](../functions-window-syntax.md)

# APPROX_PERCENTILE_ESTIMATE

Returns the desired approximated percentile value for the specified t-Digest state.

A t-Digest state produced by [APPROX_PERCENTILE_ACCUMULATE](approx_percentile_accumulate.md) and [APPROX_PERCENTILE_COMBINE](approx_percentile_combine.md) can be used to compute a percentile estimate using this function.

As such, APPROX_PERCENTILE_ESTIMATE(APPROX_PERCENTILE_ACCUMULATE(…)) is equivalent to APPROX_PERCENTILE(…).

See also:
:   [APPROX_PERCENTILE](approx_percentile.md) , [APPROX_PERCENTILE_ACCUMULATE](approx_percentile_accumulate.md) , [APPROX_PERCENTILE_COMBINE](approx_percentile_combine.md)

## Syntax

```sqlsyntax
APPROX_PERCENTILE_ESTIMATE( <state> , <percentile> )
```

## Arguments

`state`
:   An expression that contains state information generated
    by a call to [APPROX_PERCENTILE_ACCUMULATE](approx_percentile_accumulate.md) or
    [APPROX_PERCENTILE_COMBINE](approx_percentile_combine.md).

`percentile`
:   A constant real value greater than or equal to `0.0` and less than `1.0`.
    This indicates the percentile from 0 to 99.999… (e.g. the value 0.65 indicates the 65th percentile).

## Usage notes

* Decimal-float ([DECFLOAT](../data-types-numeric.md)) values aren’t supported.

## Example

Consider a scenario where you need to approximate multiple percentile values from a given set of numbers. This can be done by creating the state and then using APPROX_PERCENTILE_ESTIMATE to calculate
all the percentiles:

1. First, store the state:

   ```sqlexample
   CREATE OR REPLACE TABLE resultstate AS (
     SELECT APPROX_PERCENTILE_ACCUMULATE(c1) AS s
       FROM testtable
     );
   ```

2. Then, query the state for multiple percentiles:

   ```sqlexample
   SELECT APPROX_PERCENTILE_ESTIMATE(s, 0.01),
       APPROX_PERCENTILE_ESTIMATE(s, 0.15),
       APPROX_PERCENTILE_ESTIMATE(s, 0.845)
     FROM testtable;
   ```

For a more extensive example, see the Examples section in
[APPROX_PERCENTILE_ACCUMULATE](approx_percentile_accumulate.md).
