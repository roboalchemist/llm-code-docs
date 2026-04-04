# Source: https://docs.snowflake.com/en/sql-reference/functions/to_array.md

Categories:
:   [Conversion functions](../functions-conversion.md) , [Semi-structured and structured data functions](../functions-semistructured.md) (Array/Object)

# TO_ARRAY

Converts the input expression to an [ARRAY](../data-types-semistructured.md) value.

## Syntax

```sqlsyntax
TO_ARRAY( <expr> )
```

## Arguments

`expr`
:   An expression of any data type.

## Returns

This function returns a value of type ARRAY or NULL:

> * If the input is an ARRAY, or a VARIANT containing an ARRAY value, the value is returned unchanged.
> * If `expr` is a NULL or [JSON null](../../user-guide/semistructured-considerations.md) value, the function returns NULL.
> * For any other value, the value returned is a single-element array that contains this value.

## Usage notes

To create an array that contains more than one element, you can use [ARRAY_CONSTRUCT](array_construct.md)
or [STRTOK_TO_ARRAY](strtok_to_array.md).

## Examples

Create a table, and insert data by calling the TO_ARRAY function:

```sqlexample
CREATE OR REPLACE TABLE array_demo_2 (
  ID INTEGER,
  array1 ARRAY,
  array2 ARRAY);

INSERT INTO array_demo_2 (ID, array1, array2)
  SELECT 1, TO_ARRAY(1), TO_ARRAY(3);

SELECT * FROM array_demo_2;
```

```output
+----+--------+--------+
| ID | ARRAY1 | ARRAY2 |
|----+--------+--------|
|  1 | [      | [      |
|    |   1    |   3    |
|    | ]      | ]      |
+----+--------+--------+
```

Execute a query that shows the single-element arrays created during the insert and
the result of calling ARRAY_CAT to concatenate the two arrays:

```sqlexample
SELECT array1, array2, ARRAY_CAT(array1, array2)
  FROM array_demo_2;
```

```output
+--------+--------+---------------------------+
| ARRAY1 | ARRAY2 | ARRAY_CAT(ARRAY1, ARRAY2) |
|--------+--------+---------------------------|
| [      | [      | [                         |
|   1    |   3    |   1,                      |
| ]      | ]      |   3                       |
|        |        | ]                         |
+--------+--------+---------------------------+
```

This example demonstrates that TO_ARRAY converts a string input expression to an array with a
single element, even when the input expression includes delimiters (such as commas):

```sqlexample
SELECT TO_ARRAY('snowman,snowball,snowcone') AS to_array_result;
```

```output
+-------------------------------+
| TO_ARRAY_RESULT               |
|-------------------------------|
| [                             |
|   "snowman,snowball,snowcone" |
| ]                             |
+-------------------------------+
```

To convert the same string input expression into an array with multiple elements, you can use the
[STRTOK_TO_ARRAY](strtok_to_array.md) function:

```sqlexample
SELECT STRTOK_TO_ARRAY('snowman,snowball,snowcone', ',') AS strtok_to_array_result;
```

```output
+------------------------+
| STRTOK_TO_ARRAY_RESULT |
|------------------------|
| [                      |
|   "snowman",           |
|   "snowball",          |
|   "snowcone"           |
| ]                      |
+------------------------+
```
