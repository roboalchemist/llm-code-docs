# Source: https://docs.snowflake.com/en/sql-reference/functions/system_activate_cmk_info_postgres.md

Categories:
:   [System functions](../functions-system.md) (System Control)

# SYSTEM$ACTIVATE_CMK_INFO_POSTGRES

Activates Snowflake Postgres Tri-Secret Secure in your account by using the CMK (customer-managed key) information that you
registered for your account.

This system function performs the following actions:

* Configures your account to use Snowflake Postgres Tri-Secret Secure with the registered CMK.
* Snowflake Postgres instances created after the registered CMK is activated will use it.
* Snowflake Postgres instances that were created before the registered CMK is activated will not be rekeyed to use the new CMK, but will
  continue working with the prior CMK or no CMK.
* Snowflake Postgres replicas and forks will always inherit the CMK configuration from the parent Snowflake Postgres primary instance.

See also:
:   [Understanding CMK self-registration with support activation of Tri-Secret Secure](../../user-guide/security-encryption-tss.md)

## Syntax

```sqlsyntax
SYSTEM$ACTIVATE_CMK_INFO_POSTGRES()
```

## Returns

Success or error messages.

## Access control requirements

Only users that are granted the MODIFY privilege on the account can call this function.
The MODIFY privilege is typically granted only to the ACCOUNTADMIN role.

## Examples

Activate Snowflake Postgres Tri-Secret Secure for your Snowflake account:

```sqlexample
SELECT SYSTEM$ACTIVATE_CMK_INFO_POSTGRES();
```
