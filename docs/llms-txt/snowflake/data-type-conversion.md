# Source: https://docs.snowflake.com/en/sql-reference/data-type-conversion.md

# Data type conversion

In many cases, a value of one data type can be converted to another data type. For example, an
[INTEGER](data-types-numeric.md) value can be converted to a
[floating-point data type](data-types-numeric.md) value. Converting a data type is called *casting*.

## Explicit casting vs implicit casting

Users can explicitly convert a value from one data type to another. This is called *explicit casting*.

In some situations, Snowflake converts a value to another data type automatically. This is called *implicit casting* or *coercion*.

### Explicit casting

Users can explicitly cast a value by using any of the following options:

* The [CAST](functions/cast.md) function.
* The `::` operator, called the *cast operator*.
* The appropriate SQL function; for example, [TO_DOUBLE](functions/to_double.md).

For example, each query casts a string value to a DATE value:

> ```sqlexample
> SELECT CAST('2022-04-01' AS DATE);
>
> SELECT '2022-04-01'::DATE;
>
> SELECT TO_DATE('2022-04-01');
> ```

Casting is allowed in most contexts in which a general expression is allowed, including the WHERE clause. For example:

> ```sqlexample
> SELECT date_column
>   FROM log_table
>   WHERE date_column >= '2022-04-01'::DATE;
> ```

### Implicit casting (coercion)

Coercion occurs when a function (or operator) requires a data type that is different from, but compatible with, the arguments
(or operands).

* Examples for functions or stored procedures:

  * The following code coerces the INTEGER value in column `my_integer_column` to FLOAT so that the value can
    be passed to the function `my_float_function()`, which expects a FLOAT:

    > ```sqlexample
    > SELECT my_float_function(my_integer_column)
    >   FROM my_table;
    > ```
>
* Examples for operators:

  * The following code coerces the INTEGER value `17` to VARCHAR so that the values can be concatenated by using
    the `||` operator:

    > ```sqlexample
    > SELECT 17 || '76';
    > ```

    The result of this SELECT statement is the string `'1776'`.
  * The following statement coerces the INTEGER value in column `my_integer_column` to FLOAT so that the value can be
    compared to the value `my_float_column` by using the `<` comparison operator:

    > ```sqlexample
    > SELECT ...
    >   FROM my_table
    >   WHERE my_integer_column < my_float_column;
    > ```

Not all contexts — for example, not all operators — support coercion.

## Casting and precedence

When casting inside an expression, the code must take into account the precedence of the cast operator relative to other
operators in the expression.

Consider the following example:

```sqlexample
SELECT height * width::VARCHAR || ' square meters'
  FROM dimensions;
```

The cast operator has higher precedence than the arithmetic operator `*` (multiply), so the statement is
interpreted as shown in the following example:

```sqlexample
... height * (width::VARCHAR) ...
```

To cast the result of the expression `height * width`, use parentheses, as shown in the following example:

```sqlexample
SELECT (height * width)::VARCHAR || ' square meters'
  FROM dimensions;
```

As another example, consider the following statement:

```sqlexample
SELECT -0.0::FLOAT::BOOLEAN;
```

You might expect this to be interpreted as shown in the following example:

```sqlexample
SELECT (-0.0::FLOAT)::BOOLEAN;
```

Therefore, it would be expected to return FALSE (0 = FALSE, 1 = TRUE).

However, the cast operator has higher precedence than the unary minus (negation) operator, so the
statement is interpreted as shown in the following example:

```sqlexample
SELECT -(0.0::FLOAT::BOOLEAN);
```

Therefore, the query results in an error message because the unary minus can’t be applied to a BOOLEAN.

## Data types that can be cast

The following table shows the valid data type conversions in Snowflake. The table also shows which coercions Snowflake
can perform automatically.

> **Note:**
>
> Internally, the [CAST](functions/cast.md) function and the `::` operator call the appropriate conversion
> function. For example, if you cast a NUMBER to a BOOLEAN, Snowflake calls the [TO_BOOLEAN](functions/to_boolean.md)
> function. The usage notes for each conversion function apply when the function is called indirectly by using a cast, and also when
> the function is called directly. For example, if you execute `CAST(my_decimal_column AS BOOLEAN)`, the rules for calling
> TO_BOOLEAN with a DECIMAL value apply. For convenience, the table includes links to the relevant conversion functions.

For more information about conversions between [semi-structured types](data-types-semistructured.md) and
[structured types](data-types-structured.md), see [Converting structured and semi-structured types](data-types-structured.md).

| Source data type | Target data type | Castable | Coercible | Conversion function | Notes |
| --- | --- | --- | --- | --- | --- |
| ARRAY |  |  |  |  |  |
|  | [VARCHAR](data-types-text.md) | ✔ | ❌ | [TO_VARCHAR](functions/to_char.md) | None. |
|  | [VARIANT](data-types-semistructured.md) | ✔ | ✔ | [TO_VARIANT](functions/to_variant.md) | None. |
|  | [VECTOR](data-types-vector.md) | ✔ | ✔ |  | Use explicit casting for conversion. For more information, see [Vector conversion](data-types-vector.md). |
| BINARY |  |  |  |  |  |
|  | [VARCHAR](data-types-text.md) | ✔ | ❌ | [TO_VARCHAR](functions/to_char.md) | None. |
|  | [VARIANT](data-types-semistructured.md) | ✔ | ❌ | [TO_VARIANT](functions/to_variant.md) | None. |
| BOOLEAN |  |  |  |  |  |
|  | [DECFLOAT](data-types-numeric.md) | ✔ | ✔ | [TO_DECFLOAT](functions/to_decfloat.md) | For example, from `FALSE` to `0`. |
|  | [NUMBER](data-types-numeric.md) | ✔ | ❌ | [TO_NUMBER](functions/to_decimal.md) | None. |
|  | [VARCHAR](data-types-text.md) | ✔ | ✔ | [TO_VARCHAR](functions/to_char.md) | For example, from `TRUE` to `'true'`. |
|  | [VARIANT](data-types-semistructured.md) | ✔ | ✔ | [TO_VARIANT](functions/to_variant.md) | None. |
| DATE |  |  |  |  |  |
|  | [TIMESTAMP](data-types-datetime.md) | ✔ | ✔ | [TO_TIMESTAMP](functions/to_timestamp.md) | None. |
|  | [VARCHAR](data-types-text.md) | ✔ | ✔ | [TO_VARCHAR](functions/to_char.md) | None. |
|  | [VARIANT](data-types-semistructured.md) | ✔ | ❌ | [TO_VARIANT](functions/to_variant.md) | None. |
| DECFLOAT . *(decimal floating-point numbers)* |  |  |  |  |  |
|  | [BOOLEAN](data-types-logical.md) | ✔ | ✔ | [TO_BOOLEAN](functions/to_boolean.md) | For example, from `0` to `FALSE`. |
|  | [FLOAT](data-types-numeric.md) | ✔ | ✔ | [TO_DOUBLE](functions/to_double.md) | None. |
|  | [NUMBER[(p,s)]](data-types-numeric.md) | ✔ | ✔ | [TO_NUMBER](functions/to_decimal.md) | None. |
|  | [VARCHAR](data-types-text.md) | ✔ | ✔ | [TO_VARCHAR](functions/to_char.md) | None. |
| FLOAT . *(floating-point numbers)* |  |  |  |  |  |
|  | [BOOLEAN](data-types-logical.md) | ✔ | ✔ | [TO_BOOLEAN](functions/to_boolean.md) | For example, from `0.0` to `FALSE`. |
|  | [DECFLOAT](data-types-numeric.md) | ✔ | ✔ | [TO_DECFLOAT](functions/to_decfloat.md) | None. |
|  | [NUMBER[(p,s)]](data-types-numeric.md) | ✔ | ✔ | [TO_NUMBER](functions/to_decimal.md) | None. |
|  | [VARCHAR](data-types-text.md) | ✔ | ✔ | [TO_VARCHAR](functions/to_char.md) | None. |
|  | [VARIANT](data-types-semistructured.md) | ✔ | ✔ | [TO_VARIANT](functions/to_variant.md) | None. |
| GEOGRAPHY |  |  |  |  |  |
|  | [VARIANT](data-types-semistructured.md) | ✔ | ❌ | [TO_VARIANT](functions/to_variant.md) | None. |
| GEOMETRY |  |  |  |  |  |
|  | [VARIANT](data-types-semistructured.md) | ✔ | ❌ | [TO_VARIANT](functions/to_variant.md) | None. |
| NUMBER[(p,s)] . *(Fixed-point numbers, including INTEGER)* |  |  |  |  |  |
|  | [BOOLEAN](data-types-logical.md) | ✔ | ✔ | [TO_BOOLEAN](functions/to_boolean.md) | For example, from `0` to `FALSE`. |
|  | [DECFLOAT](data-types-numeric.md) | ✔ | ✔ | [TO_DECFLOAT](functions/to_decfloat.md) | None. |
|  | [FLOAT](data-types-numeric.md) | ✔ | ✔ | [TO_DOUBLE](functions/to_double.md) | None. |
|  | [TIMESTAMP](data-types-datetime.md) | ✔ | ✔ | [TO_TIMESTAMP](functions/to_timestamp.md) | [1] |
|  | [VARCHAR](data-types-text.md) | ✔ | ✔ | [TO_VARCHAR](functions/to_char.md) | None. |
|  | [VARIANT](data-types-semistructured.md) | ✔ | ✔ | [TO_VARIANT](functions/to_variant.md) | None. |
| OBJECT |  |  |  |  |  |
|  | [ARRAY](data-types-semistructured.md) | ✔ | ❌ | [TO_ARRAY](functions/to_array.md) | None. |
|  | [VARCHAR](data-types-text.md) | ✔ | ❌ | [TO_VARCHAR](functions/to_char.md) | None. |
|  | [VARIANT](data-types-semistructured.md) | ✔ | ✔ | [TO_VARIANT](functions/to_variant.md) | None. |
| TIME |  |  |  |  |  |
|  | [VARCHAR](data-types-text.md) | ✔ | ✔ | [TO_VARCHAR](functions/to_char.md) | None. |
|  | [VARIANT](data-types-semistructured.md) | ✔ | ❌ | [TO_VARIANT](functions/to_variant.md) | None. |
| TIMESTAMP |  |  |  |  |  |
|  | [DATE](data-types-datetime.md) | ✔ | ✔ | [TO_DATE , DATE](functions/to_date.md) | None. |
|  | [TIME](data-types-datetime.md) | ✔ | ✔ | [TO_TIME , TIME](functions/to_time.md) | None. |
|  | [VARCHAR](data-types-text.md) | ✔ | ✔ | [TO_VARCHAR](functions/to_char.md) | None. |
|  | [VARIANT](data-types-semistructured.md) | ✔ | ❌ | [TO_VARIANT](functions/to_variant.md) | None. |
| VARCHAR |  |  |  |  |  |
|  | [BOOLEAN](data-types-logical.md) | ✔ | ✔ | [TO_BOOLEAN](functions/to_boolean.md) | For example, from `'false'` to `FALSE`. |
|  | [DATE](data-types-datetime.md) | ✔ | ✔ | [TO_DATE , DATE](functions/to_date.md) | None. |
|  | [DECFLOAT](data-types-numeric.md) | ✔ | ✔ | [TO_DECFLOAT](functions/to_decfloat.md) | None. |
|  | [FLOAT](data-types-numeric.md) | ✔ | ✔ | [TO_DOUBLE](functions/to_double.md) | For example, from `'12.34'` to `12.34`. |
|  | [NUMBER[(p,s)]](data-types-numeric.md) | ✔ | ✔ | [TO_NUMBER](functions/to_decimal.md) | For example, from `'12.34'` to `12.34`. |
|  | [TIME](data-types-datetime.md) | ✔ | ✔ | [TO_TIME , TIME](functions/to_time.md) | None. |
|  | [TIMESTAMP](data-types-datetime.md) | ✔ | ✔ | [TO_TIMESTAMP](functions/to_timestamp.md) | None. |
|  | [UUID](data-types-uuid.md) | ✔ | ✔ | [TO_UUID](functions/to_uuid.md) | None. |
|  | [VARIANT](data-types-semistructured.md) | ✔ | ❌ | [TO_VARIANT](functions/to_variant.md) | None. |
| UUID |  |  |  |  |  |
|  | [VARCHAR](data-types-text.md) | ✔ | ✔ | [TO_VARCHAR](functions/to_char.md) | None. |
| VARIANT |  |  |  |  |  |
|  | [ARRAY](data-types-semistructured.md) | ✔ | ✔ | [TO_ARRAY](functions/to_array.md) | None. |
|  | [BOOLEAN](data-types-logical.md) | ✔ | ✔ | [TO_BOOLEAN](functions/to_boolean.md) | For example, from a VARIANT containing `'false'` to `FALSE`. |
|  | [DATE](data-types-datetime.md) | ✔ | ✔ | [TO_DATE , DATE](functions/to_date.md) | None. |
|  | [FLOAT](data-types-numeric.md) | ✔ | ✔ | [TO_DOUBLE](functions/to_double.md) | None. |
|  | [GEOGRAPHY](data-types-geospatial.md) | ✔ | ❌ | [TO_GEOGRAPHY](functions/to_geography.md) | None. |
|  | [NUMBER[(p,s)]](data-types-numeric.md) | ✔ | ✔ | [TO_NUMBER](functions/to_decimal.md) | None. |
|  | [OBJECT](data-types-semistructured.md) | ✔ | ✔ | [TO_OBJECT](functions/to_object.md) | None. |
|  | [TIME](data-types-datetime.md) | ✔ | ✔ | [TO_TIME , TIME](functions/to_time.md) | None. |
|  | [TIMESTAMP](data-types-datetime.md) | ✔ | ✔ | [TO_TIMESTAMP](functions/to_timestamp.md) | None. |
|  | [VARCHAR](data-types-text.md) | ✔ | ✔ | [TO_VARCHAR](functions/to_char.md) | None. |
|  | [VECTOR](data-types-vector.md) | ✔ | ❌ |  | The VARIANT must contain an ARRAY of type FLOAT or INT. |
| VECTOR |  |  |  |  |  |
|  | [ARRAY](data-types-semistructured.md) | ✔ | ✔ | [TO_ARRAY](functions/to_array.md) | None. |

[1]

NUMBER can be converted to TIMESTAMP because the values are treated as seconds since the beginning of the epoch (1970-01-01 00:00:00).

> **Note:**
>
> For each listed data type — for example, FLOAT — the rules apply to all aliases for that data type. For example, the rules for FLOAT apply to
> DOUBLE, which is an alias for FLOAT.

## Usage notes

Except where stated otherwise, the following rules apply to both explicit casting and implicit casting:

* Conversion depends not only on the data type, but also the value, of the source; for example:

  * The VARCHAR value `'123'` can be converted to a numeric value, but the VARCHAR value `'xyz'` can’t be converted to
    a numeric value.
  * The ability to cast a specific value of type VARIANT depends on the type of the data *inside* the VARIANT. For
    example, if the VARIANT contains a value of type TIME, then you can’t cast the VARIANT value to a TIMESTAMP value,
    because you can’t cast a TIME value to a TIMESTAMP value.
* Snowflake performs implicit conversion of arguments to make
  them compatible. For example, if one of the input expressions is a numeric type, the return type
  is also a numeric type. That is, `SELECT COALESCE('17', 1);` first converts the VARCHAR value `'17'`
  to the NUMBER value `17`, and then returns the first non-NULL value.

  When conversion isn’t possible, implicit conversion fails. For example, `SELECT COALESCE('foo', 1);`
  returns an error because the VARCHAR value `'foo'` can’t be converted to a NUMBER value.

  We recommend passing in arguments of the same type or explicitly converting arguments if needed.

* When implicit conversion converts a non-numeric value to a numeric value, the result is a value
  of type NUMBER(18,5).

  For numeric string arguments that aren’t constants, if NUMBER(18,5) isn’t sufficient to represent
  the numeric value, then cast the argument to a type that
  can represent the value.

* For some pairs of data types, conversion can result in loss of precision; for example:

  * Converting a FLOAT value to an INTEGER value rounds the value.
  * Converting a value from fixed-point numeric — for example, NUMBER(38, 0) — to floating point — for example, FLOAT — can result
    in rounding or truncation if the fixed-point number can’t be precisely represented in a floating point number.
  * Converting a TIMESTAMP value to a DATE value removes the information about the time of day.
* Although Snowflake converts values in some situations where loss of precision can occur, Snowflake doesn’t allow conversion in
  other situations where a loss of precision would occur. For example, Snowflake doesn’t allow conversion when conversion would cause the
  following situations to happen:

  * Truncate a VARCHAR value. For example, Snowflake doesn’t cast VARCHAR(10) to VARCHAR(5), either implicitly or explicitly.
  * Result in the loss of digits other than the least significant digits. For example, the following loss of digits fails:

    ```sqlexample
    SELECT 12.3::FLOAT::NUMBER(3,2);
    ```

    In this example, the number `12.3` has two digits before the decimal point, but the data type `NUMBER(3,2)` has room for
    only one digit before the decimal point.
* When converting from a type with less precision to a type with more precision, conversion uses default values. For example,
  converting a DATE value to a TIMESTAMP_NTZ value causes the hour, minute, second, and fractional seconds to be set to `0`.
* When a FLOAT value is cast to a VARCHAR value, trailing zeros are omitted.

  For example, the following statements create a table and insert a row that contains a VARCHAR value, a FLOAT value, and
  a VARIANT value. The VARIANT value is constructed from JSON that contains a floating-point value represented with trailing zeros:

  ```sqlexample
  CREATE OR REPLACE TABLE convert_test_zeros (
    varchar1 VARCHAR,
    float1 FLOAT,
    variant1 VARIANT);

  INSERT INTO convert_test_zeros SELECT
    '5.000',
    5.000,
    PARSE_JSON('{"Loan Number": 5.000}');
  ```

  The following SELECT statement explicitly casts both the FLOAT column and the FLOAT value inside the VARIANT column to VARCHAR.
  In each case, the VARCHAR contains no trailing zeros:

  ```sqlexample
  SELECT varchar1,
         float1::VARCHAR,
         variant1:"Loan Number"::VARCHAR
    FROM convert_test_zeros;
  ```

  ```output
  +----------+-----------------+---------------------------------+
  | VARCHAR1 | FLOAT1::VARCHAR | VARIANT1:"LOAN NUMBER"::VARCHAR |
  |----------+-----------------+---------------------------------|
  | 5.000    | 5               | 5                               |
  +----------+-----------------+---------------------------------+
  ```

* Some operations can return different data types, depending on a conditional expression. For example, the following
  [IFNULL](functions/ifnull.md) calls return slightly different data types depending on the input values:

  ```sqlexample
  SELECT SYSTEM$TYPEOF(IFNULL(12.3, 0)),
         SYSTEM$TYPEOF(IFNULL(NULL, 0));
  ```

  ```output
  +--------------------------------+--------------------------------+
  | SYSTEM$TYPEOF(IFNULL(12.3, 0)) | SYSTEM$TYPEOF(IFNULL(NULL, 0)) |
  |--------------------------------+--------------------------------|
  | NUMBER(3,1)[SB1]               | NUMBER(1,0)[SB1]               |
  +--------------------------------+--------------------------------+
  ```

  If the expression has more than one possible data type, Snowflake chooses the data type based on the actual result.
  For more information about precision and scale in calculations, see [Scale and precision in arithmetic operations](operators-arithmetic.md).
  If the query generates more than one result — for example, multiple rows of results — Snowflake chooses a data type that
  is capable of holding each of the individual results.
* Some applications, such as SnowSQL, and some graphical user interfaces, such as Snowsight, apply their
  own conversion and formatting rules when they display data. For example, SnowSQL displays BINARY values as a string that contains
  only hexadecimal digits; that string is generated by implicitly calling a conversion function. Therefore, the data that SnowSQL
  displays might not unambiguously indicate which data conversions that Snowflake coerced.
