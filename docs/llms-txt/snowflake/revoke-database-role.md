# Source: https://docs.snowflake.com/en/sql-reference/sql/revoke-database-role.md

# REVOKE DATABASE ROLE

Revokes a database role from an [account role or another database role](../../user-guide/security-access-control-overview.md).

See also:
:   [GRANT DATABASE ROLE](grant-database-role.md) , [GRANT ROLE](grant-role.md) , [REVOKE ROLE](revoke-role.md) , [GRANT <privileges> … TO ROLE](grant-privilege.md)

## Syntax

```sqlsyntax
REVOKE DATABASE ROLE <name> FROM { ROLE | DATABASE ROLE } <parent_role_name>

REVOKE DATABASE ROLE <name> FROM APPLICATION <app_name>
```

## Parameters

`name`
:   Specifies the identifier for the database role to revoke. If the identifier contains spaces or special characters, the entire string must
    be enclosed in double quotes. Identifiers enclosed in double quotes are also case-sensitive.

`DATABASE ROLE parent_role_name`
:   Revokes the database role from the specified database role.

`ROLE parent_role_name`
:   Revokes the database role from the specified account role.

`APPLICATION app_name`
:   Revokes the database role from the specified Snowflake Native App.

## Examples

Revokes the database role named `analyst` from the account role named `SYSADMIN`.

```sqlexample
REVOKE DATABASE ROLE analyst FROM ROLE SYSADMIN;
```

Revokes the database role named `dr1` from another database role named `dr2`.

```sqlexample
REVOKE DATABASE ROLE dr1 FROM DATABASE ROLE dr2;
```

Revokes the database role named `dr1` from the Snowflake Native App named `hello_snowflake_app`.

```sqlexample
REVOKE DATABASE ROLE dr1 FROM APPLICATION hello_snowflake_app;
```
