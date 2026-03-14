# Source: https://docs.acceldata.io/documentation/mariadb.md

# MariaDB

Connect your MariaDB instance to the Acceldata Data Observability Cloud (ADOC) platform to monitor data quality, schema changes, and anomalies. This integration helps ensure your database tables remain accurate, consistent, and reliable.

Once connected, you can:

- Check for missing or inconsistent data in your MariaDB tables
- Track how often data is updated (freshness)
- Detect schema changes in your database
- Run scheduled crawls to profile data automatically

This helps ensure your MariaDB data is reliable for reporting and downstream processes.

## Prerequisites

Ensure the following requirements are met before you connect MariaDB as a data source:

- JDBC URL, username, and password for your MariaDB instance.
- A Data Plane set up in ADOC.

## Add MariaDB as a Data Source

### Step 1: Start Setup

1. Click **Register** from the left main menu.
2. Click **Add Data Source**.
3. Choose **MariaDB** from the list.
4. On the **Data Source Details** page:
    1. Enter a name for the data source.
    2. (Optional) Add a short description.
    3. Choose an existing **Data Plane**, or click **Setup Data Plane** to create one.  Note _You need a Data Plane to enable data reliability features._

5. Click Next.

### Step 2: Add Connection Details

1. Enter your **JDBC URL**, **Username**, and **Password**.
2. Click **Test Connection**. Note  _If_ _the connection is successful, you'll see a “Connected” message. If not, check the credentials and try again._
3. Click Next.

### Step 3: Set Up Observability

1. Turn on **Enable Crawler Execution Schedule** to scan your MariaDB data on a regular basis.
2. Choose a **time** and **time zone** for the crawler to run.
3. Click **Submit**.

You’ve now successfully added MariaDB as a data source. It will appear on your Data Sources page, where you can trigger crawlers or review metadata.

## What's Next

After you connect MariaDB, you can go to the following pages to view and manage your data:

- **Reliability** – View data quality scores, profiling status, and rule results for your MariaDB datasets.
- **Pipelines** – Monitor how data flows from MariaDB to downstream systems.
- **Alerts** – See notifications for quality issues or pipeline delays in real time.