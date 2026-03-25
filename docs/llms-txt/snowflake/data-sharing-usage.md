# Source: https://docs.snowflake.com/en/sql-reference/data-sharing-usage.md

# Data Sharing Usage

In the SNOWFLAKE database, the DATA_SHARING_USAGE schema includes views that display information about listings published in the
Snowflake Marketplace or a data exchange. This includes telemetry data (number of clicks), as well as consumption data (queries
run by consumers).

> **Note:**
>
> This data is available only to the account that published the individual listing. By default, only account administrators (users with
> the ACCOUNTADMIN role) in the account can access the SNOWFLAKE database and schemas within the database, or perform queries on the
> views; however, privileges on the database can be granted to other roles in your account to allow other users to access the objects.
> For more details, see [Enabling other roles to use schemas in the SNOWFLAKE database](account-usage.md).

## DATA_SHARING_USAGE views

The DATA_SHARING_USAGE schema contains the following views:

| View | Type | Latency [1] | Retention duration | View audience |
| --- | --- | --- | --- | --- |
| [APPLICATION_STATE](data-sharing-usage/application-state-view.md) | Current state | up to 10 minutes | Not applicable. | Provider |
| [LISTING_ACCESS_HISTORY](data-sharing-usage/listing-access-history.md) | Historical | up to 2 days | Data retained for 1 year. | Provider |
| [LISTING_AUTO_FULFILLMENT_DATABASE_STORAGE_DAILY](data-sharing-usage/listing-auto-fulfillment-database-storage-daily.md) | Historical | up to 2 days | Data retained for 1 year. | Provider |
| [LISTING_AUTO_FULFILLMENT_REFRESH_DAILY](data-sharing-usage/listing-auto-fulfillment-refresh-daily.md) | Historical | up to 2 days | Data retained for 1 year. | Provider |
| [LISTING_CONSUMPTION_DAILY](data-sharing-usage/listing-consumption-daily.md) | Historical | up to 2 days | Data retained for 1 year. | Provider |
| [LISTING_EVENTS_DAILY](data-sharing-usage/listing-events-daily.md) | Historical | up to 2 days | Data retained for 1 year. | Provider |
| [LISTING_TELEMETRY_DAILY](data-sharing-usage/listing-telemetry-daily.md) | Historical | up to 2 days | Data retained for 1 year. | Provider |
| [MARKETPLACE_DISBURSEMENT_REPORT](../collaboration/views/marketplace-disbursement-report-ds.md) | Historical | up to 2 days | Data retained for 1 year. | Provider |
| [MARKETPLACE_LISTING_INVOICE_STATUS](../collaboration/views/marketplace_listing_invoice_status.md) | Historical | up to 2 days | Data retained for 1 year. | Provider |
| [MARKETPLACE_PAID_USAGE_DAILY](../collaboration/views/marketplace-paid-usage-daily-ds.md) | Historical | up to 2 days | Data retained for 1 year. | Consumer |
| [MARKETPLACE_PROVIDER_SPCS_USAGE](../collaboration/views/marketplace-provider-spcs-usage-ds.md) | Historical | up to 2 days | Data retained for 1 year. | Provider |
| [MONETIZED_USAGE_DAILY](../collaboration/views/monetized-usage-daily-ds.md) | Historical | up to 2 days | Data retained for 1 year. | Provider |
| [PAID_LISTING_ACCESS_AND_CHANGE_LOG](data-sharing-usage/paid-listing-access-change-log.md) | Historical | up to 2 days | Data retained for 1 year. | Provider |

[1] All latency times are approximate; in some instances, the actual latency may be lower.

## General usage notes

The Snowflake-specific views are subject to change. Avoid selecting all columns from these views. Instead, select the columns that you want.
For example, if you want the `name` column, use `SELECT name`, rather than `SELECT *`.
