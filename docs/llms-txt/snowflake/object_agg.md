# Source: https://docs.snowflake.com/en/sql-reference/functions/object_agg.md

Categories:
:   [Aggregate functions](../functions-aggregation.md) (Semi-structured Data) , [Window functions](../functions-window.md) (General) , [Semi-structured and structured data functions](../functions-semistructured.md) (Array/Object)

# OBJECT_AGG

Returns one OBJECT per group. For each (`key`, `value`) input pair, where `key`
must be a VARCHAR and `value` must be a VARIANT, the resulting OBJECT contains
a `key`:`value` field.

Aliases:
:   OBJECTAGG

## Syntax

**Aggregate function**

```sqlsyntax
OBJECT_AGG(<key>, <value>)
```

**Window function**

```sqlsyntax
OBJECT_AGG(<key>, <value>) OVER ( [ PARTITION BY <expr2> ] )
```

## Usage notes

* Input tuples with NULL `key` and/or `value` are ignored.
* Duplicate keys within a group result in a `Duplicate field key 'key'` error.
* The DISTINCT keyword is supported, but it only filters out duplicate
  rows where both `key` and `value` are equal.

* When this function is called as a window function, it does not support:

  * An ORDER BY clause within the OVER clause.
  * Explicit window frames.

## Examples

```sqlexample
CREATE OR REPLACE TABLE objectagg_example(g NUMBER, k VARCHAR(30), v VARIANT);
INSERT INTO objectagg_example SELECT 0, 'name', 'Joe'::VARIANT;
INSERT INTO objectagg_example SELECT 0, 'age', 21::VARIANT;
INSERT INTO objectagg_example SELECT 1, 'name', 'Sue'::VARIANT;
INSERT INTO objectagg_example SELECT 1, 'zip', 94401::VARIANT;

SELECT * FROM objectagg_example;
```

```output
+---+------+-------+
| G |  K   |   V   |
|---+------+-------|
| 0 | name | "Joe" |
| 0 | age  | 21    |
| 1 | name | "Sue" |
| 1 | zip  | 94401 |
+---+------+-------+
```

This example uses OBJECT_AGG as an aggregate function:

```sqlexample
SELECT OBJECT_AGG(k, v) FROM objectagg_example GROUP BY g;
```

```output
+-------------------+
| OBJECT_AGG(K, V)  |
|-------------------|
| {                 |
|  "name": "Sue",   |
|   "zip": 94401    |
| }                 |
| {                 |
|  "age": 21,       |
|  "name": "Joe"    |
| }                 |
+-------------------+
```

```sqlexample
SELECT seq, key, value
  FROM (SELECT object_agg(k, v) o FROM objectagg_example GROUP BY g),
    LATERAL FLATTEN(input => o);
```

```output
+-----+------+-------+
| SEQ | KEY  | VALUE |
|-----+------+-------|
|   1 | name | "Sue" |
|   1 | zip  | 94401 |
|   2 | age  | 21    |
|   2 | name | "Joe" |
+-----+------+-------+
```
