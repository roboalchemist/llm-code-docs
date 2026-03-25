# Source: https://docs.snowflake.com/en/sql-reference/sql/grant-application-role.md

# GRANT APPLICATION ROLE

Assigns an application role to an account role, another application role, an application, or a user.

This command creates a “parent-child” relationship between the application role and the role
to which it is granted, also referred to as a role hierarchy.

For more details, see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

See also:
:   [ALTER APPLICATION ROLE](alter-application-role.md), [CREATE APPLICATION ROLE](create-application-role.md),
    [REVOKE APPLICATION ROLE](revoke-application-role.md), [SHOW APPLICATION ROLES](show-application-roles.md)

## Syntax

```sqlsyntax
GRANT APPLICATION ROLE <name> TO  { ROLE <parent_role_name> | APPLICATION ROLE <application_role> | APPLICATION <application_name> | USER <user_name> }
```

## Parameters

`name`
:   Specifies the identifier for the application role to grant. If the identifier contains spaces or
    special characters, the entire string must be enclosed in double quotes. Identifiers enclosed in
    double quotes are also case-sensitive.

`ROLE parent_role_name`
:   Grants the application role to the specified account role.

`APPLICATION ROLE application_role`
:   Grants the application role to the specified application role. This grant creates a role
    hierarchy of application roles.

    An application role can be granted to either an account role or another application role in the
    same application. If the parent role is an application role and the identifier is not fully
    qualified in the form of `application_name.application_role_name`, the command looks
    for the application role in the current application for the session.

`APPLICATION application_name`
:   Grants the application role to the specified application.

`USER user_name`
:   Grants the application role to the specified user.

## Access control requirements

A [role](../../user-guide/security-access-control-overview.md) used to execute this operation must have the following
[privileges](../../user-guide/security-access-control-overview.md) at a minimum:

| Privilege or role | Object | Notes |
| --- | --- | --- |
| ACCOUNTADMIN | Application role | A user with this role can grant a [Budgets application role](../../user-guide/budgets.md) to a custom role. |
| OWNERSHIP | Role | Role that is granted to an account role or another application role. However the application owner can grant an application role to another application role or account role. OWNERSHIP is a special privilege on an object that is automatically granted to the role that created the object, but can also be transferred using the [GRANT OWNERSHIP](grant-ownership.md) command to a different role by the owning role (or any role with the MANAGE GRANTS privilege). |

Only the application owner can grant an application role to other roles or users. Only the SECURITYADMIN role, or a higher role, has this privilege by default. The privilege can be granted to additional roles as needed.

For instructions on creating a custom role with a specified set of privileges, see [Creating custom roles](../../user-guide/security-access-control-configure.md).

For general information about roles and privilege grants for performing SQL actions on
[securable objects](../../user-guide/security-access-control-overview.md), see [Overview of Access Control](../../user-guide/security-access-control-overview.md).

## Usage notes

Granting an application role to another application role can only be performed within the
context of an installed application, for example in application setup script.

## Examples

Grants an application role `app_role` to a different application role `other_app_role`:

```sqlexample
GRANT APPLICATION ROLE app_role to APPLICATION ROLE other_app_role;
```

Grants an application role `app_role` to a user `user1`:

```sqlexample
GRANT APPLICATION ROLE app_role to USER user1;
```
