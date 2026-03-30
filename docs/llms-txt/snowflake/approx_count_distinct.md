# Source: https://docs.snowflake.com/en/sql-reference/functions/approx_count_distinct.md

Categories:
:   [Aggregate functions](../functions-aggregation.md) (Cardinality Estimation) , [Window functions](../functions-window.md)

# APPROX_COUNT_DISTINCT

Uses HyperLogLog to return an approximation of the distinct cardinality of the input (i.e. `HLL(col1, col2, ... )` returns an approximation of `COUNT(DISTINCT col1, col2, ... )`).

For more information about HyperLogLog, see [Estimating the Number of Distinct Values](../../user-guide/querying-approximate-cardinality.md).

Aliases:
:   [HLL](hll.md).

See also:
:   [HLL_ACCUMULATE](hll_accumulate.md) , [HLL_COMBINE](hll_combine.md) , [HLL_ESTIMATE](hll_estimate.md)

## Syntax

**Aggregate function**

```sqlsyntax
APPROX_COUNT_DISTINCT( [ DISTINCT ] <expr1>  [ , ... ] )

APPROX_COUNT_DISTINCT(*)
```

**Window function**

```sqlsyntax
APPROX_COUNT_DISTINCT( [ DISTINCT ] <expr1>  [ , ... ] ) OVER ( [ PARTITION BY <expr2> ] )

APPROX_COUNT_DISTINCT(*) OVER ( [ PARTITION BY <expr2> ] )
```

## Arguments

`expr1`
:   This is the expression for which you want to know the number of distinct values.

`expr2`
:   This is the optional expression used to group rows into partitions.

`*`
:   Returns an approximation of the total number of records, excluding records with NULL values.

    When you pass a wildcard to the function, you can qualify the wildcard with the name or alias for the table.
    For example, to pass in all of the columns from the table named `mytable`, specify the following:

    ```sqlexample
    (mytable.*)
    ```

    You can also use the ILIKE and EXCLUDE keywords for filtering:

    * ILIKE filters for column names that match the specified pattern. Only one
      pattern is allowed. For example:

      ```sqlexample
      (* ILIKE 'col1%')
      ```
    * EXCLUDE filters out column names that don’t match the specified column or columns. For example:

      ```sqlexample
      (* EXCLUDE col1)

      (* EXCLUDE (col1, col2))
      ```

    Qualifiers are valid when you use these keywords. The following example uses the ILIKE keyword to
    filter for all of the columns that match the pattern `col1%` in the table `mytable`:

    ```sqlexample
    (mytable.* ILIKE 'col1%')
    ```

    The ILIKE and EXCLUDE keywords can’t be combined in a single function call.

    For this function, the ILIKE and EXCLUDE keywords are valid only in a SELECT list or GROUP BY clause.

    For more information about the ILIKE and EXCLUDE keywords, see the “Parameters” section in [SELECT](../sql/select.md).

## Returns

The data type of the returned value is INTEGER.

## Usage notes

* Although the computation is an approximation, it is deterministic. When this function is called with the same input
  data, this function returns the same results.
* For information about NULL values and aggregate functions, see [Aggregate functions and NULL values](../functions-aggregation.md).

* When this function is called as a window function, it does not support:

  * An ORDER BY clause within the OVER clause.
  * Explicit window frames.

## Examples

This example shows how to use APPROX_COUNT_DISTINCT and its alias HLL. This example calls
both `COUNT(DISTINCT i)` and `APPROX_COUNT_DISTINCT(i)` to emphasize
that the results of those two functions do not always match exactly.

The exact output of the following query might vary because APPROX_COUNT_DISTINCT returns an approximation, not an exact value.

```sqlexample
SELECT COUNT(i), COUNT(DISTINCT i), APPROX_COUNT_DISTINCT(i), HLL(i)
  FROM sequence_demo;
```

```output
+----------+-------------------+--------------------------+--------+
| COUNT(I) | COUNT(DISTINCT I) | APPROX_COUNT_DISTINCT(I) | HLL(I) |
|----------+-------------------+--------------------------+--------|
|     1024 |              1024 |                     1007 |   1007 |
+----------+-------------------+--------------------------+--------+
```
