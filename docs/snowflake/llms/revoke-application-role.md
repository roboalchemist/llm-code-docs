# Source: https://docs.snowflake.com/en/sql-reference/sql/revoke-application-role.md

# REVOKE APPLICATION ROLE

Revokes an application role from an account role or another application role.

See also:
:   [ALTER APPLICATION ROLE](alter-application-role.md), [CREATE APPLICATION ROLE](create-application-role.md), [GRANT APPLICATION ROLE](grant-application-role.md),
    [SHOW APPLICATION ROLES](show-application-roles.md)

## Syntax

```sqlsyntax
REVOKE APPLICATION ROLE <name> FROM { ROLE <parent_role_name> | APPLICATION ROLE <application_role> | APPLICATION <application> }
```

## Parameters

`name`
:   Specifies the identifier for the application role to revoke. If the identifier contains spaces or special
    characters, the entire string must be enclosed in double quotes. Identifiers enclosed in double quotes are also case-sensitive.

`FROM ROLE parent_role_name`
:   Revokes the application role from the specified account role.

`APPLICATION ROLE application_role`
:   Revokes the role from the specified application role.

`APPLICATION ROLE application`
:   Revokes the role from the specified application.

## Usage notes

An application role may only be revoked from another application role within the context of
the installed application, for example within the application setup script.

## Examples

```sqlexample
REVOKE APPLICATION ROLE app_role FROM APPLICATION ROLE other_role;
```
