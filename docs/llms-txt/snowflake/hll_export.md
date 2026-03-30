# Source: https://docs.snowflake.com/en/sql-reference/functions/hll_export.md

Categories:
:   [Aggregate functions](../functions-aggregation.md) (Cardinality Estimation) ,
    [Window functions](../functions-window-syntax.md) (Cardinality Estimation)

# HLL_EXPORT

Converts input in BINARY format to OBJECT format.

The HyperLogLog states operated on by HLL_ACCUMULATE, HLL_COMBINE, and HLL_ESTIMATE are in a proprietary binary format that may change in future versions of Snowflake. For long-term storage of HyperLogLog states, and for integration
with external tools, Snowflake supports converting states from the BINARY format to an OBJECT (which can be printed and exported as JSON), and vice versa.

See also:
:   [HLL](hll.md) , [HLL_ACCUMULATE](hll_accumulate.md) , [HLL_ESTIMATE](hll_estimate.md) , [HLL_IMPORT](hll_import.md)

## Syntax

**Aggregate function**

```sqlsyntax
HLL_EXPORT( <binary_expr> )
```

**Window function**

```sqlsyntax
HLL_EXPORT( <binary_expr> ) OVER ( [ PARTITION BY <expr> ] )
```

For details about the OVER clause, see [Window function syntax and usage](../functions-window-syntax.md).

## Arguments

`binary_expr`
:   An expression that evaluates to a HyperLogLog state in BINARY format.

## Usage notes

* This function can be used as an [aggregate function](../functions-aggregation.md) or
  a [window function](../functions-window-syntax.md).

## Examples

```sqlexample
SELECT HLL(o_orderdate), HLL_ESTIMATE(HLL_IMPORT(HLL_EXPORT(HLL_ACCUMULATE(o_orderdate))))
FROM orders;

------------------+-------------------------------------------------------------------+
 HLL(O_ORDERDATE) | HLL_ESTIMATE(HLL_IMPORT(HLL_EXPORT(HLL_ACCUMULATE(O_ORDERDATE)))) |
------------------+-------------------------------------------------------------------+
 2398             | 2398                                                              |
------------------+-------------------------------------------------------------------+
```
