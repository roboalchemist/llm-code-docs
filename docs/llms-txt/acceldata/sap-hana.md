# Source: https://docs.acceldata.io/documentation/sap-hana.md

# SAP HANA

**SAP HANA** is an in-memory, column-oriented database that stores and processes information far faster than traditional databases. Organizations use it to analyze sales, customer, or operational data in real time. It supports both transactional and analytical workloads, allowing enterprises to process large volumes of data with minimal delay.

Integrating SAP HANA with the **Acceldata Observability Cloud (ADOC)** platform gives you end-to-end visibility into your data’s health, structure, and reliability. This helps you detect data quality issues early, track changes to your data over time, and ensure your business reports and analytics are always accurate and trustworthy.

## Prerequisites

Ensure the following requirements are met before you connect SAP HANA as a data source:

- You have access to the SAP HANA database
- Have a Data Plane ready (or create one) for crawling and profiling
- Have your JDBC connection details, including: URL, username, and password
- If enabling concurrency control, decide how many jobs can run in parallel for this data source.

## Add SAP HANA as a Data Source

### Step 1: Start Setup

1. Select **Register** from the left main menu.
2. Select **Add Data Source**.
3. Select **SAP HANA** from the list of data sources.
4. On the **Data Source Details** page:
    1. Name the data source.
    2. Add a short description (optional).
    3. Enable Data Reliability and select your data plane from the dropdown.

5. Select **Next**.

### Step 2: Add Connection Details

To connect to your SAP HANA database:

1. Enter your **JDBC URL** (e.g., `jdbc:sap://<host>:<port>`)
2. Enter your **Username**.
3. Enter your **Password.**
4. Select a **Data Plane Engine**:
    - **Spark**: Executes data profiling outside SAP HANA.
    - **Pushdown**: Running processing directly inside the SAP HANA database instead of moving data elsewhere for processing.

5. Select **Test Connection**. If successful, you’ll see a **Connected** message. If unsuccessful, check your credentials and JDBC format.
6. Select **Next** to continue.

### Step 3: Set Up Observability

Now you’ll define what ADOC should monitor within SAP HANA.

1. Select the **Schema** to monitor.

**Optional Configurations**

2. Enable **Schema Drift Monitoring** to detect changes in file schemas (e.g., added, removed, or renamed columns) over time. Note Schema drift detection requires a scheduled crawler.
3. Enable **Job Concurrency** and set a maximum number of parallel jobs using Maximum Slots. For more information, see [Control Plane Concurrent Connections and Queueing Mechanism](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/apache-hdfs#control-plane-concurrent-connections-and-queueing-mechanism).
4. Use **Crawler Execution Schedule** to set when background jobs scan files and collect metadata for observability:
    1. Select how often the crawler runs (e.g., daily)
    2. Set execution time and time zone
    3. Add multiple execution times if needed

5. Set Notifications
    1. **Notify on Crawler Failure**: Select one or more channels for failure alerts.
    2. **Notify on Success**: Receive success notifications (toggle on/off)

6. Click **Submit** to save your configuration to register and begin monitoring the SAP HANA data source.

You’ve now successfully added SAP HANA as a data source. It will appear on your Data Sources page, where you can trigger crawlers or review metadata.

## What's Next

Once SAP HANA is integrated, you can:

- In Reliability, view profiling results, schema structures, and rule validation outcomes
- Use Pipelines to track data movement across systems
- Set up alerts for crawler failures or schema drifts
- Monitor and adjust concurrent job settings as usage increases