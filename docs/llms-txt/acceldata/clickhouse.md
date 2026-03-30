# Source: https://docs.acceldata.io/documentation/clickhouse.md

# ClickHouse

ClickHouse is a high-performance, column-oriented database designed for large-scale analytics. It stores data in columns instead of rows, making it extremely fast for aggregations and queries—even across billions of records. This makes it ideal for real-time reporting, dashboards, and observability use cases.

## Prerequisites

TEnsure the following requirements are met before you connect ClickHouse as a data source:

- **ClickHouse access details**: JDBC connection information (host, port, database, username, password/secret).
- **Acceldata setup**: An active ADOC account with permissions to add data sources.
- **Data Plane**: An existing data plane in ADOC (or the ability to create one for ClickHouse ingestion). See the [Data Plane Installation](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/dataplane-installation) documentation for more information.

## Add ClickHouse as a Data Source

### Step 1: Start Setup

1. From the main menu, select **Register** -&gt; **Add Data Source**.
2. Select **ClickHouse** from the list.
3. On the **Data Source Details** page:
    1. Enter a name and optional Description for the data source.

4. Ensure the Data Reliability toggle is enabled and select the required data plane.
5. Click **Next**.

### Step 2: Enter Connection Details

To connect to your ClickHouse database:

1. Enter your JDBC URL  in the format: `jdbc:clickhouse://<host>:<port>/<database>`
2. Enter your **username** and **password** (or select a secret manager)
3. Click **Test Connection**. A "Connected" message will appear if successful. Otherwise, re-check your credentials, JDBC URL, and format.

### Step 3: Set Up Observability

Now define what ADOC should monitor in ClickHouse.

1. Select the databases in **ClickHouse** you want to monitor.
2. Use **Crawler Execution Schedule** to set when background jobs scan files and collect metadata for observability:
    - Select how often the crawler runs (e.g., daily)
    - Set execution time and time zone
    - Add multiple execution schedules if needed

3. Configure Notifications:
    - **Notify on Crawler Failure**: Select one or more channels for failure alerts.
    - **Notify on Success**: Receive success notifications (toggle on/off)

4. Click **Submit** to save your configuration and start monitoring your ClickHouse data source.

Your ClickHouse data source will now appear on the Data Sources page.

## What’s Next

- **Create and Apply Policies:** Define data observability policies, such as data quality, reconciliation, data drift, schema drift, and anomaly detection.  These policies are required for ADOC to generate insights from your ClickHouse data.
- **Monitor Dashboards:** After applying policies, explore ADOC dashboards to track metrics, detect anomalies, and measure health of your ClickHouse data.
- **Set Up Alerts:** Configure  up alerts for critical events (like schema changes, anomalies, or reconciliation failures) to act quickly.