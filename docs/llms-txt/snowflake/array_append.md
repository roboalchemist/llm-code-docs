# Source: https://docs.snowflake.com/en/sql-reference/functions/array_append.md

Categories:
:   [Semi-structured and structured data functions](../functions-semistructured.md) (Array/Object)

# ARRAY_APPEND

Returns an array containing all elements from the source array as well as the new element. The new element is located at the end of the array.

See also:
:   [ARRAY_INSERT](array_insert.md) , [ARRAY_PREPEND](array_prepend.md)

## Syntax

```sqlsyntax
ARRAY_APPEND( <array> , <new_element> )
```

## Arguments

`array`
:   The source array.

`new_element`
:   The element to be appended. The type of the element depends on the type of the array:

    * If `array` is a [semi-structured array](../data-types-semistructured.md), the element can be of almost any data type.
      The data type can be different from the data type(s) of the existing elements in the array.
    * If `array` is a [structured array](../data-types-structured.md), the type of the new element must
      be [coercible](../data-types-structured.md) to the type of the array.

## Returns

The data type of the returned value is ARRAY.

When you pass a [structured array](../data-types-structured.md) to the function, the function returns a structured
array of the same type.

If the source array is NULL, the function returns NULL.

## Examples

The examples use the following table with an ARRAY column:

```sqlexample
CREATE OR REPLACE TABLE array_append_examples (array_column ARRAY);

INSERT INTO array_append_examples (array_column)
  SELECT ARRAY_CONSTRUCT(1, 2, 3);

SELECT * FROM array_append_examples;
```

```output
+--------------+
| ARRAY_COLUMN |
|--------------|
| [            |
|   1,         |
|   2,         |
|   3          |
| ]            |
+--------------+
```

Add an element of the same type to the array:

```sqlexample
UPDATE array_append_examples
  SET array_column = ARRAY_APPEND(array_column, 4);
```

Query the table to see the new element added to the array:

```sqlexample
SELECT * FROM array_append_examples;
```

```output
+--------------+
| ARRAY_COLUMN |
|--------------|
| [            |
|   1,         |
|   2,         |
|   3,         |
|   4          |
| ]            |
+--------------+
```

Add an element of a different type to the array:

```sqlexample
UPDATE array_append_examples
  SET array_column = ARRAY_APPEND(array_column, 'five');
```

Query the table to see the new element added to the array and the data type of each element in the array:

```sqlexample
SELECT array_column,
       ARRAY_CONSTRUCT(
        TYPEOF(array_column[0]),
        TYPEOF(array_column[1]),
        TYPEOF(array_column[2]),
        TYPEOF(array_column[3]),
        TYPEOF(array_column[4])) AS type
  FROM array_append_examples;
```

```output
+--------------+--------------+
| ARRAY_COLUMN | TYPE         |
|--------------+--------------|
| [            | [            |
|   1,         |   "INTEGER", |
|   2,         |   "INTEGER", |
|   3,         |   "INTEGER", |
|   4,         |   "INTEGER", |
|   "five"     |   "VARCHAR"  |
| ]            | ]            |
+--------------+--------------+
```
