# Source: https://docs.snowflake.com/en/sql-reference/functions/system_hold_privilege_on_account.md

Categories:
:   [System functions](../functions-system.md) (System Information)

# SYSTEM$HOLD_PRIVILEGE_ON_ACCOUNT

Indicates if a privilege has been granted to a Snowflake Native App. For example, providers
can use this function in the setup script to check if the app has the necessary
privileges to create an object.

> **Note:**
>
> This system function can only be called by a Snowflake Native App.

## Syntax

```sqlsyntax
SYSTEM$HOLD_PRIVILEGE_ON_ACCOUNT('<privilege_name>')
```

## Arguments

`'privilege_name'`
:   The name of the privilege.

## Returns

* Returns TRUE if the app has been granted the specified privilege. Otherwise,
  returns FALSE.

## Examples

Check if the app has been granted the CREATE COMPUTE POOL privilege:

```sqlexample
SELECT SYSTEM$HOLD_PRIVILEGE_ON_ACCOUNT('CREATE COMPUTE POOL');
```

Check if the app has been granted the IMPORTED PRIVILEGES ON SNOWFLAKE DB privilege:

```sqlexample
SELECT SYSTEM$HOLD_PRIVILEGE_ON_ACCOUNT('IMPORTED PRIVILEGES ON SNOWFLAKE DB');
```
