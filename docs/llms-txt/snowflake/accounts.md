# Source: https://docs.snowflake.com/en/sql-reference/organization-usage/accounts.md

Schema:
:   [ORGANIZATION_USAGE](../organization-usage.md)

# ACCOUNTS view

The ACCOUNTS view in the ORGANIZATION_USAGE schema can be used to obtain details about the accounts in an organization.

## Columns

| Column | Data Type | Description |
| --- | --- | --- |
| ORGANIZATION_NAME | VARCHAR | Name of the organization. |
| ACCOUNT_NAME | VARCHAR | User-defined name that identifies an account within the organization. |
| CREATED_ON | TIMESTAMP | Date and time when the account was created. |
| REGION | VARCHAR | Snowflake Region where the account is located. A Snowflake Region is a distinct location within a cloud platform region that is isolated from other Snowflake Regions. A Snowflake Region can be either multi-tenant or single-tenant (for a Virtual Private Snowflake account). |
| REGION_GROUP | VARCHAR | [Region group](../../user-guide/admin-account-identifier.md) where the account is located. |
| EDITION | VARCHAR | [Snowflake Edition](../../user-guide/intro-editions.md) of the account. |
| IS_ORG_ADMIN | BOOLEAN | Indicates whether the [ORGADMIN role](../../user-guide/organization-administrators.md) is enabled in an account. |
| IS_LOCKED | BOOLEAN | Indicates whether the account is locked. To determine if it was locked because it was dropped, look for a date and time in the SCHEDULED_DELETION_TIME column. If an account is unexpectedly locked, contact [Snowflake Support](https://docs.snowflake.com/user-guide/contacting-support). |
| ACCOUNT_URL | VARCHAR | Preferred Snowflake [account URL](../../user-guide/organizations-connect.md) that includes the values of organization_name and account_name. |
| ACCOUNT_OLD_URL | VARCHAR | If the original [account URL](../../user-guide/organizations-connect.md) was saved when the account was renamed, provides the original URL. If the original account URL was dropped, the value is NULL even if the account was renamed. |
| ACCOUNT_OLD_URL_LAST_USED | VARCHAR | If the original account URL was saved when the account was renamed, indicates the last time the account was accessed using the original URL. |
| ORGANIZATION_OLD_URL | VARCHAR | If the account’s organization was changed in a way that created a new [account URL](../../user-guide/organizations-connect.md) and the original account URL was saved, provides the original account URL. If the original account URL was dropped, the value is NULL even if the organization changed. |
| ORGANIZATION_OLD_URL_LAST_USED | VARCHAR | If the account’s organization was changed in a way that created a new account URL and the original account URL was saved, indicates the last time the account was accessed using the original account URL. |
| ACCOUNT_LOCATOR | VARCHAR | [System-assigned identifier](../../user-guide/admin-account-identifier.md) of the account. |
| MANAGED_ACCOUNTS | VARCHAR | Indicates how many [reader accounts](../../user-guide/data-sharing-reader-create.md) have been created by the account. |
| IS_MANAGED | BOOLEAN | Indicates whether the account is a reader account. If `true`, the account is a reader account. |
| PARENT_ACCOUNT | VARCHAR | For reader accounts, provides the name of the parent account that is providing the reader account to consumers. |
| CONSUMPTION_BILLING_ENTITY_NAME | VARCHAR | Name of the consumption billing entity associated with an account. |
| MARKETPLACE_CONSUMER_BILLING_ENTITY_NAME | VARCHAR | Name of the marketplace consumer billing entity associated with an account. |
| MARKETPLACE_PROVIDER_BILLING_ENTITY_NAME | VARCHAR | Name of the marketplace provider billing entity associated with an account. |
| ALTERED_ON | TIMESTAMP | Date and time of the most recent change to the account. |
| SCHEDULED_DELETION_TIME | TIMESTAMP | Date and time when a [dropped account](../../user-guide/organizations-manage-accounts-delete.md) will be permanently deleted. |
| DELETED_ON | TIMESTAMP | Date and time when the account was permanently deleted. |
| MOVED_ON | TIMESTAMP | Date and time when the account was moved from the current organization to a different one. |
| COMMENT | VARCHAR | Comment associated with the account. |
| IS_EVENTS_ACCOUNT | BOOLEAN | Indicates whether an account is an events account. For more information, see [Use logging and event tracing for an app](../../developer-guide/native-apps/event-about.md). |

## Usage notes

* Latency for the view may be up to 24 hours.
* Deleted accounts are removed from the view after one year.
