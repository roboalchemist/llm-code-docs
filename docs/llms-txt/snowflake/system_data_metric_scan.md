# Source: https://docs.snowflake.com/en/sql-reference/functions/system_data_metric_scan.md

Categories:
:   [System functions](../functions-system.md), [Table functions](../functions-table.md)

# SYSTEM$DATA_METRIC_SCAN

Returns the rows identified by a [data quality metric](../../user-guide/data-quality-intro.md) as containing data that fails a data quality
check. For example, if you use the NULL_COUNT data metric function as an argument, the function returns the rows in the table that contain a
NULL value in a specific column.

## Syntax

```sqlsyntax
SYSTEM$DATA_METRIC_SCAN(
  REF_ENTITY_NAME  => '<object>'
  , METRIC_NAME  => '<data_metric_function>'
  , ARGUMENT_NAME => '<column> [ , <column> ... ]'
  [ , ARGUMENT_EXPRESSION => '<boolean-expression>' ]
  [ , AT_TIMESTAMP => '<timestamp>' ] )
```

## Arguments

**Required:**

`REF_ENTITY_NAME => 'object'`
:   Name of the table or view on which the specified data metric function will run. The function returns rows from this object.

`METRIC_NAME => 'data_metric_function'`
:   Name of the system data metric that you want to run to evaluate the specified table or view. Only the following system functions are
    supported:

    > * SNOWFLAKE.CORE.ACCEPTED_VALUES
    > * SNOWFLAKE.CORE.BLANK_COUNT
    > * SNOWFLAKE.CORE.BLANK_PERCENT
    > * SNOWFLAKE.CORE.DUPLICATE_COUNT
    > * SNOWFLAKE.CORE.NULL_COUNT
    > * SNOWFLAKE.CORE.NULL_PERCENT

`ARGUMENT_NAME => 'column [ , column ... ]'`
:   Name of the columns in the specified table or view that are being passed as arguments to the specified data metric function.

**Optional:**

`ARGUMENT_EXPRESSION => 'boolean-expression'`
:   Required if the specified data metric function is [ACCEPTED_VALUES](dmf_accepted_values.md). Disallowed for all other DMFs.

    Specifies a Boolean expression used to evaluate whether a record passes or fails the ACCEPTED_VALUES data quality check. The
    SYSTEM$DATA_METRIC_SCAN function returns records that do *not* match the Boolean expression. The expression can include the following
    operators and functions:

    * [Comparison operators](../operators-comparison.md)
    * [Logical operators](../operators-logical.md)
    * [[ NOT ] LIKE](like.md)
    * [[ NOT ] IN](in.md)
    * [IS [ NOT ] NULL](is-null.md)

    The column in the Boolean expression must be the same column specified in the ARGUMENT_NAME argument.

    If the ACCEPTED_VALUES DMF is [associated with the object](../../user-guide/data-quality-working.md) specified by REF_ENTITY_NAME, the
    SYSTEM$DATA_METRIC_SCAN function ignores the Boolean expression that was specified when ACCEPTED_VALUES was associated with the
    object.

`AT_TIMESTAMP => 'timestamp'`
:   Timestamp that is being passed as an argument to check the results of a DMF evaluation on the table or view in the past.

## Returns

Rows from the specified table or view.

## Access control privileges

Executing this function requires the following privileges:

* SELECT on the specified table.
* USAGE on the specified data metric function.

## Usage notes

* This function does not support user-defined metrics.
* If the specified table is protected by a policy, such as a masking policy or row access policy, the function might return unexpected or
  incomplete data because results depend on the user’s role when executing the function.

## Examples

Given that the SNOWFLAKE.CORE.NULL_COUNT system metric returns the total number of NULL values in a particular column, the following returns
the rows of the `employeesTable` table that have NULL values in the `SSN` column.

```sqlexample
SELECT *
  FROM TABLE(SYSTEM$DATA_METRIC_SCAN(
    REF_ENTITY_NAME  => 'governance.sch.employeesTable',
    METRIC_NAME  => 'snowflake.core.null_count',
    ARGUMENT_NAME => 'SSN'
  ));
```

Given that the SNOWFLAKE.CORE.DUPLICATE_COUNT system metric returns the count of duplicate values, the following returns
the rows of the `employeesTable` table that had duplicate values in both the `first_name` and `last_name` columns.

```sqlexample
SELECT *
  FROM TABLE(SYSTEM$DATA_METRIC_SCAN(
    REF_ENTITY_NAME  => 'governance.sch.employeesTable',
    METRIC_NAME  => 'snowflake.core.duplicate_count',
    ARGUMENT_NAME => 'first_name, last_name'
  ));
```

Return the rows where the value of the `age` column is *not* equal to five (that is, the rows that *don’t* match the condition specified by
ARGUMENT_EXPRESSION).

```sqlexample
SELECT *
  FROM TABLE(SYSTEM$DATA_METRIC_SCAN(
    REF_ENTITY_NAME  => 'governance.sch.employeesTable',
    METRIC_NAME  => 'snowflake.core.accepted_values',
    ARGUMENT_NAME => 'age',
    ARGUMENT_EXPRESSION => 'age = 5'
  ));
```
