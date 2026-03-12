# Source: https://docs.snowflake.com/en/sql-reference/sql/desc-function-dmf.md

# DESCRIBE FUNCTION (DMF)

Describes the specified data metric function (DMF), including the signature (arguments), return value, language, and body (definition).

## Syntax

```sqlsyntax
{ DESC | DESCRIBE } FUNCTION [ IF EXISTS ] <name>(
  TABLE(  <arg_data_type> [ , ... ] ) [ , TABLE( <arg_data_type> [ , ... ] ) ]
  )
```

## Parameters

`name`
:   Specifies the identifier for the function to describe.

    If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes.
    Identifiers enclosed in double quotes are also case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

`TABLE( arg_data_type [ , ... ] ) [ , TABLE( arg_data_type [ , ... ] ) ]`
:   Specifies the data type of the column arguments for the DMF. The data types are necessary because DMFs support name overloading
    (that is, two DMFs in the same schema can have the same name), and the data types of the argument are used to identify the DMF you want to
    describe.

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| USAGE | Data metric function |  |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* To post-process the output of this command, you can use the [pipe operator](../operators-flow.md)
  (`->>`) or the [RESULT_SCAN](../functions/result_scan.md) function. Both constructs treat the output as a
  result set that you can query.

  For example, you can use the pipe operator or RESULT_SCAN function to select specific columns from the SHOW
  command output or filter the rows.

  When you refer to the output columns, use [double-quoted identifiers](../identifiers-syntax.md) for
  the column names. For example, to select the output column `type`, specify `SELECT "type"`.

  You must use double-quoted identifiers because the output column names for SHOW commands are in lowercase.
  The double quotes ensure that the column names in the SELECT list or WHERE clause match the column names
  in the SHOW command output that was scanned.

## Example

Describe the DMF to view its properties:

```sqlexample
DESC FUNCTION governance.dmfs.count_positive_numbers(
  TABLE(
    NUMBER, NUMBER, NUMBER
  )
);
```

```output
+-----------+---------------------------------------------------------------------+
| property  | value                                                               |
+-----------+---------------------------------------------------------------------+
| signature | (ARG_T TABLE(ARG_C1 NUMBER, ARG_C2 NUMBER, ARG_C3 NUMBER))          |
| returns   | NUMBER(38,0)                                                        |
| language  | SQL                                                                 |
| body      | SELECT COUNT(*) FROM arg_t WHERE arg_c1>0 AND arg_c2>0 AND arg_c3>0 |
+-----------+---------------------------------------------------------------------+
```
