# Source: https://docs.snowflake.com/en/user-guide/cost-exploring-data-storage.md

# Exploring storage cost

Total Storage cost is the sum of costs associated with:

* Staged file storage
* Database table storage
* Fail-safe and Time Travel storage

This topic describes how to gain insight into historical storage costs using [Snowsight](ui-snowsight-gs.md), or by writing queries against views in
the [ACCOUNT_USAGE](../sql-reference/account-usage.md) and [ORGANIZATION_USAGE](../sql-reference/organization-usage.md) schemas.
Snowsight allows you to quickly and easily obtain information about cost from a visual dashboard. Queries against the usage views
allow you to drill down into cost data and can help generate custom reports and dashboards.

To gain a better understanding of how storage costs are incurred, see [Understanding storage cost](cost-understanding-data-storage.md).

## Viewing the storage history

Users can use Snowsight to view the amount of data that is stored in Snowflake.

To explore storage costs:

1. Sign in to [Snowsight](ui-snowsight-gs.md).
2. Switch to a role with [access to cost-related features](cost-access-control.md).
3. In the navigation menu, select Admin » Cost management.
4. Select a warehouse to use to view the usage data. Snowflake recommends using an XS warehouse for this purpose.
5. Select Consumption.
6. Select Storage from the Usage Type drop-down.

For usage notes related to the Consumption page, see [Usage notes](cost-exploring-overall.md).

### Filter by tag

To help [attribute cost](cost-attributing.md) to a logical unit within your organization, you can filter the Usage
dashboard to show storage associated with a specific tag/value combination. This ability to filter storage by tag is similar to filtering
credit consumption by tag. For details, refer to [Exploring Compute Costs](cost-exploring-compute.md).

### View storage by type or object

When viewing the bar graph that displays storage history, you can filter the data either By Type or By Object.

Filtering By Type shows the size of storage for each storage type: Database, Fail Safe, and Stage. Storage
associated with Time Travel is included in the Database category.

Filtering By Object graphs the size of storage for each object, for example the size of a particular database or stage.

## Viewing data usage for a table

Users with the appropriate access privileges can use Snowsight to view the size (in bytes) of individual tables in a
schema/database:

To view the size of a table:

1. Sign in to [Snowsight](ui-snowsight-gs.md).
2. In the navigation menu, select Catalog » Database Explorer.
3. Expand a database, then any schema in the database.
4. Click on any table to view the table statistics, including its size.

> **Important:**
>
> The size displayed for a table represents the number of *active* bytes. In most cases, this is the number of bytes that will be scanned
> if the entire table is scanned in a query. However, this number might be different from the number of physical bytes (i.e. bytes stored
> on-disk) for the table, specifically for cloned tables and tables with deleted data:
>
> * A cloned table does not utilize additional storage (until rows are added to the table or existing rows in the table are modified or
>   deleted). As a result, the table size displayed may be larger
>   than the actual physical bytes stored for the table, i.e. the table contributes less to the overall storage for the account
>   than the size indicates.
> * Data deleted from a table is not included in the displayed table size; however, the data is maintained in Snowflake until both the
>   Time Travel retention period (default is 1 day) and the Fail-safe period (7 days) for the data has passed. During these two periods,
>   the table size displayed is smaller than the actual physical bytes stored for the table, i.e. the table contributes more
>   to the overall storage for the account than the size indicates.
> * Dropping a column from a table does not immediately delete the data in the column. The physical bytes for the data in the dropped
>   column remain in storage. In this case, the table size displayed is larger than the number of bytes that is scanned if the
>   entire table is scanned in a query. For more information, see the [usage notes](../sql-reference/sql/alter-table.md) for
>   ALTER TABLE.
>
> For more information about storage for cloned tables and deleted data, see [Data storage considerations](tables-storage-considerations.md).

## Querying data for table size

You can write SQL queries to gain insights into tables, including their size, instead of using the web interface.

A user with the proper access privileges can list data about tables using the [SHOW TABLES](../sql-reference/sql/show-tables.md) command.

In addition, users with the ACCOUNTADMIN role can use SQL to view table size information by executing queries against the
[TABLE_STORAGE_METRICS](../sql-reference/account-usage/table_storage_metrics.md) view in the ACCOUNT_USAGE schema.

For important information about interpreting the table data retrieved by these SQL queries, see the note in
Viewing data usage for a table (in this topic).

## Querying data for storage cost

Snowflake provides two schemas, [ORGANIZATION_USAGE](../sql-reference/organization-usage.md) and
[ACCOUNT_USAGE](../sql-reference/account-usage.md), that contain data related to usage and cost. The ORGANIZATION_USAGE schema provides
cost information for all of the accounts in the organization while the ACCOUNT_USAGE schema provides similar information for a single
account. Views in these schemas provide granular, analytics-ready usage data to build custom reports or dashboards.

Most views in the ORGANIZATION_USAGE and ACCOUNT_USAGE schemas contain the cost of storage in terms of the size of storage. To view cost
in currency rather than size, write queries against the [USAGE_IN_CURRENCY_DAILY view](../sql-reference/organization-usage/usage_in_currency_daily.md). This view
converts the size of storage into cost in currency using the daily price of a TB.

The following views provide usage and cost information related to storage.

| View | Description | Schema |
| --- | --- | --- |
| APPLICATION_DAILY_USAGE_HISTORY | Daily storage usage consumption for Snowflake Native Apps in an account within the last 365 days. | [ACCOUNT_USAGE](../sql-reference/account-usage/application_daily_usage_history.md) |
| DATABASE_STORAGE_USAGE_HISTORY | Daily storage in bytes for databases (including data in Time Travel), Fail-safe, and hybrid tables in the account/organization. | [ORGANIZATION_USAGE](../sql-reference/organization-usage/database_storage_usage_history.md) [ACCOUNT_USAGE](../sql-reference/account-usage/database_storage_usage_history.md) |
| HYBRID_TABLES | Data storage in bytes for each hybrid table row in the account. | [ACCOUNT_USAGE](../sql-reference/account-usage/hybrid_tables.md) |
| LISTING_AUTO_FULFILLMENT_DATABASE_STORAGE_DAILY | Data storage in bytes for databases fulfilled to other regions by Cross-Cloud Auto-Fulfillment. | [DATA_SHARING_USAGE](../sql-reference/data-sharing-usage/listing-auto-fulfillment-database-storage-daily.md) |
| LISTING_AUTO_FULFILLMENT_USAGE_HISTORY | Estimated usage associated with fulfilling data products to other regions by using Cross-Cloud Auto-Fulfillment. Refer to the SERVICE_TYPE of STORAGE. | [ORGANIZATION_USAGE](../sql-reference/organization-usage/listing_auto_fulfillment_usage_history.md) |
| POSTGRES_STORAGE_USAGE_HISTORY | Data storage in bytes for Snowflake Postgres instances. | [ACCOUNT_USAGE](../sql-reference/account-usage/postgres_storage_usage_history.md) |
| STORAGE_DAILY_HISTORY | Average daily storage for storage in bytes. Combines database storage (DATABASE_STORAGE_USAGE_HISTORY) and stage storage (STAGE_STORAGE_USAGE_HISTORY). | [ORGANIZATION_USAGE](../sql-reference/organization-usage/storage_daily_history.md) |
| STAGE_STORAGE_USAGE_HISTORY | Average daily storage usage, in bytes, for all the Snowflake stages including named internal stages and default staging areas. | [ORGANIZATION_USAGE](../sql-reference/organization-usage/stage_storage_usage_history.md) [ACCOUNT_USAGE](../sql-reference/account-usage/stage_storage_usage_history.md) |
| TABLE_STORAGE_METRICS | Storage in bytes for tables, including storage that is no longer active but continues to incur cost (e.g. deleted tables with the Time Travel retention period). | [ACCOUNT_USAGE](../sql-reference/account-usage/table_storage_metrics.md) |
| USAGE_IN_CURRENCY_DAILY | Daily average storage in bytes along with the cost of that usage in the organization’s currency. | [ORGANIZATION_USAGE](../sql-reference/organization-usage/usage_in_currency_daily.md) |

> **Note:**
>
> The views and table functions of the [Snowflake Information Schema](../sql-reference/info-schema.md) also provide usage data related to cost. Though
> the ACCOUNT_USAGE schema is preferred, the Information Schema can be faster in some circumstances.
