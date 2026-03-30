# Source: https://docs.snowflake.com/en/sql-reference/functions/current_role_type.md

Categories:
:   [Context functions](../functions-context.md) (Session Object)

# CURRENT_ROLE_TYPE

Calling the CURRENT_ROLE_TYPE function returns `ROLE` if the current active (primary) role in the session is an account role. Calling the
CURRENT_ROLE_TYPE function from a session running inside a Snowflake native application returns `APPLICATION_INSTANCE`.

## Syntax

```sqlsyntax
CURRENT_ROLE_TYPE()
```

## Arguments

None.

## Usage notes

The primary role in a session cannot be a database role. Therefore, this functions will never return `DATABASE_ROLE`.

None.

## Examples

```sqlexample
SELECT CURRENT_ROLE_TYPE();

+---------------------+
| CURRENT_ROLE_TYPE() |
|---------------------|
| ROLE                |
+---------------------+
```
