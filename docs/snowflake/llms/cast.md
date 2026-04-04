# Source: https://docs.snowflake.com/en/sql-reference/functions/cast.md

Categories:
:   [Conversion functions](../functions-conversion.md)

# CAST , `::`

Converts a value of one data type into another data type. The semantics of CAST
are the same as the semantics of the corresponding TO_`datatype` conversion
functions. If the cast is not possible, an error is raised. For more details,
see the individual TO_ `datatype` conversion functions. For more information
about data type conversion and the TO_ `datatype` conversion
functions, see [Data type conversion](../data-type-conversion.md).

The `::` operator provides alternative syntax for CAST.

See also:
:   [TRY_CAST](try_cast.md)

## Syntax

```sqlsyntax
CAST( <source_expr> AS <target_data_type> )
  [ RENAME FIELDS | ADD FIELDS ]

<source_expr> :: <target_data_type>
```

## Arguments

`source_expr`
:   Expression of any supported data type to be converted into a
    different data type.

`target_data_type`
:   The data type to which to convert the expression. If the data
    type supports additional properties, such as
    [precision and scale](../data-types-numeric.md)
    (for numbers/decimals), the properties can be included.

`RENAME FIELDS`
:   For [structured OBJECTs](../data-types-structured.md), specifies that you want to change the OBJECT to use
    different key-value pairs. The values in the original object are copied to the new key-value pairs in the order in which
    they appear.

    For an example, see [Example: Changing the key names in an OBJECT value](../data-types-structured.md).

`ADD FIELDS`
:   For [structured OBJECTs](../data-types-structured.md), specifies that you want to add key-value pairs to the
    OBJECT.

    For an example, see [Example: Adding keys to an OBJECT value](../data-types-structured.md).

    The values for the newly added keys will be set to NULL. If you want to assign a value to these keys, call the
    [OBJECT_INSERT](../data-types-structured.md) function instead.

## Usage notes

* If the scale is not sufficient to hold the input value, the function
  rounds the value.
* If the precision is not sufficient to hold the input value, the function
  raises an error.
* When numeric columns are explicitly cast to forms of the integer data type during a data unload to Parquet files, the data type of these
  columns in the Parquet files is INT. For more information, see [Explicitly convert numeric columns to Parquet data types](../../user-guide/data-unload-considerations.md).
* Collation specifications aren’t retained when values to are cast to
  [text string data types](../data-types-text.md) (for example, VARCHAR and STRING). You can include collation
  specifications when you cast values (for example, `CAST(myvalue AS VARCHAR) COLLATE 'en-ai'`).
* When you use the `::` alternative syntax, you cannot specify the `RENAME FIELDS` or `ADD FIELDS` arguments.

## Examples

The CAST examples use the data in the following table:

```sqlexample
CREATE OR REPLACE TABLE test_data_type_conversion (
  varchar_value VARCHAR,
  number_value NUMBER(5, 4),
  timestamp_value TIMESTAMP);

INSERT INTO test_data_type_conversion VALUES (
  '9.8765',
  1.2345,
  '2024-05-09 14:32:29.135 -0700');

SELECT * FROM test_data_type_conversion;
```

```output
+---------------+--------------+-------------------------+
| VARCHAR_VALUE | NUMBER_VALUE | TIMESTAMP_VALUE         |
|---------------+--------------+-------------------------|
| 9.8765        |       1.2345 | 2024-05-09 14:32:29.135 |
+---------------+--------------+-------------------------+
```

The examples use the [SYSTEM$TYPEOF](system_typeof.md) function to show the data type of the converted value.

Convert a string to a number with specified scale (2):

```sqlexample
SELECT CAST(varchar_value AS NUMBER(5,2)) AS varchar_to_number1,
       SYSTEM$TYPEOF(varchar_to_number1) AS data_type
  FROM test_data_type_conversion;
```

```output
+--------------------+------------------+
| VARCHAR_TO_NUMBER1 | DATA_TYPE        |
|--------------------+------------------|
|               9.88 | NUMBER(5,2)[SB4] |
+--------------------+------------------+
```

Convert the same string to a number with scale 5, using
the `::` notation:

```sqlexample
SELECT varchar_value::NUMBER(6,5) AS varchar_to_number2,
       SYSTEM$TYPEOF(varchar_to_number2) AS data_type
  FROM test_data_type_conversion;
```

```output
+--------------------+------------------+
| VARCHAR_TO_NUMBER2 | DATA_TYPE        |
|--------------------+------------------|
|            9.87650 | NUMBER(6,5)[SB4] |
+--------------------+------------------+
```

Convert a number to an integer. For an integer, precision and scale cannot be specified, so
the default is always NUMBER(38, 0).

```sqlexample
SELECT CAST(number_value AS INTEGER) AS number_to_integer,
       SYSTEM$TYPEOF(number_to_integer) AS data_type
  FROM test_data_type_conversion;
```

```output
+-------------------+-------------------+
| NUMBER_TO_INTEGER | DATA_TYPE         |
|-------------------+-------------------|
|                 1 | NUMBER(38,0)[SB1] |
+-------------------+-------------------+
```

Convert a number to a string:

```sqlexample
SELECT CAST(number_value AS VARCHAR) AS number_to_varchar,
       SYSTEM$TYPEOF(number_to_varchar) AS data_type
  FROM test_data_type_conversion;
```

```output
+-------------------+--------------+
| NUMBER_TO_VARCHAR | DATA_TYPE    |
|-------------------+--------------|
| 1.2345            | VARCHAR[LOB] |
+-------------------+--------------+
```

Convert a string to a VARCHAR with a specified length. If the source value exceeds
the specified length, the value is truncated:

```sqlexample
SELECT varchar_value,
       CAST(varchar_value AS VARCHAR(4)) AS truncated_varchar,
       SYSTEM$TYPEOF(truncated_varchar) AS data_type
  FROM test_data_type_conversion;
```

```output
+---------------+-------------------+---------------+
| VARCHAR_VALUE | TRUNCATED_VARCHAR | DATA_TYPE     |
|---------------+-------------------+---------------|
| 9.8765        | 9.87              | VARCHAR(4)[8] |
+---------------+-------------------+---------------+
```

Convert a timestamp to a date:

```sqlexample
SELECT CAST(timestamp_value AS DATE) AS timestamp_to_date,
       SYSTEM$TYPEOF(timestamp_to_date) AS data_type
  FROM test_data_type_conversion;
```

```output
+-------------------+-----------+
| TIMESTAMP_TO_DATE | DATA_TYPE |
|-------------------+-----------|
| 2024-05-09        | DATE[SB4] |
+-------------------+-----------+
```
