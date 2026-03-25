# Source: https://docs.snowflake.com/en/sql-reference/account-usage/internal_data_transfer_history.md

Schema:
:   [ACCOUNT_USAGE](../account-usage.md)

# INTERNAL_DATA_TRANSFER_HISTORY view

Use this view to get a historical view of Snowpark Container Services internal data transfers in your account for the last 365 days.

This view reports the following two types of internal data transfers:

* **SERVICE_FUNCTION:** When a [service function](../../developer-guide/snowpark-container-services/working-with-services.md) is invoked, it sends a request to its associated service. Note that the query invoking the service functions executes in a warehouse, while the service runs in a compute pool. There is an internal data transfer cost associated with it. The view captures any data exchanged during the request and response as an internal data transfer of the SERVICE_FUNCTION type.
* **COMPUTE_POOL:** Through [service-to-service communication](../../developer-guide/snowpark-container-services/working-with-services.md), a service can transfer data to another service running in a different compute pool. This incurs internal data transfer costs, which the view reports as data transfer cost with the COMPUTE_POOL transfer type.

## Columns

| Column name | Data type | Description |
| --- | --- | --- |
| START_TIME | TIMESTAMP_LTZ | The date and beginning of the hour (in the local time zone) in which the data transfer took place. |
| END_TIME | TIMESTAMP_LTZ | The date and end of the hour (in the local time zone) in which the data transfer took place. |
| TRANSFER_TYPE | VARCHAR | It is either `SERVICE_FUNCTION` or `COMPUTE_POOL`. |
| COMPUTE_POOL_NAME | VARCHAR | If the transfer type is `SERVICE_FUNCTION`, it represents the name of the compute pool that the service function interacts with. If the transfer type is `COMPUTE_POOL`, it represents the source compute pool that initiated the traffic. |
| BYTES_TRANSFERRED | NUMBER | Number of bytes transferred during the START_TIME and END_TIME window. |

## Usage notes

* Latency for the view can be up to 180 minutes (3 hours).
