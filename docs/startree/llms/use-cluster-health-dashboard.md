# Source: https://docs.startree.ai/reference/use-cluster-health-dashboard.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# StarTree Cloud Cluster Health Dashboard

The StarTree Cloud Cluster Health Dashboard provides a real-time overview of your Apache Pinot cluster's operational status. Designed to help you proactively identify and resolve potential issues, this dashboard displays the pass/fail status of various system checks, allowing you to quickly pinpoint performance bottlenecks or stability concerns.

By observing key health indicators and filtering checks based on specific instances or tables, you gain a holistic view of your cluster's well-being, ensuring optimal data ingestion and query performance.

## **Key Features of the Cluster Health Dashboard**

* **Comprehensive Health Checks:** Monitors essential components and operations of your Pinot cluster, including Zookeeper connectivity, controller health, segment availability, and more.
* **Clear Pass/Fail Status:** Quickly identify issues with intuitive status indicators for each check.
* **Granular Filtering:** Drill down into specific health concerns by filtering checks based on individual instances or particular tables.
* **Detailed Insights:** Access additional context and error messages for failed checks to aid in troubleshooting.

## **Accessing the Cluster Health Dashboard**

Follow these steps to view your cluster's health in the StarTree Cloud UI:

1. Log in to the StarTree Cloud Data Portal.
2. Click the **Cluster Health** link in the left navigation menu.

A dashboard will appear, displaying a comprehensive list of health checks. For each check, you'll see:

* Its descriptive name.
* A clear **PASS** or **FAIL** status indicator.
* **Additional details** which may include specific error messages, affected instances, or relevant metrics to help you understand the issue.

## **How Cluster Health Checks Work**

The cluster health checks are executed by the `ClusterHealthCheckTask`, which runs periodically every **20 minutes** by default. The results of these checks are cached in memory and overwritten with each new run, ensuring you always see the latest health status.

## **Understanding and Responding to Health Check Failures**

When a health check fails, it indicates a potential issue that may impact your cluster's performance or stability. The "additional details" provided for each failed check are crucial for diagnosis.

## **Using Cluster Health Checks Ad-Hoc (API Reference)**

For immediate insights or integration with automated scripts, you can trigger and fetch cluster health checks using the following Controller API calls:

### **Run Health Checks Immediately**

This endpoint triggers the ClusterHealthCheckTask to run at the moment you call it, bypassing the default 20-minute interval.

```
GET /periodictask/run?taskName=ClusterHealthCheckTask
```

**Example cURL Request:**

```
curl -X GET "https://<your-controller-host>/periodictask/run?taskName=ClusterHealthCheckTask"
```

**Expected Response:** A confirmation message indicating that the task has been queued or executed successfully.

### **Fetch Current Cluster Health Report**

Retrieves the latest cached cluster health report, containing the pass/fail status and details of all checks.

```
GET /clusterHealth
```

**Example cURL Request:**

```
curl -X GET "https://<your-controller-host>/clusterHealth" | json_pp
```

**Expected Response:** A JSON object detailing the status of all health checks, similar to what you would see in the dashboard.

**List All Available Cluster Health Checks**

Provides a list of all defined health check types that the system monitors, along with their brief descriptions.

```
GET /clusterHealth/list
```

**Example cURL Request:**

```
curl -X GET "https://<your-controller-host>/clusterHealth/list" | json_pp
```

**Expected Response:** A JSON array listing all available health checks, useful for understanding the scope of the dashboard.

## List of Available Health Checks

The StarTree Cloud Cluster Health Dashboard monitors a wide range of parameters to ensure your Pinot cluster's optimal operation. Below is a list of the checks performed and their descriptions:

| Check                                          | Description                                                                                                                                                                                                                                                                        |
| :--------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `IDEAL_STATE_EV_MISMATCH_CHECK`                | Checks if a table has any segments whose ExternalView state does not match with IdealState.                                                                                                                                                                                        |
| `TABLE_SEGMENTS_RELOAD_CHECK`                  | Checks if a table has any segments that need to be reloaded.                                                                                                                                                                                                                       |
| `SEGMENT_COUNT_CHECK`                          | Checks if a table has more than 50,000 segments, which could indicate potential performance issues or inefficient segment management.                                                                                                                                              |
| `SEGMENT_SIZE_CHECK`                           | Checks if more than a quarter of a table's segments are smaller than 5MB, which might suggest suboptimal segment sizing for performance.                                                                                                                                           |
| `SEGMENT_RETENTION_CHECK`                      | Checks if a table does not have segment retention configured. Proper retention policies are crucial for managing data lifecycle and storage.                                                                                                                                       |
| `REPLICATION_CHECK`                            | Checks if a table has a replication factor less than the configured threshold in the controller configuration (default is 3 if unspecified). Adequate replication ensures data availability and fault tolerance.                                                                   |
| `TABLE_COLUMN_COUNT_CHECK`                     | Checks if the number of columns in a schema exceeds 500. A high column count can impact query performance and memory usage.                                                                                                                                                        |
| `TIME_COLUMN_GRANULARITY_CHECK`                | Checks if a table has any time columns with granularity set to MILLISECONDS, MICROSECONDS, or NANOSECONDS, which can sometimes lead to performance overhead if not aligned with typical query patterns.                                                                            |
| `UPSERT_TABLE_SEGMENT_ASSIGNMENT_CHECK`        | For an upsert table, checks if segments of a partition for a single replica group are assigned to more than one server. This can indicate an incorrect configuration or assignment issue.                                                                                          |
| `INSTANCE_HEALTH_API_CHECK`                    | Checks if any of the instance `/health` API endpoints are not live, indicating that a Pinot instance (Server or Broker) is unresponsive.                                                                                                                                           |
| `SEGMENT_SKEW_HEALTH_CHECK`                    | Checks whether any server associated with a specific table (having more than 50 segments) has a segment count exceeding 50% of the average segment count across all servers for that table. This identifies uneven segment distribution.                                           |
| `CONSUMING_PARTITION_SKEW_HEALTH_CHECK`        | Checks whether any server associated with a specific table (having more than 10 consuming segments) has a consuming segment count that exceeds 50% of the average consuming segment count across all servers for that table. This highlights uneven real-time data ingestion load. |
| `TABLE_SKEW_CHECK`                             | Checks whether the number of tables hosted by a server exceeds 50% of the average number of tables hosted across all servers, indicating an imbalance in table distribution.                                                                                                       |
| `CLUSTER_LEVEL_SEGMENT_SKEW_CHECK`             | Checks whether the number of segments on any server exceeds 50% of the average segment count across all servers within the entire cluster, indicating overall segment distribution imbalance.                                                                                      |
| `CLUSTER_LEVEL_CONSUMING_PARTITION_SKEW_CHECK` | Checks whether the number of consuming segments on any server exceeds 50% of the average consuming segment count across all servers within the entire cluster, highlighting overall real-time ingestion load imbalance.                                                            |
| `HIGH_NUMBER_OF_SEGMENTS_CHECK`                | Checks whether the number of segments hosted on a server exceeds 10,000, which can lead to performance degradation.                                                                                                                                                                |
| `HIGH_NUMBER_OF_CONSUMING_PARTITIONS_CHECK`    | Checks whether the number of consuming segments hosted on a server exceeds 50, indicating a potential bottleneck for real-time ingestion on that server.                                                                                                                           |
| `HIGH_NUMBER_OF_DOCUMENTS_CHECK`               | Checks whether the number of documents hosted by a server is greater than 1 Billion, which can impact query performance and memory footprint.                                                                                                                                      |
| `HIGH_NUMBER_OF_TABLES_CHECK`                  | Checks whether the number of tables hosted by a server is greater than 10, indicating a potential concentration of tables on a single server which might affect resource utilization.                                                                                              |
| `DATA_SIZE_SKEW_CHECK`                         | Checks whether the skew in the size of data hosted by instances is asymmetric (specifically if the skew is not in the range `[-2, 2]`), indicating an uneven distribution of data storage across your cluster.                                                                     |
| `CONTROLLER_TABLES_SKEW_CHECK`                 | Checks whether the skew of table count hosted by lead controllers is asymmetric (specifically if the skew is not in the range `[-2, 2]`), indicating an uneven distribution of table management load among controllers.                                                            |
| `HIGH_UPSERT_PK_PER_PARTITION_CHECK`           | Checks if a partition hosted by an instance has a primary key count exceeding 500 million, which can impact upsert performance and memory.                                                                                                                                         |
| `UPSERT_PRIMARY_KEY_SKEW_CHECK`                | Checks whether the skew in the distribution of primary keys among servers is asymmetric (specifically if skew is not in the range `[-2, 2]`), indicating an uneven load of primary keys across servers.                                                                            |
| `PREBUILT_SNAPSHOT_CHECK`                      | Checks for any upsert/deduplication tables in a cluster where the prebuilt snapshot feature is disabled for preloading. Prebuilt snapshots can significantly improve query performance for these table types.                                                                      |
| `UPSERT_PK_SKEW_PER_PARTITION_CHECK`           | Checks whether the skew for primary keys in table partitions is asymmetric (specifically if the skew is not in the range `[-2, 2]`), indicating an uneven distribution of primary keys within partitions.                                                                          |
| `HIGH_UPSERT_PRIMARY_KEYS_CHECK`               | Checks if the primary key count for all tables hosted by an instance exceeds 800 Million, indicating a very high primary key load on that instance.                                                                                                                                |
| `INSTANCE_POOLS_CHECK`                         | Checks if any server is not part of instance pools, or if any pool is not disjoint when the cluster has more than 8 servers. Proper instance pooling is crucial for fault isolation and resource management.                                                                       |
| `INSTANCE_POOLS_N_REPLICA_GROUPS_CHECK`        | Checks if any table is not using instance pools and replica groups configurations, which are recommended for better fault tolerance and resource isolation in larger clusters.                                                                                                     |
| `HELIX_HOST_NAME_INSTANCE_NAME_MISMATCH_CHECK` | Checks if the Instance ID/Name does not match the expected value derived from the Instance Config. This can indicate a misconfiguration.                                                                                                                                           |
| `TABLE_SEGMENT_ASSIGNMENT_CHECK`               | Checks if rebalancing of segments is needed on a table, which can help ensure even data distribution and query performance across servers.                                                                                                                                         |
| `BROKER_RESOURCE_CHECK`                        | Checks if the broker resource for a table does not contain any of the brokers within the tenant, potentially leading to query routing issues.                                                                                                                                      |
| `QUERY_HEALTH_CHECK`                           | Performs a simple `SELECT $docId FROM TABLE_NAME LIMIT 1` query for each table to check if it executes unsuccessfully, indicating fundamental queryability issues.                                                                                                                 |
| `SEGMENTS_TIME_PARTITION_CHECK`                | Checks if any segments of a table are not partitioned by time (i.e., if the current segment end time is less than the previous segment end time, given that segments are sorted by their start and end times). This identifies potential issues with time-based segment ordering.  |

Built with [Mintlify](https://mintlify.com).
