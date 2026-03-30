# Source: https://docs.snowflake.com/en/developer-guide/snowpark-container-services/accounts-orgs-usage-views.md

# Snowpark Container Services costs

The costs associated with using Snowpark Container Services can be categorized into storage cost, compute pool cost, and data
transfer cost.

## Storage cost

When you use Snowpark Container Services, storage costs associated with Snowflake, including the cost of Snowflake stage usage
or database table storage, apply. For more information, see [Exploring storage cost](../../user-guide/cost-exploring-data-storage.md). In addition, the
following cost considerations apply:

* **Image repository storage cost:** The implementation of the [image repository](working-with-registry-repository.md) uses
  a Snowflake stage. Therefore, the associated cost for using the Snowflake stage applies.
* **Log storage cost:** When you store
  [local container logs in event tables](monitoring-services.md), event table storage
  costs apply.
* **Mounting volumes cost:**

  * When you mount a Snowflake stage as a volume, the cost of using the Snowflake stage applies.
  * When you mount storage from the compute pool node as a volume, it appears as local storage in the container. But there is no
    additional cost because the local storage cost is covered by the cost of the compute pool node.
* **Block storage cost:** When you create a service that uses [block storage](block-storage-volume.md), you are billed for block storage and snapshot storage. For more information about storage pricing, see the [Snowflake Service Consumption Table](https://www.snowflake.com/legal-files/CreditConsumptionTable.pdf). The SPCS Block Storage Pricing table in this document provides the information.

## Compute pool cost

A [compute pool](working-with-compute-pool.md) is a collection of one or more virtual machine (VM) nodes on which Snowflake
runs your Snowpark Container Services jobs and services. The number and type (instance family) of the nodes in the compute pool
(see [CREATE COMPUTE POOL](../../sql-reference/sql/create-compute-pool.md)) determine the credits it consumes and thus the cost you pay. For more information, see the [Snowflake Service Consumption Table](https://www.snowflake.com/legal-files/CreditConsumptionTable.pdf).

You incur charges for a compute pool in the IDLE, ACTIVE, STOPPING, or RESIZING state, but not when it is in a STARTING or
SUSPENDED state. To optimize compute pool expenses, you should leverage the AUTO_SUSPEND feature (see CREATE COMPUTE POOL).

The following views provide usage information:

* **ACCOUNT_USAGE views**

  The following ACCOUNT_USAGE views contain Snowpark Container Services credit usage information:

  * The [SNOWPARK_CONTAINER_SERVICES_HISTORY view](../../sql-reference/account-usage/snowpark_container_services_history.md) offers
    credit usage information (hourly consumption) exclusively for Snowpark Container Services.
  * In the [METERING_DAILY_HISTORY view](../../sql-reference/account-usage/metering_daily_history.md), query for rows in which the
    `service_type` column contains the value `SNOWPARK_CONTAINER_SERVICES`.
  * In the [METERING_HISTORY view](../../sql-reference/account-usage/metering_history.md), query for rows in which the
    `service_type` column contains the value `SNOWPARK_CONTAINER_SERVICES`.
* **ORGANIZATION_USAGE views**

  * In the [METERING_DAILY_HISTORY view](../../sql-reference/organization-usage/metering_daily_history.md), use the
    `SERVICE_TYPE = SNOWPARK_CONTAINER_SERVICES` query filter.

## Data transfer cost

Data transfer is the process of moving data into (ingress) and out of (egress) Snowflake. For more information, see
[Understanding data transfer cost](../../user-guide/cost-understanding-data-transfer.md). When you use Snowpark Container Services, the following additional cost
considerations apply:

* **Outbound data transfer:** Snowflake applies the same data transfer rate for outbound data transfers from services and jobs
  to other cloud regions and to the internet, consistent with the rate for all Snowflake outbound data transfers. For more
  information, see the [Snowflake Service Consumption Table](https://www.snowflake.com/legal-files/CreditConsumptionTable.pdf) (table 4a).

  You can query the [DATA_TRANSFER_HISTORY ACCOUNT_USAGE view](../../sql-reference/account-usage/data_transfer_history.md) for
  usage information. The `transfer_type` column identifies this cost as the `SNOWPARK_CONTAINER_SERVICES` type.
* **Internal data transfer:** This class of data transfer refers to data movements across compute entities within Snowflake, such as
  between two compute pools or a compute pool and a warehouse, that resulted from executing a
  [service function](working-with-services.md).
  For more information, see the [Snowflake Service Consumption Table](https://www.snowflake.com/legal-files/CreditConsumptionTable.pdf)
  (tables 4(a) for AWS, 4(b) for Azure, and the column titled “SPCS Data Transfer to Same Cloud Provider, Same Region”).

  To view the costs associated with internal data transfer, you can do the following:

  * Query the [INTERNAL_DATA_TRANSFER_HISTORY view](../../sql-reference/account-usage/internal_data_transfer_history.md) in the ACCOUNT_USAGE schema.
  * Query the [DATA_TRANSFER_HISTORY view](../../sql-reference/account-usage/data_transfer_history.md) in the ACCOUNT_USAGE schema. The
    `transfer_type` column identifies this cost as the `INTERNAL` type.
  * Query the [DATA_TRANSFER_HISTORY view](../../sql-reference/organization-usage/data_transfer_history.md) in the ORGANIZATION_USAGE schema.
    The `transfer_type` column identifies this cost as the `INTERNAL` type.
  * Query the [DATA_TRANSFER_DAILY_HISTORY view](../../sql-reference/organization-usage/data_transfer_daily_history.md) in the ORGANIZATION_USAGE schema. The `service_type` column identifies this cost as the `INTERNAL_DATA_TRANSFER` type.
  * Query the [RATE_SHEET_DAILY view](../../sql-reference/organization-usage/rate_sheet_daily.md) in the ORGANIZATION USAGE
    schema. The `service_type` column identifies this cost as the `INTERNAL_DATA_TRANSFER` type.
  * Query the [USAGE_IN_CURRENCY_DAILY view](../../sql-reference/organization-usage/usage_in_currency_daily.md) in the ORGANIZATION USAGE
    schema. The `service_type` column identifies this cost as the `INTERNAL_DATA_TRANSFER` type.

> **Note:**
>
> Data transfer costs are currently not billed for Snowflake accounts on Google Cloud.
