# Source: https://docs.acceldata.io/documentation/apache-hdfs.md

# Apache HDFS

Integrate your HDFS cluster with the ADOC platform to monitor data health, asset reliability, and file system performance. This setup helps you profile distributed data at scale and detect issues in near real-time.

## Prerequisites

Ensure the following requirements are met before you connect HDFS as a data source:

- **HDFS Access:**
Your HDFS NameNode URI (e.g., hdfs://namenode-host:8020) must be reachable over the network. This is the address of the HDFS NameNode responsible for managing file system metadata.
- **Cluster Permissions:**
Use a user that has access to read metadata and files within your HDFS cluster.
- **Data Plane Configuration:**
Choose a **Data Plane** — a background agent that connects to your data systems, fetches files, and runs profiling jobs. For more information, refer the [Data Plane Installation Guide](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/dataplane-installation).
- **Network Connectivity:**
Ensure there are no firewall or proxy rules blocking ADOC from accessing the HDFS NameNode.

---

## Add HDFS as a Data Source

Follow these steps to set up HDFS in ADOC:

### Step 1: Start Setup

1. Select **Register** from the left main menu.
2. Select **Add Data Source**.
3. Select **HDFS** from the list of data sources.
4. On the **Data Source Details** page:
    1. Enter a unique name for this data source.
    2. Optionally, add a brief description to clarify its purpose.
    3. Enable the Data Reliability toggle and select your data plane from the drop-down list.

5. Select **Next** to proceed.

### Step 2: Add Connection Details

| Field | Description | 
| ---- | ---- | 
| NameNode URI | Enter the base path to your HDFS instance (e.g., `hdfs://namenode-host:8020`) | 
| Cluster Name | Enter a name to represent your HDFS cluster in ADOC. | 


1. Select **Test Connection**. If successful, you’ll see “Connected.” If the test fails:
2. Double-check the **NameNode URI** and user credentials.
3. Ensure the `ad-analysis-standalone` service is **running** on the selected Data Plane.
4. Select **Next** to proceed.

### Step 3: Setup Observability

1. Enter the asset name.
2. Add the file **path expression** (e.g., `hdfs://namenode1:8020/user/hdfs/data/hdfs_employees.csv`)
3. Select the **file type** (e.g., CSV, ORC, PARQUET, JSON, Avro).
4. Add the **delimiter** for files like CSV  (e.g., `,`).
5. Select the **File Monitoring Channel Type**
    - Choose **NONE** to disable file-level monitoring.
    - Choose **PUBSUB** if you want to receive file-level updates via publish-subscribe mechanism (e.g., using Kafka or other messaging services).

**Optional Settings**

6. Enable **Schema Drift Monitoring** to detect changes in file schemas (e.g., added, removed, or renamed columns) over time. NOTE _**Schema drift detection requires a scheduled crawler.**_
7. Enable **Job Concurrency** and set a maximum number of parallel jobs using Maximum Slots. For more information, see [Control Plane Concurrent Connections and Queueing Mechanism](#control-plane-concurrent-connections-and-queueing-mechanism).
8. Enable **Crawler Execution Schedule** to schedule background jobs that scan files and collect metadata for observability:
    1. Choose how often the crawler runs (e.g., daily)
    2. Set execution time and time zone
    3. Add multiple execution times if needed

9. Set Notifications
    1. **Notify on Crawler Failure**: Choose one or more channels to receive failure alerts.
    2. **Notify on Success**: Toggle this if you'd like to receive success notifications.

10. Click **Submit** to save your configuration to register and begin monitoring the HDFS data source.

You have successfully added HDFS as a data source. A new card for **HDFS** will appear on the **Data Sources** page, displaying crawler status and basic connection details.

---

## What’s Next

After you connect HDFS, you can go to the following pages to view and manage your data:

- **Reliability** – View data quality scores, profiling status, and rule results for your BigQuery datasets.
- **Pipelines** – Monitor how data flows from BigQuery to downstream systems.
- **Alerts** – See notifications for quality issues or pipeline delays in real time.

These insights help your team proactively monitor large-scale distributed data.

---

## More About HDFS Integration

### Control Plane Concurrent Connections and Queueing Mechanism

Enable job concurrency control in the ADOC platform to manage how many jobs run in parallel for an HDFS data source. This helps prevent overloading your cluster and ensures efficient execution of profiling, data quality, and reconciliation jobs.

**When to use this feature**

Enable job concurrency control when:

- Limit how many jobs run in parallel on your HDFS cluster
- Prevent resource contention from frequent job triggers
- Manage high job volume during peak hours

**What it does**

- Lets you define the **maximum number of concurrent jobs** allowed for a data source.
- Automatically **queues additional jobs** that exceed the defined limit.
- Starts queued jobs as soon as a job slot becomes available.
- Uses a background service that checks every minute for available job slots.

**Example**

1. You set Maximum Slots to 1.
2. You trigger three profiling jobs at the same time.
3. One job starts immediately.
4. The remaining two jobs are added to a queue and marked as Waiting.
5. When the first job completes, the next job in the queue starts automatically.

**Benefits**

- Helps prevent overload when many jobs run at once
- Increases stability by managing resource contention
- Gives you control over how much load is sent to your HDFS cluster

### Cross-Cluster Reconciliation (MapR and Apache/Hive)

ADOC supports cross-cluster reconciliation between **MapR HDFS/Hive** and **Apache HDFS/Hive** environments. This feature helps ensure that data and metadata remain consistent across clusters, particularly in hybrid or migration scenarios.

**Objective**

**To maintain consistency of data and metadata between two clusters:**

- One running MapR HDFS and Hive
- Another running Apache HDFS and Hive

**This is useful when:**

- Migrating datasets from MapR to Apache
- Validating sync between environments in a multi-cluster architecture

**How Reconciliation Works?**

**Data Comparison**: ADOC scans data files in MapR HDFS and compares them to Apache HDFS. It also checks Hive metadata in both clusters to identify mismatches in structure, record count, or schema.

**Metadata Synchronization**: The system aligns table structures, column types, and other schema elements to reflect the most accurate and current state across clusters.

**Discrepancy Identification and Resolution**

- ADOC uses pre-defined rules to detect and classify discrepancies.
- The system can automatically update Hive metadata, flag files for manual review, or trigger alerts.

**Cross-Cluster Communication**

To enable cross-cluster operations, ensure the following:

- **Connectivity:** Establish secure communication between both clusters using SSH, VPN, or other secure network tunnels.
- **Data Transfer Optimization**: Optimize for performance and security when transferring large datasets between environments.
- **Hive and HDFS Access**: ADOC must be configured to access both Hive Metastores and HDFS layers across clusters.

**Logging and Monitoring**

- All reconciliation activities are logged.
- You can review discrepancy details, resolution actions, and timestamps in ADOC dashboards.
- Alerts can be configured for any critical mismatches or reconciliation failures.

**Operational Considerations**

| Factor | Recommendation | 
| ---- | ---- | 
| Network Latency | Schedule large-scale reconciliations during low-traffic windows. | 
| Cluster Compatibility | Ensure both clusters use compatible versions of Hive and Hadoop. | 
| Schema Drift | Monitor for schema changes that may affect metadata alignment. | 
| Permissions | Set up cross-cluster access permissions for both Hive and HDFS systems. | 
| Compliance & Security | Apply encryption and access control policies, especially for sensitive data. | 
