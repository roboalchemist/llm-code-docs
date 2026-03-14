# Source: https://docs.acceldata.io/documentation/db2.md

# IBM DB2

IBM DB2 is a powerful relational database management system (RDBMS) designed to store, manage, and retrieve structured data at scale. Known for its scalability, reliability, and enterprise-grade performance, DB2 is widely used in industries that require secure and efficient management of mission-critical data.

## Prerequisites

Ensure the following requirements are met before you connect DB2 as a data source:

- **DB2 Access Details:** JDBC connection information (hostname, port, username, and password).
- **ADOC Account & Permissions:** Access rights to add new data sources in your ADOC environment.
- **Data Plane:** An existing data plane in ADOC or readiness to create one for DB2 ingestion. See the [Data Plane Installation](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/dataplane-installation) documentation for more information.

## Add IBM DB2 as a Data Source

### Step 1: Start Setup

1. From the main menu, select **Register** -&gt; **Add Data Source**.
2. Select **IBM DB2** from the list.
3. On the **Data Source Details** page:
    1. Enter a name and optional Description for the data source.
    2. Enable the Data Reliability toggle and select the data plane.

4. Click **Next**.

### Step 2: Enter Connection Details

To connect to your ClickHouse database:

1. Enter your JDBC URL  in the format: `jdbc:db2://<host>:<port>/<database>`
2. Enter your **username** and **password** (or select a secret manager)
3. Click **Test Connection**. A "Connected" message will appear if successful. Otherwise, re-check your credentials, JDBC URL, and format.

### Step 3: Set Up Observability

Now define what ADOC should monitor in ClickHouse.

1. Select the DB2 schemas or databases you want ADOC to monitor.
2. Use **Crawler Execution Schedule** to set when background jobs scan files and collect metadata for observability:
    - Select how often the crawler runs (e.g., daily)
    - Set execution time and time zone
    - Add multiple execution schedules if needed

3. Configure Notifications
    - **Notify on Crawler Failure**: Select one or more channels for failure alerts.
    - **Notify on Success**: Receive success notifications (toggle on/off)

4. Click **Submit** to save your configuration and start monitoring your ClickHouse data source.

Your DB2 data source will now appear on the Data Sources page.

## What’s Next?

- **Create and Apply Policies:** Define observability policies such as **data quality, reconciliation, schema drift, data drift, and anomaly detection**. Without policies, dashboards will not show metrics.
- **Monitor Dashboards:** Use ADOC dashboards to track applied policies, detect anomalies, and assess DB2 data health.
- **Set Up Alerts:** Configure proactive alerts to respond quickly to schema changes or data quality issues.