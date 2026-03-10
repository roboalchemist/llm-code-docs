# Source: https://docs.aws.amazon.com/keyspaces/latest/devguide/llms.txt

# Amazon Keyspaces (for Apache Cassandra) Developer Guide

> Provides a conceptual overview of Amazon Keyspaces and includes detailed development instructions for using the various features.

- [Libraries and tools](https://docs.aws.amazon.com/keyspaces/latest/devguide/examples-tools.html)
- [Quotas](https://docs.aws.amazon.com/keyspaces/latest/devguide/quotas.html)
- [Document history](https://docs.aws.amazon.com/keyspaces/latest/devguide/doc-history.html)

## [What is Amazon Keyspaces?](https://docs.aws.amazon.com/keyspaces/latest/devguide/what-is-keyspaces.html)

- [How it works](https://docs.aws.amazon.com/keyspaces/latest/devguide/how-it-works.html): Amazon Keyspaces removes the administrative overhead of managing Cassandra.
- [Use cases](https://docs.aws.amazon.com/keyspaces/latest/devguide/use-cases.html): Learn how to use Amazon Keyspaces in your high-performance, mission-critical applications.
- [What is CQL?](https://docs.aws.amazon.com/keyspaces/latest/devguide/what-is-cql.html): Learn about Cassandra Query Language (CQL) in Amazon Keyspaces and how to use it with cqlsh, with the AWS Management Console, and programmatically with your favorite Cassandra client.


## [Compare Amazon Keyspaces with Cassandra](https://docs.aws.amazon.com/keyspaces/latest/devguide/keyspaces-vs-cassandra.html)

- [Functional differences with Apache Cassandra](https://docs.aws.amazon.com/keyspaces/latest/devguide/functional-differences.html): Learn about the key functional differences between Apache Cassandra and Amazon Keyspaces, and how these might affect your workloads when you migrate.
- [Supported Cassandra APIs, operations, functions, and data types](https://docs.aws.amazon.com/keyspaces/latest/devguide/cassandra-apis.html): Learn which Cassandra API operations, control-plane operations, data-plane operations, functions, and data types are supported by Amazon Keyspaces.
- [Supported Cassandra consistency levels](https://docs.aws.amazon.com/keyspaces/latest/devguide/consistency.html): Learn about the supported levels of read and write consistency in Amazon Keyspaces and how many request units each type incurs.


## [Migrating to Amazon Keyspaces](https://docs.aws.amazon.com/keyspaces/latest/devguide/migrating.html)

### [Migrating from Cassandra](https://docs.aws.amazon.com/keyspaces/latest/devguide/migrating-cassandra.html)

Learn how to create a migration plan to successfully migrate your data and application from Apache Cassandra to Amazon Keyspaces.

### [Online migration](https://docs.aws.amazon.com/keyspaces/latest/devguide/migrating-online.html)

Learn key strategies for migrating from Apache Cassandra to Amazon Keyspaces online while maintaining application availability and data consistency through techniques like dual writes, historical data migration, validation, and gradual roll out.

- [Writing new data](https://docs.aws.amazon.com/keyspaces/latest/devguide/migration-online-dw.html): Learn about how to implement dual writes during an online migration to Amazon Keyspaces.
- [Uploading historical data](https://docs.aws.amazon.com/keyspaces/latest/devguide/migration-online-historical.html): Learn about how to upload historical data during an online migration to Amazon Keyspaces.
- [Validating data consistency](https://docs.aws.amazon.com/keyspaces/latest/devguide/migration-online-validation.html): Learn how to validate data consistency during an online migration to Amazon Keyspaces.
- [Application migration](https://docs.aws.amazon.com/keyspaces/latest/devguide/migration-online-app-migration.html): Learn how to migrate the application during an online migration to Amazon Keyspaces.
- [Decommissioning Cassandra](https://docs.aws.amazon.com/keyspaces/latest/devguide/migration-online-decommission.html): Learn how to decommission Cassandra after an online migration to Amazon Keyspaces.
- [Offline migration](https://docs.aws.amazon.com/keyspaces/latest/devguide/migrating-offline.html): Learn how to perform an offline Apache Cassandra to Amazon Keyspaces migration using AWS Glue jobs to extract, transform, and load data via Amazon S3 for minimal downtime.

### [Hybrid migration](https://docs.aws.amazon.com/keyspaces/latest/devguide/migrating-hybrid.html)

Learn how to implement a hybrid solution when migrating from Apache Cassandra to Amazon Keyspaces online in near real time.

- [CQLReplicator](https://docs.aws.amazon.com/keyspaces/latest/devguide/migration-hybrid-cql-rep.html): Learn about how to use the CQLReplicator for a hybrid migration from Apache Cassandra to Amazon Keyspaces.
- [Change data capture](https://docs.aws.amazon.com/keyspaces/latest/devguide/migration-hybrid-cdc.html): Learn how to migrate data using change data capture (CDC) pipelines from Apache Cassandra to Amazon Keyspaces.

### [Migration tools](https://docs.aws.amazon.com/keyspaces/latest/devguide/migrating-tools.html)

Learn about the tools and tutorials available to bulk upload or migrate data to Amazon Keyspaces.

### [Loading data using cqlsh](https://docs.aws.amazon.com/keyspaces/latest/devguide/bulk-upload.html)

Learn how to use the cqlsh COPY command to load data from a CSV file into Amazon Keyspaces tables.

- [Prerequisites](https://docs.aws.amazon.com/keyspaces/latest/devguide/bulk-upload-prequs.html): Set up your environment to upload data to Amazon Keyspaces using cqlsh COPY FROM.
- [Step 1: Create source and target](https://docs.aws.amazon.com/keyspaces/latest/devguide/bulk-upload-source.html): Create the source file and target table in Amazon Keyspaces for data migration with cqlsh COPY.
- [Step 2: Prepare the source data](https://docs.aws.amazon.com/keyspaces/latest/devguide/bulk-upload-prepare-data.html): Learn how to prepare your source data to successfully load data from a CSV file into an Amazon Keyspaces table.
- [Step 3: Set throughput capacity for the table](https://docs.aws.amazon.com/keyspaces/latest/devguide/bulk-upload-capacity.html): This tutorial shows you how to tune cqlsh to load data within a set time range.
- [Step 4: Configure cqlsh COPY FROM settings](https://docs.aws.amazon.com/keyspaces/latest/devguide/bulk-upload-config.html): This section outlines how to determine the parameter values for cqlsh COPY FROM.
- [Step 5: Run the cqlsh COPY FROM command](https://docs.aws.amazon.com/keyspaces/latest/devguide/bulk-upload-run.html): To run the cqlsh COPY FROM command, complete the following steps.
- [Troubleshooting](https://docs.aws.amazon.com/keyspaces/latest/devguide/bulk-upload-troubleshooting.html): After the data upload has completed, check to see if rows were skipped.

### [Loading data using DSBulk](https://docs.aws.amazon.com/keyspaces/latest/devguide/dsbulk-upload.html)

Learn how to use the dsbulk tool to bulk upload data to Amazon Keyspaces.

- [Prerequisites](https://docs.aws.amazon.com/keyspaces/latest/devguide/dsbulk-upload-prequs.html): Set up your environment to migrate data to Amazon Keyspaces using DSBulk.
- [Step 1: Create source and target](https://docs.aws.amazon.com/keyspaces/latest/devguide/dsbulk-upload-source.html): Create the source file and target table in Amazon Keyspaces for data migration with dsbulk.
- [Step 2: Prepare the data](https://docs.aws.amazon.com/keyspaces/latest/devguide/dsbulk-upload-prepare-data.html): Learn how to prepare data before uploading to Amazon Keyspaces with dsbulk.
- [Step 3: Set throughput capacity for the table](https://docs.aws.amazon.com/keyspaces/latest/devguide/dsbulk-upload-capacity.html): Learn how to provision capacity for the Amazon Keyspaces target table before migrating data with dsbulk.
- [Step 4: Configure DSBulk settings](https://docs.aws.amazon.com/keyspaces/latest/devguide/dsbulk-upload-config.html): Apply migration settings for data migration to Amazon Keyspaces with dsbulk.
- [Step 5: Run the DSBulk load command](https://docs.aws.amazon.com/keyspaces/latest/devguide/dsbulk-upload-run.html): Learn how to run the dsbulk tool to migrate data to Amazon Keyspaces.


## [Accessing Amazon Keyspaces](https://docs.aws.amazon.com/keyspaces/latest/devguide/accessing.html)

### [Using the console](https://docs.aws.amazon.com/keyspaces/latest/devguide/console_keyspaces.html)

Use the console to access Amazon Keyspaces to perform CRUD operations, run queries, and administer your database.

- [CloudShell console integration](https://docs.aws.amazon.com/keyspaces/latest/devguide/console_cloudshell_integration.html): AWS CloudShell provides a streamlined way to connect to Amazon Keyspaces directly from the console.
- [Using AWS CloudShell](https://docs.aws.amazon.com/keyspaces/latest/devguide/using-aws-with-cloudshell.html): Learn about how you can use AWS CloudShell to work with Amazon Keyspaces.

### [Create programmatic access credentials](https://docs.aws.amazon.com/keyspaces/latest/devguide/programmatic.credentials.html)

Learn how to create credentials to programmatically connect to Amazon Keyspaces.

- [Create service-specific credentials](https://docs.aws.amazon.com/keyspaces/latest/devguide/programmatic.credentials.ssc.html): Service-specific credentials are similar to the traditional username and password that Cassandra uses for authentication and access management.

### [Create IAM credentials for AWS authentication](https://docs.aws.amazon.com/keyspaces/latest/devguide/access.credentials.html)

Learn how to create an IAM user or role and create credentials to connect to Amazon Keyspaces.

- [Required credentials for AWS authentication](https://docs.aws.amazon.com/keyspaces/latest/devguide/SigV4_credentials.html): Learn about the IAM credentials that are required for a principal to connect to Amazon Keyspaces.
- [Create temporary credentials to connect to Amazon Keyspaces](https://docs.aws.amazon.com/keyspaces/latest/devguide/temporary.credentials.IAM.html): Learn how to connect to Amazon Keyspaces using an IAM role and temporary credentials.
- [Create an IAM user for programmatic access](https://docs.aws.amazon.com/keyspaces/latest/devguide/access.credentials.IAM.html): Learn how to create an IAM user for programmatic access to Amazon Keyspaces with AWS credentials.
- [Create new access keys](https://docs.aws.amazon.com/keyspaces/latest/devguide/create.keypair.html): Learn how to create access keys for an IAM user or role to connect to Amazon Keyspaces with AWS credentials programmatically.
- [Manage access keys](https://docs.aws.amazon.com/keyspaces/latest/devguide/aws.credentials.manage.html): Learn how to store IAM access keys for programmatic access to Amazon Keyspaces.

### [Service endpoints](https://docs.aws.amazon.com/keyspaces/latest/devguide/programmatic.endpoints.html)

Service endpoints and AWS Regions available for Amazon Keyspaces

- [Connecting to dual-stack endpoints](https://docs.aws.amazon.com/keyspaces/latest/devguide/dualstack_endpoints.html): Learn how to connect to dual-stack endpoints in Amazon Keyspaces.
- [IPv6 support in Amazon Keyspaces](https://docs.aws.amazon.com/keyspaces/latest/devguide/ipv6-support.html): Computers use IPv4 and IPv6 to communicate.
- [Using cqlsh](https://docs.aws.amazon.com/keyspaces/latest/devguide/programmatic.cqlsh.html): Learn how to install the cqlsh-expansion to use a customized version of cqlsh to connect programmatically to Amazon Keyspaces.
- [Using the AWS CLI](https://docs.aws.amazon.com/keyspaces/latest/devguide/access.cli.html): Learn how to use the AWS CLI to access Amazon Keyspaces to perform DDL operations.
- [Using the API](https://docs.aws.amazon.com/keyspaces/latest/devguide/access.api.html): Learn how to use the API to connect to Amazon Keyspaces to perform data definition language (DDL) operations.

### [Using a Cassandra client driver](https://docs.aws.amazon.com/keyspaces/latest/devguide/programmatic.drivers.html)

Learn how to connect to Amazon Keyspaces using Cassandra client drivers.

- [Using a Cassandra Java client driver](https://docs.aws.amazon.com/keyspaces/latest/devguide/using_java_driver.html): Learn how to connect to Amazon Keyspaces by using Java Cassandra client drivers.
- [Using a Cassandra Python client driver](https://docs.aws.amazon.com/keyspaces/latest/devguide/using_python_driver.html): Learn how to connect to Amazon Keyspaces using a Python Cassandra client driver.
- [Using a Cassandra Node.js client driver](https://docs.aws.amazon.com/keyspaces/latest/devguide/using_nodejs_driver.html): Learn how to connect to Amazon Keyspaces by using a Node.js Cassandra client driver.
- [Using a Cassandra .NET Core client driver](https://docs.aws.amazon.com/keyspaces/latest/devguide/using_dotnetcore_driver.html): Learn how to connect to Amazon Keyspaces by using a .NET Core Cassandra client driver and C#.
- [Using a Cassandra Go client driver](https://docs.aws.amazon.com/keyspaces/latest/devguide/using_go_driver.html): Learn how to connect to Amazon Keyspaces by using a Go Cassandra client driver.
- [Using a Cassandra Perl client driver](https://docs.aws.amazon.com/keyspaces/latest/devguide/using_perl_driver.html): Learn how to connect to Amazon Keyspaces by using a Perl Cassandra client driver.

### [Configure cross-account access](https://docs.aws.amazon.com/keyspaces/latest/devguide/access.cross-account.html)

Learn how to implement cross-account access for Amazon Keyspaces with VPC endpoints.

- [Configure cross-account access in a shared VPC](https://docs.aws.amazon.com/keyspaces/latest/devguide/access.cross-account.sharedVPC.html): Learn how to implement cross-account access with interface VPC endpoints in a shared VPC in Amazon Keyspaces.
- [Configure cross-account access without a shared VPC](https://docs.aws.amazon.com/keyspaces/latest/devguide/access.cross-account.noVPC.setup.html): Learn how to configure cross-account access without shared VPC in Amazon Keyspaces.


## [Getting started](https://docs.aws.amazon.com/keyspaces/latest/devguide/getting-started.html)

- [Prerequisites](https://docs.aws.amazon.com/keyspaces/latest/devguide/getting-started.before-you-begin.html): Learn about the prerequisites you need before beginning the getting started tutorial for Amazon Keyspaces.
- [Create a keyspace](https://docs.aws.amazon.com/keyspaces/latest/devguide/getting-started.keyspaces.html): Learn how to create a keyspace using the console, CQL, or the AWS CLI in Amazon Keyspaces.
- [Check keyspace creation status](https://docs.aws.amazon.com/keyspaces/latest/devguide/keyspaces-create.html): Learn how to check the asynchronous keyspace creation status in Amazon Keyspaces.
- [Create a table](https://docs.aws.amazon.com/keyspaces/latest/devguide/getting-started.tables.html): Learn how to create a table using the console, CQL, or the AWS CLI in Amazon Keyspaces.
- [Check table creation status](https://docs.aws.amazon.com/keyspaces/latest/devguide/tables-create.html): Learn how to monitor the asynchronous table creation status in Amazon Keyspaces.

### [CRUD operations](https://docs.aws.amazon.com/keyspaces/latest/devguide/getting-started.dml.html)

Learn how to perform insert, read, update, and delete (CRUD) operations on data using CQL statements in Amazon Keyspaces.

- [Create](https://docs.aws.amazon.com/keyspaces/latest/devguide/getting-started.dml.create.html): Learn how to add data to a table using the CQL INSERT statement, or how to upload data from a CSV file with cqlsh in Amazon Keyspaces.
- [Read](https://docs.aws.amazon.com/keyspaces/latest/devguide/getting-started.dml.read.html): Learn how to read data from a table using the CQL SELECT statement in Amazon Keyspaces.
- [Update](https://docs.aws.amazon.com/keyspaces/latest/devguide/getting-started.dml.update.html): Learn how to update data values in a table using the CQL UPDATE statement in Amazon Keyspaces.
- [Delete](https://docs.aws.amazon.com/keyspaces/latest/devguide/getting-started.dml.delete.html): Learn how to delete cells and rows from a table using the CQL DELETE statement in Amazon Keyspaces.
- [Delete a table](https://docs.aws.amazon.com/keyspaces/latest/devguide/getting-started.clean-up.table.html): Learn how to delete a table using the console, CQL, and the AWS CLI in Amazon Keyspaces.
- [Delete a keyspace](https://docs.aws.amazon.com/keyspaces/latest/devguide/getting-started.clean-up.keyspace.html): Learn how to delete a keyspace using the console, CQL, and the AWS CLI in Amazon Keyspaces.


## [Tutorials and solutions](https://docs.aws.amazon.com/keyspaces/latest/devguide/tutorials.html)

### [Connecting with VPC endpoints](https://docs.aws.amazon.com/keyspaces/latest/devguide/vpc-endpoints-tutorial.html)

Learn how to connect to Amazon Keyspaces using a VPC endpoint in this step-by-step tutorial.

- [Prerequisites](https://docs.aws.amazon.com/keyspaces/latest/devguide/vpc-endpoints-tutorial.before-you-begin.html): Learn about the prerequisites that you need before beginning the VPC endpoints tutorial for Amazon Keyspaces.
- [Step 1: Launch an Amazon EC2 instance](https://docs.aws.amazon.com/keyspaces/latest/devguide/vpc-endpoints-tutorial.launch-ec2-instance.html): Learn how to create an Amazon EC2 instance to connect to Amazon Keyspaces using a VPC endpoint in this step-by-step tutorial.
- [Step 2: Configure your Amazon EC2 instance](https://docs.aws.amazon.com/keyspaces/latest/devguide/vpc-endpoints-tutorial.configure-ec2-instance.html): Learn how to configure an Amazon EC2 instance to connect to Amazon Keyspaces using a VPC endpoint in this step-by-step tutorial.
- [Step 3: Create a VPC endpoint for Amazon Keyspaces](https://docs.aws.amazon.com/keyspaces/latest/devguide/vpc-endpoints-tutorial.create-endpoint.html): Learn how to create a VPC endpoint to connect to Amazon Keyspaces in this step-by-step tutorial.
- [Step 4: Configure permissions for the VPC endpoint connection](https://docs.aws.amazon.com/keyspaces/latest/devguide/vpc-endpoints-tutorial.permissions.html): Learn how to configure the permissions to allow your VPC to connect to Amazon Keyspaces using a VPC endpoint in this step-by-step tutorial.
- [Step 5: Configure monitoring](https://docs.aws.amazon.com/keyspaces/latest/devguide/vpc-endpoints-tutorial.monitoring.html): Learn how to set up monitoring for connections to Amazon Keyspaces that use a VPC endpoint in this step-by-step tutorial.
- [Step 6: (Optional) Best practices for connections](https://docs.aws.amazon.com/keyspaces/latest/devguide/vpc-endpoints-tutorial.connections.html): Learn about best practices for configuring the connection pool size for connections to Amazon Keyspaces that use a VPC endpoint in this step-by-step tutorial.
- [Step 7: (Optional) Clean up](https://docs.aws.amazon.com/keyspaces/latest/devguide/vpc-endpoints-tutorial.clean-up.html): Learn how to clean up the resources that you created in this step-by-step tutorial.

### [Integrating with Apache Spark](https://docs.aws.amazon.com/keyspaces/latest/devguide/spark-integrating.html)

Learn about integrating Amazon Keyspaces with Apache Spark to perform data analytics or migration.

- [Prerequisites](https://docs.aws.amazon.com/keyspaces/latest/devguide/spark-tutorial-prerequisites.html): Describes what you need to install before you can connect to Amazon Keyspaces with the Spark Cassandra Connector.
- [Step 1: Configure Amazon Keyspaces](https://docs.aws.amazon.com/keyspaces/latest/devguide/spark-tutorial-step1.html): Configure Amazon Keyspaces for integration with the Apache Cassandra Spark Connector.
- [Step 2: Configure the Apache Cassandra Spark Connector](https://docs.aws.amazon.com/keyspaces/latest/devguide/spark-tutorial-step2.html): Describes best practices to configure the Spark Cassandra Connector for Amazon Keyspaces.
- [Step 3: Create the app config file](https://docs.aws.amazon.com/keyspaces/latest/devguide/spark-tutorial-step3.html): How to create the app config file that is needed to connect to Amazon Keyspaces with the Spark Cassandra Connector.
- [Step 4: Prepare the source data and the target table](https://docs.aws.amazon.com/keyspaces/latest/devguide/spark-tutorial-step4.html)
- [Step 5: Write and read Amazon Keyspaces data](https://docs.aws.amazon.com/keyspaces/latest/devguide/spark-tutorial-step5.html): In this step, you start by loading the data from the sample file into a DataFrame with the Spark Cassandra Connector.
- [Troubleshooting](https://docs.aws.amazon.com/keyspaces/latest/devguide/spark-tutorial-step6.html): Learn how to troubleshoot common errors when using the Spark Cassandra Connector with Amazon Keyspaces.

### [Connecting from Amazon EKS](https://docs.aws.amazon.com/keyspaces/latest/devguide/EKS-tutorial.html)

Learn in this step-by-step tutorial how to connect to Amazon Keyspaces using SigV4 authentication from a containerized application running on Amazon EKS.

- [Prerequisites](https://docs.aws.amazon.com/keyspaces/latest/devguide/EKS-tutorial-prerequisites.html): Learn which AWS resources you need to create before you can start with this tutorial.
- [Step 1: Configure the Amazon EKS cluster](https://docs.aws.amazon.com/keyspaces/latest/devguide/EKS-tutorial-step1.html): Learn how to configure the Amazon EKS cluster to be able to allow a containerized application to connect to Amazon Keyspaces.
- [Step 2: Configure the application](https://docs.aws.amazon.com/keyspaces/latest/devguide/EKS-tutorial-step2.html): Describes how to configure the application for the connection to Amazon Keyspaces using the SigV4 plugin.
- [Step 3: Create application image](https://docs.aws.amazon.com/keyspaces/latest/devguide/EKS-tutorial-step3.html): Build the example application, create a Docker image, and upload the file to your Amazon ECR repository.
- [Step 4: Deploy the application to Amazon EKS](https://docs.aws.amazon.com/keyspaces/latest/devguide/EKS-tutorial-step4.html): How to deploy an application that connects to Amazon Keyspaces to Amazon EKS and write data to an Amazon Keyspaces table.
- [Step 5: (Optional) Cleanup](https://docs.aws.amazon.com/keyspaces/latest/devguide/EKS-tutorial-step5.html): Learn how to remove all the resources created in this tutorial.

### [Exporting data to Amazon S3](https://docs.aws.amazon.com/keyspaces/latest/devguide/S3-tutorial.html)

Learn in this step-by-step tutorial how to export an Amazon Keyspaces table to Amazon Simple Storage Service using AWS Glue.

- [Prerequisites](https://docs.aws.amazon.com/keyspaces/latest/devguide/S3-tutorial-prerequisites.html): Learn which AWS resources you need to create before you can start with this tutorial.
- [Step 1: Create the Amazon S3 bucket, download tools, and configure the environment](https://docs.aws.amazon.com/keyspaces/latest/devguide/S3-tutorial-step1.html): Learn how to run a script that downloads all the required tools and creates the AWS resources and configuration files needed to export data to an Amazon S3 bucket.
- [Step 2: Configure the AWS Glue job](https://docs.aws.amazon.com/keyspaces/latest/devguide/S3-tutorial-step2.html): Describes how to configure the AWS Glue job to export an Amazon Keyspaces table to Amazon S3.
- [Step 3: Run the export AWS Glue job from the AWS CLI](https://docs.aws.amazon.com/keyspaces/latest/devguide/S3-tutorial-step3.html): Learn how to run a AWS Glue job that exports an Amazon Keyspaces table to Amazon S3 from the AWS CLI.
- [Step 4: (Optional) Schedule the export job](https://docs.aws.amazon.com/keyspaces/latest/devguide/S3-tutorial-step4.html): Learn how to create a trigger that schedules the AWS Glue export job of the Amazon Keyspaces table to Amazon S3.
- [Step 5: (Optional) Cleanup](https://docs.aws.amazon.com/keyspaces/latest/devguide/S3-tutorial-step5.html): Learn how to remove all the resources created in this tutorial.


## [Managing serverless resources](https://docs.aws.amazon.com/keyspaces/latest/devguide/serverless_resource_management.html)

- [Estimate row size](https://docs.aws.amazon.com/keyspaces/latest/devguide/calculating-row-size.html): Learn how to estimate the row size in Amazon Keyspaces to use the total encoded row size when calculating your bill, quota use, and when calculating provisioned throughput capacity requirements for tables.

### [Estimate capacity consumption](https://docs.aws.amazon.com/keyspaces/latest/devguide/capacity-examples.html)

Learn how to estimate read and write capacity consumption in Amazon Keyspaces.

- [Estimate the capacity consumption of range queries](https://docs.aws.amazon.com/keyspaces/latest/devguide/range_queries.html): Learn how to estimate read consumption of range queries in Amazon Keyspaces.
- [Estimate the read capacity consumption of limit queries](https://docs.aws.amazon.com/keyspaces/latest/devguide/limit_queries.html): Learn how to estimate read capacity consumption of limit queries in Amazon Keyspaces.
- [Estimate the read capacity consumption of table scans](https://docs.aws.amazon.com/keyspaces/latest/devguide/table_scans.html): Learn how to estimate read capacity consumption of table scans in Amazon Keyspaces.
- [Estimate capacity consumption of LWT](https://docs.aws.amazon.com/keyspaces/latest/devguide/lightweight_transactions.html): Learn how to estimate write capacity consumption of lightweight transactions in Amazon Keyspaces.

### [Estimate capacity consumption of static columns](https://docs.aws.amazon.com/keyspaces/latest/devguide/static-columns.html)

Learn more about static columns in Amazon Keyspaces and how to estimate your bill, calculate throughput capacity requirements, and estimate the size of encoded data when you're writing to tables with static columns.

- [Calculate static column size per logical partition](https://docs.aws.amazon.com/keyspaces/latest/devguide/static-columns-estimate.html): Learn how to estimate the logical partition size in Amazon Keyspaces for static columns to use when you're calculating your bill and quota use.
- [Estimate capacity for read/write operations on static data](https://docs.aws.amazon.com/keyspaces/latest/devguide/static-columns-metering.html): Learn how to estimate read capacity units (RCUs) and write capacity units (WCUs) for Amazon Keyspaces tables with static columns to estimate your bill, for quota use, and when you're calculating provisioned throughput capacity requirements.
- [Estimate capacity for a multi-Region table](https://docs.aws.amazon.com/keyspaces/latest/devguide/tables-multi-region-capacity.html): Learn how to provision capacity for multi-Region tables in Amazon Keyspaces, and how to estimate write throughput capacity needs for all replicas.
- [Estimate capacity consumption with CloudWatch](https://docs.aws.amazon.com/keyspaces/latest/devguide/estimate_consumption_cw.html): Learn how to monitor and estimate read and write capacity consumption in Amazon Keyspaces with CloudWatch.

### [Configure read/write capacity modes](https://docs.aws.amazon.com/keyspaces/latest/devguide/ReadWriteCapacityMode.html)

Learn about how to configure on-demand and provisioned capacity modes, and which mode is best for a given workload's reads and writes when creating or updating a table in Amazon Keyspaces.

- [Configure on-demand capacity mode](https://docs.aws.amazon.com/keyspaces/latest/devguide/ReadWriteCapacityMode.OnDemand.html): Learn how to configure on-demand capacity mode in Amazon Keyspaces.
- [Configure provisioned capacity mode](https://docs.aws.amazon.com/keyspaces/latest/devguide/ReadWriteCapacityMode.Provisioned.html): Learn how to configure provisioned throughput capacity mode in Amazon Keyspaces.
- [View the capacity mode of a table](https://docs.aws.amazon.com/keyspaces/latest/devguide/ReadWriteCapacityMode.ProvisionedThroughput.ManagingCapacity.html): Learn how to view the capacity mode of a table in Amazon Keyspaces.
- [Change capacity mode](https://docs.aws.amazon.com/keyspaces/latest/devguide/ReadWriteCapacityMode.SwitchReadWriteCapacityMode.html): Learn what to consider when changing the capacity mode of a table, and how often you can change capacity modes in Amazon Keyspaces.

### [Configure pre-warming](https://docs.aws.amazon.com/keyspaces/latest/devguide/warm-throughput.html)

Learn how to configure warm-throughput to pre-warm Amazon Keyspaces tables for optimal performance during high-throughput operations like data migrations or traffic spikes.

- [Create a table with higher warm throughput](https://docs.aws.amazon.com/keyspaces/latest/devguide/create-table-warm-throughput.html): Learn how to create a new table with warm throughput settings using the console, CQL, or the AWS CLI to prepare for increased workloads.
- [Increase your table's warm throughput](https://docs.aws.amazon.com/keyspaces/latest/devguide/update-warm-throughput.html): Learn how to modify warm throughput settings for existing tables using the console, CQL, or the AWS CLI to prepare for increased workloads.
- [View your table's warm throughput](https://docs.aws.amazon.com/keyspaces/latest/devguide/view-warm-throughput.html): Learn how to monitor warm throughput settings for existing tables using the console, CQL, or the AWS CLI to prepare for increased workloads.
- [Monitor pre-warming with CloudWatch](https://docs.aws.amazon.com/keyspaces/latest/devguide/monitor-prewarming-cloudwatch.html): Learn how to use existing Amazon Keyspaces CloudWatch metrics to monitor the performance of pre-warmed tables and validate your pre-warming configuration.

### [Manage throughput capacity with auto scaling](https://docs.aws.amazon.com/keyspaces/latest/devguide/autoscaling.html)

Set your scaling policy and let Amazon Keyspaces scale capacity up and down automatically based on your application's actual needs.

### [Configure and update auto scaling policies](https://docs.aws.amazon.com/keyspaces/latest/devguide/autoscaling.configure.html)

Learn how to use the console, CQL, or the AWS CLI to configure and update automatic scaling policies for new and existing tables in Amazon Keyspaces.

- [Configure permissions](https://docs.aws.amazon.com/keyspaces/latest/devguide/autoscaling.permissions.html): Learn how to configure the required IAM permissions to configure automatic scaling in Amazon Keyspaces.
- [Create a new table with automatic scaling](https://docs.aws.amazon.com/keyspaces/latest/devguide/autoscaling.createTable.html): Learn how to create a new table in provisioned capacity mode with automatic scaling in Amazon Keyspaces.
- [Configure automatic scaling on an existing table](https://docs.aws.amazon.com/keyspaces/latest/devguide/autoscaling.configureTable.html): Learn how to configure automatic scaling for a table in provisioned capacity mode in Amazon Keyspaces.
- [View your table's Amazon Keyspaces auto scaling configuration](https://docs.aws.amazon.com/keyspaces/latest/devguide/autoscaling.viewPolicy.html): Learn how to view a table's automatic scaling configuration in Amazon Keyspaces.
- [Turn off Amazon Keyspaces auto scaling for a table](https://docs.aws.amazon.com/keyspaces/latest/devguide/autoscaling.turnoff.html): Learn how to turn off automatic scaling for a table in Amazon Keyspaces.
- [View auto scaling activity](https://docs.aws.amazon.com/keyspaces/latest/devguide/autoscaling.activity.html): Learn how to set up monitoring for the auto scaling activity of a Amazon Keyspaces table using the CloudWatch console.
- [Use burst capacity](https://docs.aws.amazon.com/keyspaces/latest/devguide/throughput-bursting.html): Learn how to use throughput burst capacity effectively in Amazon Keyspaces databases.


## [Working with Amazon Keyspaces features](https://docs.aws.amazon.com/keyspaces/latest/devguide/working-with-overview.html)

- [System keyspaces](https://docs.aws.amazon.com/keyspaces/latest/devguide/working-with-keyspaces.html): Learn about how to work with system keyspaces in Amazon Keyspaces.

### [User-defined types (UDTs)](https://docs.aws.amazon.com/keyspaces/latest/devguide/udts.html)

Learn how to use user-defined types (UDTs) to organize your data in a more efficient way in Amazon Keyspaces.

- [Configure permissions](https://docs.aws.amazon.com/keyspaces/latest/devguide/configure-udt-permissions.html): Learn how to configure permissions that are required to create, delete, and list user-defined types (UDTs) in Amazon Keyspaces.
- [Create a UDT](https://docs.aws.amazon.com/keyspaces/latest/devguide/keyspaces-create-udt.html): Learn how to create a user-defined type (UDT) in Amazon Keyspaces.
- [View UDTs](https://docs.aws.amazon.com/keyspaces/latest/devguide/keyspaces-view-udt.html): Learn how to view user-defined types (UDTs) in Amazon Keyspaces.
- [Delete a UDT](https://docs.aws.amazon.com/keyspaces/latest/devguide/keyspaces-delete-udt.html): Learn how to delete a user-defined type (UDT) in Amazon Keyspaces.

### [Working with CQL queries](https://docs.aws.amazon.com/keyspaces/latest/devguide/working-with-queries.html)

Learn about available CQL statements for data manipulation and how to work with queries in Amazon Keyspaces.

- [Use IN SELECT](https://docs.aws.amazon.com/keyspaces/latest/devguide/in.select.html): Learn how the IN operator can be used with the SELECT statement in Amazon Keyspaces.
- [Use batch statements](https://docs.aws.amazon.com/keyspaces/latest/devguide/batchStatements.html): Learn how to use logged and unlogged batch statements in Amazon Keyspaces.
- [Order results](https://docs.aws.amazon.com/keyspaces/latest/devguide/ordering-results.html): Learn how to order results when querying tables in Amazon Keyspaces.
- [Paginate results](https://docs.aws.amazon.com/keyspaces/latest/devguide/paginating-results.html): Learn how pagination of results works in Amazon Keyspaces.

### [Working with CDC streams](https://docs.aws.amazon.com/keyspaces/latest/devguide/cdc.html)

Learn about change data capture (CDC) streams in Amazon Keyspaces.

- [How CDC streams work](https://docs.aws.amazon.com/keyspaces/latest/devguide/cdc_how-it-works.html): Learn how change data capture (CDC) streams work in Amazon Keyspaces.

### [Use CDC streams](https://docs.aws.amazon.com/keyspaces/latest/devguide/cdc_how-to-use.html)

Learn how to use change data capture (CDC) streams in Amazon Keyspaces.

- [Configure permissions](https://docs.aws.amazon.com/keyspaces/latest/devguide/configure-cdc-permissions.html): Learn how to configure permissions that are required to enable, disable, and list CDC streams in Amazon Keyspaces.
- [Access CDC stream endpoints](https://docs.aws.amazon.com/keyspaces/latest/devguide/CDC_access-endpoints.html): Learn how to use endpoints for change data capture (CDC) streams in Amazon Keyspaces.
- [Enable a CDC stream for a new table](https://docs.aws.amazon.com/keyspaces/latest/devguide/keyspaces-enable-cdc-new-table.html): Learn how to enable a CDC stream for a new table in Amazon Keyspaces.
- [Enable a CDC stream for an existing table](https://docs.aws.amazon.com/keyspaces/latest/devguide/keyspaces-enable-cdc-alter-table.html): Learn how to enable a CDC stream for an existing table in Amazon Keyspaces.
- [Disable a CDC stream](https://docs.aws.amazon.com/keyspaces/latest/devguide/keyspaces-delete-cdc.html): Learn how to disable a CDC stream in Amazon Keyspaces.
- [View CDC streams](https://docs.aws.amazon.com/keyspaces/latest/devguide/keyspaces-view-cdc.html): Learn how to view CDC streams in Amazon Keyspaces.
- [Access CDC streams](https://docs.aws.amazon.com/keyspaces/latest/devguide/keyspaces-records-cdc.html): Learn how to access records in CDC streams in Amazon Keyspaces.

### [Use KCL for processing streams](https://docs.aws.amazon.com/keyspaces/latest/devguide/cdc_how-to-use-kcl.html)

Learn how to use the Kinesis Client Library (KCL) to process Amazon Keyspaces change data capture (CDC) streams.

- [Implement a KCL consumer](https://docs.aws.amazon.com/keyspaces/latest/devguide/cdc-kcl-implementation.html): Learn how to implement a KCL consumer application to process Amazon Keyspaces CDC streams.

### [Working with partitioners](https://docs.aws.amazon.com/keyspaces/latest/devguide/working-with-partitioners.html)

Learn about available partitioners and how they work in Amazon Keyspaces.

- [Change the partitioner](https://docs.aws.amazon.com/keyspaces/latest/devguide/working-with-partitioners-change.html): Learn how to change the partitioner in Amazon Keyspaces.

### [Client-side timestamps](https://docs.aws.amazon.com/keyspaces/latest/devguide/client-side-timestamps.html)

Learn how to use client-side timestamps to add cell-level timestamp support and help control the order in which data from distributed applications is written to tables in Amazon Keyspaces.

- [Create table with client-side timestamps](https://docs.aws.amazon.com/keyspaces/latest/devguide/client-side-timestamps-create-new-table.html): Learn how to turn on client-side timestamps settings using the console, CQL, and the CLI in Amazon Keyspaces.
- [Configure client-side timestamps](https://docs.aws.amazon.com/keyspaces/latest/devguide/client-side-timestamps-existing-table.html): Learn how to turn on client-side timestamps settings for existing tables using the console, CQL, and the CLI in Amazon Keyspaces.
- [Use client-side timestamps in queries](https://docs.aws.amazon.com/keyspaces/latest/devguide/client-side-timestamps-how-to-queries.html): Learn how to work with client-side timestamps in CQL Data Manipulation Language (DML) statements in Amazon Keyspaces.

### [Multi-Region replication](https://docs.aws.amazon.com/keyspaces/latest/devguide/multiRegion-replication.html)

Use multi-Region replication in Amazon Keyspaces to replicate your tables across different AWS Regions of your choice.

- [How it works](https://docs.aws.amazon.com/keyspaces/latest/devguide/multiRegion-replication_how-it-works.html): Use multi-Region replication in Amazon Keyspaces to replicate your tables across the AWS Regions of your choice.
- [Usage notes](https://docs.aws.amazon.com/keyspaces/latest/devguide/multiRegion-replication_usage-notes.html): Configuration guidance and usage notes for Amazon Keyspaces multi-Region replication.

### [Configure multi-Region replication](https://docs.aws.amazon.com/keyspaces/latest/devguide/multiRegion-replication-configure.html)

Learn how to configure and use multi-Region replication to replicate your tables across different AWS Regions of your choice in Amazon Keyspaces.

- [Configure IAM permissions for create keyspace and table](https://docs.aws.amazon.com/keyspaces/latest/devguide/howitworks_replication_permissions.html): Learn how to configure the required IAM permissions to create keyspaces and tables with multi-Region replication in Amazon Keyspaces.
- [Configure IAM permissions for add Region](https://docs.aws.amazon.com/keyspaces/latest/devguide/howitworks_replication_permissions_addReplica.html): Learn how to configure the minimum IAM permissions required for a principal to add a Region to a keyspace in Amazon Keyspaces.
- [Create a multi-Region keyspace](https://docs.aws.amazon.com/keyspaces/latest/devguide/keyspaces-mrr-create.html): Learn how to create a multi-Region keyspace in Amazon Keyspaces.
- [Add a Region to a keyspace](https://docs.aws.amazon.com/keyspaces/latest/devguide/keyspaces-multi-region-add-replica.html): Learn how to add a new Region to single or multi-Region keyspaces in Amazon Keyspaces.
- [Check replication progress](https://docs.aws.amazon.com/keyspaces/latest/devguide/keyspaces-multi-region-replica-status.html): Learn how to check the progress of table creation when adding a new Region to a keyspace in Amazon Keyspaces.
- [Create a multi-Region table with default settings](https://docs.aws.amazon.com/keyspaces/latest/devguide/tables-mrr-create-default.html): Learn how to create a multi-Region table in on-demand capacity mode with default settings in Amazon Keyspaces.
- [Create a multi-Region table in provisioned mode](https://docs.aws.amazon.com/keyspaces/latest/devguide/tables-mrr-create-provisioned.html): Learn how to create a multi-Region table with provisioned capacity mode and automatic scaling in Amazon Keyspaces.
- [Update provisioned capacity and auto scaling settings for a multi-Region table](https://docs.aws.amazon.com/keyspaces/latest/devguide/tables-mrr-autoscaling.html): Learn how to update provisioned capacity mode and automatic scaling settings for multi-Region tables in Amazon Keyspaces.
- [View provisioned capacity and auto scaling settings for a multi-Region table](https://docs.aws.amazon.com/keyspaces/latest/devguide/tables-mrr-view.html): Learn how to view the provisioned capacity mode and automatic scaling settings of multi-Region tables in Amazon Keyspaces.
- [Turn off auto scaling](https://docs.aws.amazon.com/keyspaces/latest/devguide/tables-mrr-autoscaling-off.html): Learn how to turn off auto scaling for multi-Region tables in Amazon Keyspaces.
- [Set provisioned capacity manually](https://docs.aws.amazon.com/keyspaces/latest/devguide/tables-mrr-capacity-manually.html): Learn how to set the provisioned capacity for multi-Region tables manually in case you had to turn of automatic scaling in Amazon Keyspaces.

### [Backup and restore with point-in-time recovery](https://docs.aws.amazon.com/keyspaces/latest/devguide/PointInTimeRecovery.html)

Learn how to use automatic backup and restore functionality to protect your Amazon Keyspaces tables from accidental write or delete operations with point-in-time recovery (PITR).

- [How it works](https://docs.aws.amazon.com/keyspaces/latest/devguide/PointInTimeRecovery_HowItWorks.html): Learn how point-in-time recovery works in Amazon Keyspaces, the backup and restore options available, how to restore table settings, and how to estimate restore time.

### [Use point-in-time recovery](https://docs.aws.amazon.com/keyspaces/latest/devguide/PointInTimeRecovery_Tutorial.html)

Learn how to work with Point-in-Time Restore (PITR) in Amazon Keyspaces for example how to configure IAM permissions, how to restore a table to a point in time, or how to restore a PITR enabled deleted table.

- [Configure IAM permissions for restore](https://docs.aws.amazon.com/keyspaces/latest/devguide/howitworks_restore_permissions.html): Learn how to configure the required IAM permissions to restore tables with Point-in-Time Restore (PITR) in Amazon Keyspaces.
- [Configure PITR](https://docs.aws.amazon.com/keyspaces/latest/devguide/configure_PITR.html): Learn how to configure Point-in-Time Restore (PITR) in Amazon Keyspaces by using the console, CQL, or the AWS CLI.
- [Turn off PITR](https://docs.aws.amazon.com/keyspaces/latest/devguide/disable_PITR.html): Learn how to disable Point-in-Time Restore (PITR) in Amazon Keyspaces by using the console, CQL, or the AWS CLI.
- [Restore a table to a point in time](https://docs.aws.amazon.com/keyspaces/latest/devguide/restoretabletopointintime.html): Learn how to restore a table from backup to a specified point in time with Point-in-Time Restore (PITR) by using the console, CQL, or the AWS CLI in Amazon Keyspaces.
- [Restore a deleted table](https://docs.aws.amazon.com/keyspaces/latest/devguide/restoredeleted.html): Learn how to restore a deleted table from backup with Point-in-Time Restore (PITR) in Amazon Keyspaces.

### [Expire data with Time to Live](https://docs.aws.amazon.com/keyspaces/latest/devguide/TTL.html)

Use Time to Live (TTL) in Amazon Keyspaces to automatically expire data from tables, rows, and cells.

- [Create table with default TTL value](https://docs.aws.amazon.com/keyspaces/latest/devguide/TTL-how-to-create-table.html): In Amazon Keyspaces, you can set a default TTL value for all rows in a table when the table is created.
- [Update table default TTL value](https://docs.aws.amazon.com/keyspaces/latest/devguide/TTL-how-to-update-default.html): You can update an existing table with a new default TTL value.
- [Create table with custom TTL](https://docs.aws.amazon.com/keyspaces/latest/devguide/TTL-how-to-enable-custom-new.html): To create a new table with Time to Live custom settings that can be applied to rows and columns without enabling TTL default settings for the entire table, you can use the following commands.
- [Update table custom TTL](https://docs.aws.amazon.com/keyspaces/latest/devguide/TTL-how-to-enable-custom-alter.html): To enable Time to Live custom settings for a table so that TTL values can be applied to individual rows and columns without setting a TTL default value for the entire table, you can use the following commands.
- [Use INSERT to set custom TTL for new rows](https://docs.aws.amazon.com/keyspaces/latest/devguide/TTL-how-to-insert-cql.html)
- [Use UPDATE to set custom TTL for rows and columns](https://docs.aws.amazon.com/keyspaces/latest/devguide/TTL-how-to-update-cql.html)
- [Working with AWS SDKs](https://docs.aws.amazon.com/keyspaces/latest/devguide/sdk-general-information-section.html): Provides links to AWS SDK developer guides and to code example folders (on GitHub) to help interested customers quickly find the information they need to start building applications.

### [Working with tags](https://docs.aws.amazon.com/keyspaces/latest/devguide/tagging-keyspaces.html)

Learn to use AWS tags to label and categorize resources in Amazon Keyspaces by purpose, owner, environment, or other criteria.

- [Tagging restrictions](https://docs.aws.amazon.com/keyspaces/latest/devguide/TaggingRestrictions.html): Learn about the restrictions that apply to tags used to label Amazon Keyspaces resources.

### [Tag keyspaces, tables, and streams](https://docs.aws.amazon.com/keyspaces/latest/devguide/Tagging.Operations.html)

Learn how to use the console, CQL, or the AWS CLI to manage tags in Amazon Keyspaces, for example how to add, list, edit, or delete tags for keyspaces, tables, and streams.

- [Create keyspace with tags](https://docs.aws.amazon.com/keyspaces/latest/devguide/Tagging.Operations.new.keyspace.html): Learn how to add tags when creating keyspaces using the console, CQL or the AWS CLI in Amazon Keyspaces.
- [Add tags to a keyspace](https://docs.aws.amazon.com/keyspaces/latest/devguide/Tagging.Operations.existing.keyspace.html): Learn how to add tags to keyspaces using the console, CQL or the AWS CLI in Amazon Keyspaces.
- [Delete tags from a keyspace](https://docs.aws.amazon.com/keyspaces/latest/devguide/Tagging.Operations.existing.keyspace.drop.html): Lear how to delete tags from keyspaces using the console, CQL or the AWS CLI in Amazon Keyspaces.
- [View keyspace tags](https://docs.aws.amazon.com/keyspaces/latest/devguide/Tagging.Operations.view.keyspace.html): Learn how to view the tags of keyspaces using the console, CQL or the AWS CLI in Amazon Keyspaces.
- [Create table with tags](https://docs.aws.amazon.com/keyspaces/latest/devguide/Tagging.Operations.new.table.html): Learn how to add tags to tables when creating a new table using the console, CQL or the AWS CLI in Amazon Keyspaces.
- [Add tags to a table](https://docs.aws.amazon.com/keyspaces/latest/devguide/Tagging.Operations.existing.table.html): Learn how to add tags to a table using CQL or the AWS CLI in Amazon Keyspaces.
- [Delete tags from a table](https://docs.aws.amazon.com/keyspaces/latest/devguide/Tagging.Operations.existing.table.drop.html): Learn how to delete tags from a table in Amazon Keyspaces.
- [View table tags](https://docs.aws.amazon.com/keyspaces/latest/devguide/Tagging.Operations.view.table.html): Learn how to view tags of tables using the console, CQL, or the AWS CLI in Amazon Keyspaces.
- [Create stream with tags with new table](https://docs.aws.amazon.com/keyspaces/latest/devguide/Tagging.Operations.new.table.stream.html): Learn how to add tags to streams when creating a new table using CQL or the AWS CLI in Amazon Keyspaces.
- [Create new stream with tags for existing table](https://docs.aws.amazon.com/keyspaces/latest/devguide/Tagging.Operations.new.stream.html): Learn how to add tags to new streams for an existing table using CQL or the AWS CLI in Amazon Keyspaces.
- [Add new tags to a stream](https://docs.aws.amazon.com/keyspaces/latest/devguide/Tagging.Operations.existing.stream.html): Learn how to add new tags to an existing stream using the CQL or the AWS CLI in Amazon Keyspaces.
- [Delete tags from a stream](https://docs.aws.amazon.com/keyspaces/latest/devguide/Tagging.Operations.existing.stream.drop.html): Learn how to delete tags from a stream in Amazon Keyspaces.
- [View stream tags](https://docs.aws.amazon.com/keyspaces/latest/devguide/Tagging.Operations.view.stream.html): Learn how to view tags of streams using CQL or the AWS CLI in Amazon Keyspaces.
- [Create cost allocation reports](https://docs.aws.amazon.com/keyspaces/latest/devguide/CostAllocationReports.html): Learn how to create cost allocation reports with tags in Amazon Keyspaces.
- [Create CloudFormation resources](https://docs.aws.amazon.com/keyspaces/latest/devguide/creating-resources-with-cloudformation.html): Learn how to create templates to provision and configure keyspaces and tables for Amazon Keyspaces using AWS CloudFormation.

### [NoSQL Workbench](https://docs.aws.amazon.com/keyspaces/latest/devguide/workbench.html)

Design, create, query, and manage tables using NoSQL Workbench for Amazon Keyspaces.

- [Download](https://docs.aws.amazon.com/keyspaces/latest/devguide/workbench.settingup.html): Follow these instructions to download and install NoSQL Workbench.
- [Getting started](https://docs.aws.amazon.com/keyspaces/latest/devguide/workbench.start.html): To get started with NoSQL Workbench, on the Database Catalog page in NoSQL Workbench, choose Amazon Keyspaces, and then choose Launch.
- [Visualize a data model](https://docs.aws.amazon.com/keyspaces/latest/devguide/workbench.vizualizer.html): Learn how to visualize data models with the data visualizer in NoSQL Workbench for Amazon Keyspaces.
- [Create a data model](https://docs.aws.amazon.com/keyspaces/latest/devguide/workbench.datamodel.new.html): Learn how to create data models for Amazon Keyspaces with the data modeler and visualizer functionality in NoSQL Workbench.
- [Edit a data model](https://docs.aws.amazon.com/keyspaces/latest/devguide/workbench.datamodel.edit.html): Learn how to edit a data model in Amazon Keyspaces using the data modeler and visualizer functionality in NoSQL Workbench.

### [Commit a data model](https://docs.aws.amazon.com/keyspaces/latest/devguide/workbench.commit.html)

Describes how to commit data models created in NoSQL Workbench to Amazon Keyspaces and Apache Cassandra.

- [Connect with service-specific credentials](https://docs.aws.amazon.com/keyspaces/latest/devguide/workbench.commit.ssc.html): How to use AWS service-specific credentials to commit the Amazon Keyspaces data model with NoSQL Workbench.
- [Connect with IAM credentials](https://docs.aws.amazon.com/keyspaces/latest/devguide/workbench.commit.iam.html): How to use AWS IAM credentials to commit the Amazon Keyspaces data model with NoSQL Workbench.
- [Use a saved connection](https://docs.aws.amazon.com/keyspaces/latest/devguide/workbench.commit.default.html): Commit the data model created with NoSQL Workbench to Amazon Keyspaces using a saved connection.
- [Apache Cassandra](https://docs.aws.amazon.com/keyspaces/latest/devguide/workbench.commit.cassandra.html): Commit the data model created with NoSQL Workbench to Apache Cassandra.
- [Sample data models](https://docs.aws.amazon.com/keyspaces/latest/devguide/workbench.SampleModels.html): Describes sample data models that are included in NoSQL Workbench
- [Release history](https://docs.aws.amazon.com/keyspaces/latest/devguide/WorkbenchDocumentHistory.html): Find the revision dates, related releases, and important changes to NoSQL Workbench.


## [Code examples](https://docs.aws.amazon.com/keyspaces/latest/devguide/service_code_examples.html)

### [Basics](https://docs.aws.amazon.com/keyspaces/latest/devguide/service_code_examples_basics.html)

The following code examples show how to use the basics of Amazon Keyspaces with AWS SDKs.

- [Hello Amazon Keyspaces](https://docs.aws.amazon.com/keyspaces/latest/devguide/example_keyspaces_Hello_section.html): Hello Amazon Keyspaces
- [Learn the basics](https://docs.aws.amazon.com/keyspaces/latest/devguide/example_keyspaces_Scenario_GetStartedKeyspaces_section.html): Learn the basics of Amazon Keyspaces with an AWS SDK

### [Actions](https://docs.aws.amazon.com/keyspaces/latest/devguide/service_code_examples_actions.html)

The following code examples show how to use Amazon Keyspaces with AWS SDKs.

- [CreateKeyspace](https://docs.aws.amazon.com/keyspaces/latest/devguide/example_keyspaces_CreateKeyspace_section.html): Use CreateKeyspace with an AWS SDK
- [CreateTable](https://docs.aws.amazon.com/keyspaces/latest/devguide/example_keyspaces_CreateTable_section.html): Use CreateTable with an AWS SDK
- [DeleteKeyspace](https://docs.aws.amazon.com/keyspaces/latest/devguide/example_keyspaces_DeleteKeyspace_section.html): Use DeleteKeyspace with an AWS SDK
- [DeleteTable](https://docs.aws.amazon.com/keyspaces/latest/devguide/example_keyspaces_DeleteTable_section.html): Use DeleteTable with an AWS SDK
- [GetKeyspace](https://docs.aws.amazon.com/keyspaces/latest/devguide/example_keyspaces_GetKeyspace_section.html): Use GetKeyspace with an AWS SDK
- [GetTable](https://docs.aws.amazon.com/keyspaces/latest/devguide/example_keyspaces_GetTable_section.html): Use GetTable with an AWS SDK
- [ListKeyspaces](https://docs.aws.amazon.com/keyspaces/latest/devguide/example_keyspaces_ListKeyspaces_section.html): Use ListKeyspaces with an AWS SDK
- [ListTables](https://docs.aws.amazon.com/keyspaces/latest/devguide/example_keyspaces_ListTables_section.html): Use ListTables with an AWS SDK
- [RestoreTable](https://docs.aws.amazon.com/keyspaces/latest/devguide/example_keyspaces_RestoreTable_section.html): Use RestoreTable with an AWS SDK
- [UpdateTable](https://docs.aws.amazon.com/keyspaces/latest/devguide/example_keyspaces_UpdateTable_section.html): Use UpdateTable with an AWS SDK


## [Best practices](https://docs.aws.amazon.com/keyspaces/latest/devguide/best-practices.html)

- [NoSQL design](https://docs.aws.amazon.com/keyspaces/latest/devguide/bp-general-nosql-design.html): Review the key differences and design principles for NoSQL database systems like Amazon Keyspaces
- [Connections](https://docs.aws.amazon.com/keyspaces/latest/devguide/connections.html): Learn how to improve and optimize client driver configurations in Amazon Keyspaces.

### [Data modeling](https://docs.aws.amazon.com/keyspaces/latest/devguide/data-modeling.html)

Best practices for data modeling in Amazon Keyspaces.

### [Partition key design](https://docs.aws.amazon.com/keyspaces/latest/devguide/bp-partition-key-design.html)

Best practices for designing partition keys and using them effectively in Amazon Keyspaces.

- [Write sharding](https://docs.aws.amazon.com/keyspaces/latest/devguide/bp-partition-key-sharding.html): Learn how to use write sharding in Amazon Keyspaces databases to distribute workloads evenly across partitions.

### [Cost optimization](https://docs.aws.amazon.com/keyspaces/latest/devguide/bp-cost-optimization.html)

Identify strategies for optimizing costs of your existing Amazon Keyspaces tables.

- [Evaluate your costs at the table level](https://docs.aws.amazon.com/keyspaces/latest/devguide/CostOptimization_TableLevelCostAnalysis.html): Use Cost Explorer to enable table-level filtering and sorting of your Amazon Keyspaces tables to perform table-level cost analysis.
- [Evaluate your table's capacity mode](https://docs.aws.amazon.com/keyspaces/latest/devguide/CostOptimization_TableCapacityMode.html): Select the appropriate capacity mode to optimize costs for your Amazon Keyspaces tables.
- [Evaluate your table's Application Auto Scaling settings](https://docs.aws.amazon.com/keyspaces/latest/devguide/CostOptimization_AutoScalingSettings.html): Learn how to determine if you need to adjust the Application Auto Scaling settings of your Amazon Keyspaces tables.
- [Identify your unused resources](https://docs.aws.amazon.com/keyspaces/latest/devguide/CostOptimization_UnusedResources.html): Identify unused resources and take action to optimize costs of your Amazon Keyspaces tables.
- [Evaluate your table usage patterns](https://docs.aws.amazon.com/keyspaces/latest/devguide/CostOptimization_TableUsagePatterns.html): Determine if sub-optimal table usage patterns can lead to unintentional costs for your Amazon Keyspaces tables.
- [Evaluate your provisioned capacity for right-sized provisioning](https://docs.aws.amazon.com/keyspaces/latest/devguide/CostOptimization_RightSizedProvisioning.html): Determine if you have right-sized provisioning for your provisioned capacity Amazon Keyspaces tables.


## [Troubleshooting](https://docs.aws.amazon.com/keyspaces/latest/devguide/troubleshooting.html)

- [General errors](https://docs.aws.amazon.com/keyspaces/latest/devguide/troubleshooting.general.html): Getting general errors? Here are some common issues and how to resolve them.
- [Connection errors](https://docs.aws.amazon.com/keyspaces/latest/devguide/troubleshooting.connecting.html): Having trouble connecting? Here are some common issues and how to resolve them.
- [Capacity management errors](https://docs.aws.amazon.com/keyspaces/latest/devguide/troubleshooting.serverless.html): Having trouble with serverless capacity? Here are some common issues and how to resolve them.
- [Data definition language errors](https://docs.aws.amazon.com/keyspaces/latest/devguide/troubleshooting.cql.html): Having trouble creating resources? Here are some common issues and how to resolve them.


## [Monitoring Amazon Keyspaces](https://docs.aws.amazon.com/keyspaces/latest/devguide/monitoring-overview.html)

### [Monitoring with CloudWatch](https://docs.aws.amazon.com/keyspaces/latest/devguide/monitoring-cloudwatch.html)

Learn how to use CloudWatch to monitor Amazon Keyspaces performance by analyzing near-real-time metrics and compare to historical information.

- [Metrics and dimensions](https://docs.aws.amazon.com/keyspaces/latest/devguide/metrics-dimensions.html): Learn about the aggregated metrics and dimensions Amazon Keyspaces sends to CloudWatch and which procedures to use to view them.
- [View metrics](https://docs.aws.amazon.com/keyspaces/latest/devguide/view-metrics.html): When you interact with Amazon Keyspaces, it sends the following metrics and dimensions to Amazon CloudWatch.
- [Create alarms](https://docs.aws.amazon.com/keyspaces/latest/devguide/creating-alarms.html): You can create an Amazon CloudWatch alarm for Amazon Keyspaces that sends an Amazon Simple Notification Service (Amazon SNS) message when the alarm changes state.
- [Logging with CloudTrail](https://docs.aws.amazon.com/keyspaces/latest/devguide/logging-using-cloudtrail.html): Learn about logging Amazon Keyspaces with AWS CloudTrail.


## [Security](https://docs.aws.amazon.com/keyspaces/latest/devguide/security.html)

### [Data protection](https://docs.aws.amazon.com/keyspaces/latest/devguide/data-protection.html)

Learn about how to keep your Amazon Keyspaces data protected.

### [Encryption at rest](https://docs.aws.amazon.com/keyspaces/latest/devguide/EncryptionAtRest.html)

Encryption at rest in Amazon Keyspaces protects your data written to disk with fully managed data encryption.

- [How it works](https://docs.aws.amazon.com/keyspaces/latest/devguide/encryption.howitworks.html): Overview of the encryption at rest functionality in Amazon Keyspaces.
- [How to use customer managed keys](https://docs.aws.amazon.com/keyspaces/latest/devguide/encryption.customermanaged.html): How to enable customer managed keys to encrypt tables in Amazon Keyspaces using AWS Key Management Service.
- [Encryption in transit](https://docs.aws.amazon.com/keyspaces/latest/devguide/encryption-in-transit.html): Encryption in transit.
- [Internetwork traffic privacy](https://docs.aws.amazon.com/keyspaces/latest/devguide/inter-network-traffic-privacy.html): Describes how Amazon Keyspaces secures connections from on-premises applications to Amazon Keyspaces and between Amazon Keyspaces and other AWS resources within the same AWS Region.

### [AWS Identity and Access Management](https://docs.aws.amazon.com/keyspaces/latest/devguide/security-iam.html)

How to authenticate requests and manage access to your Amazon Keyspaces resources.

- [How Amazon Keyspaces works with IAM](https://docs.aws.amazon.com/keyspaces/latest/devguide/security_iam_service-with-iam.html): Learn how Amazon Keyspaces works with IAM
- [Identity-based policy examples](https://docs.aws.amazon.com/keyspaces/latest/devguide/security_iam_id-based-policy-examples.html): Learn about IAM policies for Amazon Keyspaces
- [AWS managed policies](https://docs.aws.amazon.com/keyspaces/latest/devguide/security-iam-awsmanpol.html): Learn about AWS managed policies for Amazon Keyspaces and recent changes to those policies.
- [Troubleshooting](https://docs.aws.amazon.com/keyspaces/latest/devguide/security_iam_troubleshoot.html): Use the following information to help you diagnose and fix common issues that you might encounter when working with Amazon Keyspaces and IAM.

### [Using service-linked roles](https://docs.aws.amazon.com/keyspaces/latest/devguide/using-service-linked-roles.html)

How to use service-linked roles to give Amazon Keyspaces access to resources in your AWS account.

- [Application auto scaling](https://docs.aws.amazon.com/keyspaces/latest/devguide/using-service-linked-roles-app-auto-scaling.html): How to use service-linked roles to give Amazon Keyspaces access to resources in your AWS account.
- [Multi-Region Replication](https://docs.aws.amazon.com/keyspaces/latest/devguide/using-service-linked-roles-multi-region-replication.html): How to use service-linked roles to give Amazon Keyspaces access to multi-Region resources in your AWS account.
- [CDC streams](https://docs.aws.amazon.com/keyspaces/latest/devguide/using-service-linked-roles-CDC-streams.html): How to use service-linked roles to give Amazon Keyspaces access to resources in your AWS account.
- [Compliance validation](https://docs.aws.amazon.com/keyspaces/latest/devguide/Keyspaces-compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/keyspaces/latest/devguide/disaster-recovery-resiliency.html): AWS architecture supports data redundancy and resiliency with Amazon Keyspaces multi-Region replication and Point-in-time recovery.

### [Infrastructure security](https://docs.aws.amazon.com/keyspaces/latest/devguide/infrastructure-security.html)

Learn how Amazon Keyspaces isolates service traffic.

- [Using interface VPC endpoints](https://docs.aws.amazon.com/keyspaces/latest/devguide/vpc-endpoints.html): Learn how to control access, help ensure load balancing, and improve read/write throughput when using Amazon Keyspaces with interface VPC endpoints.
- [Using interface VPC endpoints with streams](https://docs.aws.amazon.com/keyspaces/latest/devguide/vpc-endpoints-streams.html): Learn how to create interface VPC endpoints to control access to Amazon Keyspaces CDC streams.
- [Configuration and vulnerability analysis for Amazon Keyspaces](https://docs.aws.amazon.com/keyspaces/latest/devguide/configuration-vulnerability.html): Learn about Vulnerability Analysis and Amazon Keyspaces.

### [Security best practices](https://docs.aws.amazon.com/keyspaces/latest/devguide/best-practices-security.html)

Consider these best practices to help detect and prevent security issues in Amazon Keyspaces.

- [Preventative security best practices](https://docs.aws.amazon.com/keyspaces/latest/devguide/best-practices-security-preventative.html): Consider these preventative best practices in Amazon Keyspaces.
- [Detective security best practices](https://docs.aws.amazon.com/keyspaces/latest/devguide/best-practices-security-detective.html): Learn more about detective security practices that help to discover potential security issues in Amazon Keyspaces.


## [CQL language reference](https://docs.aws.amazon.com/keyspaces/latest/devguide/cql.html)

- [Language elements](https://docs.aws.amazon.com/keyspaces/latest/devguide/cql.elements.html): CQL language elements in Amazon Keyspaces

### [DDL statements](https://docs.aws.amazon.com/keyspaces/latest/devguide/cql.ddl.html)

Learn about data definition language (DDL), which is the set of Cassandra Query Language (CQL) statements used to manage database structures such as keyspaces and tables in Amazon Keyspaces.

- [Keyspaces](https://docs.aws.amazon.com/keyspaces/latest/devguide/cql.ddl.keyspace.html): A keyspace groups related tables that are relevant for one or more applications.
- [Tables](https://docs.aws.amazon.com/keyspaces/latest/devguide/cql.ddl.table.html): Tables are the primary data structures in Amazon Keyspaces.
- [Types](https://docs.aws.amazon.com/keyspaces/latest/devguide/cql.ddl.type.html): UDT â A grouping of fields and data types that you can use to define a single column in Amazon Keyspaces.

### [DML statements](https://docs.aws.amazon.com/keyspaces/latest/devguide/cql.dml.html)

Learn about data manipulation language (DML), which is the set of Cassandra Query Language (CQL) statements used to perform CRUD operations such as SELECT, INSERT, UPDATE, and DELETE in Amazon Keyspaces.

- [SELECT](https://docs.aws.amazon.com/keyspaces/latest/devguide/cql.dml.select.html): Use a SELECT statement to query data.
- [INSERT](https://docs.aws.amazon.com/keyspaces/latest/devguide/cql.dml.insert.html): Use the INSERT statement to add a row to a table.
- [UPDATE](https://docs.aws.amazon.com/keyspaces/latest/devguide/cql.dml.update.html): Use the UPDATE statement to modify a row in a table.
- [DELETE](https://docs.aws.amazon.com/keyspaces/latest/devguide/cql.dml.delete.html): Use the DELETE statement to remove a row from a table.
- [Built-in functions](https://docs.aws.amazon.com/keyspaces/latest/devguide/cql.functions.html): Learn how to use built-in functions from Cassandra Query Language (CQL) with Amazon Keyspaces â for example, UUIDs, and timestamps.
