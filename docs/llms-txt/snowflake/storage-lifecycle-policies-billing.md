# Source: https://docs.snowflake.com/en/user-guide/storage-management/storage-lifecycle-policies-billing.md

# Billing for storage lifecycle policies

When you use storage lifecycle policies, you incur costs for policy execution, data storage, and data operations.
This topic explains the cost components associated with storage lifecycle policies and provides
guidance on how to monitor each component.

## Policy execution costs

Each time Snowflake runs a storage lifecycle policy, you incur serverless compute charges to identify and process rows that
meet your defined conditions. Policies run automatically, approximately once every 24-hour period.
For billing details, see table 5 in the [Snowflake Service Consumption Table](https://www.snowflake.com/legal-files/CreditConsumptionTable.pdf).

### Monitoring

To view credits that are consumed by policy execution, use the following metering history views.
Filter for the STORAGE_LIFECYCLE_POLICY_EXECUTION service type:

* [ACCOUNT_USAGE.METERING_DAILY_HISTORY](../../sql-reference/account-usage/metering_daily_history.md)
* [ACCOUNT_USAGE.METERING_HISTORY](../../sql-reference/account-usage/metering_history.md)
* [ORGANIZATION_USAGE.METERING_DAILY_HISTORY](../../sql-reference/organization-usage/metering_daily_history.md)

To view policy execution history and metadata, use the following views and function:

* [ACCOUNT_USAGE.STORAGE_LIFECYCLE_POLICY_HISTORY](../../sql-reference/account-usage/storage_lifecycle_policy_history.md)
* [ORGANIZATION_USAGE.STORAGE_LIFECYCLE_POLICY_HISTORY](../../sql-reference/organization-usage/storage_lifecycle_policy_history.md)
* [INFORMATION_SCHEMA.STORAGE_LIFECYCLE_POLICY_HISTORY](../../sql-reference/functions/storage_lifecycle_policy_history.md) (table function)

> **Note:**
>
> Policy execution times can vary from execution to execution, even when processing similar amounts of data. To better understand
> the cost of policy executions, monitor the credits charged for each execution along with the amount of data expired or archived.

## Archive storage costs

When you archive data, you incur charges for moving data to archive storage,
storing data in archive storage, and
retrieving archived data. If you drop a table with archived data,
you might also incur minimum storage duration charges.

### Moving data to archive storage

When a policy archives data, you incur a one-time serverless compute charge to move data from regular storage to the
cool or cold archive storage tier. For billing details, see table 5 in the [Snowflake Service Consumption Table](https://www.snowflake.com/legal-files/CreditConsumptionTable.pdf).

#### Monitoring

To view the credits consumed to move data to archive storage, use the following metering history views.
Filter for the STORAGE_LIFECYCLE_POLICY_EXECUTION and ARCHIVE_STORAGE_WRITE service types:

* [ACCOUNT_USAGE.METERING_DAILY_HISTORY](../../sql-reference/account-usage/metering_daily_history.md)
* [ACCOUNT_USAGE.METERING_HISTORY](../../sql-reference/account-usage/metering_history.md)
* [ORGANIZATION_USAGE.METERING_DAILY_HISTORY](../../sql-reference/organization-usage/metering_daily_history.md)

### Data storage

After policy execution, you temporarily incur charges for *both* archive storage and [table storage](../cost-exploring-data-storage.md).
Snowflake immediately copies data into the specified archive storage tier when the policy runs. However, the data remains in
table storage for seven or more days, which is the 7-day [Fail-safe](../data-failsafe.md) period plus your
[Time Travel](../data-time-travel.md) retention period set by DATA_RETENTION_TIME_IN_DAYS.

After this period, data in archive storage incurs ongoing storage charges.
For billing details, see table 3(e) in the [Snowflake Service Consumption Table](https://www.snowflake.com/legal-files/CreditConsumptionTable.pdf).

#### Monitoring

To view the volume of archived data in bytes for a table, database, or for your account, use the following views:

**Account Usage views:**

* [ACCOUNT_USAGE.TABLE_STORAGE_METRICS](../../sql-reference/account-usage/table_storage_metrics.md)
* [ACCOUNT_USAGE.TABLES](../../sql-reference/account-usage/tables.md)
* [ACCOUNT_USAGE.DATABASE_STORAGE_USAGE_HISTORY](../../sql-reference/account-usage/database_storage_usage_history.md)
* [ACCOUNT_USAGE.STORAGE_USAGE](../../sql-reference/account-usage/storage_usage.md)

**Organization Usage views:**

* [ORGANIZATION_USAGE.TABLE_STORAGE_METRICS](../../sql-reference/organization-usage/table_storage_metrics.md)
* [ORGANIZATION_USAGE.TABLES](../../sql-reference/organization-usage/tables.md)
* [ORGANIZATION_USAGE.DATABASE_STORAGE_USAGE_HISTORY](../../sql-reference/organization-usage/database_storage_usage_history.md)

### Data retrieval

When you query [retrieve archived data](storage-lifecycle-policies-retrieving-archived-data.md),
you incur the following charges:

* **Retrieval cost**: One-time charge to retrieve archived data from the archive storage tier.
* **File processing**: Serverless compute charge to process the retrieved data.
* **Temporary storage** (COLD tier only): When you retrieve data from the COLD tier, Snowflake temporarily stores the
  retrieved data in normal storage. This incurs additional storage charges.

For billing details, see tables 4(f) and 5 in the [Snowflake Service Consumption Table](https://www.snowflake.com/legal-files/CreditConsumptionTable.pdf).

> **Note:**
>
> To estimate retrieval cost, use [EXPLAIN](../../sql-reference/sql/explain.md) with
> [CREATE TABLE … FROM ARCHIVE OF](../../sql-reference/sql/create-table.md). This shows the number of files that
> will be retrieved from archive storage. For an example, see [Retrieve archived data](storage-lifecycle-policies-retrieving-archived-data.md).

#### Monitoring

To view consumed credits and the cost related to retrieving archived data, use the following views:

* [ACCOUNT_USAGE.ARCHIVE_STORAGE_DATA_RETRIEVAL_USAGE_HISTORY](../../sql-reference/account-usage/archive_storage_data_retrieval_usage_history.md)

To view the credits consumed for file processing in order to retrieve archived data, use the following metering history views.
Filter for the ARCHIVE_STORAGE_RETRIEVAL_FILE_PROCESSING service type:

* [ACCOUNT_USAGE.METERING_DAILY_HISTORY](../../sql-reference/account-usage/metering_daily_history.md)
* [ACCOUNT_USAGE.METERING_HISTORY](../../sql-reference/account-usage/metering_history.md)
* [ORGANIZATION_USAGE.METERING_DAILY_HISTORY](../../sql-reference/organization-usage/metering_daily_history.md)

To view temporary storage that you use when you retreive data from the COLD storage tier,
use the ARCHIVE_STORAGE_RETRIEVAL_TEMP_BYTES column in the
[ACCOUNT_USAGE.STORAGE_USAGE](../../sql-reference/account-usage/storage_usage.md).

### Minimum storage duration charges

Cloud providers impose a minimum storage duration for archive storage tiers. When you drop a table, Snowflake
deletes the table data from storage. If the table data is in archive storage and hasn’t been there for
the minimum duration set by the cloud provider, Snowflake charges you for the minimum duration.

For example, if you drop a table with data that Snowflake moved to the AWS cold storage tier 15 days ago, you still
incur storage cost for the remaining 165 days of the minimum cold storage period, which is the 180-day minimum minus 15 days already stored.

For archive storage billing details, see table 3(e) in the [Snowflake Service Consumption Table](https://www.snowflake.com/legal-files/CreditConsumptionTable.pdf).

The minimum storage duration varies by cloud provider and storage tier:

* **COOL tier**: 90-day minimum
* **COLD tier**: 180-day minimum

#### Monitoring

To view the amount of data that is subject to minimum storage duration charges for a table, use the following columns
in the TABLE_STORAGE_METRICS view:

* ARCHIVE_STORAGE_COOL_EARLY_DELETION_PENALTY_BYTES
* ARCHIVE_STORAGE_COLD_EARLY_DELETION_PENALTY_BYTES

These columns are available in the following topics:

* [ACCOUNT_USAGE.TABLE_STORAGE_METRICS](../../sql-reference/account-usage/table_storage_metrics.md)
* [ORGANIZATION_USAGE.TABLE_STORAGE_METRICS](../../sql-reference/organization-usage/table_storage_metrics.md)
