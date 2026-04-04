# Source: https://docs.snowflake.com/en/sql-reference/functions/system_cleanup_database_role_grants.md

Categories:
:   [System functions](../functions-system.md) (Control)

# SYSTEM$CLEANUP_DATABASE_ROLE_GRANTS

Revokes privileges on dropped objects from the share and grants the database role to the share.

## Syntax

```sqlsyntax
SYSTEM$CLEANUP_DATABASE_ROLE_GRANTS( '<database_role_name>' , '<share_name>' )
```

## Arguments

`'database_role_name'`
:   The name of the database role.

    If the identifier is not fully qualified in the form of `db_name.database_role_name`, the command uses the database role
    in the current database for the session.

`'share_name'`
:   The name of the share.

## Access control requirements

To call this function, the active role must have the global [MANAGE GRANTS privilege](../../user-guide/security-access-control-privileges.md).

## Usage notes

None.

## Example

Call the function:

> ```sqlexample
> SELECT SYSTEM$CLEANUP_DATABASE_ROLE_GRANTS('mydb.dbr1' , 'myshare');
> ```
