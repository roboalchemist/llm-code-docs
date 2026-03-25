# Source: https://docs.snowflake.com/en/sql-reference/functions/system_deactivate_cmk_info.md

Categories:
:   [System functions](../functions-system.md)

# SYSTEM$DEACTIVATE_CMK_INFO

De-activates Tri-Secret Secure in your account.

This system function:

* Configures your account to stop using Tri-Secret Secure.
* Creates a new account master key.
* Retires the composed account master key.
* Registers your account with the rekeying background service.

See also:
:   [Understanding CMK self-registration with support activation of Tri-Secret Secure](../../user-guide/security-encryption-tss.md)

## Syntax

```sqlsyntax
SYSTEM$DEACTIVATE_CMK_INFO()
```

## Arguments

None.

## Returns

Success or error messages.

## Access control requirements

Only users granted the MODIFY privilege on the account can call this function. The MODIFY privilege on an account is typically granted only
to the ACCOUNTADMIN role.

## Usage notes

The background service generates email messages that notify the account administrator when Tri-Secret Secure is deactivated.

## Examples

Deactivate Tri-Secret Secure for your Snowflake account:

```sqlexample
SELECT SYSTEM$DEACTIVATE_CMK_INFO();
```
