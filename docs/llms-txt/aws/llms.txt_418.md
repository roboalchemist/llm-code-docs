# Source: https://docs.aws.amazon.com/glue/latest/dg/llms.txt

# AWS Glue User Guide

> How to use and program AWS Glue.

- [What is AWS Glue?](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html)
- [AWS CloudFormation for AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/populate-with-cloudformation-templates.html)
- [Working with AWS SDKs](https://docs.aws.amazon.com/glue/latest/dg/sdk-general-information-section.html)
- [Known issues](https://docs.aws.amazon.com/glue/latest/dg/glue-known-issues.html)
- [Documentation history](https://docs.aws.amazon.com/glue/latest/dg/doc-history.html)
- [AWS Glossary](https://docs.aws.amazon.com/glue/latest/dg/glossary.html)

## [How it works](https://docs.aws.amazon.com/glue/latest/dg/how-it-works.html)

- [Concepts](https://docs.aws.amazon.com/glue/latest/dg/components-key-concepts.html): Understand how AWS Glue works with this overview of important concepts, terminology, and architecture.
- [Components](https://docs.aws.amazon.com/glue/latest/dg/components-overview.html): Create and manage ETL jobs using the components available with AWS Glue, including the console, CLI, and API operations.
- [AWS Glue for Spark and AWS Glue for Ray](https://docs.aws.amazon.com/glue/latest/dg/how-it-works-engines.html): Provides an overview of engines available, specifically Ray, in AWS Glue.
- [Converting semi-structured schemas to relational schemas](https://docs.aws.amazon.com/glue/latest/dg/schema-relationalize.html): Provides an overview of converting schema from semi-structured to relational form.
- [AWS Glue types](https://docs.aws.amazon.com/glue/latest/dg/glue-types.html): Describes the relationship between AWS Glue and its type systems.


## [Getting started](https://docs.aws.amazon.com/glue/latest/dg/setting-up.html)

- [Overview of using AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/start-console-overview.html): Overview of the ETL workflow in the AWS Glue console.

### [Setting up IAM permissions](https://docs.aws.amazon.com/glue/latest/dg/set-up-iam.html)

Set up IAM permissions for AWS Glue.

### [Setting up for AWS Glue Studio](https://docs.aws.amazon.com/glue/latest/dg/setting-up-studio.html)

Before you can use AWS Glue Studio, you must configure an AWS user account, choose an IAM role for your job, and populate the AWS Glue Data Catalog.

- [Review IAM permissions needed for the AWS Glue Studio user](https://docs.aws.amazon.com/glue/latest/dg/getting-started-min-privs.html): To use AWS Glue Studio, the user must have access to various AWS resources.
- [Review IAM permissions needed for ETL jobs](https://docs.aws.amazon.com/glue/latest/dg/getting-started-min-privs-job.html): When you create a job using AWS Glue Studio, the job assumes the permissions of the IAM role that you specify when you create it.
- [Set up IAM permissions for AWS Glue Studio](https://docs.aws.amazon.com/glue/latest/dg/getting-started-iam-permissions.html): You can create the roles and assign policies to users and job roles by using the AWS administrator user.
- [Configure a VPC for your ETL job](https://docs.aws.amazon.com/glue/latest/dg/getting-started-vpc-config.html): You can use Amazon Virtual Private Cloud (Amazon VPC) to define a virtual network in your own logically isolated area within the AWS Cloud, known as a virtual private cloud (VPC).
- [Getting started with notebooks in AWS Glue Studio](https://docs.aws.amazon.com/glue/latest/dg/notebook-getting-started.html): When you start a notebook through AWS Glue Studio, all the configuration steps are done for you so that you can explore your data and start developing your job script after only a few seconds.

### [Setting up usage profiles](https://docs.aws.amazon.com/glue/latest/dg/start-usage-profiles.html)

Describes usage profiles in AWS Glue.

- [Managing usage profiles](https://docs.aws.amazon.com/glue/latest/dg/start-usage-profiles-managing.html): Describes creating and managing usage profiles in AWS Glue.
- [Usage profiles and jobs](https://docs.aws.amazon.com/glue/latest/dg/start-usage-profiles-jobs.html): Describes authoring and running jobs with usage profiles in AWS Glue.
- [Getting started with the AWS Glue Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/start-data-catalog.html): Create your first AWS Glue Data Catalog using this quick start tutorial.

### [Setting up network access to data stores](https://docs.aws.amazon.com/glue/latest/dg/start-connecting.html)

Set up your environment so that AWS Glue can connect to your data stores and run ETL jobs.

- [Setting up a VPC to connect to PyPI for AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/setup-vpc-for-pypi.html): Walk through the process of setting up your VPC to allow AWS Glue access to additional Python modules.
- [Setting up DNS in your VPC](https://docs.aws.amazon.com/glue/latest/dg/set-up-vpc-dns.html): Overview of the process of setting up DNS in your VPC.
- [Setting up encryption](https://docs.aws.amazon.com/glue/latest/dg/set-up-encryption.html): Overview of the process of setting up encryption with AWS Glue.
- [Setting up networking for development](https://docs.aws.amazon.com/glue/latest/dg/start-development-endpoint.html): Set up your AWS Glue environment for connecting to a development endpoint.


## [Data discovery and cataloging](https://docs.aws.amazon.com/glue/latest/dg/catalog-and-crawler.html)

### [Populating the Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/populate-catalog-methods.html)

You can populate the AWS Glue Data Catalog using the following methods:

### [Using an AWS Glue crawler](https://docs.aws.amazon.com/glue/latest/dg/add-crawler.html)

Learn about crawlers in AWS Glue, how to add them, and the types of data stores you can crawl.

- [Supported data sources for crawling](https://docs.aws.amazon.com/glue/latest/dg/crawler-data-stores.html): Crawlers can crawl the following file-based and table-based data stores.
- [Crawler prerequisites](https://docs.aws.amazon.com/glue/latest/dg/crawler-prereqs.html): The crawler assumes the permissions of the AWS Identity and Access Management (IAM) role that you specify when you define it.

### [Defining and managing classifers](https://docs.aws.amazon.com/glue/latest/dg/add-classifier.html)

Overview of built-in and custom classifiers and how they are used in AWS Glue.

- [Writing custom classifiers for diverse data formats](https://docs.aws.amazon.com/glue/latest/dg/custom-classifier.html): Describes how to create a custom classifier for AWS Glue.
- [Creating classifiers on the console](https://docs.aws.amazon.com/glue/latest/dg/console-classifiers.html): Define classifiers in the AWS Glue console to infer the schema of your metadata tables in the Data Catalog.

### [Configuring a crawler](https://docs.aws.amazon.com/glue/latest/dg/define-crawler.html)

A crawler accesses your data store, identifies metadata, and creates table definitions in the AWS Glue Data Catalog.

- [Set crawler properties](https://docs.aws.amazon.com/glue/latest/dg/define-crawler-set-crawler-properties.html)
- [Choose data sources and classifiers](https://docs.aws.amazon.com/glue/latest/dg/define-crawler-choose-data-sources.html): Next, configure the data sources and classifiers for the crawler.
- [Configure security settings](https://docs.aws.amazon.com/glue/latest/dg/define-crawler-configure-security-settings.html)
- [Set output and scheduling](https://docs.aws.amazon.com/glue/latest/dg/define-crawler-set-output-and-scheduling.html)
- [Review and create](https://docs.aws.amazon.com/glue/latest/dg/define-crawler-review.html): Review the crawler settings you configured, and create the crawler.

### [Scheduling a crawler](https://docs.aws.amazon.com/glue/latest/dg/schedule-crawler.html)

Overview of how to schedule a crawler in AWS Glue.

- [Create a crawler schedule](https://docs.aws.amazon.com/glue/latest/dg/create-crawler-schedule.html): You can create a schedule for the crawler using the AWS Glue console or AWS CLI.
- [Create a schedule for an existing crawler](https://docs.aws.amazon.com/glue/latest/dg/Update-crawler-schedule.html): Follow these steps to set up a recurring schedule for an existing crawler.

### [Viewing crawler results and details](https://docs.aws.amazon.com/glue/latest/dg/console-crawlers-details.html)

After the crawler runs successfully, it creates table definitions in the Data Catalog.

- [Parameters set on Data Catalog tables by crawler](https://docs.aws.amazon.com/glue/latest/dg/table-properties-crawler.html): These table properties are set by AWS Glue crawlers.

### [Customizing crawler behavior](https://docs.aws.amazon.com/glue/latest/dg/crawler-configuration.html)

Learn about how to configure what a crawler does when it encounters schema changes and partition changes in your data store.

- [Scheduling incremental crawls](https://docs.aws.amazon.com/glue/latest/dg/incremental-crawls.html): Configure an AWS Glue crawler run incremental crawls to add only new partitions to the table schema.
- [Generating partition indexes](https://docs.aws.amazon.com/glue/latest/dg/crawler-configure-partition-indexes.html): The Data Catalog supports creating partition indexes to provide efficient lookup for specific partitions.
- [Preventing a crawler from changing schema](https://docs.aws.amazon.com/glue/latest/dg/crawler-schema-changes-prevent.html): You can prevent AWS Glue crawlers from making any schema changes to the Data Catalog when they run.
- [Creating a single schema for each S3 paths](https://docs.aws.amazon.com/glue/latest/dg/crawler-grouping-policy.html): By default, when a crawler defines tables for data stored in Amazon S3, it considers both data compatibility and schema similarity.
- [Specifying the table location and partitioning level](https://docs.aws.amazon.com/glue/latest/dg/crawler-table-level.html): By default, when a crawler defines tables for data stored in Amazon S3 the crawler attempts to merge schemas together, and create top-level tables (year=2019).
- [Specifying a table threshold](https://docs.aws.amazon.com/glue/latest/dg/crawler-maximum-number-of-tables.html): Specify the maximum number of tables the crawler is allowed to create.

### [Configuring a crawler to use Lake Formation credentials](https://docs.aws.amazon.com/glue/latest/dg/crawler-lf-integ.html)

You can configure a crawler to use AWS Lake Formation credentials to access an Amazon S3 data store or a Data Catalog table with an underlying Amazon S3 location within the same AWS account or another AWS account.

- [Setup required when the crawler and registered Amazon S3 location reside in different accounts (cross-account crawling)](https://docs.aws.amazon.com/glue/latest/dg/cross-account-crawling.html): To allow the crawler to access a data store in a different account using Lake Formation credentials, you must first register the Amazon S3 data location with Lake Formation.

### [Accelerating crawls using Amazon S3 event notifications](https://docs.aws.amazon.com/glue/latest/dg/crawler-s3-event-notifications.html)

Instead of listing the objects from an Amazon S3 or Data Catalog target, you can configure the crawler to use Amazon S3 events to find any changes.

- [Setting up a crawler for Amazon S3 event notifications for an Amazon S3 target](https://docs.aws.amazon.com/glue/latest/dg/crawler-s3-event-notifications-setup-console-s3-target.html): Learn to set up a crawler for Amazon S3 event notifications for an Amazon S3 target.
- [Setting up a crawler for Amazon S3 event notifications for a Data Catalog table](https://docs.aws.amazon.com/glue/latest/dg/crawler-s3-event-notifications-setup-console-catalog-target.html): Learn to set up a crawler for Amazon S3 event notifications for a Data Catalog target:
- [Tutorial: Adding an AWS Glue crawler](https://docs.aws.amazon.com/glue/latest/dg/tutorial-add-crawler.html): Use this tutorial to create a crawler for a public Amazon S3 data source and create structures in the AWS Glue Data Catalog.

### [Defining metadata manually](https://docs.aws.amazon.com/glue/latest/dg/populate-dg-manual.html)

Describes how to define a database and tables in your Data Catalog using AWS Glue.

- [Creating databases](https://docs.aws.amazon.com/glue/latest/dg/define-database.html): Describes how to define a database in your Data Catalog using AWS Glue.

### [Creating tables](https://docs.aws.amazon.com/glue/latest/dg/tables-described.html)

Overview of tables and table partitions in the AWS Glue Data Catalog.

- [Creating partition indexes](https://docs.aws.amazon.com/glue/latest/dg/partition-indexes.html): Describes how to create partition indexes in a table to improve query performance.
- [Integrating with other AWS services](https://docs.aws.amazon.com/glue/latest/dg/populate-dc-other-services.html): Use AWS services such as AWS Lake Formation and Amazon Athena to populate the catalog.
- [Data Catalog settings](https://docs.aws.amazon.com/glue/latest/dg/console-data-catalog-settings.html): Update the settings page on the AWS Glue console to provide the encryption properties and AWS Glue resource policies for the Data Catalog.

### [Populating and managing transactional tables](https://docs.aws.amazon.com/glue/latest/dg/populate-otf.html)

Describes the methods to populate and manage transactional tables in the AWS Glue Data Catalog.

### [Optimizing Iceberg tables](https://docs.aws.amazon.com/glue/latest/dg/table-optimizers.html)

Enable table optimizers to manage table storage and optimize query performance for Iceberg tables in the AWS Glue Data Catalog.

- [Prerequisites](https://docs.aws.amazon.com/glue/latest/dg/optimization-prerequisites.html): The table optimizer assumes the permissions of the AWS Identity and Access Management (IAM) role that you specify when you enable optimization options (compaction, snapshot retention, and orphan file delettion) for a table.

### [Catalog-level table optimizers](https://docs.aws.amazon.com/glue/latest/dg/catalog-level-optimizers.html)

Configure and use table optimizers at the catalog-level to apply consistent optimizer settings across all tables within a catalog.

- [Enabling catalog-level automatic table optimization](https://docs.aws.amazon.com/glue/latest/dg/enable-auto-table-optimizers.html): Learn how to enable catalog-level table optimization for all new tables in the AWS Glue Data Catalog.
- [Viewing catalog-level optimizations](https://docs.aws.amazon.com/glue/latest/dg/view-catalog-optimizations.html): When catalog-level table optimization is enabled, anytime an Apache Iceberg table is created or updated via the CreateTable or UpdateTable APIs through AWS Management Console, SDK, or AWS Glue crawler, an equivalent table level setting is created for that table.
- [Disabling catalog-level table optimization](https://docs.aws.amazon.com/glue/latest/dg/disable-auto-table-optimizers.html): You can disable table optimization for new tables using the AWS Lake Formation console, the glue:UpdateCatalog API.

### [Compaction optimization](https://docs.aws.amazon.com/glue/latest/dg/compaction-management.html)

The Amazon S3 data lakes using open table formats like Apache Iceberg store data as S3 objects.

- [Enabling compaction optimizer](https://docs.aws.amazon.com/glue/latest/dg/enable-compaction.html): You can use AWS Glue console, AWS CLI, or AWS API to enable compaction for your Apache Iceberg tables in the AWS Glue Data Catalog.
- [Disabling compaction optimizer](https://docs.aws.amazon.com/glue/latest/dg/disable-compaction.html): You can disable automatic compaction for a particular Apache Iceberg table using AWS Glue console or AWS CLI.

### [Snapshot retention optimization](https://docs.aws.amazon.com/glue/latest/dg/snapshot-retention-management.html)

Apache Iceberg snapshot retention feature allows users to query historical data at specific points in time and revert unwanted modifications to their tables.

- [Enabling snapshot retention optimizer](https://docs.aws.amazon.com/glue/latest/dg/enable-snapshot-retention.html): You can use AWS Glue console, AWS CLI, or AWS API to enable snapshot retention optimizers for your Apache Iceberg tables in the Data Catalog.
- [Updating snapshot retention optimizer](https://docs.aws.amazon.com/glue/latest/dg/update-snapshot-retention.html): You can update the existing configuration of an snapshot retention optimizer for a particular Apache Iceberg table using the AWS Glue console, AWS CLI, or the UpdateTableOptimizer API.
- [Disabling snapshot retention optimizer](https://docs.aws.amazon.com/glue/latest/dg/disable-snapshot-retention.html): You can disable the snapshot retention optimizer for a particular Apache Iceberg table using AWS Glue console or AWS CLI.

### [Deleting orphan files](https://docs.aws.amazon.com/glue/latest/dg/orphan-file-deletion.html)

AWS Glue Data Catalog allows you to remove orphan files from your Iceberg tables.

- [Enabling orphan file deletion](https://docs.aws.amazon.com/glue/latest/dg/enable-orphan-file-deletion.html): You can use AWS Glue console, AWS CLI, or AWS API to enable orphan file deletion for your Apache Iceberg tables in the Data Catalog.
- [Updating orphan file deletion optimizer](https://docs.aws.amazon.com/glue/latest/dg/update-orphan-file-deletion.html): You can modify the configuration for the orphan file deletion optimizer, such as changing the retention period for orphan files or the IAM role used by the optimizer using AWS Glue console, AWS CLI, or the UpdateTableOptimizer operation.
- [Disabling orphan file deletion](https://docs.aws.amazon.com/glue/latest/dg/disable-orphan-file-deletion.html): You can disable orphan file deletion optimizer for a particular Apache Iceberg table using AWS Glue console or AWS CLI.
- [Viewing optimization details](https://docs.aws.amazon.com/glue/latest/dg/view-optimization-status.html): You can view the optimization status for Apache Iceberg tables in the AWS Glue console, AWS CLI, or using AWS API operations.
- [Viewing Amazon CloudWatch metrics](https://docs.aws.amazon.com/glue/latest/dg/view-optimization-metrics.html): After running the table optimizers successfully, the service creates Amazon CloudWatch metrics on the optimization job performance.
- [Deleting an optimizer](https://docs.aws.amazon.com/glue/latest/dg/delete-optimizer.html): You can delete an optimizer and associated metadata for the table using AWS CLI or AWS API operation.
- [Considerations and limitations](https://docs.aws.amazon.com/glue/latest/dg/optimizer-notes.html): This section includes things to consider when using table optimizers within the AWS Glue Data Catalog.
- [Supported Regions for table optimizers](https://docs.aws.amazon.com/glue/latest/dg/regions-optimizers.html): The table optimization features (compaction, snapshot retention, and orphan file deletion) for AWS Glue Data Catalog are available in the following AWS Regions:

### [Optimizing query performance for Iceberg tables](https://docs.aws.amazon.com/glue/latest/dg/iceberg-column-statistics.html)

Describes how to generate column statistics to improve query performance for Iceberg tables.

- [Prerequisites](https://docs.aws.amazon.com/glue/latest/dg/iceberg-column-stats-prereqs.html): To generate or update column statistics for Iceberg tables, the statistics generation task assumes an AWS Identity and Access Management (IAM) role on your behalf.
- [Generating column statistics for Iceberg tables](https://docs.aws.amazon.com/glue/latest/dg/iceberg-generate-column-stats.html): Follow these steps to configure a schedule for generating statistics in the Data Catalog using AWS Glue console or AWS CLI or the or run the StartColumnStatisticsTaskRun operation.

### [Managing the Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/manage-catalog.html)

Use Data Catalog management practices to securely maintain your metadata tables.

### [Updating the schema and adding new partitions](https://docs.aws.amazon.com/glue/latest/dg/update-from-job.html)

Update your AWS Glue Data Catalog with a schema and partitions from within your ETL script.

- [Integrating with MongoDB](https://docs.aws.amazon.com/glue/latest/dg/integrate-with-mongo-db.html): Use a MongoDB connection in your AWS Glue job and specify the MongoDB database and collection within your job script.

### [Optimizing query performance using column statistics](https://docs.aws.amazon.com/glue/latest/dg/column-statistics.html)

Describes how to generate column statistics to improve query performance.

- [Prerequisites](https://docs.aws.amazon.com/glue/latest/dg/column-stats-prereqs.html): To generate or update column statistics, the statistics generation task assumes an AWS Identity and Access Management (IAM) role on your behalf.

### [Automatic column statistics generation](https://docs.aws.amazon.com/glue/latest/dg/auto-column-stats-generation.html)

Learn how to automatically generate column statistics for new tables in the AWS Glue Data Catalog.

- [Enabling catalog-level automatic statistics generation](https://docs.aws.amazon.com/glue/latest/dg/enable-auto-column-stats-generation.html): Learn how to manage automatic column statistics generation for new tables in the AWS Glue Data Catalog.
- [Viewing automated table-level settings](https://docs.aws.amazon.com/glue/latest/dg/view-auto-column-stats-settings.html): When catalog-level statistics collection is enabled, anytime an Apache Hive table or Apache Iceberg table is created or updated via the CreateTable or UpdateTable APIs through AWS Management Console, SDK, or AWS Glue crawler, an equivalent table level setting is created for that table.
- [Disabling catalog-level column statistics generation](https://docs.aws.amazon.com/glue/latest/dg/disable-auto-column-stats-generation.html): You can disable automatic column statistics generation for new tables using the AWS Lake Formation console, the glue:UpdateCatalogSettings API, or the glue:DeleteColumnStatisticsTaskSettings API.

### [Generating column statistics on a schedule](https://docs.aws.amazon.com/glue/latest/dg/generate-column-stats.html)

Follow these steps to configure a schedule for generating column statistics in the AWS Glue Data Catalog using the AWS Glue console, the AWS CLI, or the CreateColumnStatisticsTaskSettings operation.

- [Managing the schedule for column statistics generation](https://docs.aws.amazon.com/glue/latest/dg/manage-column-stats-schedule.html): You can manage the scheduling operations such as updating, starting, stopping, and deleting schedules for the column statistics generation in AWS Glue.
- [Generating column statistics on demand](https://docs.aws.amazon.com/glue/latest/dg/column-stats-on-demand.html): You can run the column statistics task for the AWS Glue Data Catalog tables task on-demand without a set schedule.
- [Viewing column statistics](https://docs.aws.amazon.com/glue/latest/dg/view-column-stats.html): After generating the statistics successfully, Data Catalog stores this information for the cost-based optimizers in Amazon Athena and Amazon Redshift to make optimal choices when running queries.
- [Viewing column statistics task runs](https://docs.aws.amazon.com/glue/latest/dg/view-stats-run.html): After you run a column statistics task, you can explore the task run details for a table using AWS Glue console, AWS CLI or using GetColumnStatisticsTaskRuns operation.
- [Stopping column statistics task run](https://docs.aws.amazon.com/glue/latest/dg/stop-stats-run.html): You can stop a column statistics task run for a table using AWS Glue console, AWS CLI or using StopColumnStatisticsTaskRun operation.
- [Deleting column statistics](https://docs.aws.amazon.com/glue/latest/dg/delete-column-stats.html): You can delete column statistics using the DeleteColumnStatisticsForTable API operation or AWS CLI.
- [Considerations and limitations](https://docs.aws.amazon.com/glue/latest/dg/column-stats-notes.html): The following considerations and limitations apply to generating column statistics.
- [Encrypting your Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/catalog-encryption.html): You can protect your metadata stored in the AWS Glue Data Catalog at rest using encryption keys managed by AWS Key Management Service (AWS KMS).
- [Securing your Data Catalog using Lake Formation](https://docs.aws.amazon.com/glue/latest/dg/secure-catalog.html): AWS Lake Formation is a service that makes it easier to set up a secure data lake in AWS.
- [Working with AWS Glue Data Catalog views](https://docs.aws.amazon.com/glue/latest/dg/catalog-views.html): You can create and manage views in the AWS Glue Data Catalog, commonly known as AWS Glue Data Catalog views.

### [Accessing the Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/access_catalog.html)

Use AWS services such as AWS Lake Formation, Amazon Athena, Amazon EMR, and Amazon Redshift to access the catalog.

- [Connecting to the Data Catalog using AWS Glue Iceberg REST endpoint](https://docs.aws.amazon.com/glue/latest/dg/connect-glu-iceberg-rest.html): AWS Glue's Iceberg REST endpoint supports API operations specified in the Apache Iceberg REST specification.
- [Connecting to the Data Catalog using AWS Glue Iceberg REST extension endpoint](https://docs.aws.amazon.com/glue/latest/dg/connect-glue-iceberg-rest-ext.html): AWS Glue Iceberg REST extension endpoint provides additional APIs, which are not present in the Apache Iceberg REST specification, and provides server-side scan planning capabilities.
- [AWS Glue REST APIs for Apache Iceberg](https://docs.aws.amazon.com/glue/latest/dg/iceberg-rest-apis.html): AWS Glue Iceberg REST catalog and AWS Glue extension API specifications.
- [Connecting to Data Catalog from a standalone Spark application](https://docs.aws.amazon.com/glue/latest/dg/connect-gludc-spark.html): You can connect to the Data Catalog from a stand application using an Apache Iceberg connector.
- [Data mapping between Amazon Redshift and Apache Iceberg](https://docs.aws.amazon.com/glue/latest/dg/data-mapping-rs-iceberg.html): Redshift and Iceberg support various data types.
- [Considerations and limitations when using AWS Glue Iceberg REST Catalog APIs](https://docs.aws.amazon.com/glue/latest/dg/limitation-glue-iceberg-rest-api.html): Following are the considerations and limitations when using the Apache Iceberg REST Catalog Data Definition Language (DDL) operation behavior.
- [Data Catalog best practices](https://docs.aws.amazon.com/glue/latest/dg/best-practice-catalog.html): Best practices for effectively managing and utilizing the Data Catalog.
- [Monitoring Data Catalog usage metrics in Amazon CloudWatch](https://docs.aws.amazon.com/glue/latest/dg/data-catalog-cloudwatch-metrics.html): Monitor your AWS Glue Data Catalog usage with Amazon CloudWatch metrics to optimize performance and manage costs.

### [AWS Glue Schema registry](https://docs.aws.amazon.com/glue/latest/dg/schema-registry.html)

Describes the use of the AWS Glue Schema registry.

- [How it works](https://docs.aws.amazon.com/glue/latest/dg/schema-registry-works.html): Describes how the serialization and deserialization processes in schema registry work.

### [Getting started](https://docs.aws.amazon.com/glue/latest/dg/schema-registry-gs.html)

Provides an overview and walk you through setting up and using schema registry.

### [Installing SerDe Libraries](https://docs.aws.amazon.com/glue/latest/dg/schema-registry-gs-serde.html)

The SerDe libraries provide a framework for serializing and deserializing data.

- [Java Implementation](https://docs.aws.amazon.com/glue/latest/dg/schema-registry-gs-serde-java.html)
- [C# Implementation](https://docs.aws.amazon.com/glue/latest/dg/schema-registry-gs-serde-csharp.html)

### [Creating a registry](https://docs.aws.amazon.com/glue/latest/dg/schema-registry-gs3.html)

Explains how to create a new schema registry.

- [Dealing with a specific record (JAVA POJO) for JSON](https://docs.aws.amazon.com/glue/latest/dg/schema-registry-gs-json-java-pojo.html): You can use a plain old Java object (POJO) and pass the object as a record.
- [Creating a schema](https://docs.aws.amazon.com/glue/latest/dg/schema-registry-gs4.html): Explains how to create schemas in AWS Glue.

### [Updating a schema or registry](https://docs.aws.amazon.com/glue/latest/dg/schema-registry-gs5.html)

Explains how to update a schema, a schema version, or a registry in AWS Glue.

- [Updating a schema](https://docs.aws.amazon.com/glue/latest/dg/schema-registry-gs5b.html): You can update the description or compatibility setting for a schema.
- [Adding a schema version](https://docs.aws.amazon.com/glue/latest/dg/schema-registry-gs5c.html): When you add a schema version, you will need to compare the versions to make sure the new schema will be accepted.

### [Deleting a schema or registry](https://docs.aws.amazon.com/glue/latest/dg/schema-registry-gs7.html)

Explains how to delete a schema, a schema version, or a registry in AWS Glue

- [Deleting a registry](https://docs.aws.amazon.com/glue/latest/dg/schema-registry-gs7c.html): You may want to delete a registry when the schemas it contains should no longer be organized under that registry.
- [Accessing Amazon CloudWatch metrics](https://docs.aws.amazon.com/glue/latest/dg/schema-registry-gs-monitoring.html): Learn abou the available CloudWatch metrics for a schema registry.
- [Sample CloudFormation template for schema registry](https://docs.aws.amazon.com/glue/latest/dg/schema-registry-integrations-cfn.html): The following is a sample template for creating Schema Registry resources in CloudFormation.
- [Integrating with AWS Glue Schema Registry](https://docs.aws.amazon.com/glue/latest/dg/schema-registry-integrations.html): Learn about how AWS Glue schema registry integrates with Amazon Kinesis Data Streams, Amazon MSK or Apache Kafka.
- [Migrating to AWS Glue Schema Registry](https://docs.aws.amazon.com/glue/latest/dg/schema-registry-integrations-migration.html): Learn about migrating a third-party schema registry to the AWS Glue schema registry.


## [Connecting to data](https://docs.aws.amazon.com/glue/latest/dg/glue-connections.html)

- [Unified connections](https://docs.aws.amazon.com/glue/latest/dg/using-connectors-unified-connections.html): AWS recently introduced a new feature called "SageMaker LakeHouse Connections" or "AWS Glue Unified Connections." This feature allows you to create connections that can be used by multiple AWS services, such as AWS Glue and Amazon Athena.
- [Available connections](https://docs.aws.amazon.com/glue/latest/dg/available-connections.html): AWS Glue supports the following connection types:
- [REST API Connections](https://docs.aws.amazon.com/glue/latest/dg/rest-api-connections.html): AWS Glue connectors cover a wide range of data sources both AWS and external.
- [AWS Glue connection properties](https://docs.aws.amazon.com/glue/latest/dg/connection-properties.html): This topic includes information about properties for AWS Glue connections.
- [Storing connection credentials in AWS Secrets Manager](https://docs.aws.amazon.com/glue/latest/dg/connection-properties-secrets-manager.html): Use AWS Secrets Manager to let AWS Glue access your connection credentials at runtime for ETL jobs and crawler runs.

### [Adding an AWS Glue connection](https://docs.aws.amazon.com/glue/latest/dg/console-connections.html)

Define connections on the AWS Glue console to provide the properties required to access a data store.

### [Connecting to Adobe Analytics](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-adobe-analytics.html)

Adobe Analytics is a robust data analysis platform that collects data from multi-channel digital experiences that support the customer journey and provides tools for analyzing the data.

- [AWS Glue support for Adobe Analytics](https://docs.aws.amazon.com/glue/latest/dg/adobe-analytics-support.html): AWS Glue supports Adobe Analytics as follows:
- [IAM policies](https://docs.aws.amazon.com/glue/latest/dg/adobeanalytics-configuring-iam-permissions.html): The following sample policy describes the required AWS permissions for creating and using connections.
- [Configuring Adobe Analytics](https://docs.aws.amazon.com/glue/latest/dg/adobeanalytics-configuring.html): Before you can use AWS Glue to transfer from Adobe Analytics, you must meet the following requirements:
- [Configuring Adobe Analytics connections](https://docs.aws.amazon.com/glue/latest/dg/adobeanalytics-configuring-connections.html): Adobe Analytics supports AUTHORIZATION_CODE grant type for OAuth2.
- [Reading from Adobe Analytics entities](https://docs.aws.amazon.com/glue/latest/dg/adobeanalytics-reading-from-entities.html): Prerequisites
- [Adobe Analytics connection options](https://docs.aws.amazon.com/glue/latest/dg/adobeanalytics-connection-options.html): The following are connection options for Adobe Analytics:
- [Creating an Adobe Analytics account](https://docs.aws.amazon.com/glue/latest/dg/adobeanalytics-create-account.html)
- [Limitations](https://docs.aws.amazon.com/glue/latest/dg/adobeanalytics-connector-limitations.html): The following are limitations for the Adobe Analytics connector:

### [Connecting to Adobe Marketo Engage](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-data-adobe-marketo-engage.html)

AWS Glue provides support for connecting to Adobe Marketo Engage.

- [AWS Glue support for Adobe Marketo Engage](https://docs.aws.amazon.com/glue/latest/dg/adobe-marketo-engage-support.html): AWS Glue supports Adobe Marketo Engage as follows:
- [IAM policies](https://docs.aws.amazon.com/glue/latest/dg/adobe-marketo-engage-configuring-iam-permissions.html): The following sample policy describes the required AWS IAM permissions for creating and using connections.
- [Configuring Adobe Marketo Engage](https://docs.aws.amazon.com/glue/latest/dg/adobe-marketo-engage-configuring.html): Before you can use AWS Glue to transfer data from Adobe Marketo Engage, you must meet these requirements:
- [Configuring Adobe Marketo Engage connections](https://docs.aws.amazon.com/glue/latest/dg/adobe-marketo-engage-configuring-connections.html): Adobe Marketo Engage supports the CLIENT CREDENTIALS grant type for OAuth2.
- [Reading from Adobe Marketo Engage entities](https://docs.aws.amazon.com/glue/latest/dg/adobe-marketo-engage-reading-from-entities.html): Prerequisite
- [Writing to Adobe Marketo Engage entities](https://docs.aws.amazon.com/glue/latest/dg/adobe-marketo-engage-writing-to-entities.html): Prerequisites
- [Adobe Marketo Engage connection options](https://docs.aws.amazon.com/glue/latest/dg/adobe-marketo-engage-connection-options.html): The following are connection options for Adobe Marketo Engage:
- [Limitations and notes for Adobe Marketo Engage connector](https://docs.aws.amazon.com/glue/latest/dg/adobe-marketo-engage-connector-limitations.html): The following are limitations or notes for the Adobe Marketo Engage connector:

### [Connecting to Amazon Redshift](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-data-redshift.html)

AWS Glue provides built-in support for Amazon Redshift.

- [Creating an Amazon Redshift connection](https://docs.aws.amazon.com/glue/latest/dg/creating-redshift-connection.html)
- [Creating a Amazon Redshift source node](https://docs.aws.amazon.com/glue/latest/dg/creating-redshift-source-node.html)
- [Creating an Amazon Redshift target node](https://docs.aws.amazon.com/glue/latest/dg/creating-redshift-target-node.html)
- [Advanced options](https://docs.aws.amazon.com/glue/latest/dg/creating-redshift-connection-advanced-options.html): See Using the Amazon Redshift Spark connector on AWS Glue.

### [Connecting to Asana](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-asana.html)

Asana is a cloud-based team collaboration solution that helps teams organize, plan, and complete tasks and projects.

- [AWS Glue support for Asana](https://docs.aws.amazon.com/glue/latest/dg/asana-support.html): AWS Glue supports Asana as follows:
- [IAM policies](https://docs.aws.amazon.com/glue/latest/dg/asana-configuring-iam-permissions.html): The following sample policy describes the required AWS permissions for creating and using connections.
- [Configuring Asana](https://docs.aws.amazon.com/glue/latest/dg/asana-configuring.html): Before you can use AWS Glue to transfer from Asana, you must meet the following requirements:
- [Configuring Asana connections](https://docs.aws.amazon.com/glue/latest/dg/asana-configuring-connections.html): Asana supports the AUTHORIZATION_CODE grant type for OAuth2.
- [Reading from Asana entities](https://docs.aws.amazon.com/glue/latest/dg/asana-reading-from-entities.html): Prerequisites
- [Asana connection options](https://docs.aws.amazon.com/glue/latest/dg/asana-connection-options.html): The following are connection options for Asana:
- [Creating an Asana account](https://docs.aws.amazon.com/glue/latest/dg/asana-create-account.html)
- [Limitations](https://docs.aws.amazon.com/glue/latest/dg/asana-connector-limitations.html): The following are limitations for the Asana connector:

### [Connecting to Azure Cosmos DB](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-data-azurecosmos.html)

AWS Glue provides built-in support for Azure Cosmos DB.

- [Creating a Azure Cosmos DB connection](https://docs.aws.amazon.com/glue/latest/dg/creating-azurecosmos-connection.html): Prerequisites:
- [Creating a Azure Cosmos DB source node](https://docs.aws.amazon.com/glue/latest/dg/creating-azurecosmos-source-node.html)
- [Creating a Azure Cosmos DB target node](https://docs.aws.amazon.com/glue/latest/dg/creating-azurecosmos-target-node.html)

### [Connecting to Azure SQL](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-data-azuresql.html)

AWS Glue provides built-in support for Azure SQL.

- [Creating a Azure SQL connection](https://docs.aws.amazon.com/glue/latest/dg/creating-azuresql-connection.html): To connect to Azure SQL from AWS Glue, you will need to create and store your Azure SQL credentials in a AWS Secrets Manager secret, then associate that secret with a Azure SQL AWS Glue connection.
- [Creating a Azure SQL source node](https://docs.aws.amazon.com/glue/latest/dg/creating-azuresql-source-node.html)
- [Creating a Azure SQL target node](https://docs.aws.amazon.com/glue/latest/dg/creating-azuresql-target-node.html)

### [Connecting to Blackbaud Raiser's Edge NXT](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-data-blackbaud.html)

AWS Glue provides support for connecting to Blackbaud Raiser's Edge NXT.

- [AWS Glue support for Blackbaud Raiser's Edge NXT](https://docs.aws.amazon.com/glue/latest/dg/blackbaud-support.html): AWS Glue supports Blackbaud Raiser's Edge NXT as follows:
- [IAM policies](https://docs.aws.amazon.com/glue/latest/dg/blackbaud-configuring-iam-permissions.html): The following sample policy describes the required AWS IAM permissions for creating and using connections.
- [Configuring Blackbaud Raiser's Edge NXT](https://docs.aws.amazon.com/glue/latest/dg/blackbaud-configuring.html): Before you can use AWS Glue to transfer data from Blackbaud Raiser's Edge NXT, you must meet these requirements:
- [Configuring Blackbaud Raiser's Edge NXT connections](https://docs.aws.amazon.com/glue/latest/dg/blackbaud-configuring-connections.html): Blackbaud Raiser's Edge NXT supports the AUTHORIZATION_CODE grant type for OAuth2.
- [Reading from Blackbaud Raiser's Edge NXT entities](https://docs.aws.amazon.com/glue/latest/dg/blackbaud-reading-from-entities.html): Prerequisite
- [Blackbaud Raiser's Edge NXT connection options](https://docs.aws.amazon.com/glue/latest/dg/blackbaud-connection-options.html): The following are connection options for Blackbaud Raiser's Edge NXT:
- [Blackbaud Raiser's Edge NXT limitations](https://docs.aws.amazon.com/glue/latest/dg/blackbaud-connection-limitations.html): The following are limitations or notes for Blackbaud Raiser's Edge NXT:

### [Connecting to CircleCI](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-data-circleci.html)

AWS Glue provides support for connecting to CircleCI.

- [AWS Glue support for CircleCI](https://docs.aws.amazon.com/glue/latest/dg/circleci-support.html): AWS Glue supports CircleCI as follows:
- [IAM policies](https://docs.aws.amazon.com/glue/latest/dg/circleci-configuring-iam-permissions.html): The following sample policy describes the required AWS IAM permissions for creating and using connections.
- [Configuring CircleCI](https://docs.aws.amazon.com/glue/latest/dg/circleci-configuring.html): Before you can use AWS Glue to transfer data from CircleCI, you must meet these requirements:
- [Configuring CircleCI connections](https://docs.aws.amazon.com/glue/latest/dg/circleci-configuring-connections.html): CircleCI supports custom authentication.
- [Reading from CircleCI entities](https://docs.aws.amazon.com/glue/latest/dg/circleci-reading-from-entities.html): Prerequisite
- [CircleCI connection options](https://docs.aws.amazon.com/glue/latest/dg/circleci-connection-options.html): The following are connection options for CircleCI:
- [CircleCI limitations](https://docs.aws.amazon.com/glue/latest/dg/circleci-connection-limitations.html): The following are limitations or notes for CircleCI:

### [Connecting to Datadog](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-datadog.html)

Datadog is a monitoring and analytics platform for cloud-scale applications, including infrastructure, applications, services, and tools.

- [AWS Glue support for Datadog](https://docs.aws.amazon.com/glue/latest/dg/datadog-support.html): AWS Glue supports Datadog as follows:
- [IAM policies](https://docs.aws.amazon.com/glue/latest/dg/datadog-configuring-iam-permissions.html): The following sample policy describes the required AWS permissions for creating and using connections.
- [Configuring Datadog](https://docs.aws.amazon.com/glue/latest/dg/datadog-configuring.html): Before you can use AWS Glue to transfer from Datadog, you must meet the following requirements:
- [Configuring Datadog connections](https://docs.aws.amazon.com/glue/latest/dg/datadog-configuring-connections.html): Datadog supports custom authentication.
- [Reading from Datadog entities](https://docs.aws.amazon.com/glue/latest/dg/datadog-reading-from-entities.html): Prerequisites
- [Datadog connection options](https://docs.aws.amazon.com/glue/latest/dg/datadog-connection-options.html): The following are connection options for Datadog:
- [Creating a Datadog account](https://docs.aws.amazon.com/glue/latest/dg/datadog-create-account.html)
- [Limitations](https://docs.aws.amazon.com/glue/latest/dg/datadog-connector-limitations.html): The following are limitations for the Datadog connector:

### [Connecting to Docusign Monitor](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-data-docusign-monitor.html)

AWS Glue provides support for connecting to Docusign Monitor.

- [AWS Glue support for Docusign Monitor](https://docs.aws.amazon.com/glue/latest/dg/docusign-monitor-support.html): AWS Glue supports Docusign Monitor as follows:
- [IAM policies](https://docs.aws.amazon.com/glue/latest/dg/docusign-monitor-configuring-iam-permissions.html): The following sample policy describes the required AWS IAM permissions for creating and using connections.
- [Configuring Docusign Monitor](https://docs.aws.amazon.com/glue/latest/dg/docusign-monitor-configuring.html): Before you can use AWS Glue to transfer data from Docusign Monitor to supported destinations, you must meet these requirements:
- [Configuring Docusign Monitor connections](https://docs.aws.amazon.com/glue/latest/dg/docusign-monitor-configuring-connections.html): Docusign Monitor supports the AUTHORIZATION_CODE grant type.
- [Reading from Docusign Monitor entities](https://docs.aws.amazon.com/glue/latest/dg/docusign-monitor-reading-from-entities.html): Prerequisite
- [Docusign Monitor connection options](https://docs.aws.amazon.com/glue/latest/dg/docusign-monitor-connection-options.html): The following are connection options for Docusign Monitor:
- [Docusign Monitor limitations](https://docs.aws.amazon.com/glue/latest/dg/docusign-monitor-connection-limitations.html): The following are limitations or notes for Docusign Monitor:

### [Connecting to Domo](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-data-domo.html)

AWS Glue provides support for connecting to Domo.

- [AWS Glue support for Domo](https://docs.aws.amazon.com/glue/latest/dg/domo-support.html): AWS Glue supports Domo as follows:
- [IAM policies](https://docs.aws.amazon.com/glue/latest/dg/domo-configuring-iam-permissions.html): The following sample policy describes the required AWS IAM permissions for creating and using connections.
- [Configuring Domo](https://docs.aws.amazon.com/glue/latest/dg/domo-configuring.html): Before you can use AWS Glue to transfer data from Domo to supported destinations, you must meet these requirements:
- [Configuring Domo connections](https://docs.aws.amazon.com/glue/latest/dg/domo-configuring-connections.html): Domo supports the CLIENT_CREDENTIALS grant type for OAuth2.
- [Reading from Domo entities](https://docs.aws.amazon.com/glue/latest/dg/domo-reading-from-entities.html): Prerequisite
- [Domo connection options](https://docs.aws.amazon.com/glue/latest/dg/domo-connection-options.html): The following are connection options for Domo:
- [Domo limitations](https://docs.aws.amazon.com/glue/latest/dg/domo-connection-limitations.html): The following are limitations or notes for Domo:

### [Connecting to Dynatrace](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-data-dynatrace.html)

AWS Glue provides support for connecting to Dynatrace.

- [AWS Glue support for Dynatrace](https://docs.aws.amazon.com/glue/latest/dg/dynatrace-support.html): AWS Glue supports Dynatrace as follows:
- [IAM policies](https://docs.aws.amazon.com/glue/latest/dg/dynatrace-configuring-iam-permissions.html): The following sample policy describes the required AWS IAM permissions for creating and using connections.
- [Configuring Dynatrace](https://docs.aws.amazon.com/glue/latest/dg/dynatrace-configuring.html): Before you can use AWS Glue to transfer data from Dynatrace, you must meet these requirements:
- [Configuring Dynatrace connections](https://docs.aws.amazon.com/glue/latest/dg/dynatrace-configuring-connections.html): Dynatrace supports custom authentication.
- [Reading from Dynatrace entities](https://docs.aws.amazon.com/glue/latest/dg/dynatrace-reading-from-entities.html): Prerequisite
- [Dynatrace connection options](https://docs.aws.amazon.com/glue/latest/dg/dynatrace-connection-options.html): The following are connection options for Dynatrace:
- [Dynatrace limitations](https://docs.aws.amazon.com/glue/latest/dg/dynatrace-connection-limitations.html): The following are limitations or notes for Dynatrace:

### [Connecting to Facebook Ads](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-data-facebook-ads.html)

AWS Glue provides support for connecting to Facebook Ads.

- [AWS Glue support for Facebook Ads](https://docs.aws.amazon.com/glue/latest/dg/facebook-ads-support.html): AWS Glue supports Facebook Ads as follows:
- [IAM policies](https://docs.aws.amazon.com/glue/latest/dg/facebook-ads-configuring-iam-permissions.html): The following sample policy describes the required AWS IAM permissions for creating and using connections.
- [Configuring Facebook Ads](https://docs.aws.amazon.com/glue/latest/dg/facebook-ads-configuring.html): Before you can use AWS Glue to transfer data from Facebook Ads, you must meet these requirements:
- [Configuring Facebook Ads connections](https://docs.aws.amazon.com/glue/latest/dg/facebook-ads-configuring-connections.html): Facebook Ads supports the AUTHORIZATION_CODE grant type for OAuth2.
- [Reading from Facebook Ads entities](https://docs.aws.amazon.com/glue/latest/dg/facebook-ads-reading-from-entities.html): Prerequisite
- [Facebook Ads connection options](https://docs.aws.amazon.com/glue/latest/dg/facebook-ads-connection-options.html): The following are connection options for Facebook Ads:
- [Limitations and notes for Facebook Ads connector](https://docs.aws.amazon.com/glue/latest/dg/facebook-ads-connector-limitations.html): The following are limitations or notes for the Facebook Ads connector:

### [Connecting to Facebook Page Insights](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-data-facebook-page-insights.html)

AWS Glue provides support for connecting to Facebook Page Insights.

- [AWS Glue support for Facebook Page Insights](https://docs.aws.amazon.com/glue/latest/dg/facebook-page-insights-support.html): AWS Glue supports Facebook Page Insights as follows:
- [IAM policies](https://docs.aws.amazon.com/glue/latest/dg/facebook-page-insights-configuring-iam-permissions.html): The following sample policy describes the required AWS IAM permissions for creating and using connections.
- [Configuring Facebook Page Insights](https://docs.aws.amazon.com/glue/latest/dg/facebook-page-insights-configuring.html): Before you can use AWS Glue to transfer data from Facebook Page Insights, you must meet these requirements:
- [Configuring Facebook Page Insights connections](https://docs.aws.amazon.com/glue/latest/dg/facebook-page-insights-configuring-connections.html): To configure a Facebook Page Insights connection:
- [Reading from Facebook Page Insights entities](https://docs.aws.amazon.com/glue/latest/dg/facebook-page-insights-reading-from-entities.html): Prerequisite
- [Facebook Page Insights connection options](https://docs.aws.amazon.com/glue/latest/dg/facebook-page-insights-connection-options.html): The following are connection options for Facebook Page Insights:
- [Limitations and notes for Facebook Page Insights connector](https://docs.aws.amazon.com/glue/latest/dg/facebook-page-insights-connector-limitations.html): The following are limitations or notes for the Facebook Page Insights connector:

### [Connecting to Freshdesk](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-data-freshdesk.html)

AWS Glue provides support for connecting to Freshdesk.

- [AWS Glue support for Freshdesk](https://docs.aws.amazon.com/glue/latest/dg/freshdesk-support.html): AWS Glue supports Freshdesk as follows:
- [IAM policies](https://docs.aws.amazon.com/glue/latest/dg/freshdesk-configuring-iam-permissions.html): The following sample policy describes the required AWS IAM permissions for creating and using connections.
- [Configuring Freshdesk](https://docs.aws.amazon.com/glue/latest/dg/freshdesk-configuring.html): Before you can use AWS Glue to transfer data from Freshdesk, you must meet these requirements:
- [Configuring Freshdesk connections](https://docs.aws.amazon.com/glue/latest/dg/freshdesk-configuring-connections.html): Freshdesk supports custom authentication.
- [Reading from Freshdesk entities](https://docs.aws.amazon.com/glue/latest/dg/freshdesk-reading-from-entities.html): Prerequisite
- [Freshdesk connection options](https://docs.aws.amazon.com/glue/latest/dg/freshdesk-connection-options.html): The following are connection options for Freshdesk:
- [Limitations and notes for Freshdesk connector](https://docs.aws.amazon.com/glue/latest/dg/freshdesk-connector-limitations.html): The following are limitations or notes for the Freshdesk connector:

### [Connecting to Freshsales](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-data-freshsales.html)

AWS Glue provides support for connecting to Freshsales.

- [AWS Glue support for Freshsales](https://docs.aws.amazon.com/glue/latest/dg/freshsales-support.html): AWS Glue supports Freshsales as follows:
- [IAM policies](https://docs.aws.amazon.com/glue/latest/dg/freshsales-configuring-iam-permissions.html): The following sample policy describes the required AWS IAM permissions for creating and using connections.
- [Configuring Freshsales](https://docs.aws.amazon.com/glue/latest/dg/freshsales-configuring.html): Before you can use AWS Glue to transfer data from Freshsales, you must meet these requirements:
- [Configuring Freshsales connections](https://docs.aws.amazon.com/glue/latest/dg/freshsales-configuring-connections.html): Freshsales supports custom authentication.
- [Reading from Freshsales entities](https://docs.aws.amazon.com/glue/latest/dg/freshsales-reading-from-entities.html): Prerequisite
- [Freshsales connection options](https://docs.aws.amazon.com/glue/latest/dg/freshsales-connection-options.html): The following are connection options for Freshsales:
- [Freshsales limitations](https://docs.aws.amazon.com/glue/latest/dg/freshsales-connection-limitations.html): The following are limitations or notes for Freshsales:

### [Connecting to Google Ads](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-googleads.html)

If you're a Google Ads user, you can connect AWS Glue to your Google Ads account.

- [AWS Glue support for Google Ads](https://docs.aws.amazon.com/glue/latest/dg/googleads-support.html): AWS Glue supports Google Ads as follows:
- [IAM policies](https://docs.aws.amazon.com/glue/latest/dg/googleads-configuring-iam-permissions.html): The following sample policy describes the required AWS permissions for creating and using connections.
- [Configuring Google Ads](https://docs.aws.amazon.com/glue/latest/dg/googleads-configuring.html): Before you can use AWS Glue to transfer from Google Ads, you must meet these requirements:
- [Configuring Google Ads connections](https://docs.aws.amazon.com/glue/latest/dg/googleads-configuring-connections.html): Google Ads supports AUTHORIZATION_CODE grant type for OAuth2.
- [Reading from Google Ads entities](https://docs.aws.amazon.com/glue/latest/dg/googleads-reading-from-entities.html): Prerequisites
- [Google Ads connection options](https://docs.aws.amazon.com/glue/latest/dg/googleads-connection-options.html): The following are connection options for Google Ads:
- [Creating a Google Ads account](https://docs.aws.amazon.com/glue/latest/dg/googleads-create-account.html)
- [Limitations](https://docs.aws.amazon.com/glue/latest/dg/googleads-connector-limitations.html): The following are limitations for the Google Ads connector:

### [Connecting to Google Analytics 4](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-googleanalytics.html)

If you are a Google Analytics 4 user, you can connect AWS Glue to your Google Analytics 4 account.

- [AWS Glue support for Google Analytics 4](https://docs.aws.amazon.com/glue/latest/dg/googleanalytics-support.html): AWS Glue supports Google Analytics 4 as follows:
- [IAM policies](https://docs.aws.amazon.com/glue/latest/dg/googleanalytics-configuring-iam-permissions.html): The following sample policy describes the required AWS permissions for creating and using connections.
- [Configuring Google Analytics 4](https://docs.aws.amazon.com/glue/latest/dg/googleanalytics-configuring.html): Before you can use AWS Glue to transfer from Google Analytics 4, you must meet these requirements:
- [Configuring Google Analytics 4 connections](https://docs.aws.amazon.com/glue/latest/dg/googleanalytics-configuring-connections.html): To configure a Google Sheet connection:
- [Reading from Google Analytics 4 entities](https://docs.aws.amazon.com/glue/latest/dg/googleanalytics-reading-from-entities.html): Prerequisites
- [Google Analytics 4 connection options](https://docs.aws.amazon.com/glue/latest/dg/googleanalytics-connection-options.html): The following are connection options for Google Analytics 4:
- [Creating a Google Analytics 4 account](https://docs.aws.amazon.com/glue/latest/dg/googleanalytics-create-account.html): Follow the steps to create a Google Analytics 4 account: https://support.google.com/analytics/answer/9304153?hl=en
- [Steps to create a client app and OAuth 2.0 credentials](https://docs.aws.amazon.com/glue/latest/dg/googleanalytics-client-app-oauth-credentials.html): For more information, see Google Analytics4 API documentation .
- [Limitations and considerations](https://docs.aws.amazon.com/glue/latest/dg/googleanalytics-connector-limitations.html): The following are limitations for the Google Analytics 4 connector:

### [Connecting to Google BigQuery](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-data-bigquery.html)

AWS Glue provides built-in support for Google BigQuery.

- [Creating a BigQuery connection](https://docs.aws.amazon.com/glue/latest/dg/creating-bigquery-connection.html): To connect to Google BigQuery from AWS Glue, you will need to create and store your Google Cloud Platform credentials in a AWS Secrets Manager secret, then associate that secret with a Google BigQuery AWS Glue connection.
- [Creating a BigQuery source node](https://docs.aws.amazon.com/glue/latest/dg/creating-bigquery-source-node.html)
- [Creating a BigQuery target node](https://docs.aws.amazon.com/glue/latest/dg/creating-bigquery-target-node.html)

### [Connecting to Google Search Console](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-data-google-search-console.html)

AWS Glue provides support for connecting to Google Search Console.

- [AWS Glue support for Google Search Console](https://docs.aws.amazon.com/glue/latest/dg/google-search-console-support.html): AWS Glue supports Google Search Console as follows:
- [IAM policies](https://docs.aws.amazon.com/glue/latest/dg/google-search-console-configuring-iam-permissions.html): The following sample policy describes the required AWS IAM permissions for creating and using connections.
- [Configuring Google Search Console](https://docs.aws.amazon.com/glue/latest/dg/google-search-console-configuring.html): Before you can use AWS Glue to transfer data from Google Search Console, you must meet these requirements:
- [Configuring Google Search Console connections](https://docs.aws.amazon.com/glue/latest/dg/google-search-console-configuring-connections.html): Google Search Console supports the AUTHORIZATION_CODE grant type for OAuth2.
- [Reading from Google Search Console entities](https://docs.aws.amazon.com/glue/latest/dg/google-search-console-reading-from-entities.html): Prerequisite
- [Google Search Console connection options](https://docs.aws.amazon.com/glue/latest/dg/google-search-console-connection-options.html): The following are connection options for Google Search Console:
- [Google Search Console limitations](https://docs.aws.amazon.com/glue/latest/dg/google-search-console-limitations.html): The following are limitations or notes for Google Search Console:

### [Connecting to Google Sheets](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-googlesheets.html)

If you're a Google Sheets user, you can connect AWS Glue to your Google Sheets account.

- [AWS Glue support for Google Sheets](https://docs.aws.amazon.com/glue/latest/dg/googlesheets-support.html): AWS Glue supports Google Sheets as follows:
- [IAM policies](https://docs.aws.amazon.com/glue/latest/dg/googlesheets-configuring-iam-permissions.html): The following sample policy describes the required AWS permissions for creating and using connections.
- [Configuring Google Sheets](https://docs.aws.amazon.com/glue/latest/dg/googlesheets-configuring.html): Before you can use AWS Glue to transfer from Google Sheets, you must meet these requirements:
- [Configuring Google Sheets connections](https://docs.aws.amazon.com/glue/latest/dg/googlesheets-configuring-connections.html): To configure a Google Sheet connection:
- [Reading from Google Sheets entities](https://docs.aws.amazon.com/glue/latest/dg/googlesheets-reading-from-entities.html): Prerequisites
- [Google Sheets connection options](https://docs.aws.amazon.com/glue/latest/dg/googlesheets-connection-options.html): The following are connection options for Google Sheets:
- [Set up Authorization code OAuth flow for Google Sheets](https://docs.aws.amazon.com/glue/latest/dg/googlesheets-oauth-authorization.html): Prerequisites
- [Limitations for Google Sheets connector](https://docs.aws.amazon.com/glue/latest/dg/googlesheets-connector-limitations.html): The following are limitations for the Google Sheets connector:

### [Connecting to HubSpot](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-data-hubspot.html)

AWS Glue provides support for connecting to HubSpot.

- [AWS Glue support for HubSpot](https://docs.aws.amazon.com/glue/latest/dg/hubspot-support.html): AWS Glue supports HubSpot as follows:
- [IAM policies](https://docs.aws.amazon.com/glue/latest/dg/hubspot-configuring-iam-permissions.html): The following sample policy describes the required AWS IAM permissions for creating and using connections.
- [Configuring HubSpot](https://docs.aws.amazon.com/glue/latest/dg/hubspot-configuring.html): Before you can use AWS Glue to transfer data from HubSpot, you must meet these requirements:
- [Configuring HubSpot connections](https://docs.aws.amazon.com/glue/latest/dg/hubspot-configuring-connections.html): HubSpot supports the AUTHORIZATION_CODE grant type for OAuth2.
- [Reading from HubSpot entities](https://docs.aws.amazon.com/glue/latest/dg/hubspot-reading-from-entities.html): Prerequisite
- [Writing to HubSpot Entities](https://docs.aws.amazon.com/glue/latest/dg/hubspot-writing-to-entities.html)
- [HubSpot connection options](https://docs.aws.amazon.com/glue/latest/dg/hubspot-connection-options.html): The following are connection options for HubSpot:
- [Limitations and notes for HubSpot connector](https://docs.aws.amazon.com/glue/latest/dg/hubspot-connector-limitations.html): The following are limitations or notes for the HubSpot connector:

### [Connecting to Instagram Ads](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-data-instagram-ads.html)

AWS Glue provides support for connecting to Instagram Ads.

- [AWS Glue support for Instagram Ads](https://docs.aws.amazon.com/glue/latest/dg/instagram-ads-support.html): AWS Glue supports Instagram Ads as follows:
- [IAM policies](https://docs.aws.amazon.com/glue/latest/dg/instagram-ads-configuring-iam-permissions.html): The following sample policy describes the required AWS IAM permissions for creating and using connections.
- [Configuring Instagram Ads](https://docs.aws.amazon.com/glue/latest/dg/instagram-ads-configuring.html): Before you can use AWS Glue to transfer data from Instagram Ads, you must meet these requirements:
- [Configuring Instagram Ads connections](https://docs.aws.amazon.com/glue/latest/dg/instagram-ads-configuring-connections.html): Instagram Ads supports the AUTHORIZATION_CODE grant type for OAuth2.
- [Reading from Instagram Ads entities](https://docs.aws.amazon.com/glue/latest/dg/instagram-ads-reading-from-entities.html): Prerequisite
- [Instagram Ads connection options](https://docs.aws.amazon.com/glue/latest/dg/instagram-ads-connection-options.html): The following are connection options for Instagram Ads:
- [Limitations and notes for Instagram Ads connector](https://docs.aws.amazon.com/glue/latest/dg/instagram-ads-connector-limitations.html): The following are limitations or notes for the Instagram Ads connector:

### [Connecting to Intercom](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-data-intercom.html)

AWS Glue provides support for connecting to Intercom.

- [AWS Glue support for Intercom](https://docs.aws.amazon.com/glue/latest/dg/intercom-support.html): AWS Glue supports Intercom as follows:
- [IAM policies](https://docs.aws.amazon.com/glue/latest/dg/intercom-configuring-iam-permissions.html): The following sample policy describes the required IAM permissions for creating and using connections.
- [Configuring Intercom](https://docs.aws.amazon.com/glue/latest/dg/intercom-configuring.html): Before you can use AWS Glue to transfer from Intercom, you must meet these requirements:
- [Configuring Intercom connections](https://docs.aws.amazon.com/glue/latest/dg/intercom-configuring-connections.html): Intercom supports the AUTHORIZATION_CODE grant type for OAuth 2.
- [Reading from Intercom entities](https://docs.aws.amazon.com/glue/latest/dg/intercom-reading-from-entities.html): Prerequisites
- [Intercom connection options](https://docs.aws.amazon.com/glue/latest/dg/intercom-connection-options.html): The following are connection options for Intercom:
- [Limitations](https://docs.aws.amazon.com/glue/latest/dg/intercom-limitations.html): The following are limitations for the Intercom connector:
- [Creating a new Intercom account and configuring the client app](https://docs.aws.amazon.com/glue/latest/dg/intercom-new-account-creation.html)

### [Connecting to Jira Cloud](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-data-jira-cloud.html)

AWS Glue provides support for connecting to Jira Cloud.

- [AWS Glue support for Jira Cloud](https://docs.aws.amazon.com/glue/latest/dg/jira-cloud-support.html): AWS Glue supports Jira Cloud as follows:
- [IAM policies](https://docs.aws.amazon.com/glue/latest/dg/jira-cloud-configuring-iam-permissions.html): The following sample policy describes the required AWS IAM permissions for creating and using connections.
- [Configuring Jira Cloud](https://docs.aws.amazon.com/glue/latest/dg/jira-cloud-configuring.html): Before you can use AWS Glue to transfer data from Jira Cloud to supported destinations, you must meet these requirements:
- [Configuring Jira Cloud connections](https://docs.aws.amazon.com/glue/latest/dg/jira-cloud-configuring-connections.html): Jira Cloud supports the AUTHORIZATION_CODE grant type for OAuth2.
- [Reading from Jira Cloud entities](https://docs.aws.amazon.com/glue/latest/dg/jira-cloud-reading-from-entities.html): Prerequisite
- [Jira Cloud connection options](https://docs.aws.amazon.com/glue/latest/dg/jira-cloud-connection-options.html): The following are connection options for Jira Cloud:
- [Limitations and notes for Jira Cloud connector](https://docs.aws.amazon.com/glue/latest/dg/jira-cloud-connector-limitations.html): The following are limitations or notes for the Jira Cloud connector:

### [Connecting to Kustomer](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-data-kustomer.html)

AWS Glue provides support for connecting to Kustomer.

- [AWS Glue support for Kustomer](https://docs.aws.amazon.com/glue/latest/dg/kustomer-support.html): AWS Glue supports Kustomer as follows:
- [IAM policies](https://docs.aws.amazon.com/glue/latest/dg/kustomer-configuring-iam-permissions.html): The following sample policy describes the required AWS IAM permissions for creating and using connections.
- [Configuring Kustomer](https://docs.aws.amazon.com/glue/latest/dg/kustomer-configuring.html): Before you can use AWS Glue to transfer data from Kustomer to supported destinations, you must meet these requirements:
- [Configuring Kustomer connections](https://docs.aws.amazon.com/glue/latest/dg/kustomer-configuring-connections.html): To configure a Kustomer connection:
- [Reading from Kustomer entities](https://docs.aws.amazon.com/glue/latest/dg/kustomer-reading-from-entities.html): Prerequisite
- [Kustomer connection options](https://docs.aws.amazon.com/glue/latest/dg/kustomer-connection-options.html): The following are connection options for Kustomer:
- [Kustomer limitations](https://docs.aws.amazon.com/glue/latest/dg/kustomer-connection-limitations.html): The following are limitations or notes for Kustomer:

### [Connecting to LinkedIn](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-linkedin.html)

LinkedIn is a paid marketing tool that offers access to LinkedIn social networks through various sponsored posts and other methods.

- [AWS Glue support for LinkedIn](https://docs.aws.amazon.com/glue/latest/dg/linkedin-support.html): AWS Glue supports LinkedIn as follows:
- [IAM policies](https://docs.aws.amazon.com/glue/latest/dg/linkedin-configuring-iam-permissions.html): The following sample policy describes the required AWS permissions for creating and using connections.
- [Configuring LinkedIn](https://docs.aws.amazon.com/glue/latest/dg/linkedin-configuring.html): Before you can use AWS Glue to transfer from LinkedIn, you must meet the following requirements:
- [Configuring LinkedIn connections](https://docs.aws.amazon.com/glue/latest/dg/linkedin-configuring-connections.html): LinkedIn supports AUTHORIZATION_CODE grant type for OAuth2.
- [Reading from LinkedIn entities](https://docs.aws.amazon.com/glue/latest/dg/linkedin-reading-from-entities.html): Prerequisites
- [LinkedIn connection options](https://docs.aws.amazon.com/glue/latest/dg/linkedin-connection-options.html): The following are connection options for LinkedIn:
- [Creating a LinkedIn account](https://docs.aws.amazon.com/glue/latest/dg/linkedin-create-account.html)
- [Limitations](https://docs.aws.amazon.com/glue/latest/dg/linkedin-connector-limitations.html): For the Analytics fieldsad_analytics_all_adAccounts, ad_analytics_all_campaigns, ad_analytics_all_campaign_groups, and ad_analytics_all_adCreatives a filter is mandatory to retrieve the records.

### [Connecting to Mailchimp](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-mailchimp.html)

Mailchimp is an all-in-one marketing platform that helps you manage and talk to your clients, customers, and other interested parties.

- [AWS Glue support for Mailchimp](https://docs.aws.amazon.com/glue/latest/dg/mailchimp-support.html): AWS Glue supports Mailchimp as follows:
- [IAM policies](https://docs.aws.amazon.com/glue/latest/dg/mailchimp-configuring-iam-permissions.html): The following sample policy describes the required AWS permissions for creating and using connections.
- [Configuring Mailchimp](https://docs.aws.amazon.com/glue/latest/dg/mailchimp-configuring.html): Before you can use AWS Glue to transfer from Mailchimp, you must meet the following requirements:
- [Configuring Mailchimp connections](https://docs.aws.amazon.com/glue/latest/dg/mailchimp-configuring-connections.html): Mailchimp supports following two types for authentication mechanism:
- [Reading from Mailchimp entities](https://docs.aws.amazon.com/glue/latest/dg/mailchimp-reading-from-entities.html): Prerequisites
- [Mailchimp connection options](https://docs.aws.amazon.com/glue/latest/dg/mailchimp-connection-options.html): The following are connection options for Mailchimp:
- [Creating an Mailchimp account](https://docs.aws.amazon.com/glue/latest/dg/mailchimp-create-account.html)
- [Limitations](https://docs.aws.amazon.com/glue/latest/dg/mailchimp-connector-limitations.html): The following are limitations for the Mailchimp connector:

### [Connecting to Microsoft Dynamics 365 CRM](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-microsoft-dynamics-365.html)

Microsoft Dynamics 365 is a product line of enterprise resource planning and customer relationship management intelligent business applications.

- [AWS Glue support for Microsoft Dynamics 365](https://docs.aws.amazon.com/glue/latest/dg/microsoft-dynamics-365-support.html): AWS Glue supports Microsoft Dynamics 365 as follows:
- [IAM policies](https://docs.aws.amazon.com/glue/latest/dg/microsoft-dynamics-365-configuring-iam-permissions.html): The following sample policy describes the required AWS permissions for creating and using connections.
- [Configuring Microsoft Dynamics 365 CRM](https://docs.aws.amazon.com/glue/latest/dg/microsoft-dynamics-365-configuring.html): Before you can use AWS Glue to transfer data from Microsoft Dynamics 365 CRM, you must meet these requirements:
- [Configuring Microsoft Dynamics 365 CRM connections](https://docs.aws.amazon.com/glue/latest/dg/microsoft-dynamics-365-configuring-connections.html): AUTHORIZATION_CODE Grant Type
- [Reading from Microsoft Dynamics 365 CRM entities](https://docs.aws.amazon.com/glue/latest/dg/microsoft-dynamics-365-reading-from-entities.html): Prerequisites
- [Microsoft Dynamics 365 CRM connection option reference](https://docs.aws.amazon.com/glue/latest/dg/microsoft-dynamics-365-connection-options.html): The following are connection options for Microsoft Dynamics 365 CRM:
- [Limitations](https://docs.aws.amazon.com/glue/latest/dg/microsoft-dynamics-365-connector-limitations.html): The following are limitations for the Microsoft Dynamics 365 CRM connector:

### [Connecting to Microsoft Teams](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-microsoft-teams.html)

Microsoft Teams is a collaborative workspace within Microsoft 365 that acts as a central hub for workplace conversations, collaborative teamwork, video chats and document sharing, all designed to aid worker productivity in a unified suite of tools.

- [AWS Glue support for Microsoft Teams](https://docs.aws.amazon.com/glue/latest/dg/microsoft-teams-support.html): AWS Glue supports Microsoft Teams as follows:
- [IAM policies](https://docs.aws.amazon.com/glue/latest/dg/microsoft-teams-configuring-iam-permissions.html): The following sample policy describes the required AWS permissions for creating and using connections.
- [Configuring Microsoft Teams](https://docs.aws.amazon.com/glue/latest/dg/microsoft-teams-configuring.html): Before you can use AWS Glue to transfer data from Microsoft Teams, you must meet these requirements:
- [Configuring Microsoft Teams connections](https://docs.aws.amazon.com/glue/latest/dg/microsoft-teams-configuring-connections.html): Microsoft Teams supports following two types for authentication mechanism:
- [Reading from Microsoft Teams entities](https://docs.aws.amazon.com/glue/latest/dg/microsoft-teams-reading-from-entities.html): Prerequisites
- [Microsoft Teams connection option reference](https://docs.aws.amazon.com/glue/latest/dg/microsoft-teams-connection-options.html): The following are connection options for Microsoft Teams:
- [Limitations](https://docs.aws.amazon.com/glue/latest/dg/microsoft-teams-connector-limitations.html): The following are limitations for the Microsoft Teams connector:

### [Connecting to Mixpanel](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-mixpanel.html)

Mixpanel is a powerful real-time analytics platform that helps companies measure and optimize user engagement.

- [AWS Glue support for Mixpanel](https://docs.aws.amazon.com/glue/latest/dg/Mixpanel-support.html): AWS Glue supports Mixpanel as follows:
- [IAM policies](https://docs.aws.amazon.com/glue/latest/dg/mixpanel-configuring-iam-permissions.html): The following sample policy describes the required AWS permissions for creating and using connections.
- [Configuring Mixpanel](https://docs.aws.amazon.com/glue/latest/dg/mixpanel-configuring.html): Before you can use AWS Glue to transfer from Mixpanel, you must meet these requirements:
- [Configuring Mixpanel connections](https://docs.aws.amazon.com/glue/latest/dg/mixpanel-configuring-connections.html): Mixpanel supports username and password for BasicAuth.
- [Reading from Mixpanel entities](https://docs.aws.amazon.com/glue/latest/dg/mixpanel-reading-from-entities.html): Prerequisites
- [Mixpanel connection options](https://docs.aws.amazon.com/glue/latest/dg/mixpanel-connection-options.html): The following are connection options for Mixpanel:
- [Creating a Mixpanel account and configuring the client app](https://docs.aws.amazon.com/glue/latest/dg/mixpanel-create-account.html)
- [Limitations](https://docs.aws.amazon.com/glue/latest/dg/mixpanel-connector-limitations.html): The following are limitations for the Mixpanel connector:

### [Connecting to Monday](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-monday.html)

Monday.com is a versatile work operating system that streamlines project management and team collaboration.

- [AWS Glue support for Monday](https://docs.aws.amazon.com/glue/latest/dg/monday-support.html): AWS Glue supports Monday as follows:
- [IAM policies](https://docs.aws.amazon.com/glue/latest/dg/monday-configuring-iam-permissions.html): The following sample policy describes the required AWS permissions for creating and using connections.
- [Configuring Monday](https://docs.aws.amazon.com/glue/latest/dg/monday-configuring.html): Before you can use AWS Glue to transfer data from Monday, you must meet these requirements:
- [Configuring Monday connections](https://docs.aws.amazon.com/glue/latest/dg/monday-configuring-connections.html): Monday supports following two types for authentication mechanism:
- [Reading from Monday entities](https://docs.aws.amazon.com/glue/latest/dg/monday-reading-from-entities.html): Prerequisites
- [Monday connection option reference](https://docs.aws.amazon.com/glue/latest/dg/monday-connection-options.html): The following are connection options for Monday:
- [Limitations](https://docs.aws.amazon.com/glue/latest/dg/monday-connector-limitations.html): The following are limitations for the Monday connector:

### [Connecting to MongoDB](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-data-mongodb.html)

AWS Glue provides built-in support for MongoDB.

- [Creating a MongoDB connection](https://docs.aws.amazon.com/glue/latest/dg/creating-mongodb-connection.html): Prerequisites:
- [Creating a MongoDB source node](https://docs.aws.amazon.com/glue/latest/dg/creating-mongodb-source-node.html)
- [Creating a MongoDB target node](https://docs.aws.amazon.com/glue/latest/dg/creating-mongodb-target-node.html)

### [Connecting to Oracle NetSuite](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-data-oracle-netsuite.html)

AWS Glue provides support for connecting to Oracle NetSuite.

- [AWS Glue support for Oracle NetSuite](https://docs.aws.amazon.com/glue/latest/dg/oracle-netsuite-support.html): AWS Glue supports Oracle NetSuite as follows:
- [IAM policies](https://docs.aws.amazon.com/glue/latest/dg/oracle-netsuite-configuring-iam-permissions.html): The following sample policy describes the required AWS IAM permissions for creating and using connections.
- [Configuring Oracle NetSuite](https://docs.aws.amazon.com/glue/latest/dg/oracle-netsuite-configuring.html): Before you can use AWS Glue to transfer data from Oracle NetSuite, you must meet these requirements:
- [Configuring Oracle NetSuite connections](https://docs.aws.amazon.com/glue/latest/dg/oracle-netsuite-configuring-connections.html): Oracle NetSuite supports the AUTHORIZATION_CODE grant type for OAuth2.
- [Reading from Oracle NetSuite entities](https://docs.aws.amazon.com/glue/latest/dg/oracle-netsuite-reading-from-entities.html): Prerequisite
- [Oracle NetSuite connection options](https://docs.aws.amazon.com/glue/latest/dg/oracle-netsuite-connection-options.html): The following are connection options for Oracle NetSuite:
- [Limitations and notes for Oracle NetSuite connector](https://docs.aws.amazon.com/glue/latest/dg/oracle-netsuite-connector-limitations.html): The following are limitations or notes for the Oracle NetSuite connector:

### [Connecting to OpenSearch Service](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-data-opensearch.html)

AWS Glue provides built-in support for Amazon OpenSearch Service.

- [Creating a OpenSearch Service connection](https://docs.aws.amazon.com/glue/latest/dg/creating-opensearch-connection.html): Prerequisites:
- [Creating a OpenSearch Service source node](https://docs.aws.amazon.com/glue/latest/dg/creating-opensearch-source-node.html)
- [Creating a OpenSearch Service target node](https://docs.aws.amazon.com/glue/latest/dg/creating-opensearch-target-node.html)

### [Connecting to Okta](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-okta.html)

Okta is an identity and access management solution.

- [AWS Glue support for Okta](https://docs.aws.amazon.com/glue/latest/dg/okta-support.html): AWS Glue supports Okta as follows:
- [IAM policies](https://docs.aws.amazon.com/glue/latest/dg/okta-configuring-iam-permissions.html): The following sample policy describes the required AWS permissions for creating and using connections.
- [Configuring Okta](https://docs.aws.amazon.com/glue/latest/dg/okta-configuring.html): Before you can use AWS Glue to transfer data to or from Okta, you must meet these requirements:
- [Configuring Okta connections](https://docs.aws.amazon.com/glue/latest/dg/okta-configuring-connections.html): Okta supports two types of authentication mechanisms:
- [Reading from Okta entities](https://docs.aws.amazon.com/glue/latest/dg/okta-reading-from-entities.html): Prerequisites
- [Okta connection option reference](https://docs.aws.amazon.com/glue/latest/dg/okta-connection-options.html): The following are connection options for Okta:
- [Okta New Account and Developer App creation steps](https://docs.aws.amazon.com/glue/latest/dg/okta-create-account.html): Create a developer account on Okta for getting access to the Okta API.
- [Limitations](https://docs.aws.amazon.com/glue/latest/dg/okta-connector-limitations.html): The following are limitations for the Okta connector:

### [Connecting to PayPal](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-data-paypal.html)

AWS Glue provides support for connecting to PayPal.

- [AWS Glue support for PayPal](https://docs.aws.amazon.com/glue/latest/dg/paypal-support.html): AWS Glue supports PayPal as follows:
- [IAM policies](https://docs.aws.amazon.com/glue/latest/dg/paypal-configuring-iam-permissions.html): The following sample policy describes the required AWS IAM permissions for creating and using connections.
- [Configuring PayPal](https://docs.aws.amazon.com/glue/latest/dg/paypal-configuring.html): Before you can use AWS Glue to transfer data from PayPal, you must meet these requirements:
- [Configuring PayPal connections](https://docs.aws.amazon.com/glue/latest/dg/paypal-configuring-connections.html): PayPal supports the CLIENT CREDENTIALS grant type for OAuth2.
- [Reading from PayPal entities](https://docs.aws.amazon.com/glue/latest/dg/paypal-reading-from-entities.html): Prerequisite
- [PayPal connection options](https://docs.aws.amazon.com/glue/latest/dg/paypal-connection-options.html): The following are connection options for PayPal:
- [Limitations and notes for PayPal connector](https://docs.aws.amazon.com/glue/latest/dg/paypal-connector-limitations.html): The following are limitations or notes for the PayPal connector:

### [Connecting to Pendo](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-pendo.html)

Pendo provides a rich data store for user interaction data.

- [AWS Glue support for Pendo](https://docs.aws.amazon.com/glue/latest/dg/pendo-support.html): AWS Glue supports Pendo as follows:
- [IAM policies](https://docs.aws.amazon.com/glue/latest/dg/pendo-configuring-iam-permissions.html): The following sample policy describes the required AWS permissions for creating and using connections.
- [Configuring Pendo](https://docs.aws.amazon.com/glue/latest/dg/pendo-configuring.html): Before you can use AWS Glue to transfer from Pendo, you must meet the following requirements:
- [Configuring Pendo connections](https://docs.aws.amazon.com/glue/latest/dg/pendo-configuring-connections.html): Pendo supports custom authentication.
- [Reading from Pendo entities](https://docs.aws.amazon.com/glue/latest/dg/pendo-reading-from-entities.html): Prerequisites
- [Pendo connection options](https://docs.aws.amazon.com/glue/latest/dg/pendo-connection-options.html): The following are connection options for Pendo:
- [Limitations](https://docs.aws.amazon.com/glue/latest/dg/pendo-connector-limitations.html): The following are limitations for the Pendo connector:

### [Connecting to Pipedrive](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-pipedrive.html)

Pipedrive is a sales pipeline CRM designed to help small businesses manage leads, track sales activities and close more deals.

- [AWS Glue support for Pipedrive](https://docs.aws.amazon.com/glue/latest/dg/pipedrive-support.html): AWS Glue supports Pipedrive as follows:
- [IAM policies](https://docs.aws.amazon.com/glue/latest/dg/pipedrive-configuring-iam-permissions.html): The following sample policy describes the required AWS permissions for creating and using connections.
- [Configuring Pipedrive](https://docs.aws.amazon.com/glue/latest/dg/pipedrive-configuring.html): Before you can use AWS Glue to transfer data from Pipedrive, you must meet these requirements:
- [Configuring Pipedrive connections](https://docs.aws.amazon.com/glue/latest/dg/pipedrive-configuring-connections.html): Pipedrive supports AUTHORIZATION_CODE grant type for OAuth2.
- [Reading from Pipedrive entities](https://docs.aws.amazon.com/glue/latest/dg/pipedrive-reading-from-entities.html): Prerequisites
- [Pipedrive connection option reference](https://docs.aws.amazon.com/glue/latest/dg/pipedrive-connection-options.html): The following are connection options for Pipedrive:
- [Limitations](https://docs.aws.amazon.com/glue/latest/dg/pipedrive-connector-limitations.html): The following are limitations for the Pipedrive connector:

### [Connecting to Productboard](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-productboard.html)

Productboard is the product management system that helps product teams get the right products to market, faster.

- [AWS Glue support for Productboard](https://docs.aws.amazon.com/glue/latest/dg/productboard-support.html): AWS Glue supports Productboard as follows:
- [IAM policies](https://docs.aws.amazon.com/glue/latest/dg/productboard-configuring-iam-permissions.html): The following sample policy describes the required AWS permissions for creating and using connections.
- [Configuring Productboard](https://docs.aws.amazon.com/glue/latest/dg/productboard-configuring.html): Before you can use AWS Glue to transfer from Productboard, you must meet the following requirements:
- [Configuring Productboard connections](https://docs.aws.amazon.com/glue/latest/dg/productboard-configuring-connections.html)
- [Reading from Productboard entities](https://docs.aws.amazon.com/glue/latest/dg/productboard-reading-from-entities.html): Prerequisites
- [Productboard connection options](https://docs.aws.amazon.com/glue/latest/dg/productboard-connection-options.html): The following are connection options for Productboard:
- [Creating an Productboard account](https://docs.aws.amazon.com/glue/latest/dg/productboard-create-account.html)
- [Limitations](https://docs.aws.amazon.com/glue/latest/dg/productboard-connector-limitations.html): The following are limitations for the Productboard connector:

### [Connecting to QuickBooks](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-data-quickbooks.html)

AWS Glue provides support for connecting to QuickBooks.

- [AWS Glue support for QuickBooks](https://docs.aws.amazon.com/glue/latest/dg/quickbooks-support.html): AWS Glue supports QuickBooks as follows:
- [IAM policies](https://docs.aws.amazon.com/glue/latest/dg/quickbooks-configuring-iam-permissions.html): The following sample policy describes the required AWS IAM permissions for creating and using connections.
- [Configuring QuickBooks](https://docs.aws.amazon.com/glue/latest/dg/quickbooks-configuring.html): Before you can use AWS Glue to transfer data from QuickBooks, you must meet these requirements:
- [Configuring QuickBooks connections](https://docs.aws.amazon.com/glue/latest/dg/quickbooks-configuring-connections.html): QuickBooks supports the AUTHORIZATION_CODE grant type for OAuth2.
- [Reading from QuickBooks entities](https://docs.aws.amazon.com/glue/latest/dg/quickbooks-reading-from-entities.html): Prerequisite
- [QuickBooks connection options](https://docs.aws.amazon.com/glue/latest/dg/quickbooks-connection-options.html): The following are connection options for QuickBooks:
- [Limitations and notes for QuickBooks connector](https://docs.aws.amazon.com/glue/latest/dg/quickbooks-connector-limitations.html): The following are limitations or notes for the QuickBooks connector:

### [Connecting to a REST API](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-data-rest-api.html)

AWS Glue provides support for connecting to a REST API.

- [AWS Glue support for REST API](https://docs.aws.amazon.com/glue/latest/dg/rest-api-support.html): AWS Glue supports REST API as follows:
- [IAM policies](https://docs.aws.amazon.com/glue/latest/dg/rest-api-configuring-iam-permissions.html): The following sample IAM policy describes the required permissions for registering, creating, managing and using the REST API connections within AWS Glue ETL jobs.
- [Configuring a REST API ConnectionType](https://docs.aws.amazon.com/glue/latest/dg/rest-api-configuring.html): Before you can use AWS Glue to transfer data from the REST API-based data source, you must meet these requirements:
- [Configuring a REST API connection](https://docs.aws.amazon.com/glue/latest/dg/rest-api-configuring-connections.html): In order to configure an AWS Glue REST API connector, you need to configure an AWS Glue connection type.
- [Tutorial: Creating a REST API ConnectionType and Connection](https://docs.aws.amazon.com/glue/latest/dg/rest-api-example.html): Connecting to the Foo REST API
- [Limitations](https://docs.aws.amazon.com/glue/latest/dg/rest-api-limitations.html): The following are limitations for the REST API connector

### [Connecting to Salesforce](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-data-salesforce.html)

AWS Glue provides support for connecting to Salesforce.

- [AWS Glue support for Salesforce](https://docs.aws.amazon.com/glue/latest/dg/salesforce-support.html): AWS Glue supports Salesforce as follows:
- [IAM policies](https://docs.aws.amazon.com/glue/latest/dg/salesforce-configuring-iam-permissions.html): The following sample IAM policy describes the required permissions for creating, managing and using Salesforce connections within AWS Glue ETL jobs.
- [Configuring Salesforce](https://docs.aws.amazon.com/glue/latest/dg/salesforce-configuring.html): Before you can use AWS Glue to transfer data to or from Salesforce, you must meet these requirements:
- [Configuring Salesforce connections](https://docs.aws.amazon.com/glue/latest/dg/salesforce-configuring-connections.html): To configure a Salesforce connection:
- [Reading from Salesforce](https://docs.aws.amazon.com/glue/latest/dg/salesforce-reading-from-entities.html): Prerequisite
- [Writing to Salesforce](https://docs.aws.amazon.com/glue/latest/dg/salesforce-writing-to.html): Prerequisites
- [Salesforce connection options](https://docs.aws.amazon.com/glue/latest/dg/salesforce-connection-options.html): The following connection options are supported for the Salesforce connector:
- [Limitations for the Salesforce connector](https://docs.aws.amazon.com/glue/latest/dg/salesforce-connector-limitations.html): The following are limitations for the Salesforce connector:
- [Set up the Authorization Code flow for Salesforce](https://docs.aws.amazon.com/glue/latest/dg/salesforce-setup-authorization-code-flow.html): Refer to Salesforce public documentation for enabling the OAuth 2.0 Authorization Code flow.
- [Set up the JWT bearer OAuth flow for Salesforce](https://docs.aws.amazon.com/glue/latest/dg/salesforce-setup-jwt-bearer-oauth.html): Refer to Salesforce public documentation for enabling server-to-server integration with OAuth 2.0 JSON Web Tokens.

### [Connecting to Salesforce Marketing Cloud](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-data-salesforce-marketing-cloud.html)

AWS Glue provides support for connecting to Salesforce Marketing Cloud.

- [AWS Glue support for Salesforce Marketing Cloud](https://docs.aws.amazon.com/glue/latest/dg/salesforce-marketing-cloud-support.html): AWS Glue supports Salesforce Marketing Cloud as follows:
- [IAM policies](https://docs.aws.amazon.com/glue/latest/dg/salesforce-marketing-cloud-configuring-iam-permissions.html): The following sample policy describes the required AWS IAM permissions for creating and using connections.
- [Configuring Salesforce Marketing Cloud](https://docs.aws.amazon.com/glue/latest/dg/salesforce-marketing-cloud-configuring.html): Before you can use AWS Glue to transfer data from Salesforce Marketing Cloud, you must meet these requirements:
- [Configuring Salesforce Marketing Cloud connections](https://docs.aws.amazon.com/glue/latest/dg/salesforce-marketing-cloud-configuring-connections.html): Salesforce Marketing Cloud supports the CLIENT CREDENTIALS grant type for OAuth2.
- [Reading from Salesforce Marketing Cloud entities](https://docs.aws.amazon.com/glue/latest/dg/salesforce-marketing-cloud-reading-from-entities.html): Prerequisite
- [Writing to Salesforce Marketing Cloud entities](https://docs.aws.amazon.com/glue/latest/dg/salesforce-marketing-cloud-writing-to-entities.html): Prerequisites
- [Salesforce Marketing Cloud connection options](https://docs.aws.amazon.com/glue/latest/dg/salesforce-marketing-cloud-connection-options.html): The following are connection options for Salesforce Marketing Cloud:
- [Limitations and notes for Salesforce Marketing Cloud connector](https://docs.aws.amazon.com/glue/latest/dg/salesforce-marketing-cloud-connector-limitations.html): The following are limitations or notes for the Salesforce Marketing Cloud connector:

### [Connecting to Salesforce Commerce Cloud](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-salesforce-commerce-cloud.html)

The B2C Commerce API is a collection of RESTful APIs for interacting with B2C Commerce instances.

- [AWS Glue support for Salesforce Commerce Cloud](https://docs.aws.amazon.com/glue/latest/dg/salesforce-commerce-cloud-support.html): AWS Glue supports Salesforce Commerce Cloud as follows:
- [IAM policies](https://docs.aws.amazon.com/glue/latest/dg/salesforce-commerce-cloud-configuring-iam-permissions.html): The following sample policy describes the required AWS permissions for creating and using connections.
- [Configuring Salesforce Commerce Cloud](https://docs.aws.amazon.com/glue/latest/dg/salesforce-commerce-cloud-configuring.html): Before you can use AWS Glue to transfer data from Salesforce Commerce Cloud, you must meet these requirements:
- [Configuring Salesforce Commerce Cloud connections](https://docs.aws.amazon.com/glue/latest/dg/salesforce-commerce-cloud-configuring-connections.html): Salesforce Commerce Cloud supports CLIENT CREDENTIALS grant type for OAuth2.
- [Reading from Salesforce Commerce Cloud entities](https://docs.aws.amazon.com/glue/latest/dg/salesforce-commerce-cloud-reading-from-entities.html): Prerequisites
- [Salesforce Commerce Cloud connection option reference](https://docs.aws.amazon.com/glue/latest/dg/salesforce-commerce-cloud-connection-options.html): The following are connection options for Salesforce Commerce Cloud:
- [Limitations](https://docs.aws.amazon.com/glue/latest/dg/salesforce-commerce-cloud-connector-limitations.html): The following are limitations for the Salesforce Commerce Cloud connector:

### [Connecting to Salesforce Marketing Cloud Account Engagement](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-data-salesforce-marketing-cloud-account-engagement.html)

AWS Glue provides support for connecting to Salesforce Marketing Cloud Account Engagement.

- [AWS Glue support for Salesforce Marketing Cloud Account Engagement](https://docs.aws.amazon.com/glue/latest/dg/salesforce-marketing-cloud-account-engagement-support.html): AWS Glue supports Salesforce Marketing Cloud Account Engagement as follows:
- [IAM policies](https://docs.aws.amazon.com/glue/latest/dg/salesforce-marketing-cloud-account-engagement-configuring-iam-permissions.html): The following sample policy describes the required AWS IAM permissions for creating and using connections.
- [Configuring Salesforce Marketing Cloud Account Engagement](https://docs.aws.amazon.com/glue/latest/dg/salesforce-marketing-cloud-account-engagement-configuring.html): Before you can use AWS Glue to transfer data from Salesforce Marketing Cloud Account Engagement, you must meet these requirements:
- [Configuring Salesforce Marketing Cloud Account Engagement connections](https://docs.aws.amazon.com/glue/latest/dg/salesforce-marketing-cloud-account-engagement-configuring-connections.html): The grant type determines how AWS Glue communicates with Salesforce Marketing Cloud Account Engagement to request access to your data.
- [Reading from Salesforce Marketing Cloud Account Engagement entities](https://docs.aws.amazon.com/glue/latest/dg/salesforce-marketing-cloud-account-engagement-reading-from-entities.html): Prerequisite
- [Salesforce Marketing Cloud Account Engagement connection options](https://docs.aws.amazon.com/glue/latest/dg/salesforce-marketing-cloud-account-engagement-connection-options.html): The following are connection options for Salesforce Marketing Cloud Account Engagement:
- [Limitations and notes for Salesforce Marketing Cloud Account Engagement connector](https://docs.aws.amazon.com/glue/latest/dg/salesforce-marketing-cloud-account-engagement-connector-limitations.html): The following notes and limitations apply:

### [Connecting to SAP HANA](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-data-saphana.html)

AWS Glue provides built-in support for SAP HANA.

- [Creating a SAP HANA connection](https://docs.aws.amazon.com/glue/latest/dg/creating-saphana-connection.html): To connect to SAP HANA from AWS Glue, you will need to create and store your SAP HANA credentials in a AWS Secrets Manager secret, then associate that secret with a SAP HANA AWS Glue connection.
- [Creating a SAP HANA source node](https://docs.aws.amazon.com/glue/latest/dg/creating-saphana-source-node.html)
- [Creating a SAP HANA target node](https://docs.aws.amazon.com/glue/latest/dg/creating-saphana-target-node.html)

### [Connecting to SAP OData](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-data-sap-odata.html)

AWS Glue provides support for connecting to SAP OData.

### [AWS Glue support for SAP OData](https://docs.aws.amazon.com/glue/latest/dg/sap-odata-support.html)

AWS Glue supports SAP OData as follows:

### [Prerequisites](https://docs.aws.amazon.com/glue/latest/dg/sap-odata-prerequisites.html)

Prior to initiating an AWS Glue job for data extraction from SAP OData using the SAP OData connection, complete the following prerequisites:

- [SAP OData activation](https://docs.aws.amazon.com/glue/latest/dg/sap-odata-activation.html): Complete the following steps for SAP OData connection:
- [IAM policies](https://docs.aws.amazon.com/glue/latest/dg/sap-odata-configuring-iam-permissions.html)
- [Connectivity / VPC Connection](https://docs.aws.amazon.com/glue/latest/dg/sap-odata-connectivity-vpc-connection.html): Steps for VPC Connection:
- [SAP Authentication](https://docs.aws.amazon.com/glue/latest/dg/sap-odata-authentication.html): The SAP connector supports both CUSTOM (this is SAP BASIC authentication) and OAUTH authentication methods.
- [AWS Secrets Manager](https://docs.aws.amazon.com/glue/latest/dg/sap-odata-aws-secret-manager-auth-secret.html): You will need to store the SAP OData connection secrets in AWS Secrets Manager, configure the necessary permissions for retrieval as specified in the section, and use it while creating a connection.
- [Create connections](https://docs.aws.amazon.com/glue/latest/dg/sap-odata-creating-connections.html): To configure an SAP OData connection:

### [Creating SAP OData job](https://docs.aws.amazon.com/glue/latest/dg/sap-odata-creating-job.html)

Refer to Building visual ETL jobs with AWS Glue Studio

- [Operational Data Provisioning (ODP) Sources](https://docs.aws.amazon.com/glue/latest/dg/sap-odata-operational-data-provisioning-sources.html): Operational Data Provisioning (ODP) provides a technical infrastructure that you can use to support data extraction and replication for various target applications and supports delta mechanisms in these scenarios.
- [Delta Token based Incremental Transfers](https://docs.aws.amazon.com/glue/latest/dg/sap-odata-incremental-transfers.html): To enable Incremental Transfer using Change Data Capture (CDC) for ODP-enabled entities that support it, follow these steps:
- [OData Services (Non-ODP Sources)](https://docs.aws.amazon.com/glue/latest/dg/sap-odata-non-odp-services.html)
- [Writing to SAP OData](https://docs.aws.amazon.com/glue/latest/dg/sap-odata-writing.html): This section describes how to write data to your SAP OData Service using the AWS Glue connector for SAP OData.
- [Using the SAP OData state management script](https://docs.aws.amazon.com/glue/latest/dg/sap-odata-state-management-script.html): To use the SAP OData state management script in your AWS Glue job, follow these steps:

### [Partitioning for Non ODP entities](https://docs.aws.amazon.com/glue/latest/dg/sap-odata-non-odp-entities-partitioning.html)

In Apache Spark, partitioning refers to the way data is divided and distributed across the worker nodes in a cluster for parallel processing.

- [Limitations / Callouts](https://docs.aws.amazon.com/glue/latest/dg/sap-odata-limitations.html)
- [SAP OData connection options](https://docs.aws.amazon.com/glue/latest/dg/sap-odata-connection-options.html): The following are connection options for SAP OData:
- [SAP OData entity and field details](https://docs.aws.amazon.com/glue/latest/dg/sap-odata-entity-field-details.html)

### [Connecting to SendGrid](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-data-sendgrid.html)

AWS Glue provides support for connecting to SendGrid.

- [AWS Glue support for SendGrid](https://docs.aws.amazon.com/glue/latest/dg/sendgrid-support.html): AWS Glue supports SendGrid as follows:
- [IAM policies](https://docs.aws.amazon.com/glue/latest/dg/sendgrid-configuring-iam-permissions.html): The following sample policy describes the required AWS IAM permissions for creating and using connections.
- [Configuring SendGrid](https://docs.aws.amazon.com/glue/latest/dg/sendgrid-configuring.html): Before you can use AWS Glue to transfer data from SendGrid, you must meet these requirements:
- [Configuring SendGrid connections](https://docs.aws.amazon.com/glue/latest/dg/sendgrid-configuring-connections.html): SendGrid supports custom authentication.
- [Reading from SendGrid entities](https://docs.aws.amazon.com/glue/latest/dg/sendgrid-reading-from-entities.html): Prerequisite
- [SendGrid connection options](https://docs.aws.amazon.com/glue/latest/dg/sendgrid-connection-options.html): The following are connection options for SendGrid:
- [SendGrid limitations](https://docs.aws.amazon.com/glue/latest/dg/sendgrid-limitations.html): The following are limitations or notes for SendGrid:

### [Connecting to ServiceNow](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-data-servicenow.html)

AWS Glue provides support for connecting to ServiceNow.

- [AWS Glue support for ServiceNow](https://docs.aws.amazon.com/glue/latest/dg/servicenow-support.html): AWS Glue supports ServiceNow as follows:
- [IAM policies](https://docs.aws.amazon.com/glue/latest/dg/servicenow-configuring-iam-permissions.html): The following sample policy describes the required AWS IAM permissions for creating and using connections.
- [Configuring ServiceNow](https://docs.aws.amazon.com/glue/latest/dg/servicenow-configuring.html): Before you can use AWS Glue to transfer data from ServiceNow, you must meet these requirements:
- [Configuring ServiceNow connections](https://docs.aws.amazon.com/glue/latest/dg/servicenow-configuring-connections.html): The grant type determines how AWS Glue communicates with ServiceNow to request access to your data.
- [Reading from ServiceNow entities](https://docs.aws.amazon.com/glue/latest/dg/servicenow-reading-from-entities.html): Prerequisite
- [ServiceNow connection options](https://docs.aws.amazon.com/glue/latest/dg/servicenow-connection-options.html): The following are connection options for ServiceNow:
- [Limitations and notes for ServiceNow connector](https://docs.aws.amazon.com/glue/latest/dg/servicenow-connector-limitations.html): The following are limitations or notes for the ServiceNow connector:

### [Connecting to Slack](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-data-slack.html)

AWS Glue provides support for connecting to Slack.

- [AWS Glue support for Slack](https://docs.aws.amazon.com/glue/latest/dg/slack-support.html): AWS Glue supports Slack as follows:
- [IAM policies](https://docs.aws.amazon.com/glue/latest/dg/slack-configuring-iam-permissions.html): The following sample policy describes the required IAM permissions for creating and using connections.
- [Configuring Slack](https://docs.aws.amazon.com/glue/latest/dg/slack-configuring.html): Before you can use AWS Glue to transfer data to or from Slack, you must meet these requirements:
- [Configuring Slack connections](https://docs.aws.amazon.com/glue/latest/dg/slack-configuring-connections.html): Slack supports the AUTHORIZATION_CODE grant type for OAuth 2.
- [Reading from Slack entities](https://docs.aws.amazon.com/glue/latest/dg/slack-reading-from-entities.html): Prerequisites
- [Slack connection options](https://docs.aws.amazon.com/glue/latest/dg/slack-connection-options.html): The following are connection options for Slack:
- [Limitations](https://docs.aws.amazon.com/glue/latest/dg/slack-limitations.html): The following are limitations for the Slack connector:
- [Creating a new Slack account and configuring the client app](https://docs.aws.amazon.com/glue/latest/dg/slack-new-account-creation.html)

### [Connecting to Smartsheet](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-smartsheet.html)

Smartsheet is a work management and collaboration SaaS product.

- [AWS Glue support for Smartsheet](https://docs.aws.amazon.com/glue/latest/dg/smartsheet-support.html): AWS Glue supports Smartsheet as follows:
- [IAM policies](https://docs.aws.amazon.com/glue/latest/dg/smartsheet-configuring-iam-permissions.html): The following sample policy describes the required AWS permissions for creating and using connections.
- [Configuring Smartsheet](https://docs.aws.amazon.com/glue/latest/dg/smartsheet-configuring.html): Before you can use AWS Glue to transfer from Smartsheet, you must meet the following requirements:
- [Configuring Smartsheet connections](https://docs.aws.amazon.com/glue/latest/dg/smartsheet-configuring-connections.html): Smartsheet supports AUTHORIZATION_CODE grant type for OAuth2.
- [Reading from Smartsheet entities](https://docs.aws.amazon.com/glue/latest/dg/smartsheet-reading-from-entities.html): Prerequisites
- [Smartsheet connection options](https://docs.aws.amazon.com/glue/latest/dg/smartsheet-connection-options.html): The following are connection options for Smartsheet:
- [Creating an Smartsheet account](https://docs.aws.amazon.com/glue/latest/dg/smartsheet-create-account.html)
- [Limitations](https://docs.aws.amazon.com/glue/latest/dg/smartsheet-connector-limitations.html): Smartsheet doesn't support field-based or record-based partitioning.

### [Connecting to Snapchat Ads](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-data-snapchat-ads.html)

AWS Glue provides support for connecting to Snapchat Ads.

- [AWS Glue support for Snapchat Ads](https://docs.aws.amazon.com/glue/latest/dg/snapchat-ads-support.html): AWS Glue supports Snapchat Ads as follows:
- [IAM policies](https://docs.aws.amazon.com/glue/latest/dg/snapchat-ads-configuring-iam-permissions.html): The following sample policy describes the required AWS permissions for creating and using connections.
- [Configuring Snapchat Ads](https://docs.aws.amazon.com/glue/latest/dg/snapchat-ads-configuring.html): Before you can use AWS Glue to transfer from Snapchat Ads, you must meet these requirements:
- [Configuring Snapchat Ads connections](https://docs.aws.amazon.com/glue/latest/dg/snapchat-ads-configuring-connections.html): Snapchat Ads supports only the AUTHORIZATION_CODE grant type.
- [Reading from Snapchat Ads entities](https://docs.aws.amazon.com/glue/latest/dg/snapchat-ads-reading-from-entities.html): Prerequisites
- [Snapchat Ads connection options](https://docs.aws.amazon.com/glue/latest/dg/snapchat-ads-connection-options.html): The following are connection options for Snapchat Ads:
- [Creating new Snapchat Ad account](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-data-snapchat-ads-new-account.html): AWS Glue provides support for connecting to Snapchat Ads.
- [Creating an app in your Snapchat Ads account](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-data-snapchat-ads-managed-client-application.html): AWS Glue provides support for connecting to Snapchat Ads.

### [Connecting to Snowflake](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-data-snowflake.html)

AWS Glue provides built-in support for Snowflake.

- [Creating a Snowflake connection](https://docs.aws.amazon.com/glue/latest/dg/creating-snowflake-connection.html)
- [Creating a Snowflake source node](https://docs.aws.amazon.com/glue/latest/dg/creating-snowflake-source-node.html)
- [Creating a Snowflake target node](https://docs.aws.amazon.com/glue/latest/dg/creating-snowflake-target-node.html)

### [Connecting to Stripe](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-data-stripe.html)

AWS Glue provides support for connecting to Stripe.

- [AWS Glue support for Stripe](https://docs.aws.amazon.com/glue/latest/dg/stripe-support.html): AWS Glue supports Stripe as follows:
- [IAM policies](https://docs.aws.amazon.com/glue/latest/dg/stripe-configuring-iam-permissions.html): The following sample policy describes the required IAM permissions for creating and using connections.
- [Configuring Stripe](https://docs.aws.amazon.com/glue/latest/dg/stripe-configuring.html): Before you can use AWS Glue to transfer data from Stripe, you must meet these requirements:
- [Configuring Stripe connections](https://docs.aws.amazon.com/glue/latest/dg/stripe-configuring-connections.html): Stripe supports custom authentication.
- [Reading from Stripe entities](https://docs.aws.amazon.com/glue/latest/dg/stripe-reading-from-entities.html): Prerequisites
- [Stripe connection options](https://docs.aws.amazon.com/glue/latest/dg/stripe-connection-options.html): The following are connection options for Stripe:
- [Limitations](https://docs.aws.amazon.com/glue/latest/dg/stripe-limitations.html): The following are limitations for the Stripe connector:
- [Creating a new Stripe account and configuring the client app](https://docs.aws.amazon.com/glue/latest/dg/stripe-new-account-creation.html)

### [Connecting to Teradata](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-data-teradata.html)

AWS Glue provides built-in support for Teradata.

- [Creating a Teradata Vantage connection](https://docs.aws.amazon.com/glue/latest/dg/creating-teradata-connection.html): To connect to Teradata Vantage from AWS Glue, you will need to create and store your Teradata credentials in an AWS Secrets Manager secret, then associate that secret with a AWS Glue Teradata connection.
- [Creating a Teradata source node](https://docs.aws.amazon.com/glue/latest/dg/creating-teradata-source-node.html)
- [Creating a Teradata target node](https://docs.aws.amazon.com/glue/latest/dg/creating-teradata-target-node.html)

### [Connecting to Twilio](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-data-twilio.html)

AWS Glue provides support for connecting to Twilio.

- [AWS Glue support for Twilio](https://docs.aws.amazon.com/glue/latest/dg/twilio-support.html): AWS Glue supports Twilio as follows:
- [IAM policies](https://docs.aws.amazon.com/glue/latest/dg/twilio-configuring-iam-permissions.html): The following sample policy describes the required AWS IAM permissions for creating and using connections.
- [Configuring Twilio](https://docs.aws.amazon.com/glue/latest/dg/twilio-configuring.html): Before you can use AWS Glue to transfer data from Twilio, you must meet these requirements:
- [Configuring Twilio connections](https://docs.aws.amazon.com/glue/latest/dg/twilio-configuring-connections.html): Twilio supports username and password for Basic Authentication.
- [Reading from Twilio entities](https://docs.aws.amazon.com/glue/latest/dg/twilio-reading-from-entities.html): Prerequisite
- [Twilio connection options](https://docs.aws.amazon.com/glue/latest/dg/twilio-connection-options.html): The following are connection options for Twilio:
- [Limitations and notes for Twilio connector](https://docs.aws.amazon.com/glue/latest/dg/twilio-connector-limitations.html): The following are limitations or notes for the Twilio connector:

### [Connecting to Vertica](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-data-vertica.html)

AWS Glue provides built-in support for Vertica.

- [Creating a Vertica connection](https://docs.aws.amazon.com/glue/latest/dg/creating-vertica-connection.html): Prerequisites:
- [Creating a Vertica source node](https://docs.aws.amazon.com/glue/latest/dg/creating-vertica-source-node.html)
- [Creating a Vertica target node](https://docs.aws.amazon.com/glue/latest/dg/creating-vertica-target-node.html)

### [Connecting to WooCommerce](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-data-woocommerce.html)

AWS Glue provides support for connecting to WooCommerce.

- [AWS Glue support for WooCommerce](https://docs.aws.amazon.com/glue/latest/dg/woocommerce-support.html): AWS Glue supports WooCommerce as follows:
- [IAM policies](https://docs.aws.amazon.com/glue/latest/dg/woocommerce-configuring-iam-permissions.html): The following sample policy describes the required AWS IAM permissions for creating and using connections.
- [Configuring WooCommerce](https://docs.aws.amazon.com/glue/latest/dg/woocommerce-configuring.html): Before you can use AWS Glue to transfer data from WooCommerce, you must meet these requirements:
- [Configuring WooCommerce connections](https://docs.aws.amazon.com/glue/latest/dg/woocommerce-configuring-connections.html): WooCommerce supports custom authentication.
- [Reading from WooCommerce entities](https://docs.aws.amazon.com/glue/latest/dg/woocommerce-reading-from-entities.html): Prerequisite
- [WooCommerce connection options](https://docs.aws.amazon.com/glue/latest/dg/woocommerce-connection-options.html): The following are connection options for WooCommerce:

### [Connecting to Zendesk](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-data-zendesk.html)

AWS Glue provides support for connecting to Zendesk.

- [AWS Glue support for Zendesk](https://docs.aws.amazon.com/glue/latest/dg/zendesk-support.html): AWS Glue supports Zendesk as follows:
- [IAM policies](https://docs.aws.amazon.com/glue/latest/dg/zendesk-configuring-iam-permissions.html): The following sample policy describes the required AWS IAM permissions for creating and using connections.
- [Configuring Zendesk](https://docs.aws.amazon.com/glue/latest/dg/zendesk-configuring.html): Before you can use AWS Glue to transfer data from Zendesk, you must meet these requirements:
- [Configuring Zendesk connections](https://docs.aws.amazon.com/glue/latest/dg/zendesk-configuring-connections.html): The Zendesk connector supports the Authorization Code grant type.
- [Reading from Zendesk entities](https://docs.aws.amazon.com/glue/latest/dg/zendesk-reading-from-entities.html): Prerequisite
- [Zendesk connection options](https://docs.aws.amazon.com/glue/latest/dg/zendesk-connection-options.html): The following are connection options for Zendesk:
- [Limitations](https://docs.aws.amazon.com/glue/latest/dg/zendesk-limitations.html): The following are limitations of the Zendesk connector:

### [Connecting to Zoho CRM](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-data-zoho-crm.html)

AWS Glue provides support for connecting to Zoho CRM.

- [AWS Glue support for Zoho CRM](https://docs.aws.amazon.com/glue/latest/dg/zoho-crm-support.html): AWS Glue supports Zoho CRM as follows:
- [IAM policies](https://docs.aws.amazon.com/glue/latest/dg/zoho-crm-configuring-iam-permissions.html): The following sample policy describes the required AWS IAM permissions for creating and using connections.
- [Configuring Zoho CRM](https://docs.aws.amazon.com/glue/latest/dg/zoho-crm-configuring.html): Before you can use AWS Glue to transfer data from Zoho CRM, you must meet these requirements:
- [Configuring Zoho CRM connections](https://docs.aws.amazon.com/glue/latest/dg/zoho-crm-configuring-connections.html): The grant type determines how AWS Glue communicates with Zoho CRM to request access to your data.
- [Reading from Zoho CRM entities](https://docs.aws.amazon.com/glue/latest/dg/zoho-crm-reading-from-entities.html): Prerequisite
- [Zoho CRM connection options](https://docs.aws.amazon.com/glue/latest/dg/zoho-crm-connection-options.html): The following are connection options for Zoho CRM:
- [Limitations and notes for Zoho CRM connector](https://docs.aws.amazon.com/glue/latest/dg/zoho-crm-connector-limitations.html): The following are limitations or notes for the Zoho CRM connector:

### [Connecting to Zoom Meetings](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-data-zoom-meetings.html)

AWS Glue provides support for connecting to Zoom Meetings.

- [AWS Glue support for Zoom Meetings](https://docs.aws.amazon.com/glue/latest/dg/zoom-meetings-support.html): AWS Glue supports Zoom Meetings as follows:
- [IAM policies](https://docs.aws.amazon.com/glue/latest/dg/zoom-meetings-configuring-iam-permissions.html): The following sample policy describes the required AWS IAM permissions for creating and using connections.
- [Configuring Zoom Meetings](https://docs.aws.amazon.com/glue/latest/dg/zoom-meetings-configuring.html): Before you can use AWS Glue to transfer data from Zoom Meetings, you must meet these requirements:
- [Configuring the Zoom Meetings client app](https://docs.aws.amazon.com/glue/latest/dg/zoom-meetings-configuring-client-app.html)
- [Configuring Zoom Meetings connections](https://docs.aws.amazon.com/glue/latest/dg/zoom-meetings-configuring-connections.html): Zoom Meetings supports the AUTHORIZATION_CODE grant type for OAuth2.
- [Reading from Zoom Meetings entities](https://docs.aws.amazon.com/glue/latest/dg/zoom-meetings-reading-from-entities.html): Prerequisite
- [Zoom Meetings connection options](https://docs.aws.amazon.com/glue/latest/dg/zoom-meetings-connection-options.html): The following are connection options for Zoom Meetings:
- [Zoom Meetings limitations](https://docs.aws.amazon.com/glue/latest/dg/zoom-meetings-limitations.html): The following are limitations or notes for Zoom Meetings:
- [Adding a JDBC connection using your own JDBC drivers](https://docs.aws.amazon.com/glue/latest/dg/console-connections-jdbc-drivers.html): You can use your own JDBC driver when using a JDBC connection.

### [Using custom connectors and connections](https://docs.aws.amazon.com/glue/latest/dg/connectors-chapter.html)

Create custom connections in AWS Glue Studio that use connectors for accessing data stores not natively supported by AWS Glue.

- [Creating custom connectors](https://docs.aws.amazon.com/glue/latest/dg/creating-custom-connectors.html): You can also build your own connector and then upload the connector code to AWS Glue Studio.

### [Creating connections for connectors](https://docs.aws.amazon.com/glue/latest/dg/creating-connections.html)

An AWS Glue connection is a Data Catalog object that stores connection information for a particular data store.

- [Creating a Kafka connection](https://docs.aws.amazon.com/glue/latest/dg/creating-connections-kafka.html): When creating a Kafka connection, selecting Kafka from the drop-down menu will display additional settings to configure:
- [Authoring jobs with custom connectors](https://docs.aws.amazon.com/glue/latest/dg/job-authoring-custom-connectors.html): You can use connectors and connections for both data source nodes and data target nodes in AWS Glue Studio.
- [Managing connectors and connections](https://docs.aws.amazon.com/glue/latest/dg/managing-connectors.html): You use the Connections page in AWS Glue to manage your connectors and connections.
- [Developing custom connectors](https://docs.aws.amazon.com/glue/latest/dg/developing-custom-connectors.html): You can write the code that reads data from or writes data to your data store and formats the data for use with AWS Glue Studio jobs.
- [Restrictions for using connectors and connections in AWS Glue Studio](https://docs.aws.amazon.com/glue/latest/dg/connector-restrictions.html): When you're using custom connectors or connectors from AWS Marketplace, take note of the following restrictions:
- [Testing an AWS Glue connection](https://docs.aws.amazon.com/glue/latest/dg/console-test-connections.html): Test connections on the AWS Glue console to check that the connection can successfully connect to your data store.
- [Configuring AWS calls to go through your VPC](https://docs.aws.amazon.com/glue/latest/dg/connection-VPC-disable-proxy.html): The special job parameter disable-proxy-v2 allows you to route your calls to services such as Amazon S3, CloudWatch, and AWS Glue through your VPC.
- [Connecting to a JDBC data store in a VPC](https://docs.aws.amazon.com/glue/latest/dg/connection-JDBC-VPC.html): Typically, you create resources inside Amazon Virtual Private Cloud (Amazon VPC) so that they cannot be accessed over the public internet.
- [Using a MongoDB or MongoDB Atlas connection](https://docs.aws.amazon.com/glue/latest/dg/connection-mongodb.html): After you create a connection for MongoDB or MongoDB Atlas, you can use the connection in your ETL job.
- [Crawling an Amazon S3 data store using a VPC endpoint](https://docs.aws.amazon.com/glue/latest/dg/connection-S3-VPC.html): For security, auditing, or control purposes you may want your Amazon S3 data store or Amazon S3 backed Data Catalog tables to only be accessed through an Amazon Virtual Private Cloud environment (Amazon VPC).
- [Working with AWS Lake Formation-protected data](https://docs.aws.amazon.com/glue/latest/dg/working-with-lake-formation-protected-data.html)
- [Troubleshooting connection issues](https://docs.aws.amazon.com/glue/latest/dg/troubleshooting-connection.html): How to troubleshoot a connection in AWS Glue.
- [Tutorial: Using the AWS Glue Connector for Elasticsearch](https://docs.aws.amazon.com/glue/latest/dg/tutorial-elastisearch-connector.html): This tutorial shows how to connect to your OpenSearch nodes using the free open-source Elasticsearch Connector for AWS Glue from AWS Marketplace.


## [Building AWS Glue jobs with interactive sessions](https://docs.aws.amazon.com/glue/latest/dg/interactive-sessions-chapter.html)

### [Getting started with AWS Glue interactive sessions](https://docs.aws.amazon.com/glue/latest/dg/interactive-sessions.html)

Set up to run Spark workloads in the cloud from a Jupyter Notebook installed locally.

- [Using interactive sessions with SageMaker AI Studio](https://docs.aws.amazon.com/glue/latest/dg/interactive-sessions-sagemaker-studio.html): AWS Glue Interactive Sessions is an on-demand, serverless, Apache Spark runtime environment that data scientists and engineers can use to rapidly build, test, and run data preparation and analytics applications.
- [Using interactive sessions with Microsoft Visual Studio Code](https://docs.aws.amazon.com/glue/latest/dg/interactive-sessions-vscode.html): Prerequisites
- [Interactive sessions with IAM](https://docs.aws.amazon.com/glue/latest/dg/glue-is-security.html): These sections describe security considerations for AWS Glue interactive sessions.
- [Configuring AWS Glue interactive sessions for Jupyter and AWS Glue Studio notebooks](https://docs.aws.amazon.com/glue/latest/dg/interactive-sessions-magics.html)
- [Converting a script or notebook into an AWS Glue job](https://docs.aws.amazon.com/glue/latest/dg/interactive-sessions-convert.html): There are two ways you can convert a script or notebook into an AWS Glue job:
- [Working with streaming operations in AWS Glue interactive sessions](https://docs.aws.amazon.com/glue/latest/dg/interactive-sessions-streaming.html)
- [AWS Glue interactive session pricing](https://docs.aws.amazon.com/glue/latest/dg/interactive-sessions-session-pricing.html): AWS charges for AWS Glue interactive sessions based on how long the session is active and the number of Data Processing Units (DPU) used.

### [Developing and testing locally](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-libraries.html)

Use the publicly available AWS Glue Scala library to develop and test your Python or Scala AWS Glue ETL scripts locally.

- [Developing AWS Glue jobs locally with Docker](https://docs.aws.amazon.com/glue/latest/dg/develop-local-docker-image.html): For a production-ready data platform, the development process and CI/CD pipeline for AWS Glue jobs is a key topic.

### [Dev endpoints](https://docs.aws.amazon.com/glue/latest/dg/development.html)

The following sections provide information on using dev endpoints to develop jobs in AWS Glue version 1.0.

- [Migrating from dev endpoints to interactive sessions](https://docs.aws.amazon.com/glue/latest/dg/development-migration-checklist.html): Use the following checklist to determine the appropriate method to migrate from dev endpoints to interactive sessions.

### [Developing scripts using development endpoints](https://docs.aws.amazon.com/glue/latest/dg/dev-endpoint.html)

Use a development endpoint to develop and test your AWS Glue scripts.

- [Development endpoint workflow](https://docs.aws.amazon.com/glue/latest/dg/dev-endpoint-workflow.html): To use an AWS Glue development endpoint, you can follow this workflow:
- [How Development Endpoints Work with SageMaker Notebooks](https://docs.aws.amazon.com/glue/latest/dg/dev-endpoint-how-it-works.html): Describes how AWS Glue development endpoints work with SageMarker notebooks.
- [Adding a development endpoint](https://docs.aws.amazon.com/glue/latest/dg/add-dev-endpoint.html): Use the AWS Command Line Interface to add a development endpoint.
- [Accessing your development endpoint](https://docs.aws.amazon.com/glue/latest/dg/dev-endpoint-elastic-ip.html): Access your development endpoint using its public IP address or an Elastic IP address that you create.
- [Tutorial: Jupyter notebook in JupyterLab](https://docs.aws.amazon.com/glue/latest/dg/dev-endpoint-tutorial-local-jupyter.html): AWS Glue tutorial that shows how to connect a Jupyter notebook in JupyterLab running on your local machine to a development endpoint.
- [Tutorial: Use a SageMaker AI notebook](https://docs.aws.amazon.com/glue/latest/dg/dev-endpoint-tutorial-sage.html): Use a SageMaker AI notebook connected to a development endpoint in AWS Glue.
- [Tutorial: Use a REPL shell](https://docs.aws.amazon.com/glue/latest/dg/dev-endpoint-tutorial-repl.html): Use a REPL Shell connected to a development endpoint in AWS Glue.
- [Tutorial: Use PyCharm professional](https://docs.aws.amazon.com/glue/latest/dg/dev-endpoint-tutorial-pycharm.html): AWS Glue tutorial connecting PyCharm Professional to a development endpoint.
- [Advanced configuration: sharing dev endpoints among multiple users](https://docs.aws.amazon.com/glue/latest/dg/dev-endpoint-sharing.html): This section explains how you can take advantage of development endpoints with SageMaker notebooks in typical use cases to share development endpoints among multiple users.
- [Managing notebooks](https://docs.aws.amazon.com/glue/latest/dg/notebooks-with-glue.html): Use a notebook attached to a development endpoint to try out your code in AWS Glue.


## [Building visual ETL jobs](https://docs.aws.amazon.com/glue/latest/dg/author-job-glue.html)

### [Starting visual ETL jobs in AWS Glue Studio](https://docs.aws.amazon.com/glue/latest/dg/edit-nodes-chapter.html)

Use the visual editor in AWS Glue Studio to create and modify your ETL jobs.

- [Job editor features](https://docs.aws.amazon.com/glue/latest/dg/job-editor-features.html): The AWS Glue Studio job editor was designed to make creating and editing jobs as easy as possible.

### [Transform data with AWS Glue managed transforms](https://docs.aws.amazon.com/glue/latest/dg/edit-jobs-transforms.html)

AWS Glue Studio provides two types of transforms:

### [Using a data preparation recipe in AWS Glue Studio](https://docs.aws.amazon.com/glue/latest/dg/glue-studio-data-preparation.html)

AWS Glue DataBrew recipes can be used in AWS Glue Studio jobs.

- [Author and run data preparation recipes in a visual ETL AWS Glue job](https://docs.aws.amazon.com/glue/latest/dg/glue-studio-data-preparation-recipe-transform-tutorial.html): In this scenario, you can author data preparation recipes without having to first create them in DataBrew.
- [Import a AWS Glue DataBrew recipe in AWS Glue Studio](https://docs.aws.amazon.com/glue/latest/dg/glue-studio-data-preparation-import-recipe.html): In AWS Glue DataBrew, a recipe is a set of data transformation steps.
- [Migrating from DataBrew](https://docs.aws.amazon.com/glue/latest/dg/databrew-migration-to-glue-studio.html): The following sections provide information on how to migrate from using AWS Glue DataBrew to AWS Glue Studio.
- [Using Change Schema to remap data property keys](https://docs.aws.amazon.com/glue/latest/dg/transforms-configure-applymapping.html): A Change Schema transform remaps the source data property keys into the desired configured for the target data.
- [Using Drop Duplicates](https://docs.aws.amazon.com/glue/latest/dg/transforms-drop-duplicates.html): The Drop Duplicates transform removes rows from your data source by giving you two options.
- [Using SelectFields to remove most data property keys](https://docs.aws.amazon.com/glue/latest/dg/transforms-configure-select-fields.html): You can create a subset of data property keys from the dataset using the SelectFields transform.
- [Using DropFields to keep most data property keys](https://docs.aws.amazon.com/glue/latest/dg/transforms-configure-drop-fields.html): You can create a subset of data property keys from the dataset using the DropFields transform.
- [Renaming a field in the dataset](https://docs.aws.amazon.com/glue/latest/dg/transforms-configure-rename-field.html): You can use the RenameField transform to change the name for an individual property key in the dataset.
- [Using Spigot to sample your dataset](https://docs.aws.amazon.com/glue/latest/dg/transforms-configure-spigot.html): To test the transformations performed by your job, you might want to get a sample of the data to check that the transformation works as intended.
- [Joining datasets](https://docs.aws.amazon.com/glue/latest/dg/transforms-configure-join.html): The Join transform allows you to combine two datasets into one.
- [Using Union to combine rows](https://docs.aws.amazon.com/glue/latest/dg/transforms-configure-union.html): You use the Union transform node when you want to combine rows from more than one data source that have the same schema.
- [Using SplitFields to split a dataset into two](https://docs.aws.amazon.com/glue/latest/dg/transforms-configure-split-fields.html): The SplitFields transform allows you to choose some of the data property keys in the input dataset and put them into one dataset and the unselected keys into a separate dataset.
- [Overview of SelectFromCollection transform](https://docs.aws.amazon.com/glue/latest/dg/transforms-selectfromcollection-overview.html): Certain transforms have multiple datasets as their output instead of a single dataset, for example, SplitFields.
- [Using SelectFromCollection to choose which dataset to keep](https://docs.aws.amazon.com/glue/latest/dg/transforms-configure-select-collection.html): Use the SelectFromCollection transform to convert a collection of DynamicFrames into a single DynamicFrame.
- [Find and fill missing values in a dataset](https://docs.aws.amazon.com/glue/latest/dg/transforms-configure-fmv.html): You can use the FillMissingValues transform to locate records in the dataset that have missing values and add a new field with a value determined by imputation.
- [Filtering keys within a dataset](https://docs.aws.amazon.com/glue/latest/dg/transforms-filter.html): Use the Filter transform to create a new dataset by filtering records from the input dataset based on a regular expression.
- [Using DropNullFields to remove fields with null values](https://docs.aws.amazon.com/glue/latest/dg/transforms-dropnull-fields.html): Use the DropNullFields transform to remove fields from the dataset if all values in the field are ânullâ.
- [Using a SQL query to transform data](https://docs.aws.amazon.com/glue/latest/dg/transforms-sql.html): You can use a SQL transform to write your own transform in the form of a SQL query.
- [Using Aggregate to perform summary calculations on selected fields](https://docs.aws.amazon.com/glue/latest/dg/transforms-aggregate-fields.html)
- [Flatten nested structs](https://docs.aws.amazon.com/glue/latest/dg/transforms-flatten.html): Flatten the fields of nested structs in the data, so they become top level fields.
- [Add a UUID column](https://docs.aws.amazon.com/glue/latest/dg/transforms-uuid.html): When you add a UUID (Universally Unique Identified) column, each row will be assigned a unique 36-character string.
- [Add an identifier column](https://docs.aws.amazon.com/glue/latest/dg/transforms-identifier.html): Assign a numeric Identifier for each row in the dataset.
- [Convert a column to timestamp type](https://docs.aws.amazon.com/glue/latest/dg/transforms-to-timestamp.html): You can use the transform To timestamp to change the data type of a numeric or string column into timestamp, so that it can be stored with that data type or applied to other transforms that require a timestamp.
- [Convert a timestamp column to a formatted string](https://docs.aws.amazon.com/glue/latest/dg/transforms-format-timestamp.html): Format a timestamp column into a string based on a pattern.
- [Creating a Conditional Router transformation](https://docs.aws.amazon.com/glue/latest/dg/transforms-conditional-router.html): The Conditional Router transform allows you to apply multiple conditions to incoming data.
- [Using the Concatenate Columns transform to append columns](https://docs.aws.amazon.com/glue/latest/dg/transforms-concatenate-columns.html): The Concatenate transform allows you to build a new string column using the values of other columns with an optional spacer.
- [Using the Split String transform to break up a string column](https://docs.aws.amazon.com/glue/latest/dg/transforms-split-string.html): The Split String transform allows you to break up a string into an array of tokens using a regular expression to define how the split is done.
- [Using the Array To Columns transform to extract the elements of an array into top level columns](https://docs.aws.amazon.com/glue/latest/dg/transforms-array-to-columns.html): The Array To Columns transform allows you extract some or all the elements of a column of type array into new columns.
- [Using the Add Current Timestamp transform](https://docs.aws.amazon.com/glue/latest/dg/transforms-add-current-timestamp.html): The Add Current Timestamp transform allows you to mark the rows with the time on which the data was processed.
- [Using the Pivot Rows to Columns transform](https://docs.aws.amazon.com/glue/latest/dg/transforms-pivot-rows-to-columns.html): The Pivot Rows to Columns transform allows you to aggregate a numeric column by rotating unique values on selected columns which become new columns (if multiple columns are selected, the values are concatenated to name the new columns).
- [Using the Unpivot Columns To Rows transform](https://docs.aws.amazon.com/glue/latest/dg/transforms-unpivot-columns-to-rows.html): The Unpivot transform allows you convert columns into values of new columns generating a row for each unique value.
- [Using the Autobalance Processing transform to optimize your runtime](https://docs.aws.amazon.com/glue/latest/dg/transforms-autobalance-processing.html): The Autobalance Processing transform redistributes the data among the workers for better performance.
- [Using the Derived Column transform to combine other columns](https://docs.aws.amazon.com/glue/latest/dg/transforms-derived-column.html): The Derived Column transform allows you to define a new column based on a math formula or SQL expression in which you can use other columns in the data, as well as constants and literals.
- [Using the Lookup transform to add matching data from a catalog table](https://docs.aws.amazon.com/glue/latest/dg/transforms-lookup.html): The Lookup transform allows you to add columns from a defined catalog table when the keys match the defined lookup columns in the data.
- [Using the Explode Array or Map Into Rows transform](https://docs.aws.amazon.com/glue/latest/dg/transforms-explode-array.html): The Explode transform allows you to extract values from a nested structure into individual rows that are easier to manipulate.
- [Using the Record Matching transform to invoke an existing data classification transform](https://docs.aws.amazon.com/glue/latest/dg/transforms-record-matching.html): This transform invokes an existing Record Matching machine learning data classification transform.
- [Removing null rows](https://docs.aws.amazon.com/glue/latest/dg/transforms-remove-null-rows.html): This transform removes from the dataset rows that have all columns as null.
- [Parsing a string column containing JSON data](https://docs.aws.amazon.com/glue/latest/dg/transforms-parse-json-column.html): This transform parses a string column containing JSON data and convert it to a struct or an array column, depending if the JSON is an object or an array, respectively.
- [Extracting a JSON path](https://docs.aws.amazon.com/glue/latest/dg/transforms-extract-json-path.html): This transform extracts new columns from a JSON string column.
- [Extracting string fragments using a regular expression](https://docs.aws.amazon.com/glue/latest/dg/transforms-regex-extractor.html): This transform extracts string fragments using a regular expression and creates a new column out of it, or multiple columns if using regex groups.
- [Creating a custom transformation](https://docs.aws.amazon.com/glue/latest/dg/transforms-custom.html): If you need to perform more complicated transformations on your data, or want to add data property keys to the dataset, you can add a Custom code transform to your job diagram.

### [Transform data with custom visual transforms](https://docs.aws.amazon.com/glue/latest/dg/custom-visual-transform.html)

Custom visual transforms allow you to create transforms and make them available for use in AWS Glue Studio jobs.

- [Getting started with custom visual transforms](https://docs.aws.amazon.com/glue/latest/dg/custom-visual-transform-getting-started.html): To create a custom visual transform, you go through the following steps.
- [Step 1. Create a JSON config file](https://docs.aws.amazon.com/glue/latest/dg/custom-visual-transform-json-config-file.html): A JSON config file is required to define and describe your custom visual transform.
- [Step 2. Implement the transform logic](https://docs.aws.amazon.com/glue/latest/dg/custom-visual-transform-implementation.html)
- [Step 3. Validate and troubleshoot custom visual transforms in AWS Glue Studio](https://docs.aws.amazon.com/glue/latest/dg/custom-visual-transform-validation.html): AWS Glue Studio validates the JSON config file before custom visual transforms are loaded into AWS Glue Studio.
- [Step 4. Update custom visual transforms as needed](https://docs.aws.amazon.com/glue/latest/dg/custom-visual-transform-updating-transforms.html): Once created and used, the transform script can be updated as long as the transform follows the corresponding json definition:
- [Step 5. Use custom visual transforms in AWS Glue Studio](https://docs.aws.amazon.com/glue/latest/dg/custom-visual-transform-create-gs.html): To use a custom visual transform in AWS Glue Studio, you upload the config and source files, then select the transform from the Action menu.
- [Usage examples](https://docs.aws.amazon.com/glue/latest/dg/custom-visual-transform-example-json.html): The following is an example of all possible parameters in a .json config file.
- [Examples of custom visual scripts](https://docs.aws.amazon.com/glue/latest/dg/custom-visual-transform-example-scripts.html): The following examples perform equivalent transformations.

### [Using Data Lake frameworks with AWS Glue Studio](https://docs.aws.amazon.com/glue/latest/dg/gs-data-lake-formats.html)

Data Lake frameworks such as Apache Hudi, Delta Lake, and Apache Iceberg are supported natively in AWS Glue Studio.

- [Using Hudi framework in AWS Glue Studio](https://docs.aws.amazon.com/glue/latest/dg/gs-data-lake-formats-hudi.html): When creating or editing a job, AWS Glue Studio automatically adds the corresponding Hudi libraries for you depending on the version of AWS Glue you are using.
- [Using Delta Lake framework in AWS Glue Studio](https://docs.aws.amazon.com/glue/latest/dg/gs-data-lake-formats-delta.html)
- [Using Apache Iceberg framework in AWS Glue Studio](https://docs.aws.amazon.com/glue/latest/dg/gs-data-lake-formats-iceberg.html)

### [Connecting to data sources](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-data-chapter.html)

Use connections in a Visual ETL job to connect to data.

- [Modifying properties of a data source node](https://docs.aws.amazon.com/glue/latest/dg/edit-jobs-source.html): Edit data source properties in AWS Glue using the tabs in the node details panel for each data source node.
- [Using Data Catalog tables for the data source](https://docs.aws.amazon.com/glue/latest/dg/edit-jobs-source-catalog-tables.html): For all data sources except Amazon S3 and connectors, a table must exist in the AWS Glue Data Catalog for the source type that you choose.
- [Using a connector for the data source](https://docs.aws.amazon.com/glue/latest/dg/edit-jobs-source-connectors.html): If you select a connector for the Node type, follow the instructions at to finish configuring the data source properties.
- [Using files in Amazon S3 for the data source](https://docs.aws.amazon.com/glue/latest/dg/edit-jobs-source-s3-files.html): If you choose Amazon S3 as your data source, then you can choose either:
- [Using a streaming data source](https://docs.aws.amazon.com/glue/latest/dg/edit-jobs-source-streaming.html): You can create streaming extract, transform, and load (ETL) jobs that run continuously and consume data from streaming sources in Amazon Kinesis Data Streams, Apache Kafka, and Amazon Managed Streaming for Apache Kafka (Amazon MSK).
- [References](https://docs.aws.amazon.com/glue/latest/dg/edit-jobs-source-references.html): Best Practices
- [Configuring data target nodes](https://docs.aws.amazon.com/glue/latest/dg/data-target-nodes.html): The data target is where the job writes the transformed data.
- [Editing or uploading a job script](https://docs.aws.amazon.com/glue/latest/dg/edit-nodes-script.html): You can use the script editor in AWS Glue Studio to write your own scripts or to edit either the generated script or an uploaded script.
- [Changing the parent nodes for a node in the job diagram](https://docs.aws.amazon.com/glue/latest/dg/edit-job-change-parents.html): You can change a node's parents to move nodes within the job diagram or to change a data source for a node.
- [Deleting nodes from the job diagram](https://docs.aws.amazon.com/glue/latest/dg/edit-job-delete-node.html): When working with Visual ETL jobs, you can remove nodes from the canvas without having to re-add or restructure any nodes that are connected to the removed node.
- [Adding source and target parameters to the AWS Glue Data Catalog node](https://docs.aws.amazon.com/glue/latest/dg/edit-job-add-job-parameters.html): AWS Glue Studio allows you to parameterize visual jobs.
- [Using Git version control systems in AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/edit-job-add-source-control-integration.html)

### [Authoring code with AWS Glue Studio notebooks](https://docs.aws.amazon.com/glue/latest/dg/notebooks-chapter.html)

Data engineers can author AWS Glue jobs faster and more easily than before using the interactive notebook interface in AWS Glue Studio.

- [Overview of using notebooks](https://docs.aws.amazon.com/glue/latest/dg/using-notebooks-overview.html): AWS Glue Studio allows you to interactively author jobs in a notebook interface based on Jupyter Notebooks.
- [Creating an ETL job using notebooks in AWS Glue Studio](https://docs.aws.amazon.com/glue/latest/dg/create-notebook-job.html)
- [Notebook editor components](https://docs.aws.amazon.com/glue/latest/dg/notebook-components.html): The notebook editor interface has the following main sections.
- [Saving your notebook and job script](https://docs.aws.amazon.com/glue/latest/dg/save-notebook.html): You can save your notebook and the job script you are creating at any time.
- [Managing notebook sessions](https://docs.aws.amazon.com/glue/latest/dg/manage-notebook-sessions.html): Notebooks in AWS Glue Studio are based on the interactive sessions feature of AWS Glue.
- [Using Amazon Q Developer with AWS Glue Studio notebooks](https://docs.aws.amazon.com/glue/latest/dg/glue-studio-notebooks-amazon-q-developer.html): Amazon Q Developer is an AI code companion tool that performs generative AI to assist developers by suggesting recommendations in the code.
- [Monitoring job runs](https://docs.aws.amazon.com/glue/latest/dg/view-job-runs.html): AWS Glue ETL job run status descriptions.
- [Detect and process sensitive data](https://docs.aws.amazon.com/glue/latest/dg/detect-PII.html): AWS Glue Studio provides the ability to detect and mask or remove Personal Identifiable Information (PII) using the Detect PII transform.
- [Managing jobs](https://docs.aws.amazon.com/glue/latest/dg/managing-jobs-chapter.html): AWS Glue Studio provides a simple interface for managing your ETL jobs.


## [Working with jobs](https://docs.aws.amazon.com/glue/latest/dg/author-glue-job.html)

### [AWS Glue versions](https://docs.aws.amazon.com/glue/latest/dg/release-notes.html)

Release notes for AWS Glue describing the contents and usage notes for each AWS Glue version.

- [AWS Glue version support policy](https://docs.aws.amazon.com/glue/latest/dg/glue-version-support-policy.html): Describes the end of life support policies applicable to AWS Glue versions.
- [Migrating AWS Glue for Spark jobs to AWS Glue version 5.1](https://docs.aws.amazon.com/glue/latest/dg/migrating-version-51.html): Describes migrating Apache Spark ETL jobs to AWS Glue version 5.1.
- [Migrating AWS Glue for Spark jobs to AWS Glue version 5.0](https://docs.aws.amazon.com/glue/latest/dg/migrating-version-50.html): Describes migrating Apache Spark ETL jobs to AWS Glue version 5.0.
- [Migrating AWS Glue for Spark jobs to AWS Glue version 4.0](https://docs.aws.amazon.com/glue/latest/dg/migrating-version-40.html): Describes migrating Apache Spark ETL jobs to AWS Glue version 4.0.
- [Upgrade analysis with AI](https://docs.aws.amazon.com/glue/latest/dg/upgrade-analysis.html): The following sections provide information on how to upgrade jobs automatically in AWS Glue.

### [Working with Spark jobs](https://docs.aws.amazon.com/glue/latest/dg/etl-jobs-section.html)

Provides information on AWS Glue for Spark ETL jobs

- [Job parameters](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-glue-arguments.html): Job parameters supported by AWS Glue.

### [Spark and PySpark jobs](https://docs.aws.amazon.com/glue/latest/dg/spark_and_pyspark.html)

The following sections provide information on AWS Glue Spark and PySpark jobs.

- [Configuring Spark job properties](https://docs.aws.amazon.com/glue/latest/dg/add-job.html): Learn about how to configure Spark jobs in AWS Glue and the definitions and limitations of each property.
- [Editing Spark scripts](https://docs.aws.amazon.com/glue/latest/dg/edit-script-spark.html): Learn how to define and edit an ETL script in AWS Glue.
- [Jobs (legacy)](https://docs.aws.amazon.com/glue/latest/dg/console-edit-script.html): Learn about editing scripts using the script editor in the AWS Glue console.
- [Tracking processed data using job bookmarks](https://docs.aws.amazon.com/glue/latest/dg/monitor-continuations.html): AWS Glue uses job bookmarks to track data that has already been processed.

### [Storing Spark shuffle data](https://docs.aws.amazon.com/glue/latest/dg/monitor-spark-shuffle-manager.html)

Shuffling is an important step in a Spark job whenever data is rearranged between partitions.

- [Cloud Shuffle Storage Plugin for Apache Spark](https://docs.aws.amazon.com/glue/latest/dg/cloud-shuffle-storage-plugin.html): Describes the Cloud Shuffle Storage Plugin for Apache Spark.

### [Monitoring Spark jobs](https://docs.aws.amazon.com/glue/latest/dg/monitor-spark.html)

Learn how to automate the running of your system using metrics about crawlers and jobs in AWS Glue.

### [Monitoring with the Spark UI](https://docs.aws.amazon.com/glue/latest/dg/monitor-spark-ui.html)

Use the Apache Spark web UI to monitor and debug AWS Glue ETL jobs running on the AWS Glue job system, and Spark applications running on AWS Glue development endpoints.

- [Enabling the Spark UI for jobs](https://docs.aws.amazon.com/glue/latest/dg/monitor-spark-ui-jobs.html): Configure jobs with the Spark UI on the AWS Glue console or the AWS CLI.
- [Launching the Spark history server](https://docs.aws.amazon.com/glue/latest/dg/monitor-spark-ui-history.html): Use AWS CloudFormation or Docker to launch the Spark history server and view the Spark web UI.
- [Monitoring with AWS Glue job run insights](https://docs.aws.amazon.com/glue/latest/dg/monitor-job-insights.html): Use AWS Glue job run insights to simplify job debugging and optimization for your AWS Glue jobs.

### [Monitoring with CloudWatch](https://docs.aws.amazon.com/glue/latest/dg/monitor-cloudwatch.html)

Use Amazon CloudWatch to collect and process raw data from AWS Glue into readable, near-real-time metrics.

- [Using CloudWatch metrics](https://docs.aws.amazon.com/glue/latest/dg/monitoring-awsglue-with-cloudwatch-metrics.html): Monitor AWS Glue operations using CloudWatch metrics.
- [Setting up Amazon CloudWatch alarms on AWS Glue job profiles](https://docs.aws.amazon.com/glue/latest/dg/monitor-profile-glue-job-cloudwatch-alarms.html): You can investigate run-time problems with AWS Glue jobs.

### [Logging for AWS Glue jobs](https://docs.aws.amazon.com/glue/latest/dg/monitor-continuous-logging.html)

AWS Glue 5.0 automatically enables real-time logging for all AWS Glue 5.0 jobs.

- [Enabling continuous logging for AWS Glue 4.0 and earlier jobs](https://docs.aws.amazon.com/glue/latest/dg/monitor-continuous-logging-enable.html): Enable continuous logging of real-time information about AWS Glue 4.0 and earlier jobs.
- [Viewing logs for AWS Glue jobs](https://docs.aws.amazon.com/glue/latest/dg/monitor-continuous-logging-view.html): View real-time logs for AWS Glue jobs.
- [Monitoring with AWS Glue Observability metrics](https://docs.aws.amazon.com/glue/latest/dg/monitor-observability.html): Use AWS Glue Observability metrics to generate insights into what is happening inside your AWS Glue for Apache Spark jobs to improve triaging and analysis of issues.

### [Job monitoring and debugging](https://docs.aws.amazon.com/glue/latest/dg/monitor-profile-glue-job-cloudwatch-metrics.html)

You can investigate run-time problems with AWS Glue jobs.

- [Debugging OOM exceptions and job abnormalities](https://docs.aws.amazon.com/glue/latest/dg/monitor-profile-debug-oom-abnormalities.html): Debug out-of-memory exceptions and job abnormalities in AWS Glue.
- [Debugging demanding stages and straggler tasks](https://docs.aws.amazon.com/glue/latest/dg/monitor-profile-debug-straggler.html): You can use AWS Glue job profiling to identify demanding stages and straggler tasks in your jobs.
- [Monitoring the progress of multiple jobs](https://docs.aws.amazon.com/glue/latest/dg/monitor-debug-multiple.html): You can profile multiple AWS Glue jobs together and monitor the flow of data between them.
- [Monitoring for DPU capacity planning](https://docs.aws.amazon.com/glue/latest/dg/monitor-debug-capacity.html): Use the job metrics to estimate the number of data processing units (DPUs) that can be used to scale out an AWS Glue job.
- [Troubleshooting Spark jobs with AI](https://docs.aws.amazon.com/glue/latest/dg/troubleshoot-spark.html): The following sections provide information on how to debug Spark jobs automatically in AWS Glue.
- [Using materialized views](https://docs.aws.amazon.com/glue/latest/dg/materialized-views.html): AWS Glue version 5.1 and later supports creating and managing Apache Iceberg materialized views in the AWS Glue Data Catalog.
- [Worker types](https://docs.aws.amazon.com/glue/latest/dg/worker-types.html): Learn about AWS Glue worker types, their specifications, and how to choose the right worker type for your workload.
- [Streaming ETL jobs](https://docs.aws.amazon.com/glue/latest/dg/add-job-streaming.html): Define the job properties for streaming ETL jobs in AWS Glue.

### [Record matching with FindMatches](https://docs.aws.amazon.com/glue/latest/dg/machine-learning.html)

Use machine learning in AWS Glue as the process to create transforms.

### [Tuning machine learning transforms](https://docs.aws.amazon.com/glue/latest/dg/add-job-machine-learning-transform-tuning.html)

Improve the results of data-cleansing jobs by tuning your machine learning transforms in AWS Glue.

- [Machine learning measurements](https://docs.aws.amazon.com/glue/latest/dg/machine-learning-terminology.html): Measurements that are used to tune a machine learning transform in AWS Glue.
- [Deciding between precision and recall](https://docs.aws.amazon.com/glue/latest/dg/machine-learning-precision-recall-tradeoff.html): Understanding the precision-recall trade-off when tuning your machine learning transforms in AWS Glue.
- [Deciding Between accuracy and cost](https://docs.aws.amazon.com/glue/latest/dg/machine-learning-accuracy-cost-tradeoff.html): Understanding the accuracy-cost trade-off when tuning your machine learning transforms in AWS Glue.
- [Estimating the quality of matches using match confidence scores](https://docs.aws.amazon.com/glue/latest/dg/match-scoring.html): Estimating the quality of matches using match confidence scores.
- [Teaching the Find Matches transform](https://docs.aws.amazon.com/glue/latest/dg/machine-learning-teaching.html): Teach a transform in AWS Glue to determine what should be considered a match and what should not be considered a match.
- [Machine learning transforms](https://docs.aws.amazon.com/glue/latest/dg/console-machine-learning-transforms.html): Add, modify, and view machine learning transforms on the AWS Glue console.
- [Tutorial: Creating a machine learning transform](https://docs.aws.amazon.com/glue/latest/dg/machine-learning-transform-tutorial.html): A step-by-step tutorial for creating and managing a machine learning transform using AWS Glue.
- [Finding incremental matches](https://docs.aws.amazon.com/glue/latest/dg/machine-learning-incremental-matches.html): Finding incremental matches in AWS Glue.
- [Using FindMatches in a visual job](https://docs.aws.amazon.com/glue/latest/dg/find-matches-visual-job.html): Using FindMatches in AWS Glue Studio.
- [Migrate Spark programs](https://docs.aws.amazon.com/glue/latest/dg/glue-author-migrate-apache-spark.html): Address common challenges encountered while migrating Spark programs to AWS Glue

### [Working with Ray jobs](https://docs.aws.amazon.com/glue/latest/dg/ray-jobs-section.html)

Provides information about AWS Glue for Ray jobs.

- [Ray job parameters](https://docs.aws.amazon.com/glue/latest/dg/author-job-ray-job-parameters.html): Describes the job parameters that you use in Ray jobs.
- [Ray job metrics](https://docs.aws.amazon.com/glue/latest/dg/author-job-ray-monitor.html): Describes how to monitor Ray jobs with CloudWatch metrics.

### [Configuring Python shell job properties](https://docs.aws.amazon.com/glue/latest/dg/add-job-python.html)

Define the job properties for Python shell jobs in AWS Glue, and create files that contain your own Python libraries.

- [Migrate from AWS Glue Python shell jobs](https://docs.aws.amazon.com/glue/latest/dg/pyshell-migration.html): This topic explains how to migrate from AWS Glue Python shell jobs to alternative options.

### [Monitoring](https://docs.aws.amazon.com/glue/latest/dg/monitor-glue.html)

Learn how to automate the running of your system using metrics about crawlers and jobs in AWS Glue.

- [AWS tags](https://docs.aws.amazon.com/glue/latest/dg/monitor-tags.html): You can use tags in AWS Glue to organize and identify your resources.
- [Automating with EventBridge](https://docs.aws.amazon.com/glue/latest/dg/automating-awsglue-with-cloudwatch-events.html): Automate AWS Glue with other AWS services by using EventBridge.
- [Monitoring resources](https://docs.aws.amazon.com/glue/latest/dg/monitor-resource-metrics.html): AWS Glue resource monitoring.
- [Logging using CloudTrail](https://docs.aws.amazon.com/glue/latest/dg/monitor-cloudtrail.html): >Learn about logging AWS Glue with AWS CloudTrail.


## [AWS Glue Streaming](https://docs.aws.amazon.com/glue/latest/dg/streaming-chapter.html)

- [Tutorial: Build your first streaming workload using AWS Glue Studio](https://docs.aws.amazon.com/glue/latest/dg/streaming-tutorial-studio.html): A tutorial for AWS Glue Streaming using AWS Glue Studio.
- [Tutorial: Build your first streaming workload using AWS Glue Studio notebooks](https://docs.aws.amazon.com/glue/latest/dg/streaming-tutorial-studio-notebooks.html): A tutorial for AWS Glue Streaming using AWS Glue Studio notebooks.
- [Streaming concepts](https://docs.aws.amazon.com/glue/latest/dg/glue-streaming-concepts.html): The following sections provide information on concepts of AWS Glue Streaming.
- [Streaming connections](https://docs.aws.amazon.com/glue/latest/dg/glue-streaming-connections.html): The following sections provide information on how to use connections in AWS Glue Streaming.
- [AWS Glue streaming autoscaling](https://docs.aws.amazon.com/glue/latest/dg/glue-streaming-auto-scaling.html): The following sections provide information on AWS Glue streaming autoscaling
- [Maintenance windows](https://docs.aws.amazon.com/glue/latest/dg/glue-streaming-maintenance.html): The following topic provides information on maintenance windows for AWS Glue Streaming.
- [Advanced AWS Glue streaming concepts](https://docs.aws.amazon.com/glue/latest/dg/glue-streaming-advanced-concepts.html): Describes advanced streaming concepts in AWS Glue.

### [Monitoring AWS Glue streaming jobs](https://docs.aws.amazon.com/glue/latest/dg/glue-streaming-monitoring.html)

The following sections provide information on monitoring AWS Glue streaming jobs.

- [Visualizing AWS Glue streaming metrics](https://docs.aws.amazon.com/glue/latest/dg/glue-streaming-monitoring-visualizing.html): To plot visual metrics:
- [Using AWS Glue streaming metrics](https://docs.aws.amazon.com/glue/latest/dg/glue-streaming-monitoring-metrics.html): This section describes each of the metrics and how they co-relate with each other.


## [Zero-ETL integrations](https://docs.aws.amazon.com/glue/latest/dg/zero-etl-using.html)

- [Prerequisites](https://docs.aws.amazon.com/glue/latest/dg/zero-etl-prerequisites.html): Setting up an integration between the source and target require some prerequisites such as configuring IAM roles which AWS Glue uses to access data from the source and write to the target, and the use of KMS keys to encrypt the data in intermediate or the target location.

### [Configuring a source](https://docs.aws.amazon.com/glue/latest/dg/zero-etl-sources.html)

- [Unsupported Salesforce fields](https://docs.aws.amazon.com/glue/latest/dg/zero-etl-config-source-salesforce-unsupported-entities.html): The following Salesforce entities or fields are unsupported for use in a zero-ETL integration with a Salesforce source.
- [Unsupported SAP entities](https://docs.aws.amazon.com/glue/latest/dg/zero-etl-config-source-sap-unsupported-entities.html): The following SAP entity types are unsupported for use in a zero-ETL integration with an SAP source.
- [Unsupported ServiceNow fields](https://docs.aws.amazon.com/glue/latest/dg/zero-etl-config-source-servicenow-unsupported-entities.html): The following ServiceNow entities or fields are unsupported for use in a zero-ETL integration with a ServiceNow source.
- [Configuring a target](https://docs.aws.amazon.com/glue/latest/dg/zero-etl-target.html): There are several options offered by AWS when configuring a target for a zero-ETL integration.

### [Partition and schema unnesting](https://docs.aws.amazon.com/glue/latest/dg/zero-etl-partition-schema-unnesting.html)

Configure and manage partitioning and schema unnesting for Zero-ETL integrations with AWS Glue.

- [Schema unnesting](https://docs.aws.amazon.com/glue/latest/dg/zero-etl-ddb-schema-unnesting.html): Configure and manage schema unnesting for Zero-ETL integrations with AWS Glue.
- [Data partitioning](https://docs.aws.amazon.com/glue/latest/dg/zero-etl-data-partitioning.html): Configure and manage partitioning for Zero-ETL integrations with AWS Glue.
- [Limitations](https://docs.aws.amazon.com/glue/latest/dg/limitations.html)
- [Common tasks](https://docs.aws.amazon.com/glue/latest/dg/zero-etl-common-integration-tasks.html)
- [Using APIs](https://docs.aws.amazon.com/glue/latest/dg/zero-etl-using-apis.html): You can use the following APIs to create and manage Zero-ETL integrations in AWS Glue:
- [Monitoring an integration](https://docs.aws.amazon.com/glue/latest/dg/zero-etl-monitoring.html)
- [Limitations](https://docs.aws.amazon.com/glue/latest/dg/zero-etl-limitations.html): The following are general limitations of or considerations about zero-ETL integrations:


## [AWS Glue Data Quality](https://docs.aws.amazon.com/glue/latest/dg/glue-data-quality.html)

- [Anomaly detection in AWS Glue Data Quality](https://docs.aws.amazon.com/glue/latest/dg/data-quality-anomaly-detection.html): This topic describes how to use anomaly detection in AWS Glue Data Quality.
- [IAM permissions for AWS Glue Data Quality](https://docs.aws.amazon.com/glue/latest/dg/data-quality-authorization.html): This topic provides information to help you understand the actions and resources that you can use in an IAM policy for AWS Glue Data Quality.
- [Getting started with AWS Glue Data Quality for the Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/data-quality-getting-started.html): This tutorial covers the basic use of AWS Glue Data Quality on the AWS Glue console.

### [Evaluating data quality with AWS Glue Studio](https://docs.aws.amazon.com/glue/latest/dg/data-quality-gs-studio.html)

This topic references a topic about using AWS Glue Data Quality in AWS Glue Studio.

- [Evaluating data quality for ETL jobs in AWS Glue Studio](https://docs.aws.amazon.com/glue/latest/dg/tutorial-data-quality.html): Learn how to get started with AWS Glue Data Quality by creating rulesets on tables in your Data Catalog, running and automating data quality on your jobs, and monitoring changes to your datasets as they evolve over time.
- [Data Quality rule builder](https://docs.aws.amazon.com/glue/latest/dg/data-quality-rule-builder.html): With the Data Quality Definition Language (DQDL) rule builder, you can create data quality rules to evaluate your data.
- [Configuring anomaly detection in AWS Glue ETL jobs](https://docs.aws.amazon.com/glue/latest/dg/data-quality-configuring-anomaly-detection-etl-jobs.html): AWS Glue Data Quality analyzes data statistics gathered over time to detect anomalies and generates observations of the anomalous patterns and recommends rules to monitor them every time the job is run.
- [Viewing data quality scores and anomalies](https://docs.aws.amazon.com/glue/latest/dg/data-quality-viewing-scores-and-anomalies.html): AWS Glue Data Quality analyzes data statistics gathered over time to detect anomalies and generates observations of the anomalous patterns and recommends rules to monitor them every time the job is run.
- [Data Quality for ETL jobs in AWS Glue Studio notebooks](https://docs.aws.amazon.com/glue/latest/dg/data-quality-gs-studio-notebooks.html): This topic references a topic about using AWS Glue Data Quality in AWS Glue Studio notebooks.

### [Data Quality Definition Language (DQDL) reference](https://docs.aws.amazon.com/glue/latest/dg/dqdl.html)

This guide introduces the Data Quality Definition Language (DQDL) for AWS Glue Data Quality, and provides a DQDL reference with syntax and examples.

### [Rule type reference](https://docs.aws.amazon.com/glue/latest/dg/dqdl-rule-types.html)

A reference for each rule type that AWS Glue Data Quality supports.

- [AggregateMatch](https://docs.aws.amazon.com/glue/latest/dg/dqdl-rule-types-AggregateMatch.html): Checks the ratio of two column aggregations against a given expression.
- [ColumnCorrelation](https://docs.aws.amazon.com/glue/latest/dg/dqdl-rule-types-ColumnCorrelation.html): Checks the correlation between two columns against a given expression.
- [ColumnCount](https://docs.aws.amazon.com/glue/latest/dg/dqdl-rule-types-ColumnCount.html): Checks the column count of the primary dataset against a given expression.
- [ColumnDataType](https://docs.aws.amazon.com/glue/latest/dg/dqdl-rule-types-ColumnDataType.html): Checks if the values in a given column can be cast in Apache Spark to the provided type.
- [ColumnExists](https://docs.aws.amazon.com/glue/latest/dg/dqdl-rule-types-ColumnExists.html): Checks whether a column exists.
- [ColumnLength](https://docs.aws.amazon.com/glue/latest/dg/dqdl-rule-types-ColumnLength.html): Checks whether the length of each row in a column conforms to a given expression.
- [ColumnNamesMatchPattern](https://docs.aws.amazon.com/glue/latest/dg/dqdl-rule-types-ColumnNamesMatchPattern.html): Checks whether the names of all columns in the primary dataset match the given regular expression.
- [ColumnValues](https://docs.aws.amazon.com/glue/latest/dg/dqdl-rule-types-ColumnValues.html): Runs an expression against the values in a column.
- [Completeness](https://docs.aws.amazon.com/glue/latest/dg/dqdl-rule-types-Completeness.html): Checks the percentage of complete (non-null) values in a column against a given expression.
- [CustomSQL](https://docs.aws.amazon.com/glue/latest/dg/dqdl-rule-types-CustomSql.html): This rule type has been extended to support two use cases:
- [DataFreshness](https://docs.aws.amazon.com/glue/latest/dg/dqdl-rule-types-DataFreshness.html): Checks the freshness of data in a column by evaluating the difference between the current time and the values of a date column.
- [DatasetMatch](https://docs.aws.amazon.com/glue/latest/dg/dqdl-rule-types-DatasetMatch.html): Checks if the data in the primary dataset matches the data in a reference dataset.
- [DistinctValuesCount](https://docs.aws.amazon.com/glue/latest/dg/dqdl-rule-types-DistinctValuesCount.html): Checks the number of distinct values in a column against a given expression.
- [Entropy](https://docs.aws.amazon.com/glue/latest/dg/dqdl-rule-types-Entropy.html): Checks whether the entropy value of a column matches a given expression.
- [IsComplete](https://docs.aws.amazon.com/glue/latest/dg/dqdl-rule-types-IsComplete.html): Checks whether all of the values in a column are complete (non-null).
- [IsPrimaryKey](https://docs.aws.amazon.com/glue/latest/dg/dqdl-rule-types-IsPrimaryKey.html): Checks whether a column contains a primary key.
- [IsUnique](https://docs.aws.amazon.com/glue/latest/dg/dqdl-rule-types-IsUnique.html): Checks whether all of the values in a column are unique, and returns a Boolean value.
- [Mean](https://docs.aws.amazon.com/glue/latest/dg/dqdl-rule-types-Mean.html): Checks whether the mean (average) of all the values in a column matches a given expression.
- [ReferentialIntegrity](https://docs.aws.amazon.com/glue/latest/dg/dqdl-rule-types-ReferentialIntegrity.html): Checks to what extent the values of a set of columns in the primary dataset are a subset of the values of a set of columns in a reference dataset.
- [RowCount](https://docs.aws.amazon.com/glue/latest/dg/dqdl-rule-types-RowCount.html): Checks the row count of a dataset against a given expression.
- [RowCountMatch](https://docs.aws.amazon.com/glue/latest/dg/dqdl-rule-types-RowCountMatch.html): Checks the ratio of the row count of the primary dataset and the row count of a reference dataset against the given expression.
- [StandardDeviation](https://docs.aws.amazon.com/glue/latest/dg/dqdl-rule-types-StandardDeviation.html): Checks the standard deviation of all of the values in a column against a given expression.
- [Sum](https://docs.aws.amazon.com/glue/latest/dg/dqdl-rule-types-Sum.html): Checks the sum of all the values in a column against a given expression.
- [SchemaMatch](https://docs.aws.amazon.com/glue/latest/dg/dqdl-rule-types-SchemaMatch.html): Checks if the schema of the primary dataset matches the schema of a reference dataset.
- [Uniqueness](https://docs.aws.amazon.com/glue/latest/dg/dqdl-rule-types-Uniqueness.html): Checks the percentage of unique values in a column against a given expression.
- [UniqueValueRatio](https://docs.aws.amazon.com/glue/latest/dg/dqdl-rule-types-UniqueValueRatio.html): Checks the unique value ratio of a column against a given expression.
- [DetectAnomalies](https://docs.aws.amazon.com/glue/latest/dg/dqdl-rule-types-DetectAnomalies.html): Detects anomalies for a given data quality rule.
- [FileFreshness](https://docs.aws.amazon.com/glue/latest/dg/dqdl-rule-types-FileFreshness.html): FileFreshness ensures your data files are fresh based on the condition you provide.
- [FileMatch](https://docs.aws.amazon.com/glue/latest/dg/dqdl-rule-types-FileMatch.html): The FileMatch rule allows you to compare files against other files or checksums.
- [FileUniqueness](https://docs.aws.amazon.com/glue/latest/dg/dqdl-rule-types-FileUniqueness.html): File Uniqueness allows you to ensure that there are no duplicate files in the data you have received from your data producers.
- [FileSize](https://docs.aws.amazon.com/glue/latest/dg/dqdl-rule-types-FileSize.html): The FileSize ruletype allows you to ensure that files meet a certain file size criteria.
- [Using APIs to measure and manage data quality](https://docs.aws.amazon.com/glue/latest/dg/data-quality-using-apis.html): This topic describes how to use APIs to measure and manage data quality.
- [Setting up alerts, deployments, and scheduling](https://docs.aws.amazon.com/glue/latest/dg/data-quality-alerts.html): This topic describes how to set up alerts, deployments, and scheduling for AWS Glue Data Quality.
- [Data encryption at rest for AWS Glue Data Quality](https://docs.aws.amazon.com/glue/latest/dg/data-quality-encryption.html): AWS Glue Data Quality provides encryption by default to protect sensitive customer data at rest using AWS owned encryption keys.
- [Troubleshooting AWS Glue Data Quality errors](https://docs.aws.amazon.com/glue/latest/dg/data-quality-trouble.html): This topic describes how to troubleshoot AWS Glue Data Quality errors.


## [Amazon Q data integration in AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/q.html)

### [Setting up Amazon Q data integration](https://docs.aws.amazon.com/glue/latest/dg/q-setting-up.html)

The following sections provide information setting up Amazon Q data integration in AWS Glue.

- [Configuring IAM permissions](https://docs.aws.amazon.com/glue/latest/dg/q-setting-up-permissions.html): This topic describes the IAM permissions that you configure for the Amazon Q chat experience, and the AWS Glue Studio notebook experience.
- [Supported code generation](https://docs.aws.amazon.com/glue/latest/dg/q-supported-actions.html): The following are the combinations of the code generation abilities of Amazon Q data integration.
- [Example interactions](https://docs.aws.amazon.com/glue/latest/dg/q-using-example-interactions.html): Amazon Q data integration in AWS Glue allows you enter your question in the Amazon Q panel.
- [Using context awareness](https://docs.aws.amazon.com/glue/latest/dg/q-context-awareness.html): AWS Glue provides context awareness when creating ETL jobs in AWS Glue.


## [Orchestration](https://docs.aws.amazon.com/glue/latest/dg/etl-jobs.html)

### [Starting jobs and crawlers using triggers](https://docs.aws.amazon.com/glue/latest/dg/trigger-job.html)

Use AWS Glue triggers to start jobs and crawlers based on a schedule or event, or on demand.

- [AWS Glue triggers](https://docs.aws.amazon.com/glue/latest/dg/about-triggers.html): Use AWS Glue triggers to start specified jobs and crawlers on demand, based on a schedule, or based on a combination of events.

### [Adding triggers](https://docs.aws.amazon.com/glue/latest/dg/console-triggers.html)

Learn how to add a trigger using the AWS Glue console and AWS Command Line Interface.

- [Time-based schedules for jobs and crawlers](https://docs.aws.amazon.com/glue/latest/dg/monitor-data-warehouse-schedule.html): AWS Glue uses cron expressions to define time-based schedules for jobs and crawlers.
- [Activating and deactivating triggers](https://docs.aws.amazon.com/glue/latest/dg/activate-triggers.html): Learn how to activate and deactivate a trigger using the AWS Glue console and the AWS Command Line Interface.

### [Performing complex ETL activities using blueprints and workflows](https://docs.aws.amazon.com/glue/latest/dg/orchestrate-using-workflows.html)

Use workflows in AWS Glue to encapsulate a set of related ETL jobs, crawlers, and triggers into a single exectuable and trackable entity.

- [Overview of workflows](https://docs.aws.amazon.com/glue/latest/dg/workflows_overview.html): Use workflows in AWS Glue to create and visualize complex ETL activities involving multiple crawlers, jobs, and triggers.
- [Creating and building out a workflow manually](https://docs.aws.amazon.com/glue/latest/dg/creating_running_workflows.html): Use the AWS Glue console to create and build out a workflow one node at a time.
- [Starting a workflow with an EventBridge event](https://docs.aws.amazon.com/glue/latest/dg/starting-workflow-eventbridge.html): Start an AWS Glue workflow by using Amazon EventBridge.
- [Viewing the EventBridge events that started a workflow](https://docs.aws.amazon.com/glue/latest/dg/viewing-start-event-info.html): View information about the Amazon EventBridge event or events that started a workflow.
- [Running and monitoring a workflow](https://docs.aws.amazon.com/glue/latest/dg/running_monitoring_workflow.html): If the start trigger for a workflow is an on-demand trigger, you can start the workflow from the AWS Glue console.
- [Stopping a workflow run](https://docs.aws.amazon.com/glue/latest/dg/workflow-stopping.html): You can stop a running workflow to immediately terminate all running jobs and crawlers and prevent downstream jobs and crawlers from running.
- [Repairing and resuming a workflow run](https://docs.aws.amazon.com/glue/latest/dg/resuming-workflow.html): If one or more nodes in a workflow do not successfully complete, you can determine the reasons, correct them, and then resume the workflow run from those nodes.
- [Getting and setting workflow run properties](https://docs.aws.amazon.com/glue/latest/dg/workflow-run-properties-code.html): Review this sample code that shows how to programmatically get and set workflow run properties.
- [Querying workflows using the AWS Glue API](https://docs.aws.amazon.com/glue/latest/dg/workflows_api_concepts.html): Use the AWS Glue API to query workflows, including a static view or a dynamic view of a running workflow.
- [Blueprint and workflow restrictions](https://docs.aws.amazon.com/glue/latest/dg/blueprint_workflow_restrictions.html): Keep these restrictions in mind when you're working with workflows and blueprints.
- [Troubleshooting blueprint errors](https://docs.aws.amazon.com/glue/latest/dg/blueprint_workflow_troubleshoot.html): If you encounter errors when using AWS Glue blueprints, use the following solutions to help you find the source of the problems and fix them.
- [Permissions for blueprint personas and roles](https://docs.aws.amazon.com/glue/latest/dg/blueprints-personas-permissions.html): Suggested AWS Identity and Access Management (IAM) permissions for personas and roles that create and run AWS Glue blueprints.

### [Developing blueprints](https://docs.aws.amazon.com/glue/latest/dg/orchestrate-using-blueprints.html)

Use workflows in AWS Glue to encapsulate a set of related ETL jobs, crawlers, and triggers into a single exectuable and trackable entity.

- [Overview of blueprints](https://docs.aws.amazon.com/glue/latest/dg/blueprints-overview.html): Use blueprints in AWS Glue to create workflows for complex extract, transform, and load (ETL) processes.

### [Developing blueprints](https://docs.aws.amazon.com/glue/latest/dg/developing-blueprints.html)

Use downloadable AWS libraries to develop and test AWS Glue blueprints.

- [Overview of developing blueprints](https://docs.aws.amazon.com/glue/latest/dg/developing-blueprints-overview.html): The first step in your development process is to identify a common use case that would benefit from a blueprint.
- [Prerequisites for developing blueprints](https://docs.aws.amazon.com/glue/latest/dg/developing-blueprints-prereq.html): To develop blueprints, you should be familiar with using AWS Glue and writing scripts for Apache Spark ETL jobs or Python shell jobs.

### [Writing the blueprint code](https://docs.aws.amazon.com/glue/latest/dg/developing-blueprints-code.html)

Each blueprint project that you create must contain at a minimum the following files:

- [Creating the blueprint layout script](https://docs.aws.amazon.com/glue/latest/dg/developing-blueprints-code-layout.html): The blueprint layout script must include a function that generates the entities in your workflow.
- [Creating the configuration file](https://docs.aws.amazon.com/glue/latest/dg/developing-blueprints-code-config.html): The blueprint configuration file is a required file that defines the script entry point for generating the workflow, and the parameters that the blueprint accepts.
- [Specifying blueprint parameters](https://docs.aws.amazon.com/glue/latest/dg/developing-blueprints-code-parameters.html): The configuration file contains blueprint parameter specifications in a parameterSpec JSON object. parameterSpec contains one or more parameter objects.
- [Sample blueprint project](https://docs.aws.amazon.com/glue/latest/dg/developing-blueprints-sample.html): Data format conversion is a frequent extract, transform, and load (ETL) use case.
- [Testing a blueprint](https://docs.aws.amazon.com/glue/latest/dg/developing-blueprints-testing.html): While you develop your code, you should perform local testing to verify that the workflow layout is correct.
- [Publishing a blueprint](https://docs.aws.amazon.com/glue/latest/dg/developing-blueprints-publishing.html): After you develop a blueprint, you must upload it to Amazon S3.
- [Blueprint classes reference](https://docs.aws.amazon.com/glue/latest/dg/developing-blueprints-code-classes.html): The libraries for AWS Glue blueprints define three classes that you use in your workflow layout script: Job, Crawler, and Workflow.
- [Blueprint samples](https://docs.aws.amazon.com/glue/latest/dg/developing-blueprints-samples.html): There are a number of sample blueprint projects available on the AWS Glue blueprint Github repository.
- [Registering a blueprint](https://docs.aws.amazon.com/glue/latest/dg/registering-blueprints.html): Register a blueprint with AWS Glue to make the blueprint available for use.
- [Viewing blueprints](https://docs.aws.amazon.com/glue/latest/dg/viewing_blueprints.html): View a blueprint to review blueprint description, status, and parameter specifications, and to download the ZIP archive that the blueprint was created from.
- [Updating a blueprint](https://docs.aws.amazon.com/glue/latest/dg/updating_blueprints.html): Update a blueprint when you have a revised script or set of blueprint parameters.
- [Creating a workflow from a blueprint](https://docs.aws.amazon.com/glue/latest/dg/creating_workflow_blueprint.html): Create a workflow from an AWS Glue blueprint to design a complex extract, transform, and load (ETL) process.
- [Viewing blueprint runs](https://docs.aws.amazon.com/glue/latest/dg/viewing_blueprint_runs.html): View a blueprint run to see the associated workflow name and blueprint parameters, and the status of the workflow creation operation.


## [AWS Glue programming guide](https://docs.aws.amazon.com/glue/latest/dg/edit-script.html)

- [Providing your own custom scripts](https://docs.aws.amazon.com/glue/latest/dg/console-custom-created.html): Use AWS Glue Studio to provide your own custom ETL scripts in AWS Glue.

### [AWS Glue for Spark](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming.html)

How to program Spark ETL scripts using the AWS Glue API.

- [Tutorial: Writing a Spark script](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-intro-tutorial.html): Provides an introduction to writing an AWS Glue Apache Spark script.

### [ETL in PySpark](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python.html)

How to use Python to program AWS Glue ETL scripts.

- [Python setup](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-setup.html): How to set up your environment to use Python with AWS Glue.
- [Calling APIs](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-calling.html): How to call AWS Glue APIs from Python.
- [Python libraries](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-libraries.html): How to using Python libraries with AWS Glue.

### [Python samples](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-samples.html)

Various sample programs using Python and AWS Glue.

- [Join and relationalize sample](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-samples-legislators.html): Shows how to use AWS Glue to parse, load, and transform data stored in Amazon S3.
- [Data preparation sample](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-samples-medicaid.html): Shows how to use AWS Glue to clean and transform data stored in Amazon S3.

### [PySpark extensions](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-extensions.html)

PySpark Extensions Reference.

- [getResolvedOptions](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-pyspark-extensions-get-resolved-options.html): How to use getResolvedOptions to access parameters within an ETL script.
- [Types](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-pyspark-extensions-types.html): Types used by the AWS Glue PySpark extensions.
- [DynamicFrame](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-pyspark-extensions-dynamic-frame.html): Overview of the AWS Glue DynamicFrame Python class.
- [DynamicFrameCollection](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-pyspark-extensions-dynamic-frame-collection.html): Overview of the AWS Glue DynamicFrameCollection Python class.
- [DynamicFrameWriter](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-pyspark-extensions-dynamic-frame-writer.html): Describes the pySpark extensions DynamicFrameWriter Class.
- [DynamicFrameReader](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-pyspark-extensions-dynamic-frame-reader.html): Describes the pySpark extensions DynamicFrameReader class.
- [GlueContext](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-pyspark-extensions-glue-context.html): The GlueContext class wraps the Apache Spark SparkContext object in AWS Glue.

### [PySpark transforms](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-transforms.html)

PySpark Transforms Reference.

- [GlueTransform](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-pyspark-transforms-GlueTransform.html): GlueTransform is the base class for all the AWS Glue transform classes.
- [ApplyMapping](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-pyspark-transforms-ApplyMapping.html): The ApplyMapping class applies a mapping within a DynamicFrame in AWS Glue.
- [DropFields](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-pyspark-transforms-DropFields.html): Use the DropFields class to drop fields within a DynamicFrame in AWS Glue.
- [DropNullFields](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-pyspark-transforms-DropNullFields.html): The DropNullFields class drops all null fields whose type is NullType in this DynamicFrame in AWS Glue.
- [ErrorsAsDynamicFrame](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-pyspark-transforms-ErrorsAsDynamicFrame.html): The ErrorsAsDynamicFrame class returns a DynamicFrame that contains nested error records for errors that occurred during the creation of the source DynamicFrame in AWS Glue.
- [EvaluateDataQuality](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-pyspark-transforms-EvaluateDataQuality.html): The EvaluateDataQuality class evaluates a data quality ruleset against the data in a DynamicFrame, and returns a new DynamicFrame with results of the data quality evaluation.
- [FillMissingValues](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-pyspark-transforms-fillmissingvalues.html): The FillMissingValues class fills null values and empty strings in a specified DynamicFrame column using machine learning.
- [Filter](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-pyspark-transforms-filter.html): The Filter class builds a new DynamicFrame that contains records from the input DynamicFrame that satisfy a specified predicate function.
- [FindIncrementalMatches](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-pyspark-transforms-findincrementalmatches.html): The FindIncrementalMatches class identifies matching records in the existing and incremental DynamicFrame and creates a new DynamicFrame with a unique identifier assigned to each group of matching records.
- [FindMatches](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-pyspark-transforms-findmatches.html): The FindMatches class identifies matching records in the input DynamicFrame and creates a new DynamicFrame with a unique identifier assigned to each group of matching records.
- [FlatMap](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-pyspark-transforms-flat-map.html): The FlatMap class applies a transform to each DynamicFrame in a collection and flattens the results in AWS Glue.
- [Join](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-pyspark-transforms-join.html): The Join class performs an equality join on two DynamicFrames in AWS Glue.
- [Map](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-pyspark-transforms-map.html): The Map transform builds a new DynamicFrame by applying a function to all records in the input DynamicFrame.
- [MapToCollection](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-pyspark-transforms-MapToCollection.html): The MapToCollection class applies a transform to each DynamicFrame in the specified DynamicFrameCollection in AWS Glue.
- [Relationalize](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-pyspark-transforms-Relationalize.html): The Relationalize class flattens a nested schema in a DynamicFrame and pivots out array columns from the flattened frame in AWS Glue.
- [RenameField](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-pyspark-transforms-RenameField.html): The RenameField class renames a node within a DynamicFrame in AWS Glue.
- [ResolveChoice](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-pyspark-transforms-ResolveChoice.html): The ResolveChoice class resolves a choice type within a DynamicFrame.
- [SelectFields](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-pyspark-transforms-SelectFields.html): This page provides a reference with examples for the AWS Glue SelectFields class for PySpark.
- [SelectFromCollection](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-pyspark-transforms-SelectFromCollection.html): The SelectFromCollection class selects one DynamicFrame in a DynamicFrameCollection in AWS Glue.
- [Simplify_ddb_json](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-pyspark-transforms-simplify-ddb-json.html): The Simplify_ddb_json class simplifies nested columns in a DynamicFrame that are specifically in the DynamoDB JSON structure, and returns a new simplified DynamicFrame.
- [Spigot](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-pyspark-transforms-spigot.html): The Spigot class writes sample records to a specified destination to help you verify the transformations performed by your AWS Glue job.
- [SplitFields](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-pyspark-transforms-SplitFields.html): The SplitFields class splits a DynamicFrame into two new ones by specified fields in AWS Glue.
- [SplitRows](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-pyspark-transforms-SplitRows.html): The SplitRows class splits a DynamicFrame in two by specified rows in AWS Glue.
- [Unbox](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-pyspark-transforms-Unbox.html): The Unbox class unboxes a string field in a DynamicFrame in AWS Glue.
- [UnnestFrame](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-pyspark-transforms-UnnestFrame.html): The UnnestFrame class unnests a DynamicFrame, flattens nested objects to top-level elements, and generates join keys for array objects in AWS Glue.
- [FlagDuplicatesInColumn](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-pyspark-transforms-FlagDuplicatesInColumn.html): The FlagDuplicatesInColumn transform returns a dataframe with a new column with a specified value in each row that indicates whether the value in the row's source column matches a value in an earlier row of the source column.
- [FormatPhoneNumber](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-pyspark-transforms-FormatPhoneNumber.html): The FormatPhoneNumber transform returns a dataframe with a column in which a phone number string is converted into a formatted value.
- [FormatCase](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-pyspark-transforms-FormatCase.html): The FormatCase transform returns a dataframe and changes each string in a column to the specified case type.
- [FillWithMode](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-pyspark-transforms-FillWithMode.html): The FillWithMode transform returns a dataframe with a column with missing data replaced by the mode of all values.
- [FlagDuplicateRows](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-pyspark-transforms-FlagDuplicateRows.html): The FlagDuplicateRows transform returns a dataframe with a new column with a specified value in each row that indicates whether that row is an exact match of an earlier row in the dataset.
- [RemoveDuplicates](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-pyspark-transforms-RemoveDuplicates.html): The RemoveDuplicates transform returns a dataframe and deletes an entire row, if a duplicate value is encountered in a selected source column.
- [MonthName](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-pyspark-transforms-MonthName.html): The MonthName transform returns a dataframe and creates a new column containing the name of the month, from a string that represents a date.
- [IsEven](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-pyspark-transforms-IsEven.html): The IsEven transform returns dataframe and a Boolean value in a new column that indicates whether the source column or value is even.
- [CryptographicHash](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-pyspark-transforms-CryptographicHash.html): The CryptographicHash transform returns a dataframe and applies an algorithm to hash values in the column.
- [Decrypt](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-pyspark-transforms-Decrypt.html): The Decrypt transform returns a dataframe and decrypts inside of AWS Glue.
- [Encrypt](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-pyspark-transforms-Encrypt.html): The Encrypt transform returns a dataframe and encrypts source columns using the AWS Key Management Service key.
- [IntToIp](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-pyspark-transforms-IntToIp.html): The IntToIp transform returns a dataframe and converts the integer value of source column or other value to the corresponding IPv4 value in then target column, and returns the result in a new column.
- [IpToInt](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-pyspark-transforms-IpToInt.html): The IpToInt transform returns a dataframe and converts the Internet Protocol version 4 (IPv4) value of the source column or other value to the corresponding integer value in the target column, and returns the result in a new column.

### [ETL in Scala](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-scala.html)

How to use Scala to program AWS Glue ETL scripts.

- [Using Scala](https://docs.aws.amazon.com/glue/latest/dg/glue-etl-scala-using.html): How to use Scala to program AWS Glue.
- [Scala script example](https://docs.aws.amazon.com/glue/latest/dg/glue-etl-scala-example.html): Review this scripting example to learn how to work with streaming ETL

### [Scala API list](https://docs.aws.amazon.com/glue/latest/dg/glue-etl-scala-apis.html)

A list of the APIs in the AWS Glue Scala library for scripting ETL jobs.

- [ChoiceOption](https://docs.aws.amazon.com/glue/latest/dg/glue-etl-scala-apis-glue-choiceoption.html)
- [DataSink](https://docs.aws.amazon.com/glue/latest/dg/glue-etl-scala-apis-glue-datasink-class.html)
- [DataSource trait](https://docs.aws.amazon.com/glue/latest/dg/glue-etl-scala-apis-glue-datasource-trait.html): Package:Â com.amazonaws.services.glue

### [DynamicFrame](https://docs.aws.amazon.com/glue/latest/dg/glue-etl-scala-apis-glue-dynamicframe.html)

Package:Â com.amazonaws.services.glue

- [DynamicFrame class](https://docs.aws.amazon.com/glue/latest/dg/glue-etl-scala-apis-glue-dynamicframe-class.html): Package:Â com.amazonaws.services.glue
- [DynamicFrame object](https://docs.aws.amazon.com/glue/latest/dg/glue-etl-scala-apis-glue-dynamicframe-object.html): Package:Â com.amazonaws.services.glue
- [DynamicRecord](https://docs.aws.amazon.com/glue/latest/dg/glue-etl-scala-apis-glue-dynamicrecord-class.html)
- [GlueContext](https://docs.aws.amazon.com/glue/latest/dg/glue-etl-scala-apis-glue-gluecontext.html): Package:Â com.amazonaws.services.glue
- [MappingSpec](https://docs.aws.amazon.com/glue/latest/dg/glue-etl-scala-apis-glue-mappingspec.html): Package:Â com.amazonaws.services.glue
- [ResolveSpec](https://docs.aws.amazon.com/glue/latest/dg/glue-etl-scala-apis-glue-resolvespec.html)
- [ArrayNode](https://docs.aws.amazon.com/glue/latest/dg/glue-etl-scala-apis-glue-types-arraynode.html): Package:Â com.amazonaws.services.glue.types
- [BinaryNode](https://docs.aws.amazon.com/glue/latest/dg/glue-etl-scala-apis-glue-types-binarynode.html): Package:Â com.amazonaws.services.glue.types
- [BooleanNode](https://docs.aws.amazon.com/glue/latest/dg/glue-etl-scala-apis-glue-types-booleannode.html): Package:Â com.amazonaws.services.glue.types
- [ByteNode](https://docs.aws.amazon.com/glue/latest/dg/glue-etl-scala-apis-glue-types-bytenode.html): Package:Â com.amazonaws.services.glue.types
- [DateNode](https://docs.aws.amazon.com/glue/latest/dg/glue-etl-scala-apis-glue-types-datenode.html): Package:Â com.amazonaws.services.glue.types
- [DecimalNode](https://docs.aws.amazon.com/glue/latest/dg/glue-etl-scala-apis-glue-types-decimalnode.html): Package:Â com.amazonaws.services.glue.types
- [DoubleNode](https://docs.aws.amazon.com/glue/latest/dg/glue-etl-scala-apis-glue-types-doublenode.html): Package:Â com.amazonaws.services.glue.types
- [DynamicNode](https://docs.aws.amazon.com/glue/latest/dg/glue-etl-scala-apis-glue-types-dynamicnode.html)
- [EvaluateDataQuality](https://docs.aws.amazon.com/glue/latest/dg/glue-etl-scala-apis-glue-dq-EvaluateDataQuality.html)
- [FloatNode](https://docs.aws.amazon.com/glue/latest/dg/glue-etl-scala-apis-glue-types-floatnode.html): Package:Â com.amazonaws.services.glue.types
- [FillMissingValues](https://docs.aws.amazon.com/glue/latest/dg/glue-etl-scala-apis-glue-ml-fillmissingvalues.html): Package:Â com.amazonaws.services.glue.ml
- [FindMatches](https://docs.aws.amazon.com/glue/latest/dg/glue-etl-scala-apis-glue-ml-findmatches.html): Package:Â com.amazonaws.services.glue.ml
- [FindIncrementalMatches](https://docs.aws.amazon.com/glue/latest/dg/glue-etl-scala-apis-glue-ml-findincrementalmatches.html): Package:Â com.amazonaws.services.glue.ml
- [IntegerNode](https://docs.aws.amazon.com/glue/latest/dg/glue-etl-scala-apis-glue-types-integernode.html): Package:Â com.amazonaws.services.glue.types
- [LongNode](https://docs.aws.amazon.com/glue/latest/dg/glue-etl-scala-apis-glue-types-longnode.html): Package:Â com.amazonaws.services.glue.types
- [MapLikeNode](https://docs.aws.amazon.com/glue/latest/dg/glue-etl-scala-apis-glue-types-maplikenode.html): Package:Â com.amazonaws.services.glue.types
- [MapNode](https://docs.aws.amazon.com/glue/latest/dg/glue-etl-scala-apis-glue-types-mapnode.html): Package:Â com.amazonaws.services.glue.types
- [NullNode](https://docs.aws.amazon.com/glue/latest/dg/glue-etl-scala-apis-glue-types-nullnode.html)
- [ObjectNode](https://docs.aws.amazon.com/glue/latest/dg/glue-etl-scala-apis-glue-types-objectnode.html)
- [ScalarNode](https://docs.aws.amazon.com/glue/latest/dg/glue-etl-scala-apis-glue-types-scalarnode.html)
- [ShortNode](https://docs.aws.amazon.com/glue/latest/dg/glue-etl-scala-apis-glue-types-shortnode.html): Package:Â com.amazonaws.services.glue.types
- [StringNode](https://docs.aws.amazon.com/glue/latest/dg/glue-etl-scala-apis-glue-types-stringnode.html): Package:Â com.amazonaws.services.glue.types
- [TimestampNode](https://docs.aws.amazon.com/glue/latest/dg/glue-etl-scala-apis-glue-types-timestampnode.html): Package:Â com.amazonaws.services.glue.types
- [GlueArgParser](https://docs.aws.amazon.com/glue/latest/dg/glue-etl-scala-apis-glue-util-glueargparser.html): Package:Â com.amazonaws.services.glue.util
- [Job](https://docs.aws.amazon.com/glue/latest/dg/glue-etl-scala-apis-glue-util-job.html): Package:Â com.amazonaws.services.glue.util

### [Features and optimizations](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-general.html)

Information about features and optimizations that you use when programming with AWS Glue for Spark ETL scripts.

### [Connection parameters](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-connect.html)

Use these settings for "connectionType" and "connectionOptions" parameters in ETL scripts.

### [DynamoDB connections](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-connect-dynamodb-home.html)

You can use AWS Glue for Spark to read from and write to tables in DynamoDB in AWS Glue.

- [Cross-account cross-Region access to DynamoDB tables](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-dynamo-db-cross-account.html): Cross-Account Cross-Region Access to DynamoDB Tables.
- [DynamoDB connector with Spark DataFrame support](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-connect-dynamodb-dataframe-support.html): DynamoDB connector with Spark DataFrame support allows you to read from and write to tables in DynamoDB using Spark DataFrame APIs.

### [Kinesis connections](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-connect-kinesis-home.html)

You can use a Kinesis connection to read and write to Amazon Kinesis data streams using information stored in a Data Catalog table, or by providing information to directly access the data stream.

- [Using enhanced fan-out in Kinesis streaming jobs](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-connect-kinesis-efo.html): An enhanced fan-out consumer is able to recieve records from a Kinesis stream with dedicated throughput that can be greater than typical consumers.

### [Amazon S3 connections](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-connect-s3-home.html)

You can use AWS Glue for Spark to read and write files in Amazon S3.

- [Excluding Amazon S3 storage classes](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-storage-classes.html): Exclude Amazon S3 storage classes while reading files or partitions from Amazon S3 in an AWS Glue ETL job.
- [Managing partitions](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-partitions.html): Settings available for managing partitions in ETL programming.
- [Grouping input files](https://docs.aws.amazon.com/glue/latest/dg/grouping-input-files.html): Learn about how to set table properties or create a dynamic frame which groups input files when read.
- [Amazon VPC endpoints for Amazon S3](https://docs.aws.amazon.com/glue/latest/dg/vpc-endpoints-s3.html): Amazon VPC endpoints for Amazon S3
- [Amazon DocumentDB connections](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-connect-documentdb-home.html): You can use AWS Glue for Spark to read from and write to tables in Amazon DocumentDB.
- [OpenSearch Service connections](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-connect-opensearch-home.html): You can use AWS Glue for Spark to read from and write to tables in OpenSearch Service in AWS Glue 4.0 and later versions.
- [Redshift connections](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-connect-redshift-home.html): You can use AWS Glue for Spark to read from and write to tables in Amazon Redshift databases.
- [Kafka connections](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-connect-kafka-home.html): You can use a Kafka connection to read and write to Kafka data streams using information stored in a Data Catalog table, or by providing information to directly access the data stream.
- [Azure Cosmos DB connections](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-connect-azurecosmos-home.html): You can use AWS Glue for Spark to read from and write to existing containers in Azure Cosmos DB using the NoSQL API in AWS Glue 4.0 and later versions.
- [Azure SQL connections](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-connect-azuresql-home.html): You can use AWS Glue for Spark to read from and write to tables on Azure SQL Managed Instances in AWS Glue 4.0 and later versions.
- [BigQuery connections](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-connect-bigquery-home.html): You can use AWS Glue for Spark to read from and write to tables in Google BigQuery in AWS Glue 4.0 and later versions.

### [JDBC connections](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-connect-jdbc-home.html)

Certain, typically relational, database types support connecting through the JDBC standard.

- [Reading from JDBC in parallel](https://docs.aws.amazon.com/glue/latest/dg/run-jdbc-parallel-read-job.html): Set table properties for a JDBC table to read partitioned data in parallel in AWS Glue.
- [Setting up Amazon VPC to connect to Amazon RDS data stores](https://docs.aws.amazon.com/glue/latest/dg/setup-vpc-for-glue-access.html): Walk through the process of setting up your VPC to allow AWS Glue access Amazon RDS data stores.
- [MongoDB connections](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-connect-mongodb-home.html): You can use AWS Glue for Spark to read from and write to tables in MongoDB and MongoDB Atlas in AWS Glue 4.0 and later versions.
- [SAP HANA connections](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-connect-saphana-home.html): You can use AWS Glue for Spark to read from and write to tables in SAP HANA in AWS Glue 4.0 and later versions.
- [Snowflake connections](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-connect-snowflake-home.html): You can use AWS Glue for Spark to read from and write to tables in Snowflake in AWS Glue 4.0 and later versions.
- [Teradata Vantage connections](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-connect-teradata-home.html): You can use AWS Glue for Spark to read from and write to existing tables in Teradata Vantage in AWS Glue 4.0 and later versions.
- [Teradata NOS connections](https://docs.aws.amazon.com/glue/latest/dg/connecting-to-data-teradata-nos.html): Teradata NOS (Native Object Store) connection is a new connection for Teradata Vantage which leverages Teradata WRITE_NOS query to read from existing tables and READ_NOS query to write to tables.
- [Vertica connections](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-connect-vertica-home.html): You can use AWS Glue for Spark to read from and write to tables in Vertica in AWS Glue 4.0 and later versions.

### [Data format options](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-format.html)

Settings available for 'format' and 'format_options' parameters.

- [CSV](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-format-csv-home.html): Describes the settings available for interacting with data in the CSV format in AWS Glue.
- [Parquet](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-format-parquet-home.html): Describes the settings available for interacting with data in the Parquet format in AWS Glue.
- [XML](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-format-xml-home.html): Describes the settings available for interacting with data in the XML format in AWS Glue.
- [Avro](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-format-avro-home.html): Describes the settings available for interacting with data in the Avro format in AWS Glue.
- [grokLog](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-format-grokLog-home.html): Describes the settings available for interacting with data in the grokLog format in AWS Glue.
- [Ion](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-format-ion-home.html): Describes the settings available for interacting with data in the Ion format in AWS Glue.
- [JSON](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-format-json-home.html): Describes the settings available for interacting with data in the JSON format in AWS Glue.
- [ORC](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-format-orc-home.html): Describes the settings available for interacting with data in the ORC format in AWS Glue.

### [Data lake frameworks](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-datalake-native-frameworks.html)

This page provides an overview of AWS Glue support for data lake frameworks such as Apache Hudi, Linux Foundation Delta Lake, and Apache Iceberg.

- [Limitations](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-datalake-native-frameworks-limitations.html): This topic covers limitations and known issues for AWS Glue support for Apache Hudi, Linux Foundation Delta Lake, and Apache Iceberg.
- [Hudi](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-format-hudi.html): Describes the settings available for interacting with data using the Hudi framework in AWS Glue.
- [Delta Lake](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-format-delta-lake.html): Describes the settings available for interacting with data using the Delta Lake framework in AWS Glue.
- [Iceberg](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-format-iceberg.html): Describes the settings available for interacting with data using the Iceberg framework in AWS Glue.
- [Data Catalog support for Spark SQL jobs](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-glue-data-catalog-hive.html): Configure your jobs and development endpoints to run Spark SQL queries directly against tables stored in the AWS Glue Data Catalog.
- [Using job bookmarks](https://docs.aws.amazon.com/glue/latest/dg/programming-etl-connect-bookmarks.html): AWS Glue for Spark uses job bookmarks to track data that has already been processed.

### [Sensitive data detection outside AWS Glue Studio](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-sensitive-data-example.html)

API Reference for AWS Glue Sensitive Data Detection.

- [Managed Sensitive Data Types](https://docs.aws.amazon.com/glue/latest/dg/sensitive-data-managed-data-types.html): Global entities
- [Using fine-grained sensitive data detection](https://docs.aws.amazon.com/glue/latest/dg/sensitive-data-fine-grained-actions.html): Fine-grained sensitive data detection provides the ability to apply specific actions per entity to detect, mask, or remove entities that you define or are pre-defined by AWS Glue as sensitive data.
- [AWS Glue Visual Job API](https://docs.aws.amazon.com/glue/latest/dg/visual-job-api-chapter.html): AWS Glue provides an API that allows customers to create data integration jobs using the AWS Glue API from a JSON object that represents a visual step workflow.

### [AWS Glue for Ray](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-ray.html)

How to program Ray scripts using AWS Glue.

- [Tutorial: Writing a Ray script](https://docs.aws.amazon.com/glue/latest/dg/edit-script-ray-intro-tutorial.html): Learn how to define and edit an extract, transform, and load (ETL) script in AWS Glue for Ray.
- [Using Ray Core and Ray Data in AWS Glue for Ray](https://docs.aws.amazon.com/glue/latest/dg/edit-script-ray-scripting.html): Describes core principles that you use in writing a Ray script.
- [Providing files and Python libraries](https://docs.aws.amazon.com/glue/latest/dg/edit-script-ray-env-dependencies.html): Describes how to provide files and Python libraries to Ray jobs.
- [Connecting to data](https://docs.aws.amazon.com/glue/latest/dg/edit-script-ray-connections-formats.html): Describes how to connect to data in AWS Glue Ray jobs.


## [AWS Glue API](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api.html)

- [Security](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-jobs-security.html): This section describes the AWS Glue API related to Security.

### [Catalog objects](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog.html)

API Reference for the AWS Glue Data Catalog.

- [Catalogs](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-catalogs.html): This section describes the catalog APIs.
- [Databases](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-databases.html): This section describes database data types, along with the API for creating, deleting, locating, updating, and listing databases.
- [Tables](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-tables.html): This section describes data types and operations associated with tables.
- [Partitions](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-partitions.html): This section describes data types and operations used to work with partitions.

### [Connections](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-connections.html)

API Reference for the AWS Glue Data Catalog.

- [Connections](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-connections-connections.html): This section describes AWS Glue connection data types, along with the API for creating, deleting, updating, and listing connections.
- [Connection types](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-connections-connections-type.html): This section describes APIs related to describing connection data types
- [Connection metadata](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-connections-connections-metadata.html): This section describes connection metadata and preview APIs.
- [User-defined Functions](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-functions.html): This section describes AWS Glue data types and operations used in working with functions.
- [Importing an Athena catalog](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-migration.html): This section describes AWS Glue data types and operations having to do with migrating a Hive catalog to AWS Glue.
- [Table optimizer](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-table-optimizers.html): This section describes the AWS Glue table optimizer API for enabling compaction to improve read performance.

### [Crawlers and classifiers](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler.html)

API Reference for AWS Glue crawlers, classifiers, and script generation.

- [Classifiers](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-classifiers.html): This section describes AWS Glue classifier data types, along with the API for creating, deleting, updating, and listing classifiers.
- [Crawlers](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-crawling.html): This section describes AWS Glue crawler data types, along with the API for creating, deleting, updating, and listing crawlers.
- [Column statistics](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-column-statistics.html): This section describes AWS Glue APIs for returning statistics on columns in a table.
- [Scheduler](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-crawler-scheduler.html): This section describes the AWS Glue crawler-scheduler API.
- [Autogenerating ETL Scripts](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-etl-script-generation.html): This section describes the AWS Glue ETL script-generation API.
- [Visual job API](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-visual-job-api.html): This section describes the AWS Glue API related to creating data integration jobs via API where the job script is automatically generated from a visual configuration of a AWS Glue job (also known as a DAG).

### [Jobs](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-jobs.html)

API Reference for AWS Glue Jobs.

- [Jobs](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-jobs-job.html): This section describes the AWS Glue API related to creating, updating, deleting, or viewing jobs in AWS Glue.
- [Job runs](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-jobs-runs.html): This section describes the AWS Glue API related to Job runs.
- [Triggers](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-jobs-trigger.html): This section describes the AWS Glue API related to Job triggers.
- [Integration APIs](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-integrations.html): This section describes the use of Zero-ETL integrations in AWS.
- [Interactive sessions](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-interactive-sessions.html): This section describes the AWS Glue API related to AWS Glue interactive sessions.
- [DevEndpoints](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-dev-endpoint.html): This section describes the AWS Glue API related to testing using a custom DevEndpoint.
- [Schema registry](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-schema-registry-api.html): This section describes the AWS Glue API related to Schema registry.
- [Workflows](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-workflow.html): This section describes the AWS Glue API related to Workflows.
- [Usage profiles](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-usage-profiles.html): This section describes the AWS Glue API related to AWS Glue usage profiles.
- [Machine learning](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-machine-learning-api.html): This section describes the API related to machine learning.
- [Data Quality](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-data-quality-api.html): This section describes the API related to Data Quality.
- [Sensitive Data](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-sensitive-data-api.html): This section describes the API related to sensitive data detection.
- [Tagging APIs](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-tags.html): This section describes the use of AWS tags.
- [Common data types](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-common.html): This section describes miscellaneous common data types.
- [Exceptions](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-exceptions.html): This section describes AWS Glue exceptions.


## [AWS Glue API code examples](https://docs.aws.amazon.com/glue/latest/dg/service_code_examples.html)

### [Basics](https://docs.aws.amazon.com/glue/latest/dg/service_code_examples_basics.html)

The following code examples show how to use the basics of AWS Glue with AWS SDKs.

- [Hello AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/example_glue_Hello_section.html): Hello AWS Glue
- [Learn the basics](https://docs.aws.amazon.com/glue/latest/dg/example_glue_Scenario_GetStartedCrawlersJobs_section.html): Learn the basics of AWS Glue with an AWS SDK

### [Actions](https://docs.aws.amazon.com/glue/latest/dg/service_code_examples_actions.html)

The following code examples show how to use AWS Glue with AWS SDKs.

- [CreateCrawler](https://docs.aws.amazon.com/glue/latest/dg/example_glue_CreateCrawler_section.html): Use CreateCrawler with an AWS SDK
- [CreateJob](https://docs.aws.amazon.com/glue/latest/dg/example_glue_CreateJob_section.html): Use CreateJob with an AWS SDK or CLI
- [DeleteCrawler](https://docs.aws.amazon.com/glue/latest/dg/example_glue_DeleteCrawler_section.html): Use DeleteCrawler with an AWS SDK
- [DeleteDatabase](https://docs.aws.amazon.com/glue/latest/dg/example_glue_DeleteDatabase_section.html): Use DeleteDatabase with an AWS SDK
- [DeleteJob](https://docs.aws.amazon.com/glue/latest/dg/example_glue_DeleteJob_section.html): Use DeleteJob with an AWS SDK or CLI
- [DeleteTable](https://docs.aws.amazon.com/glue/latest/dg/example_glue_DeleteTable_section.html): Use DeleteTable with an AWS SDK
- [GetCrawler](https://docs.aws.amazon.com/glue/latest/dg/example_glue_GetCrawler_section.html): Use GetCrawler with an AWS SDK
- [GetDatabase](https://docs.aws.amazon.com/glue/latest/dg/example_glue_GetDatabase_section.html): Use GetDatabase with an AWS SDK
- [GetDatabases](https://docs.aws.amazon.com/glue/latest/dg/example_glue_GetDatabases_section.html): Use GetDatabases with an AWS SDK or CLI
- [GetJob](https://docs.aws.amazon.com/glue/latest/dg/example_glue_GetJob_section.html): Use GetJob with an AWS SDK or CLI
- [GetJobRun](https://docs.aws.amazon.com/glue/latest/dg/example_glue_GetJobRun_section.html): Use GetJobRun with an AWS SDK or CLI
- [GetJobRuns](https://docs.aws.amazon.com/glue/latest/dg/example_glue_GetJobRuns_section.html): Use GetJobRuns with an AWS SDK or CLI
- [GetTables](https://docs.aws.amazon.com/glue/latest/dg/example_glue_GetTables_section.html): Use GetTables with an AWS SDK or CLI
- [ListJobs](https://docs.aws.amazon.com/glue/latest/dg/example_glue_ListJobs_section.html): Use ListJobs with an AWS SDK
- [StartCrawler](https://docs.aws.amazon.com/glue/latest/dg/example_glue_StartCrawler_section.html): Use StartCrawler with an AWS SDK or CLI
- [StartJobRun](https://docs.aws.amazon.com/glue/latest/dg/example_glue_StartJobRun_section.html): Use StartJobRun with an AWS SDK or CLI


## [Security](https://docs.aws.amazon.com/glue/latest/dg/security.html)

### [Data protection](https://docs.aws.amazon.com/glue/latest/dg/data-protection.html)

Learn about in-flight and at-rest encryption in AWS Glue.

### [Encrypting data at rest](https://docs.aws.amazon.com/glue/latest/dg/encryption-at-rest.html)

Configure ETL jobs and endpoints in AWS Glue to use KMS keys to write encrypted data at rest.

- [Encrypting your Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/encrypt-glue-data-catalog.html): Encrypt your AWS Glue Data Catalog using the AWS Glue console or the AWS CLI.
- [Encrypting connection passwords](https://docs.aws.amazon.com/glue/latest/dg/encrypt-connection-passwords.html): Choose to encrypt passwords for connections stored in the Data Catalog.

### [Encrypting data written by AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/encryption-security-configuration.html)

Create security configurations to encrypt at-rest data written by crawlers, jobs, and development endpoints in AWS Glue.

- [Managing security configurations on the AWS Glue console](https://docs.aws.amazon.com/glue/latest/dg/console-security-configurations.html): Create security configurations on the AWS Glue console to provide the encryption properties used by crawlers, jobs, and development endpoints.
- [Encrypting data in transit](https://docs.aws.amazon.com/glue/latest/dg/encryption-in-transit.html): Use Transport Layer Security (TLS) to encrypt data in transit in AWS Glue.
- [FIPS compliance](https://docs.aws.amazon.com/glue/latest/dg/fips-compliance.html): If you require FIPS 140-2 validated cryptographic modules when accessing AWS through a command line interface or an API, use a FIPS endpoint.
- [Key management](https://docs.aws.amazon.com/glue/latest/dg/key-management.html): Learn about key management in AWS Glue using both resource-based and identity-based policies.
- [AWS Glue dependency on other AWS services](https://docs.aws.amazon.com/glue/latest/dg/dependency-on-other-services.html): Permissions needed from other AWS services in AWS Glue.
- [Development endpoints](https://docs.aws.amazon.com/glue/latest/dg/dev-endpoints.html): Use development endpoints to develop and test your AWS Glue scripts.

### [Identity and access management](https://docs.aws.amazon.com/glue/latest/dg/security-iam.html)

Describes how to authenticate requests and manage access to your AWS Glue resources.

- [How AWS Glue works with IAM](https://docs.aws.amazon.com/glue/latest/dg/security_iam_service-with-iam.html): This section provides an overview of how AWS Glue works with IAM.

### [Configuring IAM permissions for AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/configure-iam-for-glue.html)

Walk through the process of configuring access permissions for AWS Glue.

- [Step 1: Create an IAM policy for the AWS Glue service](https://docs.aws.amazon.com/glue/latest/dg/create-service-policy.html): Walk through the process of creating an AWS Glue service policy.
- [Step 2: Create an IAM role for AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/create-an-iam-role.html): Walk through the process of creating a sample IAM role for AWS Glue.
- [Step 3: Attach a policy to users or groups that access AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/attach-policy-iam-user.html): Walk through the process of attaching a policy for the AWS Glue console to a user, group, or role.
- [Step 4: Create an IAM policy for notebook servers](https://docs.aws.amazon.com/glue/latest/dg/create-notebook-policy.html): Walk through the process of creating a notebook IAM policy.
- [Step 5: Create an IAM role for notebook servers](https://docs.aws.amazon.com/glue/latest/dg/create-an-iam-role-notebook.html): Walk through the process of creating a sample IAM role.
- [Step 6: Create an IAM policy for SageMaker AI notebooks](https://docs.aws.amazon.com/glue/latest/dg/create-sagemaker-notebook-policy.html): Walk through the process of creating a notebook IAM policy for using SageMaker AI notebooks with development endpoints in AWS Glue.
- [Step 7: Create an IAM role for SageMaker AI notebooks](https://docs.aws.amazon.com/glue/latest/dg/create-an-iam-role-sagemaker-notebook.html): Walk through the process of creating a sample IAM role for an SageMaker AI notebook in AWS Glue.

### [AWS Glue access control policy examples](https://docs.aws.amazon.com/glue/latest/dg/glue-policy-examples.html)

Examples of AWS Glue access control policies.

- [Identity-based policy examples](https://docs.aws.amazon.com/glue/latest/dg/security_iam_id-based-policy-examples.html): This section contains example identity-based IAM policies for AWS Glue.
- [Resource-based policy examples](https://docs.aws.amazon.com/glue/latest/dg/security_iam_resource-based-policy-examples.html): This section contains example resource-based IAM policies for AWS Glue.
- [Granting AWS managed policies](https://docs.aws.amazon.com/glue/latest/dg/security-iam-awsmanpol.html): Learn about AWS managed policies for AWS Glue and recent changes to those policies.
- [Granting dynamically scoped policies](https://docs.aws.amazon.com/glue/latest/dg/dynamically-scoped-policies.html): This section contains information about dynamically specifying custom session policy for each job execution.
- [Specifying AWS Glue Resource ARNs](https://docs.aws.amazon.com/glue/latest/dg/glue-specifying-resource-arns.html): How to specify AWS Glue ARNs in access-control policies.
- [Granting cross-account access](https://docs.aws.amazon.com/glue/latest/dg/cross-account-access.html): This section contains information to help you grant access to Data Catalog resources across different AWS accounts so that your ETL jobs can query and join data from different accounts.
- [Troubleshooting](https://docs.aws.amazon.com/glue/latest/dg/security_iam_troubleshoot.html): This topic provides information to help you troubleshoot identity and access for AWS Glue.

### [AWS Lake Formation access control models](https://docs.aws.amazon.com/glue/latest/dg/lake-formation-access-control-models.html)

AWS Glue 5.0 and above supports two models for accessing data through AWS Lake Formation:

- [Using AWS Glue with AWS Lake Formation for Full Table Access](https://docs.aws.amazon.com/glue/latest/dg/security-access-control-fta.html)

### [Lake Formation for FGAC](https://docs.aws.amazon.com/glue/latest/dg/security-lf-enable.html)

You can use Lake Formation with AWS Glue to apply fine grained access controls on Data Catalog tables.

- [Migrating from GlueContext/Glue DynamicFrame to Spark DataFrame](https://docs.aws.amazon.com/glue/latest/dg/security-lf-migration-spark-dataframes.html): The following are Python and Scala examples of migrating GlueContext/Glue DynamicFrame in Glue 4.0 to Spark DataFrame in Glue 5.0.
- [Considerations](https://docs.aws.amazon.com/glue/latest/dg/security-lf-enable-considerations.html): Consider the following considerations and limitations when you use Lake Formation with AWS Glue.
- [Troubleshooting](https://docs.aws.amazon.com/glue/latest/dg/security-lf-troubleshooting.html): See the following sections for troubleshooting solutions.
- [Using Amazon S3 Access Grants with AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/security-s3-access-grants.html): Using Amazon S3 Access Grants with AWS Glue

### [Trusted Identity Propagation](https://docs.aws.amazon.com/glue/latest/dg/security-trusted-identity-propagation.html)

Use IAM Identity Center to propagate user identities from AWS Glue interactive sessions to downstream AWS services for secure data access.

- [Getting started with trusted identity propagation in AWS Glue ETL](https://docs.aws.amazon.com/glue/latest/dg/security-trusted-identity-propagation-getting-started.html): This section helps you configure AWS Glue application with interactive sessions to integrate with IAM Identity Center and enable Trusted identity propagation.
- [Considerations and limitations for AWS Glue ETL Trusted Identity Propagation integration](https://docs.aws.amazon.com/glue/latest/dg/security-trusted-identity-propagation-considerations.html)
- [User background sessions](https://docs.aws.amazon.com/glue/latest/dg/user-background-sessions.html): Enable long-running analytics and machine learning workloads to continue even after users have logged off from their notebook interface through AWS Glue's trusted identity propagation feature.
- [Logging and monitoring](https://docs.aws.amazon.com/glue/latest/dg/logging-and-monitoring.html): Learn about logging and monitoring jobs and crawlers in AWS Glue.
- [Compliance validation](https://docs.aws.amazon.com/glue/latest/dg/compliance.html): Learn what AWS services are in scope of a specific compliance program.
- [Resilience](https://docs.aws.amazon.com/glue/latest/dg/disaster-recovery-resiliency.html): Learn how AWS architecture supports data redundancy, and learn about specific AWS Glue features for data resiliency.

### [Infrastructure security](https://docs.aws.amazon.com/glue/latest/dg/infrastructure-security.html)

Learn how AWS Glue isolates service traffic.

- [Configuring interface VPC endpoints (AWS PrivateLink) for AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/vpc-interface-endpoints.html): You can use an interface VPC endpoint to create a private connection between your VPC and AWS Glue without requiring access over the internet or through a NAT device, a VPN connection, or an Direct Connect connection.
- [Configuring shared Amazon VPCs](https://docs.aws.amazon.com/glue/latest/dg/shared-vpc.html): AWS Glue supports shared virtual private clouds (VPCs) in Amazon Virtual Private Cloud.


## [Troubleshooting AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/troubleshooting-glue.html)

- [Gathering AWS Glue troubleshooting information](https://docs.aws.amazon.com/glue/latest/dg/troubleshooting-contact-support.html): Gather information about your error when you contact Support.
- [Troubleshooting Glue common setup errors](https://docs.aws.amazon.com/glue/latest/dg/glue-troubleshooting-errors.html): How to find the source of errors and fix them in AWS Glue for Spark.
- [Crawler errors when the crawler is using Lake Formation permissions](https://docs.aws.amazon.com/glue/latest/dg/error-crawler-config-lf.html): Common errors found when a crawler is using Lake Formation permissions.
- [Troubleshooting Ray errors](https://docs.aws.amazon.com/glue/latest/dg/troubleshooting-ray.html): Describes how to troubleshoot Ray jobs by inspecting logs.
- [AWS Glue machine learning exceptions](https://docs.aws.amazon.com/glue/latest/dg/exceptions-machine-learning.html): Describes HTTP error codes and strings for AWS Glue exceptions related to machine learning.
- [AWS Glue quotas](https://docs.aws.amazon.com/glue/latest/dg/troubleshooting-service-limits.html): Default service quotas for various objects in AWS Glue.


## [Improving AWS Glue performance](https://docs.aws.amazon.com/glue/latest/dg/performance.html)

- [Improving Spark performance](https://docs.aws.amazon.com/glue/latest/dg/tuning-aws-glue-for-apache-spark.html): In order to improve AWS Glue for Spark performance, you may consider updating certain performance related AWS Glue and Spark parameters.
- [Optimizing reads with pushdown](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-pushdown.html): Pushdown is an optimization technique that pushes logic about retrieving data closer to the source of your data.
- [Using auto scaling for AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/auto-scaling.html): Describes the Auto Scaling feature, which is in preview for AWS Glue.
- [Workload partitioning with bounded execution](https://docs.aws.amazon.com/glue/latest/dg/bounded-execution.html): Enable workload partitioning to configure the upper bounds on the dataset size or the number of files processed on ETL job runs.
