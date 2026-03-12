# Source: https://docs.snowflake.com/en/sql-reference/functions/system_is_global_data_sharing_enabled_for_account.md

Categories:
:   [System functions](../functions-system.md) (System Information)

# SYSTEM$IS_GLOBAL_DATA_SHARING_ENABLED_FOR_ACCOUNT

Specifies whether Cross-Cloud Auto-Fulfillment is enabled or disabled on an account.

See also:
:   [SYSTEM$ENABLE_GLOBAL_DATA_SHARING_FOR_ACCOUNT](system_enable_global_data_sharing_for_account.md), [SYSTEM$DISABLE_GLOBAL_DATA_SHARING_FOR_ACCOUNT](system_disable_global_data_sharing_for_account.md), [Auto-fulfillment for listings](../../collaboration/provider-listings-auto-fulfillment.md)

## Syntax

```sqlsyntax
SYSTEM$IS_GLOBAL_DATA_SHARING_ENABLED_FOR_ACCOUNT( '<account_name>' )
```

## Arguments

`account_name`
:   Specifies the account on which you want to determine if Cross-Cloud Auto-Fulfillment is enabled or disabled. To learn more about Snowflake account identifiers and how to locate them, see [Account identifiers](../../user-guide/admin-account-identifier.md).

## Returns

Returns one of the following Boolean values:

* `TRUE` (if Cross-Cloud Auto-Fulfillment is enabled for the current account)
* `FALSE` (if Cross-Cloud Auto-Fulfillment is disabled for the current account)

## Access control requirements

* Only [organization administrators](../../user-guide/organization-administrators.md) can execute this function.

## Examples

The following example determines if Cross-Cloud Auto-Fulfillment is enabled on the account named `my_account`:

```sqlexample
SELECT SYSTEM$IS_GLOBAL_DATA_SHARING_ENABLED_FOR_ACCOUNT('my_account');
```

```output
+------------------------------------------------------------------------+
| SYSTEM$SYSTEM$IS_GLOBAL_DATA_SHARING_ENABLED_FOR_ACCOUNT('my_account') |
|------------------------------------------------------------------------|
| TRUE                                                                   |
+------------------------------------------------------------------------+
```
