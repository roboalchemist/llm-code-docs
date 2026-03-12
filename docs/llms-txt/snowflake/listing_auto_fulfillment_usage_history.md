# Source: https://docs.snowflake.com/en/sql-reference/organization-usage/listing_auto_fulfillment_usage_history.md

Schema:
:   [ORGANIZATION_USAGE](../organization-usage.md)

# LISTING_AUTO_FULFILLMENT_USAGE_HISTORY view

This view in the ORGANIZATION_USAGE schema can be used to estimate the costs associated with
[Cross-Cloud Auto-Fulfillment](../../collaboration/provider-listings-auto-fulfillment.md).

When a data product is fulfilled to a region, Snowflake uses a managed account associated with your provider account, called a
*secure share area*, to store the data product in each region with consumer demand. Your provider account incurs costs associated
with the secure share areas in other regions.

For more details, see [Auto-fulfillment costs](../../collaboration/provider-understand-cost-auto-fulfillment.md).

> **Note:**
>
> Because this view provides estimated values, the usage and currency values might not match the values in the
> [USAGE_IN_CURRENCY_DAILY view](usage_in_currency_daily.md) or your usage statement.

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| ORGANIZATION_NAME | VARCHAR | Name of the organization. |
| CONTRACT_NUMBER | VARCHAR | Snowflake contract number for the organization. |
| ACCOUNT_NAME | VARCHAR | Name of the secure share area where the usage occurred. |
| ACCOUNT_LOCATOR | VARCHAR | Locator for the secure share area where the usage occurred. |
| REGION | VARCHAR | Name of the region where the secure share area is located. |
| SERVICE_LEVEL | VARCHAR | Service level (edition) of the secure share area. See [Snowflake editions](../../user-guide/intro-editions.md). |
| USAGE_DATE | DATE | Date (in UTC format) in which the secure share area usage took place. |
| SERVICE_TYPE | VARCHAR | Can be one of:   *DATA_TRANSFER* REPLICATION * STORAGE |
| CURRENCY | VARCHAR | Currency of the usage. |
| ESTIMATED_USAGE | NUMBER (38,9) | Estimated amount of usage to be charged based on SERVICE_TYPE. Units of USAGE depend on the SERVICE_TYPE. For example, when the SERVICE_TYPE is REPLICATION, USAGE is measured in credits. When the SERVICE_TYPE is DATA_TRANSFER or STORAGE, USAGE is measured in terabytes. |
| ESTIMATED_USAGE_IN_CURRENCY | NUMBER (38,9) | Estimated amount to be charged for the SERVICE_TYPE for USAGE on the USAGE_DATE. |
| PROVIDER_ACCOUNT_REGION | VARCHAR | Name of the region where the provider account that shared the data product is located. If NULL, the usage could not be attributed to a specific provider account. |
| PROVIDER_ACCOUNT_NAME | VARCHAR | Name of the provider account that shared the data product that incurred the usage in the secure share area. If NULL, the usage could not be attributed to a specific provider account. |
| PROVIDER_ACCOUNT_LOCATOR | VARCHAR | Locator for the provider account that shared the data product that incurred the usage in the secure share area. If NULL, the usage could not be attributed to a specific provider account. |

## Usage notes

* Latency for the view may be up to 24 hours.
