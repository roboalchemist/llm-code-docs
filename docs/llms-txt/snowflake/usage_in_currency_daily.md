# Source: https://docs.snowflake.com/en/sql-reference/organization-usage/usage_in_currency_daily.md

Schema:
:   [ORGANIZATION_USAGE](../organization-usage.md)

# USAGE_IN_CURRENCY_DAILY view

The USAGE_IN_CURRENCY_DAILY view in the ORGANIZATION_USAGE schema can be used to return the daily credit usage and usage in currency for
an organization.

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| ORGANIZATION_NAME | VARCHAR | Name of the organization. |
| CONTRACT_NUMBER | VARCHAR | Snowflake contract number for the organization. |
| ACCOUNT_NAME | VARCHAR | Name of the account where the usage was consumed. |
| ACCOUNT_LOCATOR | VARCHAR | Locator for the account where the usage was consumed. |
| REGION | VARCHAR | Name of the region where the account is located. |
| SERVICE_LEVEL | VARCHAR | Service level (edition) of the Snowflake account (Standard, Enterprise, Business Critical, etc.). |
| USAGE_DATE | DATE | Date (in UTC format) in which the usage took place. |
| USAGE_TYPE | VARCHAR | Corresponds to the Usage Category column in a billing statement, which exists for backward compatibility only. Use the BILLING_TYPE, RATING_TYPE, SERVICE_TYPE, and IS_ADJUSTMENT columns for billing reconciliation. |
| USAGE | NUMBER (38,3) | Total amount of usage charged based on SERVICE_TYPE. The unit of the USAGE depends on the RATING_TYPE. For example, when the RATING_TYPE is `compute`, USAGE is measured in credits. When the RATING_TYPE is `data transfer` or `storage`, the usage is rated in terabytes. |
| CURRENCY | VARCHAR | Currency of the usage. |
| USAGE_IN_CURRENCY | NUMBER (38,2) | Total amount charged for the USAGE_TYPE for USAGE on the USAGE_DATE. |
| BALANCE_SOURCE | VARCHAR | Source of the funds used to pay for the daily usage. The source can be one of the following:   *`capacity` — Usage paid with credits remaining on an organization’s capacity commitment.* `rollover` — Usage paid with rollover credits. When an organization renews a capacity commitment, unused credits are added to the   balance of the new contract as rollover credits. *`free usage` — Usage covered by the free credits provided to the organization.* `overage` — Usage that was paid at on-demand pricing, which occurs when an organization has exhausted its capacity, rollover,   and free credits. * `rebate` — Usage covered by the credits awarded to the organization when it shared data with another organization. |
| BILLING_TYPE | VARCHAR | Indicates what is being charged or credited. Possible billing types include:   *`consumption` — Usage associated with compute credits, storage costs, and data transfer costs.* `rebate` — Usage covered by the credits awarded to the organization when it shared data with another organization. *`priority support` — Charges for priority support services. This charge is associated with a stipulation in a contract, not with an account.* `vps_deployment_fee` — Charges for a [Virtual Private Snowflake](../../user-guide/intro-editions.md) deployment. * `support_credit` — Snowflake Support credited the account to reverse charges attributed to an issue in Snowflake. |
| RATING_TYPE | VARCHAR | Indicates how the usage in the record is rated, or priced. Possible values include:   *`compute`* `data_transfer` *`storage`* `other` |
| SERVICE_TYPE | VARCHAR | Type of usage. The following list includes many, but not all, of the possible service types:   *`ARCHIVE_STORAGE_RETRIEVAL_FILE_PROCESSING` — See [Billing for storage lifecycle policies](../../user-guide/storage-management/storage-lifecycle-policies-billing.md).* `ARCHIVE_STORAGE_WRITE` — See [Billing for storage lifecycle policies](../../user-guide/storage-management/storage-lifecycle-policies-billing.md). *`AUTOMATIC_CLUSTERING` — See [Automatic Clustering](../../user-guide/tables-auto-reclustering.md).* `CLOUD_SERVICES` — See [Cloud service credit usage](../../user-guide/cost-understanding-compute.md). *`COPY_FILES` — See [COPY FILES](../sql/copy-files.md).* `DATA_TRANSFER` — See [Understanding data transfer cost](../../user-guide/cost-understanding-data-transfer.md). *`EGRESS_COST_OPTIMIZER` — See [Optimizing data transfer costs with Egress Cost Optimizer](../../collaboration/provider-listings-auto-fulfillment-eco.md).* `INTERNAL_DATA_TRANSFER` — See costs associated with [Snowpark Container Services](../../developer-guide/snowpark-container-services/accounts-orgs-usage-views.md). *`LOGGING` — See [Logging, tracing, and metrics](../../developer-guide/logging-tracing/logging-tracing-overview.md).* `MATERIALIZED_VIEW` — See [Working with Materialized Views](../../user-guide/views-materialized.md). *`OUTBOUND_PRIVATELINK_DATA_PROCESSED` — See [Private connectivity for outbound network traffic](../../user-guide/private-connectivity-outbound.md).* `OUTBOUND_PRIVATELINK_ENDPOINTS` — See [Private connectivity for outbound network traffic](../../user-guide/private-connectivity-outbound.md). *`REPLICATION` — See [Introduction to replication and failover across multiple accounts](../../user-guide/account-replication-intro.md).* `QUERY_ACCELERATION` — See [Using the Query Acceleration Service (QAS)](../../user-guide/query-acceleration-service.md) *`SEARCH_OPTIMIZATION` — See [Search optimization service](../../user-guide/search-optimization-service.md)* `SENSITIVE_DATA_CLASSIFICATION` — See [Introduction to sensitive data classification](../../user-guide/classify-intro.md). *`SERVERLESS_ALERTS` — See [Setting up alerts based on data in Snowflake](../../user-guide/alerts.md).* `SERVERLESS_TASK` — See [Introduction to tasks](../../user-guide/tasks-intro.md). *`SNOWPIPE` — See [Snowpipe](../../user-guide/data-load-snowpipe-intro.md).* `SNOWPIPE_STREAMING` — See [Snowpipe Streaming](../../user-guide/snowpipe-streaming/data-load-snowpipe-streaming-overview.md). *`STORAGE` — See [Understanding storage cost](../../user-guide/cost-understanding-data-storage.md).* `STORAGE_LIFECYCLE_POLICY_EXECUTION` — See [Billing for storage lifecycle policies](../../user-guide/storage-management/storage-lifecycle-policies-billing.md). *`TRUST_CENTER` — See [Trust Center](../../user-guide/trust-center/overview.md).* `WAREHOUSE_METERING` — See [Virtual warehouse credit usage](../../user-guide/cost-understanding-compute.md). Does not indicate usage of serverless or cloud services compute. |
| IS_ADJUSTMENT | BOOLEAN | Indicates whether the record is an adjustment to usage. |

## Usage notes

* Latency for the view may be up to 72 hours.
* Until month close, data for a given day in a month can change to account for any end-of-month adjustments/credits, contract amendments,
  or Snowflake account transfers between organizations.
* Customers who signed a contract through a Snowflake reseller cannot access data in this view.
* Data is retained indefinitely.
* This view does not include data generated prior to June 2020. To obtain data before this date, contact [Snowflake Support](https://docs.snowflake.com/user-guide/contacting-support).
