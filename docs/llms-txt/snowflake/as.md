# Source: https://docs.snowflake.com/en/sql-reference/functions/as.md

Categories:
:   [Semi-structured and structured data functions](../functions-semistructured.md) (Cast)

# AS_*<object_type>*

You can use this family of functions to perform strict casting of VARIANT values to values of other data types:

> * [AS_ARRAY](as_array.md)
> * [AS_BINARY](as_binary.md)
> * [AS_BOOLEAN](as_boolean.md)
> * [AS_CHAR , AS_VARCHAR](as_char-varchar.md)
> * [AS_DATE](as_date.md)
> * [AS_DECIMAL , AS_NUMBER](as_decimal-number.md)
> * [AS_DOUBLE , AS_REAL](as_double-real.md)
> * [AS_INTEGER](as_integer.md)
> * [AS_OBJECT](as_object.md)
> * [AS_TIME](as_time.md)
> * [AS_TIMESTAMP_\*](as_timestamp.md)

See also:
:   [IS_<object_type>](is.md)

## General usage notes

* If the type of the value in the VARIANT argument doesn’t match the output
  value, then NULL is returned. For example, if the AS_DATE function is passed a VARIANT value
  that doesn’t contain a DATE value, then NULL is returned.
* If the input is NULL, the output is NULL.

## Examples

The following examples use AS_`object_type` functions.

### Cast values in VARIANT columns to different data types

Create the table and load data into it:

```sqlexample
CREATE OR REPLACE TABLE multiple_types_example (
  array1 VARIANT,
  array2 VARIANT,
  boolean1 VARIANT,
  char1 VARIANT,
  varchar1 VARIANT,
  decimal1 VARIANT,
  double1 VARIANT,
  integer1 VARIANT,
  object1 VARIANT);

INSERT INTO multiple_types_example
  (array1, array2, boolean1, char1, varchar1,
   decimal1, double1, integer1, object1)
  SELECT
    TO_VARIANT(TO_ARRAY('Example')),
    TO_VARIANT(ARRAY_CONSTRUCT('Array-like', 'example')),
    TO_VARIANT(TRUE),
    TO_VARIANT('X'),
    TO_VARIANT('Y'),
    TO_VARIANT(1.23::DECIMAL(6, 3)),
    TO_VARIANT(3.21::DOUBLE),
    TO_VARIANT(15),
    TO_VARIANT(TO_OBJECT(PARSE_JSON('{"Tree": "Pine"}')));
```

Query the table and cast values in the VARIANT columns to values of different data types:

```sqlexample
SELECT AS_ARRAY(array1) AS array1,
       AS_ARRAY(array2) AS array2,
       AS_BOOLEAN(boolean1) AS boolean,
       AS_CHAR(char1) AS char,
       AS_VARCHAR(varchar1) AS varchar,
       AS_DECIMAL(decimal1, 6, 3) AS decimal,
       AS_DOUBLE(double1) AS double,
       AS_INTEGER(integer1) AS integer,
       AS_OBJECT(object1) AS object
  FROM multiple_types_example;
```

```output
+-------------+-----------------+---------+------+---------+---------+--------+---------+------------------+
| ARRAY1      | ARRAY2          | BOOLEAN | CHAR | VARCHAR | DECIMAL | DOUBLE | INTEGER | OBJECT           |
|-------------+-----------------+---------+------+---------+---------+--------+---------+------------------|
| [           | [               | True    | X    | Y       |   1.230 |   3.21 |      15 | {                |
|   "Example" |   "Array-like", |         |      |         |         |        |         |   "Tree": "Pine" |
| ]           |   "example"     |         |      |         |         |        |         | }                |
|             | ]               |         |      |         |         |        |         |                  |
+-------------+-----------------+---------+------+---------+---------+--------+---------+------------------+
```

### Compute the average of numeric values in a VARIANT column

Compute the average of all numeric values from a VARIANT column in the `vartab` table:

Create the table and load data into it:

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

Show the data types of the values (some of which are numeric):

```sqlexample
SELECT n, AS_REAL(v), TYPEOF(v)
  FROM vartab
  ORDER BY n;
```

```output
+---+------------+------------+
| N | AS_REAL(V) | TYPEOF(V)  |
|---+------------+------------|
| 1 |       NULL | NULL_VALUE |
| 2 |       NULL | NULL       |
| 3 |       NULL | BOOLEAN    |
| 4 |     -17    | INTEGER    |
| 5 |     123.12 | DECIMAL    |
| 6 |     191.2  | DOUBLE     |
| 7 |       NULL | VARCHAR    |
| 8 |       NULL | ARRAY      |
| 9 |       NULL | OBJECT     |
+---+------------+------------+
```

Use the AS_REAL function with the [AVG](avg.md) function to compute the average of all numeric values
from the VARIANT column `v`:

```sqlexample
SELECT AVG(AS_REAL(v)) FROM vartab;
```

```output
+-----------------+
| AVG(AS_REAL(V)) |
|-----------------|
|    99.106666667 |
+-----------------+
```
