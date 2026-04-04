# Source: https://docs.snowflake.com/en/sql-reference/data-sharing-usage/listing-auto-fulfillment-database-storage-daily.md

Schema:
:   [DATA_SHARING_USAGE](../data-sharing-usage.md)

# LISTING_AUTO_FULFILLMENT_DATABASE_STORAGE_DAILY view

This view in the DATA_SHARING_USAGE schema can be used to determine the data storage used by Cross-Cloud Auto-Fulfillment. When a listing
is fulfilled to another region, the data product is stored in the region. This view contains details about how much data is stored in
specific regions, and which listings and databases the data storage is associated with.

You can use this view to help manage the costs associated with Cross-Cloud Auto-Fulfillment.
See [Auto-fulfillment costs](../../collaboration/provider-understand-cost-auto-fulfillment.md).

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| REGION_GROUP | VARCHAR | [Region group](../../user-guide/admin-account-identifier.md) where the storage usage occurred. |
| SNOWFLAKE_REGION | VARCHAR | [Snowflake region](../../user-guide/admin-account-identifier.md) where the storage usage occurred. |
| USAGE_DATE | DATE | Date in UTC when the storage usage was recorded. |
| DATABASE_NAME | VARCHAR | Name of the database. |
| SOURCE_DATABASE_ID | NUMBER | Internal ID of the source database that contains the data product shared by the provider. |
| DELETED | TIMESTAMP | Time when the database was dropped. NULL for active databases. |
| AVERAGE_DATABASE_BYTES | FLOAT | Number of bytes of database storage used, including data in [Time Travel](../../user-guide/data-time-travel.md). |
| AVERAGE_FAILSAFE_BYTES | FLOAT | Number of bytes of [Fail-safe storage](../../user-guide/data-failsafe.md) used. |
| LISTINGS | ARRAY | List of listings that reference the database in this specific region. Returns an empty array until a listing is successfully fulfilled to a region. |

## Usage notes

* Latency for the view may be up to 2 days.
* The data is retained for 365 days (1 year).
* Stage storage is not included in this view.
* The view only contains data from 2023-04-16 onward.
* In cases where auto-fulfillment is incomplete, the array returned for the LISTINGS column might be empty.
* The view contains data for all data products, whether your data product is a Snowflake Native App or a share.

> **Important:**
>
> This view is intended to help you understand the resources used by Cross-Cloud Auto-Fulfillment. It is not intended to
> be used for billing reconciliation. Instead, refer to the views in the ORGANIZATION_USAGE schema. See
> [View actual costs](../../collaboration/provider-listings-auto-fulfillment-monitor-view-costs.md) for more details.

## Examples

Shows the average storage used in each Snowflake region over a specific time period, grouped by region and database:

```sqlexample
SELECT
   snowflake_region,
   database_name,
   listings,
   AVG(average_database_bytes) AS AVG_storage
FROM snowflake.data_sharing_usage.listing_auto_fulfillment_database_storage_daily
WHERE 1=1
   AND usage_date BETWEEN '2023-04-17' AND '2023-04-30'
GROUP BY 1,2,3
ORDER BY 4 DESC;
```
