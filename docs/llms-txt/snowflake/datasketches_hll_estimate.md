# Source: https://docs.snowflake.com/en/sql-reference/functions/datasketches_hll_estimate.md

Categories:
:   [Aggregate functions](../functions-aggregation.md) (Cardinality Estimation) , [Window function syntax and usage](../functions-window-syntax.md)

# DATASKETCHES_HLL_ESTIMATE

Returns the cardinality estimate for the given sketch.

This function is a version of the [HLL](hll.md) HyperLogLog function that can read binary sketches
in the format used by Apache DataSketches. For more information, see the
[Apache DataSketches documentation](https://datasketches.apache.org/docs/HLL/HllSketches.html).

A sketch produced by the [DATASKETCHES_HLL_COMBINE](datasketches_hll_combine.md) function can be used
to compute a cardinality estimate using the DATASKETCHES_HLL_ESTIMATE function.

## Syntax

```sqlsyntax
DATASKETCHES_HLL_ESTIMATE( <binary_sketch> )
```

## Arguments

`binary_sketch`
:   An expression that contains sketch information in binary format.

## Returns

The function returns a value of type DOUBLE.

If the input is empty, the output is `0.0`.

> **Note:**
>
> This function returns a value of a different type than the [HLL_ESTIMATE](hll_estimate.md) function,
> which returns an INTEGER value.

## Examples

Create a table and insert values:

```sqlexample
CREATE OR REPLACE TABLE datasketches_demo(v INT, g INT);

INSERT INTO datasketches_demo SELECT 1, 1;
INSERT INTO datasketches_demo SELECT 2, 1;
INSERT INTO datasketches_demo SELECT 2, 1;
INSERT INTO datasketches_demo SELECT 2, 1;
INSERT INTO datasketches_demo SELECT 1, 2;
INSERT INTO datasketches_demo SELECT 1, 2;
INSERT INTO datasketches_demo SELECT 4, 2;
INSERT INTO datasketches_demo SELECT 4, 2;
INSERT INTO datasketches_demo SELECT 5, 2;
```

The following examples use the data in the table.

### Return the cardinality estimate for accumulated binary sketches

The following example performs the following actions:

1. The DATASKETCHES_HLL_ACCUMULATE function creates two binary sketches for the data in column `v`,
   grouped by the values `1` and `2` in column `g`
2. The DATASKETCHES_HLL_ESTIMATE function returns the cardinality estimate for each accumulated sketch.

```sqlexample
WITH
  accumulated AS (
    SELECT g,
           DATASKETCHES_HLL_ACCUMULATE(v) AS accumulated_sketches
      FROM datasketches_demo
      GROUP BY g)
SELECT g, DATASKETCHES_HLL_ESTIMATE(accumulated_sketches) AS accumulated_estimate
  FROM accumulated;
```

```output
+---+----------------------+
| G | ACCUMULATED_ESTIMATE |
|---+----------------------|
| 1 |          2.000000005 |
| 2 |          3.000000015 |
+---+----------------------+
```

You can see values of the accumulated sketches in the example in [DATASKETCHES_HLL_ACCUMULATE](datasketches_hll_accumulate.md).

### Return the cardinality estimate for combined binary sketches

The following example performs the following actions:

1. The DATASKETCHES_HLL_ACCUMULATE function creates two binary sketches for the data in column `v`,
   grouped by the values `1` and `2` in column `g`
2. The DATASKETCHES_HLL_COMBINE function combines these binary sketches to unify them.
3. The DATASKETCHES_HLL_ESTIMATE function returns the cardinality estimate for the unified sketch.

```sqlexample
WITH
  accumulated AS (
    SELECT g,
           DATASKETCHES_HLL_ACCUMULATE(v) AS accumulated_sketches
      FROM datasketches_demo
      GROUP BY g),
  combined AS (
    SELECT DATASKETCHES_HLL_COMBINE(accumulated_sketches) AS unified
      FROM accumulated)
SELECT DATASKETCHES_HLL_ESTIMATE(unified) AS unified_estimate
  FROM combined;
```

```output
+------------------+
| UNIFIED_ESTIMATE |
|------------------|
|       4.00000003 |
+------------------+
```

You can see value of the combined sketches in the example in [DATASKETCHES_HLL_COMBINE](datasketches_hll_combine.md).
