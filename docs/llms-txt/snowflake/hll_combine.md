# Source: https://docs.snowflake.com/en/sql-reference/functions/hll_combine.md

Categories:
:   [Aggregate functions](../functions-aggregation.md) (Cardinality Estimation) ,
    [Window functions](../functions-window-syntax.md) (Cardinality Estimation)

# HLL_COMBINE

Combines (merges) input states into a single output state.

This allows scenarios where [HLL_ACCUMULATE](hll_accumulate.md) is run over horizontal
partitions of the same table, producing an algorithm state for each table
partition. These states can later be combined using HLL_COMBINE,
producing the same output state as a single run of [HLL_ACCUMULATE](hll_accumulate.md)
over the entire table.

See also:
:   [HLL](hll.md) , [HLL_ACCUMULATE](hll_accumulate.md) , [HLL_ESTIMATE](hll_estimate.md)

## Syntax

**Aggregate function**

```sqlsyntax
HLL_COMBINE( [ DISTINCT ] <state> )
```

**Window function**

```sqlsyntax
HLL_COMBINE( [ DISTINCT ] <state> ) OVER ( [ PARTITION BY <expr1> ] )
```

For details about the OVER clause, see [Window function syntax and usage](../functions-window-syntax.md).

## Arguments

`state`
:   An expression that contains state information generated
    by a call to [HLL_ACCUMULATE](hll_accumulate.md).

## Usage notes

* This function can be used as an [aggregate function](../functions-aggregation.md) or
  a [window function](../functions-window-syntax.md).
* DISTINCT is supported syntactically, but has no effect.
* The output of this function is not fully deterministic. Running this
  function on the same inputs might return different results at different
  times. The differences are typically small and are consistent with the fact
  that the HLL_\* functions are approximation functions.

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
