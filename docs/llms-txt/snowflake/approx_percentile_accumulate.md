# Source: https://docs.snowflake.com/en/sql-reference/functions/approx_percentile_accumulate.md

Categories:
:   [Aggregate functions](../functions-aggregation.md) (Percentile Estimation) , [Window function syntax and usage](../functions-window-syntax.md)

# APPROX_PERCENTILE_ACCUMULATE

Returns the internal representation of the t-Digest state (as a JSON object) at the end of aggregation. (For more information about t-Digest, see:
[Estimating Percentile Values](../../user-guide/querying-approximate-percentile-values.md).)

The function [APPROX_PERCENTILE](approx_percentile.md) discards this internal, intermediate state when the final percentile estimate is returned. However, in certain advanced use cases, such as estimating incremental percentile during bulk
loading, you may wish to keep the intermediate state, in which case you would use APPROX_PERCENTILE_ACCUMULATE instead of [APPROX_PERCENTILE](approx_percentile.md).

APPROX_PERCENTILE_ACCUMULATE does not return a percentile value. Instead, it returns the algorithm state itself. The intermediate state can later be:

* Combined (i.e. merged) with other intermediate states from separate but
  related batches of data.
* Processed by other functions that operate directly on the intermediate state,
  for example, [APPROX_PERCENTILE_ESTIMATE](approx_percentile_estimate.md). (For an example, see the
  Examples section below.)
* Exported to external tools.

See also:
:   [APPROX_PERCENTILE_COMBINE](approx_percentile_combine.md) , [APPROX_PERCENTILE_ESTIMATE](approx_percentile_estimate.md)

## Syntax

```sqlsyntax
APPROX_PERCENTILE_ACCUMULATE( <expr> )
```

## Arguments

`expr`
:   A valid expression, such as a column name, that evaluates to a numeric
    value.

## Usage notes

* Percentile works only on numeric values, so `expr` should produce
  values that are numbers or can be cast to numbers.

* Decimal-float ([DECFLOAT](../data-types-numeric.md)) values aren’t supported.

## Example

Store the t-Digest state of the `testtable.c1` column in a table and then use the state to compute percentiles:

```sqlexample
CREATE OR REPLACE TABLE resultstate AS
  SELECT APPROX_PERCENTILE_ACCUMULATE(c1) AS s
    FROM testtable;

SELECT APPROX_PERCENTILE_ESTIMATE(s, 0.015)
  FROM resultstate;

SELECT APPROX_PERCENTILE_ESTIMATE(s, 0.2)
  FROM resultstate;
```

Here is a more extensive example that shows the usage of all three
related functions: APPROX_PERCENTILE_ACCUMULATE,
APPROX_PERCENTILE_ESTIMATE, and APPROX_PERCENTILE_COMBINE.

Create a simple table and data:

```sqlexample
CREATE OR REPLACE TABLE test_table1 (c1 INTEGER);
INSERT INTO test_table1 (c1) VALUES (1), (2), (3), (4);
```

Create a table that contains the “state” that represents the current
approximate percentile information for the table named `test_table1`:

```sqlexample
CREATE OR REPLACE TABLE resultstate1 AS (
  SELECT APPROX_PERCENTILE_ACCUMULATE(c1) AS rs1
    FROM test_table1);
```

Use that state information to display the current estimate of the median
value (0.5 means that we want the value at the 50th percentile):

```sqlexample
SELECT APPROX_PERCENTILE_ESTIMATE(rs1, 0.5)
  FROM resultstate1;
```

```output
+--------------------------------------+
| APPROX_PERCENTILE_ESTIMATE(RS1, 0.5) |
|--------------------------------------|
|                                  2.5 |
+--------------------------------------+
```

Now create a second table and add data. (In a more realistic situation,
the user could have loaded more data into the first table and divided the
data into non-overlapping sets based on the time that the data was loaded.)

```sqlexample
CREATE OR REPLACE TABLE test_table2 (c1 INTEGER);
INSERT INTO test_table2 (c1) VALUES (5), (6), (7), (8);
```

Get the “state” information for just the new data.

```sqlexample
CREATE OR REPLACE TABLE resultstate2 AS
  (SELECT APPROX_PERCENTILE_ACCUMULATE(c1) AS rs1
     FROM test_table2);
```

Combine the “state” information for the two batches of rows:

```sqlexample
CREATE OR REPLACE TABLE combined_resultstate (c1) AS
  SELECT APPROX_PERCENTILE_COMBINE(rs1) AS apc1
    FROM (
      SELECT rs1 FROM resultstate1
      UNION ALL
      SELECT rs1 FROM resultstate2
    );
```

Get the approximate median value of the combined set of rows:

```sqlexample
SELECT APPROX_PERCENTILE_ESTIMATE(c1, 0.5)
  FROM combined_resultstate;
```

```output
+-------------------------------------+
| APPROX_PERCENTILE_ESTIMATE(C1, 0.5) |
|-------------------------------------|
|                                 4.5 |
+-------------------------------------+
```
