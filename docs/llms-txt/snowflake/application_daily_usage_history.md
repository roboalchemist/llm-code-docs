# Source: https://docs.snowflake.com/en/sql-reference/account-usage/application_daily_usage_history.md

Schema:
:   [ACCOUNT_USAGE](../account-usage.md)

# APPLICATION_DAILY_USAGE_HISTORY view

Use this view to return the daily credit and storage usage for Snowflake Native Apps in an account within the last 365 days
(1 year).

## Columns

The following table provides definitions for the APPLICATION_DAILY_USAGE_HISTORY view columns.

| Field | Data type | Description |
| --- | --- | --- |
| APPLICATION_NAME | VARCHAR | The application name. |
| APPLICATION_ID | NUMBER | An internal, system-generated identifier for the application. |
| LISTING_GLOBAL_NAME | VARCHAR | The listing global name that appears in Snowflake Marketplace or in the data exchange hosting the application. |
| USAGE_DATE | DATE | The date the Snowflake Native App usage occurred. |
| CREDITS_USED | NUMBER | The number of credits consumed by the Snowflake Native App in a day. |
| CREDITS_USED_BREAKDOWN | ARRAY | An array of data objects that identify the Snowflake service that consumed daily credits. See CREDITS_USED_BREAKDOWN array for formatting. |
| STORAGE_BYTES | NUMBER | The daily average of storage bytes used by the Snowflake Native App. |
| STORAGE_BYTES_BREAKDOWN | ARRAY | An array of data objects that identify the type and number of storage bytes used. See STORAGE_BYTES_BREAKDOWN array for formatting. |

## Usage notes

* The maximum latency for this view is one day.
* Usage is attributed to the start day when usage events span multiple days.
* The APPLICATION_DAILY_USAGE_HISTORY view and the Snowsight cost management tools can return different daily credit and storage usage values. This discrepancy is caused by the methods used to determine daily credit and storage usage. To determine these values, the APPLICATION_DAILY_USAGE_HISTORY view uses the current session’s [TIMEZONE](../parameters.md) parameter and the Snowsight cost management tools use Coordinated Universal Time (UTC). To resolve any discrepancies, Snowflake recommends setting the TIMEZONE parameter to UTC.

### CREDITS_USED_BREAKDOWN array

The CREDITS_USED_BREAKDOWN array provides details about the services that consumed daily credits.

Example:

```sqljson
[
  {
    "credits": 0.005840921,
    "serviceType": "AUTO_CLUSTERING"
  },
  {
    "credits": 0.115940725,
    "serviceType": "SERVERLESS_TASK"
  },
  {
    "credits": 6.033448041,
    "serviceType": "SNOWPARK_CONTAINER_SERVICES"
  }
]
```

The following table provides descriptions for the key-value pairs in the objects in the array.

| Field | Data type | Description |
| --- | --- | --- |
| `credits` | DECIMAL | Number of credits consumed by the service type specified by `serviceType` on the usage date. |
| `serviceType` | VARCHAR | The service type, which can be one of the following values:   *`AUTO_CLUSTERING` — See [Automatic Clustering](../../user-guide/tables-auto-reclustering.md).* `DATA_QUALITY_MONITORING` — See [Introduction to data quality checks](../../user-guide/data-quality-intro.md). *`MATERIALIZED_VIEW` — See [Working with Materialized Views](../../user-guide/views-materialized.md).* `PIPE` — See [Snowpipe](../../user-guide/data-load-snowpipe-intro.md). *`SEARCH_OPTIMIZATION` — See [Search optimization service](../../user-guide/search-optimization-service.md).* `SERVERLESS_TASK` — See [Introduction to tasks](../../user-guide/tasks-intro.md). *`SNOWPARK_CONTAINER_SERVICES` — See [Snowpark Container Services](../../developer-guide/snowpark-container-services/overview.md).* `WAREHOUSE_METERING` — See [Overview of warehouses](../../user-guide/warehouses-overview.md). |

The following are used in the determination of credit consumption:

* The credits used by objects in the Snowflake Native App. For example, auto-clustering on tables in the Snowflake Native App.
* The credits used by the warehouses owned by the Snowflake Native App.
* The credits used by the compute pools dedicated to the Snowflake Native App.

### STORAGE_BYTES_BREAKDOWN array

The STORAGE_BYTES_BREAKDOWN array provides details about the services that consumed storage.

Example:

```sqljson
[
  {
    "bytes": 34043221,
    "storageType": "DATABASE"
  },
  {
    "bytes": 109779541,
    "storageType": "FAILSAFE"
  }
]
```

The following table provides descriptions for the key-value pairs in the objects in the array.

| Field | Data type | Description |
| --- | --- | --- |
| `bytes` | INTEGER | Number of storage bytes used. |
| `storageType` | VARCHAR | The storage type, which can be one of the following values:   *`DATABASE`: Database storage.* `FAILSAFE`: [Fail-safe storage](../../user-guide/data-failsafe.md). * `HYBRID_TABLE`: Storage for [hybrid tables](../../user-guide/tables-hybrid.md). |

Only data stored in the Snowflake Native App is used to determine storage byte consumption. External databases created by the Snowflake Native App are not included in the determination of this value.

## Examples

Retrieve the daily credit and storage usage for a Snowflake Native App in an account and order the results by usage date:

```sqlexample
SELECT *
  FROM SNOWFLAKE.ACCOUNT_USAGE.APPLICATION_DAILY_USAGE_HISTORY
  ORDER BY usage_date DESC;
```
