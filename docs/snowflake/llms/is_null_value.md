# Source: https://docs.snowflake.com/en/sql-reference/functions/is_null_value.md

Categories:
:   [Conditional expression functions](../expressions-conditional.md) , [Semi-structured and structured data functions](../functions-semistructured.md) (Type Predicates)

# IS_NULL_VALUE

Returns TRUE if its [VARIANT](../data-types-semistructured.md) argument is a [JSON null](../../user-guide/semistructured-considerations.md) value.

> **Important:**
>
> The JSON null value is distinct from the SQL NULL value.
>
> This function returns TRUE only for JSON null values, not SQL NULL values.
> The difference is shown in the first and third rows in
> the output for the example below.
>
> A missing JSON value is converted to a SQL NULL value, for which
> IS_NULL_VALUE returns NULL. The 4th column in
> the output for the example below
> shows this.

This function is different from the [IS [ NOT ] NULL](is-null.md) function.

See also:
:   [IS_<object_type>](is.md)

## Syntax

```sqlsyntax
IS_NULL_VALUE( <variant_expr> )
```

## Arguments

`variant_expr`
:   An expression that evaluates to a value of type VARIANT.

## Returns

This function returns a value of type BOOLEAN or NULL:

* Returns TRUE for a JSON null value.
* Returns FALSE for a non-null JSON value.
* Returns NULL for a SQL NULL value.

## Examples

This example uses the IS_NULL_VALUE function. First, create a table with a VARIANT column:

```sqlexample
CREATE OR REPLACE TABLE test_is_null_value_function (
  variant_value VARIANT);
```

Insert a string value into the column using the [PARSE_JSON](parse_json.md) function:

```sqlexample
INSERT INTO test_is_null_value_function (variant_value)
  (SELECT PARSE_JSON('"string value"'));
```

> **Note:**
>
> The PARSE_JSON function returns a VARIANT value.

Insert a JSON null value into the column:

```sqlexample
INSERT INTO test_is_null_value_function (variant_value)
  (SELECT PARSE_JSON('null'));
```

Insert an empty object into the column:

```sqlexample
INSERT INTO test_is_null_value_function (variant_value)
  (SELECT PARSE_JSON('{}'));
```

Insert two rows with JSON name/value pairs into the VARIANT column :

```sqlexample
INSERT INTO test_is_null_value_function (variant_value)
  (SELECT PARSE_JSON('{"x": null}'));

INSERT INTO test_is_null_value_function (variant_value)
  (SELECT PARSE_JSON('{"x": "foo"}'));
```

Insert a NULL into the column:

```sqlexample
INSERT INTO test_is_null_value_function (variant_value)
  (SELECT PARSE_JSON(NULL));
```

Query the table:

```sqlexample
SELECT variant_value,
       variant_value:x value_of_x,
       IS_NULL_VALUE(variant_value) is_variant_value_a_json_null,
       IS_NULL_VALUE(variant_value:x) is_x_a_json_null,
       IS_NULL_VALUE(variant_value:y) is_y_a_json_null
  FROM test_is_null_value_function;
```

```output
+----------------+------------+------------------------------+------------------+------------------+
| VARIANT_VALUE  | VALUE_OF_X | IS_VARIANT_VALUE_A_JSON_NULL | IS_X_A_JSON_NULL | IS_Y_A_JSON_NULL |
|----------------+------------+------------------------------+------------------+------------------|
| "string value" | NULL       | False                        | NULL             | NULL             |
| null           | NULL       | True                         | NULL             | NULL             |
| {}             | NULL       | False                        | NULL             | NULL             |
| {              | null       | False                        | True             | NULL             |
|   "x": null    |            |                              |                  |                  |
| }              |            |                              |                  |                  |
| {              | "foo"      | False                        | False            | NULL             |
|   "x": "foo"   |            |                              |                  |                  |
| }              |            |                              |                  |                  |
| NULL           | NULL       | NULL                         | NULL             | NULL             |
+----------------+------------+------------------------------+------------------+------------------+
```

In the query results:

* The `variant_value` column shows six rows of inserted VARIANT values.
* The `value_of_x` column shows the JSON value for the name `x` in each row.
* The `is_variant_value_a_json_null` column returns the results of the IS_NULL_VALUE function
  for the VARIANT value in each row.
* The `is_x_a_json_null` column returns the results of the IS_NULL_VALUE function
  for the name `x` in each row. Rows without an `x` name return NULL.
* The `is_y_a_json_null` column returns the results of the IS_NULL_VALUE function
  for the name `y` in each row. Because there is no matching `y` name in any
  row, all of the rows return NULL.
