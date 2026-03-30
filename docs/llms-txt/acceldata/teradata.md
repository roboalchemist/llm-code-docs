# Source: https://docs.acceldata.io/documentation/teradata.md

# Teradata

Acceldata Data Observability Cloud (ADOC) integrates with Teradata to help organizations monitor data reliability, detect schema and data changes, and maintain trusted analytics across enterprise data warehouses.

By connecting Teradata to ADOC, users can automatically discover metadata and apply observability policies that improve data quality, freshness, and operational confidence.

## Prerequisites

- **Teradata Host / URL**
- **Username**
- **Password**

## Add Teradata as a Data Source

Perform the following steps below to register Teradata in ADOC:

### Step 1: Start Setup

1. Navigate to **Register** from the left main menu.
2. Select **Add Data Source** -&gt; **Teradata**.
3. On the **Data Source Details** page:
    1. Name the data source.
    2. Add a short description (optional).

4. Select a Data Plane from the dropdown where the data source will be managed. If you don’t have one yet, select [Set Up Data Plane](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/dataplane-installation) to create one.
5. Click **Next**.

### Step 2: Add Connection Details

On the **Connection Details** page, 

1. Enter the **Teradata Host / URL**.
2. Provide the **Username** and **Password**.
3. Click **Test Connection** to validate connectivity. If the test is successful, click **Next**, else check the credentials entered. For more information, see [Troubleshooting Data Source Connection & Crawling](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/troubleshooting-data-source-connection---crawling).

### Step 3: Set Up Observability

On the **Set Up Observability** page:

1. Select the **Databases** to be monitored. To add multiple databases, click **+**.
2. (Optional) Enable **Crawler Execution Schedule** to control crawl frequency.
3. (Optional) Enable **Notify on Crawler Failure** to receive alerts.

Click **Submit** to complete the configuration.

## What's Next

Once Teradata is successfully registered:

- ADOC performs metadata crawling for selected databases
- Assets appear under **Reliability -&gt; Discover Assets**
- Users can configure:
    - Data quality policies
    - Freshness policies
    - Drift detection
    - Reliability and rule-based monitoring

---

## References

- [Teradata JDBC Driver](https://downloads.teradata.com/download/connectivity/jdbc-driver?utm_source=chatgpt.com)
- [Teradata Developers Portal](https://developers.teradata.com/)
- [Teradata JDBC Driver Reference](https://teradata-docs.s3.amazonaws.com/doc/connectivity/jdbc/reference/current/frameset.html)
- [Teradata JDBC Driver User Guide](https://teradata-docs.s3.amazonaws.com/doc/connectivity/jdbc/reference/current/jdbcug_chapter_2.html)