# Source: https://docs.snowflake.com/en/collaboration/views/marketplace-provider-spcs-usage-ds.md

Schema:
:   [Data Sharing Usage](../../sql-reference/data-sharing-usage.md)

# MARKETPLACE_PROVIDER_SPCS_USAGE View

The MARKETPLACE_PROVIDER_SPCS_USAGE view in the [Data Sharing Usage](../../sql-reference/data-sharing-usage.md) schema lets providers review their daily [Snowpark Container Services (SPCS) usage](../../developer-guide/snowpark-container-services/provider-pricing-surcharges.md). In this view, providers can see the number of compute pool hours and credits consumed by applications that the consumers purchased from the provider.

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| START_TIME | DATETIME | The date and beginning of the hour (in the local time zone) in which the usage took place. |
| END_TIME | DATETIME | The date and end of the hour (in the local time zone) in which the usage took place. |
| LISTING_NAME | VARCHAR | Identifier for the listing. |
| LISTING_DISPLAY_NAME | VARCHAR | Display name of the listing. |
| LISTING_GLOBAL_NAME | VARCHAR | Global name of the listing. |
| IDENTIFIER | VARCHAR | The compute pool name. |
| CONSUMER_ACCOUNT_NAME | VARCHAR | Account locator of the consumer account. For more information about account identifiers, see [Account identifiers](../../user-guide/admin-account-identifier.md). |
| CONSUMER_ACCOUNT_LOCATOR | VARCHAR | Account locator of the consumer account. |
| CONSUMER_ORGANIZATION_NAME | VARCHAR | Organization name for the consumer. |
| CREDITS | VARCHAR | Credits consumed by the compute pool. |
| COMPUTE_HOURS | VARCHAR | The number of hours consumed by the compute pool. |

## Usage notes

* Latency for the view can be up to 48 hours (2 days).
* The data is retained for 365 days (1 year).

## Examples

Retrieve the total number of SPCS compute pool hours consumed by each of your consumers.

```sqlexample
SELECT
  start_time,
  end_time,
  listing_name,
  listing_display_name,
  listing_global_name,
  identifier,
  consumer_account_name,
  consumer_account_locator,
  consumer_organization_name,
  credits,
  compute_hours,
FROM snowflake.data_sharing_usage.marketplace_provider_spcs_usage;
```
