# Source: https://docs.acceldata.io/documentation/singlestore--memsql-.md

# SingleStore (memSQL)

SingleStoreDB (formerly MemSQL) is a high-performance, distributed relational database designed for real-time analytics and low-latency workloads. By integrating SingleStore with the Acceldata Data Observability Cloud (ADOC), you can continuously monitor metadata, profile tables, enforce data quality policies, and track the reliability of your SingleStore assets.

## Prerequisites

### SingleStore Requirements

- SingleStore host and port
- JDBC username and password
- **OR** a SingleStore/MemSQL credentials file
- Network reachability from the ADOC Data Plane
- Permissions to read metadata (`INFORMATION_SCHEMA`)

## Add SingleStore as a Data Source

Follow these steps to register SingleStore into ADOC.

### 1. Start Setup

1. Navigate to **Register → Data Sources**.
2. Click **Add Data Source**.
3. Select **SingleStore (MemSQL)** from the data source list.
4. On the **Data Source Details** page, enter a name and optional Description for the data source.
5. Ensure the Data Reliability toggle is enabled, and select a data plane.
6. Click **Next** to proceed to the **Connection Details** page.

---

### 2. Provide Connection Details

On the **Connection Details** page, enter the required fields:

7. Enter the **MemSQL JDBC URL**.
8. Enter **JDBC Username** and **Password.**
9. Enable the **MemSQL Enabled** toggle:
    - Upload your credentials file by Drag-and-drop or clicking to browse your system.

> When this toggle is enabled, the credentials file overrides manual JDBC username/password authentication.

10. Click **Test Connection**. If it fails, verify the credentials and try again.
11. Click **Next** after a successful connection.

---

### 3. Observability Setup

On the **Set Up Observability** page, configure how ADOC should crawl and monitor your SingleStore environment.

12. **Select Databases**: Use the **Databases** dropdown to choose one or more databases that ADOC should crawl for schema discovery, profiling, and data quality monitoring.
13. _(Optional)_ **Enable Crawler Execution Schedule:** Turn on this option if you want ADOC to automatically run the crawler on a recurring schedule. When enabled, ADOC will periodically refresh schema metadata for the selected databases.
14. _(Optional)_ **Notify on Crawler Failure:** Enable this toggle if you want to receive notifications when a scheduled crawler run fails. This helps you proactively address connectivity or permission issues
15. After configuring the above settings, click **Submit** to complete the data source registration.

## What's Next

Once SingleStore is onboarded:

- The metadata crawler can be run manually or via schedule
- Discovered databases and tables appear in **Reliability → Discover Assets**
- You can:
    - View metadata
    - Run data profiling
    - Create and run Data Quality rules
    - Monitor reliability scores
    - Investigate failures using execution logs