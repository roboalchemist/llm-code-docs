# Source: https://docs.snowflake.com/en/collaboration/provider-monetization-usage.md

# Monetization usage views

Snowflake provides historical usage data for paid listings as a set of views in the [ORGANIZATION_USAGE](../sql-reference/organization-usage.md) and [DATA_SHARING_USAGE](../sql-reference/data-sharing-usage.md)
schemas in the shared SNOWFLAKE database.

You can view historical usage data for other listings using the same [ORGANIZATION_USAGE](../sql-reference/organization-usage.md) and [DATA_SHARING_USAGE](../sql-reference/data-sharing-usage.md)
schemas, or view aggregated usage analytics in the Provider Studio. Refer to [Monitor listing use](provider-listings-monitor-studio.md).

## Monetization usage views in the ORGANIZATION_USAGE schema

* [MARKETPLACE_DISBURSEMENT_REPORT (ORGANIZATION_USAGE) View](views/marketplace-disbursement-report-org.md)
* [MONETIZED_USAGE_DAILY (ORGANIZATION_USAGE) View](views/monetized-usage-daily-org.md)

## Monetization usage views in the DATA_SHARING_USAGE schema

* [LISTING_EVENTS_DAILY view](../sql-reference/data-sharing-usage/listing-events-daily.md)
* [MARKETPLACE_DISBURSEMENT_REPORT (DATA_SHARING_USAGE) View](views/marketplace-disbursement-report-ds.md)
* [MONETIZED_USAGE_DAILY (DATA_SHARING_USAGE) View](views/monetized-usage-daily-ds.md)
