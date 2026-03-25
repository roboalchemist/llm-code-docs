# Source: https://docs.snowflake.com/en/sql-reference/functions/hll_estimate.md

Categories:
:   [Aggregate functions](../functions-aggregation.md) (Cardinality Estimation) ,
    [Window functions](../functions-window-syntax.md) (Cardinality Estimation)

# HLL_ESTIMATE

Returns the cardinality estimate for the given HyperLogLog state.

A HyperLogLog state produced by [HLL_ACCUMULATE](hll_accumulate.md) and [HLL_COMBINE](hll_combine.md) can be used to compute a cardinality estimate using the HLL_ESTIMATE function.

Thus, HLL_ESTIMATE(HLL_ACCUMULATE(…)) is equivalent to HLL(…).

See also:
:   [HLL](hll.md) , [HLL_ACCUMULATE](hll_accumulate.md) , [HLL_COMBINE](hll_combine.md)

## Syntax

**Aggregate function**

```sqlsyntax
HLL_ESTIMATE( <state> )
```

**Window function**

```sqlsyntax
HLL_ESTIMATE( <state> ) OVER ( [ PARTITION BY <expr> ] )
```

For details about the OVER clause, see [Window function syntax and usage](../functions-window-syntax.md).

## Arguments

`state`
:   An expression that contains state information generated
    by a call to [HLL_ACCUMULATE](hll_accumulate.md) or [HLL_COMBINE](hll_combine.md).

## Usage notes

* This function can be used as an [aggregate function](../functions-aggregation.md) or
  a [window function](../functions-window-syntax.md).

## Examples

This example shows how to use the three related functions
HLL_ACCUMULATE, HLL_ESTIMATE, and HLL_COMBINE.

Create a simple table and data:

```sqlexample
CREATE OR REPLACE SEQUENCE seq92;
CREATE OR REPLACE TABLE sequence_demo (c1 INTEGER DEFAULT seq92.nextval, dummy SMALLINT);
INSERT INTO sequence_demo (dummy) VALUES (0);

INSERT INTO sequence_demo (dummy) SELECT dummy FROM sequence_demo;
INSERT INTO sequence_demo (dummy) SELECT dummy FROM sequence_demo;
INSERT INTO sequence_demo (dummy) SELECT dummy FROM sequence_demo;
```

Create a table that contains the “state” that represents the current
approximate cardinality information for the table named `sequence_demo`:

```sqlexample
CREATE OR REPLACE TABLE resultstate1 AS (
  SELECT HLL_ACCUMULATE(c1) AS rs1
    FROM sequence_demo);
```

Now create a second table and add data. (In a more realistic situation,
the user could have loaded more data into the first table and divided the
data into non-overlapping sets based on the time that the data was loaded.)

```sqlexample
CREATE OR REPLACE TABLE test_table2 (c1 INTEGER);
INSERT INTO test_table2 (c1) SELECT c1 + 4 FROM sequence_demo;
```

Get the “state” information for just the new data.

```sqlexample
CREATE OR REPLACE TABLE resultstate2 AS
  (SELECT HLL_ACCUMULATE(c1) AS rs1
     FROM test_table2);
```

Combine the “state” information for the two batches of rows:

```sqlexample
CREATE OR REPLACE TABLE combined_resultstate (c1) AS
  SELECT HLL_COMBINE(rs1) AS apc1
    FROM (
      SELECT rs1 FROM resultstate1
      UNION ALL
      SELECT rs1 FROM resultstate2
    );
```

Get the approximate cardinality of the combined set of rows:

```sqlexample
SELECT HLL_ESTIMATE(c1)
  FROM combined_resultstate;
```

```output
+------------------+
| HLL_ESTIMATE(C1) |
|------------------|
|               12 |
+------------------+
```
