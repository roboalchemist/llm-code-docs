# Source: https://docs.snowflake.com/en/sql-reference/billing/partner_usage_in_currency_daily.md

Schema:
:   [BILLING](../billing.md)

# PARTNER_USAGE_IN_CURRENCY_DAILY view

The PARTNER_USAGE_IN_CURRENCY_DAILY view in the BILLING schema provides the daily credit usage and daily currency usage for all of a
reseller’s customers.

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| ORGANIZATION_NAME | VARCHAR | Name of the reseller’s organization. |
| SOLD_TO_ORGANIZATION_NAME | VARCHAR | Name of the organization of the reseller’s customer. |
| SOLD_TO_CUSTOMER_NAME | VARCHAR | Name of the reseller’s customer. |
| SOLD_TO_PO_NUMBER | VARCHAR | Purchase order number associated with the reseller’s sale to the customer (if available). |
| SOLD_TO_CONTRACT_NUMBER | VARCHAR | Number associated with the customer’s contract with the reseller. |
| ACCOUNT_NAME | VARCHAR | Name of the account where the usage was consumed. |
| ACCOUNT_LOCATOR | VARCHAR | Locator for the account where the usage was consumed. The locator is used in the [legacy account identifier](../../user-guide/admin-account-identifier.md). |
| REGION | VARCHAR | Name of the region where the account is located. |
| SERVICE_LEVEL | VARCHAR | Service level of the Snowflake account (Standard, Enterprise, Business Critical, etc.). |
| USAGE_DATE | DATE | Date (in UTC) in which the usage took place. |
| USAGE_TYPE | VARCHAR | Type of usage. For each usage type, `overage` is prepended when the usage was billed at on-demand pricing because it exceeded the capacity of the contract. Possible usage types include:  *`adj for incl cloud services` — Refer to [Understanding billing for cloud services usage](../../user-guide/cost-understanding-compute.md).* `automatic clustering` — Refer to [Automatic Clustering](../../user-guide/tables-auto-reclustering.md). *`cloud services` — Refer to [Cloud service credit usage](../../user-guide/cost-understanding-compute.md).* `compute` — Refer to [Virtual warehouse credit usage](../../user-guide/cost-understanding-compute.md). Does not indicate usage of serverless or cloud services compute. *`data transfer` — Refer to [Understanding data transfer cost](../../user-guide/cost-understanding-data-transfer.md).* `materialized views` — Refer to [Working with Materialized Views](../../user-guide/views-materialized.md). *`priority support` — Indicates how much was charged for priority support services in a given month. This charge is associated with a stipulation in a contract, not with an account.* `serverless tasks` — Refer to [Introduction to tasks](../../user-guide/tasks-intro.md). *`snowpipe` — Refer to [Snowpipe](../../user-guide/data-load-snowpipe-intro.md).* `snowpipe streaming` — Refer to [Snowpipe Streaming](../../user-guide/snowpipe-streaming/data-load-snowpipe-streaming-overview.md). *`storage` — Refer to [Understanding storage cost](../../user-guide/cost-understanding-data-storage.md).* `support credit` — Indicates that Snowflake Support credited the account to reverse charges attributed to an issue in Snowflake. Represents credits applied to the account for a given month. |
| CURRENCY | VARCHAR | Currency associated with the usage. |
| USAGE | NUMBER (38,6) | Total number of credits charged for the USAGE_TYPE for usage on the USAGE_DATE. |
| USAGE_IN_CURRENCY | NUMBER (38,6) | Total amount charged for the USAGE_TYPE for USAGE on the USAGE_DATE. |
| BALANCE_SOURCE | VARCHAR | Source of the funds used to pay for the daily usage. Can be one of the following:   *`capacity` — Usage paid with credits remaining on an organization’s capacity contract.* `rollover` — Usage paid with rollover credits. When an organization renews a capacity contract, unused credits are added to the   balance of the new contract as rollover credits. *`free usage` — Usage covered by the free credits provided to the organization.* `overage` — Usage that was paid at on-demand pricing, which occurs when an organization has exhausted its capacity, rollover,   and free credits. * `rebate` — Usage covered by the credits awarded to the organization of the reseller’s customer when it shared data with another   organization. |
| BILLING_TYPE | VARCHAR | Indicates what is being charged or credited. Possible billing types include:   *`consumption` — Usage associated with compute credits, storage costs, and data transfer costs.* `rebate` — Usage covered by the credits awarded to the organization when it shared data with another organization. *`priority support` — Charges for priority support services. This charge is associated with a stipulation in a contract, not with an account.* `vps_deployment_fee` — Charges for a [Virtual Private Snowflake](../../user-guide/intro-editions.md) deployment. * `support_credit` — Snowflake Support credited the account to reverse charges attributed to an issue in Snowflake. |
| RATING_TYPE | VARCHAR | Indicates how the usage in the record is rated, or priced. Possible values include:   *`compute`* `data_transfer` *`storage`* `other` |
| SERVICE_TYPE | VARCHAR | Type of usage. The following list includes many, but not all, of the possible service types:   *`ARCHIVE_STORAGE_RETRIEVAL_FILE_PROCESSING` — See [Billing for storage lifecycle policies](../../user-guide/storage-management/storage-lifecycle-policies-billing.md).* `ARCHIVE_STORAGE_WRITE` — See [Billing for storage lifecycle policies](../../user-guide/storage-management/storage-lifecycle-policies-billing.md). *`AUTOMATIC_CLUSTERING` — See [Automatic Clustering](../../user-guide/tables-auto-reclustering.md).* `CLOUD_SERVICES` — See [Cloud service credit usage](../../user-guide/cost-understanding-compute.md). *`COPY_FILES` — See [COPY FILES](../sql/copy-files.md).* `DATA_TRANSFER` — See [Understanding data transfer cost](../../user-guide/cost-understanding-data-transfer.md). *`EGRESS_COST_OPTIMIZER` — See [Optimizing data transfer costs with Egress Cost Optimizer](../../collaboration/provider-listings-auto-fulfillment-eco.md).* `INTERNAL_DATA_TRANSFER` — See costs associated with [Snowpark Container Services](../../developer-guide/snowpark-container-services/accounts-orgs-usage-views.md). *`LOGGING` — See [Logging, tracing, and metrics](../../developer-guide/logging-tracing/logging-tracing-overview.md).* `MATERIALIZED_VIEW` — See [Working with Materialized Views](../../user-guide/views-materialized.md). *`OUTBOUND_PRIVATELINK_DATA_PROCESSED` — See [Private connectivity for outbound network traffic](../../user-guide/private-connectivity-outbound.md).* `OUTBOUND_PRIVATELINK_ENDPOINTS` — See [Private connectivity for outbound network traffic](../../user-guide/private-connectivity-outbound.md). *`REPLICATION` — See [Introduction to replication and failover across multiple accounts](../../user-guide/account-replication-intro.md).* `QUERY_ACCELERATION` — See [Using the Query Acceleration Service (QAS)](../../user-guide/query-acceleration-service.md) *`SEARCH_OPTIMIZATION` — See [Search optimization service](../../user-guide/search-optimization-service.md)* `SENSITIVE_DATA_CLASSIFICATION` — See [Introduction to sensitive data classification](../../user-guide/classify-intro.md). *`SERVERLESS_ALERTS` — See [Setting up alerts based on data in Snowflake](../../user-guide/alerts.md).* `SERVERLESS_TASK` — See [Introduction to tasks](../../user-guide/tasks-intro.md). *`SNOWPIPE` — See [Snowpipe](../../user-guide/data-load-snowpipe-intro.md).* `SNOWPIPE_STREAMING` — See [Snowpipe Streaming](../../user-guide/snowpipe-streaming/data-load-snowpipe-streaming-overview.md). *`STORAGE` — See [Understanding storage cost](../../user-guide/cost-understanding-data-storage.md).* `STORAGE_LIFECYCLE_POLICY_EXECUTION` — See [Billing for storage lifecycle policies](../../user-guide/storage-management/storage-lifecycle-policies-billing.md). *`TRUST_CENTER` — See [Trust Center](../../user-guide/trust-center/overview.md).* `WAREHOUSE_METERING` — See [Virtual warehouse credit usage](../../user-guide/cost-understanding-compute.md). Does not indicate usage of serverless or cloud services compute. |
| IS_ADJUSTMENT | BOOLEAN | Indicates whether the record is an adjustment to usage. |

## Usage notes

* Latency for the view can be up to 24 hours.
* Until month close, data for a given day in a month can change to account for any end-of-month adjustments, contract amendments, or Snowflake account transfers between organizations.

## Example query

To query the usage in credits and currency for all Snowflake accounts under your customers’ organizations for the month of January 2022:

```sqlexample
SELECT * FROM snowflake.billing.partner_usage_in_currency_daily
  WHERE MONTH(usage_date) = 01
    AND YEAR(usage_date) = 2022
  ORDER BY sold_to_contract_number, usage_date ASC;
```
