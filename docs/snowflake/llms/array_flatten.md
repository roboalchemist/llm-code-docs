# Source: https://docs.snowflake.com/en/sql-reference/functions/array_flatten.md

Categories:
:   [Semi-structured and structured data functions](../functions-semistructured.md) (Array/Object)

# ARRAY_FLATTEN

Flattens an [ARRAY](../data-types-semistructured.md) of ARRAYs into a single ARRAY. The function effectively concatenates the ARRAYs that
are elements of the input ARRAY and returns them as a single ARRAY.

## Syntax

```sqlsyntax
ARRAY_FLATTEN( <array> )
```

## Arguments

`array`
:   The ARRAY of ARRAYs to flatten.

    If any element of `array` is not an ARRAY, the function reports an error.

## Returns

This function returns an ARRAY that is constructed by concatenating the ARRAYs in `array`.

If `array` is NULL or contains any elements that are NULL, the function returns NULL.

## Usage notes

* If `array` contains multiple levels of nested ARRAYs, the function only removes one level of nesting.

  For example, if the input ARRAY is:

  ```output
  [ [ [1, 2], [3] ], [ [4], [5] ] ]
  ```

  The function returns:

  ```sqlexample
  [ [1, 2], [3], [4], [5] ]
  ```

## Examples

The following example flattens an ARRAY of ARRAYs. Each element in the input ARRAY is an ARRAY of numbers. The example flattens
the input ARRAY into an ARRAY containing the numbers as elements.

```sqlexample
SELECT ARRAY_FLATTEN([[1, 2, 3], [4], [5, 6]]);
```

```output
+-----------------------------------------+
| ARRAY_FLATTEN([[1, 2, 3], [4], [5, 6]]) |
|-----------------------------------------|
| [                                       |
|   1,                                    |
|   2,                                    |
|   3,                                    |
|   4,                                    |
|   5,                                    |
|   6                                     |
| ]                                       |
+-----------------------------------------+
```

The following example flattens an ARRAY that contains ARRAYs containing ARRAYs. The function removes the first level of nesting.

```sqlexample
SELECT ARRAY_FLATTEN([[[1, 2], [3]], [[4], [5]]]);
```

```output
+--------------------------------------------+
| ARRAY_FLATTEN([[[1, 2], [3]], [[4], [5]]]) |
|--------------------------------------------|
| [                                          |
|   [                                        |
|     1,                                     |
|     2                                      |
|   ],                                       |
|   [                                        |
|     3                                      |
|   ],                                       |
|   [                                        |
|     4                                      |
|   ],                                       |
|   [                                        |
|     5                                      |
|   ]                                        |
| ]                                          |
+--------------------------------------------+
```

The following example demonstrates that the function returns an error when an element of the input ARRAY is not an ARRAY.

```sqlexample
SELECT ARRAY_FLATTEN([[1, 2, 3], 4, [5, 6]]);
```

```output
100107 (22000): Not an array: 'Input argument to ARRAY_FLATTEN is not an array of arrays'
```

The following example demonstrates that the function returns NULL when an element of the input ARRAY is NULL.

```sqlexample
SELECT ARRAY_FLATTEN([[1, 2, 3], NULL, [5, 6]]);
```

```output
+------------------------------------------+
| ARRAY_FLATTEN([[1, 2, 3], NULL, [5, 6]]) |
|------------------------------------------|
| NULL                                     |
+------------------------------------------+
```

The following example demonstrates that the function flattens an ARRAY when an element of the input ARRAY is an ARRAY that
contains a NULL element.

```sqlexample
SELECT ARRAY_FLATTEN([[1, 2, 3], [NULL], [5, 6]]);
```

```output
+--------------------------------------------+
| ARRAY_FLATTEN([[1, 2, 3], [NULL], [5, 6]]) |
|--------------------------------------------|
| [                                          |
|   1,                                       |
|   2,                                       |
|   3,                                       |
|   undefined,                               |
|   5,                                       |
|   6                                        |
| ]                                          |
+--------------------------------------------+
```
