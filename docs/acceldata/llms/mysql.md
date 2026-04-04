# Source: https://docs.acceldata.io/documentation/mysql.md

# MySQL

MySQL is a widely adopted open-source relational database. With the MySQL connector, the Acceldata Data Observability Cloud (ADOC) enables complete reliability monitoring across your MySQL datasets—including asset discovery, metadata crawling, profiling, data quality checks, and policy execution.

This guide explains how to register MySQL as a data source in ADOC and begin monitoring your MySQL environment.

## Prerequisites

Ensure the following requirements are met before you connect MySQL as a data source::

- A running MySQL instance accessible from your ADOC Data Plane.
- Credentials with permission to read system metadata and query the selected databases.
- A Data Plane already set up—or permission to create one.

## Add MySQL as a Data Source

### Step 1: Start Setup

1.  Click **Register** from the left main menu.
2. Click **Add Data Source**.
3. Select **MySQL** from the list of supported connectors. The **Data Source Details** page is displayed. 
4. Enter a **Data Source Name** (for example: MySQL Prod).
5. (Optional) Add a **Description** to help others identify the connection.
6. Ensure the **Data Reliability** toggle is enabled.
7. From **Select Data Plane**, choose an existing Data Plane or click [Set up Data Plane](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/dataplane-installation-prerequisites) to create one.
8. Click **Next** to proceed to the **Connection Details** page.

### Step 2: Enter Connection Details

On the **Connection Details** page:

9. Provide the MySQL JDBC URL. Format example: j`dbc:mysql://<HOST>:<PORT>/<DB>`
10. Enter the **Username**.
11. Enter the **Password**.
12. Click **Test Connection** to verify access. If successful, click **Next**, else check the URL, port, firewall rules, or credentials.

### Step 3: Set Up Observability

On the **Observability Set Up** page:

13. Add one or more **Databases** that ADOC should monitor. Click  **Add** to include multiple databases.
14. (Optional) Enable **Crawler Execution Schedule** to set:
    - Frequency (hourly/daily)
    - Time of day
    - Time zone

15. Click **Submit** to complete the registration.

## What's Next

After submission:

- MySQL appears as a new data-source tile in the **Data Sources** page.
- You can choose to run the initial crawl immediately or allow it to run during the scheduled execution.
- Once crawled, MySQL assets will appear under **Reliability → Discover Assets**, where you can:
    - View schema and metadata
    - Configure data quality, freshness, and reconciliation policies
    - Monitor change history and alerts