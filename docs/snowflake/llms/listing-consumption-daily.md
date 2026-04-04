# Source: https://docs.snowflake.com/en/sql-reference/data-sharing-usage/listing-consumption-daily.md

Schema:
:   [DATA_SHARING_USAGE](../data-sharing-usage.md)

# LISTING_CONSUMPTION_DAILY view

This view in the DATA_SHARING_USAGE schema can be used to analyze consumption of a Snowflake Native App or shared data associated with listings
in a data exchange, such as the Snowflake Marketplace. The view returns a record for each consumer account that queried data for a given date.

## Columns

LISTING_CONSUMPTION_DAILY

| Field | Type | Description |
| --- | --- | --- |
| EVENT_DATE | DATETIME | Date of the consumption. |
| EXCHANGE_NAME | VARCHAR | Name of the data exchange or the Snowflake Marketplace to which the listing belongs. |
| SNOWFLAKE_REGION | VARCHAR | Snowflake Region where the consumption occurred. |
| LISTING_NAME | VARCHAR | Identifier for the listing. |
| LISTING_DISPLAY_NAME | VARCHAR | Display name of the listing. |
| LISTING_GLOBAL_NAME | VARCHAR | Global name of the listing. Unique for each listing and is used to create the listing URL. |
| PROVIDER_ACCOUNT_LOCATOR | VARCHAR | Account locator of the data product owner. |
| PROVIDER_ACCOUNT_NAME | VARCHAR | Account name of the data product owner. |
| SHARE_NAME | VARCHAR | Share name. If your data product is a Snowflake Native App, this is NULL. |
| CONSUMER_ACCOUNT_LOCATOR | VARCHAR | Account locator name of the consumer. |
| CONSUMER_ACCOUNT_NAME | VARCHAR | Account name of the consumer. |
| CONSUMER_ORGANIZATION | VARCHAR | Organization name of the consumer. |
| JOBS | NUMBER | Total jobs run that day on the data product. A job is recorded when a consumer query resolves objects included in the data share or Snowflake Native App attached to the listing. |
| REGION_GROUP | VARCHAR | [Region group](../../user-guide/admin-account-identifier.md) where the account of the consumer is located. |
| CONSUMER_NAME | VARCHAR | Contains the company name of the consumer account that accessed, used, or requested a listing. If no name is available, such as for trial accounts, the value is NULL. |
| UNIQUE_USERS_1D | NUMBER | Count of unique users (within the consumer account) who had jobs running on the date of consumption (EVENT_DATE). |
| UNIQUE_USERS_7D | NUMBER | Count of unique users (within the consumer account) who had jobs running within the 7-day period ending on the date of consumption (EVENT_DATE). |
| UNIQUE_USERS_28D | NUMBER | Count of unique users (within the consumer account) who had jobs running within the 28-day period ending on the date of consumption (EVENT_DATE). |

## Usage notes

* Latency for the view may be up to 2 days.
* The data is retained for 365 days (1 year).
* The view contains data for all data products, whether your data product is a Snowflake Native App or a share.

## Examples

Shows top listings by consumption for a given time period:

```sqlexample
 SELECT
   listing_name,
   listing_display_name,
   SUM(jobs) AS jobs
FROM snowflake.data_sharing_usage.listing_consumption_daily
WHERE 1=1
   AND event_date BETWEEN '2021-01-01' AND '2021-01-31'
GROUP BY 1,2
ORDER BY 3 DESC
```

Shows top consumers by listing:

```sqlexample
SELECT
  *,
  ROW_NUMBER() OVER (PARTITION BY listing_name, listing_display_name ORDER BY jobs DESC) AS rank
FROM (
  SELECT
    listing_name,
    listing_display_name,
    consumer_account_locator,
    SUM(jobs) AS jobs
  FROM snowflake.data_sharing_usage.listing_consumption_daily
  WHERE 1=1
    AND event_date BETWEEN '2021-01-01' AND '2021-01-31'
  GROUP BY 1,2,3
)
ORDER BY
  listing_name,
  listing_display_name,
  rank
```
