# Source: https://docs.snowflake.com/en/sql-reference/functions/agg.md

Categories:
:   [Aggregate functions](../functions-aggregation.md) (Semantic Views)

# AGG

Evaluates and returns the value of a metric in a [semantic view](../../user-guide/views-semantic/overview.md) when you
[run a query](../../user-guide/views-semantic/querying.md).

## Syntax

```sqlsyntax
AGG( <metric_in_semantic_view> )
```

## Arguments

`metric_in_semantic_view`
:   Metric that you want to return in a query of a semantic view.

## Returns

Returns the value of the specified metric.
