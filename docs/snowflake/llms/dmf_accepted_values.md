# Source: https://docs.snowflake.com/en/sql-reference/functions/dmf_accepted_values.md

Categories:
:   [Data metric functions](../functions-data-metric.md)

# ACCEPTED_VALUES (system data metric function)

Returns the number of records where the value of a column does *not* match a Boolean expression.

## Syntax

```sqlsyntax
SNOWFLAKE.CORE.ACCEPTED_VALUES ON ( <column>, <lambda-expression> )
```

## Arguments

`column`
:   Specifies the column that contains values that are compared to the Boolean expression in `lambda-expression`.

`lambda-expression`
:   Specifies a lambda expression consisting of the following syntax: `column -> expression`.

    The function returns the number of records where the value of `column` doesn’t match the Boolean expression. This expression can
    use the following operations and functions:

    * [Comparison operators](../operators-comparison.md)
    * [Logical operators](../operators-logical.md)
    * [[ NOT ] LIKE](like.md)
    * [[ NOT ] IN](in.md)
    * [IS [ NOT ] NULL](is-null.md)

    The `column` in the lambda expression always matches the `column` argument.

## Allowed data types

The column specified in the `column` and `lambda-expression` arguments can contain any of the following data types:

* DATE
* FLOAT
* NUMBER
* TIMESTAMP_LTZ
* TIMESTAMP_NTZ
* TIMESTAMP_TZ
* VARCHAR

## Returns

The function returns a NUMBER value.

## Usage notes

* You can’t call this function directly. To learn how to associate the function with a table or view so it
  runs at regular intervals, see [Associate a DMF](../../user-guide/data-quality-working.md).

  You can use the [SYSTEM$DATA_METRIC_SCAN](system_data_metric_scan.md) function to run the ACCEPTED_VALUES function against a table without
  associating it.
* You cannot associate this function with the same column more than once.
* Renaming a column that is specified in the ACCEPTED_VALUES function breaks the association between the function and the column’s table or
  view. If you rename the column, you must re-associate the function with the table or view.

## Examples

Associate the function with table `t1` so it returns the number of records where the value of the column `age` is *not* equal to five.

```sqlexample
ALTER TABLE t1
  ADD DATA METRIC FUNCTION SNOWFLAKE.CORE.ACCEPTED_VALUES ON (age, age -> age = 5);
```

Associate the function with view `order_details` so it returns the number of records where the value of column `order_status` is *not*
in the list of strings `Pending`, `Dispatched`, and `Delivered`.

```sqlexample
ALTER VIEW order_details
  ADD DATA METRIC FUNCTION SNOWFLAKE.CORE.ACCEPTED_VALUES ON (
    order_status,
    order_status -> order_status IN ('Pending', 'Dispatched', 'Delivered'));
```
