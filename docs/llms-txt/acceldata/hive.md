# Source: https://docs.acceldata.io/documentation/hive.md

# Apache Hive

Connect your Hive environment to ADOC for data profiling, governance, quality and lineage tracking.

## Prerequisites

Ensure the following requirements are met before you connect Hive as a data source:

- **Hive metastore access:**
Your Hive metastore URI must be reachable.
- **Authenticated Hive Access:**
Use credentials or configuration that allow ADOC to read metadata.
- **Data Plane Configuration:**
Select or create a Data Plane that can connect to Hive.
- **Network Connectivity:**
Ensure there are no firewall or proxy rules blocking ADOC from accessing the Hive metastore.

---

## Add Hive as a Data Source

Follow these steps to set up Hive in ADOC:

### Step 1: Start Setup

1. Select **Register** from the left main menu.
2. Select **Add Data Source**.
3. Select **Hive** from the list of data sources.
4. On the **Data Source Details** page:
    1. Enter a unique name for this data source.
    2. Optionally, add a brief description to clarify its purpose.
    3. Enable the Data Reliability toggle and select your data plane from the drop-down list.

5. Select **Next** to proceed.

### Step 2: Add Connection Details

| Field | Description | 
| ---- | ---- | 
| Metastore JDBC URL | JDBC URI used to connect to the Hive metastore (e.g., `jdbc:mysql://host:3306/hive`) | 
| Metastore Username | Hive metastore username. | 
| Metastore Password | Password for the username provided. | 
| Cluster Name | Logical name used to identify this Hive cluster in ADOC. | 
| Hive Connection Type | Connection mode for Hive integration. Select `DEFAULT` or `Hive3` as per requirement. | 


1. Select **Test Connection**. If successful, you’ll see “Connected.” If not, check the values and try again.
2. Select **Next** to proceed.

### Step 3: Setup Observability

1. Select the databases from the Databases dropdown list.

**Optional Settings**

2. Enable **Schema Drift Monitoring** to track structural changes in your Hive tables. NOTE  Schema drift detection requires scheduled crawler to be enabled.
3. Enable **Job Concurrency** and set a maximum number of parallel jobs using Maximum Slots to limit how many profiling or schema checks can run in parallel. For more information, see [Control Plane Concurrent Connections and Queueing Mechanism](https://docs.google.com/document/d/1W9E7ZGWzrtjXnNbVOHq-6x9F1FDbI0Fqa2gSPqUn5QI/edit?tab=t.0#heading=h.nnqa6y67lnw).
4. Enable **Crawler Execution Schedule** to set up scheduled scans of your Hive tables:
    1. Choose how often the crawler runs (e.g., daily)
    2. Set execution time and time zone
    3. Add multiple execution times if needed

5. Set Notifications
    1. **Notify on Crawler Failure**: Choose one or more channels to receive failure alerts via configured channels.
    2. **Notify on Success**: Toggle this if you'd like to receive success notifications.

6. Click **Submit** to save your configuration to register and begin monitoring the Hive data source.

You have successfully added Hive as a data source. A new card for **Hive** will appear on the **Data Sources** page, displaying crawler status and basic connection details.

You can choose to run the crawler immediately or schedule it for later.

---

## What’s Next

After you connect Hive, you can go to the following pages to view and manage your data:

- **Reliability** – View data quality scores, profiling status, and rule results for your BigQuery datasets.
- **Pipelines** – Monitor how data flows from BigQuery to downstream systems.
- **Alerts** – See notifications for quality issues or pipeline delays in real time.