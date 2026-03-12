# Source: https://docs.snowflake.com/en/sql-reference/functions/is_char-varchar.md

Categories:
:   [Semi-structured and structured data functions](../functions-semistructured.md) (Type Predicates)

# IS_CHAR , IS_VARCHAR

Returns TRUE if its [VARIANT](../data-types-semistructured.md) argument contains a [string value](../data-types-text.md).

These functions are synonymous.

See also:
:   [IS_<object_type>](is.md)

## Syntax

```sqlsyntax
IS_CHAR( <variant_expr> )

IS_VARCHAR( <variant_expr> )
```

## Arguments

`variant_expr`
:   An expression that evaluates to a value of type VARIANT.

## Returns

Returns a BOOLEAN value or NULL.

* Returns TRUE if the VARIANT value contains a string value. Otherwise, returns FALSE.
* If the input is NULL, returns NULL without reporting an error.

## Examples

The following examples use the IS_VARCHAR function.

### Use the IS_VARCHAR function in a WHERE clause

Create and fill the `vartab` table. The INSERT statement uses the [PARSE_JSON](parse_json.md) function to insert
[VARIANT](../data-types-semistructured.md) values in the `v` column of the table.

```sqlexample
CREATE OR REPLACE TABLE vartab (n NUMBER(2), v VARIANT);

INSERT INTO vartab
  SELECT column1 AS n, PARSE_JSON(column2) AS v
    FROM VALUES (1, 'null'),
                (2, null),
                (3, 'true'),
                (4, '-17'),
                (5, '123.12'),
                (6, '1.912e2'),
                (7, '"Om ara pa ca na dhih"  '),
                (8, '[-1, 12, 289, 2188, false,]'),
                (9, '{ "x" : "abc", "y" : false, "z": 10} ')
       AS vals;
```

Query the data. The query uses the [TYPEOF](typeof.md) function to show the data types of
the values stored in the VARIANT column.

```sqlexample
SELECT n, v, TYPEOF(v)
  FROM vartab
  ORDER BY n;
```

```output
+---+------------------------+------------+
| N | V                      | TYPEOF(V)  |
|---+------------------------+------------|
| 1 | null                   | NULL_VALUE |
| 2 | NULL                   | NULL       |
| 3 | true                   | BOOLEAN    |
| 4 | -17                    | INTEGER    |
| 5 | 123.12                 | DECIMAL    |
| 6 | 1.912000000000000e+02  | DOUBLE     |
| 7 | "Om ara pa ca na dhih" | VARCHAR    |
| 8 | [                      | ARRAY      |
|   |   -1,                  |            |
|   |   12,                  |            |
|   |   289,                 |            |
|   |   2188,                |            |
|   |   false,               |            |
|   |   undefined            |            |
|   | ]                      |            |
| 9 | {                      | OBJECT     |
|   |   "x": "abc",          |            |
|   |   "y": false,          |            |
|   |   "z": 10              |            |
|   | }                      |            |
+---+------------------------+------------+
```

Show the string values in the data by using the IS_VARCHAR function in a WHERE clause:

```sqlexample
SELECT * FROM vartab WHERE IS_VARCHAR(v);
```

```output
+---+------------------------+
| N | V                      |
|---+------------------------|
| 7 | "Om ara pa ca na dhih" |
+---+------------------------+
```

### Use the IS_VARCHAR function in a SELECT list

Create and fill the `multiple_types` table. The INSERT statement uses the [TO_VARIANT](to_variant.md) function to insert
[VARIANT](../data-types-semistructured.md) values in the columns.

```sqlexample
CREATE OR REPLACE TABLE multiple_types (
  array1 VARIANT,
  array2 VARIANT,
  boolean1 VARIANT,
  varchar1 VARIANT,
  varchar2 VARIANT,
  decimal1 VARIANT,
  double1 VARIANT,
  integer1 VARIANT,
  object1 VARIANT);

INSERT INTO multiple_types
    (array1, array2, boolean1, varchar1, varchar2,
     decimal1, double1, integer1, object1)
  SELECT
    TO_VARIANT(TO_ARRAY('Example')),
    TO_VARIANT(ARRAY_CONSTRUCT('Array-like', 'example')),
    TO_VARIANT(TRUE),
    TO_VARIANT('X'),
    TO_VARIANT('I am a real character'),
    TO_VARIANT(1.23::DECIMAL(6, 3)),
    TO_VARIANT(3.21::DOUBLE),
    TO_VARIANT(15),
    TO_VARIANT(TO_OBJECT(PARSE_JSON('{"Tree": "Pine"}')));
```

Query the data using the [TYPEOF](typeof.md) function to show the data types of
the values stored in the VARIANT values.

```sqlexample
SELECT TYPEOF(array1),
       TYPEOF(array2),
       TYPEOF(boolean1),
       TYPEOF(varchar1),
       TYPEOF(varchar2),
       TYPEOF(decimal1),
       TYPEOF(double1),
       TYPEOF(integer1),
       TYPEOF(object1)
  FROM multiple_types;
```

```output
+----------------+----------------+------------------+------------------+------------------+------------------+-----------------+------------------+-----------------+
| TYPEOF(ARRAY1) | TYPEOF(ARRAY2) | TYPEOF(BOOLEAN1) | TYPEOF(VARCHAR1) | TYPEOF(VARCHAR2) | TYPEOF(DECIMAL1) | TYPEOF(DOUBLE1) | TYPEOF(INTEGER1) | TYPEOF(OBJECT1) |
|----------------+----------------+------------------+------------------+------------------+------------------+-----------------+------------------+-----------------|
| ARRAY          | ARRAY          | BOOLEAN          | VARCHAR          | VARCHAR          | DECIMAL          | DOUBLE          | INTEGER          | OBJECT          |
+----------------+----------------+------------------+------------------+------------------+------------------+-----------------+------------------+-----------------+
```

Show whether a column contains string values in the data by using the IS_VARCHAR function in a SELECT list:

```sqlexample
SELECT IS_VARCHAR(varchar1),
       IS_VARCHAR(boolean1)
  FROM multiple_types;
```

```output
+----------------------+----------------------+
| IS_VARCHAR(VARCHAR1) | IS_VARCHAR(BOOLEAN1) |
|----------------------+----------------------|
| True                 | False                |
+----------------------+----------------------+
```
