# Source: https://docs.snowflake.com/en/sql-reference/sql/create-data-metric-function.md

# CREATE DATA METRIC FUNCTION

Creates a new data metric function (DMF) in the current or specified schema, or replaces an existing data metric function.

After creating a DMF, apply it to a table column using an
[ALTER TABLE … ALTER COLUMN](alter-table-column.md) command or a view column using the [ALTER VIEW](alter-view.md) command.

This command supports the following variants:

* CREATE OR ALTER DATA METRIC FUNCTION: Creates a new data metric function if it doesn’t exist or alters an existing data metric function.

## Syntax

```sqlsyntax
CREATE [ OR REPLACE ] [ SECURE ] DATA METRIC FUNCTION [ IF NOT EXISTS ] <name>
  ( <table_arg> TABLE( <col_arg> <data_type> [ , ... ] )
    [ , <table_arg> TABLE( <col_arg> <data_type> [ , ... ] ) ] )
  RETURNS NUMBER [ [ NOT ] NULL ]
  [ LANGUAGE SQL ]
  [ COMMENT = '<string_literal>' ]
  AS
  '<expression>'
```

## Variant syntax

### CREATE OR ALTER DATA METRIC FUNCTION

Creates a new data metric function if it doesn’t already exist, or transforms an existing data metric function into
the function defined in the statement. A CREATE OR ALTER DATA METRIC FUNCTION statement follows the syntax rules of
a CREATE DATA METRIC FUNCTION statement and has the same limitations as an [ALTER FUNCTION (DMF)](alter-function-dmf.md)
statement.

Unlike a CREATE OR REPLACE DATA METRIC FUNCTION command, a CREATE OR ALTER command updates the object without
deleting and recreating it.

Supported function alterations include changes to the COMMENT property.

For more information, see CREATE OR ALTER DATA METRIC FUNCTION usage notes.

```sqlsyntax
CREATE [ OR ALTER ] DATA METRIC FUNCTION ...
```

## Required parameters

`name`
:   Identifier for the DMF; must be unique for your schema.

    In addition, the identifier must start with an alphabetic character and cannot contain spaces or special characters unless the
    entire identifier string is enclosed in double quotes (for example, `"My object"`). Identifiers enclosed in double quotes are also
    case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

`( table_arg TABLE( col_arg data_type [ , ... ] ) [ , table_arg TABLE( col_arg data_type [ , ... ] ) ] )`
:   The signature for the DMF, which is used as input for the expression.

    You must specify:

    * An argument name for each table (`table_arg`).
    * For each table, an argument name for at least one column, along with its data type (`col_arg data_type`).

      You can optionally specify arguments for additional columns and their data types. The columns must be in the same table and cannot
      reference a different table.

`RETURNS NUMBER`
:   The data type of the output of the function.

    The data type can only be NUMBER.

`AS expression`
:   SQL expression that determines the output of the function. The expression must be deterministic and return a scalar value. The expression
    can reference other table objects, such as by using a [WITH](../constructs/with.md) clause or a
    [WHERE](../constructs/where.md) clause.

    The delimiters around the `expression` can be either single quotes or a pair of dollar signs. Using `$$` as the delimiter makes
    it easier to write expressions that contain single quotes.

    If the delimiter for the `expression` is the single quote character, then any single quotes within `expression`
    (for example, string literals) must be escaped by single quotes.

    The `expression` does not support the following:

    * Using nondeterministic functions (for example, [CURRENT_TIME](../functions/current_time.md)).
    * Referencing an object that depends on a UDF or UDTF.
    * Returning a nonscalar output.

## Optional parameters

`SECURE`
:   Specifies that the data metric function is secure. For more information, see [Protecting Sensitive Information with Secure UDFs and Stored Procedures](../../developer-guide/secure-udf-procedure.md).

`LANGUAGE SQL`
:   Specifies the language used to write the expression.

    SQL is the only supported language.

`COMMENT = 'string_literal'`
:   A comment for the DMF.

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| CREATE DATA METRIC FUNCTION | Schema | The privilege only enables the creation of data metric functions in the schema.  If you want to enable the creation of user-defined functions, such as SQL or Java UDFs, the role must have the CREATE FUNCTION privilege. |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## General usage notes

* If you want to update an existing data metric function and need to see the current definition of the function, run the
  [DESCRIBE FUNCTION (DMF)](desc-function-dmf.md) command or call the [GET_DDL](../functions/get_ddl.md) function.
* Regarding metadata:

  > **Attention:**
  >
  > Customers should ensure that no personal data (other than for a User object), sensitive data, export-controlled data, or other regulated data is entered as metadata when using the Snowflake service. For more information, see [Metadata fields in Snowflake](../metadata.md).

* The OR REPLACE and IF NOT EXISTS clauses are mutually exclusive. They can’t both be used in the same statement.
* CREATE OR REPLACE *<object>* statements are atomic. That is, when an object is replaced, the old object is deleted and the new object is created in a single transaction.

## CREATE OR ALTER DATA METRIC FUNCTION usage notes

You can’t modify the DMF’s arguments. Specifying new arguments creates a new overloaded DMF.

## Example: Single table argument

Create a DMF that calls the [COUNT](../functions/count.md) function to return the total number of rows that
have positive numbers in three columns of the table:

```sqlexample
CREATE OR REPLACE DATA METRIC FUNCTION governance.dmfs.count_positive_numbers(
  arg_t TABLE(
    arg_c1 NUMBER,
    arg_c2 NUMBER,
    arg_c3 NUMBER
  )
)
RETURNS NUMBER
AS
$$
  SELECT
    COUNT(*)
  FROM arg_t
  WHERE
    arg_c1>0
    AND arg_c2>0
    AND arg_c3>0
$$;
```

## Example: Multiple table arguments

Returns the number of records where the value of a column in one table does not have a corresponding value in the column of another table:

```sqlexample
CREATE OR REPLACE DATA METRIC FUNCTION governance.dmfs.referential_check(
  arg_t1 TABLE (arg_c1 INT), arg_t2 TABLE (arg_c2 INT))
RETURNS NUMBER
AS
$$
  SELECT
    COUNT(*)
    FROM arg_t1
  WHERE
    arg_c1 NOT IN (SELECT arg_c2 FROM arg_t2)
$$;
```

For an example that uses this DMF to validate referential integrity, see [Example: Using multiple table arguments to perform referential checks](../../user-guide/data-quality-custom-dmfs.md).

## Example: Alter a data metric function using the CREATE OR ALTER DATA METRIC FUNCTION command

Alters the single-table data metric function created in the example above to set security and comment.

```sqlexample
CREATE OR ALTER SECURE DATA METRIC FUNCTION governance.dmfs.count_positive_numbers(
  arg_t TABLE(
    arg_c1 NUMBER,
    arg_c2 NUMBER,
    arg_c3 NUMBER
  )
)
RETURNS NUMBER
COMMENT = "count positive numbers"
AS
$$
  SELECT
    COUNT(*)
  FROM arg_t
  WHERE
    arg_c1>0
    AND arg_c2>0
    AND arg_c3>0
$$;
```
