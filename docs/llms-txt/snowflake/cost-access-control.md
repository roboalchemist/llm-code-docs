# Source: https://docs.snowflake.com/en/user-guide/cost-access-control.md

# Access control for cost management

This topic describes system-defined roles (roles, application roles, and database roles) that control access to cost management
features. You can assign these roles to a user once to provide access to cost-related features.

A cost-related feature might have its own roles and privileges that provide access without granting access to other features. Refer to
the feature-specific documentation for a discussion of these privileges.

> **Note:**
>
> The access control privileges discussed in this topic do not provide access to resource monitors.

## Access to organization-level cost information

The type of account determines whether a user can view organization-level cost data. For example, the Organization overview tab is
only available from certain accounts.

You can view organization-level cost data from the following accounts:

* The [organization account](organization-accounts.md).
* A regular account with the [ORGADMIN role enabled](organization-administrators.md).

## Viewing a currency as the unit of measure

The unit of measure for cost information can be credits or a currency. You can view a currency as the unit of measure only in certain
circumstances. Being able to see a currency as the unit of measure also allows you to view related information like the remaining balance
of a contract.

To see a currency as the unit measure, you must:

* Access cost information from the organization account or a regular account with the ORGADMIN role enabled.
* Use one of the following roles:

  * ACCOUNTADMIN system-defined role
  * GLOBALORGADMIN system-defined role
  * ORGANIZATION_BILLING_VIEWER. This is a database role for some cost-related features but an application role for other features.

## Default access by administrators

By default, only users with system-defined administrator roles can use cost-related features.

* If you are signed in to the organization account, use the GLOBALORGADMIN role to view cost information.
* If you are signed in to a regular account, use the ACCOUNTADMIN role to view cost information.

  > **Tip:**
  >
  > Consider using an application role and database role to grant administrator rights to cost-related features, even if the user has the
  > ACCOUNTADMIN role. Some features might behave differently if a user with the ACCOUNTADMIN role does not also have the ORGADMIN role. For
  > information about granting administrator rights, see Granting access to other users.

## Granting access to other users

To simplify access control for cost management, Snowflake provides two levels of access:

* Users who can view cost information.
* Users who act as an administrator for cost-related features. These users can also view cost information.

There is an application role/database role combination that corresponds to each level of access. A user’s level of access is determined by
the application role and database role that they are granted. The following shows the application role and database role required
to view cost information or act as an administrator.

| Level of access | Application role | Database role |
| --- | --- | --- |
| Viewer | APP_USAGE_VIEWER | USAGE_VIEWER |
| Administrator | APP_USAGE_ADMIN | USAGE_ADMIN |

> **Note:**
>
> If you want a viewer or administrator to be able to see a currency as the unit of measure (instead of credits), you must also grant the
> ORGANIZATION_BILLING_VIEWER role. For more information, see Viewing a currency as the unit of measure.

You grant access to cost management features by granting the appropriate application role and database role. For example, if you want user
`joe` to be able to view cost information, but not act as an administrator, execute the following commands:

```sqlexample
USE ROLE ACCOUNTADMIN;
CREATE USER joe;
CREATE ROLE cost_viewer_role;

USE DATABASE SNOWFLAKE;
USE SCHEMA ACCOUNT_USAGE;
GRANT APPLICATION ROLE APP_USAGE_VIEWER TO ROLE cost_viewer_role;
GRANT DATABASE ROLE USAGE_VIEWER TO ROLE cost_viewer_role;
GRANT ROLE cost_viewer_role TO USER joe;
```

### Administrator tasks

A user granted the APP_USAGE_ADMIN application role and USAGE_ADMIN database role can view all cost information. In addition, they can
perform the following administrative tasks:

**Budgets**

> * Activate a budget.
> * Deactivate a budget.
> * Modify a spending limit.
> * Modify notification email addresses.
> * Mute notifications for the account budget and for custom budgets.
> * Delete custom budgets.

**Cost anomalies**

> * Modify notification email addresses.
