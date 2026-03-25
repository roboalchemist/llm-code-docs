# Source: https://docs.snowflake.com/en/user-guide/intro-supported-features.md

# Overview of key features

This topic lists the notable and significant features supported in the current release. It *doesn’t* list every feature provided
by Snowflake.

## Security, governance, and data protection

* Choose the geographical location where your data is stored, based on your [region](intro-regions.md).
* [User authentication](admin-user-management.md) through standard user/password credentials.
* Enhanced authentication:

  * [Multi-factor authentication (MFA)](security-mfa.md).
  * [Federated authentication and single sign-on (SSO)](admin-security-fed-auth-overview.md).
  * [Snowflake OAuth](oauth-snowflake-overview.md).
  * [External OAuth](oauth-ext-overview.md).
  * [Key-pair authentication](key-pair-auth.md).
  * [Authentication through programmatic access tokens](programmatic-access-tokens.md).
* All communication between clients, including all Snowflake connectors and drivers, and the server is protected through TLS.
* Deployment inside a cloud platform VPC (AWS or GCP) or VNet (Azure).
* Isolation of data (for loading and unloading) using:

  * [Amazon S3 policy controls](data-load-s3-config.md).
  * [Azure storage access controls](data-load-azure-config.md).
  * [Google Cloud Storage access permissions](data-load-gcs-config.md).
* Support for PHI data (in compliance with HIPAA and [HITRUST CSF](intro-cloud-platforms.md) regulations) — requires Business Critical
  Edition (or higher).
* Automatic [data encryption](security-encryption-end-to-end.md) by Snowflake using Snowflake-managed keys.
* [Object-level access control](security-access-control-overview.md).
* [Snowflake Time Travel](data-time-travel.md) (1 day standard for all accounts; additional days, up to 90, allowed with
  Snowflake Enterprise) for:

  * Querying historical data in tables.
  * Restoring and cloning historical data in databases, schemas, and tables.
* [Snowflake Fail-safe](data-failsafe.md) (7 days standard for all accounts) for disaster recovery of historical data.
* [Column-level Security](security-column-intro.md) to apply masking policies to columns in tables or views — requires Enterprise
  Edition (or higher).
* [Row-level Security](security-row-intro.md) to apply row access policies to tables and views — requires Enterprise Edition (or
  higher).
* [Introduction to object tagging](object-tagging/introduction.md) to apply tags to Snowflake objects to facilitate tracking sensitive data and resource usage
  — requires Enterprise Edition (or higher).
* [Differential privacy](diff-privacy/differential-privacy-overview.md) to protect data against targeted privacy attacks.
  — requires Enterprise Edition (or higher).

## Standard and extended SQL support

* Most DDL defined in SQL:1999, including:

  * [Databases, schemas, tables, and related objects](../sql-reference/sql-ddl-summary.md).
  * [Core data types](../sql-reference-data-types.md).
  * [SET operations](../sql-reference/constructs.md).
  * [CAST functions](../sql-reference/functions-conversion.md).
* [Standard DML](../sql-reference/sql-dml.md) such as UPDATE, DELETE, and INSERT, as well as more advanced DML:

  * [Multi-table INSERT, MERGE, and multi-merge](../sql-reference/sql-dml.md).
  * [DML for bulk data loading/unloading](../sql-reference/sql-dml.md).
* [Iceberg tables](tables-iceberg.md).
* [Transactions](../sql-reference/transactions.md).
* [Temporary and transient tables](../sql-reference/sql/create-table.md) for transitory data.
* [Lateral views](../sql-reference/constructs/from.md).
* [Materialized views](views-materialized.md).
* [Statistical aggregate functions](../sql-reference/functions-aggregation.md).
* [Analytical aggregates (Group by cube, rollup, and grouping sets)](../sql-reference/constructs/group-by.md).
* Parts of the SQL:2003 analytic extensions:

  * [Window functions](../sql-reference/functions-window.md).
  * [Grouping sets](../sql-reference/constructs/group-by.md).
* Scalar and tabular [user-defined functions (UDFs)](../developer-guide/udf/udf-overview.md), with support for Java, JavaScript,
  Python, Scala, and SQL.
* [Stored procedures](../developer-guide/stored-procedure/stored-procedures-overview.md) and procedural language support
  ([Snowflake Scripting](../developer-guide/snowflake-scripting/index.md))
* [Snowflake Information Schema](../sql-reference/info-schema.md) for querying object and account metadata, as well as query and warehouse usage history data.
* Recursive queries, including:

  * [CONNECT BY](../sql-reference/constructs/connect-by.md).
  * [Recursive CTE (common table expressions)](../sql-reference/constructs/with.md).
* [Collation support](../sql-reference/collation.md).
* [Geospatial data support](../sql-reference/data-types-geospatial.md).

## Tools and interfaces

* [Snowsight](ui-snowsight-quick-tour.md) for account and general management, monitoring of resources and system usage, and
  querying data.
* [Snowflake CLI (open source command-line client)](../developer-guide/snowflake-cli/index.md).
* [SnowSQL (Python-based command line client)](snowsql.md).
* Virtual warehouse management from the GUI or command line, including
  [creating, resizing (with zero downtime), suspending, and dropping](warehouses.md) warehouses.
* [Snowflake Extension for Visual Studio Code](vscode-ext.md) - Detailed instructions for installing, configuring and using the Snowflake Extension for Visual Studio Code.

## Apps and extensibility

* [APIs for Java, Python, and Scala](../developer-guide/snowpark/index.md) with which you can build applications that process data in
  Snowflake without moving data to the system where your application code runs.
* A [framework for creating applications](../developer-guide/native-apps/native-apps-about.md)
  to share data content and application logic with other Snowflake accounts.
* A [RESTful API](../developer-guide/sql-api/index.md) for accessing and updating data.
* Support for running [Streamlit apps natively in Snowflake](../developer-guide/streamlit/about-streamlit.md)
  to create and share custom web apps for machine learning and data science.
* Support for [developing procedures and user-defined functions (UDFs)](../developer-guide/extensibility.md) with a handler in one of
  several programming languages.
* Extensive set of client connectors and drivers provided by Snowflake:

  * [Python connector](../developer-guide/python-connector/python-connector.md)
  * [Spark connector](spark-connector.md)
  * [Node.js driver](../developer-guide/node-js/nodejs-driver.md)
  * [Go Snowflake driver](../developer-guide/golang/go-driver.md)
  * [.NET driver](../developer-guide/dotnet/dotnet-driver.md)
  * [JDBC client driver](../developer-guide/jdbc/jdbc.md)
  * [ODBC client driver](../developer-guide/odbc/odbc.md)
  * [PHP PDO driver](../developer-guide/php-pdo/php-pdo-driver.md)
* [Snowpark Container Services](../developer-guide/snowpark-container-services/overview.md) is a fully managed container offering that helps you easily deploy, manage, and scale containerized applications.

## Connectivity

* Broad [ecosystem](ecosystem.md) of supported 3rd-party partners and technologies.
* Support for using free trials to [connect to selected partners](ecosystem-partner-connect.md).

## Data import and export

* Support for bulk [loading](../guides-overview-loading-data.md) and [unloading](data-unload-overview.md) data into/out of tables, including:

  * Load any data that uses a supported character encoding.
  * Load data from compressed files.
  * Load most flat, delimited data files (CSV, TSV, etc.).
  * Load data files in JSON, Avro, ORC, Parquet, and XML format.
  * Load from files in cloud storage or local files using the Snowflake web interface or command-line client.
* Support for continuous data loading from files:

  * Use [Snowpipe](data-load-snowpipe-intro.md) to load data in micro-batches from internal (i.e. Snowflake) stages or external
    (Amazon S3, Google Cloud Storage, or Microsoft Azure) stages.
* Support for accessing data in [S3-compatible storage](data-load-s3-compatible-storage.md).

## Data sharing

* Support for both [sharing data in secured objects](../guides-overview-sharing.md) and [sharing data in non-secure views](../guides-overview-sharing.md) with other Snowflake accounts:

  * Provide data to other accounts to consume.
  * Consume data provided by other accounts.
* Support for collaborators using [Snowflake Data Clean Rooms](cleanrooms/introduction.md) to share data in a privacy-preserving environment.

## Replication and failover

* Support for [replication and failover](account-replication-intro.md) across multiple Snowflake accounts in
  different [regions](intro-regions.md) and [cloud platforms](intro-cloud-platforms.md):

  * Replicate objects between Snowflake accounts (within the same organization) and keep the objects and stored data synchronized.
  * Configure failover to one or more Snowflake accounts for business continuity and disaster recovery.
