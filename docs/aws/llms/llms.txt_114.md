# Source: https://docs.aws.amazon.com/athena/latest/ug/llms.txt

# Amazon Athena User Guide

> Use Athena to analyze data in Amazon S3 using standard SQL. Athena is serverless, so there is no infrastructure to manage, and you pay only for the queries that you run.

- [Release notes](https://docs.aws.amazon.com/athena/latest/ug/release-notes.html)
- [Document history](https://docs.aws.amazon.com/athena/latest/ug/DocHistory.html)

## [What is Amazon Athena?](https://docs.aws.amazon.com/athena/latest/ug/what-is.html)

- [When should I use Athena?](https://docs.aws.amazon.com/athena/latest/ug/when-should-i-use-ate.html): Compare Athena with other AWS analytics services to find a good fit for your use case.
- [Ways to use Athena](https://docs.aws.amazon.com/athena/latest/ug/accessing-athena.html): Learn about different ways to access Athena functionality.
- [Set up access](https://docs.aws.amazon.com/athena/latest/ug/setting-up.html): Learn how to sign up for an AWS account and create an identity that you can use with Athena.
- [AWS service integrations](https://docs.aws.amazon.com/athena/latest/ug/athena-aws-service-integrations.html): Learn more about the AWS integrations with Athena.


## [Use Athena SQL](https://docs.aws.amazon.com/athena/latest/ug/using-athena-sql.html)

- [Tables, databases, and data catalogs](https://docs.aws.amazon.com/athena/latest/ug/understanding-tables-databases-and-the-data-catalog.html): Understand the meaning and use of tables, databases, and data catalogs in Athena

### [Get started](https://docs.aws.amazon.com/athena/latest/ug/getting-started.html)

Get started using Amazon Athena.

- [Step 1: Create a database](https://docs.aws.amazon.com/athena/latest/ug/step-1-create-a-database.html): You first need to create a database in Athena.
- [Step 2: Create a table](https://docs.aws.amazon.com/athena/latest/ug/step-2-create-a-table.html): Now that you have a database, you can create an Athena table for it.
- [Step 3: Query data](https://docs.aws.amazon.com/athena/latest/ug/step-3-query-data.html): Now that you have the cloudfront_logs table created in Athena based on the data in Amazon S3, you can run SQL queries on the table and see the results in Athena.
- [Step 4: Use named queries](https://docs.aws.amazon.com/athena/latest/ug/step-4-use-named-queries.html): You can save the queries that you create or edit in the query editor with a name.
- [Step 5: Use keyboard shortcuts](https://docs.aws.amazon.com/athena/latest/ug/step-5-using-keyboard-shortcuts.html): The Athena query editor provides numerous keyboard shortcuts for actions like running a query, formatting a query, line operations, and find and replace.
- [Step 6: Connect to other data sources](https://docs.aws.amazon.com/athena/latest/ug/step-6-connect-to-other-data-sources.html): This tutorial used a data source in Amazon S3 in CSV format.

### [Connect to data sources](https://docs.aws.amazon.com/athena/latest/ug/work-with-data-stores.html)

Learn to sync datasets and metastores with Athena so you can run SQL queries on data stored virtually in virtually any format, anywhere it is.

### [Use AWS Glue Data Catalog](https://docs.aws.amazon.com/athena/latest/ug/data-sources-glue.html)

Use AWS Glue Data Catalog to connect to data sources in Amazon S3.

### [Register and use data catalogs](https://docs.aws.amazon.com/athena/latest/ug/gdc-register.html)

Register and query a AWS Glue Data Catalog from Athena.

- [Register Redshift data catalogs](https://docs.aws.amazon.com/athena/latest/ug/gdc-register-rs.html): Athena can read and write data stored in Redshift clusters or serverless namespaces that have been registered in the AWS Glue Data Catalog.
- [Register federated catalogs](https://docs.aws.amazon.com/athena/latest/ug/gdc-register-federated.html): After you create connections to federated data sources, you can register them as federated data catalogs for simplified data discovery and manage data access with fine-grained permissions using Lake Formation.
- [Register S3 table bucket catalogs](https://docs.aws.amazon.com/athena/latest/ug/gdc-register-s3-table-bucket-cat.html): Amazon S3 table buckets are a bucket type in Amazon S3 that is purpose-built to store tabular data in Apache Iceberg tables.
- [Query AWS Glue data catalogs in Athena](https://docs.aws.amazon.com/athena/latest/ug/gdc-register-query-the-data-source.html): To query data catalogs from Athena, do one of the following.
- [Register a catalog from another account](https://docs.aws.amazon.com/athena/latest/ug/data-sources-glue-cross-account.html): Register an AWS Glue Data Catalog from another account for querying in Athena.

### [Control access to data catalogs](https://docs.aws.amazon.com/athena/latest/ug/datacatalogs-iam-policy.html)

To control access to data catalogs, use resource-level IAM permissions or identity-based IAM policies.

- [Data Catalog example policies](https://docs.aws.amazon.com/athena/latest/ug/datacatalogs-example-policies.html): This section includes example policies you can use to enable various actions on data catalogs.
- [Use a form to add a table](https://docs.aws.amazon.com/athena/latest/ug/data-sources-glue-manual-table.html): Use a form in the Athena console to add a AWS Glue table

### [Use a crawler to add a table](https://docs.aws.amazon.com/athena/latest/ug/schema-crawlers.html)

Use AWS Glue crawlers to make your Amazon S3 queryable in Athena

- [Use multiple data sources with a crawler](https://docs.aws.amazon.com/athena/latest/ug/schema-crawlers-data-sources.html): When an AWS Glue crawler scans Amazon S3 and detects multiple directories, it uses a heuristic to determine where the root for a table is in the directory structure, and which directories are partitions for the table.
- [Schedule a crawler](https://docs.aws.amazon.com/athena/latest/ug/schema-crawlers-schedule.html): AWS Glue crawlers can be set up to run on a schedule or on demand.
- [Use partition indexing and filtering](https://docs.aws.amazon.com/athena/latest/ug/glue-best-practices-partition-index.html): Optimize partition processing and improve query performance on highly partitioned tables in Athena.
- [Recreate a database and tables](https://docs.aws.amazon.com/athena/latest/ug/glue-recreate-db-and-tables-cli.html): Use the AWS CLI to copy an AWS Glue database definition and its tables to a new AWS Glue database.
- [Create tables for ETL jobs](https://docs.aws.amazon.com/athena/latest/ug/schema-classifier.html): You can use Athena to create tables that AWS Glue can use for ETL jobs.
- [Work with CSV data](https://docs.aws.amazon.com/athena/latest/ug/schema-csv.html): Use AWS Glue to create schema from CSV files
- [Work with geospatial data](https://docs.aws.amazon.com/athena/latest/ug/schema-geospatial.html): AWS Glue does not natively support Well-known Text (WKT), Well-Known Binary (WKB), or other PostGIS data types.

### [Use federated queries](https://docs.aws.amazon.com/athena/latest/ug/federated-queries.html)

Connect to federated data sources from Athena.

### [Available data source connectors](https://docs.aws.amazon.com/athena/latest/ug/connectors-available.html)

Use Amazon Athena data source connectors to query a variety of data sources outside Amazon S3.

- [Azure Data Lake Storage](https://docs.aws.amazon.com/athena/latest/ug/connectors-adls-gen2.html): Run SQL queries from Athena on Azure Data Lake Storage (ADLS) Gen2 data sources.
- [Azure Synapse](https://docs.aws.amazon.com/athena/latest/ug/connectors-azure-synapse.html): Run SQL queries from Athena on Synapse data sources.
- [Cloudera Hive](https://docs.aws.amazon.com/athena/latest/ug/connectors-cloudera-hive.html): Run SQL queries from Athena on the Cloudera Hive Hadoop distribution.
- [Cloudera Impala](https://docs.aws.amazon.com/athena/latest/ug/connectors-cloudera-impala.html): Run SQL queries from Athena on the Cloudera Impala Hadoop distribution.
- [CloudWatch](https://docs.aws.amazon.com/athena/latest/ug/connectors-cloudwatch.html): Run SQL queries from Athena on CloudWatch data sources.
- [CloudWatch metrics](https://docs.aws.amazon.com/athena/latest/ug/connectors-cwmetrics.html): Run SQL queries from Athena on CloudWatch Metrics data sources.
- [CMDB](https://docs.aws.amazon.com/athena/latest/ug/connectors-cmdb.html): Run SQL queries from Athena on AWS CMDB data sources.
- [Db2](https://docs.aws.amazon.com/athena/latest/ug/connectors-ibm-db2.html): Run SQL queries from Athena on Db2 data sources.
- [Db2 iSeries](https://docs.aws.amazon.com/athena/latest/ug/connectors-ibm-db2-as400.html): Run SQL queries from Athena on Db2 AS/400 (Db2 iSeries) data sources.
- [DocumentDB](https://docs.aws.amazon.com/athena/latest/ug/connectors-docdb.html): Run SQL queries from Athena on DocumentDB data sources.
- [DynamoDB](https://docs.aws.amazon.com/athena/latest/ug/connectors-dynamodb.html): Run SQL queries from Athena on DynamoDB data sources.
- [Google BigQuery](https://docs.aws.amazon.com/athena/latest/ug/connectors-bigquery.html): Run SQL queries from Athena on Google BigQuery data sources.
- [Google Cloud Storage](https://docs.aws.amazon.com/athena/latest/ug/connectors-gcs.html): Use Athena to query your data in Google Cloud Storage buckets.
- [HBase](https://docs.aws.amazon.com/athena/latest/ug/connectors-hbase.html): Run SQL queries from Athena on HBase data sources.
- [Hortonworks](https://docs.aws.amazon.com/athena/latest/ug/connectors-hortonworks.html): Run SQL queries from Athena on Hortonworks Hive data sources.
- [Kafka](https://docs.aws.amazon.com/athena/latest/ug/connectors-kafka.html): Use Athena to query your Apache Kafka topics.
- [MSK](https://docs.aws.amazon.com/athena/latest/ug/connectors-msk.html): The Amazon Athena connector for Amazon MSK enables Amazon Athena to run SQL queries on your Apache Kafka topics.
- [MySQL](https://docs.aws.amazon.com/athena/latest/ug/connectors-mysql.html): Run SQL queries from Athena on MySQL data sources.
- [Neptune](https://docs.aws.amazon.com/athena/latest/ug/connectors-neptune.html): Run SQL queries from Athena on Neptune data sources.
- [OpenSearch](https://docs.aws.amazon.com/athena/latest/ug/connectors-opensearch.html): Run SQL queries from Athena on OpenSearch data sources.
- [Oracle](https://docs.aws.amazon.com/athena/latest/ug/connectors-oracle.html): Run SQL queries from Athena on Oracle data sources.
- [PostgreSQL](https://docs.aws.amazon.com/athena/latest/ug/connectors-postgresql.html): Run SQL queries from Athena on PostgreSQL data sources.
- [Redis OSS](https://docs.aws.amazon.com/athena/latest/ug/connectors-redis.html): Use the Amazon Athena Redis OSS connector to query your Redis OSS data from Athena.
- [Redshift](https://docs.aws.amazon.com/athena/latest/ug/connectors-redshift.html): Run SQL queries from Athena on Redshift data sources.
- [SAP HANA](https://docs.aws.amazon.com/athena/latest/ug/connectors-sap-hana.html): Run SQL queries from Athena on SAP HANA data sources.

### [Snowflake](https://docs.aws.amazon.com/athena/latest/ug/connectors-snowflake.html)

Run SQL queries from Athena on Snowflake data sources.

- [Snowflake authentication](https://docs.aws.amazon.com/athena/latest/ug/connectors-snowflake-authentication.html): Configure authentication methods for the Amazon Athena Snowflake connector.
- [SQL Server](https://docs.aws.amazon.com/athena/latest/ug/connectors-microsoft-sql-server.html): Run SQL queries from Athena on SQL Server data sources.
- [Teradata](https://docs.aws.amazon.com/athena/latest/ug/connectors-teradata.html): Run SQL queries from Athena on Teradata data sources.
- [Timestream](https://docs.aws.amazon.com/athena/latest/ug/connectors-timestream.html): Run SQL queries from Athena on Timestream data sources.
- [TPC-DS](https://docs.aws.amazon.com/athena/latest/ug/connectors-tpcds.html): Run SQL queries from Athena on TPC-DS data sources.
- [Vertica](https://docs.aws.amazon.com/athena/latest/ug/connectors-vertica.html): Run SQL queries from Athena on Vertica data sources.

### [Create a data source connection](https://docs.aws.amazon.com/athena/latest/ug/connect-to-a-data-source.html)

To use an Athena data source connector, you create the AWS Glue connection that stores the connection information about the connector and your data source.

- [Permissions](https://docs.aws.amazon.com/athena/latest/ug/connect-to-a-data-source-permissions.html): To create and use a data source, you need the following sets of permissions.
- [Use the Athena console](https://docs.aws.amazon.com/athena/latest/ug/connect-to-a-data-source-console-steps.html): You can use the Athena console to create and configure a data source connection.
- [Use the SAR](https://docs.aws.amazon.com/athena/latest/ug/connect-data-source-serverless-app-repo.html): To deploy a data source connector, you can use the AWS Serverless Application Repository instead of using a AWS Glue connection.
- [Create a VPC](https://docs.aws.amazon.com/athena/latest/ug/athena-connectors-vpc-creation.html): Create a VPC for use with an Athena data source connector.
- [Pull ECR images](https://docs.aws.amazon.com/athena/latest/ug/pull-ecr-customer-account.html): Athena federation connector Lambda functions use container images that are stored in Athena-managed Amazon ECR repositories.
- [Register your connection as a Glue Data Catalog](https://docs.aws.amazon.com/athena/latest/ug/register-connection-as-gdc.html): After you create your data source, you can use the Athena console to register your connection as a Glue Data Catalog.
- [Enable cross-account federated queries](https://docs.aws.amazon.com/athena/latest/ug/xacct-fed-query-enable.html): Enable cross-account federated queries by sharing your data connector with another user's account, or by adding a shared Lambda ARN from another account to your account.

### [Update a data source connector](https://docs.aws.amazon.com/athena/latest/ug/connectors-updating.html)

Learn how to update your existing Athena data source connectors to use the latest Athena Query Federation version.

- [Glue connections (recommended)](https://docs.aws.amazon.com/athena/latest/ug/connectors-updating-gc.html)
- [Legacy connections](https://docs.aws.amazon.com/athena/latest/ug/connectors-updating-legacy.html)
- [Edit or delete a data source connection](https://docs.aws.amazon.com/athena/latest/ug/connectors-edit-data-source.html): You can use the Athena console to update the description, host, port, database, and other properties for an existing connection.
- [Run federated queries](https://docs.aws.amazon.com/athena/latest/ug/running-federated-queries.html): Use data connectors to write Amazon Athena queries across multiple data sources.
- [Use passthrough queries](https://docs.aws.amazon.com/athena/latest/ug/federated-query-passthrough.html): Query federated data sources using the query language of the data source itself.
- [Understand federated table name qualifiers](https://docs.aws.amazon.com/athena/latest/ug/tables-qualifiers.html): Understand the differences in data object naming conventions between Athena and federated data sources.
- [Develop a data source connector](https://docs.aws.amazon.com/athena/latest/ug/connect-data-source-federation-sdk.html): To write your own data source connectors, you can use the Athena Query Federation SDK.
- [Work with connectors for Spark](https://docs.aws.amazon.com/athena/latest/ug/connectors-spark.html)
- [Use DataZone](https://docs.aws.amazon.com/athena/latest/ug/datazone-using.html): Use Amazon DataZone environments in Athena.

### [Use a Hive metastore](https://docs.aws.amazon.com/athena/latest/ug/connect-to-data-source-hive.html)

Use Amazon Athena to query your data sources in Amazon S3 using an Apache Hive-based metastore in your private VPC.

- [Connect to a Hive metastore](https://docs.aws.amazon.com/athena/latest/ug/connect-to-data-source-hive-connecting-athena-to-an-apache-hive-metastore.html): To connect Athena to an Apache Hive metastore, you must create and configure a Lambda function.
- [Use the SAR](https://docs.aws.amazon.com/athena/latest/ug/connect-data-source-sar-hive.html): To deploy an Athena data source connector for Hive, you can use the AWS Serverless Application Repository instead of starting with the Athena console.
- [Connect Athena to Hive using an existing role](https://docs.aws.amazon.com/athena/latest/ug/connect-data-source-hive-existing-iam-role.html): Connect Athena to an Apache Hive metastore with a Lambda function that uses an existing IAM execution role.
- [Use a deployed Hive metastore connector](https://docs.aws.amazon.com/athena/latest/ug/connect-data-source-hive-existing-lambda.html): After you have deployed a Lambda data source connector like AthenaHiveMetastoreFunction to your account, you can configure Athena to use it.
- [Omit the catalog name](https://docs.aws.amazon.com/athena/latest/ug/datastores-hive-default-catalog.html): Simplify your query syntax by using a default catalog in Athena.
- [Work with Hive views](https://docs.aws.amazon.com/athena/latest/ug/hive-views.html): Query views in an external Hive metastore from Athena.
- [Use the AWS CLI with Hive metastores](https://docs.aws.amazon.com/athena/latest/ug/datastores-hive-cli.html): Use the AWS CLI with Athena to manage external Hive metastore catalogs and run.
- [Modify the Hive connector](https://docs.aws.amazon.com/athena/latest/ug/datastores-hive-reference-implementation.html): Learn about the Athena connector for external Hive metastore reference implementation.
- [Manage your data sources](https://docs.aws.amazon.com/athena/latest/ug/data-sources-managing.html): Use the Data sources and catalogs page of the Amazon Athena console to view, edit, or delete data sources.

### [Connect to Amazon Athena with ODBC and JDBC drivers](https://docs.aws.amazon.com/athena/latest/ug/athena-bi-tools-jdbc-odbc.html)

Use ODBC or JDBC drivers to connect to Athena from third-party SQL clients, business intelligence tools, and custom applications.

### [Connect to Athena with JDBC](https://docs.aws.amazon.com/athena/latest/ug/connect-with-jdbc.html)

Download the Athena JDBC driver and documentation and connect Athena to JDBC data sources.

### [JDBC 3.x](https://docs.aws.amazon.com/athena/latest/ug/jdbc-v3-driver.html)

Learn how to configure and use the Athena JDBC version 3 driver.

- [Get started](https://docs.aws.amazon.com/athena/latest/ug/jdbc-v3-driver-getting-started.html): Get started using the Athena JDBC 3.x driver.

### [JDBC 3.x connection parameters](https://docs.aws.amazon.com/athena/latest/ug/jdbc-v3-driver-connection-parameters.html)

Supported connection parameters are divided here into three sections: , , and .

- [Basic](https://docs.aws.amazon.com/athena/latest/ug/jdbc-v3-driver-basic-connection-parameters.html): The following sections describe the basic connection parameters for the JDBC 3.x driver.
- [Advanced](https://docs.aws.amazon.com/athena/latest/ug/jdbc-v3-driver-advanced-connection-parameters.html): The following sections describe the advanced connection parameters for the JDBC 3.x driver.

### [Authentication](https://docs.aws.amazon.com/athena/latest/ug/jdbc-v3-driver-authentication-connection-parameters.html)

The Athena JDBC 3.x driver supports several authentication methods.

- [IAM](https://docs.aws.amazon.com/athena/latest/ug/jdbc-v3-driver-iam-credentials.html): You can use your IAM credentials with the JDBC driver to connect to Amazon Athena by setting the following connection parameters.
- [Default](https://docs.aws.amazon.com/athena/latest/ug/jdbc-v3-driver-default-credentials.html): You can use the default credentials that you configure on your client system to connect to Amazon Athena by setting the following connection parameters.
- [AWS configuration profile](https://docs.aws.amazon.com/athena/latest/ug/jdbc-v3-driver-aws-configuration-profile-credentials.html): You can use credentials stored in an AWS configuration profile by setting the following connection parameters.
- [Instance profile](https://docs.aws.amazon.com/athena/latest/ug/jdbc-v3-driver-instance-profile-credentials.html): This authentication type is used on Amazon EC2 instances.
- [Custom](https://docs.aws.amazon.com/athena/latest/ug/jdbc-v3-driver-custom-credentials.html): You can use this authentication type to provide your own credentials by using a Java class that implements the AwsCredentialsProvider interface.
- [JWT](https://docs.aws.amazon.com/athena/latest/ug/jdbc-v3-driver-jwt-credentials.html): With this authentication type, you can use a JSON web token (JWT) obtained from an external identity provider as a connection parameter to authenticate with Athena.
- [JWT trusted identity propagation](https://docs.aws.amazon.com/athena/latest/ug/jdbc-v3-driver-jwt-tip-credentials.html): This authentication type allows you to use a JSON web token (JWT) obtained from an external identity provider as a connection parameter to authenticate with Athena.
- [Browser trusted identity propagation](https://docs.aws.amazon.com/athena/latest/ug/jdbc-v3-driver-browser-oidc-tip-credentials.html): This authentication type allows you to fetch a new JSON web token (JWT) from an external identity provider and authenticate with Athena.
- [Azure AD](https://docs.aws.amazon.com/athena/latest/ug/jdbc-v3-driver-azure-ad-credentials.html): Use Azure AD credentials with the Athena JDBC 3.x driver.
- [Okta](https://docs.aws.amazon.com/athena/latest/ug/jdbc-v3-driver-okta-credentials.html): A SAML-based authentication mechanism that enables authentication to Athena using the Okta identity provider.
- [Ping](https://docs.aws.amazon.com/athena/latest/ug/jdbc-v3-driver-ping-credentials.html): A SAML-based authentication mechanism that enables authentication to Athena using the Ping Federate identity provider.
- [AD FS](https://docs.aws.amazon.com/athena/latest/ug/jdbc-v3-driver-adfs-credentials.html): Authenticate to Microsoft AD FS using the Athena JDBC version 3 driver.
- [Browser Azure AD](https://docs.aws.amazon.com/athena/latest/ug/jdbc-v3-driver-browser-azure-ad-credentials.html): Browser Azure AD is a SAML-based authentication mechanism that works with the Azure AD identity provider and supports multi-factor authentication.
- [Browser SAML](https://docs.aws.amazon.com/athena/latest/ug/jdbc-v3-driver-browser-saml-credentials.html): Browser SAML is a generic authentication plugin that can work with SAML-based identity providers and supports multi-factor authentication.
- [DataZone IdC](https://docs.aws.amazon.com/athena/latest/ug/jdbc-v3-driver-datazone-idc.html): Connect to DataZone-governed data in Athena using IAM Identity Center.
- [DataZone IAM](https://docs.aws.amazon.com/athena/latest/ug/jdbc-v3-driver-datazone-iamcp.html): Use IAM credentials to connect to DataZone-governed data in Athena.
- [Other JDBC 3.x configuration](https://docs.aws.amazon.com/athena/latest/ug/jdbc-v3-driver-other-configuration.html): The following sections describe some additional configuration settings for the JDBC 3.x driver.
- [JDBC 3.x release notes](https://docs.aws.amazon.com/athena/latest/ug/jdbc-v3-driver-release-notes.html): Athena JDBCv3 release notes
- [Previous versions](https://docs.aws.amazon.com/athena/latest/ug/jdbc-v3-driver-previous-versions.html): Download previous versions of the Athena JDBC 3.x driver
- [JDBC 2.x](https://docs.aws.amazon.com/athena/latest/ug/jdbc-v2.html): Use a JDBC connection to connect Athena to business intelligence tools and other applications.

### [Connect to Athena with ODBC](https://docs.aws.amazon.com/athena/latest/ug/connect-with-odbc.html)

Download the Athena ODBC driver and documentation and connect Athena to ODBC data sources.

### [ODBC 2.x](https://docs.aws.amazon.com/athena/latest/ug/odbc-v2-driver.html)

Use the Athena driver to use ODBC to connect Windows clients to Athena.

### [Get started with ODBC 2.x](https://docs.aws.amazon.com/athena/latest/ug/odbc-v2-driver-getting-started.html)

Get set up to use the Amazon Athena ODBC driver.

- [Windows](https://docs.aws.amazon.com/athena/latest/ug/odbc-v2-driver-getting-started-windows.html): Install the Athena ODBC driver on a Windows client computer.
- [Linux](https://docs.aws.amazon.com/athena/latest/ug/odbc-v2-driver-getting-started-linux.html): Install the Athena ODBC driver on a Linux client computer.
- [macOS](https://docs.aws.amazon.com/athena/latest/ug/odbc-v2-driver-getting-started-macos.html): Install the Athena ODBC driver on a macOS client computer.

### [ODBC 2.x connection parameters](https://docs.aws.amazon.com/athena/latest/ug/odbc-v2-driver-connection-parameters.html)

See connection parameter information for the Amazon Athena ODBC driver.

- [Main parameters](https://docs.aws.amazon.com/athena/latest/ug/odbc-v2-driver-main-connection-parameters.html): See information for the main connection parameters in the Amazon Athena ODBC driver.

### [Authentication](https://docs.aws.amazon.com/athena/latest/ug/odbc-v2-driver-authentication-options.html)

Learn about authentication parameters for the Amazon Athena ODBC driver.

- [IAM credentials](https://docs.aws.amazon.com/athena/latest/ug/odbc-v2-driver-iam-credentials.html): See authentication parameters for IAM credentials.
- [IAM profile](https://docs.aws.amazon.com/athena/latest/ug/odbc-v2-driver-iam-profile.html): See authentication parameters for IAM profile.
- [AD FS](https://docs.aws.amazon.com/athena/latest/ug/odbc-v2-driver-ad-fs.html): See authentication parameters for AD FS.
- [Azure AD](https://docs.aws.amazon.com/athena/latest/ug/odbc-v2-driver-azure-ad.html): See authentication parameters for Azure AD.
- [Browser Azure AD](https://docs.aws.amazon.com/athena/latest/ug/odbc-v2-driver-browser-azure-ad.html): See authentication parameters for Browser Azure AD.
- [Browser SAML](https://docs.aws.amazon.com/athena/latest/ug/odbc-v2-driver-browser-saml.html): See authentication parameters for Browser SAML.
- [Browser SSO OIDC](https://docs.aws.amazon.com/athena/latest/ug/odbc-v2-driver-browser-sso-oidc.html): See authentication parameters for Browser SSO OIDC.
- [Default credentials](https://docs.aws.amazon.com/athena/latest/ug/odbc-v2-driver-default-credentials.html): See authentication parameters for default credentials.
- [External credentials](https://docs.aws.amazon.com/athena/latest/ug/odbc-v2-driver-external-credentials.html): Authentication parameters for external credentials, a plugin that you can use to connect to any external SAML based identity provider.
- [Instance profile](https://docs.aws.amazon.com/athena/latest/ug/odbc-v2-driver-instance-profile.html): See authentication parameters for instance profile.
- [JWT](https://docs.aws.amazon.com/athena/latest/ug/odbc-v2-driver-jwt.html): See authentication parameters for JSON Web Token (JWT).
- [JWT trusted identity propagation](https://docs.aws.amazon.com/athena/latest/ug/odbc-v2-driver-jwt-tip.html): See authentication parameters for JSON Web Token (JWT) trusted identity propagation.
- [Browser trusted identity propagation](https://docs.aws.amazon.com/athena/latest/ug/odbc-v2-driver-browser-oidc-tip.html): See authentication parameters for browser-based trusted identity propagation.
- [Okta](https://docs.aws.amazon.com/athena/latest/ug/odbc-v2-driver-okta.html): See authentication parameters for Okta.
- [Ping](https://docs.aws.amazon.com/athena/latest/ug/odbc-v2-driver-ping.html): See authentication parameters for Ping.
- [Common auth parameters](https://docs.aws.amazon.com/athena/latest/ug/odbc-v2-driver-common-authentication-parameters.html): See common authentication parameters for the Amazon Athena ODBC driver.
- [Endpoints](https://docs.aws.amazon.com/athena/latest/ug/odbc-v2-driver-endpoint-overrides.html): See endpoint override parameter information for the Amazon Athena ODBC driver.
- [Advanced](https://docs.aws.amazon.com/athena/latest/ug/odbc-v2-driver-advanced-options.html): See advanced options for the Amazon Athena ODBC driver.
- [Proxy](https://docs.aws.amazon.com/athena/latest/ug/odbc-v2-driver-proxy-options.html): See proxy parameter information for the Amazon Athena ODBC driver.
- [Logging](https://docs.aws.amazon.com/athena/latest/ug/odbc-v2-driver-logging-options.html): Learn about logging parameters for the Amazon Athena ODBC driver.
- [Migrate to ODBC 2.x](https://docs.aws.amazon.com/athena/latest/ug/odbc-v2-driver-migrating.html): See migration information for the Amazon Athena ODBC 2.x driver.
- [Troubleshoot ODBC 2.x](https://docs.aws.amazon.com/athena/latest/ug/odbc-v2-driver-troubleshooting.html): Learn how to get support for the Amazon Athena ODBC 2.x driver.
- [ODBC 2.x release notes](https://docs.aws.amazon.com/athena/latest/ug/odbc-v2-driver-release-notes.html): Athena ODBCv2 release notes

### [ODBC 1.x](https://docs.aws.amazon.com/athena/latest/ug/connect-with-odbc-driver-and-documentation-download-links.html)

Download the Athena 1.x ODBC driver and documentation and connect Athena to ODBC data sources.

- [AD FS access using ODBC](https://docs.aws.amazon.com/athena/latest/ug/odbc-adfs-saml.html): Set up federated access to Athena for Microsoft AD FS users using an ODBC client
- [SSO for ODBC and Okta](https://docs.aws.amazon.com/athena/latest/ug/odbc-okta-plugin.html): Configure the Athena ODBC driver and Okta plugin for single sign-on (SSO) capability.
- [SSO using ODBC, SAML 2.0, and Okta](https://docs.aws.amazon.com/athena/latest/ug/okta-saml-sso.html): Configure single sign-on for Athena using SAML 2.0 and the Okta identity provider
- [Use the Power BI connector](https://docs.aws.amazon.com/athena/latest/ug/connect-with-odbc-and-power-bi.html): Analyze your Athena data in the Microsoft Power BI Desktop.

### [Use trusted identity propagation with drivers](https://docs.aws.amazon.com/athena/latest/ug/using-trusted-identity-propagation.html)

Learn how to use trusted identity propagation with Athena JDBC and ODBC drivers through IAM Identity Center.

- [Connect Athena to IAM Identity Center](https://docs.aws.amazon.com/athena/latest/ug/using-trusted-identity-propagation-setup.html): The following section lists the process of connecting Athena to IAM Identity Center.
- [Configure and deploy resources using AWS CloudFormation](https://docs.aws.amazon.com/athena/latest/ug/using-trusted-identity-propagation-cloudformation.html): You can configure and deploy resources using CloudFormation templates to start using Trusted Identity Propagation with Athena drivers as following.

### [Create databases and tables](https://docs.aws.amazon.com/athena/latest/ug/work-with-data.html)

Learn how to create databases and tables in Amazon Athena.

### [Create databases](https://docs.aws.amazon.com/athena/latest/ug/creating-databases.html)

Create databases in Athena by using HIVE DDL.

- [Create a query output location](https://docs.aws.amazon.com/athena/latest/ug/creating-databases-prerequisites.html): If you do not already have a query output location set up in Amazon S3, perform the following prerequisite steps to do so.
- [Create a database](https://docs.aws.amazon.com/athena/latest/ug/creating-databases-query-editor.html): After you have set up a query results location, creating a database in the Athena console query editor is straightforward.

### [Create tables](https://docs.aws.amazon.com/athena/latest/ug/creating-tables.html)

Learn how to create tables in Athena.

- [Use AWS Glue or the Athena console](https://docs.aws.amazon.com/athena/latest/ug/creating-tables-how-to.html): You can create tables in Athena by using AWS Glue, the add table form, or by running a DDL statement in the Athena query editor.
- [Specify a table location](https://docs.aws.amazon.com/athena/latest/ug/tables-location-format.html): Learn the details of specifying the location of your data when you create a table in Athena.
- [Show table information](https://docs.aws.amazon.com/athena/latest/ug/creating-tables-showing-table-information.html): After you have created a table in Athena, its name displays in the Tables list on the left in the Athena console.
- [Name databases, tables, and columns](https://docs.aws.amazon.com/athena/latest/ug/tables-databases-columns-names.html): Learn the rules for database, table, and column naming in Athena.
- [Escape reserved keywords](https://docs.aws.amazon.com/athena/latest/ug/reserved-words.html): When you run queries in Athena that include reserved keywords, you must escape them by enclosing them in special characters.

### [Create a table from query results (CTAS)](https://docs.aws.amazon.com/athena/latest/ug/ctas.html)

A CREATE TABLE AS SELECT (CTAS) query in Athena allows you to create a new table from the results of a query in one step, without repeatedly querying raw data sets.

- [Considerations and limitations for CTAS queries](https://docs.aws.amazon.com/athena/latest/ug/ctas-considerations-limitations.html): The following sections describe considerations and limitations to keep in mind when you use CREATE TABLE AS SELECT (CTAS) queries in Athena.
- [Create CTAS queries](https://docs.aws.amazon.com/athena/latest/ug/ctas-console.html): In the Athena console, you can create a CTAS query from another query.
- [CTAS examples](https://docs.aws.amazon.com/athena/latest/ug/ctas-examples.html): See examples of CTAS queries in Athena.
- [Use CTAS and INSERT INTO for ETL](https://docs.aws.amazon.com/athena/latest/ug/ctas-insert-into-etl.html): Use Create Table as Select (CTAS) and INSERT INTO statements in Athena to extract, transform, and load (ETL) data into Amazon S3 for data processing.
- [Work around the 100 partition limit](https://docs.aws.amazon.com/athena/latest/ug/ctas-insert-into.html): Use CTAS and INSERT INTO statements in series to overcome the per-query limit of 100 partitions.

### [Use SerDes](https://docs.aws.amazon.com/athena/latest/ug/serde-reference.html)

Learn about serializer/serializers in Athena.

- [Choose a SerDe for your data](https://docs.aws.amazon.com/athena/latest/ug/supported-serdes.html): See the SerDe libraries that you can use in Athena to create tables for particular data formats.
- [Use a SerDe to create a table](https://docs.aws.amazon.com/athena/latest/ug/serde-create-a-table.html): To use a SerDe when creating a table in Athena, use one of the following methods:

### [Amazon Ion Hive SerDe](https://docs.aws.amazon.com/athena/latest/ug/ion-serde.html)

Use the Amazon Ion Hive SerDe to read and write data in the Amazon Ion and standard JSON formats.

- [Create Amazon Ion tables](https://docs.aws.amazon.com/athena/latest/ug/ion-serde-using-create-table.html): Learn how to create Amazon Ion tables in Athena.
- [Use CTAS to create Amazon Ion tables](https://docs.aws.amazon.com/athena/latest/ug/ion-serde-using-ctas-and-insert-into-to-create-ion-tables.html): Use CTAS and INSERT INTO statements to create tables in Athena from Amazon Ion data.
- [Amazon Ion SerDe property reference](https://docs.aws.amazon.com/athena/latest/ug/ion-serde-using-ion-serde-properties.html): This topic contains information about the SerDe properties for CREATE TABLE statements in Athena.

### [Use path extractors](https://docs.aws.amazon.com/athena/latest/ug/ion-serde-using-path-extractors.html)

Use Amazon Ion SerDe path extractor properties to map Amazon Ion data to Hive columns.

- [Use Athena generated path extractors](https://docs.aws.amazon.com/athena/latest/ug/ion-serde-generated-path-extractors.html): By default, Athena searches for top level Amazon Ion values that match Hive column names and creates path extractors at runtime based on these matching values.
- [Specify your own path extractors](https://docs.aws.amazon.com/athena/latest/ug/ion-serde-specifying-your-own-path-extractors.html): If your Amazon Ion fields do not map neatly to Hive columns, you can specify your own path extractors.
- [Use search paths in path extractors](https://docs.aws.amazon.com/athena/latest/ug/ion-serde-using-search-paths-in-path-extractors.html): The SerDe property syntax for path extractor contains a <path_extractor_expression>:
- [Path extractor examples](https://docs.aws.amazon.com/athena/latest/ug/ion-serde-examples.html): The following path extractor examples show how to flatten and rename fields or extract data as Amazon Ion text.
- [Avro SerDe](https://docs.aws.amazon.com/athena/latest/ug/avro-serde.html): Use the Avro SerDe to create Athena tables from Avro data.
- [Grok SerDe](https://docs.aws.amazon.com/athena/latest/ug/grok-serde.html): The Logstash Grok SerDe is a library with a set of specialized patterns for deserialization of unstructured text data, usually logs.

### [JSON SerDe libraries](https://docs.aws.amazon.com/athena/latest/ug/json-serde.html)

Learn about the libraries for JSON data that you can use to create tables for Athena.

- [Hive JSON SerDe](https://docs.aws.amazon.com/athena/latest/ug/hive-json-serde.html): The Hive JSON SerDe is commonly used to process JSON data like events.
- [OpenX JSON SerDe](https://docs.aws.amazon.com/athena/latest/ug/openx-json-serde.html): Like the Hive JSON SerDe, you can use the OpenX JSON to process JSON data.

### [CSV SerDe libraries](https://docs.aws.amazon.com/athena/latest/ug/serde-csv-choices.html)

Choose a SerDe library to use for CSV data in Athena.

- [Lazy Simple SerDe for CSV](https://docs.aws.amazon.com/athena/latest/ug/lazy-simple-serde.html): Because this is the default SerDe in Athena for data in CSV, TSV, and custom-delimited formats, specifying it is optional.
- [OpenCSVSerDe](https://docs.aws.amazon.com/athena/latest/ug/csv-serde.html): Use the Open CSV SerDe library to create tables in Athena for comma-separated data.
- [ORC SerDe](https://docs.aws.amazon.com/athena/latest/ug/orc-serde.html): Use the ORC SerDe to create Athena tables from ORC data.
- [Parquet SerDe](https://docs.aws.amazon.com/athena/latest/ug/parquet-serde.html): Use the Parquet SerDe to create Athena tables from Parquet data.
- [Regex SerDe](https://docs.aws.amazon.com/athena/latest/ug/regex-serde.html): The Regex SerDe uses a regular expression (regex) to deserialize data by extracting regex groups into table columns.

### [Run queries](https://docs.aws.amazon.com/athena/latest/ug/querying-athena-tables.html)

You can run SQL queries using Amazon Athena on data sources that are registered with the AWS Glue Data Catalog and data sources such as Hive metastores and Amazon DocumentDB instances that you connect to using the Athena Federated Query feature.

- [View query plans](https://docs.aws.amazon.com/athena/latest/ug/query-plans.html): View graphical representations of execution plans for your SQL queries in the Athena console.

### [Work with query results and recent queries](https://docs.aws.amazon.com/athena/latest/ug/querying.html)

Learn about working with query results, query output files, and recent queries in Athena

### [Managed query results](https://docs.aws.amazon.com/athena/latest/ug/managed-results.html)

Documentation for Managed query results.

- [Encrypt managed query results](https://docs.aws.amazon.com/athena/latest/ug/encrypting-managed-results.html): Learn how to encrypt Amazon Athena managed query results.

### [Specify a query result location](https://docs.aws.amazon.com/athena/latest/ug/query-results-specify-location.html)

The query result location that Athena uses is determined by a combination of workgroup settings and client-side settings.

- [Use the Athena console](https://docs.aws.amazon.com/athena/latest/ug/query-results-specify-location-console.html): Before you can run a query, a query result bucket location in Amazon S3 must be specified, or you must use a workgroup that has specified a bucket and whose configuration overrides client settings.
- [Use a workgroup](https://docs.aws.amazon.com/athena/latest/ug/query-results-specify-location-workgroup.html): You specify the query result location in a workgroup configuration using the AWS Management Console, the AWS CLI, or the Athena API.
- [Download query results](https://docs.aws.amazon.com/athena/latest/ug/saving-query-results.html): You can download the query results CSV file from the query pane immediately after you run a query.
- [View recent queries](https://docs.aws.amazon.com/athena/latest/ug/queries-viewing-history.html): You can use the Athena console to see which queries succeeded or failed, and view error details for the queries that failed.
- [Download recent queries](https://docs.aws.amazon.com/athena/latest/ug/queries-downloading-multiple-recent-queries-to-csv.html): You can use the Recent queries tab of the Athena console to export one or more recent queries to a CSV file in order to view them in tabular format.
- [Configure recent query options](https://docs.aws.amazon.com/athena/latest/ug/queries-recent-queries-configuring-options.html): You can configure options for the Recent queries tab like columns to display and text wrapping.
- [Keep your query history longer](https://docs.aws.amazon.com/athena/latest/ug/querying-keeping-query-history.html): If you want to keep the query history longer than 45 days, you can retrieve the query history and save it to a data store such as Amazon S3.
- [Find query output files in Amazon S3](https://docs.aws.amazon.com/athena/latest/ug/querying-finding-output-files.html): Query output files are stored in sub-folders on Amazon S3 in the following path pattern unless the query occurs in a workgroup whose configuration overrides client-side settings.
- [Reuse query results in Athena](https://docs.aws.amazon.com/athena/latest/ug/reusing-query-results.html): Reuse query results in Athena for better performance and reduced cost.
- [View query stats](https://docs.aws.amazon.com/athena/latest/ug/query-stats.html): See query statistics and runtime details for completed queries in the Athena console.

### [Work with views](https://docs.aws.amazon.com/athena/latest/ug/views.html)

Learn how to work with Athena and AWS Glue Data Catalog views in Athena.

### [Athena views](https://docs.aws.amazon.com/athena/latest/ug/views-console.html)

Learn how to work with views in Athena.

- [Examples](https://docs.aws.amazon.com/athena/latest/ug/views-examples.html): To show the syntax of the view query, use .
- [Manage Athena views](https://docs.aws.amazon.com/athena/latest/ug/views-managing.html): In the Athena console, you can:
- [Considerations and limitations](https://docs.aws.amazon.com/athena/latest/ug/considerations-limitations-views.html): Learn about the considerations and limitations for Athena views.

### [Glue Data Catalog views](https://docs.aws.amazon.com/athena/latest/ug/views-glue.html)

Use a single view object for multiple AWS services.

- [Manage Data Catalog views](https://docs.aws.amazon.com/athena/latest/ug/views-glue-managing.html): Manage Data Catalog views in Athena

### [Use saved queries](https://docs.aws.amazon.com/athena/latest/ug/saved-queries.html)

Use the Athena console to save, edit, run, rename, and delete the queries that you create in the Athena query editor.

- [Save a query with a name](https://docs.aws.amazon.com/athena/latest/ug/saved-queries-name.html)
- [Run a saved query](https://docs.aws.amazon.com/athena/latest/ug/saved-queries-run.html)
- [Edit a saved query](https://docs.aws.amazon.com/athena/latest/ug/saved-queries-edit.html)
- [Rename or delete a saved query](https://docs.aws.amazon.com/athena/latest/ug/saved-queries-rename-or-delete.html)
- [Rename an undisplayed saved query](https://docs.aws.amazon.com/athena/latest/ug/saved-queries-rename-not-displayed.html)
- [Delete an undisplayed saved query](https://docs.aws.amazon.com/athena/latest/ug/saved-queries-delete-not-displayed.html)
- [Use the Athena API to update saved queries](https://docs.aws.amazon.com/athena/latest/ug/saved-queries-update-with-api.html): For information about using the Athena API to update a saved query, see the UpdateNamedQuery action in the Athena API Reference.

### [Use parameterized queries](https://docs.aws.amazon.com/athena/latest/ug/querying-with-prepared-statements.html)

Use parameterized queries in Athena to re-run the same query with different values and avoid SQL injection attacks.

### [Use execution parameters](https://docs.aws.amazon.com/athena/latest/ug/querying-with-prepared-statements-querying-using-execution-parameters.html)

You can use question mark placeholders in any DML query to create a parameterized query without creating a prepared statement first.

- [Use the Athena console](https://docs.aws.amazon.com/athena/latest/ug/querying-with-prepared-statements-running-queries-with-execution-parameters-in-the-athena-console.html): When you run a parameterized query that has execution parameters (question marks) in the Athena console, you are prompted for the values in the order in which the question marks occur in the query.
- [Use the AWS CLI](https://docs.aws.amazon.com/athena/latest/ug/querying-with-prepared-statements-running-queries-with-execution-parameters-using-the-aws-cli.html): To use the AWS CLI to run queries with execution parameters, use the start-query-execution command and provide a parameterized query in the query-string argument.

### [Use prepared statements](https://docs.aws.amazon.com/athena/latest/ug/querying-with-prepared-statements-querying.html)

You can use a prepared statement for repeated execution of the same query with different query parameters.

### [SQL syntax](https://docs.aws.amazon.com/athena/latest/ug/querying-with-prepared-statements-sql-statements.html)

You can use the PREPARE, EXECUTE and DEALLOCATE PREPARE SQL statements to run parameterized queries in the Athena console query editor.

- [PREPARE](https://docs.aws.amazon.com/athena/latest/ug/querying-with-prepared-statements-prepare.html): Prepares a statement to be run at a later time.
- [EXECUTE](https://docs.aws.amazon.com/athena/latest/ug/querying-with-prepared-statements-execute.html): Runs a prepared statement.
- [DEALLOCATE PREPARE](https://docs.aws.amazon.com/athena/latest/ug/querying-with-prepared-statements-deallocate-prepare.html): Removes the prepared statement with the specified name from the list of prepared statements in the current workgroup.
- [Use the Athena console](https://docs.aws.amazon.com/athena/latest/ug/querying-with-prepared-statements-executing-prepared-statements-without-the-using-clause-athena-console.html): If you run an existing prepared statement with the syntax EXECUTE prepared_statement in the query editor, Athena opens the Enter parameters dialog box so that you can enter the values that would normally go in the USING clause of the EXECUTE ...

### [Use the AWS CLI](https://docs.aws.amazon.com/athena/latest/ug/querying-with-prepared-statements-cli-section.html)

You can use the AWS CLI to create, execute, and list prepared statements.

- [Create](https://docs.aws.amazon.com/athena/latest/ug/querying-with-prepared-statements-creating-prepared-statements-using-the-aws-cli.html): To use the AWS CLI to create a prepared statement, you can use one of the following athena commands:
- [Execute](https://docs.aws.amazon.com/athena/latest/ug/querying-with-prepared-statements-cli-executing-prepared-statements.html): To execute a prepared statement with the AWS CLI, you can supply values for the parameters by using one of the following methods:
- [List](https://docs.aws.amazon.com/athena/latest/ug/querying-with-prepared-statements-listing.html): To list the prepared statements for a specific workgroup, you can use the Athena list-prepared-statements AWS CLI command or the ListPreparedStatements Athena API action.
- [Additional resources](https://docs.aws.amazon.com/athena/latest/ug/querying-with-prepared-statements-additional-resources.html): See the following related posts in the AWS Big Data Blog.
- [Use the cost-based optimizer](https://docs.aws.amazon.com/athena/latest/ug/cost-based-optimizer.html): Learn how to generate statistics for AWS Glue tables to optimize your queries in Athena.
- [Query S3 Express One Zone](https://docs.aws.amazon.com/athena/latest/ug/querying-express-one-zone.html): Query S3 Express One Zone data with Athena.
- [Query Amazon Glacier](https://docs.aws.amazon.com/athena/latest/ug/querying-glacier.html): Use Athena to query restored Amazon Glacier objects

### [Handle schema updates](https://docs.aws.amazon.com/athena/latest/ug/handling-schema-updates-chapter.html)

Learn how to handle table schema changes in Athena.

### [Make schema updates](https://docs.aws.amazon.com/athena/latest/ug/make-schema-updates.html)

Learn about schema updates in Athena.

- [Add columns at the beginning or in the middle of the table](https://docs.aws.amazon.com/athena/latest/ug/updates-add-columns-beginning-middle-of-table.html): Adding columns is one of the most frequent schema changes.
- [Add columns at the end of the table](https://docs.aws.amazon.com/athena/latest/ug/updates-add-columns-end-of-table.html): If you create tables in any of the formats that Athena supports, such as Parquet, ORC, Avro, JSON, CSV, and TSV, you can use the ALTER TABLE ADD COLUMNS statement to add columns after existing columns but before partition columns.
- [Remove columns](https://docs.aws.amazon.com/athena/latest/ug/updates-removing-columns.html): You may need to remove columns from tables if they no longer contain data, or to restrict access to the data in them.
- [Rename columns](https://docs.aws.amazon.com/athena/latest/ug/updates-renaming-columns.html): You may want to rename columns in your tables to correct spelling, make column names more descriptive, or to reuse an existing column to avoid column reordering.
- [Reorder columns](https://docs.aws.amazon.com/athena/latest/ug/updates-reordering-columns.html): You can reorder columns only for tables with data in formats that read by name, such as JSON or Parquet, which reads by name by default.
- [Change a column data type](https://docs.aws.amazon.com/athena/latest/ug/updates-changing-column-type.html): You might want to use a different column type when the existing type can no longer hold the amount of information required.
- [Update tables with partitions](https://docs.aws.amazon.com/athena/latest/ug/updates-and-partitions.html): In Athena, a table and its partitions must use the same data formats but their schemas may differ.

### [Query arrays](https://docs.aws.amazon.com/athena/latest/ug/querying-arrays.html)

Amazon Athena lets you create arrays, concatenate them, convert them to different data types, and then filter, flatten, and sort them.

- [Create arrays](https://docs.aws.amazon.com/athena/latest/ug/creating-arrays.html): To build an array literal in Athena, use the ARRAY keyword, followed by brackets [ ], and include the array elements separated by commas.
- [Concatenate strings and arrays](https://docs.aws.amazon.com/athena/latest/ug/concatenating-strings-and-arrays.html): Learn how to concatenate strings and arrays in Athena queries.
- [Convert array data types](https://docs.aws.amazon.com/athena/latest/ug/converting-array-data-types.html): To convert data in arrays to supported data types, use the CAST operator, as CAST(value AS type).
- [Find array lengths](https://docs.aws.amazon.com/athena/latest/ug/finding-lengths.html): The cardinality function returns the length of an array, as in this example:
- [Access array elements](https://docs.aws.amazon.com/athena/latest/ug/accessing-array-elements.html): To access array elements, use the [] operator, with 1 specifying the first element, 2 specifying the second element, and so on, as in this example:
- [Flatten nested arrays](https://docs.aws.amazon.com/athena/latest/ug/flattening-arrays.html): When working with nested arrays, you often need to expand nested array elements into a single array, or expand the array into multiple rows.
- [Create arrays from subqueries](https://docs.aws.amazon.com/athena/latest/ug/creating-arrays-from-subqueries.html): Create an array from a collection of rows.
- [Filter arrays](https://docs.aws.amazon.com/athena/latest/ug/filtering-arrays.html): Create an array from a collection of rows if they match the filter criteria.
- [Sort arrays](https://docs.aws.amazon.com/athena/latest/ug/sorting-arrays.html): To create a sorted array of unique values from a set of rows, you can use the array_sort function, as in the following example.
- [Use aggregation functions with arrays](https://docs.aws.amazon.com/athena/latest/ug/arrays-and-aggregation.html): Learn about using aggregation functions with arrays in Athena.
- [Convert arrays to strings](https://docs.aws.amazon.com/athena/latest/ug/converting-arrays-to-strings.html): To convert an array into a single string, use the array_join function.
- [Use arrays to create maps](https://docs.aws.amazon.com/athena/latest/ug/arrays-create-maps.html): Maps are key-value pairs that consist of data types available in Athena.

### [Query arrays with complex types](https://docs.aws.amazon.com/athena/latest/ug/rows-and-structs.html)

Your source data often contains arrays with complex data types and nested structures.

- [Create a ROW](https://docs.aws.amazon.com/athena/latest/ug/creating-row.html)
- [Change field names in arrays using CAST](https://docs.aws.amazon.com/athena/latest/ug/changing-row-arrays-with-cast.html): To change the field name in an array that contains ROW values, you can CAST the ROW declaration:
- [Filter arrays using the . notation](https://docs.aws.amazon.com/athena/latest/ug/filtering-with-dot.html): In the following example, select the accountId field from the userIdentity column of a AWS CloudTrail logs table by using the dot . notation.
- [Filter arrays with nested values](https://docs.aws.amazon.com/athena/latest/ug/filtering-nested-with-dot.html): Large arrays often contain nested structures, and you need to be able to filter, or search, for values within them.
- [Filter arrays using UNNEST](https://docs.aws.amazon.com/athena/latest/ug/filtering-with-unnest.html): To filter an array that includes a nested structure by one of its child elements, issue a query with an UNNEST operator.
- [Find keywords in arrays using regexp_like](https://docs.aws.amazon.com/athena/latest/ug/filtering-with-regexp.html): The following examples illustrate how to search a dataset for a keyword within an element inside an array, using the regexp_like function.

### [Query geospatial data](https://docs.aws.amazon.com/athena/latest/ug/querying-geospatial-data.html)

Query geospatial data in Athena.

- [Examples: Geospatial queries](https://docs.aws.amazon.com/athena/latest/ug/geospatial-example-queries.html): Use Athena to create and query tables based on sample geospatial data.

### [Query JSON data](https://docs.aws.amazon.com/athena/latest/ug/querying-JSON.html)

Query JSON data in Athena.

### [Best practices for reading JSON data](https://docs.aws.amazon.com/athena/latest/ug/parsing-json-data.html)

JavaScript Object Notation (JSON) is a common method for encoding data structures as text.

- [Convert Athena data types to JSON](https://docs.aws.amazon.com/athena/latest/ug/converting-native-data-types-to-json.html): To convert Athena data types to JSON, use CAST.
- [Convert JSON to Athena data types](https://docs.aws.amazon.com/athena/latest/ug/converting-json-to-native-data-types.html): To convert JSON data to Athena data types, use CAST.
- [Extract JSON data from strings](https://docs.aws.amazon.com/athena/latest/ug/extracting-data-from-JSON.html): You may have source data containing JSON-encoded strings that you do not necessarily want to deserialize into a table in Athena.
- [Search for values in JSON arrays](https://docs.aws.amazon.com/athena/latest/ug/searching-for-values.html): To determine if a specific value exists inside a JSON-encoded array, use the json_array_contains function.
- [Get the length and size of JSON arrays](https://docs.aws.amazon.com/athena/latest/ug/length-and-size.html): To get the length and size of JSON arrays, you can use the json_array_length and json_size functions.
- [Troubleshoot JSON queries](https://docs.aws.amazon.com/athena/latest/ug/json-troubleshooting.html): Resources to consult when troubleshooting queries on JSON data in Amazon Athena.

### [Use ML with Athena](https://docs.aws.amazon.com/athena/latest/ug/querying-mlmodel.html)

Use Athena to write SQL statements that run Machine Learning (ML) inference using Amazon SageMaker AI.

- [Use ML with Athena syntax](https://docs.aws.amazon.com/athena/latest/ug/ml-syntax.html): The USING EXTERNAL FUNCTION clause specifies an ML with Athena function or multiple functions that can be referenced by a subsequent SELECT statement in the query.
- [See customer use examples](https://docs.aws.amazon.com/athena/latest/ug/ml-videos.html): The following videos, which use the Preview version of Machine Learning (ML) with Amazon Athena, showcase ways in which you can use SageMaker AI with Athena.

### [Query with UDFs](https://docs.aws.amazon.com/athena/latest/ug/querying-udf.html)

Learn how to use create and deploy user defined functions (UDFs) in Athena.

- [Videos on UDFs in Athena](https://docs.aws.amazon.com/athena/latest/ug/udf-videos.html): Watch the following videos to learn more about using UDFs in Athena.
- [Considerations and limitations](https://docs.aws.amazon.com/athena/latest/ug/udf-considerations-limitations.html): Consider the following points when you use user defined function (UDFs) in Athena.
- [Query using UDF query syntax](https://docs.aws.amazon.com/athena/latest/ug/udf-query-syntax.html): The USING EXTERNAL FUNCTION clause specifies a UDF or multiple UDFs that can be referenced by a subsequent SELECT statement in the query.
- [Create and deploy a UDF using Lambda](https://docs.aws.amazon.com/athena/latest/ug/udf-creating-and-deploying.html): To create a custom UDF, you create a new Java class by extending the UserDefinedFunctionHandler class.
- [Query across regions](https://docs.aws.amazon.com/athena/latest/ug/querying-across-regions.html): Use Athena to query Amazon S3 data across AWS Regions.

### [Query the AWS Glue Data Catalog](https://docs.aws.amazon.com/athena/latest/ug/querying-glue-catalog.html)

Use Athena to query metadata in Data Catalog.

- [List databases](https://docs.aws.amazon.com/athena/latest/ug/querying-glue-catalog-querying-available-databases-including-rdbms.html): The examples in this section show how to list the databases in metadata by schema name.
- [List tables](https://docs.aws.amazon.com/athena/latest/ug/querying-glue-catalog-listing-tables.html): To list metadata for tables, you can query by table schema or by table name.
- [List partitions](https://docs.aws.amazon.com/athena/latest/ug/querying-glue-catalog-listing-partitions.html): You can use SHOW PARTITIONS table_name to list the partitions for a specified table, as in the following example.
- [List columns for one table or view](https://docs.aws.amazon.com/athena/latest/ug/querying-glue-catalog-listing-columns.html): You can list all columns for a table, all columns for a view, or search for a column by name in a specified database and table.
- [List columns in common](https://docs.aws.amazon.com/athena/latest/ug/querying-glue-catalog-listing-columns-in-common.html): You can list the columns that specific tables in a database have in common.
- [List all columns](https://docs.aws.amazon.com/athena/latest/ug/querying-glue-catalog-listing-all-columns-for-all-tables.html): You can list all columns for all tables in AwsDataCatalog or for all tables in a specific database in AwsDataCatalog.

### [Query AWS service logs](https://docs.aws.amazon.com/athena/latest/ug/querying-aws-service-logs.html)

This section includes several procedures for using Amazon Athena to query popular datasets, such as AWS CloudTrail logs, Amazon CloudFront logs, Classic Load Balancer logs, Application Load Balancer logs, Amazon VPC flow logs, and Network Load Balancer logs.

### [Application Load Balancer](https://docs.aws.amazon.com/athena/latest/ug/application-load-balancer-logs.html)

Use Athena to read Application Load Balancer logs.

- [ALB access logs](https://docs.aws.amazon.com/athena/latest/ug/create-alb-access-logs-table.html)
- [Partition projection with access logs](https://docs.aws.amazon.com/athena/latest/ug/create-alb-access-logs-table-partition-projection.html): Because ALB access logs have a known structure whose partition scheme you can specify in advance, you can reduce query runtime and automate partition management by using the Athena partition projection feature.
- [Access log example queries](https://docs.aws.amazon.com/athena/latest/ug/query-alb-access-logs-examples.html): The following query counts the number of HTTP GET requests received by the load balancer grouped by the client IP address:
- [Connection logs](https://docs.aws.amazon.com/athena/latest/ug/create-alb-connection-logs-table.html)
- [Partition projection with connection logs](https://docs.aws.amazon.com/athena/latest/ug/create-alb-connection-logs-table-partition-projection.html): Because ALB connection logs have a known structure whose partition scheme you can specify in advance, you can reduce query runtime and automate partition management by using the Athena partition projection feature.
- [Connection log example queries](https://docs.aws.amazon.com/athena/latest/ug/query-alb-connection-logs-examples.html): The following query count occurrences where the value for tls_verify_status was not 'Success', grouped by client IP address:
- [Additional resources](https://docs.aws.amazon.com/athena/latest/ug/application-load-balancer-logs-additional-resources.html): For more information about using ALB logs, see the following resources.
- [Elastic Load Balancing](https://docs.aws.amazon.com/athena/latest/ug/elasticloadbalancer-classic-logs.html): Use Classic Load Balancer logs to analyze and understand traffic patterns to and from Elastic Load Balancing instances and backend applications.

### [CloudFront](https://docs.aws.amazon.com/athena/latest/ug/cloudfront-logs.html)

Use Athena to query CloudFront logs.

- [Standard logs (legacy)](https://docs.aws.amazon.com/athena/latest/ug/create-cloudfront-table-standard-logs.html)
- [Manual partitioning (JSON)](https://docs.aws.amazon.com/athena/latest/ug/create-cloudfront-table-manual-json.html)
- [Manual partitioning (Parquet)](https://docs.aws.amazon.com/athena/latest/ug/create-cloudfront-table-manual-parquet.html)
- [Partition projection (JSON)](https://docs.aws.amazon.com/athena/latest/ug/create-cloudfront-table-partition-json.html): You can reduce query runtime and automate partition management with Athena partition projection feature.
- [Partition projection (Parquet)](https://docs.aws.amazon.com/athena/latest/ug/create-cloudfront-table-partition-parquet.html): The following example CREATE TABLE statement automatically uses partition projection on CloudFront logs in Parquet, from a specified CloudFront distribution until present for a single AWS Region.
- [Real-time logs](https://docs.aws.amazon.com/athena/latest/ug/create-cloudfront-table-real-time-logs.html)
- [Additional resources](https://docs.aws.amazon.com/athena/latest/ug/cloudfront-logs-additional-resources.html): For more information about using Athena to query CloudFront logs, see the following posts from the AWS big data blog.

### [CloudTrail](https://docs.aws.amazon.com/athena/latest/ug/cloudtrail-logs.html)

Use Athena to query CloudTrail log files.

- [Understand CloudTrail logs](https://docs.aws.amazon.com/athena/latest/ug/create-cloudtrail-table-understanding.html): Before you begin creating tables, you should understand a little more about CloudTrail and how it stores data.
- [Use the CloudTrail console](https://docs.aws.amazon.com/athena/latest/ug/create-cloudtrail-table-ct.html): You can create a non-partitioned Athena table for querying CloudTrail logs directly from the CloudTrail console.
- [Use manual partitioning](https://docs.aws.amazon.com/athena/latest/ug/create-cloudtrail-table.html): You can manually create tables for CloudTrail log files in the Athena console, and then run queries in Athena.
- [Org wide trail](https://docs.aws.amazon.com/athena/latest/ug/create-cloudtrail-table-org-wide-trail.html): To create a table for organization wide CloudTrail log files in Athena, follow the steps in , but make the modifications noted in the following procedure.
- [Use partition projection](https://docs.aws.amazon.com/athena/latest/ug/create-cloudtrail-table-partition-projection.html): Because CloudTrail logs have a known structure whose partition scheme you can specify in advance, you can reduce query runtime and automate partition management by using the Athena partition projection feature.
- [Example CloudTrail log queries](https://docs.aws.amazon.com/athena/latest/ug/query-examples-cloudtrail-logs.html): The following example shows a portion of a query that returns all anonymous (unsigned) requests from the table created for CloudTrail event logs.

### [Amazon EMR](https://docs.aws.amazon.com/athena/latest/ug/emr-logs.html)

Use Athena to query Amazon EMR logs.

- [Query a basic table](https://docs.aws.amazon.com/athena/latest/ug/emr-create-table.html): The following example creates a basic table, myemrlogs, based on log files saved to s3://aws-logs-123456789012-us-west-2/elasticmapreduce/j-2ABCDE34F5GH6/elasticmapreduce/.
- [Query a partitioned table](https://docs.aws.amazon.com/athena/latest/ug/emr-create-table-partitioned.html): These examples use the same log location to create an Athena table, but the table is partitioned, and a partition is then created for each log location.
- [Global Accelerator](https://docs.aws.amazon.com/athena/latest/ug/querying-global-accelerator-flow-logs.html): Query your AWS Global Accelerator flow logs from Athena.
- [GuardDuty](https://docs.aws.amazon.com/athena/latest/ug/querying-guardduty.html): Use Athena to query your findings from Amazon GuardDuty.

### [Network Firewall](https://docs.aws.amazon.com/athena/latest/ug/querying-network-firewall-logs.html)

Query AWS Network Firewall logs with Amazon Athena.

- [Alert logs](https://docs.aws.amazon.com/athena/latest/ug/querying-network-firewall-logs-sample-alert-logs-table.html)
- [Netflow logs](https://docs.aws.amazon.com/athena/latest/ug/querying-network-firewall-logs-sample-netflow-logs-table.html)
- [Network Load Balancer](https://docs.aws.amazon.com/athena/latest/ug/networkloadbalancer-classic-logs.html): Use Athena to analyze and process logs from Network Load Balancer.

### [RouteÂ 53](https://docs.aws.amazon.com/athena/latest/ug/querying-r53-resolver-logs.html)

Use Athena to query RouteÂ 53 Resolver logs.

- [Create the table](https://docs.aws.amazon.com/athena/latest/ug/querying-r53-resolver-logs-creating-the-table.html): You can use the Query Editor in the Athena console to create and query a table for your RouteÂ 53 Resolver query logs.
- [Use partition projection](https://docs.aws.amazon.com/athena/latest/ug/querying-r53-resolver-logs-partitioning-example.html): The following example shows a CREATE TABLE statement for Resolver query logs that uses partition projection and is partitioned by vpc and by date.
- [Example queries](https://docs.aws.amazon.com/athena/latest/ug/querying-r53-resolver-logs-example-queries.html): The following examples show some queries that you can perform from Athena on your Resolver query logs.
- [Amazon SES](https://docs.aws.amazon.com/athena/latest/ug/querying-ses-logs.html): Query Amazon SES event logs with Athena.

### [Amazon VPC](https://docs.aws.amazon.com/athena/latest/ug/vpc-flow-logs.html)

Use Athena to view Amazon Virtual Private Cloud flow logs.

- [Create a table](https://docs.aws.amazon.com/athena/latest/ug/vpc-flow-logs-create-table-statement.html): The following procedure creates an Amazon VPC table for Amazon VPC flow logs.
- [Use Parquet](https://docs.aws.amazon.com/athena/latest/ug/vpc-flow-logs-parquet.html): The following procedure creates an Amazon VPC table for Amazon VPC flow logs in Apache Parquet format.
- [Use partition projection](https://docs.aws.amazon.com/athena/latest/ug/vpc-flow-logs-partition-projection.html): Use a CREATE TABLE statement like the following to create a table, partition the table, and populate the partitions automatically by using partition projection.
- [Use Parquet and partition projection](https://docs.aws.amazon.com/athena/latest/ug/vpc-flow-logs-partition-projection-parquet-example.html): The following partition projection CREATE TABLE statement for VPC flow logs is in Apache Parquet format, not Hive compatible, and partitioned by hour and by date instead of day.
- [Additional resources](https://docs.aws.amazon.com/athena/latest/ug/query-examples-vpc-logs-additional-resources.html): For more information about using Athena to analyze VPC flow logs, see the following AWS Big Data blog posts:

### [AWS WAF](https://docs.aws.amazon.com/athena/latest/ug/waf-logs.html)

Use Athena to query AWS WAF logs

- [Use partition projection](https://docs.aws.amazon.com/athena/latest/ug/create-waf-table-partition-projection.html): Because AWS WAF logs have a known structure whose partition scheme you can specify in advance, you can reduce query runtime and automate partition management by using the Athena partition projection feature.
- [Use manual partition](https://docs.aws.amazon.com/athena/latest/ug/create-waf-table-manual-partition.html): This section describes how to create a table for AWS WAF logs using manual partition.
- [Create a table without partitioning](https://docs.aws.amazon.com/athena/latest/ug/create-waf-table.html): This section describes how to create a table for AWS WAF logs without partitioning or partition projection.

### [Example queries](https://docs.aws.amazon.com/athena/latest/ug/query-examples-waf-logs.html)

Many of the example queries in this section use the partition projection table created previously.

- [Query for counts](https://docs.aws.amazon.com/athena/latest/ug/query-examples-waf-logs-count.html): The examples in this section query for counts of log items of interest.
- [Query using date and time](https://docs.aws.amazon.com/athena/latest/ug/query-examples-waf-logs-date-time.html): The examples in this section include queries that use date and time values.
- [Query for blocked requests or addresses](https://docs.aws.amazon.com/athena/latest/ug/query-examples-waf-logs-blocked-requests.html): The examples in this section query for blocked requests or addresses.

### [Query web server logs](https://docs.aws.amazon.com/athena/latest/ug/querying-web-server-logs.html)

Use Athena to query Web server logs stored in Amazon S3.

- [Query Apache logs](https://docs.aws.amazon.com/athena/latest/ug/querying-apache-logs.html): Query Apache web server logs stored in Amazon S3 from Amazon Athena.

### [IIS logs](https://docs.aws.amazon.com/athena/latest/ug/querying-iis-logs.html)

Query your Microsoft Internet Information Server (IIS) logs stored in Amazon S3 from Amazon Athena.

- [W3C extended](https://docs.aws.amazon.com/athena/latest/ug/querying-iis-logs-w3c-extended-log-file-format.html): The W3C extended log file data format has space-separated fields.
- [IIS](https://docs.aws.amazon.com/athena/latest/ug/querying-iis-logs-iis-log-file-format.html): Unlike the W3C extended format, the IIS log file format has a fixed set of fields and includes a comma as a delimiter.
- [NCSA](https://docs.aws.amazon.com/athena/latest/ug/querying-iis-logs-ncsa-log-file-format.html): IIS also uses the NCSA logging format, which has a fixed number of fields in ASCII text format separated by spaces.

### [Use ACID transactions](https://docs.aws.amazon.com/athena/latest/ug/acid-transactions.html)

Use Athena transactions for reliable and secure transactions

### [Query Delta Lake tables](https://docs.aws.amazon.com/athena/latest/ug/delta-lake-tables.html)

Query Delta Lake tables from Athena.

- [Supported column data types](https://docs.aws.amazon.com/athena/latest/ug/delta-lake-tables-supported-data-types-columns.html): This section describes the supported data types for non-partition and partition columns.
- [Get started with Delta Lake tables](https://docs.aws.amazon.com/athena/latest/ug/delta-lake-tables-getting-started.html): To be queryable, your Delta Lake table must exist in AWS Glue.
- [Query with SQL](https://docs.aws.amazon.com/athena/latest/ug/delta-lake-tables-querying.html): To query a Delta Lake table, use standard SQL SELECT syntax:
- [Synchronize Delta Lake metadata](https://docs.aws.amazon.com/athena/latest/ug/delta-lake-tables-syncing-metadata.html): Athena synchronizes table metadata, including schema, partition columns, and table properties, to AWS Glue if you use Athena to create your Delta Lake table.
- [Additional resources](https://docs.aws.amazon.com/athena/latest/ug/delta-lake-tables-additional-resources.html): For a discussion of using Delta Lake tables with AWS Glue and querying them with Athena, see Handle UPSERT data operations using open-source Delta Lake and AWS Glue in the AWS Big Data Blog.

### [Query Hudi datasets](https://docs.aws.amazon.com/athena/latest/ug/querying-hudi.html)

Query Apache Hudi datasets using Athena.

- [Considerations and limitations](https://docs.aws.amazon.com/athena/latest/ug/querying-hudi-in-athena-considerations-and-limitations.html): When you use Athena to read Apache Hudi tables, consider the following points.
- [Copy on write examples](https://docs.aws.amazon.com/athena/latest/ug/querying-hudi-copy-on-write-create-table-examples.html): If you have Hudi tables already created in AWS Glue, you can query them directly in Athena.
- [Merge on read examples](https://docs.aws.amazon.com/athena/latest/ug/querying-hudi-merge-on-read-create-table-examples.html): Hudi creates two tables in the metastore for MoR: a table for snapshot queries, and a table for read optimized queries.
- [Use Hudi metadata](https://docs.aws.amazon.com/athena/latest/ug/querying-hudi-metadata-table.html): The Apache Hudi has a metadata table that contains indexing features for improved performance like file listing, data skipping using column statistics, and a bloom filter based index.
- [Additional resources](https://docs.aws.amazon.com/athena/latest/ug/querying-hudi-additional-resources.html): For additional resources on using Apache Hudi with Athena, see the following resources.

### [Query Iceberg tables](https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg.html)

Use Athena to query Apache Iceberg tables that use Parquet data and the AWS Glue catalog.

- [Create Iceberg tables](https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg-creating-tables.html): Learn how to create Apache Iceberg tables in Amazon Athena.
- [Query Iceberg table data](https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg-table-data.html): Query Apache Iceberg tables in Athena.
- [Perform time and version travel](https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg-time-travel-and-version-travel-queries.html): Each Apache Iceberg table maintains a versioned manifest of the Amazon S3 objects that it contains.

### [Update table data](https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg-updating-iceberg-table-data.html)

Update your Apache Iceberg table data in Athena.

- [INSERT INTO](https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg-insert-into.html): Inserts data into an Iceberg table.
- [DELETE](https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg-delete.html): Athena Iceberg DELETE writes Iceberg position delete files to a table.
- [UPDATE](https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg-update.html): Athena Iceberg UPDATE writes Iceberg position delete files and newly updated rows as data files in the same transaction.
- [MERGE INTO](https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg-merge-into.html): Conditionally updates, deletes, or inserts rows into an Iceberg table.

### [Manage Iceberg tables](https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg-managing-tables.html)

Manage Apache Iceberg tables in Athena.

- [ALTER TABLE RENAME](https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg-alter-table-rename.html): Renames a table.
- [ALTER TABLE SET TBLPROPERTIES](https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg-alter-table-set-properties.html): Adds properties to an Iceberg table and sets their assigned values.
- [ALTER TABLE UNSET TBLPROPERTIES](https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg-alter-table-unset-properties.html): Drops existing properties from an Iceberg table.
- [DESCRIBE](https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg-describe-table.html): Describes table information.
- [DROP TABLE](https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg-drop-table.html): Drops an Iceberg table.
- [SHOW CREATE TABLE](https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg-show-create-table.html): Displays a CREATE TABLE DDL statement that can be used to recreate the Iceberg table in Athena.
- [SHOW TBLPROPERTIES](https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg-show-table-properties.html): Shows one or more table properties of an Iceberg table.

### [Evolve Iceberg table schema](https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg-evolving-table-schema.html)

Update your Iceberg table schema in Athena.

- [ALTER TABLE ADD COLUMNS](https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg-alter-table-add-columns.html): Adds one or more columns to an existing Iceberg table.
- [ALTER TABLE DROP COLUMN](https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg-alter-table-drop-column.html): Drops a column from an existing Iceberg table.
- [ALTER TABLE CHANGE COLUMN](https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg-alter-table-change-column.html): Changes the name, type, order or comment of a column in an Iceberg table.
- [SHOW COLUMNS](https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg-show-columns.html): Shows the columns in a table.
- [Other Iceberg DDL operations](https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg-additional-operations.html): Learn about additional operations for Apache Iceberg tables in Athena.
- [Optimize Iceberg tables](https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg-data-optimization.html): Optimize your Apache Iceberg tables in Athena.
- [Query AWS Glue Data Catalog materialized views](https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg-gdc-mv.html): Learn how to query AWS Glue Data Catalog materialized views in Athena.
- [Supported data types](https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg-supported-data-types.html): Learn about supported data types for Iceberg tables in Athena
- [Additional resources](https://docs.aws.amazon.com/athena/latest/ug/querying-iceberg-additional-resources.html): See additional articles about using Apache Iceberg with Amazon Athena.

### [Security](https://docs.aws.amazon.com/athena/latest/ug/security.html)

Configure Athena to meet your security and compliance objectives, and learn how to use other AWS services that can help you to secure your Athena resources.

### [Data protection](https://docs.aws.amazon.com/athena/latest/ug/security-data-protection.html)

Protect source data, metadata, query results, and query history in Athena.

### [Encryption at rest](https://docs.aws.amazon.com/athena/latest/ug/encryption.html)

Learn how Athena handles stored encrypted data.

### [Migrate from CSE-KMS to SSE-KMS](https://docs.aws.amazon.com/athena/latest/ug/migrating-csekms-ssekms.html)

You can specify CSE-KMS encryption in two ways â during the workgroup query results encryption configuration and in the client-side settings.

- [Convert CSE-KMS table data to SSE-KMS](https://docs.aws.amazon.com/athena/latest/ug/convert-csekms-table-ssekms.html): If your workflows currently use CSE-KMS for table data encryption, transition to SSE-KMS with the following steps.
- [Encrypt Athena query results stored in Amazon S3](https://docs.aws.amazon.com/athena/latest/ug/encrypting-query-results-stored-in-s3.html): You set up query result encryption using the Athena console or when using JDBC or ODBC.
- [Create tables based on encrypted datasets in Amazon S3](https://docs.aws.amazon.com/athena/latest/ug/creating-tables-based-on-encrypted-datasets-in-s3.html): Athena can read and write to tables whose underlying datasets are SSE-S3, SSE-KMS, or CSE-KMS encrypted.
- [Encryption in transit](https://docs.aws.amazon.com/athena/latest/ug/encryption-in-transit.html): In addition to encrypting data at rest in Amazon S3, Amazon Athena uses Transport Layer Security (TLS) encryption for data in-transit between Athena and Amazon S3, and between Athena and customer applications accessing it.
- [Key management](https://docs.aws.amazon.com/athena/latest/ug/key-management.html): Amazon Athena supports AWS Key Management Service (AWS KMS) to encrypt datasets in Amazon S3 and Athena query results.
- [Internetwork traffic privacy](https://docs.aws.amazon.com/athena/latest/ug/internetwork-traffic-privacy.html): Traffic is protected both between Athena and on-premises applications and between Athena and Amazon S3.

### [Identity and access management](https://docs.aws.amazon.com/athena/latest/ug/security-iam-athena.html)

Amazon Athena uses AWS Identity and Access Management (IAM) policies to restrict access to Athena operations.

- [AWS managed policies](https://docs.aws.amazon.com/athena/latest/ug/managed-policies.html): Learn about AWS managed policies for Athena and recent changes to those policies.
- [Data perimeters](https://docs.aws.amazon.com/athena/latest/ug/data-perimeters.html): A data perimeter is a set of permissions guardrails in your AWS environment you use to help ensure that only your trusted identities are accessing trusted resources from expected networks.
- [Access through JDBC and ODBC connections](https://docs.aws.amazon.com/athena/latest/ug/policy-actions.html): To gain access to AWS services and resources, such as Athena and the Amazon S3 buckets, provide the JDBC or ODBC driver credentials to your application.
- [Control access to Amazon S3 from Athena](https://docs.aws.amazon.com/athena/latest/ug/s3-permissions.html): Learn about policies and permissions related to accessing Amazon S3 from Athena.
- [Cross-account access to S3 buckets](https://docs.aws.amazon.com/athena/latest/ug/cross-account-permissions.html): Learn how to configure cross-account access in Athena to Amazon S3 buckets.
- [Access to databases and tables in AWS Glue](https://docs.aws.amazon.com/athena/latest/ug/fine-grained-access-to-glue-resources.html): Define resource-level permissions policies for the database and table Data Catalog objects that are used in Athena.
- [Cross-account access to AWS Glue data catalogs](https://docs.aws.amazon.com/athena/latest/ug/security-iam-cross-account-glue-catalog-access.html): Query AWS Glue data catalogs across Amazon Web Services accounts from Athena.
- [Access to encrypted metadata in the Data Catalog](https://docs.aws.amazon.com/athena/latest/ug/access-encrypted-data-glue-data-catalog.html): If you use the AWS Glue Data Catalog with Amazon Athena, you can enable encryption in the AWS Glue Data Catalog using the AWS Glue console or the API.
- [Access to workgroups and tags](https://docs.aws.amazon.com/athena/latest/ug/workgroups-access.html): A workgroup is a resource managed by Athena.

### [Use IAM policies to control workgroup access](https://docs.aws.amazon.com/athena/latest/ug/workgroups-iam-policy.html)

Learn about IAM policies for Athena workgroups.

- [Example workgroup policies](https://docs.aws.amazon.com/athena/latest/ug/example-policies-workgroup.html): This section includes example policies you can use to enable various actions on workgroups.
- [IAM Identity Center enabled workgroups](https://docs.aws.amazon.com/athena/latest/ug/workgroups-identity-center.html): Learn how to create Athena workgroups that use IAM Identity Center authentication.
- [Configure minimum encryption](https://docs.aws.amazon.com/athena/latest/ug/workgroups-minimum-encryption.html): As an administrator of an Athena SQL workgroup, you can enforce a minimal level of encryption in Amazon S3 for all query results from the workgroup.
- [Configure access to prepared statements](https://docs.aws.amazon.com/athena/latest/ug/security-iam-athena-prepared-statements.html): Learn how to use IAM permissions for prepared statements in Amazon Athena.
- [Use CalledVia context keys](https://docs.aws.amazon.com/athena/latest/ug/security-iam-athena-calledvia.html): Use the aws:CalledVia context key to ensure that callers only have access to a specified resource through Athena.
- [Allow access to the Athena Data Connector for External Hive Metastore](https://docs.aws.amazon.com/athena/latest/ug/hive-metastore-iam-access.html): The permission policy examples in this topic demonstrate required allowed actions and the resources for which they are allowed.
- [Allow Lambda function access to external Hive metastores](https://docs.aws.amazon.com/athena/latest/ug/hive-metastore-iam-access-lambda.html): Learn about the permissions related to Lambda functions for accessing external Hive metastores from Athena.
- [Permissions required to create connector and Athena catalog](https://docs.aws.amazon.com/athena/latest/ug/athena-catalog-access.html): Learn about the permissions related to CreateDataCatalog.
- [Allow access to Athena Federated Query](https://docs.aws.amazon.com/athena/latest/ug/federated-query-iam-access.html): See example IAM permissions policies for allowing Athena Federated Query
- [Allow access to UDFs](https://docs.aws.amazon.com/athena/latest/ug/udf-iam-access.html): The permission policy examples in this topic demonstrate required allowed actions and the resources for which they are allowed.
- [Allow access for ML with Athena](https://docs.aws.amazon.com/athena/latest/ug/machine-learning-iam-access.html): IAM principals who run Athena ML queries must be allowed to perform the sagemaker:invokeEndpoint action for Sagemaker endpoints that they use.
- [Enable federated access to the Athena API](https://docs.aws.amazon.com/athena/latest/ug/access-federation-saml.html): This section discusses federated access that allows a user or client application in your organization to call Amazon Athena API operations.

### [Logging and monitoring](https://docs.aws.amazon.com/athena/latest/ug/security-logging-monitoring.html)

Learn about logging and monitoring in Athena.

- [Log Amazon Athena API calls with AWS CloudTrail](https://docs.aws.amazon.com/athena/latest/ug/monitor-with-cloudtrail.html): Learn about logging Athena with AWS CloudTrail.
- [Compliance validation](https://docs.aws.amazon.com/athena/latest/ug/security-compliance-validation.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/athena/latest/ug/security-resilience.html): Learn how Athena architecture supports data redundancy as well as specific Athena features for data resiliency.

### [Infrastructure security](https://docs.aws.amazon.com/athena/latest/ug/security-infrastructure.html)

Learn how Athena isolates service traffic.

- [Connect to Amazon Athena using an interface VPC endpoint](https://docs.aws.amazon.com/athena/latest/ug/interface-vpc-endpoint.html): Access Athena using an interface VPC endpoint.
- [Configuration and vulnerability analysis](https://docs.aws.amazon.com/athena/latest/ug/security-vulnerability-management.html): Describes the customer responsibility regarding updates and patches in Athena.

### [Use Athena with Lake Formation](https://docs.aws.amazon.com/athena/latest/ug/security-athena-lake-formation.html)

Use Athena with Lake Formation.

- [How data access works](https://docs.aws.amazon.com/athena/latest/ug/lf-athena-access.html): The access workflow described in this section applies when you run Athena queries on Amazon S3 locations, data catalogs, or metadata objects that are registered with Lake Formation.
- [Considerations and limitations](https://docs.aws.amazon.com/athena/latest/ug/lf-athena-limitations.html): Consider the following when using Athena to query data registered in Lake Formation.
- [Cross-account access](https://docs.aws.amazon.com/athena/latest/ug/lf-athena-limitations-cross-account.html): To access a data catalog in another account, you can use Athena's cross-account AWS Glue feature or set up cross-account access in Lake Formation.
- [Manage user permissions](https://docs.aws.amazon.com/athena/latest/ug/lf-athena-user-permissions.html): Lake Formation vends credentials to query Amazon S3 data stores or federated catalogs that are registered with Lake Formation.

### [Use Lake Formation and JDBC or ODBC for federated access](https://docs.aws.amazon.com/athena/latest/ug/security-athena-lake-formation-jdbc.html)

Use the Athena JDBC and ODBC drivers to enable SAML 2.0-based federation with Athena.

- [Tutorial: Configuring federated access for Okta users](https://docs.aws.amazon.com/athena/latest/ug/security-athena-lake-formation-jdbc-okta-tutorial.html): Enable federated use of Athena by using Lake Formation, the Athena JDBC driver, and Okta.

### [Workload management](https://docs.aws.amazon.com/athena/latest/ug/workload-management.html)

Workload management

### [Use workgroups](https://docs.aws.amazon.com/athena/latest/ug/workgroups-manage-queries-control-costs.html)

You can use Athena workgroups to separate workloads, control team access, enforce configuration, and track query metrics and control costs.

### [Create a workgroup](https://docs.aws.amazon.com/athena/latest/ug/creating-workgroups.html)

Creating a workgroup requires permissions to CreateWorkgroup API actions.

- [Override client-side settings](https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html): Learn how workgroup settings interact with client-side settings in Athena.

### [Manage workgroups](https://docs.aws.amazon.com/athena/latest/ug/workgroups-create-update-delete.html)

Learn how to manage workgroups in Athena.

- [View the workgroup's details](https://docs.aws.amazon.com/athena/latest/ug/viewing-details-workgroups.html): For each workgroup, you can view its details.
- [Specify a workgroup for queries](https://docs.aws.amazon.com/athena/latest/ug/specify-wkgroup-to-athena-in-which-to-run-queries.html): To specify a workgroup to use, you must have permissions to the workgroup.
- [Switch workgroups](https://docs.aws.amazon.com/athena/latest/ug/switching-workgroups.html): You can switch from one workgroup to another if you have permissions to both of them.
- [Edit a workgroup](https://docs.aws.amazon.com/athena/latest/ug/editing-workgroups.html): Editing a workgroup requires permissions to UpdateWorkgroup API operations.
- [Enable or disable a workgroup](https://docs.aws.amazon.com/athena/latest/ug/workgroups-enabled-disabled.html): If you have permissions to do so, you can enable or disable workgroups in the console, by using the API operations, or with the JDBC and ODBC drivers.
- [Copy a saved query between workgroups](https://docs.aws.amazon.com/athena/latest/ug/copy-a-query-between-workgroups.html): Currently, the Athena console does not have an option to to copy a saved query from one workgroup to another directly, but you can perform the same task manually by using the following procedure.
- [Delete a workgroup](https://docs.aws.amazon.com/athena/latest/ug/deleting-workgroups.html): You can delete a workgroup if you have permissions to do so.

### [Use CloudWatch and EventBridge to monitor queries](https://docs.aws.amazon.com/athena/latest/ug/workgroups-control-limits.html)

Workgroups allow you to set data usage control limits per query or per workgroup, set up alarms when those limits are exceeded, and publish metrics to CloudWatch.

- [Enable query metrics](https://docs.aws.amazon.com/athena/latest/ug/athena-cloudwatch-metrics-enable.html): When you create a workgroup in the console, the setting for publishing query metrics to CloudWatch is selected by default.
- [Monitor query metrics with CloudWatch](https://docs.aws.amazon.com/athena/latest/ug/query-metrics-viewing.html): Monitor Athena query metrics with CloudWatch.
- [Monitor usage metrics with CloudWatch](https://docs.aws.amazon.com/athena/latest/ug/monitoring-athena-usage-metrics.html): Monitor Athena usage metrics
- [Monitor query events with EventBridge](https://docs.aws.amazon.com/athena/latest/ug/athena-events.html): Use Amazon EventBridge to receive real-time notifications of the state of your queries.
- [Configure data usage controls](https://docs.aws.amazon.com/athena/latest/ug/workgroups-setting-control-limits-cloudwatch.html): Athena allows you to set two types of cost controls: per-query limit and per-workgroup limit.
- [Use Athena workgroup APIs](https://docs.aws.amazon.com/athena/latest/ug/workgroups-api-list.html): The following are some of the REST API operations used for Athena workgroups.
- [Troubleshoot workgroups](https://docs.aws.amazon.com/athena/latest/ug/workgroups-troubleshooting.html): Troubleshoot issues with workgroups in Athena.

### [Manage query processing capacity](https://docs.aws.amazon.com/athena/latest/ug/capacity-management.html)

Learn how to use capacity reservations to manage query processing capacity in Athena

- [Determine capacity requirements](https://docs.aws.amazon.com/athena/latest/ug/capacity-management-requirements.html): Estimate the required number of data processing units for your capacity reservation in Athena.
- [Create capacity reservations](https://docs.aws.amazon.com/athena/latest/ug/capacity-management-creating-capacity-reservations.html): Create a capacity reservation to provision processing capacity for the Athena workgroups that you specify.
- [Control capacity usage](https://docs.aws.amazon.com/athena/latest/ug/capacity-management-control-capacity-usage.html): You can control the number of DPU that Athena allocates to your queries by setting maximum or minimum DPU controls.
- [Automatically adjust capacity](https://docs.aws.amazon.com/athena/latest/ug/capacity-management-automatically-adjust-capacity.html): You can automatically adjust the capacity of your reservation in response to workload utilization using Athena's auto-scaling solution.

### [Manage reservations](https://docs.aws.amazon.com/athena/latest/ug/capacity-management-managing-reservations.html)

Manage your capacity reservations in Amazon Athena.

- [Edit capacity reservations](https://docs.aws.amazon.com/athena/latest/ug/capacity-management-editing-capacity-reservations.html): After you create a capacity reservation, you can adjust its number of DPUs and add or remove its custom tags.
- [Add workgroups to a reservation](https://docs.aws.amazon.com/athena/latest/ug/capacity-management-adding-workgroups-to-a-reservation.html): After you create a capacity reservation, you can add up to 20 workgroups to the reservation.
- [Remove a workgroup from a reservation](https://docs.aws.amazon.com/athena/latest/ug/capacity-management-removing-a-workgroup-from-a-reservation.html): If you no longer require dedicated capacity for a workgroup or want to move a workgroup to its own reservation, you can remove it at any time.
- [Cancel a capacity reservation](https://docs.aws.amazon.com/athena/latest/ug/capacity-management-cancelling-a-capacity-reservation.html): If you no longer want to use a capacity reservation, you can cancel it.
- [Delete a capacity reservation](https://docs.aws.amazon.com/athena/latest/ug/capacity-management-deleting-a-capacity-reservation.html): If you want to remove all references to a cancelled capacity reservation, you can delete the reservation.

### [IAM policies for capacity reservations](https://docs.aws.amazon.com/athena/latest/ug/capacity-reservations-iam-policy.html)

Learn about IAM policies for controlling access to capacity reservations.

- [Example policies](https://docs.aws.amazon.com/athena/latest/ug/example-policies-capacity-reservations.html): Use resource policies to control access to your capacity reservations in Athena.
- [Athena capacity reservation APIs](https://docs.aws.amazon.com/athena/latest/ug/capacity-management-api-list.html): Reference the capacity management API actions in Amazon Athena.

### [Optimize performance](https://docs.aws.amazon.com/athena/latest/ug/performance-tuning.html)

Learn some techniques for improving the memory usage and performance of your Athena queries.

- [Optimize service use](https://docs.aws.amazon.com/athena/latest/ug/performance-tuning-service-level-considerations.html): Service level considerations include the number of workloads you run per account, service quotas not only for Athena, but across services, and thinking about how to reduce 'out of resource' errors.
- [Optimize queries](https://docs.aws.amazon.com/athena/latest/ug/performance-tuning-query-optimization-techniques.html): Use the query optimization techniques described in this section to make queries run faster or as workarounds for queries that exceed resource limits in Athena.
- [Optimize data](https://docs.aws.amazon.com/athena/latest/ug/performance-tuning-data-optimization-techniques.html): Performance depends not only on queries, but also importantly on how your dataset is organized and on the file format and compression that it uses.
- [Use columnar storage](https://docs.aws.amazon.com/athena/latest/ug/columnar-storage.html): Learn about using columnar storage formats in Athena.

### [Use partitioning and bucketing](https://docs.aws.amazon.com/athena/latest/ug/ctas-partitioning-and-bucketing.html)

Learn the advantages of partitioning and bucketing as they apply to CTAS queries in Athena.

- [What is partitioning?](https://docs.aws.amazon.com/athena/latest/ug/ctas-partitioning-and-bucketing-what-is-partitioning.html): Partitioning means organizing data into directories (or "prefixes") on Amazon S3 based on a particular property of the data.
- [What is bucketing?](https://docs.aws.amazon.com/athena/latest/ug/ctas-partitioning-and-bucketing-what-is-bucketing.html): Bucketing is a way to organize the records of a dataset into categories called buckets.
- [Additional resources](https://docs.aws.amazon.com/athena/latest/ug/ctas-partitioning-and-bucketing-additional-resources.html)
- [Partition your data](https://docs.aws.amazon.com/athena/latest/ug/partitions.html): Learn about partitioning data in Athena.

### [Partition projection](https://docs.aws.amazon.com/athena/latest/ug/partition-projection.html)

Use partition projection in Athena to speed up query processing of highly partitioned tables and automate partition management.

- [Set up partition projection](https://docs.aws.amazon.com/athena/latest/ug/partition-projection-setting-up.html): Set up partition projection in Athena.
- [Supported types for partition projection](https://docs.aws.amazon.com/athena/latest/ug/partition-projection-supported-types.html): A table can have any combination of enum, integer, date, or injected partition column types.
- [Use dynamic ID partitioning](https://docs.aws.amazon.com/athena/latest/ug/partition-projection-dynamic-id-partitioning.html): Use dynamic ID partitioning for data partitioned by high cardinality or unknown properties.

### [Amazon Data Firehose example](https://docs.aws.amazon.com/athena/latest/ug/partition-projection-kinesis-firehose-example.html)

Example that shows how to use partition projection in Athena .

- [How to use the date type](https://docs.aws.amazon.com/athena/latest/ug/partition-projection-kinesis-firehose-example-using-the-date-type.html): When you use the date type for a projected partition key, you must specify a range.
- [How to choose partition keys](https://docs.aws.amazon.com/athena/latest/ug/partition-projection-kinesis-firehose-example-choosing-partition-keys.html): You can specify how partition projection maps the partition locations to partition keys.
- [Use custom prefixes](https://docs.aws.amazon.com/athena/latest/ug/partition-projection-kinesis-firehose-example-using-custom-prefixes-and-dynamic-partitioning.html): Firehose can be configured with custom prefixes and dynamic partitioning.

### [Prevent throttling](https://docs.aws.amazon.com/athena/latest/ug/performance-tuning-s3-throttling.html)

Avoid Amazon S3 throttling issues when you use Athena.

- [Reduce throttling at the service level](https://docs.aws.amazon.com/athena/latest/ug/performance-tuning-s3-throttling-reduce-throttling-at-the-service-level.html): To avoid Amazon S3 throttling at the service level, you can monitor your usage and adjust your service quotas, or you use certain techniques like partitioning.
- [Optimize your tables](https://docs.aws.amazon.com/athena/latest/ug/performance-tuning-s3-throttling-optimizing-your-tables.html): Structuring your data is important if you encounter throttling issues.
- [Optimize your queries](https://docs.aws.amazon.com/athena/latest/ug/performance-tuning-s3-throttling-optimizing-queries.html): Use the suggestions in this section for optimizing your SQL queries in Athena.
- [Additional resources](https://docs.aws.amazon.com/athena/latest/ug/performance-tuning-additional-resources.html): For additional information about performance tuning in Athena, consider the following resources:

### [Use compression](https://docs.aws.amazon.com/athena/latest/ug/compression-formats.html)

Learn about the compression support in Athena for various storage file formats.

- [Hive table compression](https://docs.aws.amazon.com/athena/latest/ug/compression-support-hive.html): The compression options for Hive tables in Athena vary by engine version and file format.
- [Iceberg table compression](https://docs.aws.amazon.com/athena/latest/ug/compression-support-iceberg.html): The compression options for Iceberg tables in Athena vary by engine version and file format.
- [ZSTD compression levels](https://docs.aws.amazon.com/athena/latest/ug/compression-support-zstd-levels.html): Learn how to specify ZSTD compression levels in Athena

### [Tag resources](https://docs.aws.amazon.com/athena/latest/ug/tags.html)

Use tags to label Athena resources like workgroups and data catalogs for management purposes.

- [Tags for workgroups](https://docs.aws.amazon.com/athena/latest/ug/tags-console.html): Using the Athena console, you can see which tags are in use by each workgroup in your account.
- [API and CLI tag operations](https://docs.aws.amazon.com/athena/latest/ug/tags-operations.html): Use the following tag operations to add, remove, or list tags on a resource.
- [Use tag-based IAM access control](https://docs.aws.amazon.com/athena/latest/ug/tags-access-control.html): Create IAM policies with resource tags, as shown in these examples.
- [Service Quotas](https://docs.aws.amazon.com/athena/latest/ug/service-limits.html): Learn about the service quotas for Athena.

### [Athena engine versioning](https://docs.aws.amazon.com/athena/latest/ug/engine-versions.html)

Learn about Athena query engine versioning.

- [Change engine versions](https://docs.aws.amazon.com/athena/latest/ug/engine-versions-changing.html): Change the engine version for an Athena workgroup.
- [Engine version 3](https://docs.aws.amazon.com/athena/latest/ug/engine-versions-reference-0003.html): Learn about changes in Athena engine version 3.

### [SQL reference for Athena](https://docs.aws.amazon.com/athena/latest/ug/ddl-sql-reference.html)

Learn about the DML and DDL statements used in Athena SQL.

### [Data types in Athena](https://docs.aws.amazon.com/athena/latest/ug/data-types.html)

Learn about the data types used in Athena.

- [Data type examples](https://docs.aws.amazon.com/athena/latest/ug/data-types-examples.html): The following table shows example literals for DML data types.
- [Considerations for data types](https://docs.aws.amazon.com/athena/latest/ug/data-types-considerations.html)
- [Work with timestamp data](https://docs.aws.amazon.com/athena/latest/ug/data-types-timestamps.html): This section describes some considerations for working with timestamp data in Athena.

### [DML queries, functions, and operators](https://docs.aws.amazon.com/athena/latest/ug/dml-queries-functions-operators.html)

Learn about DML query statements and functions used in Athena.

- [SELECT](https://docs.aws.amazon.com/athena/latest/ug/select.html): Summary reference for the SELECT statement in Athena.
- [INSERT INTO](https://docs.aws.amazon.com/athena/latest/ug/insert-into.html): Inserts new rows into a destination table based on a SELECT query statement that runs on a source table, or based on a set of VALUES provided as part of the statement.
- [VALUES](https://docs.aws.amazon.com/athena/latest/ug/values-statement.html): Use the VALUES statement to create literal inline tables.
- [DELETE](https://docs.aws.amazon.com/athena/latest/ug/delete-statement.html): Delete rows in Apache Iceberg tables in Athena.
- [UPDATE](https://docs.aws.amazon.com/athena/latest/ug/update-statement.html): Update rows in Apache Iceberg tables in Athena.
- [MERGE INTO](https://docs.aws.amazon.com/athena/latest/ug/merge-into-statement.html): Conditionally updates, deletes, or inserts rows into an Apache Iceberg table in Athena.
- [OPTIMIZE](https://docs.aws.amazon.com/athena/latest/ug/optimize-statement.html): Optimizes rows in Apache Iceberg tables in Athena.
- [VACUUM](https://docs.aws.amazon.com/athena/latest/ug/vacuum-statement.html): Remove no longer needed data files for Apache Iceberg tables in Athena.

### [EXPLAIN and EXPLAIN ANALYZE](https://docs.aws.amazon.com/athena/latest/ug/athena-explain-statement.html)

Use the EXPLAIN and EXPLAIN ANALYZE statements in Athena to analyze and optimize your SQL queries.

- [Understand EXPLAIN results](https://docs.aws.amazon.com/athena/latest/ug/athena-explain-statement-understanding.html): Learn to understand EXPLAIN statement results in Athena.

### [PREPARE](https://docs.aws.amazon.com/athena/latest/ug/sql-prepare.html)

Create parameterized SQL statements for reuse.

- [EXECUTE](https://docs.aws.amazon.com/athena/latest/ug/sql-execute.html): Run a prepared statement, supplying values for optional parameters.
- [DEALLOCATE PREPARE](https://docs.aws.amazon.com/athena/latest/ug/sql-deallocate-prepare.html): Removes the prepared statement with the specified name from the prepared statements in the current workgroup.
- [UNLOAD](https://docs.aws.amazon.com/athena/latest/ug/unload.html): Specify the output location and file format for the results of a query in Athena.

### [Functions](https://docs.aws.amazon.com/athena/latest/ug/functions.html)

Resource links for functions in Athena.

- [Athena engine version 3](https://docs.aws.amazon.com/athena/latest/ug/functions-env3.html): Resource links for functions in Athena.
- [Use supported time zones](https://docs.aws.amazon.com/athena/latest/ug/athena-supported-time-zones.html): Lists the time zones that can be used with the AT TIME ZONE operator in Amazon Athena.

### [DDL statements](https://docs.aws.amazon.com/athena/latest/ug/ddl-reference.html)

Use the supported data definition language (DDL) statements presented here directly in Athena.

- [Unsupported DDL](https://docs.aws.amazon.com/athena/latest/ug/unsupported-ddl.html): Learn which DDL commands are not supported in Athena
- [ALTER DATABASE SET DBPROPERTIES](https://docs.aws.amazon.com/athena/latest/ug/alter-database-set-dbproperties.html): Creates one or more properties for a database.
- [ALTER TABLE ADD COLUMNS](https://docs.aws.amazon.com/athena/latest/ug/alter-table-add-columns.html): Add columns dynamically to an existing table in Athena.
- [ALTER TABLE ADD PARTITION](https://docs.aws.amazon.com/athena/latest/ug/alter-table-add-partition.html): Creates one or more partition columns for the table.
- [ALTER TABLE CHANGE COLUMN](https://docs.aws.amazon.com/athena/latest/ug/alter-table-change-column.html): Change the name, type, order, or comment for a column in an Athena table.
- [ALTER TABLE DROP PARTITION](https://docs.aws.amazon.com/athena/latest/ug/alter-table-drop-partition.html): Drops one or more specified partitions for the named table.
- [ALTER TABLE RENAME PARTITION](https://docs.aws.amazon.com/athena/latest/ug/alter-table-rename-partition.html): Rename partition values for a specified table.
- [ALTER TABLE REPLACE COLUMNS](https://docs.aws.amazon.com/athena/latest/ug/alter-table-replace-columns.html): Replace columns dynamically in an existing table in Athena.
- [ALTER TABLE SET LOCATION](https://docs.aws.amazon.com/athena/latest/ug/alter-table-set-location.html): Changes the location for the table named table_name, and optionally a partition with partition_spec.
- [ALTER TABLE SET TBLPROPERTIES](https://docs.aws.amazon.com/athena/latest/ug/alter-table-set-tblproperties.html): Use DDL to change a table's custom or predefined properties and their values.
- [ALTER VIEW DIALECT](https://docs.aws.amazon.com/athena/latest/ug/alter-view-dialect.html): Adds or drops an engine dialect from a AWS Glue Data Catalog view.
- [CREATE DATABASE](https://docs.aws.amazon.com/athena/latest/ug/create-database.html): Creates a database.
- [CREATE TABLE](https://docs.aws.amazon.com/athena/latest/ug/create-table.html): Use the CREATE TABLE DDL statement to create tables in Athena.
- [CREATE TABLE AS](https://docs.aws.amazon.com/athena/latest/ug/create-table-as.html): Create a table with the results of a inline SELECT query.
- [CREATE VIEW](https://docs.aws.amazon.com/athena/latest/ug/create-view.html): Learn how to create Athena and AWS Glue Data Catalog views in Athena.
- [DESCRIBE](https://docs.aws.amazon.com/athena/latest/ug/describe-table.html): Shows one or more columns, including partition columns, for the specified table.
- [DESCRIBE VIEW](https://docs.aws.amazon.com/athena/latest/ug/describe-view.html): See the list of columns in an Athena or AWS Glue Data Catalog view.
- [DROP DATABASE](https://docs.aws.amazon.com/athena/latest/ug/drop-database.html): Removes the named database from the catalog.
- [DROP TABLE](https://docs.aws.amazon.com/athena/latest/ug/drop-table.html): Removes the metadata table definition for the table named table_name.
- [DROP VIEW](https://docs.aws.amazon.com/athena/latest/ug/drop-view.html): Delete an existing view in Athena.
- [MSCK REPAIR TABLE](https://docs.aws.amazon.com/athena/latest/ug/msck-repair-table.html): Learn how to use MSCK REPAIR TABLE in Athena.
- [SHOW COLUMNS](https://docs.aws.amazon.com/athena/latest/ug/show-columns.html): Display the names of the columns in a specified Athena table, Athena view, or Data Catalog view.
- [SHOW CREATE TABLE](https://docs.aws.amazon.com/athena/latest/ug/show-create-table.html): Analyzes an existing table named table_name to generate the query that created it.
- [SHOW CREATE VIEW](https://docs.aws.amazon.com/athena/latest/ug/show-create-view.html): See the SQL statement that created a view.
- [SHOW DATABASES](https://docs.aws.amazon.com/athena/latest/ug/show-databases.html): List the databases the default Athena SQL data catalog.
- [SHOW PARTITIONS](https://docs.aws.amazon.com/athena/latest/ug/show-partitions.html): List all the partitions in an Athena table.
- [SHOW TABLES](https://docs.aws.amazon.com/athena/latest/ug/show-tables.html): Lists all the base tables and views in a database.
- [SHOW TBLPROPERTIES](https://docs.aws.amazon.com/athena/latest/ug/show-tblproperties.html): Lists table properties for the named table.
- [SHOW VIEWS](https://docs.aws.amazon.com/athena/latest/ug/show-views.html): List the views in a database.
- [Considerations and limitations](https://docs.aws.amazon.com/athena/latest/ug/other-notable-limitations.html): Learn the considerations and limitations about using SQL queries in Athena.

### [Troubleshoot issues](https://docs.aws.amazon.com/athena/latest/ug/troubleshooting-athena.html)

Troubleshoot errors in Athena.

- [Athena error catalog](https://docs.aws.amazon.com/athena/latest/ug/error-reference.html): See standardized error information for queries in Athena.

### [Code samples](https://docs.aws.amazon.com/athena/latest/ug/code-samples.html)

Use the SDK for Java 2.x to write Athena applications.

- [Constants](https://docs.aws.amazon.com/athena/latest/ug/constants.html): The ExampleConstants.java class demonstrates how to query a table created by the tutorial in Athena.
- [Create a client to access Athena](https://docs.aws.amazon.com/athena/latest/ug/create-a-client-to-access-athena.html): The AthenaClientFactory.java class shows how to create and configure an Amazon Athena client.
- [Start query execution](https://docs.aws.amazon.com/athena/latest/ug/start-query-execution.html): The StartQueryExample shows how to submit a query to Athena, wait until the results become available, and then process the results.
- [Stop query execution](https://docs.aws.amazon.com/athena/latest/ug/stop-query-execution.html): The StopQueryExecutionExample runs an example query, immediately stops the query, and checks the status of the query to ensure that it was canceled.
- [List query executions](https://docs.aws.amazon.com/athena/latest/ug/list-query-executions.html): The ListQueryExecutionsExample shows how to obtain a list of query execution IDs.
- [Create a named query](https://docs.aws.amazon.com/athena/latest/ug/create-a-named-query.html): The CreateNamedQueryExample shows how to create a named query.
- [Delete a named query](https://docs.aws.amazon.com/athena/latest/ug/delete-a-named-query.html): The DeleteNamedQueryExample shows how to delete a named query by using the named query ID.
- [List named queries](https://docs.aws.amazon.com/athena/latest/ug/list-named-queries.html): The ListNamedQueryExample shows how to obtain a list of named query IDs.


## [Use Apache Spark](https://docs.aws.amazon.com/athena/latest/ug/notebooks-spark.html)

- [Release versions](https://docs.aws.amazon.com/athena/latest/ug/notebooks-spark-release-versions.html): Amazon Athena for Apache Spark offers the following release versions:
- [Considerations and limitations](https://docs.aws.amazon.com/athena/latest/ug/notebooks-spark-considerations-and-limitations.html)
- [Get started](https://docs.aws.amazon.com/athena/latest/ug/notebooks-spark-getting-started.html): Get started using Jupyter notebooks in Athena.
- [Manage notebook files](https://docs.aws.amazon.com/athena/latest/ug/notebooks-spark-managing.html): Manage notebook files in Athena.

### [Notebook editor](https://docs.aws.amazon.com/athena/latest/ug/notebooks-spark-editor.html)

Use the Athena notebook editor for writing and running code for Jupyter notebooks.

### [Magic commands](https://docs.aws.amazon.com/athena/latest/ug/notebooks-spark-magics.html)

Use magic commands in Athena for Apache Spark to show session information and perform specialized functions.

- [Cell magics](https://docs.aws.amazon.com/athena/latest/ug/notebooks-spark-magics-cell-magics.html): Magics that are written on several lines are preceded by a double percent sign (%%) and are called cell magic functions or cell magics.
- [Line Magics](https://docs.aws.amazon.com/athena/latest/ug/notebooks-spark-magics-line-magics.html): Magics that are on a single line are preceded by a percent sign (%) and are called line magic functions or line magics.
- [Graph magics](https://docs.aws.amazon.com/athena/latest/ug/notebooks-spark-magics-graphs.html): Use magic commands in Athena for Spark to create data graphs in your notebooks.

### [Non-Hive table formats](https://docs.aws.amazon.com/athena/latest/ug/notebooks-spark-table-formats.html)

Learn how to use non-Hive table formats in Amazon Athena for Apache Spark.

- [Iceberg](https://docs.aws.amazon.com/athena/latest/ug/notebooks-spark-table-formats-apache-iceberg.html): Use Apache Iceberg tables in Amazon Athena for Apache Spark.
- [Hudi](https://docs.aws.amazon.com/athena/latest/ug/notebooks-spark-table-formats-apache-hudi.html): Use Apache Hudi tables in Amazon Athena for Apache Spark.
- [Delta Lake](https://docs.aws.amazon.com/athena/latest/ug/notebooks-spark-table-formats-linux-foundation-delta-lake.html): Use Linux Foundation Delta Lake tables in Amazon Athena for Apache Spark.

### [Python library support](https://docs.aws.amazon.com/athena/latest/ug/notebooks-spark-python-library-support.html)

Learn about Athena support for the runtimes, libraries, and packages used in Amazon Athena for Apache Spark.

- [Python libraries](https://docs.aws.amazon.com/athena/latest/ug/notebooks-spark-preinstalled-python-libraries.html): See the list of Python libraries preinstalled in Amazon Athena for Apache Spark.
- [Import files and libraries](https://docs.aws.amazon.com/athena/latest/ug/notebooks-import-files-libraries.html): Import files and libraries into an Apache Spark notebook in Athena.
- [Specify custom configuration](https://docs.aws.amazon.com/athena/latest/ug/notebooks-spark-custom-jar-cfg.html): Learn how to add JAR files and use a custom configuration for your Athena for Spark sessions.
- [Supported data and storage formats](https://docs.aws.amazon.com/athena/latest/ug/notebooks-spark-data-and-storage-formats.html): See the data and storage formats supported in Amazon Athena for Apache Spark.
- [Monitor Apache Spark](https://docs.aws.amazon.com/athena/latest/ug/notebooks-spark-metrics.html): Monitor Apache Spark in Athena with CloudWatch metrics.
- [Cost attribution](https://docs.aws.amazon.com/athena/latest/ug/notebooks-spark-cost-attribution.html): Track costs for individual Apache Spark sessions using cost allocation tags in Athena.
- [Logging and monitoring](https://docs.aws.amazon.com/athena/latest/ug/notebooks-spark-logging-monitoring.html): Configure managed, Amazon S3, or CloudWatch logging and monitoring for your Athena Apache Spark sessions.
- [Spark UI access](https://docs.aws.amazon.com/athena/latest/ug/notebooks-spark-ui-access.html): View and monitor your Apache Spark jobs using native Spark UIs in Athena.
- [Spark Connect](https://docs.aws.amazon.com/athena/latest/ug/notebooks-spark-connect.html): Connect to Athena Apache Spark sessions remotely using Spark Connect client-server architecture.
- [Enable requester pays buckets](https://docs.aws.amazon.com/athena/latest/ug/notebooks-spark-requester-pays.html): Learn how to enable requester pays Amazon S3 buckets in Athena for Spark
- [Lake Formation integration](https://docs.aws.amazon.com/athena/latest/ug/notebooks-spark-lakeformation.html): Use AWS Lake Formation with Athena Apache Spark interactive sessions for fine-grained access control.
- [Enable Spark encryption](https://docs.aws.amazon.com/athena/latest/ug/notebooks-spark-encryption.html): Learn how to enable encryption for Spark clusters in Athena for Spark.
- [Cross-account catalog access](https://docs.aws.amazon.com/athena/latest/ug/spark-notebooks-cross-account-glue.html): Learn how to configure cross-account AWS Glue access for Spark in Athena.
- [Service quotas](https://docs.aws.amazon.com/athena/latest/ug/notebooks-spark-quotas.html): Learn about the service quotas in Amazon Athena for Apache Spark
- [Athena Spark APIs](https://docs.aws.amazon.com/athena/latest/ug/notebooks-spark-api-list.html): Explore the notebook API actions in Amazon Athena.

### [Troubleshoot](https://docs.aws.amazon.com/athena/latest/ug/notebooks-spark-troubleshooting.html)

Troubleshoot issues with Jupyter notebooks and Python in Athena.

- [Known issues](https://docs.aws.amazon.com/athena/latest/ug/notebooks-spark-known-issues.html): Learn about known issues in Athena for Apache Spark.
- [Spark-enabled workgroups](https://docs.aws.amazon.com/athena/latest/ug/notebooks-spark-troubleshooting-workgroups.html): Troubleshoot Spark-enabled workgroups in Athena.
- [Use Spark EXPLAIN](https://docs.aws.amazon.com/athena/latest/ug/notebooks-spark-troubleshooting-explain.html): Use the Spark EXPLAIN statement to troubleshoot Spark SQL in Athena.
- [Log application events](https://docs.aws.amazon.com/athena/latest/ug/notebooks-spark-logging.html): Log Spark session events in Athena to CloudWatch.
- [Use CloudTrail for notebook API calls](https://docs.aws.amazon.com/athena/latest/ug/notebooks-spark-troubleshooting-cloudtrail.html): Use CloudTrail to troubleshoot Athena notebook API calls
- [Code block size limit](https://docs.aws.amazon.com/athena/latest/ug/notebooks-spark-troubleshooting-code-block-size-limit.html): Learn how to overcome the 68k code block character limit in Athena for Spark.
- [Session errors](https://docs.aws.amazon.com/athena/latest/ug/notebooks-spark-troubleshooting-sessions.html): Use the information in this section to troubleshoot session issues.
- [Table errors](https://docs.aws.amazon.com/athena/latest/ug/notebooks-spark-troubleshooting-tables.html): Use the information in this section to troubleshoot Athena for Spark table errors.
- [Get support](https://docs.aws.amazon.com/athena/latest/ug/notebooks-spark-troubleshooting-support.html): For assistance from AWS, choose Support, Support Center from the AWS Management Console.
