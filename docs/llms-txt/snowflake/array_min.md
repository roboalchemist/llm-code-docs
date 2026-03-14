# Source: https://docs.snowflake.com/en/sql-reference/functions/array_min.md

Categories:
:   [Semi-structured and structured data functions](../functions-semistructured.md) (Array/Object)

# ARRAY_MIN

Given an input [ARRAY](../data-types-semistructured.md), returns the element with the lowest value that is not a SQL NULL. If the input ARRAY
is empty or contains only SQL NULL elements, this function returns NULL.

## Syntax

```sqlsyntax
ARRAY_MIN( <array> )
```

## Arguments

`array`
:   The input ARRAY.

## Returns

This function returns a [VARIANT](../data-types-semistructured.md) that contains the element with the lowest value that is not a SQL NULL.

The function returns NULL if `array` is NULL, empty, or contains only SQL NULL elements.

## Usage notes

* A SQL NULL is distinct from an explicit null value in semi-structured data (for example, a [JSON null](../../user-guide/semistructured-considerations.md)
  in JSON data). Explicit null values are considered when identifying the element with the lowest value.

* The function determines the element to return by comparing the elements in the array. The function supports comparing elements
  of the same data type or of the following data types:

  * Elements of the NUMBER and FLOAT data types.
  * Elements of the TIMESTAMP_LTZ and TIMESTAMP_TZ data types.

  If the array contains elements of other data types, [cast](cast.md) the elements to a common data type,
  as shown in the example below.

## Examples

The following example returns a VARIANT containing the element with the lowest value in an
[ARRAY constant](../data-types-semistructured.md):

```sqlexample
SELECT ARRAY_MIN([20, 0, NULL, 10, NULL]);
```

```output
+------------------------------------+
| ARRAY_MIN([20, 0, NULL, 10, NULL]) |
|------------------------------------|
| 0                                  |
+------------------------------------+
```

The following example demonstrates that the function returns NULL if the input ARRAY is empty:

```sqlexample
SELECT ARRAY_MIN([]);
```

```output
+---------------+
| ARRAY_MIN([]) |
|---------------|
| NULL          |
+---------------+
```

The following example demonstrates that the function returns NULL if the input ARRAY contains only SQL NULLs:

```sqlexample
SELECT ARRAY_MIN([NULL, NULL, NULL]);
```

```output
+-------------------------+
| ARRAY_MIN([NULL, NULL]) |
|-------------------------|
| NULL                    |
+-------------------------+
```

To determine the minimum value in an array with elements of different data types, [cast](cast.md) the elements
to the same data type. The following example casts a DATE element to a TIMESTAMP element to determine the minimum value in the array:

```sqlexample
SELECT ARRAY_MIN([date1::TIMESTAMP, timestamp1]) AS array_min
  FROM (
      VALUES ('1999-01-01'::DATE, '2023-12-09 22:09:26.000000000'::TIMESTAMP),
             ('2023-12-09'::DATE, '1999-01-01 22:09:26.000000000'::TIMESTAMP)
          AS t(date1, timestamp1)
      );
```

```output
+---------------------------+
| ARRAY_MIN                 |
|---------------------------|
| "1999-01-01 00:00:00.000" |
| "1999-01-01 22:09:26.000" |
+---------------------------+
```
