# Source: https://docs.snowflake.com/en/migrations/sma-docs/translation-reference/notebooks/databricks/sample.md

# Source: https://docs.snowflake.com/en/sql-reference/constructs/sample.md

Categories:
:   [Query syntax](../constructs.md)

# SAMPLE / TABLESAMPLE

Returns a subset of rows sampled randomly from the specified table. You can specify different types of sampling methods, and
you can sample a fraction of a table or a fixed number of rows:

* When you sample a fraction of a table, with a specified probability for including a given row, the number of rows returned depends
  on the size of the table and the requested probability. You can specify a seed to make the sampling deterministic.
* When you sample a fixed, specified number of rows, the query returns the exact number of specified rows unless the table
  contains fewer rows.

SAMPLE and TABLESAMPLE are synonymous and can be used interchangeably.

## Syntax

```sqlsyntax
SELECT ...
FROM ...
  { SAMPLE | TABLESAMPLE } [ samplingMethod ]
[ ... ]
```

Where:

> ```sqlsyntax
> samplingMethod ::= { { BERNOULLI | ROW } ( { <probability> | <num> ROWS } ) |
>                      { SYSTEM | BLOCK } ( <probability> ) [ { REPEATABLE | SEED } ( <seed> ) ] }
> ```

## Parameters

`{ BERNOULLI | ROW }` or . `{ SYSTEM | BLOCK }`
:   Specifies the sampling method to use:

    * `BERNOULLI` (or `ROW`): Includes each row with a `probability` of `p/100`.
      This method is similar to flipping a weighted coin *for each row*.
    * `SYSTEM` (or `BLOCK`): Includes each block of rows with a `probability` of `p/100`.
      This method is similar to flipping a weighted coin *for each block of rows*. This method doesn’t support fixed-size sampling.

    The sampling method is optional. If no method is specified, the default is `BERNOULLI`.

`probability` or . `num ROWS`
:   Specifies whether to sample based on a fraction of the table or a fixed number of rows in the table, where:

    * `probability` specifies the percentage probability to use for selecting the sample. Can be any decimal number
      between `0` (no rows selected) and `100` (all rows selected) inclusive.
    * `num` specifies the number of rows (up to 1,000,000) to sample from the table. Can be any integer between
      `0` (no rows selected) and `1000000` inclusive.

    In addition to using literals to specify `probability` or `num ROWS`, you can also use session or bind variables.

`{ REPEATABLE | SEED ( seed ) }`
:   Specifies a seed value to make the sampling deterministic. Can be any integer between `0` and `2147483647` inclusive.
    This parameter only applies to `SYSTEM` and `BLOCK` sampling.

    In addition to using literals to specify `seed`, you can also use session or bind variables.

## Usage notes

* The following keywords can be used interchangeably:

  > * `SAMPLE | TABLESAMPLE`
  > * `BERNOULLI | ROW`
  > * `SYSTEM | BLOCK`
  > * `REPEATABLE | SEED`
* The number of rows returned depends on the sampling method specified and whether the sample is based on a fraction of the table or
  a fixed number of rows in the table:

  Fraction-based:
  :   + For `BERNOULLI | ROW` sampling, the expected number of returned rows is `(p/100)*n`. For `SYSTEM | BLOCK` sampling,
        the sample might be biased, in particular for small tables.

        > **Note:**
        >
        > For very large tables, the difference between the two methods should be negligible.
        >
        > Also, because sampling is a probabilistic process, the number of rows returned isn’t exactly equal to `(p/100)*n` rows, but it is close to this value.
      + If no `seed` is specified, SAMPLE generates different results when the same query is repeated.
      + If a table doesn’t change, and the same `seed` and `probability` are specified, SAMPLE generates the same result. However,
        sampling on a copy of a table might not return the same result as sampling on the original table, even if the same `probability` and
        `seed` are specified.

  Fixed-size:
  :   + If the table is larger than the requested number of rows, the number of requested rows is always returned.
      + If the table is smaller than the requested number of rows, the entire table is returned.
      + `SYSTEM | BLOCK` and `SEED (seed)` aren’t supported for fixed-size sampling. For example, the following queries produce errors:

        ```sqlexample
        SELECT * FROM example_table SAMPLE SYSTEM (10 ROWS);

        SELECT * FROM example_table SAMPLE ROW (10 ROWS) SEED (99);
        ```
* Sampling with `SEED (seed)` isn’t supported on views or subqueries. For example, the following query produces an error:

  ```sqlexample
  SELECT * FROM (SELECT * FROM example_table) SAMPLE (1) SEED (99);
  ```

* Sampling the result of a join is allowed, but only when both of the following are true:

  * The sampling is row-based (Bernoulli).
  * The sampling doesn’t use a seed.

  The sampling is done after the join has been fully processed. Therefore, sampling doesn’t reduce the number of
  rows joined and doesn’t reduce the cost of the join. The Examples section includes an example of
  sampling the result of a join.
* Both the [LIMIT](limit.md) clause and the SAMPLE clause return a subset of rows from a table. When you use the
  LIMIT clause, Snowflake returns the specified number of rows in the fastest way possible. When you use the SAMPLE
  clause, Snowflake returns rows based on the sampling method specified in the clause.

## Performance considerations

* `SYSTEM | BLOCK` sampling is often faster than `BERNOULLI | ROW` sampling.
* Sampling without a `seed` is often faster than sampling with a `seed`.
* Fixed-size sampling might be slower than equivalent fraction-based sampling because fixed-size sampling prevents some query optimization.

## Examples

The following examples use the SAMPLE clause.

### Fraction-based row sampling

Return a sample of a table in which each row has a 10% probability of being included in the sample:

```sqlexample
SELECT * FROM testtable SAMPLE (10);
```

Return a sample of a table in which each row has a 20.3% probability of being included in the sample:

```sqlexample
SELECT * FROM testtable TABLESAMPLE BERNOULLI (20.3);
```

Return an entire table, including all rows in the table:

```sqlexample
SELECT * FROM testtable TABLESAMPLE (100);
```

Return an empty sample:

```sqlexample
SELECT * FROM testtable SAMPLE ROW (0);
```

### Sampling with joins

This example shows how to sample multiple tables in a join. It samples 25% of the rows in `table1` and
50% of the rows in `table2`:

```sqlexample
SELECT i, j
  FROM
    table1 AS t1 SAMPLE (25)
      INNER JOIN
    table2 AS t2 SAMPLE (50)
  WHERE t2.j = t1.i;
```

The `SAMPLE` clause applies to only one table, not all preceding tables or the entire expression prior to the
`SAMPLE` clause. The following `JOIN` operation joins all rows of `table1` to a sample of 50% of the rows in `table2`.
It doesn’t sample 50% of the rows that result from joining all rows in both tables:

```sqlexample
SELECT i, j
  FROM table1 AS t1 INNER JOIN table2 AS t2 SAMPLE (50)
  WHERE t2.j = t1.i;
```

To apply the `SAMPLE` clause to the result of a join, rather than to the individual tables in the join,
apply the join to an inline view that contains the result of the join. For example, perform
the join as a subquery, and then apply the SAMPLE to the result of the subquery. The example below samples
approximately 1% of the rows returned by the join:

```sqlexample
SELECT *
  FROM (
       SELECT *
         FROM t1 JOIN t2
           ON t1.a = t2.c
       ) SAMPLE (1);
```

### Fraction-based block sampling with seeds

Return a sample of a table in which each block of rows has a 3% probability of being included in the sample, and set the seed to 82:

```sqlexample
SELECT * FROM testtable SAMPLE SYSTEM (3) SEED (82);
```

Return a sample of a table in which each block of rows has a 0.012% probability of being included in the sample, and set the seed to 99992:

```sqlexample
SELECT * FROM testtable SAMPLE BLOCK (0.012) REPEATABLE (99992);
```

> **Note:**
>
> If either of these queries are run again without making any changes to the table, they return the same sample set.

### Fixed-size row sampling

Return a fixed-size sample of 10 rows in which each row has a `min(1, 10/n)` probability of being included in the sample, where `n` is the number of rows in the table:

```sqlexample
SELECT * FROM testtable SAMPLE (10 ROWS);
```
