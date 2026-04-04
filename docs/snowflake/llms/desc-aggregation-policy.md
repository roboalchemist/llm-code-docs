# Source: https://docs.snowflake.com/en/sql-reference/sql/desc-aggregation-policy.md

# DESCRIBE AGGREGATION POLICY

Describes the details about an [aggregation policy](../../user-guide/aggregation-policies.md), including the creation date, name, and the
SQL expression.

DESCRIBE can be abbreviated to DESC.

See also:
:   [Aggregation policy DDL reference](../../user-guide/aggregation-policies.md)

## Syntax

```sqlsyntax
DESC[RIBE] AGGREGATION POLICY <name>
```

## Parameters

`name`
:   Specifies the identifier for the aggregation policy to describe.

    If the identifier contains spaces or special characters, the entire string must be enclosed in double quotes.
    Identifiers enclosed in double quotes are also case-sensitive.

    For more information, see [Identifier requirements](../identifiers-syntax.md).

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this SQL command must have at least one of the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| APPLY AGGREGATION POLICY | Account |  |
| APPLY | Aggregation policy |  |
| OWNERSHIP | Aggregation policy | OWNERSHIP is a special privilege on an object that is automatically granted to the role that created the object, but can also be transferred using the [GRANT OWNERSHIP](grant-ownership.md) command to a different role by the owning role (or any role with the MANAGE GRANTS privilege). |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

For additional details on aggregation policy DDL and privileges, see [Privileges and commands](../../user-guide/aggregation-policies.md).

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

Describe the aggregation policy:

> ```sqlexample
> DESC AGGREGATION POLICY my_aggpolicy;
> ```
