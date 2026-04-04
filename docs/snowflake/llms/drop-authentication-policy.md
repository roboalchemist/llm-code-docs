# Source: https://docs.snowflake.com/en/sql-reference/sql/drop-authentication-policy.md

# DROP AUTHENTICATION POLICY

Removes an [authentication policy](../../user-guide/authentication-policies.md) from the system.

See also:
:   [CREATE AUTHENTICATION POLICY](create-authentication-policy.md), [ALTER AUTHENTICATION POLICY](alter-authentication-policy.md), [DESCRIBE AUTHENTICATION POLICY](desc-authentication-policy.md), [SHOW AUTHENTICATION POLICIES](show-authentication-policies.md)

## Syntax

```sqlsyntax
DROP AUTHENTICATION POLICY [ IF EXISTS ] <name>
```

## Parameters

`name`
:   Specifies the identifier for the authentication policy to drop. If the identifier contains spaces or special characters, you must enclose
    the string in double quotation marks. Identifiers enclosed in double quotation marks are case-sensitive. The identifier must meet the
    [identifier requirements](../identifiers-syntax.md).

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege | Object | Notes |
| --- | --- | --- |
| OWNERSHIP | Authentication policy | OWNERSHIP is a special privilege on an object that is automatically granted to the role that created the object, but can also be transferred using the [GRANT OWNERSHIP](grant-ownership.md) command to a different role by the owning role (or any role with the MANAGE GRANTS privilege). |

Operating on an object in a schema requires at least one privilege on the parent database and at least one privilege on the parent schema.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

* You cannot recover dropped authentication policies. You must recreate them.
* You cannot drop an authentication policy if it is set on an account or user.

* When the IF EXISTS clause is specified and the target object doesn’t exist, the command completes successfully
  without returning an error.

## Examples

Drop an authentication policy named `my_auth_policy`:

```sqlexample
DROP AUTHENTICATION POLICY my_auth_policy;
```
