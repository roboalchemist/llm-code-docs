# Source: https://docs.snowflake.com/en/collaboration/provider-listings-auto-fulfillment-manage-privileges.md

# Manage privileges for auto-fulfillment

After auto-fulfillment is enabled on an account, the ACCOUNTADMIN role can delegate the MANAGE LISTING AUTO FULFILLMENT privilege to other roles in the account, revoke the privileges, and determine whether the privileges have been delegated to a specific account within their organization.

## Delegate privileges to set up auto-fulfillment

SQL

After enabling auto-fulfillment on an account, the ACCOUNTADMIN role can grant the MANAGE LISTING AUTO FULFILLMENT privilege to other roles in the account.

```sqlsyntax
USE ROLE ACCOUNTADMIN;
GRANT MANAGE LISTING AUTO FULFILLMENT ON ACCOUNT TO ROLE <role_name>;
```

The ACCOUNTADMIN role can also revoke the MANAGE LISTING AUTO FULFILLMENT privilege.

```sqlsyntax
USE ROLE ACCOUNTADMIN;
REVOKE MANAGE LISTING AUTO FULFILLMENT ON ACCOUNT FROM ROLE <my_role>;
```

## Verify whether auto-fulfillment is enabled for an account

SQL

To determine whether auto-fulfillment is enabled on an account, call the [SYSTEM$IS_GLOBAL_DATA_SHARING_ENABLED_FOR_ACCOUNT](../sql-reference/functions/system_is_global_data_sharing_enabled_for_account.md) system function. The arguments for this system function are described below.

Calling this system function requires the ORGADMIN role.

```sqlsyntax
SELECT SYSTEM$IS_GLOBAL_DATA_SHARING_ENABLED_FOR_ACCOUNT(
  '<account_name>'
  );
```

Where:

`account_name`
:   Specifies the name of the account for which you want to check if users with the ACCOUNTADMIN role can manage auto-fulfillment. See [Finding the organization and account name for an account](../user-guide/admin-account-identifier.md).
