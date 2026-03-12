# Source: https://docs.snowflake.com/en/sql-reference/organization-usage/warehouse_events_history.md

# Source: https://docs.snowflake.com/en/sql-reference/account-usage/warehouse_events_history.md

Schema:
:   [ACCOUNT_USAGE](../account-usage.md)

# WAREHOUSE_EVENTS_HISTORY view

This Account Usage view can be used to return the events that have been triggered for the single-cluster and multi-cluster warehouses
in your account in the last 365 days (1 year).

Supported events include:

* Creating, dropping, or altering a warehouse, including resizing the warehouse.
* Resuming or suspending a warehouse.
* Resuming, suspending, or resizing a cluster in a warehouse (single-cluster and multi-cluster warehouses).
* Stopping or starting additional clusters in a warehouse (multi-cluster warehouses only).

## Columns

| Column name | Data type | Description |
| --- | --- | --- |
| TIMESTAMP | TIMESTAMP_LTZ | The timestamp when the event is triggered. |
| WAREHOUSE_ID | NUMBER | The unique warehouse ID (assigned by Snowflake) that corresponds to the warehouse name in your account. |
| WAREHOUSE_NAME | VARCHAR | The name of the warehouse in your account. |
| CLUSTER_NUMBER | NUMBER | If an event was triggered for a specific cluster in a multi-cluster warehouse, the number of the cluster (starting with 1) for which the event was triggered; if the event was triggered for all clusters in the warehouse or is not applicable for a single-cluster warehouse, NULL is displayed. |
| EVENT_NAME | VARCHAR | Name of the event. For the list of possible values, see below. |
| EVENT_REASON | VARCHAR | The cause of the event. For the list of possible values, see below. |
| EVENT_STATE | VARCHAR | State of an event that might take time to complete: STARTED or COMPLETED. |
| USER_NAME | VARCHAR | User who initiated the event. |
| ROLE_NAME | VARCHAR | Role that was active in the session at the time the event was initiated. |
| QUERY_ID | VARCHAR | Internal/system-generated identifier for the SQL statement. |
| SIZE | VARCHAR | Current size of the warehouse at the time of the event. This value is only available for WAREHOUSE_CONSISTENT events. Otherwise, this value is NULL. |
| CLUSTER_COUNT | VARCHAR | Number of warehouse clusters at the time of the event. This value is only available for WAREHOUSE_CONSISTENT events. Otherwise, this value is NULL. |
| WAREHOUSE_TYPE | VARCHAR | One of `STANDARD` or `SNOWPARK-OPTIMIZED`. This value is only available for WAREHOUSE_CONSISTENT events. Otherwise, this value is NULL. |
| RESOURCE_CONSTRAINT | VARCHAR | One of: . - `STANDARD_GEN_1` . - `STANDARD_GEN_2` . - `MEMORY_1X` . - `MEMORY_1X_x86` . - `MEMORY_16X` . - `MEMORY_16X_x86` . - `MEMORY_64X` . - `MEMORY_64X_x86` . This value is only available for WAREHOUSE_CONSISTENT events. Otherwise, this value is NULL. It’s also NULL for standard warehouses created before the release of the STANDARD_GEN_2 feature. |

### EVENT_NAME descriptions

The following sections describe the valid values for the EVENT_NAME column for warehouse-related and cluster-related events.

#### Warehouse-related events

The following table describes the valid values for the EVENT_NAME column for warehouse-related events:

| EVENT_NAME | Description |
| --- | --- |
| CONVERT_WAREHOUSE | Triggered by the conversion of a warehouse from standard to Snowpark-optimized, from Snowpark-optimized to standard, from Gen1 to Gen2, or Gen2 to Gen1. This event happens whether the warehouse is running or suspended when the conversion happens.   |  |  | | --- | --- | | Cluster number | None (N/A) | | Event state | COMPLETED or STARTED | | Event reason | CONVERT_TO_SNOWPARK_OPTIMIZED, CONVERT_TO_STANDARD, or CONVERT_RESOURCE_CONSTRAINT |   Cost impact: Newly added resources start metering when they are provisioned. Removed resources stop metering after they finish processing any currently executing queries.  **Tip:** For information about cost implications of changing the RESOURCE_CONSTRAINT property, see [considerations for changing RESOURCE_CONSTRAINT while a warehouse is running or suspended](../../user-guide/warehouses-gen2.md). |
| CREATE_WAREHOUSE | Triggered by the creation of a new warehouse, which can occur when a user manually creates a warehouse or when an account is provisioned and the default warehouse is automatically created in the account.   |  |  | | --- | --- | | Cluster number | None (N/A) | | Event state | COMPLETED or STARTED | | Event reason | None (N/A) |   Cost impact: None if the cluster is created with INITIALLY_SUSPENDED = TRUE. Otherwise, metering starts when all compute resources are provisioned for the warehouse or the warehouse starts processing statements (if the warehouse starts processing statements before the resources are fully provisioned). |
| DROP_WAREHOUSE | Triggered when an existing warehouse is dropped; all currently executing queries on the warehouse are stopped and the compute resources are released.   |  |  | | --- | --- | | Cluster number | None (N/A) | | Event state | COMPLETED or STARTED | | Event reason | None (N/A) |   Cost impact: Metering on the compute resources for the warehouse stops after all currently executing queries complete. |
| ALTER_WAREHOUSE | Triggered when the properties of an existing warehouse are changed, including resizing the warehouse. If the warehouse is resized, additional RESIZE_WAREHOUSE events are triggered. This event can also trigger RESUME_WAREHOUSE or SUSPEND_WAREHOUSE events.   |  |  | | --- | --- | | Cluster number | None (N/A) | | Event state | COMPLETED or STARTED | | Event reason | None (N/A) |   Cost impact: Depends on the event(s) that are triggered by the ALTER statement. |
| RESIZE_WAREHOUSE | Triggered by changing the size of a warehouse, which increases or decreases the compute resources in each cluster in the warehouse. For a running warehouse, this event also triggers a RESIZE_CLUSTER event for each cluster in the warehouse.   |  |  | | --- | --- | | Cluster number | None (N/A) | | Event state | STARTED | | Event reason | WAREHOUSE_RESIZE |   Cost impact: Resizing a running warehouse adds or removes compute resources in each cluster in the warehouse. Newly added resources start metering when they are provisioned. Removed resources stop metering after they finish processing any currently executing queries.  Resizing a suspended warehouse does not provision any new resources for the warehouse. |
| RESUME_WAREHOUSE | Triggered when a suspended warehouse is resumed or a new warehouse is created with INITIALLY_SUSPENDED = FALSE. This event also triggers a RESUME_CLUSTER event for each cluster in the warehouse.   |  |  | | --- | --- | | Cluster number | None (applies to all clusters) | | Event state | STARTED | | Event reason | WAREHOUSE_AUTORESUME or WAREHOUSE_RESUME |   Cost impact: Metering begins after all the compute resources are provisioned for the warehouse. |
| SUSPEND_WAREHOUSE | Triggered when a running warehouse is suspended. This event also triggers a SUSPEND_CLUSTER event for each cluster in the warehouse.   |  |  | | --- | --- | | Cluster number | None (applies to all clusters) | | Event state | STARTED | | Event reason | WAREHOUSE_AUTOSUSPEND or WAREHOUSE_SUSPEND |   Cost impact: Metering on the compute resources for the warehouse stops after all running statements complete. |
| WAREHOUSE_CONSISTENT | Triggered when pending changes to a warehouse complete. For more information, see Usage notes.   |  |  | | --- | --- | | Cluster number | NULL | | Event state | COMPLETED | | Event reason | NULL |   Cost impact: None. Metering occurs for the warehouse event that is logged with the STARTED state before the WAREHOUSE_CONSISTENT event.  For more information, see the cost impact of the warehouse events described in the previous rows. |

#### Cluster-related events

The following table describes the valid values for the EVENT_NAME column for cluster-related events:

| EVENT_NAME | Description |
| --- | --- |
| CONVERT_CLUSTER | Triggered by the conversion of a warehouse from standard to Snowpark-optimized, or from Snowpark-optimized to standard. This event is only emitted when the conversion happens while the warehouse is running.   |  |  | | --- | --- | | Cluster number | Number of the converted cluster (always `1` for a single-cluster warehouse) | | Event state | COMPLETED or STARTED | | Event reason | CONVERT_TO_SNOWPARK_OPTIMIZED or CONVERT_TO_STANDARD |   Cost impact: Newly added resources start metering when they are provisioned. Removed resources stop metering after they finish processing any currently executing queries.  **Tip:** For information about cost implications of changing the RESOURCE_CONSTRAINT property, see [considerations for changing RESOURCE_CONSTRAINT while a warehouse is running or suspended](../../user-guide/warehouses-gen2.md). |
| RESUME_CLUSTER | Triggered when a suspended cluster is resumed.   |  |  | | --- | --- | | Cluster number | Number of the resumed cluster (always `1` for a single-cluster warehouse) | | Event state | STARTED | | Event reason | *WAREHOUSE_AUTORESUME or WAREHOUSE_RESUME (single-cluster warehouse)* MULTICLUSTER_SPINUP (multi-cluster warehouse) |   Cost impact: Metering starts on the compute resources for the cluster after they are provisioned. |
| SUSPEND_CLUSTER | Triggered when a running cluster is suspended.   |  |  | | --- | --- | | Cluster number | Number of the suspended cluster (always `1` for a single-cluster warehouse) | | Event state | STARTED | | Event reason: | *WAREHOUSE_AUTOSUSPEND or WAREHOUSE_SUSPEND (single-cluster warehouse)* MULTICLUSTER_SPINDOWN (multi-cluster warehouse) * RESOURCE_MONITOR_SUSPEND |   Cost impact: Metering stops on the compute resources for the cluster after all currently executing queries complete. |
| RESIZE_CLUSTER | Triggered when a cluster is resized, usually as a result of resizing a warehouse.   |  |  | | --- | --- | | Cluster number | Number of the resized cluster (always `1` for a single-cluster warehouse) | | Event state | STARTED | | Event reason | *WAREHOUSE_AUTORESUME or WAREHOUSE_RESUME (single-cluster warehouse)* MULTICLUSTER_SPINDOWN or MULTICLUSTER_SPINUP (multi-cluster warehouse) * WAREHOUSE_RESIZE |   Cost impact: Depends on whether compute resources are added or removed due to resizing. Newly added resources start metering when they are provisioned. Removed resources stop metering after they finish processing any currently executing queries. |
| SPINUP_CLUSTER | Triggered when a cluster is started (multi-cluster warehouse only); usually happens when the mininimum or maximum cluster size is increased.   |  |  | | --- | --- | | Cluster number | Number of the cluster that was started | | Event state | STARTED | | Event reason | *WAREHOUSE_RESIZE (single-cluster warehouse)* MULTICLUSTER_SPINUP (multi-cluster warehouse) |   Cost impact: Metering starts on the compute resources for the cluster after they are provisioned. |
| SPINDOWN_CLUSTER | Triggered when a running cluster is shut down (multi-cluster warehouse only); usually happens when the minimum or maximum cluster size is decreased.   |  |  | | --- | --- | | Cluster number | Number of the cluster that was shut down | | Event state | STARTED | | Event reason | *WAREHOUSE_RESIZE (single-cluster warehouse)* MULTICLUSTER_SPINDOWN (multi-cluster warehouse) |   Cost impact: Metering stops on the compute resources for the cluster after all currently executing queries complete. |

### EVENT_REASON descriptions

The following table describes the valid values for the EVENT_REASON column:

| EVENT_REASON | Description |
| --- | --- |
| WAREHOUSE_AUTORESUME | A suspended warehouse was resumed automatically because AUTO_RESUME is enabled for the warehouse and a SQL statement was submitted to the warehouse. |
| WAREHOUSE_RESUME | A suspended warehouse was resumed manually by a user. |
| WAREHOUSE_AUTOSUSPEND | A running warehouse was suspended automatically because AUTO_SUSPEND is enabled for the warehouse and the defined period of inactivity for AUTO_SUSPEND has passed. |
| WAREHOUSE_SUSPEND | A running warehouse was suspended manually by a user. |
| WAREHOUSE_RESIZE | A warehouse was resized. |
| RESOURCE_MONITOR_SUSPEND | A warehouse was suspended because the credit quota for the resource monitor for the warehouse was reached. |
| MULTICLUSTER_SPINUP | A new or suspended cluster was provisioned in a multi-cluster warehouse; not applicable to single-cluster warehouses. |
| MULTICLUSTER_SPINDOWN | A running cluster was shut down in a multi-cluster warehouse; not applicable to single-cluster warehouses. |

## Usage notes

* Latency for the view may be up to three hours.

* An event can produce multiple rows in the view if it triggers additional, related events.
* The value for the EVENT_REASON, USER_NAME, ROLE_NAME, and QUERY_ID columns is NULL for a WAREHOUSE_CONSISTENT event.
* The WAREHOUSE_CONSISTENT event might share the same timestamp with another warehouse event and be listed out of order.

### Warehouse event that indicates that an operation has completed

Events that create a warehouse, change the size of the warehouse or the number of clusters, or suspend a warehouse are not atomic
operations. This means that some small amount of time is required for these operations to fully complete.

For example, if a warehouse is suspended using an ALTER WAREHOUSE … SUSPEND statement, any queries that are currently executing on the
warehouse must complete (or time out) before it can be suspended. In some cases, multiple warehouse events might be in-flight
(for example, resize and suspend). When all warehouse events have completed, the warehouse is in a *consistent* state.

If a warehouse event is logged with the STARTED state in the EVENT_STATE column, it is never
logged with a COMPLETED state. Instead, an event logged with the STARTED state is always followed by a subsequent WAREHOUSE_CONSISTENT
event. If multiple warehouse events are logged with the STARTED event state, those events coalesce to the same WAREHOUSE_CONSISTENT event.

If a warehouse event is logged with the COMPLETED state in the EVENT_STATE column, no subsequent WAREHOUSE_CONSISTENT event follows
unless another pending event is logged with a STARTED state.

## Examples

### View events history for the previous week

View the events history for warehouse `my_wh` for the previous week by executing the following statement:

```sqlexample
SELECT timestamp, warehouse_name, cluster_number,
       event_name, event_reason, event_state,
       size, cluster_count
  FROM SNOWFLAKE.ACCOUNT_USAGE.WAREHOUSE_EVENTS_HISTORY
  WHERE warehouse_name = 'MY_WH'
  AND timestamp > DATEADD('day', -7, CURRENT_TIMESTAMP())
  ORDER BY timestamp DESC;
```

### Example events history results

#### Events history for a statement with no pending changes

An ALTER WAREHOUSE statement is logged with the COMPLETED state when there are no additional changes pending. For example,
the following statement updates the comment for warehouse `my_wh`:

```sqlexample
ALTER WAREHOUSE my_wh SET
  COMMENT = 'Updated comment for warehouse';
```

This statement results in the following row in the WAREHOUSE_EVENTS_HISTORY view:

| TIMESTAMP | WAREHOUSE_NAME | EVENT_NAME | EVENT_STATE | SIZE | CLUSTER_COUNT |
| --- | --- | --- | --- | --- | --- |
| 2024-04-26 16:42:13.513 +0000 | MY_WH | ALTER_WAREHOUSE | COMPLETED | NULL | NULL |

#### Events history for a statement that is followed by a WAREHOUSE_CONSISTENT event

When an ALTER WAREHOUSE statement changes the warehouse size, additional events follow. For example, resize warehouse
`my_wh`:

```sqlexample
ALTER WAREHOUSE my_wh SET
  WAREHOUSE_SIZE = 'SMALL';
```

This statement results in the following rows in the WAREHOUSE_EVENTS_HISTORY view:

| TIMESTAMP | WAREHOUSE_NAME | EVENT_NAME | EVENT_STATE | SIZE | CLUSTER_COUNT |
| --- | --- | --- | --- | --- | --- |
| 2024-05-29 15:13:05.874 +0000 | MY_WH | ALTER_WAREHOUSE | STARTED | NULL | NULL |
| 2024-05-29 15:13:05.874 +0000 | MY_WH | RESIZE_WAREHOUSE | STARTED | NULL | NULL |
| 2024-05-29 15:13:06.036 +0000 | MY_WH | WAREHOUSE_CONSISTENT | COMPLETED | SMALL | 1 |
| 2024-05-29 15:13:06.036 +0000 | MY_WH | RESIZE_CLUSTER | COMPLETED | NULL | NULL |

#### Events history for a Snowflake-initiated warehouse event

When Snowflake resumes a multi-cluster warehouse, the following warehouse events are logged:

| TIMESTAMP | WAREHOUSE_NAME | EVENT_NAME | EVENT_STATE | SIZE | CLUSTER_COUNT |
| --- | --- | --- | --- | --- | --- |
| 2024-04-23 17:04:11.618 +0000 | MY_WH | SPINUP_CLUSTER | STARTED | NULL | NULL |
| 2024-04-23 17:04:11.657 +0000 | MY_WH | RESUME_CLUSTER | STARTED | NULL | NULL |
| 2024-04-23 17:04:11.657 +0000 | MY_WH | WAREHOUSE_CONSISTENT | COMPLETED | LARGE | 5 |
