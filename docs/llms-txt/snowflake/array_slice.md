# Source: https://docs.snowflake.com/en/sql-reference/functions/array_slice.md

Categories:
:   [Semi-structured and structured data functions](../functions-semistructured.md) (Array/Object)

# ARRAY_SLICE

Returns an array constructed from a specified subset of elements of the input array.

## Syntax

```sqlsyntax
ARRAY_SLICE( <array> , <from> , <to> )
```

## Arguments

`array`
:   The source array of which a subset of the elements are used to construct the resulting array.

`from`
:   A position in the source array. The position of the first element is `0`. Elements from positions less than `from`
    aren’t included in the resulting array.

`to`
:   A position in the source array. Elements from positions equal to or greater than `to` are not included in
    the resulting array.

## Returns

This function returns a value of type ARRAY.

Returns NULL if the any argument is NULL, including the input `array`, `from`, or `to`.

## Usage notes

* The output includes elements up to, but not including the element
  specified by the parameter `to`.
* If either `from` or `to` is negative, it is relative to
  the end of the array, not the beginning of the array. For example, `-2` refers
  to the second-from-the-last position in the array.
* If `from` and `to` are both beyond the upper end of the
  array, or are both beyond the lower end of the array, then the result is
  the empty set.
* When you pass a [structured array](../data-types-structured.md) to the function, the function returns a structured
  array of the same type.

Note that many of these rules (for example, interpretation of negative numbers as
indexes from the end of the array, and the rule that the slice is up to, but
not including, the `to` index), are similar to the rules for array
slices in programming languages such as Python.

Each of these rules is illustrated in at least one example below.

## Examples

These examples use [ARRAY constants](../data-types-semistructured.md) to construct arrays. Alternatively, you can
use the [ARRAY_CONSTRUCT](array_construct.md) function to construct arrays.

This example shows a simple array slice:

```sqlexample
SELECT ARRAY_SLICE([0,1,2,3,4,5,6], 0, 2);
```

```output
+------------------------------------+
| ARRAY_SLICE([0,1,2,3,4,5,6], 0, 2) |
|------------------------------------|
| [                                  |
|   0,                               |
|   1                                |
| ]                                  |
+------------------------------------+
```

This example slices an array to the last index by using the [ARRAY_SIZE](array_size.md) function with the
ARRAY_SLICE function:

```sqlexample
SELECT ARRAY_SLICE([0,1,2,3,4,5,6], 3, ARRAY_SIZE([0,1,2,3,4,5,6])) AS slice_to_last_index;
```

```output
+---------------------+
| SLICE_TO_LAST_INDEX |
|---------------------|
| [                   |
|   3,                |
|   4,                |
|   5,                |
|   6                 |
| ]                   |
+---------------------+
```

Although the indexes must be numeric, the elements of the array don’t need
to be numeric:

```sqlexample
SELECT ARRAY_SLICE(['foo','snow','flake','bar'], 1, 3);
```

```output
+-------------------------------------------------+
| ARRAY_SLICE(['FOO','SNOW','FLAKE','BAR'], 1, 3) |
|-------------------------------------------------|
| [                                               |
|   "snow",                                       |
|   "flake"                                       |
| ]                                               |
+-------------------------------------------------+
```

This example shows the effect of using NULL as the input array:

```sqlexample
SELECT ARRAY_SLICE(NULL, 2, 3);
```

```output
+-------------------------+
| ARRAY_SLICE(NULL, 2, 3) |
|-------------------------|
| NULL                    |
+-------------------------+
```

This example shows the effect of using NULL as one of the slice indexes:

```sqlexample
SELECT ARRAY_SLICE([0,1,2,3,4,5,6], NULL, 2);
```

```output
+---------------------------------------+
| ARRAY_SLICE([0,1,2,3,4,5,6], NULL, 2) |
|---------------------------------------|
| NULL                                  |
+---------------------------------------+
```

This example shows the effect of using a negative number as an index. The number
is interpreted as the offset from the end of the array:

```sqlexample
SELECT ARRAY_SLICE([0,1,2,3,4,5,6], 0, -2);
```

```output
+-------------------------------------+
| ARRAY_SLICE([0,1,2,3,4,5,6], 0, -2) |
|-------------------------------------|
| [                                   |
|   0,                                |
|   1,                                |
|   2,                                |
|   3,                                |
|   4                                 |
| ]                                   |
+-------------------------------------+
```

This example shows that both indexes can be negative (that is, both can be relative to the end of
the array):

```sqlexample
SELECT ARRAY_SLICE([0,1,2,3,4,5,6], -5, -3);
```

```output
+--------------------------------------+
| ARRAY_SLICE([0,1,2,3,4,5,6], -5, -3) |
|--------------------------------------|
| [                                    |
|   2,                                 |
|   3                                  |
| ]                                    |
+--------------------------------------+
```

In this example, both indexes are beyond the end of the array:

```sqlexample
SELECT ARRAY_SLICE([0,1,2,3,4,5,6], 10, 12);
```

```output
+--------------------------------------+
| ARRAY_SLICE([0,1,2,3,4,5,6], 10, 12) |
|--------------------------------------|
| []                                   |
+--------------------------------------+
```

In this example, both indexes are before the start of the array:

```sqlexample
SELECT ARRAY_SLICE([0,1,2,3,4,5,6], -10, -12);
```

```output
+----------------------------------------+
| ARRAY_SLICE([0,1,2,3,4,5,6], -10, -12) |
|----------------------------------------|
| []                                     |
+----------------------------------------+
```
