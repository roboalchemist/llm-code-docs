# Source: https://docs.snowflake.com/en/sql-reference/functions/minhash.md

Categories:
:   [Aggregate functions](../functions-aggregation.md) (Similarity Estimation) ,
    [Window functions](../functions-window-syntax.md) (Similarity Estimation)

# MINHASH

Returns a MinHash state containing an array of size `k` constructed by applying `k` number of different hash functions to the input rows and keeping the minimum of each hash function. This MinHash state can
then be input to the [APPROXIMATE_SIMILARITY](approximate_similarity.md) function to estimate the similarity with one or more other MinHash states.

For more information about MinHash states, see [Estimating Similarity of Two or More Sets](../../user-guide/querying-approximate-similarity.md).

See also:
:   [MINHASH_COMBINE](minhash_combine.md)

## Syntax

**Aggregate function**

```sqlsyntax
MINHASH( <k> , [ DISTINCT ] expr+ )

MINHASH( <k> , * )
```

**Window function**

```sqlsyntax
MINHASH( <k> , [ DISTINCT ] expr+ ) OVER ( [ PARTITION BY <expr1> ] )

MINHASH( <k> , * ) OVER ( [ PARTITION BY <expr1> ] )
```

For details about the OVER clause, see [Window function syntax and usage](../functions-window-syntax.md).

## Arguments

`k`
:   The number of hash functions to create. The larger the value, the better the approximation;
    however, this value has a linear impact on the computation time for estimating similarity
    using APPROXIMATE_SIMILARITY. The suggested value is 100. The maximum value is 1024.

`expr`
:   One or more expressions (typically column names) that determine the values to hash.

`*`
:   Hash all columns in the input rows.

## Usage notes

* This function can be used as an [aggregate function](../functions-aggregation.md) or
  a [window function](../functions-window-syntax.md).
* DISTINCT can be included as an argument, but has no effect.

## Examples

```sqlexample
USE SCHEMA snowflake_sample_data.tpch_sf1;

SELECT MINHASH(5, *) FROM orders;

+----------------------+
| MINHASH(5, *)        |
|----------------------|
| {                    |
|   "state": [         |
|     78678383574307,  |
|     586952033158539, |
|     525995912623966, |
|     508991839383217, |
|     492677003405678  |
|   ],                 |
|   "type": "minhash", |
|   "version": 1       |
| }                    |
+----------------------+
```

Here is a more extensive example, showing the three related functions
MINHASH, MINHASH_COMBINE and APPROXIMATE_SIMILARITY. This
example creates 3 tables (`ta`, `tb`, and `tc`), two of which (`ta` and `tb`) are
similar, and two of which (`ta` and `tc`) are completely dissimilar.

Create and populate tables with values:

```sqlexample
CREATE TABLE ta (i INTEGER);
CREATE TABLE tb (i INTEGER);
CREATE TABLE tc (i INTEGER);

INSERT INTO ta (i) VALUES (1), (2), (3), (4), (5), (6), (7), (8), (9), (10);
INSERT INTO tb (i) VALUES (1), (2), (3), (4), (5), (6), (7), (8), (9), (11);
INSERT INTO tc (i) VALUES (-1), (-20), (-300), (-4000);
```

Calculate minhash info for the initial set of data:

```sqlexample
CREATE TABLE minhash_a_1 (mh) AS SELECT MINHASH(100, i) FROM ta;
CREATE TABLE minhash_b (mh) AS SELECT MINHASH(100, i) FROM tb;
CREATE TABLE minhash_c (mh) AS SELECT MINHASH(100, i) FROM tc;
```

Add more data to one of the tables:

```sqlexample
INSERT INTO ta (i) VALUES (12);
```

Demonstrate the MINHASH_COMBINE function:

```sqlexample
CREATE TABLE minhash_a_2 (mh) AS SELECT MINHASH(100, i) FROM ta WHERE i > 10;

CREATE TABLE minhash_a (mh) AS
  SELECT MINHASH_COMBINE(mh)
    FROM (
      (SELECT mh FROM minhash_a_1)
      UNION ALL
      (SELECT mh FROM minhash_a_2)
    );
```

This query shows the approximate similarity of the two similar tables
(`ta` and `tb`):

```sqlexample
SELECT APPROXIMATE_SIMILARITY(mh)
  FROM (
    (SELECT mh FROM minhash_a)
    UNION ALL
    (SELECT mh FROM minhash_b)
  );
```

```output
+-----------------------------+
| APPROXIMATE_SIMILARITY (MH) |
|-----------------------------|
|                        0.75 |
+-----------------------------+
```

This query shows the approximate similarity of the two very different tables
(`ta` and `tc`):

```sqlexample
SELECT APPROXIMATE_SIMILARITY(mh)
  FROM (
    (SELECT mh FROM minhash_a)
    UNION ALL
    (SELECT mh FROM minhash_c)
  );
```

```output
+-----------------------------+
| APPROXIMATE_SIMILARITY (MH) |
|-----------------------------|
|                           0 |
+-----------------------------+
```
