# Source: https://developers.webflow.com/browser/data-exports/destinations.mdx

***

title: Data destinations
slug: data-exports/destinations
description: Overview of supported data destinations for Data Exports
---------------------------------------------------------------------

Data Exports supports a wide range of data destinations, allowing you to send your Analyze and Optimize data to your preferred data warehouse, database, or object storage solution.

## Supported destinations

### OLAP data warehouses

Cloud-based analytical data warehouses optimized for large-scale data analysis and reporting.

| Destination                                                                          | Description                                         |
| ------------------------------------------------------------------------------------ | --------------------------------------------------- |
| [Snowflake](/browser/data-exports/destinations/snowflake)                            | Cloud data platform with near-unlimited scalability |
| [Google BigQuery](/browser/data-exports/destinations/bigquery)                       | Serverless, highly scalable data warehouse          |
| [Amazon Redshift](/browser/data-exports/destinations/redshift)                       | Fully managed data warehouse service                |
| [Amazon Redshift Serverless](/browser/data-exports/destinations/redshift-serverless) | Serverless option for Redshift                      |
| [Amazon Athena](/browser/data-exports/destinations/athena)                           | Serverless query service for S3                     |
| [Databricks](/browser/data-exports/destinations/databricks)                          | Unified analytics platform                          |
| [ClickHouse](/browser/data-exports/destinations/clickhouse)                          | Column-oriented database for analytics              |
| [MotherDuck](/browser/data-exports/destinations/motherduck)                          | Serverless analytics with DuckDB                    |

### Open table formats

Open-source table formats that provide ACID transactions on data lakes.

| Destination                                                         | Description                                      |
| ------------------------------------------------------------------- | ------------------------------------------------ |
| [Delta Lake](/browser/data-exports/destinations/delta-lake)         | Open-source storage layer with ACID transactions |
| [Apache Iceberg](/browser/data-exports/destinations/apache-iceberg) | Open table format for large analytic tables      |

### OLTP databases

Transactional databases for operational workloads.

| Destination                                                             | Description           |
| ----------------------------------------------------------------------- | --------------------- |
| [PostgreSQL](/browser/data-exports/destinations/postgres)               | PostgreSQL database   |
| [Aurora PostgreSQL](/browser/data-exports/destinations/aurora-postgres) | AWS Aurora PostgreSQL |
| [MySQL](/browser/data-exports/destinations/mysql)                       | MySQL database        |
| [Aurora MySQL](/browser/data-exports/destinations/aurora-mysql)         | AWS Aurora MySQL      |
| [SQL Server](/browser/data-exports/destinations/sql-server)             | Microsoft SQL Server  |
| [Oracle](/browser/data-exports/destinations/oracle)                     | Oracle Database       |
| [MongoDB](/browser/data-exports/destinations/mongodb)                   | Document database     |

### Object storage

Cloud-based file storage for data lakes and archival.

| Destination                                                                     | Description                                            |
| ------------------------------------------------------------------------------- | ------------------------------------------------------ |
| [Amazon S3](/browser/data-exports/destinations/s3)                              | AWS object storage                                     |
| [S3-compatible storage](/browser/data-exports/destinations/s3-compatible)       | Object storage platforms that support S3 compatibility |
| [Google Cloud Storage](/browser/data-exports/destinations/google-cloud-storage) | GCP object storage                                     |
| [Azure Blob Storage](/browser/data-exports/destinations/azure-blob-storage)     | Azure object storage                                   |
| [SFTP](/browser/data-exports/destinations/sftp)                                 | Secure file transfer                                   |

### Spreadsheets

Spreadsheet destinations for smaller datasets and reporting.

| Destination                                                       | Description               |
| ----------------------------------------------------------------- | ------------------------- |
| [Google Sheets](/browser/data-exports/destinations/google-sheets) | Google Sheets integration |

## Common configuration steps

Most destinations follow a similar setup process:

1. **Create a dedicated user** - Create a special-purpose user in your destination to perform write operations
2. **Configure permissions** - Grant the necessary permissions for the user to create schemas, tables, and write data
3. **Allowlist IP addresses** - Add the required IP addresses to your destination's firewall or security group
4. **Add credentials** - Enter your destination's connection details and credentials in the Data Exports settings

## Format of landed data

### Data warehouses and databases

Data transferred to data warehouses and relational databases is loaded as properly typed tables within a single schema. A `_transfer_status` table records transfer metadata, including a `transfer_last_updated_at` timestamp for each table.

### Object storage

Data transferred to object storage destinations is loaded as Apache Parquet files (recommended) or CSV/JSON in Apache Hive-style partitions:

```
<bucket>/<folder>/<model>/dt=<date>/<part>_<timestamp>.parquet
```

Where:

* `<model>` is the data model name (equivalent to a table name)
* `<date>` is the transfer date (e.g., `2024-01-15`)
* `<timestamp>` is the transfer timestamp

### Spreadsheets

Data transferred to spreadsheet destinations is loaded as a new tab per data model. Where possible, tabs are created as protected (read-only) to prevent accidental modification.

## Next steps

Select your destination from the list above to view detailed configuration instructions.
