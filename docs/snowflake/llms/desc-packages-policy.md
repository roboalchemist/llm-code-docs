# Source: https://docs.snowflake.com/en/sql-reference/sql/desc-packages-policy.md

# DESCRIBE PACKAGES POLICY

Describes the details about a packages policy.

DESCRIBE can be abbreviated to DESC.

## Syntax

```sqlsyntax
DESC[RIBE] PACKAGES POLICY <name>
```

## Parameters

`name`
:   Specifies the identifier for the packages policy to describe. If the identifier contains spaces or special characters, the entire string must be
    enclosed in double quotes. Identifiers enclosed in double quotes are also case-sensitive.

    For more details, see [Identifier requirements](../identifiers-syntax.md).

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this SQL command must have at least one of the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| OWNERSHIP | Packages policy | OWNERSHIP is a special privilege on an object that is automatically granted to the role that created the object, but can also be transferred using the [GRANT OWNERSHIP](grant-ownership.md) command to a different role by the owning role (or any role with the MANAGE GRANTS privilege). |
| USAGE | Packages policy | Enables viewing a packages policy. Grants the ability to view the contents of a packages policy in a SHOW or DESCRIBE command and [INFORMATION_SCHEMA.CURRENT_PACKAGES_POLICY](../info-schema/current_packages_policy.md). Can be granted to a role using the [GRANT <privileges> … TO ROLE](grant-privilege.md) command. |

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

```sqlexample
DESC PACKAGES POLICY packages_policy_prod_1;
```
