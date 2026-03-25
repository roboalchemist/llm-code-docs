# Source: https://docs.snowflake.com/en/sql-reference/sql/revoke-role.md

# REVOKE ROLE

Removes a role from another role or a user.

See also:
:   [GRANT ROLE](grant-role.md)

## Syntax

```sqlsyntax
REVOKE ROLE <name> FROM { ROLE <parent_role_name> | USER <user_name> }
```

## Parameters

`name`
:   Specifies the identifier for the role to revoke. If the identifier contains spaces or special characters, the entire string must
    be enclosed in double quotes. Identifiers enclosed in double quotes are also case-sensitive.

`ROLE parent_role_name`
:   Revokes the role from the specified role.

`USER user_name`
:   Revokes the role from the specified user.

## Examples

```sqlexample
REVOKE ROLE analyst FROM ROLE SYSADMIN;
```

```sqlexample
REVOKE ROLE analyst FROM USER user1;
```
