# Source: https://docs.snowflake.com/en/sql-reference/functions/to_boolean.md

Categories:
:   [Conversion functions](../functions-conversion.md)

# TO_BOOLEAN

Converts the input text or numeric expression to a [BOOLEAN](../data-types-logical.md) value.

See also:
:   [TRY_TO_BOOLEAN](try_to_boolean.md)

## Syntax

```sqlsyntax
TO_BOOLEAN( <string_or_numeric_expr> )
```

## Arguments

`string_or_numeric_expr`
:   A string expression or numeric expression that can be evaluated to a BOOLEAN value.

## Returns

Returns a BOOLEAN value or NULL.

* Returns TRUE if `string_or_numeric_expr` evaluates to TRUE.
* Returns FALSE if `string_or_numeric_expr` evaluates to FALSE.
* If the input is NULL, returns NULL without reporting an error.

## Usage notes

* For a string expression:

  * `'true'`, `'t'`, `'yes'`, `'y'`, `'on'`, `'1'` return TRUE.
  * `'false'`, `'f'`, `'no'`, `'n'`, `'off'`, `'0'` return FALSE.
  * All other strings return an error.

  The evaluations of the strings are case-insensitive.
* For a numeric expression:

  * `0` returns FALSE.
  * All non-zero numeric values return TRUE.
  * When converting from the [FLOAT](../data-types-numeric.md) data type, non-numeric values, such as
    `NaN` (not a number) and `INF` (infinity), return an error.

## Examples

The following examples use the TO_BOOLEAN function.

Create a table and insert data:

```sqlexample
CREATE OR REPLACE TABLE test_boolean(
  b BOOLEAN,
  n NUMBER,
  s STRING);

INSERT INTO test_boolean VALUES
  (true, 1, 'yes'),
  (false, 0, 'no'),
  (null, null, null);

SELECT * FROM test_boolean;
```

```output
+-------+------+------+
| B     |    N | S    |
|-------+------+------|
| True  |    1 | yes  |
| False |    0 | no   |
| NULL  | NULL | NULL |
+-------+------+------+
```

Convert a text string to a BOOLEAN value:

```sqlexample
SELECT s, TO_BOOLEAN(s) FROM test_boolean;
```

```output
+------+---------------+
| S    | TO_BOOLEAN(S) |
|------+---------------|
| yes  | True          |
| no   | False         |
| NULL | NULL          |
+------+---------------+
```

Convert a number to a BOOLEAN value:

```sqlexample
SELECT n, TO_BOOLEAN(n) FROM test_boolean;
```

```output
+------+---------------+
|    N | TO_BOOLEAN(N) |
|------+---------------|
|    1 | True          |
|    0 | False         |
| NULL | NULL          |
+------+---------------+
```
