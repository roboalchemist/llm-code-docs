# Source: https://docs.snowflake.com/en/sql-reference/functions/array_except.md

Categories:
:   [Semi-structured and structured data functions](../functions-semistructured.md) (Array/Object)

# ARRAY_EXCEPT

Returns a new [ARRAY](../data-types-semistructured.md) that contains the elements from one input ARRAY that are not in another input
ARRAY.

The function is NULL-safe, meaning it treats NULLs as known values for comparing equality.

See also:
:   [ARRAY_INTERSECTION](array_intersection.md)

## Syntax

```sqlsyntax
ARRAY_EXCEPT( <source_array> , <array_of_elements_to_exclude> )
```

## Arguments

`source_array`
:   An array that contains elements to be included in the new ARRAY.

`array_of_elements_to_exclude`
:   An array that contains elements to be excluded from the new ARRAY.

## Returns

This function returns an ARRAY that contains the elements from `source_array` that are not in
`array_of_elements_to_exclude`.

If no elements remain after excluding the elements in `array_of_elements_to_exclude` from `source_array`, the
function returns an empty ARRAY.

If one or both arguments are NULL, the function returns NULL.

The order of the values within the returned array is unspecified.

## Usage notes

* When you compare data of the type OBJECT, the objects must be identical to be considered matching. For details,
  see Examples (in this topic).
* In Snowflake, arrays are multi-sets, not sets. In other words, arrays can contain multiple copies of the same value.

  `ARRAY_EXCEPT` compares arrays by using multi-set semantics (sometimes called “bag semantics”). If
  `source_array` includes multiple copies of a value, the function only removes the number of copies of that value that
  are specified in `array_of_elements_to_exclude`.

  In other words, if `source_array` has N copies of a value and `array_of_elements_to_exclude` has M copies of the
  same value, the function excludes M copies of the value from the returned array. The number of copies of the value in the
  returned array is N - M or, if M is larger than N, 0.

  For example, if `source_array` contains 5 elements with the value `'A'` and `array_of_elements_to_exclude`
  contains 2 elements with the value `'A'`, the returned array contains 3 elements with the value `'A'`.

* Both arguments must either be [structured ARRAYs](../data-types-structured.md) or
  [semi-structured ARRAYs](../data-types-semistructured.md).

* If you are passing in a structured ARRAY:

  * The ARRAY in the second argument must be [comparable](../data-types-structured.md) to the ARRAY in
    the first argument.
  * The function returns a structured ARRAY of the same type as the ARRAY in the first argument.

## Examples

The examples in this section use [ARRAY constants](../data-types-semistructured.md) and [OBJECT constants](../data-types-semistructured.md)
to specify ARRAYs and OBJECTs.

The following example demonstrates how to use the function:

```sqlexample
SELECT ARRAY_EXCEPT(['A', 'B'], ['B', 'C']);

+--------------------------------------+
| ARRAY_EXCEPT(['A', 'B'], ['B', 'C']) |
|--------------------------------------|
| [                                    |
|   "A"                                |
| ]                                    |
+--------------------------------------+
```

The following example adds the element `'C'` to `source_array`. The returned ARRAY excludes `'C'` because `'C'` is
also specified in `array_of_elements_to_exclude`.

```sqlexample
SELECT ARRAY_EXCEPT(['A', 'B', 'C'], ['B', 'C']);

+-------------------------------------------+
| ARRAY_EXCEPT(['A', 'B', 'C'], ['B', 'C']) |
|-------------------------------------------|
| [                                         |
|   "A"                                     |
| ]                                         |
+-------------------------------------------+
```

In the following example, `source_array` contains 3 elements with the value `'B'`. Because
`array_of_elements_to_exclude` contains only 1 `'B'` element, the function excludes only 1 `'B'` element and returns
an ARRAY containing the other 2 `'B'` elements.

```sqlexample
SELECT ARRAY_EXCEPT(['A', 'B', 'B', 'B', 'C'], ['B']);

+------------------------------------------------+
| ARRAY_EXCEPT(['A', 'B', 'B', 'B', 'C'], ['B']) |
|------------------------------------------------|
| [                                              |
|   "A",                                         |
|   "B",                                         |
|   "B",                                         |
|   "C"                                          |
| ]                                              |
+------------------------------------------------+
```

In the following example, no elements remain after excluding the elements in `array_of_elements_to_exclude` from
`source_array`. As a result, the function returns an empty ARRAY.

```sqlexample
SELECT ARRAY_EXCEPT(['A', 'B'], ['A', 'B']);

+--------------------------------------+
| ARRAY_EXCEPT(['A', 'B'], ['A', 'B']) |
|--------------------------------------|
| []                                   |
+--------------------------------------+
```

The following example demonstrates how the function treats NULL elements as known values. As explained earlier, because
`source_array` contains one more NULL element than `array_of_elements_to_exclude`, the returned ARRAY excludes
only one NULL element and includes the other (which is printed out as `undefined`).

```sqlexample
SELECT ARRAY_EXCEPT(['A', NULL, NULL], ['B', NULL]);

+----------------------------------------------+
| ARRAY_EXCEPT(['A', NULL, NULL], ['B', NULL]) |
|----------------------------------------------|
| [                                            |
|   "A",                                       |
|   undefined                                  |
| ]                                            |
+----------------------------------------------+
```

In the following example, `source_array` and `array_of_elements_to_exclude` contain the same number of NULL
elements, so the returned ARRAY excludes the NULL elements.

```sqlexample
SELECT ARRAY_EXCEPT(['A', NULL, NULL], [NULL, 'B', NULL]);

+----------------------------------------------------+
| ARRAY_EXCEPT(['A', NULL, NULL], [NULL, 'B', NULL]) |
|----------------------------------------------------|
| [                                                  |
|   "A"                                              |
| ]                                                  |
+----------------------------------------------------+
```

The following example demonstrates how specifying the same object in `source_array` and
`array_of_elements_to_exclude` excludes that object from the returned ARRAY:

```sqlexample
SELECT ARRAY_EXCEPT([{'a': 1, 'b': 2}, 1], [{'a': 1, 'b': 2}, 3]);

+------------------------------------------------------------+
| ARRAY_EXCEPT([{'A': 1, 'B': 2}, 1], [{'A': 1, 'B': 2}, 3]) |
|------------------------------------------------------------|
| [                                                          |
|   1                                                        |
| ]                                                          |
+------------------------------------------------------------+
```

The following example demonstrates that passing in NULL results in the function returning NULL.

```sqlexample
SELECT ARRAY_EXCEPT(['A', 'B'], NULL);

+--------------------------------+
| ARRAY_EXCEPT(['A', 'B'], NULL) |
|--------------------------------|
| NULL                           |
+--------------------------------+
```
