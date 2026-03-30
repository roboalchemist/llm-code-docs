# Source: https://docs.snowflake.com/en/sql-reference/functions/hll_import.md

Categories:
:   [Aggregate functions](../functions-aggregation.md) (Cardinality Estimation) ,
    [Window functions](../functions-window-syntax.md) (Cardinality Estimation)

# HLL_IMPORT

Converts input in OBJECT format to BINARY format.

The HyperLogLog states operated on by HLL_ACCUMULATE, HLL_COMBINE, and HLL_ESTIMATE are in a proprietary binary format that may change in future versions of Snowflake. For long-term storage of HyperLogLog states, and for integration
with external tools, Snowflake supports using HLL_IMPORT to convert states from an OBJECT format to BINARY, and vice versa.

See also:
:   [HLL](hll.md) , [HLL_ACCUMULATE](hll_accumulate.md) , [HLL_ESTIMATE](hll_estimate.md) , [HLL_EXPORT](hll_export.md)

## Syntax

**Aggregate function**

```sqlsyntax
HLL_IMPORT( <obj> )
```

**Window function**

```sqlsyntax
HLL_IMPORT( <obj> ) OVER ( [ PARTITION BY <expr> ] )
```

For details about the OVER clause, see [Window function syntax and usage](../functions-window-syntax.md).

## Arguments

`obj`
:   An expression that evaluates to a HyperLogLog state in OBJECT format.

## Usage notes

* This function can be used as an [aggregate function](../functions-aggregation.md) or
  a [window function](../functions-window-syntax.md).

## Examples

See examples for [HLL_EXPORT](hll_export.md).
