# Source: https://docs.snowflake.com/en/user-guide/intro-editions.md

# Snowflake editions

Snowflake offers multiple editions to choose from, ensuring that your usage fits your organization’s specific requirements. Each successive
edition builds on the previous edition through the addition of edition-specific features and/or higher levels of service. As your
organization’s needs change and grow, changing editions is easy.

For information about working with editions, including viewing and changing an account’s edition, see [Working with account editions](organizations-manage-accounts-editions.md).

> **Note:**
>
> The Snowflake Edition that your organization chooses determines the unit costs for the credits and the data storage you use. Other factors
> that impact unit costs are the [region](intro-regions.md) where your Snowflake account is located and whether it is
> an *On Demand* or *Capacity* account:
>
> * On Demand: Usage-based pricing with no long-term licensing requirements.
> * Capacity: Discounted pricing based on an upfront Capacity commitment.
>
> For pricing details, see the [pricing page](http://www.snowflake.com/pricing) (on the Snowflake website).

## Overview of editions

### Standard Edition

Standard Edition is our introductory level offering, providing full, unlimited access to all of Snowflake’s standard features. It provides
a strong balance between features, level of support, and cost.

### Enterprise Edition

Enterprise Edition provides all the features and services of Standard Edition, with additional features
that are designed specifically for the needs of large-scale enterprises and organizations.

### Business Critical Edition

Business Critical Edition, formerly known as Enterprise for Sensitive Data (ESD), offers even higher levels of data protection to support
the needs of organizations with extremely sensitive data, particularly PHI data that must comply with HIPAA and
[HITRUST CSF](intro-cloud-platforms.md) regulations.

It includes all the features and services of Enterprise Edition, with the addition of enhanced security and data
protection. In addition, account failover/failback adds support for business continuity and disaster recovery.

> **Note:**
>
> As required by HIPAA and [HITRUST CSF](intro-cloud-platforms.md) regulations, before any PHI data can be stored in Snowflake, a
> signed business associate agreement (BAA) must be in place between your agency/organization and Snowflake Inc.

### Virtual Private Snowflake (VPS)

Virtual Private Snowflake offers our highest level of security for organizations that have the strictest requirements, such as financial
institutions and any other large enterprises that collect, analyze, and share highly sensitive data.

It includes all the features and services of Business Critical Edition, but in a completely separate Snowflake
environment, isolated from all other Snowflake accounts (i.e. VPS accounts do not share any type of hardware resources with accounts outside the VPS).

> **Note:**
>
> To access your account, you can use an [account identifier](admin-account-identifier.md) that specifies your
> organization name and account name.
>
> If you instead choose to use an [account locator](admin-account-identifier.md) as the account identifier, note that
> the account locator for VPS accounts uses a different format than the accounts for other Snowflake Editions. For details, see
> [Finding the account locator format for a VPS account](admin-account-identifier.md).

## Find your current edition

You can find the Snowflake edition for your account in the following ways:

* To find your Snowflake edition by using Snowsight, follow the instructions in
  [Locate your Snowflake account information in Snowsight](ui-snowsight-gs.md).
* To find your Snowflake edition by using SQL, query the
  [ACCOUNTS view](../sql-reference/organization-usage/accounts.md) in the ORGANIZATION_USAGE schema,
  and select the `edition` column:

  ```sqlexample
  SELECT edition
    FROM SNOWFLAKE.ORGANIZATION_USAGE.ACCOUNTS
    WHERE account_name = CURRENT_ACCOUNT();
  ```

  To query this view, you must have [access to the ORGANIZATION_USAGE schema](../sql-reference/organization-usage.md).

## Feature and edition matrix

The following tables provide a list of the major features and services included with each edition.

> **Note:**
>
> This is only a partial list of the features. For a more complete and detailed list, see [Overview of key features](intro-supported-features.md).

### Release management

| Feature/Service | Standard | Enterprise | Business Critical | VPS |
| --- | --- | --- | --- | --- |
| 24-hour [early access to weekly new releases](intro-releases.md), which can be used for additional testing or validation before each release is deployed to your production accounts. |  | ✔ | ✔ | ✔ |

### Security, governance, and data protection

| Feature/Service | Standard | Enterprise | Business Critical | VPS |
| --- | --- | --- | --- | --- |
| SOC 2 Type II certification. | ✔ | ✔ | ✔ | ✔ |
| [Federated authentication and SSO](admin-security-fed-auth-overview.md) for centralizing and streamlining user authentication. | ✔ | ✔ | ✔ | ✔ |
| [OAuth](oauth-intro.md) for authorizing account access without sharing or storing user login credentials. | ✔ | ✔ | ✔ | ✔ |
| [Network policies](network-policies.md) for limiting/controlling site access by user IP address. | ✔ | ✔ | ✔ | ✔ |
| Automatic [encryption of all data](../guides-overview-secure.md). | ✔ | ✔ | ✔ | ✔ |
| Support for [multi-factor authentication](security-mfa.md). | ✔ | ✔ | ✔ | ✔ |
| Object-level [access control](security-access-control-overview.md). | ✔ | ✔ | ✔ | ✔ |
| Standard [Time Travel](data-time-travel.md) (up to 1 day) for accessing/restoring modified and deleted data. | ✔ | ✔ | ✔ | ✔ |
| [Object tags](object-tagging/introduction.md) that can be applied to Snowflake objects to help track sensitive data and resource usage. Some tagging features require Enterprise Edition or higher. | ✔ | ✔ | ✔ | ✔ |
| Disaster recovery of modified/deleted data (for 7 days beyond Time Travel) through [Fail-safe](data-failsafe.md). | ✔ | ✔ | ✔ | ✔ |
| [Generating synthetic data](synthetic-data.md) |  | ✔ | ✔ | ✔ |
| [Extended Time Travel](data-time-travel.md) (up to 90 days). |  | ✔ | ✔ | ✔ |
| [Periodic rekeying of encrypted data](security-encryption-manage.md) for increased protection. |  | ✔ | ✔ | ✔ |
| [Column-level Security](security-column-intro.md) to apply masking policies to columns in tables or views. |  | ✔ | ✔ | ✔ |
| [Row-level Security](security-row-intro.md) to apply row access policies to determine which rows are visible in a query result. |  | ✔ | ✔ | ✔ |
| [Aggregation policies](aggregation-policies.md) that enforce privacy by requiring queries to aggregate data to return results. |  | ✔ | ✔ | ✔ |
| [Projection policies](projection-policies.md) that restrict who can use a SELECT statement to project a column. |  | ✔ | ✔ | ✔ |
| [Differential privacy](diff-privacy/differential-privacy-overview.md) to protect data against targeted privacy attacks. |  | ✔ | ✔ | ✔ |
| Support for classifying potentially sensitive data using [classification](classify-intro.md). |  | ✔ | ✔ | ✔ |
| Audit the user access history through the Account Usage [ACCESS_HISTORY](../sql-reference/account-usage/access_history.md) view. |  | ✔ | ✔ | ✔ |
| Event tables associated with a database by [associating an event table with an object](../developer-guide/logging-tracing/event-table-setting-up.md). |  | ✔ | ✔ | ✔ |
| Customer-managed encryption keys through [Tri-Secret Secure](security-encryption-manage.md). |  |  | ✔ | ✔ |
| Support for private connectivity [to the Snowflake service](private-connectivity-inbound.md). |  |  | ✔ | ✔ |
| Support for private connectivity [to Snowflake internal stages](private-connectivity-inbound.md). |  |  | ✔ | ✔ |
| Support for [Pinning private connectivity endpoints for inbound traffic](pin-private-endpoints.md). |  |  | ✔ | ✔ |
| Support for [private connectivity for inbound network traffic in Snowflake Open Catalog](https://other-docs.snowflake.com/en/opencatalog/private-connectivity-inbound). |  |  | ✔ | ✔ |
| Support for private connectivity for outbound network traffic [to external stages](private-connectivity-outbound.md). |  |  | ✔ | ✔ |
| Support for private connectivity for outbound network traffic [to external volumes for Apache Iceberg tables](private-connectivity-outbound.md). |  |  | ✔ | ✔ |
| Support for private connectivity to a key management service through [Tri-Secret Secure](security-encryption-tss-self-serve-private.md). |  | . | ✔ | ✔ |
| Support for private connectivity to the Snowflake service using AWS PrivateLink, Azure Private Link, or Google Cloud Private Service Connect. |  |  | ✔ | ✔ |
| Support for private connectivity to Snowflake internal stages using [AWS PrivateLink](private-internal-stages-aws.md), [Azure Private Link](private-internal-stages-azure.md), and [Google Cloud](private-internal-stages-gcp.md) |  |  | ✔ | ✔ |
| Support for [Pinning private connectivity endpoints for inbound traffic](pin-private-endpoints.md). |  |  | ✔ | ✔ |
| Support for [Cross-Region Connectivity for AWS PrivateLink](admin-security-privatelink.md). |  | . | ✔ | ✔ |
| Support for [private connectivity for inbound network traffic in Snowflake Open Catalog](https://other-docs.snowflake.com/en/opencatalog/private-connectivity-inbound). |  |  | ✔ | ✔ |
| Support for [private connectivity for outbound network traffic in Snowflake Open Catalog](https://other-docs.snowflake.com/en/opencatalog/private-connectivity-outbound). |  |  | ✔ | ✔ |
| Support for PHI data (in accordance with HIPAA and [HITRUST CSF](intro-cloud-platforms.md) regulations). |  |  | ✔ | ✔ |
| Support for PCI DSS. |  |  | ✔ | ✔ |
| Support for public sector workloads that meet U.S. Federal and state government requirements, such as [FedRAMP and ITAR](intro-regions.md). |  |  | ✔ | ✔ |
| Support for IRAP - Protected (P) data (in specified [Asia Pacific regions](intro-regions.md)). |  |  | ✔ | ✔ |
| Dedicated metadata store and pool of compute resources (used in virtual warehouses). |  |  |  | ✔ |
| [Data Quality and data metric functions](data-quality-intro.md) to monitor the state and integrity of data. |  | ✔ | ✔ | ✔ |

### Compute Resource Management

| Feature/Service | Standard | Enterprise | Business Critical | VPS |
| --- | --- | --- | --- | --- |
| [Virtual warehouses](warehouses.md), separate compute clusters for isolating query and data loading workloads. | ✔ | ✔ | ✔ | ✔ |
| [Resource monitors](resource-monitors.md) for monitoring virtual warehouse credit usage. | ✔ | ✔ | ✔ | ✔ |
| [Multi-cluster virtual warehouses](warehouses-multicluster.md) for scaling compute resources to meet concurrency needs. |  | ✔ | ✔ | ✔ |

### SQL support

| Feature/Service | Standard | Enterprise | Business Critical | VPS |
| --- | --- | --- | --- | --- |
| [Standard SQL](../sql-reference-commands.md), including most DDL and DML defined in SQL:1999. | ✔ | ✔ | ✔ | ✔ |
| [Advanced DML](../sql-reference/sql-dml.md) such as multi-table INSERT, MERGE, and multi-merge. | ✔ | ✔ | ✔ | ✔ |
| Broad support for standard [data types](../sql-reference-data-types.md). | ✔ | ✔ | ✔ | ✔ |
| Native support for [semi-structured data](semistructured-intro.md) (JSON, Avro, ORC, Parquet, and XML). | ✔ | ✔ | ✔ | ✔ |
| Native support for [geospatial data](../sql-reference/data-types-geospatial.md). | ✔ | ✔ | ✔ | ✔ |
| Native support for [unstructured data](unstructured-intro.md). | ✔ | ✔ | ✔ | ✔ |
| [Collation rules](../sql-reference/collation.md) for string/text data in table columns. | ✔ | ✔ | ✔ | ✔ |
| [Integrity constraints](../sql-reference/constraints.md) (not enforced) on table columns for informational and modeling purposes. | ✔ | ✔ | ✔ | ✔ |
| Multi-statement [transactions](../sql-reference/transactions.md). | ✔ | ✔ | ✔ | ✔ |
| [User-defined functions (UDFs)](../developer-guide/udf/udf-overview.md) with support for Java, JavaScript, Python, and SQL. | ✔ | ✔ | ✔ | ✔ |
| [External access](../developer-guide/external-network-access/external-network-access-overview.md) for enabling user-defined functions (UDFs) or stored procedures to securely connect to external network locations, such as a third-party API or another database. | ✔ | ✔ | ✔ | ✔ |
| [External functions](../sql-reference/external-functions.md) for extending Snowflake to other development platforms. | ✔ | ✔ | ✔ | ✔ |
| [Amazon API Gateway private endpoints for external functions](../sql-reference/external-functions-creating-aws-planning.md). |  |  | ✔ | ✔ |
| [Stored procedures](../developer-guide/stored-procedure/stored-procedures-overview.md) with support for Java, JavaScript, Python, Scala, and SQL (Snowflake Scripting). | ✔ | ✔ | ✔ | ✔ |
| [Dynamic tables](dynamic-tables-about.md) for automatically materializing the results of a specified SQL query and keeping them up to date to meet your data freshness target. | ✔ | ✔ | ✔ | ✔ |
| [External tables](tables-external-intro.md) for referencing data in a cloud storage data lake. | ✔ | ✔ | ✔ | ✔ |
| [Hybrid tables](tables-hybrid.md) for data in transactional and analytical workloads. | ✔ | ✔ | ✔ | ✔ |
| Support for [clustering data](tables-clustering-keys.md) in very large tables to improve query performance, with automatic maintenance of clustering. | ✔ | ✔ | ✔ | ✔ |
| [Query acceleration](query-acceleration-service.md) for parallel processing portions of eligible queries. |  | ✔ | ✔ | ✔ |
| [Search optimization](search-optimization-service.md) for point lookup queries, with automatic maintenance. |  | ✔ | ✔ | ✔ |
| [Snowflake Optima](snowflake-optima.md) for automatic workload performance improvements. | ✔ | ✔ | ✔ | ✔ |
| [Materialized views](views-materialized.md), with automatic maintenance of results. |  | ✔ | ✔ | ✔ |
| [Iceberg tables](tables-iceberg.md) for referencing data in a cloud storage data lake. | ✔ | ✔ | ✔ | ✔ |
| [Schema detection](data-load-overview.md) for automatically detecting the schema in a set of staged semi-structured data files and retrieving the column definitions. | ✔ | ✔ | ✔ | ✔ |
| [Schema evolution](data-load-schema-evolution.md) for automatically evolving tables to support the structure of new data received from the data sources. | ✔ | ✔ | ✔ | ✔ |

### Interfaces and tools

| Feature/Service | Standard | Enterprise | Business Critical | VPS |
| --- | --- | --- | --- | --- |
| [Snowsight](ui-snowsight.md), the next-generation SQL worksheet for advanced query development, data analysis, and visualization. | ✔ | ✔ | ✔ | ✔ |
| [Snowflake CLI](../developer-guide/snowflake-cli/index.md), Open-source command-line tool explicitly designed for developer-centric workloads in addition to SQL operations, including querying, executing DDL/DML commands, and bulk loading/unloading of data. | ✔ | ✔ | ✔ | ✔ |
| [SnowSQL](snowsql.md), a command line client for building/testing queries, loading/unloading bulk data, and automating DDL operations. | ✔ | ✔ | ✔ | ✔ |
| [SnowCD](snowcd.md), a command line diagnostic tool for identifying and fixing client connectivity issues. | ✔ | ✔ | ✔ | ✔ |
| Programmatic interfaces for [Python](../developer-guide/python-connector/python-connector.md), [Spark](spark-connector.md), [Node.js](../developer-guide/node-js/nodejs-driver.md), [.NET.js](../developer-guide/dotnet/dotnet-driver.md), [PHP](../developer-guide/php-pdo/php-pdo-driver.md), and [Go](../developer-guide/golang/go-driver.md). | ✔ | ✔ | ✔ | ✔ |
| Native support for [JDBC](../developer-guide/jdbc/jdbc.md) and [ODBC](../developer-guide/odbc/odbc.md). | ✔ | ✔ | ✔ | ✔ |
| [Snowflake SQL API](../developer-guide/sql-api/index.md), a REST API for accessing and updating data in a Snowflake database. | ✔ | ✔ | ✔ | ✔ |
| Extensive [ecosystem](ecosystem.md) for connecting to ETL, BI, and other third-party vendors and technologies. | ✔ | ✔ | ✔ | ✔ |
| [Snowflake Partner Connect](ecosystem-partner-connect.md) for initiating free software/service trials with a growing network of partners in the Snowflake ecosystem. | ✔ | ✔ | ✔ | ✔ |
| [Snowpark](../developer-guide/snowpark/index.md), the set of libraries and runtimes that securely deploy and process non-SQL code, including Python, Java, and Scala. | ✔ | ✔ | ✔ | ✔ |
| [Streamlit in Snowflake](../developer-guide/streamlit/about-streamlit.md) for building, deploying, and sharing Streamlit apps on Snowflake data cloud. | ✔ | ✔ | ✔ | ✔ |

### Data import and export

| Feature/Service | Standard | Enterprise | Business Critical | VPS |
| --- | --- | --- | --- | --- |
| [Bulk loading](../guides-overview-loading-data.md) from delimited flat files (CSV, TSV, etc.) and semi-structured data files (JSON, Avro, ORC, Parquet, and XML). | ✔ | ✔ | ✔ | ✔ |
| [Bulk unloading](data-unload-overview.md) to delimited flat files and JSON files. | ✔ | ✔ | ✔ | ✔ |
| [Snowpipe](data-load-snowpipe-intro.md) for continuous micro-batch loading. | ✔ | ✔ | ✔ | ✔ |
| [Snowpipe Streaming](snowpipe-streaming/data-load-snowpipe-streaming-overview.md) for low-latency loading of streaming data. | ✔ | ✔ | ✔ | ✔ |
| [Snowflake Connector for Kafka](kafka-connector.md) for loading data from Apache Kafka topics. | ✔ | ✔ | ✔ | ✔ |

### Data pipelines

| Feature/Service | Standard | Enterprise | Business Critical | VPS |
| --- | --- | --- | --- | --- |
| [Streams](streams-intro.md) for tracking table changes. | ✔ | ✔ | ✔ | ✔ |
| [Tasks](tasks-intro.md) for scheduling the execution of SQL statements, often in conjunction with table streams. | ✔ | ✔ | ✔ | ✔ |

### Data replication and failover

| Feature/Service | Standard | Enterprise | Business Critical | VPS |
| --- | --- | --- | --- | --- |
| [Database and share replication](account-replication-intro.md) between Snowflake accounts (within an organization) to synchronize databases, shared objects, and stored data. | ✔ | ✔ | ✔ | ✔ |
| [Failover and failback](account-replication-failover-failback.md) between Snowflake accounts for business continuity and disaster recovery. |  |  | ✔ | ✔ |
| [Redirecting client connections](client-redirect.md) between Snowflake accounts for business continuity and disaster recovery. |  |  | ✔ | ✔ |

### Data sharing

| Feature/Service | Standard | Enterprise | Business Critical | VPS |
| --- | --- | --- | --- | --- |
| Snowflake Marketplace | ✔ | ✔ | ✔ |  |
| Universal Search | ✔ | ✔ | ✔ | ✔ |
| Build data products, monetize listings, and analyze your successes in Snowflake Marketplace. | ✔ | ✔ | ✔ |  |
| Public Listings | ✔ | ✔ | ✔ |  |
| Private Listings | ✔ | ✔ | ✔ | ✔ |
| With VPS, collaborate privately while strictly upholding requirements for security and isolation. |  |  |  | ✔ |
| Make data accessible without moving it using cross-cloud auto-fulfillment powered by Snowgrid™. | ✔ | ✔ | ✔ | ✔ |
| Collaborate with [Snowflake Data Clean Rooms](cleanrooms/introduction.md). | ✔ | ✔ | ✔ |  |
| Create and manage your own Snowflake Data Clean Rooms. |  | ✔ | ✔ | ✔ |
| Collaborate using one of Snowflake’s many collaborative technologies. | ✔ | ✔ | ✔ | ✔ |
| Replicate shared data to keep it synchronized within your organization. | ✔ | ✔ | ✔ | ✔ |

### Artificial intelligence and machine learning

| Feature/Service | Standard | Enterprise | Business Critical | VPS |
| --- | --- | --- | --- | --- |
| Use [Snowflake Cortex AI Functions](snowflake-cortex/aisql.md) to respond to plain-language prompts, answer questions, summarize or translate text, find similar documents, and more. | ✔ | ✔ | ✔ | ✔ |
| Use [Snowflake Copilot](snowflake-copilot.md) to engage in conversations about your structured data. | ✔ | ✔ | ✔ | ✔ |
| Use [Cortex Analyst](snowflake-cortex/cortex-analyst.md) to help write applications that can engage in conversations about your structured data. | ✔ | ✔ | ✔ | ✔ |
| Use [Cortex Fine-tuning](snowflake-cortex/cortex-finetuning.md) to create large language models specialized for your needs without the usual training costs. | ✔ | ✔ | ✔ | ✔ |
| Use [Cortex Search](snowflake-cortex/cortex-search/cortex-search-overview.md) to enable high-quality semantic search over your Snowflake data. | ✔ | ✔ | ✔ | ✔ |
| Use [Document AI](snowflake-cortex/document-ai/overview.md) to extract data from PDFs and other documents and to create pipelines for processing documents of a specific type. | ✔ | ✔ | ✔ | ✔ |
| Use [ML Functions](../guides-overview-ml-functions.md) to analyze your data using our machine-learning models trained on your data. | ✔ | ✔ | ✔ | ✔ |
| Use the [Snowflake Model Registry](../developer-guide/snowflake-ml/model-registry/overview.md) as a central repository for machine learning models within your organization. | ✔ | ✔ | ✔ | ✔ |
| Use the [Snowflake Feature Store](../developer-guide/snowflake-ml/feature-store/overview.md) to create a repository of data transformations that can be used to train machine learning models. | ✔ | ✔ | ✔ | ✔ |

### Customer support

| Feature/Service | Standard | Enterprise | Business Critical | VPS |
| --- | --- | --- | --- | --- |
| [Snowflake Community](https://community.snowflake.com), Snowflake’s online Knowledge Base and support portal (for logging and tracking Snowflake Support tickets). | ✔ | ✔ | ✔ | ✔ |
| [Premier support](https://www.snowflake.com/wp-content/uploads/2019/02/Snowflake-Support-Policy-02202019.pdf), which includes 24/7 coverage and 1-hour response window for Severity 1 issues. | ✔ [1] | ✔ | ✔ | ✔ |

[1] Applies only to Standard accounts provisioned after May 1, 2020; Standard accounts provisioned before May 1 will continue to receive Standard support (as defined in ‘Support Policy and Service Level Agreement’) until the account is transitioned to Premier support.
