# Source: https://docs.snowflake.com/en/sql-reference/functions/array_reverse.md

Categories:
:   [Semi-structured and structured data functions](../functions-semistructured.md) (Array/Object)

# ARRAY_REVERSE

Returns an [array](../data-types-semistructured.md) with the elements of the input array in reverse order.

## Syntax

```sqlsyntax
ARRAY_REVERSE( <array> )
```

## Arguments

`array`
:   The source array.

## Returns

An array containing the elements of the input array in reverse order.

## Usage notes

* If the argument is NULL, the result will be NULL.
* When you pass a [structured array](../data-types-structured.md) to the function, the function returns a structured
  array of the same type.

## Examples

The following example returns an array containing the elements from the input array in reverse order:

```sqlexample
SELECT ARRAY_REVERSE([1,2,3,4]);
```

```output
+--------------------------+
| ARRAY_REVERSE([1,2,3,4]) |
|--------------------------|
| [                        |
|   4,                     |
|   3,                     |
|   2,                     |
|   1                      |
| ]                        |
+--------------------------+
```
