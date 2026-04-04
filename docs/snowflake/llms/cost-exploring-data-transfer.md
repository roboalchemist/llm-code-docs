# Source: https://docs.snowflake.com/en/user-guide/cost-exploring-data-transfer.md

# Exploring data transfer cost

Snowflake does not charge a data ingress fee to bring data into your account, but does charge a per-byte fee to transfer data from a
Snowflake account into another region on the same cloud platform or into a different cloud platform.

This topic describes how to gain insight into historical data transfer costs using [Snowsight](ui-snowsight-gs.md), or by writing queries against
views in the [ACCOUNT_USAGE](../sql-reference/account-usage.md) and [ORGANIZATION_USAGE](../sql-reference/organization-usage.md) schemas.
Snowsight allows you to quickly and easily obtain information about cost from a visual dashboard. Queries against the usage views
allow you to drill down into cost data and can help generate custom reports and dashboards.

To gain a better understanding of how data transfer fees accrue, see [Understanding data transfer cost](cost-understanding-data-transfer.md).

## Viewing the data transfer history

Users can use Snowsight to view the amount of data transferred from your Snowflake account to
a different cloud provider or region within a specified date range. The unit of measure is bytes.

To explore data transfer costs:

1. Sign in to [Snowsight](ui-snowsight-gs.md).
2. Switch to a role with [access to cost-related features](cost-access-control.md).
3. In the navigation menu, select Admin » Cost management.
4. Select a warehouse to use to view the usage data. Snowflake recommends using an XS warehouse for this purpose.
5. Select Consumption.
6. Select Data Transfer from the Usage Type drop-down.

For usage notes related to the Consumption page, see [Usage notes](cost-exploring-overall.md).

## Querying data for data transfer cost

Snowflake provides two schemas, [ORGANIZATION_USAGE](../sql-reference/organization-usage.md) and
[ACCOUNT_USAGE](../sql-reference/account-usage.md), that contain data related to usage and cost. The ORGANIZATION_USAGE schema provides
cost information for all of the accounts in the organization while the ACCOUNT_USAGE schema provides similar information for a single
account. Views in these schemas provide granular, analytics-ready usage data to build custom reports or dashboards.

Most views in the ORGANIZATION_USAGE and ACCOUNT_USAGE schemas contain the cost of data transfers in terms of the volume of data
transferred. To view cost in currency rather than volume, write queries against the
[USAGE_IN_CURRENCY_DAILY view](../sql-reference/organization-usage/usage_in_currency_daily.md). This view converts the volume of data transferred into cost in currency
using the daily price of transferring a TB.

The following views provide usage and cost information related to transferring data from your Snowflake account to a different cloud
provider or region.

| View | Description | Schema |
| --- | --- | --- |
| DATA_TRANSFER_DAILY_HISTORY | Number of bytes transferred on a given day. For more detailed data, use the DATA_TRANSFER_HISTORY view instead. | [ORGANIZATION_USAGE](../sql-reference/organization-usage/data_transfer_daily_history.md) |
| DATA_TRANSFER_HISTORY | Number of bytes transferred, include the source cloud and region, target cloud and region, and type of transfer. | [ORGANIZATION_USAGE](../sql-reference/organization-usage/data_transfer_history.md) [ACCOUNT_USAGE](../sql-reference/account-usage/data_transfer_history.md) |
| DATABASE_REPLICATION_USAGE_HISTORY | Number of bytes transferred and credit consumed during database replication. | [ACCOUNT_USAGE](../sql-reference/account-usage/database_replication_usage_history.md) |
| LISTING_AUTO_FULFILLMENT_USAGE_HISTORY | Estimated usage associated with fulfilling data products to other regions by using Cross-Cloud Auto-Fulfillment. Refer to the SERVICE_TYPE of DATA_TRANSFER. | [ORGANIZATION_USAGE](../sql-reference/organization-usage/listing_auto_fulfillment_usage_history.md) |
| REPLICATION_USAGE_HISTORY | Number of bytes transferred and credits consumed during database replication. If possible, use the [DATABASE_REPLICATION_USAGE_HISTORY view](../sql-reference/account-usage/database_replication_usage_history.md) instead. | [ORGANIZATION_USAGE](../sql-reference/organization-usage/replication_usage_history.md) [ACCOUNT_USAGE](../sql-reference/account-usage/replication_usage_history.md) |
| REPLICATION_GROUP_USAGE_HISTORY | Number of bytes transferred and credits consumed during replication for a specific replication group. | [ORGANIZATION_USAGE](../sql-reference/organization-usage.md) [ACCOUNT_USAGE](../sql-reference/account-usage/replication_group_usage_history.md) |
| USAGE_IN_CURRENCY_DAILY | Daily data transfer in TB along with the cost of that usage in the organization’s currency. | [ORGANIZATION_USAGE](../sql-reference/organization-usage/usage_in_currency_daily.md) |

> **Note:**
>
> The views and table functions of the [Snowflake Information Schema](../sql-reference/info-schema.md) also provide usage data related to cost. Though
> the ACCOUNT_USAGE schema is preferred, the Information Schema can be faster in some circumstances.
