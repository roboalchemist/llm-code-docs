# Source: https://docs.snowflake.com/en/sql-reference/functions/system_enable_global_data_sharing_for_account.md

Categories:
:   [System functions](../functions-system.md) (System Control)

# SYSTEM$ENABLE_GLOBAL_DATA_SHARING_FOR_ACCOUNT

Enables Cross-Cloud Auto-Fulfillment on an account. Cross-Cloud Auto-Fulfillment allows you to automatically provide the share or application package attached to your listing to other Snowflake consumer regions.

See also:
:   [SYSTEM$IS_GLOBAL_DATA_SHARING_ENABLED_FOR_ACCOUNT](system_is_global_data_sharing_enabled_for_account.md) , [SYSTEM$DISABLE_GLOBAL_DATA_SHARING_FOR_ACCOUNT](system_disable_global_data_sharing_for_account.md), [Auto-fulfillment for listings](../../collaboration/provider-listings-auto-fulfillment.md)

## Syntax

```sqlsyntax
SYSTEM$ENABLE_GLOBAL_DATA_SHARING_FOR_ACCOUNT( '<account_name>' )
```

## Arguments

`account_name`
:   Specifies the account on which to enable Cross-Cloud Auto-Fulfillment. To learn more about Snowflake account identifiers and how to locate them, see [Account identifiers](../../user-guide/admin-account-identifier.md).

## Returns

Returns the VARCHAR value `Statement executed successfully` if the function successfully enables Cross-Cloud Auto-Fulfillment on the account.

## Access control requirements

* Only [organization administrators](../../user-guide/organization-administrators.md) can execute this function.

## Examples

The following example enables Cross-Cloud Auto-Fulfillment on the account named `my_account`:

```sqlexample
SELECT SYSTEM$ENABLE_GLOBAL_DATA_SHARING_FOR_ACCOUNT('my_account');
```

```output
+--------------------------------------------------------------------+
| SYSTEM$SYSTEM$ENABLE_GLOBAL_DATA_SHARING_FOR_ACCOUNT('my_account') |
|--------------------------------------------------------------------|
| Statement executed successfully                                    |
+--------------------------------------------------------------------+
```
