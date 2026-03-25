# Source: https://docs.snowflake.com/en/sql-reference/sql/desc-authentication-policy.md

# DESCRIBE AUTHENTICATION POLICY

Describes the properties of an [authentication policy](../../user-guide/authentication-policies.md).

See also:
:   [CREATE AUTHENTICATION POLICY](create-authentication-policy.md), [ALTER AUTHENTICATION POLICY](alter-authentication-policy.md), [DROP AUTHENTICATION POLICY](drop-authentication-policy.md), [SHOW AUTHENTICATION POLICIES](show-authentication-policies.md)

## Syntax

```sqlsyntax
{ DESC | DESCRIBE } AUTHENTICATION POLICY <name>
```

## Parameters

`name`
:   Specifies the identifier for the authentication policy to describe. If the identifier contains spaces or special characters, you must enclose
    the string in double quotation marks. Identifiers enclosed in double quotation marks are case-sensitive. The identifier must meet the
    [identifier requirements](../identifiers-syntax.md).

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this SQL command must have at least one of the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| APPLY AUTHENTICATION POLICY | Account | Only the SECURITYADMIN role, or a higher role, has this privilege by default. The privilege can be granted to additional roles as needed. |
| OWNERSHIP | Authentication policy | OWNERSHIP is a special privilege on an object that is automatically granted to the role that created the object, but can also be transferred using the [GRANT OWNERSHIP](grant-ownership.md) command to a different role by the owning role (or any role with the MANAGE GRANTS privilege). |

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

## Examples

Describe an authentication policy named `my_auth_policy`:

```sqlexample
DESC AUTHENTICATION POLICY my_auth_policy;
```

Use the [pipe operator](../operators-flow.md) to select specific output from the DESCRIBE AUTHENTICATION POLICY command:

```sqlexample
DESCRIBE AUTHENTICATION POLICY go_driver_policy
  ->> SELECT "property", "value"
        FROM $1
        WHERE "property" IN('NAME', 'CLIENT_TYPES', 'CLIENT_POLICY');
```

```output
+---------------+--------------------------------------+
| property      | value                                |
|---------------+--------------------------------------|
| NAME          | GO_DRIVER_POLICY                     |
| CLIENT_TYPES  | [DRIVERS]                            |
| CLIENT_POLICY | {GO_DRIVER={MINIMUM_VERSION=3.14.1}} |
+---------------+--------------------------------------+
```
