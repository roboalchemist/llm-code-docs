# Source: https://docs.snowflake.com/en/sql-reference/constructs/top_n.md

Categories:
:   [Query syntax](../constructs.md)

# TOP *<n>*

Constrains the maximum number of rows returned by a statement or subquery.

See also:
:   [LIMIT / FETCH](limit.md)

## Syntax

```sqlsyntax
SELECT
  [ TOP <n> ]
    ...
FROM ...
[ ORDER BY ... ]
[ ... ]
```

## Parameters

`n`
:   The maximum number of rows to return in the result set.

## Usage notes

* An [ORDER BY](order-by.md) clause is not required; however, without an [ORDER BY](order-by.md) clause, the results are non-deterministic because results within a result set are not necessarily in any particular order. To control the results returned, use an [ORDER BY](order-by.md) clause.
* When TOP *<n>* and ORDER BY are at different nesting levels in a query, results can be unpredictable.
  For details and examples, see the [LIMIT / FETCH usage notes](limit.md).
* `n` must be a non-negative integer constant.
* TOP `n` and LIMIT `count` are equivalent.

## Examples

The following example shows the effect of TOP N. For simplicity, these
queries omit the ORDER BY clause and assume that the output order is
always the same as shown by the first query. **Real-world queries should
include an ORDER BY clause.**

```sqlexample
SELECT c1 FROM testtable;
```

```output
+------+
|   C1 |
|------|
|    1 |
|    2 |
|    3 |
|   20 |
|   19 |
|   18 |
|    1 |
|    2 |
|    3 |
|    4 |
| NULL |
|   30 |
| NULL |
+------+
```

```sqlexample
SELECT TOP 4 c1 FROM testtable;
```

```output
+----+
| C1 |
|----|
|  1 |
|  2 |
|  3 |
| 20 |
+----+
```
