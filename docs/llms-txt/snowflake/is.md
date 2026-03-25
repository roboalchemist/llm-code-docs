# Source: https://docs.snowflake.com/en/sql-reference/functions/is.md

Categories:
:   [Semi-structured and structured data functions](../functions-semistructured.md) (Type Predicates)

# IS_*<object_type>*

This family of functions serves as Boolean predicates that can be used to determine the data type of a value stored in a VARIANT column:

* [IS_ARRAY](is_array.md)
* [IS_BINARY](is_binary.md)
* [IS_BOOLEAN](is_boolean.md)
* [IS_CHAR , IS_VARCHAR](is_char-varchar.md)
* [IS_DATE , IS_DATE_VALUE](is_date-value.md)
* [IS_DECIMAL](is_decimal.md)
* [IS_DOUBLE , IS_REAL](is_double-real.md)
* [IS_INTEGER](is_integer.md)
* [IS_NULL_VALUE](is_null_value.md)
* [IS_OBJECT](is_object.md)
* [IS_TIME](is_time.md)
* [IS_TIMESTAMP_\*](is_timestamp.md)

See also:
:   [AS_<object_type>](as.md) , [TYPEOF](typeof.md)

## General usage notes

* All the functions are unary, taking a VARIANT expression as the only argument.
* All the functions return FALSE if the input is SQL NULL or the VARIANT expression contains NULL.

## Examples

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

Count all rows in `vartab` table where the VARIANT column `v` contains a string value:

```sqlexample
SELECT COUNT(*) FROM vartab WHERE IS_VARCHAR(v);
```

```output
+----------+
| COUNT(*) |
|----------|
|        1 |
+----------+
```

Select rows in `vartab` table where the VARIANT column `v` contains the specified data type:

```sqlexample
SELECT * FROM vartab WHERE IS_NULL_VALUE(v);
```

```output
+---+------+
| N | V    |
|---+------|
| 1 | null |
+---+------+
```

```sqlexample
SELECT * FROM vartab WHERE IS_BOOLEAN(v);
```

```output
+---+------+
| N | V    |
|---+------|
| 3 | true |
+---+------+
```

```sqlexample
SELECT * FROM vartab WHERE IS_INTEGER(v);
```

```output
+---+-----+
| N | V   |
|---+-----|
| 4 | -17 |
+---+-----+
```

```sqlexample
SELECT * FROM vartab WHERE IS_DECIMAL(v);
```

```output
+---+--------+
| N | V      |
|---+--------|
| 4 | -17    |
| 5 | 123.12 |
+---+--------+
```

```sqlexample
SELECT * FROM vartab WHERE IS_DOUBLE(v);
```

```output
+---+-----------------------+
| N | V                     |
|---+-----------------------|
| 4 | -17                   |
| 5 | 123.12                |
| 6 | 1.912000000000000e+02 |
+---+-----------------------+
```

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

```sqlexample
SELECT * FROM vartab WHERE IS_ARRAY(v);
```

```output
+---+-------------+
| N | V           |
|---+-------------|
| 8 | [           |
|   |   -1,       |
|   |   12,       |
|   |   289,      |
|   |   2188,     |
|   |   false,    |
|   |   undefined |
|   | ]           |
+---+-------------+
```

```sqlexample
SELECT * FROM vartab WHERE IS_OBJECT(v);
```

```output
+---+---------------+
| N | V             |
|---+---------------|
| 9 | {             |
|   |   "x": "abc", |
|   |   "y": false, |
|   |   "z": 10     |
|   | }             |
+---+---------------+
```
