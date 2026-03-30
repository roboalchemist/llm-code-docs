# Source: https://docs.snowflake.com/en/collaboration/provider-listings-auto-fulfillment-monitor-view-costs.md

# Monitor resources and view costs

This section describes how to monitor auto-fulfillment resources and view estimated and actual costs associated with auto-fulfillment.

## Monitor resources

If you want to minimize costs associated with auto-fulfillment, review the usage of your listings and learn more
about preparing your data for auto-fulfillment:

Monitor Compute Resources
:   Identify the queries run by Snowflake and review the refresh frequency interval for your listings.

    Refer to the [LISTING_AUTO_FULFILLMENT_REFRESH_DAILY view](../sql-reference/data-sharing-usage/listing-auto-fulfillment-refresh-daily.md) to identify the listings and databases contributing to compute cost.

    To identify the queries run by Snowflake to support auto-fulfillment, review the Query History and filter on
    Client generated statements. Refer to the [Query History Page](../user-guide/ui-snowsight-activity.md).

    Review the refresh frequency interval that you set for the listing. Refer to [Set the account-level refresh interval](provider-listings-auto-fulfillment-set-refresh-interval.md).

Monitor Storage Resources
:   Determine what data to put in your listing and how to structure your data to minimize the amount that needs to be auto-fulfilled.
    Refer to [Prepare data for a listing](provider-listings-preparing.md).
    Cross-Cloud Auto-Fulfillment does not support secure views that reference data stored in other databases.

    Refer to the [LISTING_AUTO_FULFILLMENT_DATABASE_STORAGE_DAILY view](../sql-reference/data-sharing-usage/listing-auto-fulfillment-database-storage-daily.md) to identify listings and databases contributing to storage cost.

Monitor Data Transfer Resources
:   Identify the regions in which secure share areas have been created. Run the [SHOW REPLICATION ACCOUNTS](../sql-reference/sql/show-replication-accounts.md) command.

Monitor ECO costs
:   Monitor the ECO costs across your organization. Run the [USAGE_IN_CURRENCY_DAILY view](../sql-reference/organization-usage/usage_in_currency_daily.md) in the [ORGANIZATION_USAGE](../sql-reference/organization-usage.md) schema of the SNOWFLAKE database. In the SERVICE_TYPE column, review the EGRESS_COST_OPTIMIZER value.

## View estimated costs

SQL

To view estimated costs for all secure share areas associated with the provider accounts in your organization, use the
[LISTING_AUTO_FULFILLMENT_USAGE_HISTORY view](../sql-reference/organization-usage/listing_auto_fulfillment_usage_history.md) in the [ORGANIZATION_USAGE](../sql-reference/organization-usage.md) schema of the SNOWFLAKE database.

To view actual costs for accounts in your organization, use other views in the [ORGANIZATION_USAGE](../sql-reference/organization-usage.md) schema of the SNOWFLAKE database.

## View actual costs

You can use the [ORGANIZATION_USAGE](../sql-reference/organization-usage.md) view or the Snowsight Usage dashboard to view costs associated with Cross-Cloud
Auto-Fulfillment and attribute costs associated with fulfilling listings to specific regions. Use the accounts prefixed with
SNOWFLAKE_MANAGED$ and AUTO_FULFILLMENT_AREA$ to attribute cost to specific regions.

You must be an account administrator (use the ACCOUNTADMIN role) or use the [ORGANIZATION_USAGE_VIEWER](../sql-reference/snowflake-db-roles.md) database role to view usage data for Snowflake.

SnowsightSQL

To view actual costs in Snowsight, do the following:

1. Sign in to [Snowsight](../user-guide/ui-snowsight-gs.md).
2. In the navigation menu, select Admin » Cost management, and then select Consumption.
3. Select a warehouse to use to view the usage data.
4. Using the accounts filter, select the accounts titled SNOWFLAKE_MANAGED$PUBLIC_<region_name> or AUTO_FULFILLMENT_AREA$-<region_name> to filter on the secure share areas used by auto-fulfillment.

   > For example, select SNOWFLAKE_MANAGED$PUBLIC_AWS_EU_WEST_2 to view the costs associated with using auto-fulfilling data to the AWS region eu_west_2.
5. Use the filters to view all usage types, or focus on compute, storage, or data transfer costs.

To view estimated costs using SQL, you can query the [LISTING_AUTO_FULFILLMENT_USAGE_HISTORY view](../sql-reference/organization-usage/listing_auto_fulfillment_usage_history.md) in the [ORGANIZATION_USAGE](../sql-reference/organization-usage.md) schema. To view actual costs, refer to the other views in the ORGANIZATION_USAGE schema. For more details on viewing costs, see [Exploring overall cost](../user-guide/cost-exploring-overall.md).

The costs that you see reflect all listings shared to a particular region by any account in your organization. To identify which listings
are being consumed in which regions and contributing to the costs in a specific region, see [Monitor listing use](provider-listings-monitor-studio.md).
