# Source: https://docs.snowflake.com/en/sql-reference/sql/drop-function-dmf.md

# DROP FUNCTION (DMF)

Removes the specified data metric function (DMF) from the current or specified schema.

## Syntax

```sqlsyntax
DROP FUNCTION [ IF EXISTS ] <name>(
TABLE(  <arg_data_type> [ , ... ] ) [ , TABLE( <arg_data_type> [ , ... ] ) ]
)
```

## Parameters

`name`
:   Identifier for the DMF to drop.

    If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes.
    Identifiers enclosed in double quotes are also case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

`TABLE( arg_data_type [ , ... ] ) [ , TABLE( arg_data_type [ , ... ] ) ]`
:   Specifies the data type of the column arguments for the DMF. The data types are necessary because DMFs support name overloading
    (that is, two DMFs in the same schema can have the same name), and the data types of the arguments are used to identify the DMF you want to
    drop.

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| OWNERSHIP | Data metric function |  |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* When the IF EXISTS clause is specified and the target object doesn’t exist, the command completes successfully
  without returning an error.

## Example

Drop a custom DMF from the system:

```sqlexample
DROP FUNCTION governance.dmfs.count_positive_numbers(
  TABLE(
    NUMBER, NUMBER, NUMBER
  )
);
```
