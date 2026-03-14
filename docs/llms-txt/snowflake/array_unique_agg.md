# Source: https://docs.snowflake.com/en/sql-reference/functions/array_unique_agg.md

Categories:
:   [Aggregate functions](../functions-aggregation.md) (Counting Distinct Values) ,
    [Window functions](../functions-window-syntax.md) (Semi-structured Data Aggregation)

# ARRAY_UNIQUE_AGG

Returns an [ARRAY](../data-types-semistructured.md) that contains all of the distinct values from the specified column.

See also:
:   [Using Arrays to Compute Distinct Values for Hierarchical Aggregations](../../user-guide/querying-arrays-for-distinct-counts.md)

## Syntax

**Aggregate function**

```sqlsyntax
ARRAY_UNIQUE_AGG( <column> )
```

**Window function**

```sqlsyntax
ARRAY_UNIQUE_AGG( <column> ) OVER ( [ PARTITION BY <expr> ] )
```

For details about the OVER clause, see [Window function syntax and usage](../functions-window-syntax.md).

## Arguments

`column`
:   The column containing the values.

## Returns

The function returns an array containing the distinct values in the specified column. The values in the array are in no particular
order, and the order is not deterministic.

The function ignores NULL values in `column`. If `column` contains only NULL values or the table containing
`column` is empty, the function returns an empty array.

## Usage notes

* This function can be used as either of the following types of functions:

  * [aggregate function](../functions-aggregation.md)
  * [window function](../functions-window-syntax.md).
* When this function is called as a window function, it does not support explicit window frames.

* This function doesn’t support a [structured type](../data-types-structured.md) as an input argument.

## Examples

### Aggregation

See [Using Arrays to Compute Distinct Values for Hierarchical Aggregations](../../user-guide/querying-arrays-for-distinct-counts.md).
