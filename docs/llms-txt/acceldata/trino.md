# Source: https://docs.acceldata.io/documentation/trino.md

# Trino

Trino is a powerful distributed SQL query engine designed to efficiently query vast datasets spread across multiple heterogeneous data sources. It enables organizations to run fast, interactive, and complex queries on data lakes, data warehouses, and various storage systems without needing to move or transform data. 

By integrating Trino with Acceldata, organizations can gain deeper insights into query performance, resource utilization, and data reliability. This integration enhances observability by providing real-time monitoring, optimizing query execution, and ensuring data quality—helping data teams improve efficiency, reduce costs, and maintain high-performance data operations.

## Prerequisites

To establish a connection between Trino and the ADOC platform, ensure the following details are available:

- **Trino JDBC URL** – The connection string required for establishing communication with the Trino server.
- **Trino Username** – The user account credentials for authentication.
- **Trino Password** – The corresponding password for authentication (file-based password authentication is supported).

Note SSL must be enabled in Trino to establish a secure connection.

## Add Trino as a Data Source

To add Trino with ADOC, perform the following:

### Step 1: Start Setup

1. Navigate to **Register** from the left main menu.
2. Select **Add Data Source** -&gt; **Trino**.
3. On the **Data Source Details** page:
    1. Name the data source.
    2. Add a short description (optional).

4. Select a Data Plane from the dropdown where the data source will be managed. If you don’t have one yet, select [Set Up Data Plane](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/dataplane-installation) to create one.
5. Click **Next**.

### Step 2: Add Connection Details

Provide the following configurations:

- Enter the **JDBC URL** in the format: jdbc:trino://&lt;host&gt;:&lt;port&gt;/ . Example: jdbc:trino://trino-server.example.com:8080/
- Enter the **username** and **password** for authentication.
- _(Optional)_ Enable the **Use Secret Manager** toggle if you want to store credentials securely.

    - Select the **Secret Manager** (e.g., AWS Secrets Manager).
    - Provide the associated **secret key**.

- Select the **Dataplane engine** for data processing:

    - Spark: Recommended for large-scale processing.
    - Pushdown: Executes queries directly in Trino for faster query performance.

- Click **Test Connection** to verify the connectivity. Once the connection is successful, click **Next** to configure observability settings for the data catalog.

### Step 3: Setup Observability

- Select the catalog names for which you want to enable observability.
- _(Optional)_ Enable **Schema Drift Monitoring** to detect unexpected schema changes.
- _(Optional)_ Enable **Crawler Execution Schedule** to automate metadata crawling. 

Finally, click **Submit** to complete the configuration and add the **Trino** as a data source with ADOC.

## What's Next

After successfully integrating Trino with ADOC:

- **Crawl the data source** to index metadata and gather insights. Navigate to the **Data Sources** page and trigger a crawl.
- **Profile the data source** to analyze data quality and detect anomalies.
- **Perform ADOC reliability operations**, such as monitoring data freshness, detecting schema changes, adding policies, and setting alerts.