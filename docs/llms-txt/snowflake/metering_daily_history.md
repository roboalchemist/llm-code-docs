# Source: https://docs.snowflake.com/en/sql-reference/organization-usage/metering_daily_history.md

# Source: https://docs.snowflake.com/en/sql-reference/account-usage/metering_daily_history.md

Schema:
:   [ACCOUNT_USAGE](../account-usage.md)

# METERING_DAILY_HISTORY view

The METERING_DAILY_HISTORY view in the ACCOUNT_USAGE schema can be used to return the daily credit usage and a cloud services rebate for an account within the last 365 days (1 year).

> **Note:**
>
> As of March 1, 2026, Snowflake no longer bills customers for hybrid table requests;
> however, you can still query this view to see historical consumption data.
> Any new data in the view as of March 1, 2026, will not be billed to customers.

## Columns

| Column Name | Data Type | Description |
| --- | --- | --- |
| SERVICE_TYPE | VARCHAR | Type of service that is consuming credits. The following list includes many, **but not all**, of the possible service types:   *`AI_SERVICES`: See [Snowflake Cortex AI Functions (including LLM functions)](../../user-guide/snowflake-cortex/aisql.md), [Cortex Analyst](../../user-guide/snowflake-cortex/cortex-analyst.md), and [Document AI](../../user-guide/snowflake-cortex/document-ai/overview.md).* `ARCHIVE_STORAGE_RETRIEVAL_FILE_PROCESSING`: See [Billing for storage lifecycle policies](../../user-guide/storage-management/storage-lifecycle-policies-billing.md). *`ARCHIVE_STORAGE_WRITE`: See [Billing for storage lifecycle policies](../../user-guide/storage-management/storage-lifecycle-policies-billing.md).* `AUTO_CLUSTERING`: See [Automatic Clustering](../../user-guide/tables-auto-reclustering.md). *`BACKUP`: See [Backups for disaster recovery and immutable storage](../../user-guide/backups.md).* `COPY_FILES`: See [COPY FILES](../sql/copy-files.md). *`DATA_QUALITY_MONITORING`: See [Introduction to data quality checks](../../user-guide/data-quality-intro.md).* `FAILSAFE_RECOVERY`: See [Understanding and viewing Fail-safe](../../user-guide/data-failsafe.md). *`HYBRID_TABLE_REQUESTS`: See [Hybrid tables](../../user-guide/tables-hybrid.md).* `MATERIALIZED_VIEW`: See [Working with Materialized Views](../../user-guide/views-materialized.md). *`OPENFLOW_COMPUTE_BYOC`: See [Openflow BYOC cost and scaling considerations](../../user-guide/data-integration/openflow/cost-byoc.md).* `OPENFLOW_COMPUTE_SNOWFLAKE`: See [Openflow Snowflake Deployment cost and scaling considerations](../../user-guide/data-integration/openflow/cost-spcs.md). *`PIPE`: See [Snowpipe](../../user-guide/data-load-snowpipe-intro.md).* `POSTGRES_COMPUTE`: See [Snowflake Postgres](../../user-guide/snowflake-postgres/about.md). *`POSTGRES_COMPUTE_HA`: See [Snowflake Postgres](../../user-guide/snowflake-postgres/about.md).* `QUERY_ACCELERATION`: See [Using the Query Acceleration Service (QAS)](../../user-guide/query-acceleration-service.md). *`REPLICATION`: See [Introduction to replication and failover across multiple accounts](../../user-guide/account-replication-intro.md).* `SEARCH_OPTIMIZATION`: See [Search optimization service](../../user-guide/search-optimization-service.md). *`SENSITIVE_DATA_CLASSIFICATION`: See [Introduction to sensitive data classification](../../user-guide/classify-intro.md).* `SERVERLESS_ALERTS`: See [Setting up alerts based on data in Snowflake](../../user-guide/alerts.md). *`SERVERLESS_TASK`: See [Introduction to tasks](../../user-guide/tasks-intro.md).* `SNOWPARK_CONTAINER_SERVICES`: See [Snowpark Container Services](../../developer-guide/snowpark-container-services/overview.md). *`SNOWPIPE_STREAMING`: See [Snowpipe Streaming](../../user-guide/snowpipe-streaming/data-load-snowpipe-streaming-overview.md).* `STORAGE_LIFECYCLE_POLICY_EXECUTION`: Compute cost to apply a policy on a target table and expire or archive rows (policy execution). See [Storage lifecycle policies](../../user-guide/storage-management/storage-lifecycle-policies.md). *`TELEMETRY_DATA_INGEST`: See [Event table overview](../../developer-guide/logging-tracing/event-table-setting-up.md).* `TRUST_CENTER`: See [Trust Center](../../user-guide/trust-center/overview.md). *`WAREHOUSE_METERING`: See [Overview of warehouses](../../user-guide/warehouses-overview.md).* `WAREHOUSE_METERING_READER`: See [Manage reader accounts](../../user-guide/data-sharing-reader-create.md). |
| USAGE_DATE | DATE | Date when the usage took place. |
| CREDITS_USED_COMPUTE | NUMBER | Number of credits billed for warehouses, serverless compute, and [Openflow](../../user-guide/data-integration/openflow/about.md) resources in the day. |
| CREDITS_USED_CLOUD_SERVICES | NUMBER | Number of credits billed for cloud services in the day. Always `0` when the SERVICE_TYPE is one of the Openflow types. |
| CREDITS_USED | NUMBER | Sum of CREDITS_USED_COMPUTE and CREDITS_USED_CLOUD_SERVICES. |
| CREDITS_ADJUSTMENT_CLOUD_SERVICES | NUMBER | Number of credits [adjusted for cloud services](../../user-guide/cost-understanding-compute.md). This is a negative value (e.g. `-9`). |
| CREDITS_BILLED | NUMBER | Total number of credits billed for the account in the day. This is a sum of CREDITS_USED_COMPUTE, CREDITS_USED_CLOUD_SERVICES, and CREDITS_ADJUSTMENT_CLOUD_SERVICES. |

## Usage notes

* Latency for the view may be up to 180 minutes (3 hours).
* If you want to reconcile the data in this view with a corresponding view in the [ORGANIZATION USAGE schema](../organization-usage.md), you must first set the timezone of the session to UTC. Before querying the Account Usage view, execute:

  > ```sqlexample
  > ALTER SESSION SET TIMEZONE = UTC;
  > ```

## Example

[Usage for cloud services](../../user-guide/cost-understanding-compute.md) is billed only if the daily consumption of cloud
services exceeds 10% of the daily usage of virtual warehouses. This query returns how much of cloud services consumption was actually
billed for a particular day, ordered by the highest billed amount.

```sqlexample
SELECT
    usage_date,
    credits_used_cloud_services,
    credits_adjustment_cloud_services,
    credits_used_cloud_services + credits_adjustment_cloud_services AS billed_cloud_services
FROM snowflake.account_usage.metering_daily_history
WHERE usage_date >= DATEADD(month,-1,CURRENT_TIMESTAMP())
    AND credits_used_cloud_services > 0
ORDER BY 4 DESC;
```
