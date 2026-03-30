# Source: https://docs.snowflake.com/en/sql-reference/functions/array_remove.md

Categories:
:   [Semi-structured and structured data functions](../functions-semistructured.md) (Array/Object)

# ARRAY_REMOVE

Given a source [ARRAY](../data-types-semistructured.md), returns an ARRAY with elements of the specified value removed.

For example, `ARRAY_REMOVE([2, 5, 7, 5, 1], 5)` returns an ARRAY with the elements equal to 5 removed (`[2, 7, 1]`).

## Syntax

```sqlsyntax
ARRAY_REMOVE( <array> , <value_of_elements_to_remove> )
```

## Arguments

`array`
:   The source array.

`value_of_elements_to_remove`
:   The VARIANT value of the elements to be removed. The function removes elements equal to this value.

    If you specify a VARCHAR value, you must first cast the value to VARIANT.

## Returns

An ARRAY with all elements equal to the specified value removed.

If `value_of_elements_to_remove` is NULL, the function returns NULL.

## Usage notes

* If all of the elements in `array` are equal to `value_of_elements_to_remove`, the function returns an empty
  ARRAY.

## Examples

The following example returns an ARRAY with elements with the value 5 removed.

```sqlexample
SELECT ARRAY_REMOVE(
  [1, 5, 5.00, 5.00::DOUBLE, '5', 5, NULL],
  5);
```

```output
+---------------------------------------------+
| ARRAY_REMOVE(                               |
|   [1, 5, 5.00, 5.00::DOUBLE, '5', 5, NULL], |
|   5)                                        |
|---------------------------------------------|
| [                                           |
|   1,                                        |
|   "5",                                      |
|   undefined                                 |
| ]                                           |
+---------------------------------------------+
```

The following example removes the elements with the value 5 from an ARRAY that contains only elements with the value 5. The
function returns an empty ARRAY:

```sqlexample
SELECT ARRAY_REMOVE([5, 5], 5);
```

```output
+-------------------------+
| ARRAY_REMOVE([5, 5], 5) |
|-------------------------|
| []                      |
+-------------------------+
```

The following example removes elements with the value `'a'` from an ARRAY. As shown in the example, you must cast the value
as VARIANT.

```sqlexample
SELECT ARRAY_REMOVE(
  ['a', 'b', 'a', 'c', 'd', 'a'],
  'a'::VARIANT);
```

```output
+-----------------------------------+
| ARRAY_REMOVE(                     |
|   ['A', 'B', 'A', 'C', 'D', 'A'], |
|   'A'::VARIANT)                   |
|-----------------------------------|
| [                                 |
|   "b",                            |
|   "c",                            |
|   "d"                             |
| ]                                 |
+-----------------------------------+
```
