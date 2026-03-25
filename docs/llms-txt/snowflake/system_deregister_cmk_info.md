# Source: https://docs.snowflake.com/en/sql-reference/functions/system_deregister_cmk_info.md

Categories:
:   [System functions](../functions-system.md) (System Control)

# SYSTEM$DEREGISTER_CMK_INFO

Cancels registration of your currently-registered customer-managed key (CMK) for use with Tri-Secret Secure.

See also:
:   [Understanding CMK self-registration with support activation of Tri-Secret Secure](../../user-guide/security-encryption-tss.md)

## Syntax

```sqlsyntax
SYSTEM$DEREGISTER_CMK_INFO();
```

## Arguments

None.

## Returns

Returns a status message to system administrators stating that registration of your current CMK is cancelled.

## Access control requirements

Only account administrators (users with the ACCOUNTADMIN role) can call this function.

## Examples

De-register your CMK for your Snowflake account:

```sqlexample
SELECT SYSTEM$DEREGISTER_CMK_INFO();
```
