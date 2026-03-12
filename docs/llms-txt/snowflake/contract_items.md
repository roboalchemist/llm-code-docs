# Source: https://docs.snowflake.com/en/sql-reference/organization-usage/contract_items.md

Schema:
:   [ORGANIZATION_USAGE](../organization-usage.md)

# CONTRACT_ITEMS view

The CONTRACT_ITEMS view in the ORGANIZATION_USAGE schema can be used to return the contract information for an organization.

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| ORGANIZATION_NAME | VARCHAR | Name of the organization. |
| CONTRACT_NUMBER | VARCHAR | Snowflake contract number for the organization. |
| START_DATE | DATE | The start date for the Snowflake contract or the date the CONTRACT_ITEM goes into effect for the organization. |
| END_DATE | DATE | The end date for the Snowflake contract or the date the CONTRACT_ITEM stops being used for the organization. |
| EXPIRATION_DATE | DATE | The expiration date for the Snowflake contract or the date after which either the Renewal Contract goes into effect if signed within 30 days or the Snowflake relationship is terminated. |
| CONTRACT_ITEM | VARCHAR | One of capacity, additional capacity, or free usage. |
| CURRENCY | VARCHAR | The currency for the CONTRACT_ITEM. |
| AMOUNT | NUMBER (38,2) | The amount for the CONTRACT_ITEM measured in CURRENCY, not credits. |
| CONTRACT_MODIFIED_DATE | DATE | The date (in the UTC timezone) the CONTRACT_ITEM was last modified. |

## Usage notes

* Latency for the view may be up to 24 hours.
* If multiple organizations draw down from the same capacity contract, only the primary organization can access this view. The primary
  organization is also known as the funding organization.
* This view shows only the active contract for the organization.
* Customers who signed a contract through a Snowflake reseller cannot access data in this view.
* Data is retained indefinitely.
* This view does not include data generated prior to June 2020. To obtain data before this date, contact [Snowflake Support](https://docs.snowflake.com/user-guide/contacting-support).
