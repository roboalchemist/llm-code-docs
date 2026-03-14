# Source: https://docs.acceldata.io/documentation/amazon-aurora-mysql.md

# Amazon Aurora MySQL

Amazon Aurora MySQL is a fully managed, MySQL-compatible relational database designed for high performance and availability on AWS.

By integrating **Amazon Aurora MySQL** with **Acceldata Data Observability Cloud (ADOC)**, teams can monitor data reliability, freshness, drift, and quality for Aurora-hosted datasets. This helps ensure that downstream analytics and applications are built on trusted, reliable data.

This integration is metadata-driven and read-only, ensuring zero impact on your production workloads.

## Prerequisites

ADOC supports the following authentication method for Aurora MySQL:

- **Username and Password–based authentication**
(MySQL native user)

Note Other authentication methods such as IAM Database Authentication, SSL certificates, or Kerberos are not supported as part of this integration.

The MySQL user configured in ADOC must have **read-only access** to fetch metadata and (optionally) sample data.

### Minimum Required Permissions

- `SELECT` on target databases and tables
- `SHOW VIEW` for view metadata
- `SELECT` on `information_schema` (for schema discovery)
- `SHOW DATABASES` (for database discovery)

### Example Minimum Grants

```sql
GRANT SELECT ON <database>.* TO 'your_username'@'%';
GRANT SHOW DATABASES ON *.* TO 'your_username'@'%';
```



## Supported Features

| Capability | Supported | Notes | 
| ---- | ---- | ---- | 
| Crawling | Yes | Discovers databases, tables, columns, constraints | 
| Data Profiling | Yes | Profiles column-level statistics | 
| Data Quality | Yes | Rule-based validation | 
| Data Freshness | Yes | Monitors update delays | 
| Data Reconciliation | Yes | Compares datasets for consistency | 
| Data Drift | Yes | Detects distribution changes | 
| Schema Drift | Yes | Identifies structural changes | 
| Rule Set Executions | Yes | Reusable validation logic | 
| Auto Anomaly Detection | No | Not supported | 


ADOC supports incremental crawling strategies where applicable, including:

- **ID-based incremental fetch**: Works when tables have primary keys or monotonically increasing identifiers.

## Add AWS Aurora MySQL as a Data Source

### Step 1: Start Setup

1. Select **Register** from the left main menu.
2. Select **Add Data Source** -&gt; **AWS Aurora MySQL** from the list of data sources.
3. On the **Data Source Details** page:

    1. Name the data source.
    2. Add a short description (optional).

4. Select a Data Plane from the dropdown where the data source will be managed. If you don’t have one yet, select [Set Up Data Plane](https://docs.acceldata.io/acceldata-data-observability-cloud/documentation/dataplane-installation) to create one.
5. Click **Next**.

### Step 2: Add Connection Details

Provide the following connection information:

- **Aurora MySQL Endpoint**
- **Port** (default: `3306`)
- **Username**
- **Password**

Click **Test Connection** to validate connectivity.

If the test is successful, click **Next**.

### Step 3: Set Up Observability

On the **Set Up Observability** page:

1. Select one or more **databases** to enable monitoring
2. (Optional) Enable **Crawler Execution Schedule** to keep metadata in sync
3. (Optional) Enable **Notify on Crawler Failure** to receive alerts

Click **Submit** to complete the setup.

## What's Next

After Aurora MySQL is onboarded:

- Metadata is crawled automatically
- Assets appear in **Reliability → Discover Assets**
- Users can configure data quality, freshness, drift, and reconciliation policies
- Reliability scores are calculated based on policy execution
- Changes to schema and data patterns are continuously tracked