# Source: https://docs.snowflake.com/en/sql-reference/functions/system_deregister_cmk_info_postgres.md

Categories:
:   [System functions](../functions-system.md) (System Control)

# SYSTEM$DEREGISTER_CMK_INFO_POSTGRES

Cancels registration of your currently-registered customer-managed key (CMK) for use with Snowflake Postgres Tri-Secret Secure.

## Syntax

```sqlsyntax
SYSTEM$DEREGISTER_CMK_INFO_POSTGRES();
```

## Arguments

None.

## Returns

Returns a status message to system administrators stating that registration of your current CMK is cancelled.

## Arguments

None.

## Access control requirements

Only account administrators (users with the ACCOUNTADMIN role) can call this function.

## Examples

De-register your CMK for your Snowflake account:

```sqlexample
SELECT SYSTEM$DEREGISTER_CMK_INFO_POSTGRES();
```
